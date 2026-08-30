# 1830 — The Physical Region Pair Has a Canonical Local Double-Leray Germ

## Source boundary value

The frozen source prescription places the homogeneous energy and every
labelled internal energy in the negative-imaginary tube.  For the ordered
representative

\[
(g_{123},g_{125}),
\]

the local wall coordinates are

\[
q_1=3t+y_{34}+y_{51},
\qquad
q_2=3t+y_{23}+y_{45}.
\]

Both inherit the same negative boundary-value side.

## Ordered pivots and orientation

Use the source-labelled pivots \((y_{34},y_{23})\).  Since the two cut pairs
are disjoint,

\[
\frac{\partial(q_1,q_2)}{\partial(y_{34},y_{23})}
=
\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

Relative to the frozen source measure

\[
dy_{12}\wedge dy_{23}\wedge dy_{34}\wedge dy_{45}\wedge dy_{51},
\]

moving the ordered pivots to the front has sign \(-1\).  The ordered local
double-Leray factor is therefore

\[
\boxed{-(2\pi i)^2.}
\]

Transporting the pivots and retained coordinates together around the labelled
\(C_5\) orbit preserves this sign.  The five-cycle permutation of the source
measure is even, so no fitted occurrence sign is required.

## Result and boundary

Each of Entry 1829's five labelled occurrences has a canonical local
boundary-value germ with source-fixed orientation.  This strengthens the
local physical interpretation beyond a bare de Rham logarithm.

It still does not construct the global relative chain.  The current
five-cycle packet contains incidence and denominator data but no contour
orientation, contour-to-regulator map, or relative-boundary morphism.  Thus

\[
\boxed{
\text{local continued germ: canonical},
\qquad
\text{global chain pairing: undefined}.
}
\]

Undefined is neither zero nor nonzero.  Importing a regulator hierarchy from
another graph would violate the frozen-source rule.

## Next source requirement

Acquire or derive the five-cycle loop integration representation carrying its
actual Bunch--Davies contour.  The required datum is the induced relative
boundary map into the ordered pair stratum; only that map can determine the
global intersection number of the logarithmic coefficient.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_double_leray_germ.py`
- `research/benincasa/results/five-site-region-pair-double-leray-germ.json`
- Entries 1783, 1816, and 1827--1829
- allocator claim: `seqclaim-77fbe784425a37ca86b9b5a2`
