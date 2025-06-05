# MMM-2 Streamlit App Deployment Guide

### by Asif Rasool, Ph.D.

This guide documents the step-by-step process for building, pushing, and deploying the MMM-2 Streamlit application (Dockerized) to Google Cloud Run. It also covers mounting secrets from Secret Manager and configuring the application to listen on the correct port.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Directory and File Overview](#directory-and-file-overview)
4. [Dockerfile Configuration](#dockerfile-configuration)

   - 4.1. Port Configuration for Cloud Run

5. [Building the Docker Image Locally](#building-the-docker-image-locally)
6. [Tagging and Pushing to Google Container Registry (GCR)](#tagging-and-pushing-to-google-container-registry-gcr)
7. [Deploying to Cloud Run](#deploying-to-cloud-run)

   - 7.1. Mounting Secrets from Secret Manager
   - 7.2. Deploy Command Explanation

8. [Verification and Testing](#verification-and-testing)
9. [Cleanup (Optional)](#cleanup-optional)
10. [Troubleshooting Tips](#troubleshooting-tips)
11. [Appendix: Example Docker Commands](#appendix-example-docker-commands)

---

## 1. Introduction

This guide is intended for developers and DevOps engineers who want to containerize a Streamlit app, push it to Google Container Registry (GCR), and deploy it on Google Cloud Run. The steps below assume you already have:

- A working Dockerfile for your Streamlit app.
- Two secrets stored in Secret Manager:

  - `livingston-parish-library-config`: contains the contents of `.streamlit/config.toml`.
  - `southeastern-lions-ide-secrets`: contains the contents of `.streamlit/secrets.toml`.

- A GCP project (in this case, `eia-livingston-southeastern`).

By the end of this guide, you will have a fully operational MMM-2 Streamlit app running on Cloud Run, with secrets securely mounted and the correct port configuration.

---

## 2. Prerequisites

1. **Google Cloud SDK installed and authenticated**

   ```bash
   gcloud auth login
   gcloud config set project eia-livingston-southeastern
   ```

2. **Docker installed**
3. **Secrets stored in Secret Manager**

   - `livingston-parish-library-config`
   - `southeastern-lions-ide-secrets`

4. **Cloud Run, Secret Manager, and Container Registry APIs enabled**

   ```bash
   gcloud services enable run.googleapis.com \
       secretmanager.googleapis.com \
       containerregistry.googleapis.com \
       cloudbuild.googleapis.com
   ```

5. **IAM Permissions**

   - Ensure the Cloud Run runtime service account (e.g., `PROJECT_NUMBER-compute@developer.gserviceaccount.com`) has the `Secret Manager Secret Accessor` role for both secrets.

---

## 3. Directory and File Overview

Below is an example of the `MMM-2` project root structure:

```
MMM-2/
├── .git/
├── .streamlit/
│   ├── config.toml        # Streamlit configuration (theme, icons, etc.)
│   └── secrets.toml       # Streamlit secrets (API keys, database credentials)
├── Data/
├── Figures/
├── Multipliers/
├── Outputs/
├── pages/                # Additional multipage scripts
├── .gitattributes
├── .gitignore
├── 0_Background.py       # Main Streamlit entrypoint
├── Dockerfile
├── LICENSE
├── main.ipynb
├── Procfile              # (Optional) for Heroku or similar
├── README.md
├── requirements.txt
└── runtime.txt            # Python version specifiers
```

Key files:

- \`\`: Defines how to containerize the Streamlit application.
- \`\`: Lists all Python dependencies, including pinned versions of `langchain` and `langchain-google-genai`.
- \`\`: Contains Streamlit UI settings (e.g., theme, favicon).
- \`\`: Contains sensitive information (e.g., API keys). We will mount this from Secret Manager in production.
- \`\`: The main Streamlit script (entrypoint).

---

## 4. Dockerfile Configuration

Below is the canonical `Dockerfile` used for MMM-2. Note the use of the `PORT` environment variable to support both local testing (on port 8501) and Cloud Run (on port 8080).

```dockerfile
# Use Python 3.11 slim base image\ nFROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the entire project into /app
COPY . .

# Expose port 8080 for Cloud Run (documentation only)
EXPOSE 8080

# ENTRYPOINT uses PORT environment variable; fallback to 8501 if not set
ENTRYPOINT ["sh", "-c", "streamlit run 0_Background.py --server.port=${PORT:-8501} --server.address=0.0.0.0"]
```

### 4.1. Port Configuration for Cloud Run

- \`\`: When running locally, `PORT` is unset, so Streamlit defaults to port `8501`. When running on Cloud Run, the platform always sets `PORT=8080`, so Streamlit binds to port `8080` automatically.
- \`\`: While this line is not strictly required for Cloud Run, it documents the intended listening port.

---

## 5. Building the Docker Image Locally

From the `MMM-2` project root, run:

```bash
cd /path/to/MMM-2

docker build -t mmm-2-app:latest .
```

- \`\`: Tags the image as `mmm-2-app` with the `latest` tag.
- \`\`: Uses the current directory as the build context (it will include your `Dockerfile`, `.streamlit/`, and other files).

Once complete, verify by listing local images:

```bash
docker images | grep mmm-2-app
```

You should see something like:

```
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
mmm-2-app     latest    <image_id>     <time_ago>      <size>
```

Run the Container Locally

```
docker run --rm -p 8501:8501 southeastern-lionide-app:latest

```

Or,

if you want to test your image throgh live edit feature:

```
docker run --rm -p 8501:8501 ^
  -v "%cd%":/app ^
  southeastern-lionide-light-app:latest
```

View the image in the browser:

```
http://localhost:8501

```

---

## 6. Tagging and Pushing to Google Container Registry (GCR)

1. **Tag the local image** for GCR:

   ```bash
   docker tag southeastern-lionide-app:latest gcr.io/eia-livingston-southeastern/southeastern-lionide-app:v1
   ```

2. **Authenticate Docker with GCR**:

   ```bash
   gcloud auth configure-docker
   ```

3. **Push the tagged image**:

   ```bash
   docker push gcr.io/eia-livingston-southeastern/southeastern-lionide-app:v1
   ```

After pushing, the image is stored at:

```
gcr.io/eia-livingston-southeastern/mmm-2-app:v1
```

---

## 7. Deploying to Cloud Run

Once your image is in GCR, deploy it to Cloud Run while mounting your Secret Manager secrets.

### 7.1. Mounting Secrets from Secret Manager

We have two secrets:

- \`\` → to be mounted as `/workspace/.streamlit/config.toml`
- \`\` → to be mounted as `/home/cnb/.streamlit/secrets.toml`

Use the `--update-secrets` flag to map each secret to a file path inside the container.

### 7.2. Deploy Command Explanation

Run the following command from your local environment (Anaconda Prompt or terminal):

```bash
gcloud run deploy southeastern-lionide ^
  --image gcr.io/eia-livingston-southeastern/southeastern-lionide-app:v1 ^
  --region us-central1 ^
  --platform managed ^
  --allow-unauthenticated ^
  --update-secrets=/workspace/.streamlit/config.toml=southeastern-lions-ide-config:latest ^
  --update-secrets=/home/cnb/.streamlit/secrets.toml=southeastern-lions-ide-secrets:latest
```

- `mmm-2-app`: Name of the Cloud Run service.
- `--image gcr.io/eia-livingston-southeastern/mmm-2-app:v1`: Uses your pushed image.
- `--region us-central1`: Deploys in the `us-central1` region (adjust if desired).
- `--platform managed`: Uses Cloud Run (fully managed).
- `--allow-unauthenticated`: Makes the service publicly accessible. Omit if you want to restrict access.
- `--update-secrets=/workspace/.streamlit/config.toml=livingston-parish-library-config:latest`: Mounts the secret as a file at `/workspace/.streamlit/config.toml`.
- `--update-secrets=/home/cnb/.streamlit/secrets.toml=southeastern-lions-ide-secrets:latest`: Mounts the secret as a file at `/home/cnb/.streamlit/secrets.toml`.

**What happens under the hood**:

1. Cloud Run spins up a new revision of `mmm-2-app` using the specified image.
2. At runtime, the contents of the Secret Manager secrets (`latest` versions) are projected into the container file system at the given paths.
3. Streamlit automatically reads `/workspace/.streamlit/config.toml` for UI config and `/home/cnb/.streamlit/secrets.toml` for `st.secrets`.
4. Cloud Run sets `PORT=8080` in the container’s environment. Our Dockerfile’s `ENTRYPOINT` reads `${PORT:-8501}`, so Streamlit binds to port 8080.

Once the command completes, you’ll see a message similar to:

```
Service [mmm-2-app] revision [mmm-2-app-00001-abc] has been deployed and is serving 100% of traffic.
Service URL: https://mmm-2-app-xyz-uc.a.run.app
```

Copy the **Service URL** and open it in your browser.

---

## 8. Verification and Testing

1. **Open the Service URL** in your browser. The app should load as expected with all pages (including those in `pages/`).
2. **Check Cloud Run logs** to confirm secrets were mounted:

   1. In the GCP Console, navigate to **Cloud Run → mmm-2-app → Revisions**.
   2. Click the latest revision and go to the **Logs** tab.
   3. Look for lines such as:

      ```
      Using config file: /workspace/.streamlit/config.toml
      Using secrets file: /home/cnb/.streamlit/secrets.toml
      ```

3. **Test sensitive operations**:

   - If you rely on `st.secrets[...]` (e.g., API keys), add a temporary `st.write(st.secrets)` to one page to visually confirm the values.
   - Verify that any database connections or API calls using those secrets succeed.

---

## 9. Cleanup (Optional)

If you ever need to remove the Cloud Run service and/or delete the image from GCR:

1. **Delete the Cloud Run service**:

   ```bash
   gcloud run services delete mmm-2-app --region us-central1
   ```

2. **Remove the image from GCR**:

   ```bash
   gcloud container images delete gcr.io/eia-livingston-southeastern/mmm-2-app:v1
   ```

3. **Remove local Docker images** (on your dev machine):

   ```bash
   docker rmi mmm-2-app:latest
   docker rmi gcr.io/eia-livingston-southeastern/mmm-2-app:v1
   ```

---

## 10. Troubleshooting Tips

- **Container fails health checks (port errors)**

  - Ensure your `ENTRYPOINT` uses `${PORT:-8501}` so that Cloud Run’s `PORT=8080` is respected.
  - If you cannot modify the Dockerfile, deploy with `--port 8501` so Cloud Run knows to hit port 8501.

- **Secrets not found at runtime**

  - Verify that the Cloud Run runtime service account has the **Secret Manager Secret Accessor** role for each secret.
  - Check that your `--update-secrets` flags use the correct secret resource name (`projects/PROJECT_ID/secrets/SECRET_NAME:latest`).
  - Inspect Cloud Run logs for messages like “Using secrets file: /home/cnb/.streamlit/secrets.toml.”

- **Permission denied when reading secrets**

  - In Secret Manager → select the secret → “Show info panel” → “Permissions” → “Add member.”
  - Add `SERVICE_ACCOUNT_EMAIL` (e.g., `PROJECT_NUMBER-compute@developer.gserviceaccount.com`) with **Secret Manager Secret Accessor** role.

- **Different region or service name**

  - Adjust `--region` to your preferred region (e.g., `us-east1`, `europe-west1`).
  - If you need a different Cloud Run service name, replace `mmm-2-app` accordingly.

---

## 11. Appendix: Example Docker Commands

For quick reference, here are the core Docker commands used in this guide:

```bash
# Build the Docker image locally (tag as 'latest')
docker build -t mmm-2-app:latest .

# Tag for Container Registry
docker tag mmm-2-app:latest gcr.io/eia-livingston-southeastern/mmm-2-app:v1

# Authenticate Docker with GCR
gcloud auth configure-docker

# Push the image to GCR
docker push gcr.io/eia-livingston-southeastern/mmm-2-app:v1

# Save a local tarball of the image (optional)
docker save -o mmm-2-app-latest.tar mmm-2-app:latest

# Load the tarball back into Docker (optional)
docker load -i mmm-2-app-latest.tar

# List local Docker images
docker images | grep mmm-2-app

# Remove local Docker images
docker rmi mmm-2-app:latest
docker rmi gcr.io/eia-livingston-southeastern/mmm-2-app:v1
```

---

_This guide should serve as a single reference for future MMM-2 Streamlit app deployments. Keep it updated as your workflow or project structure evolves!_
