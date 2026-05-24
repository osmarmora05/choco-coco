# Choco coco API

## Prerequisites

1. [uv](https://docs.astral.sh/uv/)
2. [docker](https://www.docker.com/)

## Run the project

1. Navigate to the project root directory:

```sh
  cd ../../
```

2. Create the `.env` file from the development template:

```sh
  cat .env.dev > .env
```

3. Install the dependences using :

```sh
  uv sync --all-packages --frozen
```

3. Start the Ollama server, then spin up the API.
   To optimize the developer experience (DX) and avoid rebuild delays, we only run the Ollama service via Docker. Running the entire Docker Compose setup would require rebuilding the image after every local API change. Note: Running this command will download and execute the models directly on your local machine.

```sh
  docker compose up ollama
  uv run apps/api/src/main.py
```
