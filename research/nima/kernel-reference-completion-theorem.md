# Kernel-reference completion: invisible modes must be retained, not deleted

## Linear theorem

Let

\[
L:V\to W
\]

be an observation, syndrome, projection, or implementable-tail map, and
let \(K=\ker L\) be its invisible mode space. Add a reference channel

\[
R:V\to U.
\]

The completed observation

\[
(L,R):V\to W\oplus U
\]

is faithful exactly when \(K\cap\ker R=0\), equivalently when \(R|_K\) is
injective.

For finite-dimensional spaces,

\[
\dim U\ge\dim K.
\]

Thus a one-dimensional common mode requires at least one independently
rooted bit or scalar channel.

## No internally derived repair

If the proposed reference is computed solely from the old observation,

\[
R=T L,
\]

then \(K\subseteq\ker R\). Therefore

\[
\ker(L,R)=K,
\]

and no lost distinction is restored.  Post-processing, duplicated
syndromes, scalar reformulations, or renormalized outputs that factor
through (L) cannot repair its invisible kernel.

## Relative completion law

A valid decomposition

\[
x\longmapsto
(Lx,Rx)
]

may move a non-implementable or non-observable component into a distinct
typed channel.  It may not discard it.  For every finite cutoff (X),
there must be a reconstruction constructor

\[
J_X(L_Xx,R_Xx)=x_X
\]

or the exact original finite-cutoff observable derived from (x_X).
The completed limit is faithful only if these reconstruction squares
commute with cutoff inclusions.

This separates:

- **typing/splitting authority:** identifies the invisible mode;
- **reference authority:** supplies a channel nonzero on that mode;
- **reconstruction coherence:** proves that the split did not delete it;
- **limit authority:** justifies the completed topology or
  renormalization.

## Kitaev application

For the repetition complex,

\[
E_n(b)=b\mathbf1_n,qquad H_nE_n=0.
\]

The common mode (K=\langle\mathbf1_n\rangle) is one-dimensional.
Any internal syndrome-derived bit has the form (T H_n) and vanishes on
(K).  One independently rooted intended-command bit (R) with
(R(\mathbf1_n)=1) is necessary and sufficient to restore faithfulness.
Physical fault meaning still requires the interface map
(\Phi_{\rm fault}).

## Local Tate application

The local Fock plethystic logarithm canonically separates:

\[
\log\gamma_p
=
\underbrace{
2ip^{-1/2}\sin(t\log p)
}_{\text{one-particle primitive current}}
+
\underbrace{
2i\sum_{k\ge2}
\frac{p^{-k/2}\sin(kt\log p)}{k}
}_{\text{prime-power dressing}}.
\]

The tail has square-summable local deviations, while the primitive
current has norm-square mass (sum_p1/p) and lives only in the
distributional rigging.  The Fock grammar authorizes this split of
types.  It does not authorize deletion of the primitive current.

A faithful relative determinant must therefore retain both:

\[
(\text{implementable tail},\text{primitive distributional current}),
\]

and reproduce every finite Euler cutoff before taking the completed
limit.  Deriving the reference channel from the already-renormalized
tail would factor through (L) and fail the theorem.

## Compiler rejection witnesses

```json
{
  "code": "reference_factors_through_lossy_projection",
  "kernel_dimension": 1,
  "reference_rank_on_kernel": 0
}
```

```json
{
  "code": "renormalization_deleted_typed_current",
  "deleted_type": "primitive_one_particle_current",
  "finite_cutoff_reconstruction": false
}
```

## Boundary

This theorem proves the minimal information and coherence requirements
for faithful completion.  It does not construct the global relative
determinant, prove positivity of its generator, or identify physical
controller faults without an authorized interface map.
