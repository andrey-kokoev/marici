# 2887 — The Internal Bypass Survives as a Deck-Anti-Invariant Gysin-Kernel Line

## Full marked occurrence divisor

On the compact elliptic fiber, retain the four labelled marked points

\[
D=
\{(1,+),(1,-),(-3,+),(-3,-)\}.
\]

The signs label the two square-root sheets. The source differential has
residue vector

\[
\mathbf R=(R_1,-R_1,R_3,-R_3),
\]

where

\[
R_1
=
\frac{(\kappa+\xi)^2+2(1+\kappa\xi)}
{64p^4(\xi+1)(\kappa+\xi)^3},
\]

and

\[
R_3
=
-\frac1{64p^4(\xi+1)(\kappa-\xi)}.
\]

## Gysin kernel

For four marked points on the compact connected fiber, the point-to-fundamental
class Gysin map is

\[
\operatorname{Gys}
=
\begin{pmatrix}1&1&1&1\end{pmatrix}.
\]

It has rank one and kernel rank three. One exact integral basis is

\[
\begin{aligned}
e_{1,-}&=(1,-1,0,0),\\
e_{3,-}&=(0,0,1,-1),\\
e_{13}&=(1,1,-1,-1).
\end{aligned}
\]

The global residue theorem is explicit:

\[
\operatorname{Gys}(\mathbf R)=0.
\]

## Internal bypass class

Entry 2885's internal tube is the line

\[
\mathcal L_{\rm bypass}
=
\mathbb Q\langle(1,-1,0,0)\rangle
\subset
\ker(\operatorname{Gys}).
\]

Therefore it is not killed by the generic occurrence-resolved Gysin
totalization.

The deck trace does kill it:

\[
(1,-1,0,0)
\longmapsto
1-1=0.
\]

But the physical positive-occurrence covector

\[
(1,0,0,0)
\]

detects it. Deck trace and physical chamber evaluation are thus inequivalent
readouts.

## Narrow conclusion

The internal bypass packet survives generically as a deck-anti-invariant
relative coefficient line. It becomes invisible only after an additional
coarse deck trace, not through the occurrence-resolved Gysin kernel itself.

This is a coefficient/readout distinction over existing marked carrier
support. It does not require a new carrier stratum.

## Remaining gate

Derive the Gauss–Manin transport of this rank-one kernel line through the full
base puncture atlas. Determine whether the line is horizontal by itself or
mixes with the other two Gysin-kernel directions.

## Durable artifacts

- `research/benincasa/check_soft_internal_residue_gysin_kernel.py`
- `research/benincasa/soft-internal-residue-gysin-kernel.json`

