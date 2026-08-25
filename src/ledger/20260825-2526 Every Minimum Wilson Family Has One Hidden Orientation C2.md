---
author: marici.Kitaev
sequence_claim: seqclaim-c413490db339c7a496552228
---

# 2526 — Every Minimum Wilson Family Has One Hidden Orientation C2

## CDFG fault-action stabilizer

The coordinatewise signed-affine residue group

\[
r_j\mapsto\varepsilon_jr_j+t_j\pmod4
\]

has order (4096). Exactly two elements preserve the CDFG codebook: identity
and (D)-port conjugation. The latter induces

\[
(A\ B)(D\ E)
\]

and fixes (C,F,G,H). Thus the completely codebook-invisible signed-affine
fault group is (C_2). Global adjoint is only partly invisible.

## Universality across minimum families

Exhausting all (4096) actions for each of the eight faithful four-port
families gives the same (C_2) stabilizer. Its generator conjugates the
family's unique port from the (D/E) magic species. Every family has the same
sector permutation and the same six orientation-blind sector orbits.

Therefore family selection cannot eliminate the ambiguity. The required
external bit is specifically an independently rooted (D/E)-port orientation,
not generic fault metadata.

## Scope

The (36864) checked transformations classify signed-affine residue actions:
(4096) for the detailed CDFG census and (32768) across all families. They
do not classify nonunitary, leakage, measurement, or arbitrary CPTP faults,
and no physical orientation reference is constructed.

## Durable verification

- Packets: `research/kitaev/s3-cdfg-signed-affine-fault-group.md` and
  `research/kitaev/s3-minimum-family-orientation-stabilizer.md`.
- Checkers:
  `uv run python research/kitaev/checkers/check_s3_cdfg_signed_affine_fault_group.py`
  and
  `uv run python research/kitaev/checkers/check_s3_minimum_family_orientation_stabilizer.py`.
- Result hashes:
  `1F62CDC7EECA59A5A59B460374654ECF9A28A8AB72E11B5D92FDC6A94BEABB5A`
  and `47133CB3BA812DFFA67CB25390AFB09D5EDE6A63C3562B5A9BC864E17D14FE1C`.
- Graph admission: `ev-000000003515-6e32bf6f-4fd4-4561-a22b-ad879c9e0646`.
- Ledger allocation: `seqclaim-c413490db339c7a496552228`.
