# Theta prime-interval incidence divergence is entirely the old half-amplitude direction

## Status

Exact completion decomposition under the standard theta tail bound. Raw
prime-power interval currents reproduce the primitive, square, and trace-class
tail filtration because every long interval current tends to the same
half-amplitude.

After subtracting that common half-amplitude, the genuinely new interval
remainder is a translated theta tail and is absolutely summable even in the
primitive channel. Thus the (k=1\) and (k=2\) divergences occupy an old
rank-one amplitude direction; the new boundary-incidence information has a
much better completion class.

## Interval and tail decomposition

Let

\[
H_A(z)=\int_0^\infty A(v)e^{izv}\,dv
\]

and

\[
B_\ell[A](z)=\int_0^\ell A(v)e^{izv}\,dv.
\]

Define the centered interval current

\[
\widetilde B_\ell[A](z)
=B_\ell[A](z)-H_A(z).
\]

Then

\[
\widetilde B_\ell[A](z)
=-\int_\ell^\infty A(v)e^{izv}\,dv.
\]

For the prime-power displacement \(\ell_{p,k}=k\log p\),

\[
B_{p,k}=H_A+\widetilde B_{p,k}.
\]

The first term is independent of (p\) and (k\); all typed interval geometry
resides in the second.

## Theta-tail estimate

The completed theta half-source has super-exponential scale decay. On every
fixed vertical strip in (z\), one may bound it in the form

\[
|A(v)e^{izv}|
\leq C_R e^{-c e^{2v}}
\]

for (v\geq0\) and \(|\operatorname{Im}z|\leq R\), after adjusting constants.

Therefore

\[
|\widetilde B_{p,k}(z)|
\leq
C_R'
e^{-c' p^{2k}}
\]

uniformly on compact vertical strips. Any harmless polynomial factor in
(p\), (k\), or \(\log p\) is absorbed by this decay.

## Logarithmic-derivative weights

For the completed logarithmic-derivative current, the prime-power coefficient
has the von Mangoldt scale

\[
w_{p,k}^{\mathrm{LD}}
=(\log p)p^{-k/2}.
\]

The raw interval sum at fixed (k\) is

\[
\sum_p w_{p,k}^{\mathrm{LD}}B_{p,k}
=H_A\sum_p(\log p)p^{-k/2}
+\sum_p(\log p)p^{-k/2}\widetilde B_{p,k}.
\]

The first sum has the familiar filtration:

- (k=1\): divergent primitive current;
- (k=2\): divergent prime-square current;
- (k\geq3\): absolutely convergent tail.

The centered second sum converges absolutely for every (k\geq1\) because of
the super-exponential factor (e^{-c'p^{2k}}\).

## Euler-log weights

For the logarithm of the Euler product, the coefficients instead have scale

\[
w_{p,k}^{\log}
=\frac1k p^{-k/2}.
\]

The same classification holds:

- the common-amplitude component diverges for (k=1\) and (k=2\);
- it converges for (k\geq3\);
- every centered interval remainder converges absolutely.

Thus the conclusion is independent of which of the two standard arithmetic
normalizations is being typed.

## Rank-one nature of the divergence

At a finite cutoff (P\), write

\[
\mathcal I_{k,P}(z)
=\sum_{p\leq P}w_{p,k}B_{p,k}(z).
\]

Then

\[
\mathcal I_{k,P}(z)
=c_{k,P}H_A(z)+\widetilde{\mathcal I}_{k,P}(z),
\]

where

\[
c_{k,P}=\sum_{p\leq P}w_{p,k}
\]

and \(\widetilde{\mathcal I}_{k,P}\) converges as (P\to\infty\).

All divergent cutoff dependence is scalar multiplication of the existing
half-amplitude row. The new interval-incidence quotient has a finite limit.

## Coupled completion requirement

The divergent (H_A\) direction cannot be deleted. It must combine with the
endpoint, gamma, and reciprocal channels through the already known completed
coherence relation. Removing it from the primitive or square current alone
would change every finite Euler cutoff.

The correct completed object therefore retains:

1. the typed divergent coefficient (c_{k,P}\) multiplying (H_A\);
2. the convergent centered incidence \(\widetilde{\mathcal I}_k\);
3. the endpoint–gamma countercurrent that completes the common amplitude;
4. the finite-cutoff reconstruction identity.

This is a relative completion, not separate regularization of positive ports.

## Reciprocal channels

The reciprocal centered current is

\[
\widetilde B_{p,k}(-z)
=-\int_{k\log p}^{\infty}A(v)e^{-izv}\,dv.
\]

For real (A\) on the seam, it is conjugate to the positive-sheet current. Off
the seam, the two centered sums remain separately convergent but no universal
relative phase is fixed.

Completion therefore exists before orientation.

## Finite falsifiers

Any proposed completion fails if:

- it assigns the primitive or square divergence to the centered interval tail;
- it discards the common (H_A\) direction instead of coupling it to completion;
- it merges logarithmic-derivative and Euler-log weights;
- it loses the finite-cutoff identity
  \(B_{p,k}=H_A+\widetilde B_{p,k}\);
- it infers a sign for the convergent complex centered current from source
  positivity alone.

The smallest numerical audit is to compare the raw interval current with
(H_A\) as (p\) grows; their difference must exhibit theta-tail decay.

## Consequence

The missing finite incidence map extends farther than expected. Its genuinely
new boundary information is already completion-safe across primitive, square,
and higher prime-power channels. The only non-trace-class behavior is the old
half-amplitude direction repeated with divergent arithmetic multiplicity.

The decisive next question is whether the convergent centered incidence adds
observation rank after reciprocal sewing and completed endpoint–gamma coupling.
If it does not, the multiplicative boundary branch closes as another graph
extension. If it does, its finite matrix against the transverse (X/Y\) channel
is the first plausible nonlocal orientation port.
