# Observer coordination requires timely information, not always a common commit

## Test question

Can different observers of one source development issue sound, mutually compatible decisions by a deadline without a common commit boundary?

Nima's `../nima/versioned-observer-coherence-does-not-require-a-completion-barrier.md` already establishes versioned coherence and retention for a bounded-error integrator. The present test adds a decision deadline on the actual forgotten-source history, rather than duplicating that transport test or inferring control performance from coherence alone.

This is an exact finite observer-decision experiment, not a simulation of subsequent physical actuation.

## Source history and evidence

The initial source is q=a_P P+a_Q Q. The admitted history appends P-Q in blocks two and three. Actual marked-source multiplication verifies the history map.

Observer A measures the INITIAL terminal value a_P+a_Q at source stage zero. Observer B measures the FINAL canonical vacuum value a_P at stage two, in the affine presentation 2*a_P+3.

The shared prior is -2<=a_P,a_Q<=2. A's interval radius is 1/10; B's display radius is 1/5, equivalent to radius 1/10 in canonical coordinates.

The task is to certify a_Q>=1/20 or a_Q<=-1/20 by wall-clock time five. The certificate must hold on the entire compatible source polygon, not merely its center. Indeterminate evidence is not guessed into a definite answer.

For the positive fixture q=(7/10,3/10), the evidence is

    9/10 <= a_P+a_Q <= 11/10,
    3/5 <= a_P <= 4/5.

Together these imply 1/10<=a_Q<=1/2. Either observation alone leaves both signs possible. The full correlated history is retained as the image of this joint polygon under the admitted transition map.

A second fixture q=(13/10,-3/10) has the SAME initial terminal evidence but a different final vacuum interval and implies a negative a_Q.

## The asynchronous schedule

A samples at time zero and finishes at one. B samples at time two and finishes at four. Data from A take three units to reach B; data from B take one unit to reach A.

Therefore:

- B has both facts and issues its certificate at time four.
- A has both facts and issues its certificate at time five.

They use the same source/history contract but do not wait for mutual acknowledgement, simultaneous readiness or a common commit time. Both meet the deadline and issue the same sound sign certificate in each fixture.

A fixed scheduled commit at five also succeeds. The test does not manufacture a claim that synchronization necessarily fails.

For comparison, a PARTICULAR mutual-ready acknowledgement protocol completes at time eight and misses the deadline. All policies have the same observation and message schedules; this protocol adds a waiting condition, not extra sensing accuracy. Its failure is not a lower bound for every conceivable barrier protocol.

Both local certificates in this example ultimately use the same two facts. What is absent is a protocol requiring the observers to establish mutual readiness before certifying them.

## A genuine timing impossibility

Increase the B-to-A message delay from one to six. No B-dependent information reaches A by the deadline. B can still certify at four; A can only certify at ten.

The positive and negative fixtures give A exactly the same received transcript through time five, yet require opposite answers. Thus no causal rule using that transcript can guarantee the correct definite answer in both worlds by the deadline.

This is stronger than observing a failed scheduling heuristic. It is an indistinguishability obstruction. A new shared clock or an extra acknowledgement cannot supply the absent distinguishing evidence.

The remedies would have to change the information or task contract: faster delivery, another measurement, a justified stronger prior, a later deadline, or permission to abstain.

## What coordination still requires

The successful asynchronous case retains:

- a common source/history identity;
- the correct source stage of each observation;
- the actual observation anchors and affine normalization;
- the joint interval constraints, without independent re-boxing;
- the admitted dynamics and bounded message-delivery model.

Negative controls show that treating B's affine display as a canonical reading creates a false inconsistency. Moving A's INITIAL terminal evidence onto the FINAL terminal row also creates a false inconsistency: the final source lies in I and has terminal zero.

Neither error is repaired by making the observations arrive simultaneously.

## Conclusion

For this task, observer coordination requires timely access to enough compatible evidence, but not a common commit boundary. There is still an information dependency: neither observer can certify from its own measurement alone.

The meaningful timing constraint is that distinguishing information must arrive before the required decision. It is observer- and task-relative, not a fundamental periodicity established by this experiment.

This does not settle tasks requiring simultaneous irreversible actions, mutual knowledge of commitment, consensus under message loss, or uncertain source dynamics. Such requirements would change the decision contract and can introduce additional coordination obligations.

## Verification

    python research/voevodsky/checkers/check_observer_coordination_deadline.py

Artifact: `results/observer-coordination-deadline.json`.

The checker uses the existing exact rational history-polytope machinery, verifies source products and anchors, retains whole correlated history vertices, tests both signs and delivery schedules, and exhibits the identical-transcript obstruction. All checks pass. Every example is synthetic and conditional on the admitted source/history model.
