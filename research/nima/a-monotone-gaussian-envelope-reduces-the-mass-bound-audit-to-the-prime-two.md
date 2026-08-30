# A monotone Gaussian envelope reduces the mass-bound audit to the prime two

## Common Gaussian coordinate

Let

\[
L=\log p,
\qquad
A(L)
=
\int_{-L/2}^{L/2}e^{-\pi x^2}\,dx,
\qquad
T(L)=1-A(L).
\]

Both quantities are explicit:

\[
A(L)
=
\operatorname{erf}
\left(
\frac{\sqrt\pi L}{2}
\right).
\]

The function \(A\) is increasing and \(T\) is decreasing.

## Endpoint lower envelope

For \(|q|\le L/2\), the window interval

\[
[q-L,q+L]
\]

contains \([-L/2,L/2]\). Therefore

\[
|W_L(q)|\ge A(L).
\]

The Stieltjes measure of the same central region is also \(A(L)\). Hence

\[
a_p
=
\int_{\mathbb R}|W_L(q)|^2e^{-\pi q^2}\,dq
\ge
A(L)^3.
\]

This is a fully explicit lower envelope requiring no quadrature.

## Disagreement upper envelope

The established core-tail split gives

\[
\|d_p\|_\nu^2
\le
T(L)^2+T(L).
\]

Consequently the theta-mass Schur certificate

\[
\|d_p\|_\nu^2
<
8(1-M_\Phi)^2a_p
\]

follows from the scalar inequality

\[
T(L)^2+T(L)
<
8(1-M_\Phi)^2A(L)^3.
\]

The left side decreases with \(L\), while the right side increases.
Therefore this sufficient envelope, once true at one value \(L_0\), remains
true for all \(L\ge L_0\).

## Prime-three threshold

Set

\[
L_0=log3.
\]

The threshold check becomes the single explicit inequality

\[
[1-A(\log3)]^2+[1-A(\log3)]
<
8(1-M_\Phi)^2A(\log3)^3,
\]

with

\[
M_\Phi
=
\xi\!\left(\frac12\right)
\approx0.497120778.
\]

Direct interval evaluation of the error function certifies this inequality
with a wide margin. Monotonicity then proves the Schur mass-bound certificate
for every prime

\[
p\ge3.
\]

Thus only \(p=2\) lies outside this analytic envelope.

## Remaining finite calculation

At \(p=2\), one should evaluate rigorous enclosures for

\[
a_2
=
\int_{\mathbb R}
|W_{\log2}(q)|^2e^{-\pi q^2}\,dq
\]

and

\[
d_2^2
=
\int_{\mathbb R}
|W_{2\log2}(q)-W_{\log2}(q)|^2
e^{-\pi q^2}\,dq.
\]

The sufficient test is

\[
d_2^2
<
8(1-M_\Phi)^2a_2.
\]

This is one certified Gaussian integral comparison, not a search over primes.

## Rigorous quadrature protocol

A proof-producing computation may:

1. choose \(Q>0\);
2. integrate on \([-Q,Q]\) using interval arithmetic;
3. bound both tails by explicit Gaussian estimates;
4. enclose \(M_\Phi\) from its source theta formula;
5. compare disjoint rational intervals for the two sides.

No floating-point sample without outward error control is sufficient for the
final theorem.

## Exact-symbol fallback

If the coarse mass test fails at \(p=2\), this does not imply Schur failure.
The exact quantity is

\[
q_{2,\pm}
=
2\int
\frac{|\widehat d_2(\xi)|^2}
{|1\pm im(\xi)|^2}
\,d\xi.
\]

A certified symbol-weighted integral can exploit spectral alignment discarded
by the uniform inverse bound.

## Constructor qualification

The numerical reduction remains conditional on:

- identification of \(d_p\) with the source odd incidence;
- exact shifted-history normalization;
- reciprocal character selection through \(j_\theta\);
- prime-diagonal completion.

The calculation certifies a margin; it does not create these constructors.

## Verdict

A monotone Gaussian envelope removes every prime except two from the local
Schur-survival audit. The only unresolved numerical inequality in the
theta-mass route is the explicit \(p=2\) Gaussian comparison.

This is the smallest possible finite pilot for the first enlarged Adams cell.
