from __future__ import annotations

from typing import Any

from corbin.notion.client import NotionClient


def fetch_block_tree(client: NotionClient, block_id: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    cursor: str | None = None

    while True:
        payload = client.get_block_children(block_id=block_id, start_cursor=cursor)

        for block in payload.get("results", []):
            block_copy = dict(block)

            if block.get("has_children", False):
                block_copy["children"] = fetch_block_tree(client=client, block_id=block["id"])

            results.append(block_copy)

        if not payload.get("has_more", False):
            break

        cursor = payload.get("next_cursor")

    return results
