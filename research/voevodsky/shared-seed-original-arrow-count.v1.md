# Shared-seed two-body construction: 7,128 original-convention arrows

For the seed AB, BC, CA, AD, DB, BA and the specified area-packet two-body
construction, reapply exactly the primitive convention used for the original
1,836 construction: one nonzero coefficient transfer between distinct typed
(stage, triangle, coordinate) endpoints counts once.

The complete local-selection, alignment and dense-return network has

    216 + 1728 + 5184 = 7128 arrows.

The support partitions as

    1836 within body A + 1836 within body B + 3456 between bodies.

The 24 generated triangle positions each carry three coefficients, at three
stages: 216 typed port configurations. A geometric edge, a scalar arithmetic
operation, a Python instruction and a configuration-transfer arrow are not
interchangeable counting units. The earlier 11,371 record-instruction count
is withdrawn as an answer to this arrow-count question.

## Fresh verification without changing the owning sources

`checkers/check_shared_seed_original_arrow_count.py` copies the original
`check_twenty_four_triangle_shared_seed.py` and `check_pair_arrow_ledger.py`
unchanged into an isolated output directory and executes both. Their source
helpers are imported read-only. No Nima source or result is rewritten.

The first execution reconstructs the geometry and coefficient modes from the
seed under its existing frame, area-action and character rules. The second
executes the original three-stage arrow enumeration and algebraic controls.
The independently generated dense arrow file is byte-for-byte equal to the
archived source arrow file.

A separate verifier then reads every actual generated endpoint and exact
coefficient and checks:

- all 7,128 endpoint pairs are unique, nonzero and correctly stage-typed;
- the stage and body partitions above exhaust the support;
- all 5,184 dense feedback arrows have their actual closed three-step return;
- every return product is positive real, and the products sum to trace one;
- the union of the closed returns includes every one of the 7,128 arrows.

Thus the count includes the entire specified return network, not only a chosen
route or a list of selected nonzero entries. The least return-trace loss on
deleting one arrow at fixed remaining weights is exactly 1/129600. Any nonempty
fixed-weight deletion loses a positive closed-cycle contribution, so this
construction is pruning-minimal. No minimality under reweighting or refactoring
is asserted.

## Exact scope of the answer

7,128 is the full three-stage support for this **shared-seed two-body** candidate
under the unchanged original coefficient-arrow convention. It is not 1,837,
not the old single-body count 1,836, and not 11,371 compiler transitions.
The bare six-arrow seed does not uniquely select all of the supplied frame,
representation and dense-feedback architecture. If a different 'new seed' or
architecture is intended, this receipt does not count it. The certificate also
does not identify an extra arithmetic preparation cost or derive a physical
mass calibration.

## Reproduction

    python research/voevodsky/checkers/check_shared_seed_original_arrow_count.py
    python research/voevodsky/checkers/test_shared_seed_original_arrow_count.py

Result: `results/shared_seed_original_arrow_count.v1.json`.
Seven independent regression controls pass, including coefficient tampering,
zero insertion, deletion, duplicate endpoints and wrong stage typing.
