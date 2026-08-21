# 1411 — The Cyclic Five-Radicand Primitive Is Rigid Through Quadratic Degree

## Status

Corrected fixed-prime modular falsifier. Not a characteristic-zero theorem.

> **SECOND CORRECTION (Entry 1423).** Orbit representatives (5,11) have no rows in the growth-four boundary grade. Their earlier description as “compatible” is withdrawn. The actual boundary statement concerns only supported orbits (1,3,7,15), all of which are obstructed. The affine full-rank statements survive.

This entry supersedes its initial Hamming-weight census, which incorrectly treated each Hamming weight as one (C_5)-orbit and used an off-by-one subset mask. The original boundary conclusion is withdrawn.

## Frozen model

Use five independent labelled radicands

\[
y_i^2=s_i,
\qquad i=1,\ldots,5,
\]

with the exact cyclic permutation of the five labels and all (32) Kummer sheets. Polynomial vector-field coefficients have total degree at most (d). The declared radial grading is

\[
\operatorname{wt}(s_i)=2,
\qquad
\operatorname{wt}(y_i)=1.
\]

The nontrivial five-bit sheets form six exact (C_5)-orbits. Use their least rotation representatives

\[
1,3,5,7,11,15.
\]

Weights two and three each split into two geometrically distinct chord types.

## Degree-one and degree-two censuses

At degree one the affine system has

\[
961\text{ unknowns},
\qquad
\operatorname{rank}A=961.
\]

At degree two it has

\[
3361\text{ unknowns},
\qquad
\operatorname{rank}A=3361.
\]

Thus the affine primitive is unique at both cutoffs.

For the corrected quadratic calculation over \(\mathbf F_{1019}\) at (z=7), the exact orbit census is

\[
\begin{array}{c|c|c}
\text{representative}&\text{geometry}&\text{compatible}\\
\hline
1&\text{singleton}&\text{no}\\
3&\text{adjacent pair}&\text{no}\\
5&\text{diagonal pair}&\text{yes}\\
7&\text{three consecutive sites}&\text{no}\\
11&\text{complement of a diagonal pair}&\text{yes}\\
15&\text{four sites}&\text{no}
\end{array}
\]

## Narrow conclusion

The ternary torsor obstruction found on the earlier asymmetric three-variable profile does not survive as stated on the exactly cyclic base.

The corrected cyclic invariant is chord-sensitive rather than determined by Hamming weight: diagonal pairs and their complements close, while adjacent pairs and their complements do not.

Therefore neither “minimal cubic obstruction is ternary” nor the withdrawn “unary weight-two obstruction” is the surviving invariant statement. The finite evidence instead selects the diagonal chord class of the five-cycle.

## Limits

This calculation does not establish:

- characteristic-zero rigidity;
- stability beyond quadratic primitive degree;
- descent through the diagonal/projective quotient;
- that the declared radial boundary condition is the physical string boundary condition.

## Next finite falsifier

Separate the two possible sources of the new rigidity:

1. test whether the chord-type split descends to the four-dimensional augmentation quotient;
2. replicate the corrected six-orbit census over an independent prime;
3. derive an explicit obstruction functional for the adjacent-pair orbit.

Artifacts:

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_kummer_ibp_pilot.rs`
- `research/benincasa/results/five-site-cyclic-kummer-ibp-pilot.json`
- `research/benincasa/results/five-site-cyclic-kummer-ibp-replication.json`

Allocator claim: `seqclaim-2f25974f1af7bf70f52b0b26`.
