# Bivariate Clark prolongation supplies the negative jet tower

## Status

Exact product-rule theorem and multiplicity repair. Applying matched spectral
jets to the two-variable Green identity automatically generates a negative
endpoint square at every jet order. Thus the filtered negative seam-current
tower is already source-derived; it need not be postulated separately.

The new residual is the triangular Jordan current produced when the jets hit
the linear spectral prefactor. Together with the high-frequency finite-band
no-go, this shows that the surviving source object is doubly filtered: by jet
order and by phase-band resolution.

## Two-variable Green form

Write the denominator-free Green identity schematically as

\[
p(z,w)N(z,w)
=
B(z,w)-S(z,w)-F(z)\overline{F(w)},
\]

where

\[
p(z,w)=i(\overline w-z).
\]

Here \(N\) is the tail pairing, \(B\) is the positive forced-feature pairing,
\(S\) is the fixed source reservoir term, and the final term is the negative
endpoint kernel.

The identity is formed before division by a scalar transform.

## Matched pure jets

Apply

\[
\partial_z^m\partial_{\overline w}^m
\]

to the complete identity. The endpoint term becomes

\[
-F^{(m)}(z)\overline{F^{(m)}(w)}.
\]

On the diagonal it is the negative jet square

\[
-|F^{(m)}(z)|^2.
\]

Therefore every positive \(m\)-th jet observation has a source-derived
negative endpoint partner at the same order.

## Exact Jordan product rule

The prefactor \(p\) is linear. Its only nonzero first derivatives are

\[
\partial_zp=-i,
\qquad
\partial_{\overline w}p=i.
\]

All second derivatives of \(p\) vanish. Hence

\[
\begin{aligned}
\partial_z^m\partial_{\overline w}^m(pN)
={}&p\,\partial_z^m\partial_{\overline w}^mN\\
&-im\,\partial_z^{m-1}\partial_{\overline w}^mN\\
&+im\,\partial_z^m\partial_{\overline w}^{m-1}N.
\end{aligned}
\]

The last two terms are the induced Jordan current. They couple adjacent jet
levels with opposite orientation.

No higher derivative of the prefactor appears. The current is triangular in
the jet filtration.

## Clark iterates

For

\[
\mathcal C_a=1+ia\partial_z,
\]

the iterates \(\mathcal C_a^m\) are triangular combinations of the first
\(m\) pure jets with nonzero top coefficient \((ia)^m\). Applying matched
Clark iterates in \(z\) and \(\overline w\) therefore gives:

- a positive Clark bulk at level \(m\);
- the negative endpoint square
  \(-|\mathcal C_a^mF|^2\);
- lower-level triangular Jordan couplings;
- the appropriately prolonged source-reservoir terms.

At a zero of multiplicity \(m\),

\[
\mathcal C_a^mF(z_0)
=(ia)^mF^{(m)}(z_0)\neq0.
\]

The matching negative endpoint square is therefore nonzero at exactly the
stage where the positive Clark sensor first becomes nonzero.

This repairs the multiplicity defect of the lone first seam line.

## What cancels automatically

The positive observation of a higher jet and its negative endpoint kernel have
the same source normalization because they are produced by applying one
bivariate differential constructor to one Green identity.

Their coefficient matching is not fitted. But they do not simply disappear
from the full conservation law: the product-rule Jordan current and prolonged
bulk terms remain. The RH-bearing content moves to the sign and sewing of that
triangular residual.

## Fixed finite truncation is insufficient

For any individual zero, finite multiplicity means some finite jet level sees
it. No fixed finite jet depth is known to cover every zero uniformly.

Independently, the physical Hardy audit shows that every fixed finite block of
complete phase periods inherits the same negative high-frequency source gate.
The number of retained bands must grow with inverse microscopic scale, or the
construction must act before band projection.

Thus the source block has two unbounded filtrations:

\[
(m,M),
\]

where \(m\) is jet order and \(M\) is phase-band resolution.

Neither direction may be frozen before completion.

## Relation to the user's size intuition

The state size cannot remain constant because two independent forms of hidden
structure become visible under refinement:

1. higher zero multiplicity demands higher spectral jets;
2. higher oscillation demands more phase bands to preserve macroscopic source
   scale.

The growth is not arbitrary bookkeeping. It is forced by exact failure of
every fixed finite projection.

## Completion architecture

The appropriate object is a filtered or pro-object, not one unweighted direct
sum. Each finite stage carries:

- its Green identity;
- matched positive bulk and negative endpoint jet;
- adjacent-level Jordan current;
- primitive, square, seam, and archimedean types;
- bonding maps in both filtration directions.

Completion must preserve the total paired identity. Separate completion of the
positive and negative towers can destroy the cancellation.

## Finite falsifier

At jet level \(m\), compute the complete bivariate differentiated identity. The
route fails if:

- the endpoint coefficient differs from the Clark observation coefficient;
- a nontriangular jet component appears;
- the Jordan current has an undeclared source type;
- reciprocal sewing fails to match adjacent-level orientations;
- or a finite band projection is claimed uniform despite the high-frequency
  negative-block theorem.

The smallest multiplicity test is \(F(z)=z^2\) at \(m=2\). The smallest
product-rule test is the displayed \(m=1\) Jordan pair.

## Decisive conclusion

The negative seam hierarchy required by arbitrary multiplicity is already
generated by bivariate Clark prolongation of the source Green identity. The
remaining obstruction is not absence of negative ports. It is the induced
Jordan current and the necessity of an unbounded phase-band filtration.

The next exact calculation should sew the adjacent-jet Jordan current through
the reciprocal Tate sectors before any fixed band projection. If that current
closes with the arithmetic boundary hierarchy, the balance route survives; if
it retains an unmatched sign component, the route closes there.
