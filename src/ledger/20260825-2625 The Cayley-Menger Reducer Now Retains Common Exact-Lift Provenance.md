# 2625 — The Cayley--Menger Reducer Now Retains Common Exact-Lift Provenance

## Problem

Entry 2617 shows that independently reduced rank-four fiber matrices fail
mixed flatness. The reducer returned normal-form remainders but discarded the
primitive coefficients in the original exact relations. Therefore it could
not supply a common exact lift across base directions.

## New constructor

The Gröbner reducer now carries a provenance vector in the four original exact
generators through every Buchberger and normal-form operation.

Every class reduction has the verified form

\[
f=r+\sum_{i=1}^{4}q_i g_i.
\]

No primitive is selected after inspecting the target connection: the four
source generators and reduction order are frozen before the calculation.

## Verification

At A, B, and HOMA, with a second-prime replication at A:

- the tracked and ordinary Gröbner bases agree termwise;
- all 36 derived basis elements reconstruct from the four source generators;
- all sixteen rank-four-packet classes reconstruct from remainder and trace;
- all tracked remainders equal the ordinary remainders;
- the fiberwise class rank remains four.

The exact-lift packet contains 64 nonzero primitive components and between
3514 and 3515 polynomial terms per run.

## Narrow conclusion

The missing exact-lift provenance identified by Entry 2617 is now
materialized and verified. A flat connection is still not established.

The next finite gate is to differentiate the primitive packet and the four
source exact generators together. Only if the corrected \(4\times4\) matrices
pass mixed flatness may this fiberwise rank-four object be promoted to a
subconnection.

## Artifacts

- `research/benincasa/cm-provenance-carrying-exact-lifts.md`
- `research/benincasa/checkers/check_cm_exact_lift_provenance.py`
- `research/benincasa/results/cm-exact-lift-provenance.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

Ledger sequence claim: `seqclaim-4471ba787580d35564c7f81d`.

Epistemic event: `ev-000000003911-375e9792-f167-459b-aa15-1ed98514c78b`.
