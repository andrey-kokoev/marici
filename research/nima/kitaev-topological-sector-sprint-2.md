# Kitaev topological-sector sprint 2: three disappearances and constructor access

Owner: `marici.Kitaev`

## Objective

Realize, within one controlled topological-code family, the three distinct
ways a logical observable can disappear:

1. access denial;
2. readout/projection loss;
3. constitutive collapse under a new physical boundary relation.

Then derive the logical readout algebra from explicit source constructors
rather than declaring abstract logical Pauli generators available.

## Frozen inputs

- Your WP1--WP10 packets and exact checkers.
- `research/nima/physical-groupoid-descent-and-reference-port.md`
- `research/nima/constructible-reference-port-conjecture.md`
- `research/nima/accessible-readout-algebra-gate.md`

## WP11: same class, three disappearance mechanisms

Choose one explicit annular or toric logical class \([\gamma]\). Construct
three packets with identical upstream conventions wherever possible:

- remove or forbid the loop-measurement constructor while preserving the
  Hamiltonian and homology;
- retain the constructor but compose its record with a coarse readout that
  identifies distinct logical values;
- introduce the rough-boundary relation whose relative-chain map sends
  \([\gamma]\) to zero.

Export invariants distinguishing the cases:

\[
[\gamma]\ne0\text{ but inaccessible},
\qquad
[\gamma]\ne0\text{ but readout-killed},
\qquad
[\gamma]=0\text{ in the successor relative quotient}.
\]

## WP12: constructor-derived accessible algebra

Supply explicit finite protocols for:

- one logical loop measurement;
- two commuting logical loop measurements;
- one intersecting primal--dual pair;
- the complete four-port logical Pauli family.

Use controlled-string/ancilla circuits or an equally source-defined
construction. Compute the induced operations on the ground space and verify
the generated projective operator-basis sizes \(2,4,\ldots,16\). If a protocol
cannot be derived from the frozen controls, report the smaller accessible
algebra rather than assuming the desired port.

## WP13: operational cost and locality

Measure support depth, ancilla extent, or circuit depth of each constructor.
Verify the subdistance no-access theorem in the chosen protocol model and
determine whether noncontractible support is necessary, or whether time-like
ancilla transport provides an equivalent resource.

## WP14: boundary migration as view invalidation

Treat the rough-boundary change as a physical deformation, not a database
analogy. Produce the exact maps from absolute to relative chains, cycles,
boundaries, and logical readouts. Identify which cached/readout statements
become false and which source data remains unchanged.

## WP15: hostile stability test

Repeat WP11 under the admitted single-edge perturbation. Determine whether the
three disappearance mechanisms remain distinguishable when stabilizer
commutation is partially lost but the cellular complex survives. Do not infer
generic topological stability from this special perturbation.

## Deliverables

- Bounded packets and exact checkers under `research/kitaev/`.
- A comparison table with separate columns for class existence, constructor
  accessibility, readout kernel, successor quotient, and spectral response.
- One consolidated graph report with exact residuals and explicit scope.
- Cross-sector suggestions only after the sector-native maps are complete.

Do not commit or push.

