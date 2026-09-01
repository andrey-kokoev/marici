# Physical16 event-representation no-go: WP1118

## Question

Do the six physical16 event roles admit a source representation assignment
that enables WP1117's singlet constraints?

## Exact event labels

The event atoms are

\[
F_{\rm det},F_{\rm null},R_{\rm det},R_{\rm null},X_{\rm det},X_{\rm null},
\]

each with weight \(1/4\). These labels encode detector, monitor, cross, and
null provenance. They do not carry an \(SU(4)\times SU(2)\times U(1)\)
source-transformation law. There are zero source-authorized representation
assignments and therefore zero evaluable singlet constraints.

Assigning all six events the trivial singlet would be an additional posit, not
a derivation, and would leave all \(36\) coupling entries unconstrained.
Assigning branch-matching representations to manufacture zeros would be target
fitting.

## Classification

Negative gate. The production kernel requires physical event dynamics, not
just the finite support labels.

Checker: `research/flavor/checkers/wp1118_physical16_event_representation_no_go.py`

Result: `results/wp1118_physical16_event_representation_no_go.json`
