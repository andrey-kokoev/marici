# The Tate reflection lift propagates to all even arities

Date: 2026-08-23

The six-point loaded reflection lift is unique, and its first physical
(6\times4) Cut enlargement passes at eight points.  Entry 542 supplies
the general induction.

Every nonempty family of compatible physical Cuts decomposes an even polygon
into strictly smaller even polygons.  Maximal Cut families are
quadrangulations, so their terminal factors are four-point units.  Changing
the order of (r) Cut restrictions contributes the same sign twice:

\[
\operatorname{sgn}(\sigma)_{\rm Koszul}
\operatorname{sgn}(\sigma)_{\rm Thom}=+1.
\]

Since the lower-arity framed mapping spaces are pointed and contractible,
their products and descent diagram remain contractible.  The unique local
reflection lifts therefore glue to a unique global lift:

\[
\boxed{
H_{\rm refl}^{(2m)}
\text{ exists, is rigid, and is Cut-natural for every }m\ge2
}
\]

inside the cellular fs/Kato sector.

This turns the six mixed conductor faces from a one-off repair into the
local generator of an all-even natural transformation.  The theorem does
not extend to a raw global scheme correspondence, the nontrivial-inertia
Artin category, or numerical amplitude readout.

Evidence:

- `research/nima/checkers/check_tate_reflection_lift_all_even_cut_induction.py`
- Entries 435, 542, and 544.
