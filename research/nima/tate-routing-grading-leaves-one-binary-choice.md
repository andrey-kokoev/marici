# Tate routing grading leaves one binary choice

Date: 2026-08-23

Grade a full-log source row by the number of negative rays among its two
contracted conductor directions.  Its census over all eight maximal cones
and three contracted pairs is

\[
(6,12,6).
\]

Grade a literal replacement row by

\[
(|H|-2)+\operatorname{Tor},
\]

where \(|H|=2,3\) is the missing Boolean-state size and
\(\operatorname{Tor}=0,1\).  Across six road/sheet halves its census is also

\[
(6,12,6).
\]

Conditional on identifying each source pair/remaining-sheet base with one
literal road/sheet base, the grading fixes the extreme assignments:

- zero negative contracted rays must land in \((|H|=2,\operatorname{Tor}=0)\);
- two negative contracted rays must land in \((|H|=3,\operatorname{Tor}=1)\).

The two mixed-sign source rows both have degree one, as do

\[
(|H|=2,\operatorname{Tor}=1),
\qquad
(|H|=3,\operatorname{Tor}=0).
\]

Thus grading reduces the routing to one binary middle swap after imposing
the common \(D_3\) transport.  It does not choose that swap.

The target four-state packet is a bicomplex square.  The flip-normal
differential changes missing-Boolean size while preserving Tor grade; the
Cartier Bockstein changes Tor grade while preserving Boolean state.  Hence
the two candidate routings exchange which ordered source sign flip is sent
to those two directions.  Entry 210 orders the corridor labels as
`moving_then_persistent`, suggesting

\[
\text{moving}\longmapsto\Delta\operatorname{Tor},
\qquad
\text{persistent}\longmapsto\Delta|H|.
\]

But Entry 210 also states that Tor is spectator in the proved support
dictionary and that the occurrence-line/excess-Gysin transformation is
unconstructed.  Therefore this assignment is a prediction, not a theorem.
Proving it is exactly the missing ordered extraordinary comparison; neither
the Bockstein nor the flip-normal differential can decide it alone.

Evidence:

- `research/nima/checkers/check_tate_routing_bigrading_gate.py`.
- Entries 251, 259--262, and 627.
