# RH publication workspace

This workspace implements the internal drafting and release-control plan for task #2533.

## Current status

The manuscripts are internal drafts. They are not submission-ready and must not be represented as a proof of the Riemann hypothesis while any gate in `rh-proof-ledger.json` is open.

## Package layout

- `papers/rh-main/main.tex`: concise theorem-chain manuscript.
- `papers/rh-foundations/main.tex`: technical constructor and verification companion.
- `publication/rh-proof-ledger.json`: canonical claim and release-gate ledger.
- `publication/internal-arxiv-readiness-verdict.md`: current mathematical release decision and exact blockers.
- `publication/check_release.py`: mechanical preflight check.
- `publication/audit_reproducibility.py`: theorem dependency, evidence receipt,
  source-hygiene, and clean-build audit for G6.

## Release procedure

1. Close G1 through G4 with durable mathematical evidence.
2. Complete internal and external review under G5.
3. Build both manuscripts from a clean checkout and complete G6.
4. Freeze authorship, license, categories, and metadata.
5. Obtain explicit operator authorization under G7.
6. Only then create and externally upload the arXiv archives.

Authorship remains deliberately unresolved until the contribution audit. The planned package is a main paper plus a simultaneous technical companion.
