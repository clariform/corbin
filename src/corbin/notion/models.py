from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class NormalizedProperty(BaseModel):
    type: str
    value: Any | None = None
    ids: list[str] = Field(default_factory=list)


class NormalizedBlock(BaseModel):
    id: str | None = None
    type: str
    text: str | None = None
    language: str | None = None
    checked: bool | None = None
    children: list["NormalizedBlock"] = Field(default_factory=list)


class ParentRef(BaseModel):
    type: str | None = None
    id: str | None = None
    workspace: bool | None = None


class NormalizedPage(BaseModel):
    page_id: str
    title: str
    url: str | None = None
    created_time: str | None = None
    last_edited_time: str | None = None
    parent: ParentRef | dict[str, Any] | None = None
    archived: bool = False
    in_trash: bool = False
    properties: dict[str, NormalizedProperty] = Field(default_factory=dict)
    content: list[NormalizedBlock] = Field(default_factory=list)
    plain_text: str = ""
