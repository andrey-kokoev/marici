# Cyclic soft-sheet anchor audit

## Question

Do the local `X1`, `X2`, and `X3` soft positive-sheet normalizations overlap and determine a generic cyclic branch of `sqrt(K)`?

## Frozen anchor

Only the `X1` soft strict transform is explicitly constructed. On the physical soft-triangle locus

\[
X_1=0,\qquad X_2=X_3=p>0,
\]

the measure Jacobian cancels the soft square-root factor with unit leading ratio on a chosen positive sheet. The normalized source form is exact in that chart, and the graded observer has nonzero source-normalized readouts at grades zero and two.

The sourced cyclic action formally transports this statement to candidate anchors

\[
X_2=0,\quad X_3=X_1=p>0,
\]

and

\[
X_3=0,\quad X_1=X_2=p>0.
\]

No independent `X2` or `X3` strict-transform artifact was found, so even these transported formulas are symmetry candidates rather than separately checked charts.

## Overlap test

The three physical soft loci have no pairwise intersection for `p>0`. For example, imposing the `X1` and `X2` anchors simultaneously gives `X1=X2=0`, while their equal-energy conditions force `X3=0`. This reaches the triple-soft point and violates `p>0` in both charts.

Therefore the local positive-sheet anchors have no physical overlap on which transition signs can be compared. Their common closure is the triple-soft degeneration, where the strict-transform charts and branch order must be reconstructed separately.

## Generic extension gate

A boundary germ does not determine a branch on a generic nonsoft chamber without a path from that germ into the chamber and proof that `K` remains nonzero along the path. No such path or overlap descent is materialized. Assigning the same sign to the three cyclic anchors is compatible with symmetry but remains an extra gluing convention.

## Strongest falsification attempt

Use cyclic symmetry alone to identify the three chosen positive sheets. This matches their formal local equations but supplies no overlap equality: the anchors are disjoint, and the only common limiting point is singular. Hence symmetry gives candidate signs, not a descent certificate.

## Acceptance test

1. construct independent strict transforms in all three soft charts;
2. construct a resolved triple-soft chart containing their closures;
3. compare sheet signs on nonempty resolved overlaps;
4. provide branch-free paths from one resolved anchor to a generic nonsoft basepoint;
5. verify cyclic closure and reverse one overlap sign as a deliberate failure.

## Disposition

The `X1` local positive sheet does not normalize the generic cyclic branch. Its cyclic images are disjoint physical boundary anchors with no checked overlap; a resolved triple-soft gluing and generic continuation path are missing.

## Evidence

- `research/benincasa/x1-soft-physical-strict-transform.json`
- `research/benincasa/check_physical_soft_triangle_graded_observer.py`
- `research/benincasa/physical-soft-triangle-graded-observer.json`
- `research/nima/qG12-positive-chamber-branch-selection-audit.md`
