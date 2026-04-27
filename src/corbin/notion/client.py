from __future__ import annotations

import os
from typing import Any

import httpx

class NotionClient:
    def __init__(
        self,
        token: str | None = None,
        notion_version: str = "2026-03-11",
        timeout: float = 30.0,
    ) -> None:
        self.token = token or os.environ["NOTION_TOKEN"]
        self.notion_version = notion_version
        self.timeout = timeout
        self.base_url = "https://api.notion.com/v1"

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
        }

    def get_page(self, page_id: str) -> dict[str, Any]:
        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(
                f"{self.base_url}/pages/{page_id}",
                headers=self.headers,
            )
            response.raise_for_status()
            return response.json()

    def get_block_children(
        self,
        block_id: str,
        start_cursor: str | None = None,
        page_size: int = 100,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {"page_size": page_size}
        if start_cursor:
            params["start_cursor"] = start_cursor

        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(
                f"{self.base_url}/blocks/{block_id}/children",
                headers=self.headers,
                params=params,
            )
            response.raise_for_status()
            return response.json()
