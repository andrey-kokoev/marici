# Closed indexed composition of witnessed refinements

## Problem and discriminating test

The earlier relative `FullComposition` retained a chosen pair's sources, but was not a reusable composition operand. The conjecture tested here is that dependent admission **and proof-dependent witness extension** suffice to construct a composition closed in one indexed refinement family. The rival retains only endpoints or projected laws and consequently cannot represent a second layer that depends on the first layer's actual proof.

SCC obligation: forward realization and full-step route/coherencer compatibility on a fixed universe of total WGs. No physical-time or readout-descent interpretation is assigned. The owner-local model is `scc-models/composable-witness-specialization.json`.

## Construction

`agda/ComposableWitnessSpecialization.agda` defines `Refinement L` with source data, an admission family, advancement along the actual base generator, an `Extra` type indexed by each individual base witness, and a certificate for that generated edge. Compilation extends both state and relation by dependent pairs.

The closed operation has the signature

$$
\mathsf{compose}:\prod_{F:\mathsf{Refinement}(L)}
\mathsf{Refinement}(\mathsf{compile}(F))\to\mathsf{Refinement}(L).
$$

It is an **indexed** operation, not a function on two unrelated domain specifications. Typing the second operand over the compiled first makes the shared interface explicit. Admission becomes a dependent pair. For a base witness $r$, the composite extra witness is a pair $(e,f)$ where $f$ may depend on $(r,e)$. The composite advancement and certificate are constructed from those of its operands; no finished composite, equivalence, or associator is requested as input. Source records are retained as a product.

`Composite.correct` supplies a state isomorphism, isomorphisms of **all** endpoint-plus-witness step packages, endpoint compatibility, and equality of generated steps. Both directions preserve individual proofs. `FromDomain` embeds the existing compatible-domain compiler; `compiler-agrees` is reflexivity on the entire compiled WG.

`Composite.rebase` moves a third refinement from the nested compiled target to the flattened one, including its witness indices. `Associativity` then compares the actual expressions `compose (compose F G) (rebase F G H)` and `compose F (compose G H)`, not just two names for one already compiled relation. It constructs the full-step associator and a source-product associator preserving the actual sources. `Units` proves left and right behavioral unit comparisons, using an explicit pullback across the empty refinement for the left unit. These are realization certificates, not literal equality of source-record types.

`Composer.solve` accepts a base WG and two indexed refinements and returns a composite in that same family plus its realization certificate. `Composer.WG` packages the request/answer transition as a WG and retains the input request. Leaf refinements must still supply their advancement and generated-edge certification; this constructor does not discover arbitrary domain compatibility.

## Proof-sensitive fixture

`ProofDependentFixture` uses Boolean negation with Boolean admission flags that also change on each step. Its first layer carries a Boolean proof payload. The second requires that **that payload** equal the first input's admission flag. `rejects-erasure` proves that substituting `false` for the required `true` payload is impossible, even at the same endpoints and with the same original relation witness. This is a typed impossibility theorem, not a compiler-negative test.

A third proof-dependent layer consumes the result through `rebase`. `reused-is-left` confirms the composite is reusable as an operand; `generated-associator` checks the associator on the resulting nonidentity generated step. `returned-composite` checks that the composition WG actually returns the constructed composite.

## Verification

Run the existing entrypoint:

`pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module ComposableWitnessSpecialization -Fresh`

The launcher initially failed because the command-service environment did not recognize `.EXE` as an executable extension. The canonical checker now restores that recognition when absent, supplies the safe Cubical flags and adapter include paths, and records stable compiler, checker, adapter, owner-source and library hashes. No transient wrapper was used to execute Agda. The earlier direct-command policy refusal is superseded by this operator-identified admitted checker route.

Fresh Agda 2.8.0 with `--ignore-interfaces --safe --cubical --guardedness --transliterate` and Cubical 0.9 passed after all declarations and the fixture were added. Receipt: `results/agda-ComposableWitnessSpecialization.json`; log: `results/agda-ComposableWitnessSpecialization.log`. The pre-existing `TypedGeneratorLayers.agda` import warning remains.

`checkers/check_composable_witness_specialization.py` validates receipt freshness against the current compiler and full recorded source inventories, and rejects an incremental receipt in a fail-closed control; it does not launch a compiler. `python research/aspect/scc/scc.py check composable-witness-specialization` passed. SCC records that bounded check and does not independently certify mathematics.

## Disposition

Closed indexed binary composition, full-step correctness, source retention, both behavioral units, an actual-operation associator, and a composition WG are checked. The follow-up `CoherentWitnessSpecialization.agda` now checks the actual-operation pentagon and triangle on states, full steps and sources; see `coherent-witness-specialization.md`. This is not inferred from the older presentation pentagon. `DisplayedWitnessSpecialization.agda` identifies the underlying displayed construction and supplies a conditional hom-set bridge to Cubical's category library; see `displayed-witness-specialization.md`. General transport across arbitrary WG equivalences, arbitrary-domain compatibility inference, and finite/infinite execution transport for this new operation are not claimed by this module. No new ledger entry or commit was made.
