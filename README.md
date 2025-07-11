# codif-ape-agentic-rag
A one-shot LLM-based (Embeddings, RAG) NACE classification module, with multi-agent cooperation and tool-calling to provide richer contextual grounding.

## Init a uv project

cd codif-ape-agentic-rag/
uv init --description "Hello world" --author-from git --vcs git --python-pin

If you want to add dependencies in your pyproject.toml:

```bash
uv add ag2
```
```bash
uv add openai
```
```bash
uv add mlflow
```
```bash
uv add s3fs
```

If you're nostalgic of requirements.txt you can still use it. It's not an anti-pattern but it's time to move on ! Here is the command line to help to understand/migrate:

```bash
uv add -r requirements.txt
```

If you want to remove dependencies:
```bash
uv remove ag2
```

Then install the dependencies using:

```bash
uv sync
```

To add pre-commit:

- first install pre-commit tool
```bash
uv tool install pre-commit --with pre-commit-uv
uv tool update-shell
source ~/.bashrc
```
- then install hooks
```bash
uv run pre-commit install
```
