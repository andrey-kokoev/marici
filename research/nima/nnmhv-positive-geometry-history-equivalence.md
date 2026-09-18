# NNMHV positive geometry and history representations

## Positive-geometric formulation

For positive external data

\[
Z_a\in\mathbb R^6,
\qquad
\langle Z_{a_1}\cdots Z_{a_6}\rangle>0
\quad(a_1<\cdots<a_6),
\]

the tree-level `n`-point NNMHV amplituhedron is

\[
\mathcal A_{n,2,4}(Z)
=
\{Y=CZ\mid C\in G_+(2,n)\}
\subset G(2,6).
\]

Its dimension is fixed:

\[
\dim\mathcal A_{n,2,4}=2\cdot4=8,
\qquad n\ge6.
\]

A positive-cell triangulation gives its canonical form:

\[
\Omega_{n,2,4}
=
\sum_{h\in\mathcal H_n}\Omega_h.
\]

Here `H_n` is the sourced generalized-R coherence-history set. Increasing `n` refines the cellulation by adding external positive data; it does not increase geometric dimension.

## Verified history-to-cell bridge

At six points, the unique sourced history is the top cell of `G_+(2,6)` with bounded affine permutation

\[
(3,4,5,6,7,8).
\]

At seven points, all six sourced histories match parity-dual simplex canonical forms exactly, including all 35 one-component fermionic coefficients and complete bosonic normalization. The matched NMHV simplex labels are

\[
[13467],\ [14567],\ [12456],\ [23456],\ [12346],\ [12367].
\]

This is a different triangulation from the standard anchored NMHV BCFW triangulation. Parity preserves the complete canonical form, not a chosen termwise cellulation.

For the normalized selected component,

\[
\widehat C_{23}(n)
=
\sum_{5\le b_2\le b_1\le n-1}T_n(b_1,b_2),
\]

with exact support restricted to left-nested histories with `a_1=2` and `a_2=3`. In shifted coordinates

\[
u=b_2-5,
\qquad
v=b_1-b_2,
\]

the support is the positive triangular lattice

\[
u\ge0,
\qquad
v\ge0,
\qquad
u+v\le n-6.
\]

## Representation table

| # | Representation | Dimension | Symmetry source | Fundamental object |
|---:|---|---|---|---|
| 1 | Positive geometry | 8 | Positivity and canonical-form invariance | `A_(n,2,4)` |
| 2 | History poset | `m(m+1)/2`, with `m=n-5` | Ordered cell refinement | `K_n(b1,b2)` |
| 3 | Polarized coherence | 2 real channels | Insertion/reflow polarity | `Psi_n` |
| 4 | Projective correspondence | `P(Mat_2)=P^3`, stratified by rank | Projective matrix semigroup | `[T_n]` |
| 5 | Incidence algebra | History-module dimension | Zeta/Mobius convolution | `zeta, mu` |
| 6 | Discrete connection | Cutoff-dependent | History-frame gauge symmetry | `U_n, B_n, C_n` |
| 7 | Transfer operator | 2 by 2 real | `GL(2,R)` channel transport | `M_n` |
| 8 | Generating function | One complex variable | Cutoff translation | `G(z)` |
| 9 | Projective twistor | `CP^1`; singular boundary `CP^1 x CP^1` | `PGL(2,C)` on the invertible stratum | image/kernel lines |
| 10 | Clifford rotor | Even algebra dimension 8 real | `Spin^+(1,3)` where transport is invertible | `R_n=U_n P_n` |
| 11 | Tensor network | Bond-dependent | Internal bond gauge | Resolved phase tensors |
| 12 | Renormalization flow | Infinite refinement trajectory | Scale semigroup | `K_n -> K_infinity` |

## Equivalence and projection map

| From | To | Map | Status |
|---|---|---|---|
| Positive geometry | Positive cells | Choose a triangulation | Standard |
| Positive cells | Coherence histories | Generalized-R history labels | Verified through `n=7` |
| Coherence histories | History kernel | Retain endpoint indices `(b1,b2)` | Exact for the selected component |
| History kernel | Incidence algebra | Zeta transform and Mobius inversion | Exact |
| History kernel | Polarized coherence | Split cutoff change into insertion and reflow | Numerically exact definition |
| Polarized coherence | Scalar coefficient | Augmentation by `(1,1)` | Exact |
| History transitions | Projective correspondence | Complex boundary-path transport modulo scale | Exact; ranks one and two occur |
| Rank-one correspondence | Segre boundary | `T=u v^T`, giving image and kernel lines | Exact at `n=7` |
| Invertible correspondence | Local twistor holonomy | Restrict to the `PGL(2,C)` open stratum | Exact locally |
| Local twistor holonomy | Clifford rotor | Polar decomposition into rotation and boost | Exact only on the invertible stratum |
| Shell sequence | Generating function | `z`-transform | Formal |
| Finite kernels | Completion flow | Inductive cutoff refinement | Numerically studied through `n=64` |

## Claim boundary

Established:

- complete finite NNMHV history compilation and boundary updates;
- exact six-point anti-MHV equality;
- seven-point history/canonical-cell matching;
- fixed eight-dimensional positive geometry;
- selected-component history support theorem;
- incidence-algebra and polarized-flux reductions;
- numerical `n^-2` completion tail across tested coherent families.

Open:

- positive-cell compiler for arbitrary histories and arbitrary `n`;
- analytic derivation of the `n^-2` completion law;
- a global category-valued connection using projective correspondences;
- identification of its rank-one image/kernel polarities with insertion/reflow channels;
- a curvature notion that remains defined across singular strata.

The local Lorentz/rotor representation applies only to invertible complex transport loops. Raw NNMHV boundary transport can contain rank-one null-edge bispinors, so it does not define a global `SL(2,C)` frame connection. It is not a replacement definition of the amplituhedron.

## Evidence

- `research/nima/results/nnmhv-positroid-seed.json`
- `research/nima/results/seven-point-history-parity-cell-matching.json`
- `research/nima/results/nnmhv-component-23-support-theorem.json`
- `research/nima/results/history-poset-boundary-calculus.json`
- `research/nima/results/phase-boundary-biconvolution-rule.json`
- `research/nima/results/nnmhv-long-exponent-two-limit.json`
- `research/nima/results/nnmhv-boundary-update-holonomy.json`
- `research/nima/results/nnmhv-boundary-transport-frame-obstruction.json`
- `research/nima/results/nnmhv-projective-transport-correspondences.json`
- `research/nima/results/rank-one-transport-segre-boundary.json`
- `research/nima/nnmhv-fixed-dimension-refinement-correction.md`
