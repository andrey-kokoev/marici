# 4005 — The Repaired Low Quotient Has a Canonical Occurrence Transition

## Question

Entry 4001 left the residual action on (A_7/L_5) undefined because the available chart transition belonged to the retracted ambient-reduction presentation.

SCC identified one admissible constructor: derive the (G_{12}	o G_{31}) map before any nonfaithful reduction or serialization.

## Construction

In each chart, retain the 36 simple-pole monomials of degree at most seven and derive the ten relations that close internally in that sector. Their quotients have rank 26.

Apply the labelled occurrence inversion

[
(i,j)longmapsto(j,i)
]

with the source-derived Poincaré-residue orientation sign (-1) to the raw monomials. Reduce only by the target chart's ten internal relations.

No ambient coordinate is discarded.

## Two-prime result

At primes (32009) and (32003):

- source internal relation count: 10;
- target internal relation count: 10;
- every source relation maps to zero in the target quotient;
- the induced transition has rank 26;
- the transition carries the canonical source (L_5) onto the independently derived target (L_5).

Thus the naturality square for the physical rank-five infinity map closes directly on the repaired quotients.

## Remaining gate

This does not yet define an action on (A_7/L_5).

The existing (A_7) packets were computed and serialized in the legacy ambient-reduction convention. They cannot be imported into the repaired quotient merely because both presentations have rank 26.

The next finite task is to reconstruct the source and target (A_7) planes directly in the repaired internal low quotients. Only then may one test whether the new transition preserves (A_7) and descends to (A_7/L_5).

## Narrow conclusion

The obstruction of Entry 4001 is partly resolved:

- the repaired occurrence transition exists;
- it is source-authorized;
- it preserves (L_5);
- the residual action remains undefined solely because repaired-convention (A_7) has not been constructed.

## Artifacts

- `research/benincasa/checkers/check_repaired_low_occurrence_transition.py`
- `research/benincasa/results/repaired-low-occurrence-transition-p32009.json`
- `research/benincasa/results/repaired-low-occurrence-transition-p32003.json`

Sequence claim: `seqclaim-3506d040e4c4a2265f6107a3`.
