from __future__ import annotations

from pathlib import Path
from typing import Any

from swivelpy import (
    SwivelClient,
    SwivelConfig,
    SwivelEntryKind,
    SwivelEntryPoint,
    SwivelSource,
)


class CorbinSwivelSource:
    """
    Corbin source adapter for retrieving chunks from Swivel.

    Swivel handles:
    - Notion API access
    - source normalization
    - document generation
    - chunk generation

    Corbin handles:
    - tokenization
    - embeddings
    - vector database storage
    """

    def __init__(
        self,
        *,
        swivel_project_root: Path | None = None,
        use_cargo: bool = False,
        binary: str = "swivel",
    ) -> None:
        self.client = SwivelClient(
            SwivelConfig(
                binary=binary,
                use_cargo=use_cargo,
                project_root=swivel_project_root,
            )
        )

    def get_chunks(
        self,
        *,
        entry_id: str,
        kind: SwivelEntryKind,
    ) -> list[dict[str, Any]]:
        entry = SwivelEntryPoint(
            source=SwivelSource.NOTION,
            kind=kind,
            id=entry_id,
        )

        return self.client.retrieve_chunks(entry)

    def get_database_chunks(self, database_id: str) -> list[dict[str, Any]]:
        return self.get_chunks(
            entry_id=database_id,
            kind=SwivelEntryKind.DATABASE,
        )

    def get_data_source_chunks(self, data_source_id: str) -> list[dict[str, Any]]:
        return self.get_chunks(
            entry_id=data_source_id,
            kind=SwivelEntryKind.DATA_SOURCE,
        )

    def get_page_chunks(self, page_id: str) -> list[dict[str, Any]]:
        return self.get_chunks(
            entry_id=page_id,
            kind=SwivelEntryKind.PAGE,
        )
