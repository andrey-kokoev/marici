# Volterra history couples both reciprocal theta channels exactly

## Causal and anti-causal histories

On a rapidly decreasing bilateral source function \(g\), define

\[
(H_+g)(u)=\int_{-\infty}^{u}g(v)\,dv,
\qquad
(H_+^{*}g)(u)=\int_u^{\infty}g(v)\,dv.
\]

Their even and odd combinations are

\[
S=\frac{H_++H_+^{*}}2,
\qquad
T=\frac{H_+-H_+^{*}}2.
\]

Reflection exchanges \(H_+\) and \(H_+^{*}\), hence \(S\) is reciprocal-even and \(T\) is reciprocal-odd.

Let \(\Phi\) be the bilateral completed theta forcing and set

\[
m=\int_{\mathbb R}\Phi(u)\,du,
\qquad
F(u)=\int_{-\infty}^{u}\Phi(v)\,dv.
\]

Then

\[
S\Phi=\frac m2,
\qquad
T\Phi=F-\frac m2.
\]

Because \(\Phi\) is even, \(T\Phi\) is odd.

## Exact even incidence

The even channel has scalar incidence

\[
c_+
=
\langle \Phi,S\Phi\rangle
=
\frac{m^2}{2}.
\]

Thus it is nonzero whenever the bilateral mass \(m\) is nonzero.

## Exact odd incidence

The reciprocal-odd source vector is \(\Phi'\). Its causal incidence is

\[
c_-
=
\langle \Phi',T\Phi\rangle.
\]

Since \((T\Phi)'=\Phi\), integration by parts gives

\[
c_-
=
-\int_{\mathbb R}\Phi(u)^2\,du
=
-\|\Phi\|_2^2.
\]

The boundary term vanishes because \(\Phi'\) decays and \(T\Phi\) is bounded. Therefore

\[
c_-<0
\]

for every nonzero real theta forcing. The odd channel cannot be dark.

This identity is stronger than a generic nonvanishing argument: it fixes the sign and magnitude by a source square law.

## Consequences for the Schur cell

The minimal reflection-equivariant incidence coefficients are now

\[
c_+=\frac{m^2}{2},
\qquad
c_-=-\|\Phi\|_2^2.
\]

Hence the induced odd Schur coordinate has sign

\[
\operatorname{sgn}h
=
-\operatorname{sgn}\tau
\]

under the previously frozen ordering, while its magnitude is

\[
|h|
=
\frac{m^2\|\Phi\|_2^2}{2}
\frac{|\tau|}{s_+s_--\tau^2}.
\]

The exact sign must still be compared with the Euler and Wronskian conventions.

## Analytic qualification

The constant function \(S\Phi=m/2\) is not in unweighted \(L^2(\mathbb R)\). Thus \(S\) belongs naturally to the wall-extended or rigged history space, not to the ordinary Hilbert carrier. This is consistent with the earlier result that the constant wall is a coefficient direction represented by an identity-type noncompact operator.

The odd history \(T\Phi\) approaches \(\pm m/2\) at the two ends and is likewise a relative boundary object. Its derivative is Hilbert:

\[
(T\Phi)'=\Phi\in L^2.
\]

Therefore the exact incidences are relative Green pairings. Treating them as ordinary \(L^2\) operator matrix elements would mistype the construction.

## Next gate

Build the wall-extended Sobolev history space in which \(S\Phi\) and \(T\Phi\) are legitimate relative classes, and prove the two identities survive closure and Mellin transport. The finite incidence-rank defect itself is closed.
