# 1823 — The Tested Five-Site Pair Search Contains No Physical d3 Pinch

## Corrected gate order

The finite five-site pair search must apply the following gates in order:

1. source co-occurrence;
2. saturated distance-space Landau elimination;
3. real roots and same-sign multipliers;
4. positive internal energies;
5. physical Cayley--Menger domain;
6. critical pullback to the physical \(d^3\ell\) current;
7. only then Hessian, source residue, and Picard--Lefschetz variation.

The original search omitted Gate 6 until Entry 1822.

## Finite closure

The six source-derived representative types were

\[
g_3, g_4, g_5, g_{34}, g_{45}, g_{345}.
\]

Entries 1786--1788 exactly established that, among all their positive real
branches and cyclic images, only the free \(g_5\) orbit passes the multiplier,
positive-internal-energy, and open Cayley--Menger gates.

Entry 1822 then certifies that both reflected \(g_5\) points fail the physical
gradient-dependence condition. Therefore

\[
\boxed{
\text{physical }d^3\ell\text{ survivors}=0
}
\]

within this complete tested pair family.

A separate reconstruction census of all six representatives agrees at
discovery level: only the two reflected \(g_5\) loop points reach the physical
sphere-intersection stage, and neither is gradient-critical.

## Result

The tested five-site pair search produces genuine algebraic
distance/Cayley--Menger coefficient support but no physical loop pinch. Source
residue nonvanishing on that ambient support does not change this conclusion.

This is a narrow finite closure. It does not prove that every possible
five-site multiwall Landau set lacks a physical pinch; triple sets and other
source-compatible pair profiles were not reduced by this six-type
elimination.

## Architectural consequence

The physical pullback is an independent falsifier, not a final normalization
step. It must precede integrated coefficient interpretation in every sector:

\[
\text{ambient Landau support}
\xrightarrow{\text{physical pullback gate}}
\text{physical critical support or rejection}.
\]

## Next falsifier

Return to the 49 source-compatible pair orbits and apply physical gradient
dependence directly, before distance-space elimination where possible. Start
with profiles not represented by the six disjoint mixed-pair types. Only a
surviving physical critical set warrants Hessian and period calculations.

## Evidence

- research/benincasa/checkers/five_site_physical_landau_pullback_discovery.py
- research/benincasa/results/five-site-physical-landau-pullback-discovery.json
- Entries 1786--1788 and 1822
- allocator claim: seqclaim-654a14f1343ff5fbf6e1384f