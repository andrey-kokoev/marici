# The commuting reflections force only one common pencil direction

## Global reflection group

The branch polynomial is even separately in \(a,b,h\). Weighted-projectively, simultaneous sign change of \((a,b,h)\) is trivial, so the three reflections satisfy

\[
r_ar_br_h=1,
\qquad r_h=r_ar_b.
\]

They commute.

For each coordinate reflection, the fixed locus consists generically of:

- the double cover of the fixed coordinate line, branched at four points, hence a genus-one curve with Euler characteristic zero;
- two points over the isolated opposite coordinate point.

Genericity is verified directly: at \((x,y,z)=(2,3,4)\), the three binary-quartic branch restrictions have nonzero discriminants

\[
7718556706799616000,
\quad4487314368531456000,
\quad10497600,
\]

and the branch values at the three isolated coordinate points are respectively \(4,9,109440\), all nonzero. Hence these discriminants and point values are not identically zero in parameter space.

Thus each generic fixed-locus Euler characteristic is \(2\). Lefschetz gives trace zero on the rank-eight Picard lattice and trace \(-1\) on the rank-seven \(E_7\) lattice. Equivalently, every nontrivial reflection has \(E_7\) multiplicities

\[
(+1)^3\oplus(-1)^4.
\]

## Joint character decomposition

Let \(n_{\epsilon_a\epsilon_b}\) be the multiplicity of the joint character \((\epsilon_a,\epsilon_b)\) on \(E_7\). The dimensions and traces of \(r_a,r_b,r_ar_b\) force

\[
(n_{++},n_{+-},n_{-+},n_{--})=(1,2,2,2).
\]

Therefore

\[
\operatorname{rank}igl(E_7^{r_a=+1}\cap E_7^{r_b=+1}\bigr)=1.
\]

## Pencil interpretation

The component-difference lattice of the \(b\)-adapted split-fiber pencil lies in the \(r_a\)-fixed rank-three sector. By site symmetry, the corresponding \(a\)-pencil lattice lies in the \(r_b\)-fixed rank-three sector. Their ambient invariant sectors intersect in only one rational direction.

Hence there cannot be a canonical rank-three identification obtained merely by viewing both pencil lattices inside the same \(E_7\). Only one direction is common; the other two directions occupy distinct joint-character sectors.

This explains the earlier central-fiber observation that the two collapsed fixed-pencil supports expose only one primitive line. The missing comparison is genuinely a correspondence between two different rank-two character sectors, not a forgotten relabeling of one common sublattice.

## Information-flow consequence

The response channels decompose as

\[
\text{common invariant line}
\oplus
\text{two-dimensional }b\text{-pencil sector}
\oplus
\text{two-dimensional }a\text{-pencil sector}.
\]

Site exchange interchanges the latter sectors. A return map must choose an integral identification between them. Ambient inclusion and reflection characters alone cannot provide that identification or decide the final kernel-orientation bit.

Verification:

- `research/voevodsky/checkers/check_joint_reflection_character_decomposition.py`
- `research/voevodsky/results/joint_reflection_character_decomposition.json`
