# Corbin

Corbin is a graph-aware retrieval system for Notion-backed technical knowledge bases.

It turns structured Notion content into a retrieval-ready mirror with documents, chunks, metadata, aliases, and typed relationships, then exposes that knowledge through an API that can power search, grounded answers, and ChatGPT tool use.

## Why Corbin

Most note systems are pleasant to write in but weak at retrieval once the knowledge base grows.
Corbin keeps Notion as the authoring layer and builds a retrieval layer that is deterministic, inspectable, and easy to evolve.

The goal is not generic semantic search alone. The goal is to answer questions using:

- chunk embeddings
- exact identifiers
- metadata filters
- typed relationships
- freshness and verification state
- provenance back to the source note

## Core idea

Corbin treats each Notion page as a source record that can become:

- a document
- one or more chunks
- one or more graph edges
- optional aliases and extracted entities

That makes it possible to combine semantic retrieval with structural expansion.
A chunk about a CUDA fix can lead to the host it applies to, the service it affects, and the playbook that verifies it.

## Architecture

Corbin is split into a few clear layers:

1. **Notion source layer**  
   Pull canonical databases, page metadata, and recursive block content.

2. **Sync and normalization layer**  
   Flatten Notion blocks into clean text, extract metadata, normalize relation properties, and compute content hashes.

3. **Indexing layer**  
   Chunk documents by structure, enrich chunks with compact headers, generate embeddings, and upsert into PostgreSQL with pgvector.

4. **Retrieval layer**  
   Run hybrid search across semantic similarity, full-text search, metadata filters, and graph expansion.

5. **Orchestration API**  
   Expose search and answer endpoints through FastAPI.

6. **Chat integration layer**  
   Present Corbin as tools through MCP so ChatGPT can call into the knowledge base directly.

## Planned stack

- Python 3.12
- FastAPI
- PostgreSQL
- pgvector
- SQLAlchemy
- Alembic
- Pydantic
- HTTPX
- Notion API
- uv
- Docker Compose
- MCP server for ChatGPT integration

## Retrieval model

Corbin is designed around hybrid retrieval rather than embedding-only search.
A query can be analyzed into intent, entities, and constraints, then resolved through several channels:

- semantic chunk search
- PostgreSQL full-text search
- exact and fuzzy alias matching
- metadata filters such as host, project, or status
- graph expansion from related nodes and edges

The final answer should prefer verified, host-specific, and current documentation whenever possible.

## Example use cases

- Find the exact playbook for rebuilding a service on a specific host.
- Explain how a component, machine, and script are related.
- Retrieve the most relevant troubleshooting note, then expand to nearby docs.
- Answer a question in ChatGPT using private internal knowledge instead of generic recall.
- Surface stale notes that need verification after infra changes.

## Initial project layout

```text
corbin/
├── pyproject.toml
├── README.md
├── .env.example
├── configs/
│   ├── app.yaml
│   ├── notion.yaml
│   ├── retrieval.yaml
│   └── chunking.yaml
├── src/
│   └── corbin/
│       ├── notion/
│       │   ├── client.py
│       │   ├── sync.py
│       │   ├── blocks.py
│       │   └── normalize.py
│       ├── indexing/
│       │   ├── chunker.py
│       │   ├── embed.py
│       │   ├── extract.py
│       │   └── upsert.py
│       ├── graph/
│       │   ├── entities.py
│       │   ├── relations.py
│       │   └── traversal.py
│       ├── retrieval/
│       │   ├── analyze.py
│       │   ├── hybrid.py
│       │   ├── rerank.py
│       │   └── answer.py
│       ├── db/
│       │   ├── models.py
│       │   ├── session.py
│       │   └── migrations/
│       ├── api/
│       │   └── main.py
│       └── app/
│           └── mcp_server.py
└── tests/
```

## First milestones

### Phase 1
Sync one or two Notion databases into PostgreSQL.

### Phase 2
Chunk content and add embeddings.

### Phase 3
Capture relation properties as graph edges.

### Phase 4
Expose retrieval through FastAPI.

### Phase 5
Connect ChatGPT through MCP tools.

## Design principles

- Notion stays the authoring layer.
- PostgreSQL is the retrieval mirror.
- Retrieval must be inspectable and testable.
- Chunking should follow structure before token count.
- Relations are first-class signals, not just metadata.
- Answers should always preserve provenance.

## Status

Early scaffold.
The first version focuses on reliable sync, clean normalization, and grounded retrieval before adding richer answer synthesis and write-back workflows.
