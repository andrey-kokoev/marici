# The semilocal geometry-to-trace edge has an eight-node factorization following Connes Theorem 4

## Edge

The conductor edge

\[
C_{24}:
V_2
\longrightarrow
V_4
\]

connects the semilocal geometric presentation to the finite-part trace presentation.

Fix a finite place set `S`, an observer `h`, and a cutoff parameter `Lambda`. The proof of Connes's semilocal Theorem 4 gives a natural eight-node factorization.

## Node `C_(24,0)`: semilocal geometric data

\[
\boxed{
C_{24,0}
=
(X_S,C_S,L^2(X_S),U_S,F_S).
}
\]

This contains the semilocal adele-class space, scaling representation, and Fourier transform.

No observer operator or cutoff has yet been inserted.

## Arrow `d_(24,0)`: integrate the observer

For compactly supported `h` on the semilocal idele class group, define

\[
U_S(h)
=
\int_{C_S}h(g)U_S(g)d^*g.
\]

For `h=g*g*`,

\[
U_S(h)
=
U_S(g)U_S(g)^*
\succeq0.
\]

## Node `C_(24,1)`: integrated scaling operator

\[
\boxed{
C_{24,1}
=
(L^2(X_S),U_S(h)).
}
\]

This is the positive observer insertion before cutoff.

## Arrow `d_(24,1)`: descend to the quotient kernel

Choose a compactly supported lift `f` on the semilocal ideles whose sum over `S`-units represents `h`. Write the Schwartz kernel of `U_S(f)` on the additive semilocal space and descend it to `X_S` by the orbit sum.

## Node `C_(24,2)`: orbit-kernel presentation

\[
\boxed{
C_{24,2}
=
K_{S,h}(x,y)
}
\]

with quotient trace rule

\[
\operatorname{Tr}(T)
=
\sum_{q\in O_S^*}
\int_D
K_T(x,qx)dx.
\]

This is the geometric fixed-orbit presentation used in the proof.

## Arrow `d_(24,2)`: impose the physical/Fourier cutoff pair

Define

\[
P_\Lambda
=1_{\{|x|\le\Lambda\}},
\qquad
\widehat P_\Lambda
=F_SP_\Lambda F_S^{-1},
\]

and

\[
R_\Lambda
=P_\Lambda\widehat P_\Lambda.
\]

Insert the transpose kernel of `R_Lambda` in the quotient trace calculation.

## Node `C_(24,3)`: product-cutoff operator

\[
\boxed{
C_{24,3}
=
R_\Lambda U_S(h)
=
P_\Lambda\widehat P_\Lambda U_S(h).
}
\]

This is generally trace class in the theorem's regulated setting, but it is not positive because `P_Lambda hat P_Lambda` is not self-adjoint.

This is the first node at which positivity of `U_S(g)U_S(g)*` is no longer manifest.

## Arrow `d_(24,3)`: take the ordinary regulated trace

\[
R_\Lambda U_S(h)
\longmapsto
\operatorname{Tr}
(R_\Lambda U_S(h)).
\]

## Node `C_(24,4)`: scalar cutoff trace

\[
\boxed{
C_{24,4}
=
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h)).
}
\]

This is the scalar expression to which the orbit-kernel calculation applies.

## Arrow `d_(24,4)`: subtract the canonical volume density

The Plancherel trace on the scaling-group von Neumann algebra satisfies

\[
\tau_S(\lambda_S(h))
=h(1).
\]

Define

\[
\mathfrak T_{\Lambda,S}(h)
=
C_{24,4}
-
2\log\Lambdah(1).
\]

## Node `C_(24,5)`: relative cutoff trace

\[
\boxed{
C_{24,5}
=
\mathfrak T_{\Lambda,S}(h).
}
\]

This is the trace relative to the canonical scaling-volume density. It is signed.

## Arrow `d_(24,5)`: orbit-volume decomposition

The proof evaluates the cutoff orbit volume as

\[
2\log\Lambda-\log|u|_S.
\]

After the volume subtraction, decompose

\[
-\log|u|_S
=
\sum_{v\in S}
-\log|u_v|_v
\]

and use the local principal-value identity at each place.

## Node `C_(24,6)`: local Weil sum plus controlled error

\[
\boxed{
C_{24,6}
=
W_S(h)+
\operatorname{Err}_{\Lambda,S}(h),
}
\]

where

\[
W_S(h)
=
\sum_{v\in S}
\int_{k_v^*}^{\prime}
\frac{h(u^{-1})}{|1-u|_v}d^*u.
\]

Lemma 2 in the proof gives

\[
\operatorname{Err}_{\Lambda,S}(h)
=
O(\Lambda^{-N})
\]

for every `N`, with constants depending on the test data.

## Arrow `d_(24,6)`: remove the cutoff

Take

\[
\Lambda	o\infty.
\]

The rapidly decaying error vanishes.

## Node `C_(24,7)`: finite-place Weil functional

\[
\boxed{
C_{24,7}
=
W_S(h).
}
\]

This is the trace vertex `V_4` in its local Weil presentation.

## Complete edge factorization

The seven arrows are

\[
\boxed{
\begin{aligned}
d_{24,0}&:
\text{geometry}
\to
\text{integrated observer},\\
d_{24,1}&:
\text{observer}
\to
\text{quotient kernel},\\
d_{24,2}&:
\text{kernel}
\to
\text{product cutoff},\\
d_{24,3}&:
\text{cutoff operator}
\to
\text{ordinary trace},\\
d_{24,4}&:
\text{trace}
\to
\text{relative trace},\\
d_{24,5}&:
\text{relative trace}
\to
\text{local Weil sum plus error},\\
d_{24,6}&:
\text{asymptotic local sum}
\to
\text{Weil functional}.
\end{aligned}
}
\]

## Positive counterplane

There is a natural alternative at node `C_(24,3)`. Replace

\[
P_\Lambda\widehat P_\Lambda
\]

by the positive triple compression

\[
P_\Lambda\widehat P_\Lambda P_\Lambda
\succeq0.
\]

For a convolution square,

\[
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda P_\Lambda
U_S(g)U_S(g)^*)
=
\|
\widehat P_\Lambda P_\Lambda U_S(g)
\|_{HS}^2.
\]

Thus `C_24` has two natural planes:

1. the source trace plane through `P hat P`;
2. the positive Gram plane through `P hat P P`.

Their comparison is the infinite-rank sewing remainder

\[
P_\Lambda\widehat P_\Lambda
(I-P_\Lambda).
\]

This is the local location of the rung-four filler problem.

## Alignment test for the other edges

The stages on `C_24` have the global semantic labels

\[
\boxed{
\text{geometry},
\text{observer},
\text{kernel},
\text{cutoff},
\text{trace},
\text{renormalization},
\text{localization},
\text{limit}.
}
\]

For a uniform edgewise-subdivision model, every other conductor edge must admit compatible restrictions of these eight stages. This is not automatic:

- `C_13` naturally has spectral-transform and phase stages rather than quotient-kernel stages;
- `C_23` is unitary and has no obvious volume subtraction;
- `C_34` is precisely the missing comparison between spectral phase and cutoff localization.

Therefore this factorization is source-backed on `C_24`, but it already suggests that a uniform eight-stage labeling across all six edges may require a common refinement with more than eight nodes or degeneracy nodes on some edges.

## Disposition

The edge `C_24` has a genuine eight-node, seven-arrow factorization extracted from the proof of Connes's theorem. Its source and positive counterplanes separate at the product-cutoff node. The next step is to factor `C_13` into the same semantic stages and identify which stages are identities, which require refinement, and which expose the missing `C_34` filler.
