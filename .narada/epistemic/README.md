# Epistemic graph authority

This directory is Marici's tracked authority for evolving research problem
situations. `ledger/` contains immutable, hash-linked admitted events;
`proposals/` preserves submitted proposals and structural reviews.

The graph records problems, conjectures, criticisms, tests, versioned sources,
and attributed assessments. Admission means that a record satisfied the
surface's structural, provenance, evidence-location, reference, and concurrency
policy. It does not certify truth.

The SQLite projection beneath `.narada/.ai/epistemic-graph/` is ignored runtime
state and may be deleted and rebuilt from this ledger. External literature
search remains provider-owned. Search activity is recorded here only when it
explains coverage or changes the problem situation.

`research/nima/publication_claim_dag.json` is the legacy migration input. Future
compatibility exports are projections and must not become a second authority.
