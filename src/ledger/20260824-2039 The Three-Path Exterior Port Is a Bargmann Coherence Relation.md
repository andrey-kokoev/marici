# The Three-Path Exterior Port Is a Bargmann Coherence Relation

The hostile three-alternative test separates magnitude readout from full
coherence data.

For normalized record states with Gram matrix

\[
G=\begin{pmatrix}
1&a&b\\
\bar a&1&c\\
\bar b&\bar c&1
\end{pmatrix},
\]

the grade-three exterior weight is

\[
\det G
=1-|a|^2-|b|^2-|c|^2
+2\operatorname{Re}(ac\bar b).
\]

Two exact strictly positive packets with

\[
|a|=|b|=|c|=1/3
\]

have identical pairwise distinguishabilities and identical \(\wedge^2\)
weight but different Bargmann phases.  Their \(\wedge^3\) weights are

\[
20/27
\qquad\text{and}\qquad
2/3.
\]

Thus pairwise magnitudes do not reconstruct the three-occurrence interface.
However, full oriented pairwise coherences determine the determinant exactly.
The rank-three port is therefore a coherence relation among pairwise ports,
not an independent amplitude Carrier cell.

This is compatible with a quadratic Born readout having no independent
third-order Sorkin interference while the three record states retain
nontrivial Bargmann geometry.

The next cross-sector test is whether three-mode Gaussian purity has the same
determinantal closure or a source-forced symplectic/Pfaffian refinement.

The exact checker passes 6/6 gates.

Artifacts:

- `research/nima/three-path-exterior-purity-gate.md`
- `research/nima/checkers/check_three_path_exterior_purity.py`
- `research/nima/results/three-path-exterior-purity.json`

Sequence claim: `seqclaim-2f981181fd5d60ea1d24e409`.

