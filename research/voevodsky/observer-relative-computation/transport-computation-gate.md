# Strict transport gate: local repair verified, whole-programme gate still red

The warning was reproduced as a failure with -Werror. Baseline: results/agda-transport-gate-before.log. No warning suppression was added.

## Repair performed

ObserverNonuniqueHistory retains the SAME State, Step and Run datatypes and history endpoints. Its observer/replay proofs now use a general eliminator over ALL endpoint pairs, with a Shape family and a proved decode/encode roundtrip. The implementation no longer pattern-matches directly on specialized indexed histories requiring unsupported constructor-injectivity machinery. Bool is the proven observational encoding of the original histories, not a silent replacement for them.

The generic faithful-recovery theorem was extracted into ObserverFaithfulRecovery. ObserverPolicyReconstruction reexports it under the old module name. The internal observer therefore no longer imports unrelated concrete-machine uniqueness proofs solely to obtain a generic truncation theorem.

ObserverTransportRegression checks by refl that rule readout COMPUTES on red and blue histories transported in the constant History family. These are definitional tests, not equalities obtained by rewriting transport away. Recovery also holds for an arbitrary transported history. These tests are scoped: they are not a test of every possible nonconstant indexed transport or compiler behavior.

## Reproducible gate and current result

Run:

`python research/voevodsky/observer-relative-computation/check_transport_gate.py`

The checker performs three fresh --ignore-interfaces checks and records source hashes/unchanged-source verification, compiler version, commands and logs in results/transport-gate.json:

- local internal-observer/transport regression with -Werror: PASS;
- entire aggregate with ordinary safe typechecking: ACCEPTED;
- entire aggregate with -Werror: FAIL.

The script intentionally returns exit1 and passed=false while the whole warning-free gate fails. The local repair is independently marked verified. Older successful audit receipts must not be read as satisfying this newly enforced computation gate.

## Remaining localized blocker

The accepted whole-closure log identifies the remaining UnsupportedIndexedMatch diagnostics in ObserverPolicyReconstruction.Fixture: finished-unique, middle-unique and history-unique (the latter triggers two constructor-injectivity diagnostics). The strict whole check stops at the first one. The accepted log lists them all, with repeated summary diagnostics.

The propositions remain accepted, but the compiler warns their definitions do not compute on transports. This is a computational limitation, not evidence of a proved contradiction. The next leaf must generalize or otherwise replace these concrete-machine eliminators while preserving the ACTUAL Run witness type and the existing uniqueness statement. Until then, the whole programme is not warning-free.
