# 1888 — The Hexagon Excess Is a Length-Two Cartier Coefficient Object

## Derived question

Entry 1887 identifies the exceptional critical scheme

\[
(L^2,M),
\]

supported on the regular-hexagon Gram divisor.  Determine its derived
coefficient object before reducing \(L^2\) to \(L\).

## Koszul calculation

The linear forms

\[
L=-2+x-6z+4v+w,
\qquad
M=-6+2x-6z+5v-w
\]

have a nonzero constant Jacobian minor.  Hence they are independent, and

\[
L^2,M
\]

is a regular sequence.  Its Koszul homology is therefore

\[
H_2=H_1=0,
\qquad
H_0=\mathbb Q[x,v,w,z]/(L^2,M).
\]

Over the reduced line \(\mathbb Q[v,z]\), the coefficient object has the
canonical Cartier basis

\[
\boxed{\langle1,L\rangle}
\]

and length two.

## Source-map audit

All nine frozen six-site source completions restrict generically nontrivially
to this object.  An exact positive-square-root point on the reduced line,

\[
z=v=1,qquad x=11/3,qquad w=1/3,qquad t=-1,
\]

makes every active wall vanish while every uncut denominator in each of the
nine source terms remains nonzero.  Thus no completion is identically lost
on the excess line.

## Narrow result

\[
\boxed{
\mathcal E_6
=
\mathcal O_{(L,M)}[L]/(L^2)
}
\]

is the complete algebraic/de Rham exceptional coefficient object in this
sector.  It has no higher Koszul homology and requires no fitted support
summand.

This is exactly the existing Cartier/excess pattern: a reduced Carrier
support with a sector-specific nilpotent coefficient thickening.  No new
Carrier incidence operation is required.

## Scope

The result classifies the algebraic exceptional object and its generic source
restrictions.  It does not assert an independent Betti vanishing cycle or
physical discontinuity along the Gram divisor.  Such activation would need a
source-derived relative-cycle specialization.

## Next falsifier

Compute the \(C_3\) stabilizer action on \(\langle1,L\rangle\) and the nine
source restriction maps.  Determine whether the nilpotent generator is
invariant, carries a nontrivial character, or is killed after cyclic descent.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_excess_koszul.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-excess-koszul.json`
- allocator claim: `seqclaim-47c101da1615bd7a785bcf3d`
- epistemic event: `ev-000000002250-2c1029b2-d8ac-4fcb-bc27-6025161aff88`
