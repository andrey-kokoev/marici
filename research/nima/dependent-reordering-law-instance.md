# An explicit dependent reordering law in the normalization-map algebra

## Frozen interpretation

`DependentResolutionAlgebra.agda` fixes the semantic carrier at a package q to
normalization maps on **every** value of its expression:

    NormalMap(Q) = Π(x : El Q). Σ(y : Normal(Q)). y = normalize(Q,x).

A seed is a full retained route from the original presentation to its normal
presentation. Seed evaluation evaluates that route, including its coordinate
witness. This is not the earlier observer that merely reads the chosen endpoint
value.

For the existing E-rule, the algebra uses the appropriate child map and lifts
its comparison through dependent pairing. For Pi-rule, it uses every child map
and function extensionality, then the checked dependent-product equivalence.
No enumeration or inhabitance assumption on the indices appears.

For the remaining rule constructors, the algebra selects the canonical
normalization map of the complete output expression. Their comparison and path
payloads remain in that expression/value. This is an explicit choice of
normalization semantics, not a theorem that this observer captures every
possible history-sensitive interpretation.

## Concrete law, rather than an arbitrary witness import

`DependentReorderingLawInstance.agda` defines one named `dependent-reorder`
schema for arbitrary I, J(i), K(i,j), L(i,j,k), B(i,j,k,l).

Its two boundaries are resolution seeds containing the actual three-step and
four-step routes from `DependentArbitraryIndexRoutes`, each extended by a final
map into the shared normal presentation. The law interpreter uses the checked
comparison of these complete routes. It does not accept an arbitrary semantic
path as a constructor argument.

The law is then lifted through the **existing** E-rule and Pi-rule using the
actual `Structural.Generated.congruence` constructor. These Generated terms
pass directly to `GeneratedNormalizationBridge`. This closes the previously
missing connection for this explicit reordering schema and its contexts.

Both route records and resolution histories remain provably distinct. The
reified package retains the original source value, seven-edge value trace,
both histories, derivation, original witness, normalized witness and witness
reconstruction.

## Exact embedding boundary

The primitive three/four-step routes are retained **inside resolution seeds**.
The surrounding E/Pi contexts are native Resolve rule applications. This is a
route-seed embedding, not yet a compiler expanding every primitive route step
into a native Resolve rule tree. That separate compilation/endpoint-alignment
obligation must not be confused with the checked law interpretation.

Nor is one reordering schema a complete comparison basis. The next executable
question is whether canonical seed normalization and rule normalization at
canonical children give a finite complete basis for this frozen
normalization-map interpretation. Atomic source identities and arbitrary
history-sensitive interpretations remain separate obligations.

## Fresh verification

`DependentReorderingLawRegression.agda` instantiates infinitely many first
indices, dependent Fin fibres at the next three levels and a nontrivial
circle-index loop as a leaf witness. Checks cover:

* the explicit root reordering;
* native Pi congruence over Nat and the empty type;
* native E congruence with an actual selected index;
* both contextual comparisons passing through the Generated bridge;
* distinct raw route histories;
* retention and nontriviality of the original loop in the next package;
* the algebra's guarantee for all source values, not just the stored value.

Fresh safe Cubical Agda verification passed:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module DependentReorderingLawRegression -Fresh
```

Evidence:

* `research/nima/agda/DependentResolutionAlgebra.agda`
* `research/nima/agda/DependentReorderingLawInstance.agda`
* `research/nima/agda/DependentReorderingLawRegression.agda`
* `research/nima/results/agda-DependentReorderingLawRegression.json`
* `research/nima/results/agda-DependentReorderingLawRegression.log`
