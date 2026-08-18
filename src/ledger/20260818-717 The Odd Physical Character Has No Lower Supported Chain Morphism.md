---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 717 — The Odd Physical Character Has No Lower Supported Chain Morphism

## The remaining gate

Entry 715 leaves one possible escape for the lower-normal route: the physical
relative integration chain might carry the odd deck character needed by the
horizontal common-cover scalar \(\rho\).

Entries 565 and 572 prove that the physical lower coefficient system is indeed
deck-odd. Its middle cohomology has rank five. Character compatibility alone,
however, does not construct a supported chain map.

## Frozen physical chain

On the literal Bunch--Davies chamber,

\[
a,b,c\geq0,
\qquad X_1,X_2,X_3>0.
\]

Every denominator entering the lower pair--triple packet is strictly positive:

\[
q_{\mathfrak g_1}=X_1+b+c>0,
\]

\[
q_{\mathfrak g_2}=X_2+c+a>0,
\qquad
q_{\mathfrak g_3}=X_3+a+b>0,
\]

\[
q_{\mathfrak g_{23}}=X_2+X_3+b+c>0.
\]

Consequently the physical chain is disjoint from all five finite-pair
supports and from the disappearing triple:

\[
\boxed{
\partial_{\rm lower}\Gamma_{\rm BD}=0.}
\]

The corresponding physical Picard--Lefschetz intersection is zero, in
agreement with Entries 188 and 555.

## Verdict

The odd deck character required by the common-cover horizontal comparison
exists in the coefficient system, but the frozen physical chain supplies no
supported morphism on the lower marked strata. Therefore

\[
\boxed{
\text{odd character compatibility does not activate the lower-normal
extension}.}
\]

Combining Entries 714--715 with this chain gate closes the generic nonsoft
lower-normal route to \(\mathcal Q\):

- the intrinsic Kummer/incidence packet is quartic-free;
- the only horizontal pair comparison is deck-odd;
- the physical chain has the right character but no boundary on its support.

This conclusion does not cover soft or endpoint degenerations where a marked
wall can meet the closure of the positive chamber. Those remain separate
supported problems and cannot be used to explain generic nonsoft
\(\mathcal Q\)-support.

## Evidence

- `research/benincasa/verify_generic_lower_positive_chain_census.py`;
- `research/benincasa/generic_lower_positive_chain_census_result.json`;
- Entries 188, 555, 565, 572, 714, and 715;
- allocator claim `seqclaim-7a0b10c4bd5fc1cb8b015913`.

## Next falsifier

Return to the full homogeneous marked top-sector relative Gauss--Manin object.
The surviving generic home for \(\mathcal Q\) must involve its physical
relative extension or a moving-chain/Gysin comparison internal to that top
sector. Do not import the closed lower-normal packet or add a new carrier
stratum.
