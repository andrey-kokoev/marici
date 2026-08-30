# 1679 — Cardinality-Weighted Cut Merge Preserves Every Finite Hankel Cone

## Positive-map falsifier

Entry 1678 identifies positivity as a filtered family of Hankel cones. Prove
that cardinality-weighted independent Cut merge preserves each finite cone
directly on truncated polynomial squares.

Let (L_X,L_Y) be positive moment functionals through degree (2d), with
Hankel matrices (H_X,H_Y). For

\[
Z=\alpha X+\beta Y,
\qquad
\alpha^2+\beta^2=1,
\]

the pullback of the monomial (z^k) is

\[
(\alpha x+\beta y)^k
=
\sum_{i=0}^k
\binom ki\alpha^i\beta^{k-i}x^iy^{k-i}.
\]

Let (T) be this substitution matrix. The product functional has Gram matrix

\[
H_X\otimes H_Y,
\]

and the merged Hankel matrix is exactly

\[
\boxed{
H_Z=T^T(H_X\otimes H_Y)T.
}
\]

Hence, for every truncated polynomial coefficient vector (c),

\[
c^TH_Zc
=(Tc)^T(H_X\otimes H_Y)(Tc)
\ge0.
\]

This is a finite algebraic positivity proof; it does not assume an unrecorded
global measure.

The exact checker verifies sixty rational weighted-merge cases through Hankel
degree four:

\[
810\text{ congruence entries},
\qquad
810\text{ positive Gram entries},
\qquad
360\text{ positive product atoms}.
\]

An initial recursive-determinant diagnostic overflowed `i128`; it was rejected
before admission and replaced by the exact Gram certificate.

## Narrow result

\[
\boxed{
\text{cardinality-weighted independent Cut merge preserves every finite Hankel cone.}
}

Combined with Entry 1678, the global positive object is a compatible inverse
system of finite cones, and Cut merge acts grade by grade by positive
congruence. No positivity-specific carrier cell is required.

This result assumes the tensor-product functional for independent blocks.
Correlated blocks require the complete joint positive functional, not merely
its marginal Hankel matrices.

## Durable artifacts

- `research/benincasa/checkers/hankel_cone_cut_congruence.rs`
- `research/benincasa/results/hankel-cone-cut-congruence.json`
- `research/benincasa/hankel-cone-cut-congruence.md`

## Next falsifier

Test correlated positivity. Construct the multivariate truncated moment matrix
for the complete labelled joint cumulant packet and verify that normalized
linear pushforward is again a congruence. Determine precisely which marginal
data fail to reconstruct this positive map.
