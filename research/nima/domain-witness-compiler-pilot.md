# Domain Witness Generator compiler: first cross-domain pilot

`agda/DomainWitnessCompiler.agda` takes a supplied dependent presentation with `Input`, `Output : Input → Type`, and `compute : (i : Input) → Output i`. One generic `Compile` module turns it into a `TypedGeneratorLayers.Layer1`: states are tagged requests or tagged responses, and its relation records an `evaluated` or `idle` witness. On a request, `run` returns the computed response, preserving the exact request index. On a response, `run` is stationary. `result-beta` and `retained-input` typecheck without assuming output values as independent seeds.

The same compiler is instantiated for Boolean complement and for composition of two composable arrows in an arbitrary *supplied* ordinary category. Its category result agrees definitionally with the supplied composition; it does not derive category laws. `Admitted` restricts inputs by a supplied predicate and retains its evidence in the request index (tested on Boolean `false`). `CompileLaw` reuses the compiler with equality proofs as computed outputs: Boolean double negation is checked by cases, while category associativity is imported from the supplied category, with the triple of composable arrows retained in the certificate. These are typed law-certificate histories through the same Layer-1 interface, not law discovery.

A unified `DomainPresentation` now links one operation, a typed admission predicate, a law request, an expected output and its proof. `CompileDomain.execute-law` returns the *same* computed response with its transition witness and law proof; `retained-history` makes a one-edge Layer-2 history of that transition. Boolean double negation and the left-unit law for a supplied category instantiate this same interface. An identity-versus-negation example proves that equal input/output types do not force equal results. This is a cross-domain witness-generator **adapter prototype**, not a proof of the universal domain-constructor conjecture: laws and admission evidence are supplied; no native node/rule derivations, reversible view compiler, or generated Yoneda theorem have been constructed.

Fresh safe Cubical Agda check:

```text
agda --ignore-interfaces --safe --cubical --guardedness --transliterate -i research/nima/agda -i research/nima/adapters/yoneda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/nima/agda/DomainWitnessCompiler.agda
```

Exit zero after these additions. The imported `TypedGeneratorLayers.agda` reports a pre-existing unused-import warning for `isPropIsContr`; no holes or postulates were added. Next discriminating test: retain *multi-step* law histories (associativity across differently indexed composition operations) and connect them to actual native node/rule endpoints. The present one-step certificate does not prove that the underlying twelve-rule native closure can execute the new operation.
