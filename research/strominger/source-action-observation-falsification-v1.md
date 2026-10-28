# Falsifying universal source–action–observation existence

## Verdict

The **unconditional nonempty-existence reading** of the proposed Source–Action–Observation Correspondence Conjecture is false. The actual six-arrow source, its free path-realization task, and its original discrete endpoint observation cannot all be preserved by one diagram.

The earlier wording was not a fully quantified conjecture. If “determines a family” allows an empty family, this counterexample does not refute that weak classification claim. Nor does it refute existence for some compatible observation tasks. It does refute a guarantee of simultaneous realization, action and observation for independently declared tasks without a compatibility premise.

The failure is before empirical physics. No empirical model or prediction was specified by the proposed conjecture, so this packet does not claim an empirical falsification.

## Frozen test, not a repaired target

Use the unchanged source:

- vertices A, B, C, D;
- occurrences AB, BC, CA, AD, DB, BA;
- sigma=(A B)(C D), exchanging AB/BA, BC/AD, CA/DB.

Take the already declared free-incidence task: each occurrence becomes a path between its endpoint images. Retain the original discrete native observation type `NativeExtensionFamilyAudit.Vertex`. First ask that the observation recover the original endpoint label. Then test the weaker condition that it merely be sigma-equivariant, without label recovery.

This freezes both the realization and observation meanings. It does not assert that all physically useful observations must be discrete or homotopy-invariant.

## Obstruction 1: no endpoint decoder for any such realization

Let X be any type, with points p_v and the required AB attachment

    gamma : p_A = p_B.

If an observation o:X->Vertex recovers each original label, congruence gives

    A = o(p_A) = o(p_B) = B,

contradicting distinct vertex constructors.

This is not peculiar to the bouquet presentation, a choice of spanning tree, or a particular producer. Every realization retaining this attachment path fails the requested decoder. The prior free-realization packet already proved the special case; the new proof states the obstruction for arbitrary X.

## Obstruction 2: even equivariance without label recovery is impossible

Suppose an action map a:X->X sends p_A to p_B and the observation obeys

    o(a(x)) = sigma(o(x)).

The same attachment gives

    o(p_A) = o(p_B) = o(a(p_A)) = sigma(o(p_A)).

But sigma has no fixed vertex. Contradiction.

Thus relaxing exact label recovery is insufficient. There is no equivariant observation into this fixed discrete target at all. Additional action coherence cannot repair failure of this necessary one-step equation.

In particular, factoring the observation through a structured or physical model does not help if its composite is still required to be this equivariant map.

## Positive control and verification

`agda/SourceActionObservationObstruction.agda` constructs `swap` on the actual `SeedTetrahedronBridge.Realization`, mapping all six attaching paths to their actual swapped occurrences. It proves `swap²` by HIT clauses. It then proves:

- `AnyRealization.no-endpoint-decoder`;
- `AnyRealization.no-equivariant-decoder`;
- `no-actual-equivariant-decoder` for the actual free realization.

The positive control shows that the obstruction is not simply failure to define the source swap. The packet does not claim an all-dimensional BG-action structure.

Fresh headless Agda checking passed with `--safe --cubical --guardedness --ignore-interfaces --no-libraries --no-import-sorts`, using the existing four owner include roots and Cubical 0.9. The run log is `results/source-action-observation-obstruction/agda.log`. This run did not create a new full dependency-lock manifest or update net pins.

An independent exhaustive Python integer/enumeration check considered all 256 node assignments into the four discrete labels. Exactly four satisfy all edge-equality conditions (the constant assignments); zero recover endpoints; zero commute with sigma. This finite check corroborates the obstruction but does not replace the universal Agda proof.

## Consequence for the proposed high-level conjecture

The proposal silently treated two distinct requirements as automatically compatible:

1. interpreting a directed source transition as a path/equality in the realized object;
2. retaining a discrete observation that distinguishes its endpoints.

They are not compatible. “Observable faithfulness under all future contexts” makes this failure more pronounced: the original endpoint observation already distinguishes the endpoints before any future context is added.

A viable successor must explicitly admit partiality/refusal, or change a declared interface. Possible changes include keeping endpoint labels as external construction provenance, supplying a dependent observation family with transport, using a different nondiscrete observation target, or interpreting arrows as transitions rather than equalities. Each requires a new typed contract and its own compatibility proof; none is a rescue of the frozen statement tested here.

No claim that the source uniquely selects one repair follows. No blanket nonexistence claim for source-faithful realizations follows either.

## State boundary

The completed revision-27 theorem concerns certified finite-reader/mixed operations and explicitly excludes this topology-changing extension. It is not contradicted. Its contract, verdicts and immutable pins remain unchanged. The three downstream obligations remain blocked rather than being closed by this counterexample.
