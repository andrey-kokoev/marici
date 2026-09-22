# Source/observer change squares have portable coherence certificates

## First deliverable

There is now a verified change layer above the scalar task certificates: it checks a finite square of source-coordinate/prior changes and observer-coordinate/data refinements, together with the task certificate at every node.

Two squares pass, including one built from a saved physical-source task model. Both routes induce the same source, observation and target maps. A deliberately noncommuting square is rejected even though its four edges individually pass.

This is a first RESTRICTED coherence product, not certification of arbitrary source/observer towers. It supports positive diagonal coordinate changes and monotone refinements in the declared real scalar model. It does not verify new channel additions, source-ideal actions, filtration changes or derived-class transport.

## Physical calibration boundary

As clarified in `../voevodsky/the-current-calibration-refinements-fix-one-physical-sector-ratio-not-a-family-of-observers.md`, narrowing the present theta-calibration enclosure leaves ONE actual detector and its source kernel unchanged. Its physical structural comparison is the identity. The parameter-box transport below is a model/evidence calculation, not proof that every boxed value is a realized observer. Whole-row coordinate gains are distinct from installing new relative sector coefficients.

## 1. What an edge means

For positive rational scale vectors a,b and scalar g>0, declare

`x_new=diag(a)x_old`,

`z_new=diag(b)z_old`,

`E_new=diag(b/a)E_old`.

The source and observation maps relevant to restriction point BACKWARDS:

`T_source(x_new)=diag(1/a)x_new`,

`T_observer(z_new)=diag(1/b)z_new`.

For a compatible parameter E_old=diag(a/b)E_new, the observation square is exactly

`O_old T_source = T_observer O_new`.

This is checked for the declared model reparameterization. When an edge relates physical protocols, the assertion that their actual calibration parameters obey that relation is an external model-identification hypothesis. Overlapping numerical calibration intervals alone do not establish it.

## 2. What the edge verifier checks

Each edge certificate binds the old and new problems by digest and contains only the scale vectors and target scale. The verifier independently requires:

- the new calibration box, pulled back by a/b, lies in the old calibration box;
- the new reading intervals, pulled back by 1/b, lie in the old intervals;
- w_old,i/a_i <= w_new,i and B_new<=B_old;
- t_new,i a_i=g t_old,i and threshold_new=g threshold_old.

The budget inequalities are a conservative sufficient rule, not a characterization of every possible valid budget transformation.

For each new feasible parameter/source pair (E_new,x_new), these conditions give an old feasible pair with the same source-relative task truth value. They also transport observation uncertainty through its declared scale: a new scalar radius epsilon pulls back as epsilon/b_i. No measurement precision is manufactured by changing units.

A stronger new prior is recorded as a change of assumption. The verifier proves its implication for the old model; it does not justify that stronger prior physically.

## 3. What survives a change

A universal old task statement remains true of every feasible new source under the compatible parameter map. But new constraints may empty the feasible set. Therefore a non-vacuous new task conclusion still needs a newly verified feasible witness.

The test suite explicitly checks an edge from a nonempty TARGET_TRUE problem to an INFEASIBLE refinement. It rejects the interpretation that old feasibility must automatically persist.

Similarly an old ambiguity need not survive refinement: its opposing witnesses may be excluded by the new data. The demonstrated square begins ambiguous and becomes task-certified after observation refinement.

Nothing here transports a new calibration-dependent witness to ALL old calibration values: the pulled-back new calibration box may be a proper subset of the old one. The statement is about compatible parameter/source pairs.

## 4. Coherence is stronger than four valid transitions

The portable square contains nodes 00,10,01,11, their numerical task certificates and the four edge certificates. The verifier checks all nodes and edges, then composes both routes:

`00 -> 10 -> 11`,

`00 -> 01 -> 11`.

Composition multiplies source scales, observation scales and target scales. Both products must agree exactly. The induced direct edge 00->11 is checked again against the endpoint problems.

This composition law is associative for finite chains. The implemented verifier checks a square; it does not silently establish coherence of an unprovided infinite diagram.

A corruption test doubles all three scale types on one edge. That edge remains individually admissible because its pulled-back constraints still refine its parent. Nevertheless its route disagrees with the other route, and the square verifier rejects it. Thus node validity and edge validity are insufficient substitutes for route coherence.

## 5. Demonstrated squares

The first example combines:

- source scales (2,3), with an explicitly tighter source budget;
- observer scales (5,7), with narrower data and calibration intervals.

The source-first and observer-first constructions yield the exact same final problem. Node statuses are

`00: AMBIGUOUS`, `10: AMBIGUOUS`,

`01: TARGET_TRUE`, `11: TARGET_TRUE`.

The second square applies declared coordinate rescalings to a previously certified physical-source task problem. It checks the scalar model transport; it does not automatically transport that problem's external source-specific assumptions or a structural manifest.

## 6. Independent and portable evidence

New checker:

`research/nima/certificates/verify_diagonal_transition.py`.

It uses the hardened standalone task verifier for node certificates and strict JSON parsing. It imports no solver, producer, numerical integration package or source recorder.

The test run verifies two squares, rejects six invalid edges/routes, checks the feasibility-loss example and executes outside the repository under isolated Python using only the two verifier files and one square bundle.

Run the producer/tests:

`python research/nima/checkers/check_source_observer_coherence.py`

Verify a saved square:

`python research/nima/certificates/verify_diagonal_transition.py --square research/nima/results/source-observer-square.json`

Artifacts:

- `research/nima/results/source-observer-square.json`
- `research/nima/results/physical-source-observer-square.json`
- `research/nima/results/source-observer-coherence-tests.json`

## 7. Boundary of the architectural claim

This layer verifies that a supported source-model change and observer-model change continue to express the same scalar task, with explicit parameter and uncertainty transport. It is a concrete beginning of coherence between the two productization paths.

It is NOT yet a certificate that source-algebra actions, inherited ideal-depth filtrations, corrected module frames or adjacent extensions commute with these numerical changes. Those require typed structural maps and their owning proofs. In particular the filtered/unfiltered cubic distinction must not be inferred from a commuting scalar diagram.

The next enlargement should supply another explicit transition type and its verification obligations, rather than relabel this finite diagonal result as a general observer-tower theorem.
