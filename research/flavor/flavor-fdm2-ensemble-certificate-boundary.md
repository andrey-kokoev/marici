# Ensemble certificate boundary for FDM-2 (WP108)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

Three claims must remain distinct.

1. **Measured-ensemble compatibility.** The predeclared coarse prediction
   `J != 0` holds on all 1,210 stored fitted sheets. Their minimum stored
   `|J|` is approximately `3.1413288219e-5`.
2. **Exact model witness.** WP89-WP107 construct one explicit mediator source
   family with a nonzero physical16 commutator determinant and a conditional
   lower bound.
3. **Ensemble-wide source-map margin.** This would require applying one
   declared vacuum-to-Yukawa map and canonical matching calculation to every
   fitted physical16 point, in a common normalization, and bounding the
   resulting invariant error sheet by sheet.

Only the first two are currently established. The stored fitted `J` values
and the dimensionful commutator determinant are different coordinates; their
numerical minima cannot be compared without masses, normalization, matching,
and a per-sheet source map. WP87's sweep is therefore a valid falsification
test of the qualitative prediction, but not evidence for WP107's quantitative
instrument gap on all sheets.

This does not weaken the exact coarse result: the complete stored ensemble has
zero counterexamples to `J != 0`. It blocks only the stronger inheritance
claim. The smallest exact falsifier of automatic inheritance is a two-sheet
source map `J(s,q)=s j(q)` with `j(q_1)=1` and `j(q_2)=0`; one nonzero witness
does not constrain the second sheet. In the actual programme, no such zero is
observed, but source dynamics has not been evaluated sheetwise.

Classification: the proposed source gives a qualitative ensemble-compatible
branchwise selector; its quantitative finite-resolution margin remains
witness-local. It is not a rigidifier. Remaining instrument gate: define a
common physical16 normalization and canonical source map for all 1,210 sheets,
then compute the minimum post-error invariant gap over that full ensemble.

Verification: `uv run --with sympy python
research/flavor/checkers/wp108_fdm2_ensemble_certificate_boundary.py`.
