# The local Tate seam is unitary, but its naive global tensor product diverges

## Local result

For

\[
\gamma_p(s)=\frac{1-p^{-s}}{1-p^{s-1}},
\qquad s=\frac12+it,
\]

the denominator is the conjugate of the numerator, hence
(|\gamma_p|=1).  The critical line is therefore the unitary sewing
seam between the two local valuation cones.

This local explanation is independent of zero locations.

## Global implementability gate

Let each local seam act on a chosen reference ray by the phase
(gamma_p).  The ordinary infinite tensor product relative to that
reference exists only if the local deviations are square summable:

\[
\boxed{
\sum_p |1-\gamma_p(\tfrac12+it)|^2<\infty.
}
\]

Writing (a=p^{-1/2}) and (	heta=t\log p), direct calculation gives

\[
|1-\gamma_p|^2
=
\frac{4a^2\sin^2\theta}
{1-2a\cos\theta+a^2}
=
\frac{4p^{-1}\sin^2(t\log p)}
{1-2p^{-1/2}\cos(t\log p)+p^{-1}}.
\]

For fixed (t\ne0), the denominator tends to one and the weighted
prime phases have nonzero mean square.  The prime-number theorem then
gives

\[
\sum_{p\le X}|1-\gamma_p|^2
=2\log\log X+O_t(1),
\]

up to the normalization implicit in the displayed local phase.
In particular, the sum diverges.  At (t=0), every local phase is one
and the obstruction vanishes.

Therefore:

\[
\boxed{
t\ne0:
\text{ the raw reference-based infinite tensor product is not
implementable.}
}
\]

The local sewings can still define a renormalized relative determinant,
a projective operator, or an implementer after a nontrivial change of
reference representation.  None of those follows from local unitarity
alone.

## Finite falsifier

For a cutoff (X), compute

\[
S_t(X)=\sum_{p\le X}|1-\gamma_p(\tfrac12+it)|^2.
\]

A proposed raw restricted-product implementation must provide a uniform
Cauchy bound on the tails.  Persistent growth of (S_t(X)), together
with the analytic divergence theorem above, rejects that proposal.

```json
{
  "code": "local_unitaries_not_raw_restricted_product",
  "reference": "canonical_local_vacua",
  "parameter_t": 1.0,
  "obstruction": "sum_p |1-gamma_p|^2 diverges",
  "remaining_options": [
    "renormalized_relative_determinant",
    "projective_implementer",
    "changed_reference_representation"
  ]
}
```

## Interpretation

This gives a sharp separation:

1. **Local geometry:** (Re s=1/2) is forced by unitary Tate sewing.
2. **Global operator:** the naive tensor product fails for (t\ne0).
3. **Renormalization:** any global construction must name its subtraction,
   reference change, or central extension.
4. **RH:** no zero-selection or positivity statement follows yet.

The next noncircular question is whether the completed adelic theory
supplies a canonical renormalization whose generator has an independent
positive-orientation law.

