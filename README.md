# Corbin

Corbin is the Python-side RAG indexing layer for Clariform.

At this stage, Corbin consumes already-normalized chunks from Swivel. Swivel handles source retrieval and chunk generation. Corbin is responsible for the next stage: tokenization, embeddings, and vector database storage.

Repository:

```text
https://github.com/clariform/corbin
```

Current release:

```text
v0.1.1
```

## Current scope

Corbin currently provides a source adapter for Swivel:

```text
Swivel chunks → Corbin ingestion path
```

The old direct Notion code has been removed or deprecated. Notion retrieval now belongs to Swivel.

## Project layout

```text
corbin
├── examples
│   └── retrieve_swivel_chunks.py
├── src
│   └── corbin
│       ├── sources
│       │   ├── __init__.py
│       │   └── swivel.py
│       ├── __init__.py
│       └── py.typed
├── tests
│   └── test_swivel_source.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Relationship to Swivel

Swivel owns:

```text
source retrieval → normalization → chunk generation
```

Corbin owns:

```text
chunks → tokenization → embeddings → vector database storage
```

This separation keeps Corbin source-agnostic. Corbin does not need to know how Notion works. It only needs clean chunk records.

## Requirements

Install the Swivel CLI:

```bash
cargo install swivelcli
```

Verify:

```bash
swivel --help
```

Install Python dependencies:

```bash
uv sync
```

Set Notion credentials for live Swivel-backed tests:

```bash
export NOTION_API_KEY="ntn_..."
export NOTION_VERSION="2026-03-11"
```

## Usage

```python
from corbin import CorbinSwivelSource

source = CorbinSwivelSource(
    binary="swivel",
    use_cargo=False,
)

chunks = source.get_database_chunks("your-database-id")

print(len(chunks))
print(chunks[0]["text"])
```

## Available source methods

```python
source.get_database_chunks(database_id)
source.get_data_source_chunks(data_source_id)
source.get_page_chunks(page_id)
```

All three methods return a list of Swivel chunk dictionaries.

## Example

Run:

```bash
uv run python examples/retrieve_swivel_chunks.py
```

Expected output includes:

```text
retrieved chunks: <count>
```

## Tests

Run:

```bash
uv run pytest
```

The live Swivel source test requires `NOTION_API_KEY`. If the environment variable is missing, the test is skipped.

## Development

Recommended local environment:

```bash
source ~/.venvs/corbin/bin/activate
uv sync
```

Run checks:

```bash
uv run pytest
uv run ruff check .
```

Optional type check:

```bash
uv run mypy src
```

## Packaging

Build:

```bash
uv build
```

Publish:

```bash
uv publish
```

## Status

Corbin is early and currently focused on consuming Swivel chunks. The next major step is to add tokenization, embedding generation, and vector database storage.
