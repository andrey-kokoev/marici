# DPC controlled-observability and closure attack

## Scope

This packet performs the bounded hostile requested by Nima. It tests exact
finite controlled observability, source-admitted calibration, trace semantics,
Blackwell preservation, provenance-bearing closures, and the smallest
autonomous counterexample to universal idempotent-closure dynamics. It does
not restore DPC as a universal explanatory law.

## Static clock gates

On `X={0,...,19}` with phase frame `delta in Z/5`, the passive record is

\[
R(f,\delta)=(f\bmod4,f+\delta\bmod5).
\]

Every passive record has exactly five source-frame preimages. One independently
known zero reference produces `(0,delta)` and makes the joint record injective
on all 100 source-frame states. A second unknown source does not: simultaneous
translation of both sources and the frame leaves both records fixed, so every
joint record retains a fivefold ambiguity.

## Reset and oracle-policy hostiles

The smallest reset hostile has a hidden predecessor `delta in {0,1}`, constant
readout, and a reset taking both predecessors to zero. Terminal certainty is
complete, but the full input-output traces coincide. The reset controls a
successor and does not observe the predecessor.

An admitted policy receives the same observation history in both states and
must choose the same input. A policy choosing its input from the hidden state
separates only by leaking the answer and is rejected as an oracle.

Reset is not intrinsically non-diagnostic. With informative pre/post readouts,
an intervention can help distinguish predecessor states. The exact criterion
is trace separation, not the presence or absence of reset.

## Blackwell hostile

Let states be pairs `(a,b)`. The old experiment reports `a`; a replacement
reports `b`. The replacement separates the new `b` target, but `(0,0)` and
`(1,0)` have the same replacement law and different old laws. No
state-independent garbling of `b` can reproduce `a`. New-target separation
therefore does not imply constructive preservation.

Blackwell comparison is nevertheless only terminal. Two instruments may emit
the same first record and hence be Blackwell-equivalent as one-use experiments,
while preparing different successor states. A later probe then separates their
complete traces. Dynamic constructive preservation therefore requires an
instrument/process simulation intertwining outputs and successor evolution;
ordinary Blackwell dominance is its terminal shadow after successor state is
forgotten.

## Closure ontology

On the smallest source set supporting two nonidentity alternatives, define
idempotent closures on `{0,1,2}` by sending source zero to one or two. A
constant terminal readout identifies their results, while an admitted residual
probe separates them. Bare fixed-point value is not a sufficient Carrier
packet; the provenance/boundary packet is necessary relative to that future
intervention.

The smallest autonomous counterexample to idempotent closure as a universal
model of dynamics is the two-state toggle

\[
0\longmapsto1\longmapsto0.
\]

Its transition is not idempotent and its observable trace alternates forever.
A controlled invariant set `{0,1}` says where the trajectory remains but not
which temporal phase occurs. Coalgebraic trace semantics represents the
behavior directly. Thus Nima's weakened stabilization-packet interface
survives only because it explicitly permits coalgebraic behavior in place of
one universal closure algebra.

## Verdict

The clean generalization is a source-indexed behavioral packet:

- source/generative presentation;
- typed transition or stabilization law;
- complete trace semantics;
- protocol-relative sufficient statistic;
- residual interface for declared future interventions;
- authority and coherence witnesses.

Provenance is retained exactly when deletion changes an admitted future trace
or capability. Otherwise behavioral minimality requires its removal. A bare
fixed point is insufficient, while complete genealogy is unnecessary.

The exact checker is
`checkers/dpc_controlled_observability_closure_attack.py`; results are written
to `results/dpc_controlled_observability_closure_attack.json`.
