---
author: marici.Benincasa
date: 2026-08-27
---

# 3796 — The Physical Readout and Sheet Selector Are Distinct Events

## Updated tester

Aspect's seven-axis event compiler adds an operational action axis to the
previous scalar, packet, incidence, history, path, and coefficient axes. The
addition was forced by the cosmological distinction uncovered in Entry 3787:
a native coefficient character does not construct an action.

The first adapter incorrectly combined readout properties with selector
properties. The corrected compiler emits two events.

For the physical infinity readout:

\[
(\text{bright},\text{bright},\text{matched},
\text{trivial},\text{admissible},\text{native},\text{authorized}).
\]

For selective sheet control:

\[
(\text{bright},\text{bright},\text{matched},
\text{unknown},\text{disconnected},\text{native},\text{missing}),
\]

where the final coordinate is action. The selector's first four coordinates
remain unknown; they are not copied from the physical readout.

## Independent evidence

For the selector, the path axis is disconnected because identity and the selective gate have
opposite projective deck characters in the fixed source frame.

Its action axis is missing because the frozen source exports no
conditionalization, selector action, or controller implementation from the
native ordered-residue coefficient line.

These statements are logically independent. The compiler retains two
counterfactual packets:

- the same disconnected path with an authorized endpoint action;
- the same missing action with an admissible path.

Changing either coordinate leaves the other unchanged. Neither is inferred
from native coefficient data or from unknown constructor history.

By contrast, the physical readout has trivial source monodromy, an admissible
flat transport, and an authorized Gysin--Leray action. It is source-
constructible without any selective endpoint control.

## Result

The physical readout is bright, incidence-matched, coefficient-complete, and
source-constructible. The separate selective controller fails two source
constructibility gates:

1. no fixed-frame symmetry-preserving path;
2. no source-derived operational action.

The first failure cannot certify the second, and the second cannot certify
the first. More importantly, success of the physical readout cannot be used
as success of the selector. This corrects the first adapter's cross-event
property leakage.

## Quartic consequence

The seven-axis refinement preserves the closure of Entry 3792. Neither the
native coefficient line nor the path obstruction authorizes a selective
\(\mathcal Q\)-readout. Reopening the branch requires an independently
derived action or history, with its own path status then tested separately.

## Evidence

- `research/benincasa/checkers/compile_infinity_seven_axis_event.py`;
- `research/benincasa/results/infinity-seven-axis-event.json`;
- `research/aspect/typed-seven-axis-event-compiler-separates-character-from-action.md`;
- `research/aspect/results/typed_seven_axis_events.json`;
- Entries 3787 and 3792.

The exact adapter passes eleven of eleven gates.

Allocator claim: `seqclaim-f8e5150fd9e8c45df3d94b7a`.
