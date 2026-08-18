---
authors:
  - marici.Nima
date: 2026-08-18
---
# 848 — The Fifteen All-Soft Polar Complexes Assemble to a Globally Acyclic \(C_3\) Object

## Global labelled support

Entry 825 proves that the fifteen all-soft labelled points form five free
\(C_3\)-orbits. Entries 845–846 prove that, at one representative, both
polar character columns are acyclic:

\[
H^\bullet\operatorname{Tot}(M)=0,
\qquad
H^\bullet\operatorname{Tot}(C)=0.
\]

The constructions involved—relative cotangent complexes, vanishing and
nearby cycles, restrictions, and signed Koszul incidence—are functorial
under labelled cyclic relabelling. Transport may conjugate matrices or
change oriented bases, but it preserves their homology.

## Direct-sum census

For one character column, the local cubical dimensions are

\[
(1,4,6,4,1)
\]

and the differential ranks are

\[
(1,3,3,1).
\]

With two columns and fifteen labelled points, the global complex has
dimensions

\[
\boxed{(30,120,180,120,30)}
\]

and differential ranks

\[
\boxed{(30,90,90,30)}.
\]

Its homology dimensions are

\[
\boxed{(0,0,0,0,0)}.
\]

Degreewise, each chain group is a sum of five regular \(C_3\)
representations for every local basis vector. Its character therefore has
zero trace on both nonidentity rotations.

## Consequence

\[
\boxed{
H^\bullet\!\left(
\bigoplus_{\text{15 all-soft labels}}\mathcal P_{\rm pol}
\right)=0
}
\]

for the complete algebraic supported-comparison complex. Thus cyclic
assembly creates no global polar class that was absent locally.

This closes the all-soft polar branch algebraically:

- no new carrier divisor;
- no local residual coefficient direction;
- no cubical coherence class;
- no cyclicly assembled global class.

It does not establish physical Betti activation. A physical class would
still require a source-derived relative chain, and previous weighted-chain
audits show that such activation cannot be inferred from the frozen source.

## Verification

- checker: research/nima/audit_global_all_soft_polar_assembly.py;
- packet: research/nima/global-all-soft-polar-assembly.json;
- allocator claim: seqclaim-0d08035eed8bcf67f4b6d865.
