# The raw prime-delay Cayley law has the wrong late-shell order to be the diagonal reciprocal response coefficient

## Question

Can the existing strict prime-delay Cayley law be used directly as the missing
diagonal reciprocal shell coefficient?

## Claim boundary

No. After removal of its constant phase, its first correction has Euler
half-density order \(p^{-1/2}\), while the required correction to the full
endpoint jet has order \(\Lambda(\log p)^{-1}\sim p^{-2}\). The raw Cayley law
may remain a zero-free arithmetic complement. A graded source totalization
could alter the comparison only if it explicitly cancels the intervening
orders.

## Prime-delay law

In the centered chart, the prime delay is

\[
 S_p(z)=p^{-1/2}e^{i(\log p)z}.
\]

The source Cayley impedance is

\[
 \Theta_p(z)
 =i\frac{1+S_p(z)}{1-S_p(z)}.
\]

For large \(p\),

\[
 \Theta_p(z)
 =i\left(1+2S_p(z)+2S_p(z)^2+O(S_p(z)^3)\right).
\]

After dividing by the constant phase \(i\), the first nonconstant term is

\[
 2p^{-1/2}e^{i(\log p)z}.
\]

## Required diagonal multiplier

The completed-theta late-shell calculation requires, relative to the full
curvature-aware endpoint jet,

\[
 1-\frac{1}{2\Lambda(\log p)}
 +O(\Lambda(\log p)^{-2}).
\]

Since

\[
 \Lambda(\log p)=2\pi p^2-\frac92+O(p^{-2}),
\]

this is

\[
 1-\frac{1}{4\pi p^2}+O(p^{-4}).
\]

Its first correction is order \(p^{-2}\) and has no leading oscillatory
factor in \(z\).

## Order mismatch

The normalized raw Cayley correction is order \(p^{-1/2}\), larger than the
required correction by a factor of order \(p^{3/2}\). Its parameter dependence
also carries the delay character \(e^{i(\log p)z}\).

No fixed phase or reciprocal sign changes either the power of \(p\) or the
delay character. Therefore the raw Cayley impedance cannot be the diagonal
shell multiplier.

## Graded qualification

The Euler filtration separates:

- primitive order;
- square order;
- connected grades beginning at order three;
- the order-three regularized determinant.

A larger constitutive compiler might cancel or relocate lower delay orders
before producing a diagonal boundary coefficient. Such a compiler must show
those cancellations at the operator or determinant-line level. They cannot be
assumed from the existence of \(\Theta_p\).

In particular, calling the strict Cayley law a passive realization proves
half-plane orientation and zero-free complement control, not the required
shell response normalization.

## Relation to existing no-go results

This asymptotic mismatch is consistent with two established facts:

1. strict same-sign passive complements cannot create the Xi seam divisor;
2. rigid two-by-two reciprocal sewing does not make its determinant equal Xi.

The present result is narrower: even as a response coefficient rather than a
divisor compiler, the unmodified prime-delay Cayley law has the wrong late-shell
order.

## Minimal hostile

Normalize any proposed Cayley-derived coefficient by its constant phase and
expand at one late prime. If a nonzero \(p^{-1/2}\), \(p^{-1}\), or
\(p^{-3/2}\) term survives, it cannot equal the required endpoint-relative
multiplier through order \(p^{-2}\).

## Disposition

The prime-delay Cayley law remains admissible as the arithmetic complement but
is rejected as the raw diagonal reciprocal shell coefficient. Candidate one
still requires a source-derived graded endpoint or constitutive response whose
first surviving correction is \(-1/(4\pi p^2)\). No RH conclusion is
authorized.
