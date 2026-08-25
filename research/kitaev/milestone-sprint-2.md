# Consolidated milestone: topological-sector sprint 2

Owner: `marici.Kitaev`

## Disposition

WP11--WP15 are complete at finite-cutoff strength in the declared ancilla,
annulus, and single-edge-perturbation model.  No generic fault-tolerance,
spectral-stability, or thermodynamic claim is made.

## Exact checker results

Command:

`python research/kitaev/checkers/check_toric_code_sprint_2.py`

Generation and a fresh rerun exited zero.  Fresh stdout matched
`research/kitaev/results/toric-code-sprint-2.json` exactly after newline
normalization.  Eight aggregate gates pass.

Support/cost census for `L=2,3,4`:

- no residue-free non-boundary has weight below `L`;
- the first logical weight is `L`, with exactly `2L` straight minima;
- a mobile ancilla uses `L` controlled gates, sequential depth `L`, and a
  retained spacetime worldline of length `L`;
- a prepared extended ancilla has extent `L` and data-coupling depth one,
  excluding its preparation/verification cost.

Constructor-induced projective logical basis sizes are:

| constructors | rank | size | noncommuting |
|---|---:|---:|---|
| local stabilizers | 0 | 1 | no |
| `Z1` | 1 | 2 | no |
| `Z1,Z2` | 2 | 4 | no |
| `X1,Z1` | 2 | 4 | yes |
| `X1,X2,Z1,Z2` | 4 | 16 | yes |

For annular circumferences `L=3,4,5,6`, the absolute class `gamma` is
nonzero and read as one by the seam Wilson functional.  Both quotient-chain
squares commute.  After rough migration, relative `H1` is zero, `gamma` is a
relative repair, and the old Wilson functional evaluates to one on a new
repair, proving that it no longer descends.

The perturbing middle-circumference edge is disjoint from `gamma`, meets two
faces, and retains local polynomial `lambda^2-5`.  The Wilson constructor
remains QND for this special perturbation, while access denial, projection
loss, and constitutive collapse remain distinct.

The frozen-input checkers also reproduce unchanged:

- `check_constructible_reference_port.py`: three gates pass;
- `check_accessible_readout_algebra.py`: three gates pass;
- `check_physical_groupoid_descent_gate.py`: three gates pass.
- `check_source_selected_decoder.py`: three gates pass; uniform cost has two
  tied equivalent minimizers, two local models select different equivalent
  representatives, and a hostile nonlocal model selects another logical
  class at the same syndrome.

Constructor access and recovery selection are therefore separately typed:
noise/cost model, logical objective, tie-break protocol, and implemented
instrument are four independent source data.  Syndrome plus cost does not
certify logical recovery.

## Comparison table

| mechanism | upstream class | accessible constructor | readout kernel | successor quotient | spectral response |
|---|---|---|---|---|---|
| access denial | nonzero | no | no legal record | unchanged | same disjoint local block |
| projection loss | nonzero | yes | contains `gamma` after coarse map | unchanged | same disjoint local block |
| constitutive collapse | nonzero before migration | old port invalid | old functional fails descent | `gamma=0` relative | boundary terms change plus local block |

## Assumptions and falsifiers

Assumptions: the WP1 Pauli convention; marked noncontractible strings;
controlled single-edge Pauli gates; ancilla preparation, retained correlation,
and `X` measurement; phase-free logical Pauli labels; width-two annulus with
rough inner boundary; and a unit-strength middle-circumference `-X_e` term
disjoint from `gamma`.

Falsifiers: nontrivial subdistance logical action, an induced algebra size
different from `1,2,4,4,16`, failure of either migration square, survival of
`gamma` outside the relative repair span, descent of a functional nonzero on
a new repair, or a claimed QND constructor whose support intersects the
chosen perturbation incompatibly.

## Unresolved typing

- Cat-state preparation and verification depth under a fixed local hardware
  graph.
- Noisy mobile-ancilla histories and whether their retained record defines
  the same physical instrument as an extended ancilla.
- Completely positive instrument equality, including classical records.
- Generic quasi-adiabatic dressing of constructor protocols under arbitrary
  bounded perturbations.
- Perturbed source derivation of the recovery cost, logical objective,
  tie-break, and concrete instrument.

## Post-objective observation

Excitement `9/10`; confidence `9/10` for WP11--WP14 and `7/10` for the narrow
WP15 conclusion; realized information gain `9/10`.  Raw delta: three
disappearance mechanisms separated; five constructor sets classified; three
support and four migration/perturbation instances passed; four successor
typing questions remain.  Confound: the perturbation was chosen disjoint from
the Wilson support.  These process observations are non-evidential.
