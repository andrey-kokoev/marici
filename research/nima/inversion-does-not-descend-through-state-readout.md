# Inversion does not descend through state readout

## Question

Can the inverse process required to recover a source relation be reconstructed
from the final state or its objective record alone?

## Claim boundary

Let (mathcal P) be a category of source-authorized processes and let
(mathcal S) be a category of state readouts. Evaluation on a declared source
state (x) gives a forgetful map

\[
E_x:mathcal P\longrightarrow\mathcal S,
\qquad
E_x(U)=U(x).
\]

If two distinct invertible processes (U,V) satisfy

\[
U(x)=V(x),
\]

then (E_x) is not faithful on those processes. Their inverses differ even
though their final readout agrees. Consequently, no function of the final
readout alone can return the correct inverse for both histories.

Inversion descends through a quotient of process histories only when that
quotient is faithful for the inverse action required on the admitted recovery
domain.

## Exact finite witness

On four basis states, take

\[
U=I
\]

and let (V) fix states zero and one while exchanging states two and three.
For source state zero,

\[
U(0)=V(0)=0,
\]

but

\[
U^{-1}\neq V^{-1}.
\]

The same ambiguity survives every readout restricted to the visible subspace
spanned by states zero and one. It is exposed only by process provenance or by
probing the hidden recovery domain.

## Required repair

The reversible object must retain a typed process record

\[
(x,U,U(x)),
\]

not merely the endpoint (U(x)). The process record needs enough information
to distinguish inverse-action equivalence classes. For the two-class witness,
one additional bit is necessary and sufficient.

Redundant copies can protect that bit against faults, but they do not reduce
the information needed to distinguish the classes.

## Controller regress

Storing the process record moves the recovery obligation into a controller
memory. Three cases remain distinct:

1. The memory is retained reversibly, so the global inverse remains available.
2. The memory is retained but becomes inaccessible, so reversal is blocked by
   control support or authority.
3. The memory is reset through a many-to-one operation, so process distinction
   is physically discarded into another carrier or environment.

The third case is where a thermodynamic erasure analysis may apply. It does not
apply merely because the system evolved through a long reversible circuit.

This produces a tower rather than a paradox. Every reversible inverse requires
a sufficiently faithful control record. The tower terminates operationally at
the first layer whose record is erased, unavailable, or outside the admitted
controller.

## Categorical consequence

Objective state formation and reversible process recovery point in opposite
directions:

- objective descent intentionally identifies globally distinct states or
  histories that have the same admitted records;
- inversion requires enough provenance to distinguish histories with different
  inverse actions.

Therefore the objective-record quotient generally cannot also be the carrier
of complete reversal authority. A separate process-provenance object and an
interface coherencer are required.

## Disposition

The finite descent obstruction is closed. The arrow of practical
irreversibility can be located precisely at a nonfaithful forgetting of process
provenance, but the theorem does not claim that nature fundamentally erases
that provenance. It identifies what an actual physical model must demonstrate.

Verification is provided by
`research/nima/checkers/check_inversion_descent_through_readout.py` and
`research/nima/results/inversion-descent-through-readout.json`.
