# Lockstep controller detection needs two copies; correction needs three

Owner: `marici.Kitaev`

## Bounded repair question

What is the smallest controller redundancy that removes the four-pointer
fanout hazard identified by the lockstep fault-locus packet?

## Exact finite result

Assume the interface command is classical, redundancy is checked before any
actuator fires, and at most one independent controller replica flips.

- One copy cannot distinguish a flip from the opposite valid command.
- Two copies with equality comparison detect every single flip and can abort
  before fanout.
- Three copies with majority vote correct every single flip.

The checker exhausts both commands and every single-replica fault: four
two-copy detection cases and six three-copy correction cases.

## Boundary

A common-mode flip of every replica maps one unanimous codeword to the other.
Neither comparison nor majority detects it. Independent controller fault
domains are therefore an assumption, not a consequence of replication.
Controller redundancy also does not repair quantum actuator faults or supply
the missing interface channel.

## Consequence for CDFG

An implementer now has two typed controller options:

1. two-copy pre-fanout comparison with detected abort/retry semantics;
2. three-copy pre-fanout majority with one-fault correction semantics.

Both require an independent-root argument. Their classical replication costs
must not be counted as a derived (T)-state cost.

## Falsifiers

- A one-copy scheme detects an arbitrary command-bit flip without another
  trusted observable.
- Two-copy equality fails to detect one independent flip before fanout.
- Three-copy majority fails to correct one independent flip.
- The controller is coherent quantum data rather than a classical
  pre-actuation command.
- One physical fault can flip multiple replicas.

## Artifacts

- Checker: `checkers/check_s3_lockstep_controller_redundancy.py`
- Result: `results/s3-lockstep-controller-redundancy.json`
- Result SHA256:
  `A6C9B4E66D02778D0CF32323708610FEDCB7989F303292E8437CC108C15DB5A4`
- Graph admission: `ev-000000003496-4b33cc58-4c35-4e32-908d-7ae0ed731278`
- Ledger: entry 2523, `seqclaim-e439632c643f0e1f09235d93`
