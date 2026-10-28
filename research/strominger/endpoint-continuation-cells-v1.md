# Endpoint-restricted continuations: exact classification and experimental consequences

Status: exact finite mathematical result; physical realization remains a proposed experiment.

## Question and method

Starting from the frozen A4 x Bool fragment, keep all 24 supplied preparations and the Boolean pointer observation. Restrict only the allowed generator alphabet, allowing arbitrary finite words over that alphabet. These restrictions are candidate tasks, not source-selected endpoint protocols.

Enumerate all 256 subsets of the eight generators. For each, compute the stable Moore partition and independently perform paired-state breadth-first search for every unordered pair. This yields 70,656 complete paired-state searches. A failed search proves equivalence for all finite words in that restricted alphabet; a successful search yields a shortest separating word. Verify partition refinement monotonicity under alphabet inclusion.

Checker: `checkers/check_endpoint_continuation_cells.py`.
Receipt: `results/endpoint-continuation-cells/verification.json`.

## 1. The full task needs all 24 predictive states, but only short witnesses

Across the 276 unordered state pairs:

- 144 pairs differ at the current pointer: empty witness.
- 126 pairs have a shortest one-operation witness.
- 6 pairs require two operations.

This confirms the earlier behavioural-minimality result with an independent finite implementation. Every pair has a witness of length at most two; this does not say that one fixed word distinguishes all states.

## 2. A stronger retention experiment than a single hidden-pointer reveal

Use the identity permutation `ABCD` and the permutation `ADBC` (notation lists images of A,B,C,D), both with pointer false.

Every one of the six query predicates is false on both. Consequently, EVERY query-only word leaves their readings identical. They are not merely indistinguishable under one current readout.

But the chronological continuation

    L_ABC ; Q_BC

gives pointer true for `ABCD` and false for `ADBC`.

This is an exact controlled contrast: an entire static query family cannot distinguish the preparations, while a single transport followed by a query can. Include `CBDA` as a third member of the same query-only class if useful; other words can separate the three.

The scientific message is not mysterious information creation. Static observation equivalence is not preserved by all admitted transports. A physical experiment can test retention of exactly this otherwise-hidden distinction, with an erasure control and controller-label-leakage controls.

## 3. One queried input vertex produces a genuine four-position quotient

With both left transports available, and only one query Q_st, the stable state is exactly

    (g(s), b).

There are four possible images g(s) and two pointer values: eight predictive states rather than 24. The identity of t does not affect this count.

Proof:

- Left translation h changes g(s) to h(g(s)), without requiring the rest of g.
- Q_st toggles b according to g(s)=t, which depends only on this coordinate.
- Two different images can be distinguished by choosing a generated h that carries one to t and not the other, then querying.
- Different initial bits are already distinguishable.

Each carrier class contains three A4 elements. These are residual stabilizer/coset distinctions, not three physical RF modes inferred from measurement. The quotient carries the natural tetrahedral vertex action: there is a real tetrahedral mathematical connection here, but not yet a minimal spatial face or coherence-cell law.

The checker verifies the stronger rule for all 64 query subsets when both transports remain enabled:

| Queried input vertices | Sufficient coordinates | Predictive states |
| --- | --- | ---: |
| None | b | 2 |
| Exactly one s | (g(s),b) | 8 |
| At least two distinct s,r | (g(s),g(r),b), determining g | 24 |

Why two are enough: two distinct image assignments leave two completions in S4; exactly one is even. Thus in A4 they determine the entire permutation. This is a discrete transition from one vertex image to the full carrier, not a gradual sequence of tetrahedral faces.

Only A, B and C occur as query input vertices in the frozen six queries. No Q_Dt operation has been added.

## 4. Which transports matter is itself endpoint-dependent

For every individual query, no transport gives four predictive states: pointer and truth of the predicate. Both transports give eight.

A single transport can suffice, but there are two exceptions among the six queries:

- Q_BC with only L_ADB still gives four states: L_ADB fixes C, so the tested equality is invariant.
- Q_AD with only L_ABC still gives four states: L_ABC fixes D.

All other individual-query/single-transport combinations give eight. The target vertex's orbit under the available transport group controls which images the probe can distinguish.

This offers a specific intervention prediction: one transport leaves a probe's distinctions unchanged, another refines them. It is stronger than choosing a cell after viewing a response matrix.

## 5. There is no unique smallest control set for full distinguishability

The 256 alphabets yield 59 distinct partitions. Of those alphabets, 155 distinguish all 24 states. There are 19 inclusion-minimal full-distinguishing alphabets: 18 triples and one quadruple. Examples:

    {L_ABC, Q_AB, Q_BC}
    {L_ADB, Q_AB, Q_BA}
    {L_ABC, L_ADB, Q_BC, Q_AD}

These are alternative minimal control resources, NOT geometric cells. Their multiplicity rules out a unique least full-distinguishing alphabet under inclusion. It does not rule out a least cell in some separately defined geometric model.

A three-generator separating experiment may therefore be substantially narrower than implementing the entire eight-generator language. Its physical correctness claim must remain correspondingly narrower.

## 6. Updated experiment choice

### Retention experiment: sharpened first target

Use preparations indistinguishable under all six static queries, then distinguish them with L_ABC;Q_BC. Measure retention versus genuine physical erasure and independently calibrated continuation. This is a short, exact mathematical target.

### Cell experiment: sharpened hypothesis

Use the coordinate quotient (g(s),b) and the endpoint-dependent effect of transports as the first source-grounded structure. Ask whether a physical response/intervention model realizes that quotient, and whether changing the allowed probes produces the predicted 4-to-8-to-24 changes in predictive-state requirements. Counts refer to exact deterministic task models, not RF dimension or noisy clustering thresholds.

Do not claim that the original proposed source–probe cell law has been derived. A native query's input and target labels still need a justified mapping to physical preparation/probe endpoints. The present result supplies a concrete bridge candidate: the tetrahedral vertex action and its stabilizer, rather than a face that 'lights up'.

## Next decision

Before choosing circuitry, choose between two scientific claims:

1. Transport reveals distinctions invisible to a complete static query family.
2. Changing the observation/transport task changes the minimal sufficient state according to the derived coordinate-quotient rule.

The first has the shortest decisive witness. The second connects more directly to observer-relative structure. They can share an apparatus, but the mathematical targets should remain separate.
