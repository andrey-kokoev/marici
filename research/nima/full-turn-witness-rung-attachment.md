# Retained 2pi Hamiltonian witness attached to rung4

## What is attached

Use the actual two triangle components and the existing endpoint-compatible
composition. Retain the initial LR/RL products and all six full-seed
continuations. With the previously attached positive rotor lift, their
angles are 0,pi/3,2pi/3,pi,4pi/3,5pi/3,2pi.

The completed packet stores:

- the actual primitive registry;
- all 17 operand/payload records (two component inputs, full seed, and seven
  successive pairs of role-labelled composites);
- all parent-slot bindings and ordered path words;
- the seven ordered stage pairs;
- the unwrapped angular lift, including its nonzero final value.

The validator checks completeness of endpoint joins, coefficient products,
chronological parent chains, actual incidence continuation and agreement
with the existing rotor plane. It computes the signed return U(2pi)=I.
The ordinary endpoint contrast returns after three updates, but U(pi)=-I;
that shorter record fails validation as a complete signed-rotor turn.

This is the operator's intended full-turn witnessing interpretation in the
existing realization, not an independently introduced classical measurement.
It is not asserted that every abstract witness type is such a rotation.

## Actual rung attachment

The numeric Row type did not itself contain this complete certificate. The
adapter explicitly enriches its original leaves with a FullTurn record,
using a WitnessRow subclass. It then reuses the UNCHANGED source/target
indexing and two-stage promotion functions for BOTH existing policies and
BOTH complete routes through the confirmed rung diagram.

There are 172 leaves, covering all seven actual role-labelled path families.
This is NOT the historical 137-row matrix-response fixture, and no equality
is inferred from calling both outputs rung4.

At rung4 the retained-leaf decoder recovers the full packet, including phase,
operands, source labels and stage ordering. It also reconstructs the expected
leaf table from that packet and compares it against the recovered leaves.
Thus carrying a certificate as opaque metadata while losing its actual
attachment data is rejected.

The checks establish exact equality of the two routes, recovery under both
policies, and preservation of the final unwrapped angle 2pi. Transport does
not create another completed turn or reset the clock.

## Controls

Rejected:

1. A three-update adjoint return substituted for the full signed turn.
2. Erasing the nonzero lifted angle while retaining endpoint data.
3. Dropping a source operand.
4. Reordering stage comparisons.
5. Dropping a leaf while retaining the otherwise complete certificate.
6. Replacing the enriched leaves by numeric-only rows.

The existing fixed reference remains 2I. For these unit-count leaves its
numeric mean residual is -I, which is not the full witness. That scalar's
inability to recover the packet is not a failure of witnessing; it is loss
under that particular coarse representation.

## Status of question 6 — closed for the constructed attachment

The agreed task is to attach the actual retained full-turn witness to rung4
while preserving phase, comparisons and history. That task is closed by the
checks below. Identification with another native constructor is a separate,
stronger question, not an additional acceptance condition for question 6.

A concrete finite attachment now transports the actual full-turn record
through the existing rung implementation without losing its witnesses and
histories. It is a typed-data/enriched-row adapter, not a new Agda proof
identifying it with the original native square-cone Tick, every native rung4
object, or the 137-row physical-response construction.

The prior coherent continuous-generator tests rerun as a dependency. No
new clock, external observer, Born rule, physical seconds, charge assignment
or mass/recoil interpretation is added. A universal or cross-constructor identification is not claimed. That scope
boundary does not reopen the completed attachment task.

## Verification

    uv run --with sympy python research/nima/checkers/check_full_turn_witness_rung_attachment.py

21 exact attachment/control checks pass, rerunning the earlier coherent
Hamiltonian/clock chain and original rung-diagram checks.
Receipt: `results/full-turn-witness-rung-attachment.json`.
