# Frozen Lean formalization targets for information-preserving reconstruction

## Question

Which programme statements are sufficiently stable and assumption-complete to hand to the Lean formalization owner without importing active conjectures as axioms?

## Claim boundary

This packet freezes four theorem targets and two finite algebra targets. It does not contain Lean source because `research/buzzard/` is owned by `marici.Buzzard`, and no cross-locus mutation authority has been granted. The standard candidate toolchain files `lean-toolchain`, `lakefile.lean`, `research/buzzard/lean-toolchain`, and `research/buzzard/lakefile.lean` were not present at those paths. The exact existing project root and checking command remain a toolchain-discovery obligation for the formalization owner.

## Target F1: lower-bound transport

### Source

`research/voevodsky/boundedly_invertible_comparisons_transport_observer_margins_with_condition_number_loss_20260910.md`

### Mathematical statement

Let \(X,X',Z\) be normed spaces, let \(C:X\to X'\) be a bounded linear equivalence, and let \(T:X\to Z\) be bounded linear. If

\[
\delta\|x\|\le\|Tx\|
\]

for every \(x\), then

\[
\frac{\delta}{\|C\|}\|x'\|
\le
\|TC^{-1}x'\|
\]

for every \(x'\), provided \(\|C\|>0\).

### Lean-shaped signature

```lean
theorem lowerBound_comp_equiv_symm
    {X X' Z : Type*}
    [NormedAddCommGroup X] [NormedSpace ℝ X]
    [NormedAddCommGroup X'] [NormedSpace ℝ X']
    [NormedAddCommGroup Z] [NormedSpace ℝ Z]
    (C : X ≃L[ℝ] X') (T : X →L[ℝ] Z)
    (δ : ℝ) (hδ : 0 ≤ δ)
    (hT : ∀ x, δ * ‖x‖ ≤ ‖T x‖) :
    ∀ x', (δ / ‖C‖) * ‖x'‖ ≤ ‖T (C.symm x')‖
```

### Hidden-assumption audit

- scalar field may be generalized after the real version passes;
- the zero-space case requires care because \(\|C\|\) may be zero;
- a cleaner theorem may use any supplied constant \(M_C>0\) with \(\|Cx\|\le M_C\|x\|\), avoiding division by operator norm;
- no Hilbert structure is needed.

### Acceptance test

A checked theorem with no imported conclusion assumptions, plus a scalar example proving sharpness.

## Target F2: quotient--vertical block row

### Source

`research/voevodsky/quotient_vertical_and_finite_repair_observers_form_a_stable_block_row_20260910.md`

### Mathematical statement

Let \(X,Y,Z\) be real or complex Hilbert spaces, \(V\subseteq X\) a closed subspace, \(P_V\) its orthogonal projection, and \(A:X\to Y\), \(E:X\to Z\) bounded linear. Assume

\[
\|Ax\|\ge a\|x-P_Vx\|
\]

for all \(x\), and

\[
\|Ev\|\ge d\|v\|
\]

for all \(v\in V\), with \(a,d>0\). Then

\[
\sqrt{\|Ax\|^2+\|Ex\|^2}
\ge
\frac{d}{\sqrt{1+((d+\|E\|)/a)^2}}
\|x\|.
\]

### Formalization recommendation

First prove a constant-parameter lemma replacing \(\|E\|\) by an explicit \(M\ge0\) satisfying

\[
\|Ex\|\le M\|x\|.
\]

This avoids operator-norm rewriting during the geometric proof. Instantiate \(M=\|E\|\) only in a corollary.

### Required library objects

- `Submodule.orthogonalProjection` or the current mathlib equivalent;
- product norm on \(Y\times Z\), or a squared-norm formulation;
- Cauchy--Schwarz in \(\mathbb R^2\);
- closedness assumption needed for orthogonal projection.

### Acceptance test

The theorem compiles without assuming \(E\) preserves \(V^\perp\). A deliberate test must fail if the vertical lower-bound hypothesis is removed.

## Target F3: finite residual repair

### Source

Same Phase 2 packet.

### Mathematical statement

Let \(V,Z_D,Z_K\) be Hilbert spaces. Let \(D:V\to Z_D\) be bounded with closed range and finite-dimensional kernel \(N\). Let \(K:V\to Z_K\) be bounded and injective on \(N\). Then

\[
v\longmapsto(Dv,Kv)
\]

is bounded below.

### Formalization split

1. closed range gives a lower bound on \(N^\perp\);
2. finite-dimensional injectivity gives a lower bound on \(N\);
3. contradiction or compact-sphere argument combines them.

The first missing library lemma, if any, should be reported rather than replaced by an assumed lower bound unless the weaker conditional theorem is explicitly named.

### Acceptance test

A finite-dimensional example with nonzero \(N\) and a deliberate failure at \(K|_N=0\).

## Target F4: product lower-Lipschitz theorem

### Source

`research/voevodsky/product_bulk_and_holonomy_moduli_observers_are_stable_in_the_explicit_product_metric_20260910.md`

### Mathematical statement

Let \((X,d_X)\), \((M,d_M)\), \((Y,d_Y)\), and \((R,d_R)\) be metric spaces with squared \(\ell^2\) product metrics. If \(F:X\to Y\) and \(G:M\to R\) have lower-Lipschitz constants \(\delta_X,\delta_M\ge0\), then

\[
(F,G):X\times M\to Y\times R
\]

has lower constant \(\min(\delta_X,\delta_M)\).

### Formalization recommendation

Use nonnegative reals or squared real distances to avoid unnecessary square-root order obligations. A normed-space specialization may be easier than a fully generic metric product if mathlib's product metric is the max metric rather than the declared \(\ell^2\) metric. Do not silently use the library default product metric if it is not the theorem's metric.

### Acceptance test

Two examples in which each factor separately determines the minimum.

## Target A1: reciprocal block classification

### Source

`research/voevodsky/the_full_nonlocal_reciprocal_commutant_splits_over_the_two_parity_sectors_20260911.md`

### Frozen finite statement

For a commutative star field, unit \(u\), and square matrices \(A,B,C,D\) of the same size, define

\[
W_u=
\begin{pmatrix}0&u^{-1}I\\uI&0\end{pmatrix},
\qquad
M=
\begin{pmatrix}A&C\\D&B\end{pmatrix}.
\]

Then

\[
MW_u=W_uM
\]

if and only if \(B=A\) and \(D=u^2C\). Likewise,

\[
MW_u=-W_uM
\]

if and only if \(B=-A\) and \(D=-u^2C\).

### Scope restriction

Formalize finite matrices first. The bounded-operator version has the same block algebra but requires continuous-linear-map block infrastructure. No analytic conclusion is part of A1.

### Acceptance test

Both directions for even and odd variance, with a mutated lower-left block rejected by simplification.

## Target A2: tree-gauge Wilson lower bound

### Source

`research/voevodsky/spanning_tree_gauge_gives_explicit_combinatorial_bounds_for_wilson_observer_stability_20260911.md`

### Frozen finite statement

For a finite connected graph, positive edge weights, a spanning tree \(T\), and two edge-phase assignments in tree gauge,

\[
d_\Gamma([z],[z'])^2
\le
\Lambda_T
\sum_{e\notin T}
|\operatorname{Hol}_{c_e}(z)-
\operatorname{Hol}_{c_e}(z')|^2,
\]

where

\[
\Lambda_T=\max_{e\notin T}\lambda_e.
\]

### Dependency boundary

This target requires a chosen finite-graph and gauge-action representation. If no reusable graph cochain representation exists, formalize the square-with-diagonal model first rather than inventing a general graph library inside this task.

### Acceptance test

The square-with-diagonal example proves the unit-weight lower constant one and rejects omission of either independent fundamental cycle.

## Priority order

1. F1: smallest reusable theorem, no Hilbert structure.
2. F4: independent product theorem with a metric-definition audit.
3. A1: finite block algebra.
4. F2: core Hilbert reconstruction theorem.
5. F3: finite-defect theorem, dependent on closed-range library support.
6. A2: graph formalization, dependent on available combinatorial infrastructure.

## Ownership and checking blocker

`marici.Buzzard` owns the Lean lane and `research/buzzard/`. This packet author has no authority to create or modify Lean files there. No standard Lean project marker was found at the four candidate paths inspected. The first required action by the formalization owner is to identify the admitted existing Lean project root, toolchain, and exact checking command without installing a new global toolchain or creating a second project root.

The acceptance object for the handoff is:

\[
(\text{project root},\text{toolchain},\text{target file},
\text{exact command},\text{first theorem status}).
\]

## Disposition

Six formalization targets are frozen with exact sources, statements, assumptions, failure tests, and dependency boundaries. Lean implementation is blocked on owner authority and project discovery, not on statement ambiguity. The smallest executable target is F1; the central theorem is F2. No Lean theorem is claimed checked in this packet.
