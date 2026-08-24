# Supported Cyclic Memory Is Clique Homology

For a labelled coherence support graph \(G\), the cyclic information not
reconstructed from triangle Bargmann ports is canonically

\[
H_1(\operatorname{Cl}G)
=\ker\partial_1/\operatorname{im}\partial_2,
\]

where \(\operatorname{Cl}G\) is the clique complex obtained by filling every
supported triangle.

Precisely, \(H_1\) types the supported cycle carrier; its phase-valued
readouts lie in

\[
H^1(\operatorname{Cl}G;U(1))
\simeq\operatorname{Hom}(H_1(\operatorname{Cl}G),U(1)).
\]

The exact census of all 64 support graphs on four labels gives only three
nonzero cases: the three chordless Hamiltonian four-cycles.  Each carries one
supported cyclic direction.  The complete graph has cycle rank three, but its
triangle boundaries also have rank three, so it has no independent generic
four-cycle grade.

Thus

\[
\boxed{
\text{higher cyclic memory is the homology left when lower coherence cells
can no longer fill a supported cycle.}
}
\]

This supplies a coordinate-free explanation of Entry 2044 and a stratified
target for Entry 2045's unresolved Gaussian finite branch: test the three
Gaussian Hamiltonian traces on the corresponding chord-deletion strata.

Verification: exact exhaustive checker, 7/7 gates. Epistemic event
`ev-000000002798-a2c07e5f-cd10-4079-90d5-cfad3274e22f`.

Artifacts:

- `research/nima/four-occurrence-clique-homology.md`
- `research/nima/checkers/check_four_occurrence_clique_homology.py`
- `research/nima/results/four-occurrence-clique-homology.json`

Sequence claim: `seqclaim-a3dd9472ae28d46dfb164c49`.
