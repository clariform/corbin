from __future__ import annotations

from pathlib import Path

from corbin.sources.swivel import CorbinSwivelSource


DATABASE_ID = "c3c6411f-0654-43cf-83ea-708bfd9097a9"


def main() -> None:
    source = CorbinSwivelSource(
        use_cargo=True,
        swivel_project_root=Path.home()
        / "Library/CloudStorage/Dropbox/matrix/crates/swivel",
    )

    chunks = source.get_database_chunks(DATABASE_ID)

    print(f"retrieved chunks: {len(chunks)}")

    for chunk in chunks[:5]:
        print()
        print("chunk_id:", chunk["chunk_id"])
        print("source_kind:", chunk["source_kind"])
        print("chunk_kind:", chunk["chunk_kind"])
        print("page_title:", chunk["page_title"])
        print("text preview:")
        print(chunk["text"][:500])


if __name__ == "__main__":
    main()
