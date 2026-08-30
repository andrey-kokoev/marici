# Revision-binding deletion replay

Author: `marici.Aspect`

Date: 2026-08-26

Status: executed end-to-end hostile

## Directed test

Nima requested one execution of the frozen optical source-connection contract
with three outcomes:

1. reject a cross-run witness splice;
2. accept a same-run source-certified frame transport;
3. delete the connection revision and make transported acceptance unavailable.

The third outcome must not silently revert to literal epoch equality. That
fallback would misclassify missing transport authority as evidence that the
two frames disagree.

## Frozen connection

The transported packet binds the phase connection by both stable identity and
revision:

    connection_id = phase5-connection
    revision = rev-7

The port record belongs to epoch 1 and the decoder/calibration to epoch 0. A
certified transport with displacement one maps the record into the decoder
frame. All records, the connection contract, and the transport certificate
belong to one run.

## Three-valued validator

The validator now returns:

- `accept` when one run and either one common frame or a revision-bound
  coherent transport realizes the packet;
- `reject` when present evidence contradicts the joint contract, including a
  cross-run splice;
- `unavailable` when cross-frame evaluation requires a connection artifact
  whose identity or revision binding is absent.

Deletion of `revision_binding` preserves the epoch mismatch. The verdict is
`unavailable`, not `reject`, and the ordinary Boolean acceptance remains
false. Thus neither permissive acceptance nor literal-epoch fallback occurs.

## Result boundary

This is the requested prospective hostile against the frozen representation.
It demonstrates the exact acceptance semantics in the Aspect checker. It does
not claim the blocked native lifecycle store has executed or admitted the
contract; that store still requires its missing result-contract migration.

## Reproduction

Run:

    python research/aspect/checkers/cross_run_optical_witness_splicing.py

