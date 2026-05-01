# SmartField LA

Hugo project website for **SmartField LA: An End-to-End Deep Learning Framework for Real-Time Strawberry Disease Detection in Louisiana**, using the PaperMod theme.

The static site transfers the Streamlit app's informational pages into GitHub Pages:

- Home / Introduction
- Overview
- Objectives
- Methodology
- Data
- Web & Mobile
- References

The existing Streamlit, Docker, and Google Cloud deployment files are intentionally kept in this repository for now. Do not remove the deployed GCP web app until the GitHub Pages site is live and verified.

## Local Development

```powershell
git submodule update --init --recursive
hugo server
```

The site will be available at `http://localhost:1313/`.

## Production Build

```powershell
hugo --minify
```

## GitHub Pages

The repository includes a GitHub Actions workflow at `.github/workflows/hugo.yml`.

After pushing to GitHub:

1. Go to the repository settings.
2. Open **Pages**.
3. Set **Source** to **GitHub Actions**.

The live site will publish to:

`https://asif-rasool.github.io/Strawberry-Disease-Classifier/`
