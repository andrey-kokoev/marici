# Costed orientation records with an additive comparison budget

## Budget contract

Choose primitive class cost6 from the unit rectangle-cell metric, and require
independent comparison to add class costs:

    Q(h)=6*sum_i h_i^2,
    Q(h_left,h_right)=Q(h_left)+Q(h_right).

Given the previously derived unit-rectangle class scale6/84^(n-1), this contract
sets the weight of each rectangle cell to84^(n-1). The implemented ranks use
weight1 for a primitive record and weight84 for a two-factor record. The budget
law is an explicit architectural choice; the weight conversion follows from it.

## Retained costed records

The store materializes all rectangle-cell values in the harmonic orientation
sector: six cells at rank1 and1152 cells at rank2. Each has a value, weight and
revision. The record also retains:

- normalized class coordinates and the certified harmonic basis;
- the mapped triangle-chain view;
- the minimum unconstrained source lift and its closure-restoring residual;
- immutable parent-snapshot identities for a composed record;
- accepted update and compensation events.

For every committed state, reconstruction from lift plus residual equals the
source cell vector, the source boundary is zero, and

    source cell cost = weighted lift cost + weighted residual cost
                     = 6*sum_i h_i^2.

The store represents the harmonic sector. Other closed source chains can carry
additional boundary-mode data and cost; they are not accepted as independent
state variables in this prototype.

## Updates and composition

A request carries store identity, expected revision and a class-increment vector.
Identity, revision, arity, rational conversion and increment closure are checked
before mutation. A successful serialized commit updates the cell records and
all derived views, records its exact edit cost, and advances the revision.

Comparing two primitive snapshots concatenates their class coordinates and
constructs the two-factor harmonic record. Its source-cell cost is the sum of
the parent costs. Parent links identify those snapshots; they are not automatic
subscriptions to later parent changes.

The checker performs the same differential covector return in two routes:

1. edit the rank2 record directly;
2. edit each primitive record and construct a fresh comparison snapshot.

The routes agree exactly in rectangle values/weights, target view, closure
residual and total edit cost. For a=(1,2) and requested increment1/3, the update
is(1/15,2/15), with cost2/15 on both routes. Revisions and event histories differ
according to the actual operations performed.

## Reversal and provenance

Stale and foreign requests leave the entire store unchanged. Serialized LIFO
compensation restores coordinates, cell values and budget while issuing a fresh
revision and retaining the original event. The tests apply nine further rational
updates and unwind them, recovering the original content and cost.

## Structural result

The primitive and paired harmonic sectors now share an executable costed-record
contract: additive budget, explicit metric weights, chain closure, complementary
records, versioned returns and retained provenance. The direct/staged return
law is implemented on actual higher-cell values rather than only class scalars.

Extending beyond snapshot composition requires live parent-version propagation
and retention of nonharmonic closed-cell modes. A chosen physical readout must
also specify which of these records it observes; the additive budget alone does
not identify energy or a coupling.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_costed_orientation_records.py

The test reruns the primitive and paired chain certificates, then checks costed
record reconstruction, additive promotion, direct/staged differential returns,
full-store rejection invariance and compensation. Exact Fraction identities
certify all budgets and updates. The paired least-norm solver's numerical proposal
is accepted only after its rational certificate passes. Storage is in-memory
and serialized; the implementation is scoped to ranks1 and2.
