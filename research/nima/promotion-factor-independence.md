# Does promotion create independent factors?

## Test the two projections, not just the pair count

Start with the full four-label off-diagonal relation, whose Dowker complex is
S^2. For each constrained pair relation, pull back the primitive degree2
cohomology generator along its two coordinate projections. Compute the rank
of their span modulo coboundaries. Rank2 means the two primitive classes survive
independently; rank1 means only one direction survives.

All calculations use exact rational simplicial chains. A cocycle evaluating
on the oriented triangle(0,1,2) represents the primitive sphere generator.
Degenerate projected triangles evaluate to zero. The checker verifies both
pullbacks are closed, then computes their rank modulo the row space of d2.

| Pair construction | Arrow pairs | Nonzero Betti numbers | Projection-class rank |
|---|---:|---|---:|
| Independent ordered pairs | 144 | b0=1,b2=2,b4=1 | 2 |
| Same arrow in both slots | 12 | b0=1,b2=1 | 1 |
| Equal source endpoints | 36 | b0=1,b2=1 | 1 |
| Equal target endpoints | 36 | b0=1,b2=1 | 1 |
| Composable arrows (first target=second source) | 36 | b0=4 | 0 |

For the rank1 cases the two projection cocycles represent the SAME class.
For independent pairs, explicit sphere cycles vary one source coordinate while
holding the other fixed. The two projection cocycles evaluate on these cycles
as a diagonal matrix with nonzero entries. This directly witnesses independence.

Sharing a fixed reference tag preserves the independent pair relation: forgetting
the tag is a bijection. Equating variable endpoints imposes a different, measured
constraint. These operations have different consequences despite both being
described informally as sharing a reference.

## Trace the implemented promotion

Incoming-family promotion groups the12 primitive arrows into four freshly
labelled records. Each retains its original arrow IDs and members. Drill-down
reconstructs precisely the same12-arrow relation and its single degree2 class.
The new label supplies an address, with no second independent operand.

As a separate scalar edit control, encoding the same12 leaf values in two
presentations maps x to (x,x). This map has rank12. Two independently writable
12-value copies would have24 independent scalar directions. These edit ranks
are a check on copied state, distinct from the topological degree2 calculation
and from assigning arbitrary values to144 pair records.

In the existing fixture, the two factors are introduced BEFORE family promotion,
by the explicit constructor product(primitive_arrows, repeat=2). The promoted
source and target presentations then index that already paired record set.
Consequently the measured b2=2 belongs to the pair constructor of the restored
fixture. The grouping operation has not generated another factor.

## Consequence for the tower

The candidate doubling mechanism requires an independently variable second
comparison operand at each recursive step. The current retained-family
promotion supplies another presentation of one operand. Its coherence and
edit machinery preserve that operand's data.

The next architecture decision is explicit: does a promoted family participate
in a new all-pairs comparison with an independently selected family? If so,
that comparison constructor must be represented separately from fresh labelling,
with its two projections, admissibility constraints and reference policy.
The tests above provide the acceptance criterion: both primitive projection
classes must survive independently at the intended step.

Composable pairing and equal-endpoint pairing fail that criterion in this
fixture. Independent pairing passes. The absolute137-slot input still has disk
factors; its removed-arrow/reference data need their own treatment to support
sphere classes.

## Verification

    python research/nima/checkers/check_promotion_factor_independence.py

Five exact homology computations, induced projection-class ranks and equality
checks, two explicit independent sphere slices, shared-tag recovery, retained
family drill-down and scalar diagonal-edit rank. The computations use the
shared biclique_complex.py utilities with optional returned Dowker face labels.
