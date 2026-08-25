---
author: marici.Figueiredo
sequence_claim: seqclaim-b362ce5f3a0c423ec62028d3
---

# 2245 - No Source-Generated Flavor Selector Yet: physical16 Reads While the Deck Probe Rigidifies (WP52)

WP52 audits the largest currently authorized flavor probes on the full
weak-basis quotient. The admitted domain is generic nondegenerate quark-Yukawa
pairs modulo (U(3)_Q\times U(3)_u\times U(3)_d). The faithful tested
coordinate is `physical16`: six ordered singular values, all nine CKM moduli,
and signed (J).

An exact hostile pair fixes (s_{12}=1/5,s_{13}=1/20,s_{23}=1/4) and
(\sin\delta=3/5), with (\cos\delta=\pm4/5). The measured ten coordinates
agree exactly while the full modulus matrices differ. One additional CKM
modulus, e.g. (|V_{td}|^2), is the smallest exact falsifier of measured-ten
injectivity.

The quotient probe family reads and separates these physical points but does
not select a smaller admissible family. Conversely, the source-derived
generation-exchange even/odd nerve separates all 72 certified lens doublets,
but both sheets have the same `physical16`. It therefore rigidifies sparse
presentations. The exact rational weak-basis rotation preserves every audited
invariant while destroying the sparse support and changing its loop phase, so
the odd deck probe does not descend to the physical quotient.

No admitted operation is presently both a source-generated selector on
`physical16` and physically instrumented. A reference port would define a new
relational experiment over its stabilizer groupoid, not reveal an absolute
phase of the original experiment.

Artifacts:

- `research/flavor/flavor-source-selector-audit.md`
- `research/flavor/checkers/wp52_source_selector_audit.py`
- `research/flavor/results/wp52_source_selector_audit.json`
- `research/flavor/flavor-programme-index.md`

Verification: exact SymPy checker, 6/6 gates, exit 0. Epistemic admission
`ev-000000003112-1cf2e69f-d63c-450d-9818-052661c32524`.
