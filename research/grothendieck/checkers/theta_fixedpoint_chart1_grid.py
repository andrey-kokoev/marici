"""Retired unsupported Chart-1 grid candidate.

The former 174x276 factorization was inferred only from a requested total of
48,024 cells. A fresh MCP filesystem search found no durable source for that
geometry. Import or execution is refused so it cannot be mistaken for a
certificate.
"""

raise RuntimeError(
    "unsupported Chart-1 grid geometry: supply a source-derived cell cover"
)
