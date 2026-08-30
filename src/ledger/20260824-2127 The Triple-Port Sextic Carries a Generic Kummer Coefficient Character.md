# 2127 — The Triple-Port Sextic Carries a Generic Kummer Coefficient Character

> **Superseded by Entry 2129.** The local Kummer calculation is correct for
> the artificially restricted Cayley--Menger family, but that restriction is
> not an admitted source object. No cosmological coefficient-support claim
> follows from it.

## Hard-to-vary claim

The source-derived sextic of Entry 2126 is genuine coefficient support for the triple-deleted correlator sector: at a generic smooth point it carries the anti-invariant rank-one Kummer character of the Cayley--Menger square root.

It remains unactivated by the literal physical contour.

## Source coefficient

In three physical spatial dimensions, the frozen Cayley--Menger loop measure contains

\[
K^{-1/2}.
\]

On the triple deletion-port section,

\[
K=-\frac12\widetilde{\mathcal Q}_3,
\]

so the restricted coefficient is, up to a source-fixed unit,

\[
\widetilde{\mathcal Q}_3^{-1/2}.
\]

## Generic smoothness test

Set

\[
p_1=p_2=p_3=1,
\qquad U=E_T^2.
\]

Then

\[
\Lambda=-3,
\qquad
\widetilde{\mathcal Q}_3=-3U+4.
\]

At `U=4/3`, the sextic vanishes and

\[
\partial_U\widetilde{\mathcal Q}_3=-3\ne0.
\]

Thus the divisor has a transverse smooth locus. Around a positively oriented local loop,

\[
\widetilde{\mathcal Q}_3^{-1/2}
\longmapsto
e^{-\pi i}\widetilde{\mathcal Q}_3^{-1/2}
=-\widetilde{\mathcal Q}_3^{-1/2}.
\]

Hence

\[
\boxed{T_{\widetilde{\mathcal Q}_3}=-1.}
\]

## Classification

\[
\boxed{
\text{unchanged Cayley--Menger Carrier}
+
\text{new section-induced Kummer coefficient support}.
}
\]

This is outcome 2 of Entry 2126's decision table: coefficient variation exists, while physical activation is not established.

It is a concrete positive instance of H2. The new complexity is carried by a sector-specific coefficient object over a source-derived section of the common Carrier, not by a new incidence primitive.

## Verification

The exact rational smooth-point and derivative check is

`research/benincasa/checkers/triple_port_sextic_kummer.rs`.

## Physical qualification

The defining section has

\[
y_{12}=y_{23}=y_{31}=-E_T/2,
\]

and therefore misses the literal positive Cayley--Menger chamber for `E_T>0`. The coefficient monodromy does not by itself imply a physical correlator singularity.

## Next falsifier

Derive the analytically continued source relative cycle near a generic smooth point of `\widetilde{\mathcal Q}_3=0`. Compute its intersection with the vanishing cycle and its deck character.

- zero intersection closes physical activation;
- nonzero intersection promotes the sextic to a genuine correlator singularity;
- path-dependent intersection indicates missing continuation data rather than a physical class.
