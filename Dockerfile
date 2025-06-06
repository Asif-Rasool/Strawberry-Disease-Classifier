FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# Tell Docker to expose the Cloud Run default (8080),
# but this is merely documentation: Cloud Run enforces PORT=8080 at runtime.
EXPOSE 8080

# Use the $PORT environment variable. If not set, default to 8501 for local testing.
ENTRYPOINT ["sh", "-c", "streamlit run 0_Introduction.py --server.port=${PORT:-8501} --server.address=0.0.0.0"]
