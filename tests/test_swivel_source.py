from __future__ import annotations

import os
from pathlib import Path

import pytest

from corbin.sources.swivel import CorbinSwivelSource


DATABASE_ID = "c3c6411f-0654-43cf-83ea-708bfd9097a9"


@pytest.mark.skipif(
    "NOTION_API_KEY" not in os.environ,
    reason="NOTION_API_KEY is required for live Swivel source test",
)
def test_get_database_chunks_from_swivel() -> None:
    source = CorbinSwivelSource(
        use_cargo=True,
        swivel_project_root=Path.home()
        / "Library/CloudStorage/Dropbox/matrix/crates/swivel",
    )

    chunks = source.get_database_chunks(DATABASE_ID)

    assert len(chunks) > 0

    first = chunks[0]

    assert "chunk_id" in first
    assert "document_id" in first
    assert "source" in first
    assert "source_kind" in first
    assert "chunk_kind" in first
    assert "text" in first
