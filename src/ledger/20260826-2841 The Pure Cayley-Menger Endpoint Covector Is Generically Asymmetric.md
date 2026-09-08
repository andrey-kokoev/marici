# 2841 — The Pure Cayley–Menger Endpoint Covector Is Generically Asymmetric

## Full-fiber local calculation

Entry 2840 retracts the unsupported separable arcsine covector. A legitimate local covector can instead be derived from the vanishing cycle of the full exceptional kernel.

Write \(A=a^2\). At the two \(\xi\)-endpoint discriminants, the quadratic in \(A\) develops double roots

\[
A_-=(5-4\kappa)p^2
\qquad(\xi=-1),
\]

and

\[
A_+=(5+4\kappa)p^2
\qquad(\xi=+1).
\]

For \(-1<\kappa<1\) and \(p>0\), both roots lie on the positive real \(A\)-axis.

## Positive-sheet vanishing periods

Near a colliding pair in the \(A\)-plane,

\[
\oint\frac{dA}{w}=2\pi i
\]

up to the ordered orientation. Since

\[
dA=2a\,da,
\]

the corresponding positive-\(a\)-sheet periods are

\[
c_-=\frac{\pi i}{p\sqrt{5-4\kappa}},
\]

\[
c_+=\frac{\pi i}{p\sqrt{5+4\kappa}}.
\]

These are the source-derived local covector entries for the pure Cayley–Menger vanishing-cycle block.

## Cancellation locus

The two entries have equal squared magnitude exactly when

\[
5-4\kappa=5+4\kappa,
\]

hence

\[
\kappa=0.
\]

Therefore the equal-weight cancellation of the route packet \((-1,+1)\) is confined to the symmetric slice \(\kappa=0\) at the pure Cayley–Menger level. It is not a generic invariant zero.

## Scope

The full marked source form also contains

\[
\frac{a+p}{2p(a-p)^2(a+3p)(\xi+1)}.
\]

In particular, the negative endpoint carries an additional marked pole. The present calculation does not transport that relative extension and therefore does not yet supply the complete physical endpoint covector or the requested global \(VU-I\) test.

## Narrow conclusion

The physical coefficient architecture already refines the unweighted route packet: the two endpoint occurrences receive source-derived, generally unequal local vanishing-cycle weights. Equality is a symmetry condition, not a property of the Carrier incidence alone.

## Durable artifacts

- `research/benincasa/check_soft_endpoint_vanishing_covector.py`
- `research/benincasa/soft-endpoint-vanishing-covector.json`