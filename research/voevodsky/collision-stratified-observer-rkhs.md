# Collision-stratified observers and RKHS reconstruction

## Question

Why can no arithmetic cutoff be uniform over all observer packets, and what positive object would canonically assemble the inverse family of Gram constraints?

## Claim boundary

The packet verifies the near-collision obstruction and derives the compact-stratum and RKHS mechanisms. It does not construct a source-derived feature map for the completed arithmetic kernel.

## Near-collision obstruction

For the Gaussian kernel

\[
K(x,y)=e^{-(x-y)^2},
\]

the packet on labels \((0,h)\) has eigenvalues

\[
1+e^{-h^2},
\qquad
1-e^{-h^2}.
\]

Hence

\[
\lambda_{\min}(h)=1-e^{-h^2}
\sim h^2
\]

as \(h\to0\). Exact repetition at \(h=0\) is a presentation relation, but quotienting exact repetitions does not control arbitrarily close distinct labels.

For every fixed positive tail error there is a nonzero \(h\) whose Gram margin is smaller. Thus no cutoff can be uniform even at rank two over all distinct labels.

## Collision-free strata

Uniformity becomes meaningful only after fixing a compact stratum with:

- packet rank \(r\);
- bounded label diameter;
- minimum separation \(\Delta>0\);
- a compact observer-width range.

If the completed kernel is continuous and strictly positive definite on such a stratum, continuity of the least eigenvalue and compactness give a positive stratumwise minimum. A tail cutoff can then depend on \((r,D,\Delta,W)\).

The separation parameter is essential. Removing only exact repetitions leaves the stratum noncompact toward its collision boundary.

## Reconstruction from the inverse cone

Suppose every finite Gram restriction of a kernel \(K\) is positive semidefinite. Formal kernel sections \(K_x\) carry the form

\[
\left\langle
\sum_i a_iK_{x_i},
\sum_j b_jK_{y_j}
\right\rangle
=
\sum_{i,j}\overline{a_i}b_jK(x_i,y_j).
\]

Quotienting its null space and completing constructs the canonical reproducing-kernel Hilbert space. Therefore the inverse system of finite positive cones generates a direct-limit pre-Hilbert space and then a completion.

This is a second appearance of opposed limits: universal finite restrictions point backward, while their compatible kernel sections assemble forward into a Hilbert object.

## Circularity boundary

Moore--Aronszajn reconstruction is equivalent to positive definiteness. It reorganizes a proof but cannot establish positivity by itself. The desired compression still requires either:

- an explicit source-derived feature map \(\Phi\) satisfying
  \[
  K(x,y)=\langle\Phi(x),\Phi(y)\rangle;
  \]
- or the global Douglas contraction yielding such a feature map.

An RKHS constructed only after assuming all Gram matrices positive is a semantic realization, not the missing arithmetic proof.

## Disposition

Observer infinity must be stratified by collision geometry. Pointwise cutoffs are unavoidable globally; uniform cutoffs may exist on compact collision-free strata. The canonical endpoint of successful positivity is an RKHS, but the proof-producing object must be a source-derived feature map or contraction rather than an abstract reconstruction from assumed positivity.

## Verification

- `research/voevodsky/collision-stratified-observer-rkhs-v1.json`
- `research/voevodsky/checkers/check_collision_stratified_observer_rkhs.py`
- `research/voevodsky/results/collision_stratified_observer_rkhs.json`
