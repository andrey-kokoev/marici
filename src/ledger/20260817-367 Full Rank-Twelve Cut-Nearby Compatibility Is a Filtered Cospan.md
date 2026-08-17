---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Full Rank-Twelve Cut--Nearby Compatibility Is a Filtered Cospan

## Question

The occurrence-level Leray square of Entry 366 is (C_3)-natural. The
stronger proposed discriminator between H2 and H3 was strict compatibility
of Cut residue with the complete rank-twelve total-energy nearby system,
including its second Rees grade. The hard-to-vary claim tested here is

\[
\boxed{
\text{the logarithmic nearby image and the Cut--nearby image coincide as
subobjects of the full rank-twelve coefficient system}.}
\]

All maps used below were derived independently before this comparison:

- the rank-twelve nilpotent and algebraic extension columns of Entry 300;
- the exceptional Cut--nearby realization of Entries 226 and 301;
- the orientation-twisted conductor intertwiner of Entries 305 and 308;
- the unimodular occurrence quotient of Entry 312; and
- the second-Rees regularization of Entries 292--293.

No projector or basis change is fitted to align the two images.

## Two algebraic realizations

Work on the generic nonsoft locus (xy(x+y)\ne0). In ambient algebraic
coordinates

\[
(e_2,e_3,e_4,e_5,e_6,v_0)\subset\mathcal T_7,
\]

the logarithmic rank-three image is

\[
L_{\log}
=\left\langle
\Theta_{101}^{\rm fix},
\Theta_{110}^{\rm fix},
\frac{e_6}{8(x+y)}
\right\rangle .
\]

Its first two generators have nonzero (e_4) and (e_2) coordinates,
respectively, together with opposite (v_0) tails. Its third generator is
the (e_6) line.

In the orientation-twisted enhanced frame, the Cut--nearby realization of
the same primitive conductor basis is

\[
L_{\rm Cut}
=\left\langle
2y e_3,
2x e_5,
y e_3+x e_5+e_6
\right\rangle .
\]

This is the image of the source-derived matrix (J), with the four enhanced
occurrences presented by the unimodular quotient (K).

## Exact rank test

At the exact generic fiber ((x,y)=(2,3)), independently clearing each
nonzero column denominator gives integral matrices with

\[
\operatorname{rank}L_{\log}=3,
\qquad
\operatorname{rank}L_{\rm Cut}=3,
\]

and

\[
\operatorname{rank}(L_{\log}+L_{\rm Cut})=5.
\]

Therefore

\[
\boxed{
\dim(L_{\log}\cap L_{\rm Cut})=1.}
\]

The support pattern proves the same statement generically: membership in
(L_{\rm Cut}\subset\langle e_3,e_5,e_6\rangle) forces the coefficients of
the unique (e_4) and (e_2) logarithmic generators to vanish. Hence

\[
\boxed{
L_{\log}\cap L_{\rm Cut}=\langle e_6\rangle .}
\]

The strict-equality claim is falsified.

## Second-Rees bridge

The common line is not accidental. The raw primitive two-wall connection
has the fixed second-order term

\[
E^{-2}\frac18e_6.
\]

The source-normalized Rees correction removes the double pole and produces
the logarithmic top line

\[
\frac{e_6}{8(x+y)}.
\]

On the Cut side,

\[
e_6
=left(y e_3+x e_5+e_6\right)
-\frac12(2y e_3)-\frac12(2x e_5).
\]

Thus the sole geometric intersection of the two rank-three images is exactly
the primitive second-Rees top direction.

## Elliptic separation

The complete logarithmic nilpotent image has one additional elliptic line,
so

\[
\operatorname{rank}\operatorname{im}N_E^{(12)}=4.
\]

The Cut--nearby commutator has zero infinity-Gysin image and therefore no
elliptic component. The elliptic line remains independent rather than being
matched or cancelled.

## Cyclic transport

Entry 366 transports the frozen source descriptors, orientations, and Leray
normalizations through all three marked-Cut sectors. Consequently every
sector has the same profile

\[
(\operatorname{rank}L_{\log},
\operatorname{rank}L_{\rm Cut},
\operatorname{rank}(L_{\log}\cap L_{\rm Cut}))
=(3,3,1).
\]

No sector-specific support or carrier correction appears.

## Narrow result

Strict full-rank Cut--nearby commutation is false. The surviving
compatibility is the filtered cospan

\[
L_{\log}
\longleftarrow
\mathcal C_{\rm cond}
\longrightarrow
L_{\rm Cut},
\]

where (mathcal C_{\rm cond}) is the common primitive conductor occurrence
lattice. Its top line is realized geometrically on both sides by the
second-Rees (e_6) bridge; the two wall directions have different
layer-specific realizations. The elliptic line belongs only to the
logarithmic nearby layer.

## Classification

| Datum | Classification |
|---|---|
| common conductor lattice | occurrence/Tate--Kummer coefficient data |
| (L_{\log}) | logarithmic marked-extension realization |
| (L_{\rm Cut}) | enhanced higher-Rees realization |
| common (e_6) line | second-Rees bridge |
| elliptic line | Legendre nearby-cycle coefficient data |
| strict equality | falsified |
| cyclic profile | identical in all three sectors |
| new carrier datum | none |

## Update to H2 versus H3

This test rejects an overly strict form of H2 in which the two operations
must have identical images. It does not force H3: both realizations are
still related by the same source-derived conductor lattice, purity,
orientation, Leray, and Rees calculus, with no sector-specific operation or
new carrier stratum.

The surviving H2 statement is genuinely filtered:

\[
\boxed{
\text{shared calculus relates distinct coefficient layers by a canonical
cospan and higher-Rees bridge, not by strict commutation}.}
\]

## Evidence

- `research/benincasa/marici-gm/src/bin/full_rank12_cut_nearby_layers.rs`;
- `research/benincasa/full-rank12-cut-nearby-layers-certificate.json`;
- Entries 226, 292--293, 300--301, 305, 308, 312, and 366.

## Next falsifier

Determine whether this generic filtered cospan extends through the first
nontransverse supports where the two wall directions can collide:

\[
xy(x+y)=0
\]

and the conductor/elliptic discriminant intersections. Compute the joint
Rees/nearby Smith data of both legs simultaneously. A new torsion prime,
irreducible support factor, or loss of the common (e_6) line would push the
architecture toward H3. Closure using only soft normals, the existing two
half-sums, and the Legendre node would strongly support filtered H2.
