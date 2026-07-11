"""Minimal FastAPI application used as the immutable nightly seed."""

from fastapi import FastAPI

app = FastAPI(title="Collègue nightly fixture")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
