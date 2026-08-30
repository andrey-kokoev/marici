# Full Yoneda Probing Stabilizes While Restricted Probing Produces Quotients

In the finite category fragment of \(\mathbf F_2\)-vector spaces of dimensions
zero through two, every map \(f:V\to W\), for \(V=W=\mathbf F_2^2\), is
reconstructed from its complete natural probe profile:

\[
\eta_A(g)=f\circ g,\qquad f=\eta_V(1_V).
\]

All 16 maps have distinct profiles, and exhaustive composition checks verify
naturality across the fragment.  The second full probe-profile rung therefore
adds no new map information.

A restricted one-coordinate probe creates a two-class quotient of the four
states.  Adding the missing independent probe restores joint faithfulness.

This supports, in a bounded exact model, the conjecture that full Yoneda
rotation stabilizes the tower up to equivalence while sector-restricted probe
families produce genuine operational quotients and the need for coherence
repair.  It does not establish completeness of Marici's physical probes.

Verification: dependency-free exact checker, 7/7 gates. Epistemic event
`ev-000000002830-c59ed43b-d0bb-4beb-a9b6-a06a4d6a4e6f`.

Artifacts:

- `research/nima/yoneda-tower-stabilization-finite-test.md`
- `research/nima/checkers/check_yoneda_tower_stabilization_f2.py`
- `research/nima/results/yoneda-tower-stabilization-f2.json`

Sequence claim: `seqclaim-835a36f4df0fab8c7fc408a0`.
