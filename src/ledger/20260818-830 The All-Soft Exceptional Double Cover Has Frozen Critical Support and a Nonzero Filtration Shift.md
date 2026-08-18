---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 830 — The All-Soft Exceptional Double Cover Has Frozen Critical Support and a Nonzero Filtration Shift

## Question after Entries 828–829

Entry 828 proves exact radial self-similarity, and Entry 829 proves that
the scalar Kummer coordinate glues with the weight-three projective
cocycle.  Two checks remained:

1. whether saturation of the exceptional singular ideal creates a new
   critical stratum;
2. whether the transformed source measure is genuinely trivial, rather
   than merely having trivial monodromy.

## Correct exceptional object

The exceptional family is not only the projective sextic
(K_{\rm CM}=0).  It is the double cover

\[
\boxed{
W^2=K_{\rm CM}
(\widehat E,\widehat P_1,\widehat P_2,\widehat P_3,
 \widehat a,\widehat b)
}
\]

in the total space of \(\mathcal O_{\mathbf P^5}(3)\), equivalently the
corresponding weighted-projective hypersurface.

The complete source polynomial has 22 distinct monomials, each of radial
degree six.  Therefore

\[
K_{\rm CM}(\rho\widehat{\boldsymbol k})
=\rho^6K_{\rm CM}(\widehat{\boldsymbol k}),
\qquad
w=\rho^3W,
\]

and the strict-transform equation contains no \(\rho\).

## Saturated exceptional critical scheme

The affine double-cover singular ideal is

\[
J_{\rm aff}=(w,\partial K_{\rm CM}).
\]

Differentiating the degree-six homogeneity identity gives

\[
(\partial_iK_{\rm CM})(\rho\widehat{\boldsymbol k})
=\rho^5(\partial_iK_{\rm CM})(\widehat{\boldsymbol k})
\]

for every one of the six labelled variables.  After removing only these
forced exceptional powers, the exceptional ideal is exactly

\[
J_E=(W,\partial K_{\rm CM}(\widehat{\boldsymbol k})).
\]

Consequently its projective singular scheme is defined by saturation with
the irrelevant ideal:

\[
\boxed{
\operatorname{Sing}(E_{\rm exc})
=
\operatorname{Proj}
\frac{\mathbb Q[\widehat{\boldsymbol k},W]}
{(J_E:\mathfrak m^\infty)}.
}
\]

Because \(J_E\) is exactly the homogeneous copy of \(J_{\rm aff}\), this is
the projectivization of the already frozen Cayley–Menger critical cone.
Saturation removes components supported only at the radial vertex; it
does not add generators or incidence divisors.  This statement does not
claim that every projective direction has the same coefficient rank.

## Measure and support grading

For the source relative Kummer form, at fixed radial base coordinate,

\[
\frac{da\wedge db}{w}
=
\rho^{-1}
\frac{d\widehat a\wedge d\widehat b}{W}.
\]

Thus the radial exponent is integral and its monodromy is trivial,

\[
\boxed{M_\rho=1,}
\]

but the form retains a nonzero radial filtration weight:

\[
\boxed{\operatorname{wt}_\rho(da\wedge db/w)=-1.}
\]

Every frozen marked denominator is radially linear.  Hence its relative
logarithmic differential has weight zero:

\[
d_{\rm rel}\log q=d_{\rm rel}\log\widehat q.
\]

The labelled support maps therefore acquire no new exceptional overlap
divisor.  Their usual codimension/Gysin shift and the density's integral
Rees step must nevertheless be retained; trivial monodromy does not erase
this filtration data.

## Narrow result

\[
\boxed{
\begin{array}{c|c}
\text{exceptional object}&\text{weight-three CM double cover}\\
\text{singular support}&\text{projectivized frozen critical cone}\\
\text{new singular/carrier generator}&0\\
\text{radial monodromy}&1\\
\text{relative density weight}&-1
\end{array}}
\]

The all-soft locus is therefore self-similar coefficient geometry over the
existing radial Rees carrier.  It creates neither a new finite-rank
coefficient object nor a new carrier stratum, but it is not filtration
trivial.

## Verification

- exact sparse Rust certificate:
  `research/benincasa/marici-gm/src/bin/all_soft_exceptional_saturation.rs`;
- machine-readable packet:
  `research/benincasa/all-soft-exceptional-saturation.json`;
- allocator claim: `seqclaim-d27b8a565cceb2aa3966c53e`.

## Next falsifier

Pull the labelled residue/Gysin maps through all six projective charts and
test whether their orientation and filtration shifts obey the same Čech
cocycle as Entry 829's Kummer line.  A nonunit transition would be
coefficient support; only a transition requiring an undeclared incidence
divisor would reopen H2 at carrier level.
