# The missing spectral-to-trace edge can be factored into eight nodes with one central operator-realization gap

## Edge

The edge

\[
C_{34}:
V_3
\longrightarrow
V_4
\]

must compare the dual--canonical spectral connection with Connes's semilocal finite-part trace.

Unlike `C_13` and `C_24`, this edge is not already supplied as one complete operator theorem. Its eight-node factorization separates known analytic equalities from the missing realization.

## Node `C_(34,0)`: paired local connection

\[
\boxed{
C_{34,0}
=
(H_S^+,H_S^-,B_S,V_{loc,S}).
}
\]

Here

\[
V_{loc,S}(s)
=
\frac1{2i}
\partial_s\log J_{loc,S}(s).
\]

This is vertex `V_3`.

## Arrow `d_(34,0)`: insert the polarized observer

For the spectral transform of `h=g*g*`, form the paired connection functional

\[
\mathcal L_{S}(h)
=
B_S
\left(
\widehat h,
V_{loc,S}
\right)
\]

with the precise argument placement inherited from the dual/canonical pairing.

## Node `C_(34,1)`: scalar spectral-current pairing

\[
\boxed{
C_{34,1}
=
\langle
\widehat h,
V_{loc,S}
\rangle_{paired}.
}
\]

This is still expressed on the critical spectral line.

## Arrow `d_(34,1)`: expand the logarithmic derivative locally

Decompose

\[
V_{loc,S}
=
V_\infty+
\sum_{p\in S}V_p,
\]

where

\[
V_p(s)
=(\log p)
\sum_{k\ge1}
p^{-k/2}
\cos(ks\log p).
\]

## Node `C_(34,2)`: gamma plus prime-power distribution

\[
\boxed{
C_{34,2}
=
W_\infty^{phase}(h)
+
\sum_{p\in S}
W_p^{powers}(h).
}
\]

This is the Fourier/Mellin expansion of the local scattering phase.

## Arrow `d_(34,2)`: identify with normalized local principal values

Use the local distribution identity

\[
W_v(h)
=
\int_{k_v^*}^{\prime}
\frac{h(u^{-1})}{|1-u|_v}d^*u
\]

with the additive-character normalization whose Fourier transform vanishes at `1`.

For finite primes this is the equivalence between the prime-power series and the local principal-value distribution. For infinity it is the gamma/digamma identity.

## Node `C_(34,3)`: normalized local distributions

\[
\boxed{
C_{34,3}
=
\{W_v(h):v\in S\}.
}
\]

The local pieces are now in the same normalization as Connes's trace theorem.

## Arrow `d_(34,3)`: sum over places

\[
\{W_v(h)
\}_{v\in S}
\longmapsto
W_S(h)
=
\sum_{v\in S}W_v(h).
\]

## Node `C_(34,4)`: semilocal Weil distribution

\[
\boxed{
C_{34,4}=W_S(h).
}
\]

At the scalar distribution level, the spectral route has reached the same local functional as the endpoint of Connes's theorem.

## Arrow `d_(34,4)`: realize the local sum as an orbit-volume defect

Reverse the key step in Connes's proof:

\[
W_S(h)
=
\sum_q
\int
g_q(u)(-\log|u|_S)du.
\]

This step is known as a scalar distribution identity after the local principal-value formulas are summed.

What is not known is a positive or unitary operator map carrying the spectral connection feature to the cutoff orbit-kernel feature before tracing.

## Node `C_(34,5)`: orbit-volume finite-part presentation

\[
\boxed{
C_{34,5}
=
\sum_q
\int
g_q(u)(-\log|u|_S)du.
}
\]

This is the common scalar bridge between the local spectral and cutoff proofs.

## Arrow `d_(34,5)`: restore the cutoff volume and controlled error

Add

\[
2h(1)\log\Lambda
\]

and the rapidly decaying cutoff error to obtain

\[
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h)).
\]

## Node `C_(34,6)`: cutoff trace asymptotic

\[
\boxed{
C_{34,6}
=
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
-
2h(1)\log\Lambda
=
W_S(h)+O(\Lambda^{-N}).
}
\]

## Arrow `d_(34,6)`: take the finite part

\[
\Lambda	o\infty.
\]

## Node `C_(34,7)`: finite-part trace realization

\[
\boxed{
C_{34,7}
=

\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
=
W_S(h).
}
\]

This is vertex `V_4`.

## Seven-arrow summary

\[
\boxed{
\begin{aligned}
d_{34,0}&:
\text{connection}
\to
\text{observer pairing},\\
d_{34,1}&:
\text{pairing}
\to
\text{local logarithmic expansion},\\
d_{34,2}&:
\text{prime powers/gamma}
\to
\text{principal values},\\
d_{34,3}&:
\text{local pieces}
\to
\text{semilocal sum},\\
d_{34,4}&:
\text{local sum}
\to
\text{orbit-volume defect},\\
d_{34,5}&:
\text{orbit defect}
\to
\text{cutoff trace asymptotic},\\
d_{34,6}&:
\text{asymptotic trace}
\to
\text{finite-part trace}.
\end{aligned}
}
\]

## Status audit

### Established at scalar/distribution level

The following are source-backed or direct local calculations:

- logarithmic derivative to gamma/prime-power expansion;
- prime-power expansion to normalized local principal values;
- summation over places;
- orbit-volume identity;
- cutoff asymptotic and finite-part limit.

Thus the scalar endpoints of `C_34` agree.

### Affiliated operator lift now constructed; positive feature lift still missing

Subsequent work identifies the common affiliated operator

\[
\mathcal L_S=M_{-\log|x|_S},
\]

with

\[
V_{loc,S}
\xleftrightarrow{\text{Mellin/Fourier}}
\mathcal L_S
\xrightarrow{\text{observer pairing}}
W_S.
\]

Thus the route no longer has to scalarize immediately between nodes `C_(34,1)` and `C_(34,5)`. What remains absent is a positive Hilbert-feature correspondence from the signed spectral towers of `mathcal L_S` to the noncommuting physical/Fourier cutoff pair, including the Sonin boundary sector.

## Why scalar equality is insufficient

Both routes evaluate to `W_S(h)`, so one can declare `C_34` commutative after applying the scalar trace. Doing so would make the tetrahedral filler tautological and would not prove positivity.

Rung-four requires a lift of the middle square before scalarization:

\[
\begin{matrix}
\text{spectral paired feature}
&\longrightarrow&
\text{local distribution}\\
\downarrow&&\downarrow\\
\text{positive/common bulk feature}
&\longrightarrow&
\text{cutoff orbit feature}.
\end{matrix}
\]

The lower-left common affiliated object is now `mathcal L_S`. The positive vertical maps and Sonin/boundary sewing are what remain to be constructed.

## Polarity

The opposite edge uses

\[
J_{loc,S}^{-1},
\qquad
\widehat P_\Lambda P_\Lambda,
\]

and conjugate principal-value placement. The two scalar finite parts agree after Hermitian polarization, but their feature-level sewing maps need not coincide.

The inner filler must pair these two orientations before taking the trace.

## Disposition

The edge `C_34` has eight explicit nodes and now admits an affiliated/distributional lift through `mathcal L_S` before scalar trace. Its remaining substantive gap is the positive Hilbert-feature lift from the two sign towers of `mathcal L_S` to the orbit/cutoff colligation, including Sonin-sector boundary sewing. This is the exact positive rung-four filler problem.
