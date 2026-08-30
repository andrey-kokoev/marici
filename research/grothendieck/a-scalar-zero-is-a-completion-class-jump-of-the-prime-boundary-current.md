# A scalar zero is a completion-class jump of the prime boundary current

## Bounded question

Do the primitive, prime-square, and connected prime-translation boundary
currents leave a finite cocycle anomaly, or does their first nontrivial effect
occur only at restricted-product completion?

## Prime-translation boundary cocycle

For a completed half-line source (A), define

\[
B_\ell^+(z)
=
\int_0^\ell A(v)e^{izv}\,dv,
\qquad
B_\ell^-(z)=B_\ell^+(-z).
\]

Forward translation by (ell) satisfies

\[
\mathcal M_+[S_\ell A](z)
=
e^{-iz\ell}
\left[H_+(z)-B_\ell^+(z)\right].
\]

The boundary port obeys the exact cocycle

\[
B_{\ell_1+\ell_2}^+[A]
=
B_{\ell_1}^+[A]
+e^{iz\ell_1}B_{\ell_2}^+[S_{\ell_1}A].
\]

## Every finite prime square closes

For (ell_p=\log p) and (ell_q=\log q), the two staged paths both equal

\[
B_{\ell_p+\ell_q}^+[A].
\]

The paths partition the same interval in different orders. Their typed pieces
are related by canonical resegmentation, and their aggregate residual is
exactly zero. Since prime translations commute and

\[
QS_pS_q=p^2q^2S_pS_qQ,
\]

the mixed Gaussian--valuation square also has no finite braid anomaly.

Thus no finite prime set can supply the missing obstruction through cocycle
failure.

## Reciprocal boundary current

Let

\[
X(z)=H_+(z)+H_+(-z)
\]

be the completed symmetric scalar readout. Define the reciprocal boundary
packet at prime-power depth (k) by

\[
C_{k,p}(z)
=
p^{-k/2}
\left[
B_{k\log p}^+(z)+B_{k\log p}^+(-z)
\right].
\]

Because the completed Gaussian source decays faster than every exponential,

\[
B_{k\log p}^+(z)
=
H_+(z)+O_N(p^{-Nk})
\]

for every (N>0), locally uniformly in (z). Hence

\[
C_{k,p}(z)
=
p^{-k/2}X(z)
+O_N\left(p^{-k(N+1/2)}\right).
\]

## Exact completion classes

Summing over primes gives three regimes.

For the primitive channel,

\[
\sum_{p\le P}C_{1,p}(z)
=
X(z)\sum_{p\le P}p^{-1/2}+O(1).
\]

For the prime-square channel,

\[
\sum_{p\le P}C_{2,p}(z)
=
X(z)\sum_{p\le P}p^{-1}+O(1).
\]

For every (k\ge3), the prime sum converges absolutely.

Therefore

\[
X(z)=0
\]

is equivalent to convergence of the reciprocal primitive current and also to
convergence of the reciprocal prime-square current. When (X(z)\ne0), their
partial sums diverge with the displayed source-fixed leading coefficient.

## Result

The scalar completed readout is exactly the obstruction coefficient for the
two exceptional completion levels:

1. (k=1) is distributional because its leading coefficient multiplies
   (sum_pp^{-1/2});
2. (k=2) is non-trace-class because its leading coefficient multiplies
   (sum_pp^{-1});
3. (k\ge3) is ordinarily summable;
4. at a scalar zero, the leading obstruction disappears and the first two
   currents upgrade to the summable class.

A zero is therefore not merely loss of one scalar projection. It is a precise
change in the regularity type of the global reciprocal boundary current.

## Explanatory boundary

This theorem does not confine the class jump to the critical line. It explains
what changes at every zero. RH now asks for a source-derived reason why this
completion-class upgrade can occur only where the two Tate sectors are
unitarily sewn.

The next theorem should compare the upgraded (k=1) and (k=2) limits under
the two sector orientations. A source law forcing their limiting values to be
adjoints only on (operatorname{Re}s=1/2) would convert the regularity jump
into zero confinement. A hostile off-seam source whose exceptional currents
also converge with the required adjoint relation would falsify that route.
