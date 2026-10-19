# Iteration1: certified-image continuations and the actual ambient-exchange boundary

## Fresh state and selected obligation

Read the mutable WG contract at its32-node/v8-pin state. Its recommendation was `wg-phase-relative-roles`, whose next obligation was an interface allowing lossless forward transport without a global inverse. This result addresses that precise obligation; it does not close the root assembly or select the full conceptual phase schedule.

## Certified image with complete provenance

For the existing promotion run:A->B, define

    Generated = Sigma(c:A) Sigma(y:B) (run(c)=y).

The type retains the actual source, target and comparison path without truncation. `pack(c)=(c,run(c),refl)` and `origin` give an isomorphism A<->Generated. Its dependent-record eta path is explicitly constructed, not inferred by erasing proof payloads. This graph-type isomorphism is a general dependent-sum fact; it does NOT assert run:A->B is a global equivalence. The preceding proper-image counterexample is unchanged.

For a source continuation f:A->A, define lift(f,x)=pack(f(origin(x))). `lift-unit` proves the unit up to the dependent eta path, and `lift-compose` proves exact preservation of successive source operations. `Execution(f)` additionally retains the actual pre-execution Generated record, result, and agreement; `execution-input` recovers that original record exactly. Canonical output normalization therefore need not erase the input construction history from the execution package.

## Independently selected target operations need a comparison

An ambient target operation h:B->B lifts with source continuation f when supplied with

    square(c): run(f(c)) = h(run(c)).

`ambient-lift` preserves the actual target h(y), using square(c) followed by cong(h) of the retained image certificate. `compatible-compose` constructs the square for two compatible continuation pairs. This theorem composes the squares; it does not claim a new full higher-coherence theorem about independently supplied squares.

The induced operation h=run composed f composed decode has a square from decode-run. It is one constructed target law, not automatic identification with an independently given h.

## A new, source-specific unavailable-role control

Take h to be the actual next-level exchange G.exchange. The existing counterexample says h(run(input)) lies outside run's image. Therefore NO total source continuation f can provide square(c) for this h on every source. `exchange-not-compatible` proves this by applying the putative square at input.

This is stronger than the previous absence of a global inverse: a concrete valid ambient operation cannot be treated as an image-preserving re-expression of an old-source operation. Exact source recovery does not grant arbitrary target continuation compatibility.

This does not ban exchange as a new generative step. It says that using exchange requires a different/enlarged retained state interface or explicit change of phase, rather than falsely claiming closure in the original certified image. It may retain the original source alongside an extended history; that extension is the next nonredundant task.

## Role/phase consequence

Three situations are now distinguished with actual types:

- a source operation transported within its certified image: constructed;
- an independently supplied ambient operation with a commuting square: conditionally constructed and composable;
- the actual ambient exchange claimed to preserve that image: impossible for every source continuation.

The phase boundary is therefore not merely the name of an operation. It can be the boundary between a fixed certified image and a richer target context. No claim identifies this boundary with one of the operator's numbered rungs or four conceptual stages.

## Verification

New source: `research/strominger/agda/NativePromotionCertifiedImage.agda`.

Executed `python research/strominger/checkers/check_native_promotion_certified_image.py`. Fresh safe Cubical closure with ignored interfaces passed, with stable source/compiler/checker inventories. The first run found a name clash with the Prelude lift constructor; hiding that imported name fixed it. The known owner import warning remains nonfatal. Receipt: `research/strominger/results/native-promotion-certified-image-agda-v1.json`.

No source-owner code was changed. The formal module rechecks the native promotion and proper-image dependencies. No global quotient, universal phase classification, complete137-leaf schedule or physical claim is made.
