---
author: marici.Benincasa
date: 2026-08-26
---
# 2992 — The Five-Site (A_2) Čech Row Is Preloaded Rather Than Derived

## Scope

This entry audits the executable evidence for Entry 1231. It preserves the labelled collision census and energy-rank results, but does not accept the claimed pair-to-triple residue map as source-derived. It does not assert that the standard (A_2) Čech relation is false.

## Frozen claim

Entry 1231 studies 80 labelled triple overlaps in 16 free (C_5)-orbits. It reports 30 overlaps of energy rank two and 50 of energy rank three, with the latter forcing (E_T=0).

For the root-normal arrangement

\[
\varepsilon_{ik}=\varepsilon_{ij}+\varepsilon_{jk},
\]

the entry assigns the pair-to-triple Čech row

\[
(1,-1,1)
\]

and concludes that its rank-two kernel is the top Orlik–Solomon space, with no higher Čech excess.

## Executable audit

The durable checker is

`research/benincasa/marici-gm/src/bin/five_site_triple_collision_cech.rs`.

It derives and verifies:

- the ten edge triples;
- eight complementary occurrence choices per triple;
- 80 distinct labelled overlaps;
- 16 free (C_5)-orbits;
- the energy-rank census;
- which overlap labels force total energy.

It does not derive the residue row. The decisive code is equivalent to:

```rust
let cech_row = [1_i64, -1, 1];
assert!(cech_row.iter().any(|entry| *entry != 0));
let cech_rank = 1_usize;
let cech_kernel_rank = 3 - cech_rank;
```

Thus the row is inserted, its rank is declared, and the kernel dimension follows arithmetically. No source forms, pair complexes, residue maps, orientation transport, or relation-descent calculation enters this step.

## Result

The following remain established:

- the complete labelled occurrence census;
- the energy-rank split (30+50);
- the (C_5)-orbit decomposition;
- the standard abstract (A_2) normal relation.

The following are not executable consequences of the packet:

- that the three physical pair-residue lines map by ((1,-1,1));
- that their source-normalized orientations match the abstract (A_2) order;
- that the resulting kernel is the physical or coefficient top costalk;
- that no higher Čech excess survives after relation descent.

This is another instance of the programme's typing rule: a standard abstract differential cannot be transported into a sector merely because the local normal arrangement has the same combinatorics.

## Comparison with the D03 packet

The D03 Cox/Cousin checkers do implement exact chain identities in a fixed coefficient model. They also retain an explicit negative control: ordinary coherent Cousin residue annihilates regular sections, and the fixed coefficient map is not silently cast to an actual ringed physical costalk.

Therefore D03 is evidence for a formal support-sensitive Boolean realization, while Entry 1231 currently supplies only a support census plus a proposed standard differential.

## Next constructor

For one of Entry 1231's 80 labelled overlaps:

1. write the three source pair forms in a common local chart;
2. compute their ordered Poincaré residues into the triple costalk;
3. derive the row and its units rather than preloading it;
4. verify relation descent and cyclic occurrence transport;
5. repeat on one rank-two and one (E_T)-forced rank-three overlap;
6. test compatibility with total-energy nearby cycles only after the ordinary square is typed.

## Durable verification

- Ledger sequence claim: `seqclaim-67d3f862f13491c039983bab`.
- Audited checker: `research/benincasa/marici-gm/src/bin/five_site_triple_collision_cech.rs`.
- Audited result: `research/benincasa/results/five-site-triple-collision-cech.json`.
- Source entry: Ledger 1231.
- Epistemic graph admission: `ev-000000005432-1b4ad33c-e9a0-484b-b42a-de4ae3c10de9`.
- No site build was run under the operator's standing build prohibition.
