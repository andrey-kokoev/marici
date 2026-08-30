# Consolidated milestone: toric-code WP1--WP6

Owner: `marici.Kitaev`

## Disposition

WP1--WP6 are complete at finite-cutoff strength for the frozen periodic
square toric code.  No theorem-changing source or typing blocker required a
pause.  The work is split into two theorem packets; this file is only their
bounded handoff.

## Pilot reproduction

Command:

`python research/nima/checkers/check_toric_code_chain_carrier.py`

Exit code was zero.  For `L=2,3,4,5`, the detailed checker output gives
`rank(d1)=rank(d2)=L^2-1`, `dim(H1)=2`, and joint-kernel dimensions
`3,8,15,24`, each equal to `rank(d2)`.  At `L=2` it gives 256 chains, eight
syndromes, 32 chains per syndrome, eight local repairs, and four logical
cosets per syndrome.  At `L=3` it gives exactly two weight-two minimum
decoders differing by a local repair.

Provenance residual: `research/nima/results/toric-code-chain-carrier.json`
is a hand-written/curated summary schema, not the checker's detailed stdout
schema.  Its stated values agree, but it is not an exact generated-output
reproduction.

## New exact checker result

Command:

`python research/kitaev/checkers/check_toric_code_wp1_wp6.py`

Two consecutive runs exited zero, and fresh stdout matched
`research/kitaev/results/toric-code-wp1-wp6.json` exactly after newline
normalization.  On every `2 <= L <= 5`:

- electric and magnetic syndrome ranks are `L^2-1`;
- every star--plaquette commutator is zero;
- the ground-space dimension is four;
- `dim H1=dim H^1=2`;
- the selected primal--dual intersection matrix is the `2 x 2` identity;
- the full Pauli readout kernel equals the stabilizer rank `2L^2-2`;
- four added logical binary commutator probes are rank-minimal;
- deleting one face-boundary edge produces a nonzero residual of weight two.

The `L=3` decoder counterexample has syndrome bitmask `17`, representatives
`514` and `4097`, and nontrivial plaquette-stabilizer quotient `4611`.

Framing correction: the ordered logical probes are jointly faithful only
relative to the frozen marked `(x,y)` homology basis.  The amended checker
finds all six elements of `GL(2,F_2)`, with unframed orbits `{0}` and
`{1,2,3}`; the first loop bit is not invariant.  “Four probes are minimal”
is therefore a framed rank theorem, not a canonical unmarked-torus readout.

## Assumptions and falsifiers

Assumptions: periodic oriented square cellulation; coefficients `F_2`; one
qubit per primal edge; `A_v=X(star(v))`, `B_f=Z(boundary(f))`; positive
Hamiltonian couplings; phase-free binary Pauli coordinates for syndrome and
quotient calculations; stabilizers are the admitted local equivalences.

Falsifiers: odd star--face overlap, failure of either commutator syndrome to
equal its typed incidence map, ground dimension other than four, degenerate
primal--dual pairing, a combined-probe kernel larger than the stabilizer
span, or separation of all full-Pauli quotient classes by fewer than four
additional binary functionals.

## Unresolved typing and frontier

Physical-instrument equality still requires an explicit domain of admitted
states and a decision on retaining classical measurement history.  Full
tomography minimality is not the same optimization problem as binary Pauli
quotient separation.  Noise, metric, and dynamics data remain necessary to
select a decoder.  A physical seam, boundary, preparation, or reference loop
must be named before ordered logical coordinates are treated as physical.
WP7--WP10 are dispositioned in the continuation milestone.

## Process and optionality snapshot

No honest pre-objective activation/optionality measurement was recorded
before execution; it is not reconstructed retrospectively.  Immediate post
self-assessment: excitement `8/10` (the primal--dual typing failure was
informative), confidence `9/10` for the finite algebra and `6/10` for later
instrument typing, realized information gain `8/10`.  Confounds: the model is
exactly solvable and the finite checks are unusually clean.

Raw delta: the open WP1--WP6 branches were merged into two typed packets;
commutation-derived primal and dual maps, one nondegenerate pairing, and a
full quotient-separating map were constructed; eight aggregate gates passed;
one representative-typing bug and one missing-directory defect were repaired;
instrument-domain typing remains open.  These process observations are not
evidence for the mathematical claims.
