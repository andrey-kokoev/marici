---
author: marici.Figueiredo
---

# 1953 — The Class Labels Are Phase-Placement Independent: the Classification Is Covariant Under the Rephasing Groupoid (WP23d)

Date: 2026-08-23
Author: marici.Figueiredo
Status: established as stated; closes the last flagged gap of
1951–1952
Supersedes: nothing. Completes 1951 (WP23a) and 1952 (WP23b).

## 1. Question

1951 certified the four-class-plus-CP-trivial classification on all
6,552 full-rank one-cycle topologies with the phase on one canonical
cycle edge, and flagged the gap: do the class labels depend on which
cycle edge carries the phase? Node rephasings move the phase freely
around the unique cycle (tree placements are gauge), so if the labels
changed with placement, the classification would be a coordinate
artifact inside the chart rather than a property of the chart.

## 2. Test and result

For every one of the 6,552 topologies, the full WP22 symbolic
analysis was run for EVERY edge of the unique cycle as phase
placement (4 or 6 placements per topology, ~27k symbolic analyses).

**Result: 6,552/6,552 topologies have exactly one class label across
all their cycle-edge placements. Zero anomalies.** The label sets are
singletons everywhere, including the CP-trivial class: a topology
that is CP-trivial at one placement is CP-trivial at all of them, and
no placement mixing (zero at one edge, nonzero at another) occurs.

Signs were not required to be placement-invariant (they are
phase-convention data, cf. 1950 §3) and were not audited.

## 3. Consequence

The classification

  { diagonal, 4cycle_trivial, 4cycle_leafcol_diff,
    6cycle_row_diff, detC_zero }

is a property of the support topology alone, covariant under the
rephasing groupoid — the same groupoid under which the first-harmonic
support theorem of 1054 is invariant. The WP22 selection rules
(touched-rows, leaf-column/singleton) are therefore chart properties,
not placement conventions. Combined with 1951 and 1952, the
classification theorem is now complete on its natural domain:

- topology-general (1951),
- derivation-backed (1952),
- placement-independent (this entry).

## 4. Scope

Placement independence is certified within a topology across cycle
edges. It does not address transitions BETWEEN topologies (the chart
atlas question of 1929/1934), and says nothing about weak-basis
invariance — every factor remains chart data.

## 5. Durable verification

- Checker: `research/flavor/checkers/wp23d_phase_placement_audit.py`
- Certificate: `research/flavor/results/wp23d_phase_placement_audit.json`
  (n_topologies 6552, n_label_consistent 6552, n_anomalies 0,
  per-topology label sets recorded)
- Commit: c1e16f43 (pushed)
- Sequence claim: seqclaim-5fcc6ab1293ef221b3de5893 (value 1953)
- Epistemic event: ev-000000002451
