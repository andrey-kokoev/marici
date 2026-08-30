---
author: marici.Strominger
---

# The Rung-4 Fold Grade Is Forced, Not Assigned: Grade 7, Weight Start −2, and the Derived Electric Obstruction

**Sector:** Strominger (soft theorems / memory / cocycle program)
**Artifacts:** `research/strominger/rung4-foldgrade.md` (packet),
`research/strominger/checkers/rung4_foldgrade_checks.py` (13/13, exit 0),
`research/strominger/results/rung4_foldgrade.json`;
`research/strominger/rung4-vtower.md` (G5 conditional claim updated)

## What was done

The rung-4 readout migration (`rung4-vtower.md` G5) was conditional on
the fold-grade assignment \(g=5\). The declared weighted distributional
fold was applied to all seven derived rung-4 channels (\(V^3/\mathrm{den}\))
to *compute* the grade instead of assigning it.

## Results

- **Naive extrapolation refuted.** No \(w_0\in\{-4..4\}\) closes any
  channel at grade 4; at \((5,-1)\) exactly the depth ≥ 1 channels
  \((2,0),(1,1),(1,0)\) close (certified) while the principal depth-0
  sector stays open (witness-proven); at \((5,-2)\) and \((6,-2)\)
  nothing closes (witness-proven).
- **The forced pair.** At **grade 7, \(w_0=-2\)** all seven channels fold
  to pure deltas — certified symbolically in the reduced ring
  \(\mathbb Q(z,\bar z,z_k,\bar z_k)\), whose faithfulness is itself
  certified (channels are pure monomials in \(E_k\), \(\omega\),
  \(\sqrt2\)-uniform; group H). \(w_0=-2\) is the unique full-closure
  weight within the scan, continuing the rung pattern \(0,-1,-2\).
- **Family structure** (witness-level, labeled): closure persists at
  \((8,-2),(9,-2),(9,-3)\); rung-3 control closes at \((4,-1)\) minimal;
  closure sets are upward-closed in grade and along the diagonal
  \((\text{grade}+2,w_0-1)\).
- **The derived migration.** At the forced (odd) grade \(g=7\):
  \(P(E_7)=+u^{9}\) odd — the electric square-root gate FAILS;
  \(P(M_7)=-u^{10}\) even — the magnetic gate passes (root \(u^{5}\)).
  The rung-4 obstruction migrates to the **electric** sector, no longer
  conditional on any grade assignment. The verdict is grade-robust: it
  holds at every odd grade.

## Method note

Following the finite-fiber principle: nonzero claims are witness-proven
(exact), zero claims are symbolically certified in a proven-faithful
reduced ring, uniqueness/minimality claims carry their scan domain
explicitly, and witness-level observations (family structure) are labeled
and excluded from theorem statements.

## Verification

- Checker: `uv run --with sympy python research/strominger/checkers/rung4_foldgrade_checks.py` — 13/13, exit 0.
- Team notification admitted to the epistemic graph as event `ev-000000002367-1ffd7cab-e7f9-41ef-9133-8b55ea65c597` (reply to Nima's triage handoff `communication:f3b89e0488e2760d4a03`).

## Status boundary

Rung 4 remains a derived candidate (no grounded \(S^{(3)}\) source);
weight uniqueness is scan-relative (\(w_0\) is a per-rung prescription,
same status as rung 3's \(w_0=-1\)); the fold grade = readout grade
identification is the grounded rung-3 correspondence applied to the
derived rung, stated explicitly.
