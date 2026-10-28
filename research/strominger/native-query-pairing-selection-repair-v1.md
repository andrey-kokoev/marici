# Native query selection: conjecture, falsification, and conditional repair

## 1. Conjecture C1 (to be tested, not assumed)

Fix the unchanged six-arrow seed, its two triangle permutations, and their generated group G=A4. Fix the task-selected native Boolean query

    f_ab(g) = [g(a)=b].

Conjecture: positive pairing, source-relabel covariance, unit-normalized features, and local reversible agreement-fixing exchange suffice to determine a single continuation-response class for this query.

The task reads the six named persistent records at typed route boundaries. The common preparation is carrier zero, record AB equal to one, and all other records zero. No intermediate reset or measurement is performed. The exchange formula, preparation and reader are identical in both models. Source covariance means simultaneous relabelling of vertices, group elements by conjugation, and record labels; the source's actual swap is included. It does NOT mean invariance under independent left translation of the group argument.

This conjecture is stronger than the earlier ambiguity between two different queries: here the query itself is already fixed by the native task. Pairings may vary subject to the stated laws; no physical interpretation of a pairing is presumed.

## 2. Falsification with the SAME query and exchange

Assign a positive weight mu(g) to each of the twelve group elements:

- model U: every weight is one;
- model W: double transpositions have weight two; all other weights are one.

Both weights are invariant even under conjugation by all S4 relabellings. They preserve the same query truth table and its supplied-transport composition law.

More generally put weight d>0 on the three double transpositions and one on the identity and eight 3-cycles. For every off-diagonal edge ab, exactly one double transposition and two 3-cycles send a to b. Thus

    <f_ab,f_ab>_mu = d+2.

Exactly one group element swaps A and B: the double transposition (AB)(CD). Hence

    <f_AB,f_BA>_mu = d,
    normalized overlap = d/(d+2).

Use the positive carrier pairing

    <x,y>_d = sum_g mu(g) x(g)y(g)/(d+2).

Every f_ab is a unit vector in this pairing. This is equivalent to feature normalization; it changes no Boolean query values. A common rescaling of mu cancels, so the difference is not overall normalization.

At port e execute the SAME exchange:

    delta = r_e - <f_e,q>_d,
    q' = q + f_e delta,
    r'_e = <f_e,q>_d,

with other records untouched. Each event is a linear involutive isometry for

    <q,q>_d + sum_e r_e^2.

It fixes all matched states and changes no unread sector. Covariance follows from the query's relabelling identity and the conjugation-invariant pairing. Ordered word evaluation supplies units and composition.

From the common AB-record preparation, both models have budget one. After AB, both have exactly the same coordinate state: q=f_AB and every record zero. The common continuation BA then reads

    model U: r_BA = 1/3,
    model W: r_BA = 1/2.

Consequently C1 is false. The same native question, same prepared records, same first state, same exchange formula and same reader still leave operationally distinct responses. This is a counterexample to selection, not an assertion that both pairings are physically realized.

An isometric identification carrying every named feature to its counterpart cannot remove the distinction: it would preserve their normalized Gram entry. More generally, a context equivalence preserving preparation and record readings would preserve the displayed two-event reading, which it does not.

## 3. Repair C2: separate query authority from pairing authority

A sufficient repaired statement is:

Given the native query, ALSO supply a positive left-translation-invariant measure on G. Specify unit feature normalization, the prepared state and record reader, and require each real linear event to:

1. act only on its selected carrier component and its record, fixing the complementary sector pointwise;
2. preserve the positive quadratic budget;
3. fix every matched state;
4. be nonidentity.

Then the normalized pairing on the selected features and every event map are uniquely determined, up to pairing-preserving coordinate changes. The fixed preparation therefore has a unique response for every authorized finite word.

### Why the repair works

**Measure.** Left invariance says mu(hg)=mu(g) for all h,g. Taking g to be the identity gives mu(h)=mu(identity). Thus mu is uniform; if normalized to total mass one it is 1/12. Feature normalization removes any unfixed common scale. This selects the U Gram and the response 1/3.

**Event.** On the real two-dimensional plane (selected carrier amplitude, record), an orthogonal map fixing the agreement diagonal pointwise is identity or reflection in that diagonal. Nonidentity selects the reflection, namely swap. Locality fixes the complementary sector. This is the prior exchange-uniqueness argument, not a new dynamics proposal.

**Words.** With the same initial state and identical selected event maps, equality of states and records follows by induction on every typed finite word. This is not restricted to the two-event discriminator.

### What the repair does NOT derive

Left invariance is strictly stronger than relabelling/conjugation invariance. Model W proves the distinction. The native query does not itself justify uniform preparation over transports or a physical energy pairing. Those are additional semantic/physical assumptions, not consequences of Boolean evaluation.

The assumptions are sufficient, not proved necessary or minimal. Other independently justified pairings and interaction contracts may select different models. The repaired statement does not supply an autonomous preparation, pointer/reset cycle, calibrated duration, apparatus realization or empirical validation. It must not be promoted to a source-generated physical constructor.

## 4. Verification and relation to prior work

    python research/strominger/checkers/check_native_query_pairing_selection.py

The standard-library checker regenerates A4 from the two documented seed cycles, reads the actual six edges from the existing source contract, constructs their transition tables, and checks exact rational positivity-by-diagonal-weights, equal feature norms, all S4 conjugations, all six event involutions and whole-domain isometries, both complete two-event executions, and the left-invariance separator. It records source hashes and normalized Grams.

The general uniqueness and arbitrary-word statements above are written proofs. This run does not recompile the prior native Agda module or prove a new native physical binding. The finite query is an independent replay of its documented table, with the Agda source hashed for provenance, not a new formal bridge certificate.

Receipt: `results/native-query-pairing-selection/verification.json`.

Prior sources reused conceptually:

- `../nima/native-seed-transition-probe.md`: native query selected by its stated task;
- `../nima/source-group-probe-selection-audit.md`: actual triangle-generated A4;
- `../nima/carrier-probe-adapter-and-state-reference.md`: invariant measure freedom;
- `../nima/record-exchange-uniqueness.md` and `../nima/unread-record-selection.md`: sufficient exchange selection and the full-state agreement distinction.

The new falsifier holds the directed-transition query fixed and varies only a conjugation-invariant pairing. The repair makes the additional measure symmetry explicit instead of silently treating it as source covariance.
