# All-Prime Positive Sieving Is the First Arithmetic Law the Gaussian Hostile Cannot Imitate

## Exact theta sieve operators

The labelled theta cells satisfy

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n),
\qquad
\Phi(u)=\sum_{n\ge1}\phi_n(u).
\]

For each prime \(p\), define

\[
D_p=I-p^{-1/2}T_{\log p},
\qquad
(T_Lf)(u)=f(u+L).
\]

Then

\[
p^{-1/2}T_{\log p}\Phi
=
\sum_{p\mid n}\phi_n,
\]

and therefore

\[
D_p\Phi
=
\sum_{p\nmid n}\phi_n
>0.
\]

The positivity is not an estimate. It is exact label deletion.

## Iterated sieve

For a finite prime set \(S\), the operators commute and

\[
\prod_{p\in S}D_p\Phi
=
\sum_{\gcd(n,\prod_{p\in S}p)=1}\phi_n
>0.
\]

As \(S\) exhausts the primes, these positive remainders decrease pointwise to
the primitive cell

\[
\phi_1.
\]

Thus theta carries a complete positive sieve resolution indexed by the prime
semilattice. It retains which labels were deleted at every stage.

## Gaussian hostile failure

Let

\[
G(u)=\sum_{j=1}^r c_j e^{-\alpha_j u^2},
\qquad c_j,\alpha_j>0.
\]

For every \(L>0\),

\[
\frac{G(u+L)}{G(u)}\longrightarrow\infty
\qquad (u\to-\infty).
\]

The slowest-decaying Gaussian controls the ratio, whose leading exponential
is \(e^{-2\alpha Lu}\). Hence, for every prime \(p\),

\[
G(u)-p^{-1/2}G(u+\log p)<0
\]

on a sufficiently negative tail.

The positive two-Gaussian pointed source from the preceding packet therefore
fails the first prime sieve gate despite passing positivity, heat, symmetry,
and conormal tests.

## Explanatory gain

This is the first property in the current chain that is both:

- derived from the labelled arithmetic source;
- and absent from the explicit positive off-seam hostile.

It separates theta from generic positive heat seeds by an operation law, not
by naming the desired function.

## Remaining gate

Positive sieving does not yet imply critical-line support. The next theorem
must determine whether the complete commuting family \(\{D_p\}\), together
with Poisson reflection and the moving endpoint, yields a variation-diminishing
or collision-exclusion law after Fourier–Mellin transport.

A new hostile source that admits the entire positive sieve resolution while
retaining off-seam zeros would close this route decisively.
