# Vacuum-tail splitting has an order-independent restriction certificate

## Result

The coherence layer now supports a genuine increase in source/observer coordinates: split an unacquired aggregate vacuum tail into a newly exposed coordinate and a remaining tail.

A portable certificate verifies two different splitting orders leading to the same three-coordinate task. The coarse and both intermediate problems are ambiguous; the common refined problem certifies positivity. Both restriction routes agree exactly.

This is a finite source-aggregation and acquisition result. It is not a claim about arbitrary observer modules, infinite inverse limits or filtered attachment transport.

## 1. Actual source interpretation

Use real coefficients b_A of the admitted forgotten cubic products k_A at arithmetic backgrounds A>=3, with

`sum_(A>=3) 8(A/2)^12 |b_A|<=40`.

Each b_A is the unit vacuum readout of its labelled product. The scalar task is positivity of their sum. Retained-feature coefficients are absent from this restricted example.

Define T_r=sum_(A>=r)b_A. The triangle inequality gives

`8(r/2)^12 |T_r| <= sum_(A>=r)8(A/2)^12 |b_A|`.

A scalar aggregate coefficient can be realized by a finite source at its first permitted background. Thus the aggregate budget is a valid coarse model and its finite witnesses have actual source realizations. The interval |T_r|<=40/[8(r/2)^12] is prior-derived, not a measured vacuum channel.

## 2. The two refinement routes

Starting with T_3, compare

`T_3 -> (b_3,T_4) -> (b_3,b_4,T_5)`

and

`T_3 -> (T_34,T_5) -> (b_3,b_4,T_5)`,

where T_34=b_3+b_4. Its coarse cost weight is 8(3/2)^12; this does not assert that b_4 has the same true moment cost as b_3.

In the final problem the returned intervals are

`b_3 in [0.001,0.002]`, `b_4 in [0,0.0001]`.

The rest is unacquired and budget-bounded. The common final task is b_3+b_4+T_5>0. Its solver certificate includes both a feasible witness and a universal dual bound.

The two routes induce the same restriction T_3=b_3+b_4+T_5. Coordinate counts increase, unlike the preceding diagonal-rescaling squares.

## 3. Edge checks

A tail-refinement edge supplies a partition of new coordinates into nonempty groups, one for each old coordinate. Every new coordinate must occur exactly once. Restriction sums the coordinates in each group.

The verifier requires:

- each new cost weight is at least its parent weight and the new budget does not increase;
- each target coefficient is copied to all its child coordinates, with the threshold unchanged;
- split groups have unit calibration;
- an old aggregate data interval contains either the summed child intervals or the full aggregate range already implied by the new budget;
- singleton rows retain compatible calibration and data enclosures.

The weighted triangle inequality proves source-budget transport. Unit calibration makes the observation sum agree with the source sum. The interval rule prevents discarding an already acquired constraint while splitting a coordinate.

These are sufficient rules, not a general characterization of all valid aggregate refinements. In particular the verifier does not split an unknown feature response into several differently calibrated signals.

## 4. Coherence and preservation checks

The square verifier independently checks all four node certificates and edge certificates, flattens the two nested partitions, and requires equal final groups. It also verifies the induced direct edge.

The test rejects a missing/duplicated coordinate and a proposed split that would erase an old exact aggregate reading. Isolated verification succeeds outside the repository using only the task verifier, tail-refinement verifier and square JSON.

This proves that the selected refinement order does not alter the declared task restriction. It does not promise that all feasible coarse states extend to the finer model; new acquisitions can exclude them.

## 5. Fixed calibration remains fixed

Voevodsky's `../voevodsky/the-current-calibration-refinements-fix-one-physical-sector-ratio-not-a-family-of-observers.md` clarifies that the existing numerical calibration refinements concern ONE physical theta detector. Tighter bounds on its ratio do not instantiate a family of different source kernels.

This tail example introduces additional labelled vacuum coordinates and source aggregation maps; it performs no physical parameter sweep. Calibration-dependent source policies elsewhere remain uncertainty certificates, not assertions that all enclosure points are realized physical settings. Installing new relative sector coefficients would require a separate detector/source audit.

## Verification

`python research/nima/checkers/check_tail_refinement_coherence.py`

Portable verification:

`python research/nima/certificates/verify_tail_refinement.py research/nima/results/tail-refinement-square.json`

The verified node statuses are AMBIGUOUS at the coarse and both intermediate nodes, and TARGET_TRUE at the final node. All examples are conditional synthetic acquisitions under the explicit moment prior.
