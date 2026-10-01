# Primitive comparison task: two probes answer different questions

## Source audit

The original seed/table construction makes AB a labelled occurrence with endpoints A and B. Its primitive operations expose endpoint fields, form fibers, retain members and re-present those records. None of these declarations supplies a permutation g as a physical action executed by that occurrence.

The carrier-probe construction introduces a DIFFERENT argument: g in S4 acts on vertex labels and therefore on directed relation labels. The following two functions ask different questions of that argument.

| Probe | Operational mathematical query | Not automatically implied |
|---|---|---|
|Endpoint fixing f_AB(g)|Does g preserve the labelled relation AB, i.e. fix A and B individually?|Does executing AB transfer a state from A to B?|
|Directed transition t_AB(g)|Does g send A to B?|Does g preserve the AB record or realize its primitive execution?|
|Retained row lookup|Which occurrence has these source/target fields?|A probability measure, feature metric or state-change operation|

Endpoint fixing is the literal restriction of the earlier fixed-label stabilizer probes. Directed transition is another source-equivariant query, not the same query with a more faithful normalization.

## Exact query controls

For every supplied nonidentity seed edge:

- 2 of the 24 permutations fix both endpoints;
- 6 send its source to its target;
- these sets are disjoint;
- the remaining 16 satisfy neither;
- identity satisfies endpoint fixing and fails directed transition.

Consequently no scalar normalization can make the queries agree. Relational preservation and state transfer must not be treated as interchangeable meanings of a primitive comparison.

The transition indicators obey

    t_st(h g) = sum_v t_sv(g) t_vt(h),

with all four intermediate vertices included. This is composition of actual supplied permutations, not a proof that the six seed edges form a closed transition-operator basis. Endpoint-stabilizer membership is not multiplicative under arbitrary composition: two permutations outside the stabilizer can compose to identity.

The existing endpoint-fixing field also reads all slot coefficients at the identity carrier pair; transition probes for nonidentity edges vanish at identity. Transferring that old identity-readout recipe to the transition field would therefore change the measurement, not preserve it. The prior faithful marked-context adapter has its own decoder and extra marking; it does not make these two probes equivalent.

## What the source selects

The requirement 'use the existing S12 fixed-label probe restriction' selects the endpoint-fixing query as a mathematical construction. The seed's occurrence-incidence specification does not identify it as physical exchange coupling. Nor does the label AB alone select the transition query as its physical task.

Both may be retained as separate mathematical observation channels over the same group argument. This does not prescribe adding them with equal weights, declaring them independent physical resources, or driving one exchange event with both. The choice of prepared transformation, interaction and interrogation remains additional operational data.

The native compare rule is yet a third typed operation: a supplied equivalence acting between complete packages with a marked-value witness. Its existence is not an instruction to equate either indicator query with primitive traversal.

## Result and next decision

The audit locates the remaining ambiguity in the MEANING of the physical task, not in the computed overlap tables. To select an exchange kernel, the source must say what transformation is prepared and what primitive comparison tests: persistence of a relationship, transfer of a marked value, or another specified interaction. It must then connect that task to the exchange carrier and record.

Until that statement is supplied, keep the two conditional predictions separate. Do not infer a transition measurement from arrow notation or a physical stabilization interaction from a stabilizer Gram. No new task definition is imposed in this audit.

## Verification

    python research/nima/checkers/check_seed_probe_exchange_bridge.py

Fresh exact checks pass. Added tests cover disjoint query supports and identity controls for all six edges, all 24^2 permutation compositions and all intermediate states, and a stabilizer-multiplicativity counterexample. Existing kernel and exchange-discrimination checks remain intact. No physical preparation or calibrated readout was derived.
