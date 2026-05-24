FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ARG API_PORT

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc=4:14* \
  binutils=2.4* \
  libc6-dev=2.41* \
  && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./
COPY .env ./

COPY libs/choco-coco-brain ./libs/choco-coco-brain
COPY libs/choco-coco-image-to-ascii ./libs/choco-coco-image-to-ascii

COPY apps/api ./apps/api

EXPOSE ${API_PORT}

RUN uv sync --all-packages --frozen

CMD ["uv", "run", "--package", "api", "python", "apps/api/src/main.py", "--log-level=DEBUG"]
