ARG PYTHON_IMAGE=python:3.13-slim
FROM ${PYTHON_IMAGE} AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        openssh-client \
        tmux \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md ./
COPY pocketclaw ./pocketclaw

FROM base AS runtime

RUN python -m pip install --upgrade pip \
    && python -m pip install .

ENV POCKETCLAW_HOST=0.0.0.0 \
    POCKETCLAW_PORT=8787 \
    POCKETCLAW_STORE=/data/profiles.json

VOLUME ["/data"]
EXPOSE 8787

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD python -c "import os, urllib.request; port=os.getenv('POCKETCLAW_PORT','8787'); token=os.getenv('POCKETCLAW_TOKEN',''); req=urllib.request.Request(f'http://127.0.0.1:{port}/api/health' + (f'?token={token}' if token else '')); urllib.request.urlopen(req, timeout=3)" || exit 1

CMD ["python", "-m", "pocketclaw", "serve"]

FROM base AS devcontainer

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
