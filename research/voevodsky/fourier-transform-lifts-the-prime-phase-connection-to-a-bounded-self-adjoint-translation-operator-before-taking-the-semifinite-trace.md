# Fourier transform lifts the prime-phase connection to a bounded self-adjoint translation operator before taking the semifinite trace

## Spectral prime connection

For one prime `p`, the real spectral connection is

\[
V_p(t)
=(\log p)
\sum_{k\ge1}
p^{-k/2}
\cos(kt\log p).
\]

This series converges absolutely and uniformly on the real line because `p^(-1/2)<1`. Hence `V_p` is a bounded real multiplication operator.

## Fourier lift to logarithmic physical space

Let

\[
\mathcal F:
L^2(\mathbb R_x)
\to
L^2(\mathbb R_t)
\]

be the additive Fourier transform in logarithmic scale, with convention

\[
(\mathcal Ff)(t)
=
\int_\mathbb R
f(x)e^{-itx}dx.
\]

Let

\[
(T_af)(x)=f(x-a)
\]

be translation by `a`. Then

\[
\mathcal FT_a\mathcal F^{-1}
=e^{-iat}.
\]

Therefore multiplication by `cos(at)` is Fourier-conjugate to

\[
\frac12(T_a+T_{-a}).
\]

Define

\[
\boxed{
K_p
=
\mathcal F^{-1}M_{V_p}
\mathcal F
=
\frac{\log p}{2}
\sum_{k\ge1}
p^{-k/2}
\left(
T_{k\log p}+T_{-k\log p}
\right).
}
\]

The series converges in operator norm:

\[
\sum_{k\ge1}
(\log p)p^{-k/2}
<\infty.
\]

Thus

\[
\boxed{
K_p=K_p^*
\in
VN(\mathbb R)
}
\]

is a bounded self-adjoint element of the logarithmic scaling-group von Neumann algebra.

## Complete finite-prime operator

For a finite prime set `S`, define

\[
\boxed{
K_S
=
\sum_{p\in S}K_p.
}
\]

This is bounded and self-adjoint. Every prime and prime power acts in one common translation representation. No prime-labelled Hilbert direct sum is introduced.

Under Fourier transform,

\[
\mathcal FK_S\mathcal F^{-1}
=M_{V_S},
\qquad
V_S=
\sum_{p\in S}V_p.
\]

This is the desired operator-level lift of the spectral pairing connection.

## Semifinite trace pairing

Let

\[
\lambda(h)
=
\int_\mathbb R
h(x)T_xdx
\]

be the convolution operator associated with a suitable logarithmic observer. The Plancherel trace on `VN(R)` satisfies

\[
\tau(\lambda(f))=f(0)
\]

when the expression is defined, and

\[
\tau
\left(
\lambda(h)T_a
\right)
=h(-a)
\]

under the displayed translation convention.

Consequently

\[
\boxed{
\tau
\left(
\lambda(h)K_p
\right)
=
\frac{\log p}{2}
\sum_{k\ge1}
p^{-k/2}
\left[
 h(-k\log p)
+h(k\log p)
\right].
}
\]

This is exactly the real prime-power contribution in logarithmic coordinates, up to the global sign and Haar/Fourier normalization of the explicit formula.

Thus the map

\[
M_{V_p}
\longmapsto
K_p
\]

followed by `tau(lambda(h)-)` reproduces the local prime distribution without scalarizing at the Fourier-transform step.

## Convolution-square observer

For

\[
h=g*g^*,
\]

one has

\[
\lambda(h)
=
\lambda(g)\lambda(g)^*
\succeq0.
\]

The prime functional is

\[
\tau
\left(
\lambda(g)\lambda(g)^*K_p
\right).
\]

Because `K_p` is self-adjoint but not positive, this trace has no fixed sign. Nevertheless it is now a correctly typed operator pairing inside one semifinite von Neumann algebra.

## Positive Poisson decomposition at operator level

Let

\[
U_p=T_{\log p},
\qquad
r=p^{-1/2}.
\]

The operator-valued Poisson kernel is

\[
\mathcal P_{p}
=
(1-r^2)
(I-rU_p)^{-1}
(I-rU_p^*)^{-1}
\succeq0.
\]

Its norm-convergent Fourier series is

\[
\mathcal P_p
=
I+

\sum_{k\ge1}
r^k(U_p^k+U_p^{*k}).
\]

Therefore

\[
\boxed{
K_p
=
\frac{\log p}{2}
(\mathcal P_p-I).
}
\]

This is the physical-space operator version of the positive Poisson density minus Plancherel baseline.

## Embedding into the semilocal scaling representation

The logarithmic module map

\[
C_S
\longrightarrow
\mathbb R
\]

identifies the continuous scaling direction. The translations `T_(k log p)` are the images of the semilocal idele-class scaling elements corresponding to the local idele classes `iota_p(p^k)`, with `p^k` in the `p`-component and `1` elsewhere. The diagonal rational `p^k` itself is an `S`-unit and becomes trivial in the quotient, so this local embedding must be retained.

Hence `K_p` can be represented intrinsically as

\[
\boxed{
K_p
=
\frac{\log p}{2}
\sum_{k\ge1}
p^{-k/2}
\left(
U_S(\iota_p(p^k))+
U_S(\iota_p(p^{-k}))
\right)
}
\]

on the `K_S`-invariant semilocal carrier, subject to the source normalization of the scaling representation.

This places the prime phase directly inside the same operator algebra used by Connes's cutoff trace.

## Candidate operator lift of `C_34`

The previously missing middle arrow can now be factored as

\[
\boxed{
M_{V_S}
\xrightarrow{\mathcal F^{-1}(-)\mathcal F}
K_S
\xrightarrow{\tau_S(U_S(h)-)}
W_S^{finite}(h).
}
\]

The first arrow is unitary Fourier conjugation and preserves adjoints. The second is the semifinite Plancherel pairing.

For finite primes, this is a genuine feature/operator lift before the scalar trace.

## Archimedean extension

The gamma connection `V_infinity(t)` is real but unbounded, growing logarithmically. Fourier conjugation defines a self-adjoint operator or distribution

\[
K_\infty
=
\mathcal F^{-1}
M_{V_\infty}
\mathcal F
\]

affiliated with the scaling-group von Neumann algebra rather than a bounded element.

To complete `C_34`, one must specify a common form domain and prove that

\[
\tau_S
\left(
U_S(h)K_\infty
\right)
\]

equals the normalized archimedean principal value. This is the operator-domain counterpart of the known gamma distribution identity.

## Relation to Connes's cutoff trace

Connes's theorem gives

\[
W_S(h)
=
\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h)).
\]

The Fourier lift gives, for the finite-prime sector,

\[
W_S^{finite}(h)
=
\tau_S
\left(
U_S(h)K_S
\right)
\]

up to source signs and normalizations.

Thus the remaining operator comparison is reduced from an unspecified feature map to the relative trace identity

\[
\boxed{

\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
=
	au_S
\left(
U_S(h)(K_\infty+K_S)
\right)
+
E_{end}(h).
}
\]

The scalar equality follows from the explicit formula; proving it as equality of relative trace pairings with controlled domains is the remaining lift.

## Positivity status

The construction solves the operator-typing gap for finite primes but not positivity:

\[
K_p
=
\frac{\log p}{2}
(\mathcal P_p-I)
\]

is signed. With the hostile explicit-formula orientation, the positive Poisson operator appears with a negative sign.

A positive filler must combine the full operator family

\[
K_\infty+
\sum_pK_p+
K_{end}
\]

before applying the observer trace.

## Disposition

The finite-prime part of the missing `C_34` operator lift exists explicitly:

\[
\boxed{
K_S
=
\frac12
\sum_{p\in S}
(\log p)
\sum_{k\ge1}
p^{-k/2}
\left(
U_S(\iota_p(p^k))+
U_S(\iota_p(p^{-k}))
\right).
}
\]

Its semifinite trace pairing with `U_S(h)` is the prime-power Weil distribution. The unresolved portions are the affiliated archimedean operator, endpoint boundary operator, and positive factorization of their completed sum.
