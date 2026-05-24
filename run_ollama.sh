#!/bin/bash

ollama serve &

until ollama list > /dev/null 2>&1; do
      sleep 1
done

echo "Pulling model: qwen2.5:3b-instruct"
ollama pull qwen2.5:3b-instruct

echo "Pulling embebeder model: embeddinggemma:300m"
ollama pull embeddinggemma:300m

wait
