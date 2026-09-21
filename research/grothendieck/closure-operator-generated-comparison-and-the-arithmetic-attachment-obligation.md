# Closure-generated comparison and the arithmetic attachment obligation

## Corrected finding

Following the actual construction rather than stopping at its client facade changes the diagnosis. Global cut frames **are already derived** for arbitrary finite linear gluing chains. The source supplies pieces, boundary types, and their two attachment maps; recursive homotopy-pushout normalization constructs the frames, including both external endpoint laws.

The earlier claim that the programme stops simply at unconstructed frames was too broad. The real test is whether the arithmetic and Green candidates are evaluations of the same complete attachment data. This note constructs and formally checks the local-to-global necessity theorem that makes that test precise, then attempts its application to the existing arithmetic residual.

## 1. Source trail

`ClosureFiniteGluingNormalization.System` takes K, Piece, Boundary, attachL, attachR. `Realize` interprets bracket trees by actual homotopy pushouts. `appendFrame` derives a joining frame recursively using the three-piece associator; `normalizeFirst` and `normalizeLast` supply the attachment squares for the next recursion. `normalize` derives Realize(t) equivalent to Normal(w).

`ClosureDependentRefinementTrees` adds dependent Sigma/Pi nodes; its local node equivalences remain declared data. Its twisted-circle regression shows that reference-route coherence does not trivialize internal boundary monodromy.

`ClosureReferenceNormalForm` then consumes these constructed global frames. Reading its parameter list in isolation hid this existing upstream construction.

## 2. Necessity theorem from the operator

For a single gluing P=A amalgam_S B with maps f:S->A, g:S->B, define the complete target cocone by

Cocone(T) = Sigma(l:A->T) Sigma(r:B->T) product_(s:S) [l(f(s))=r(g(s))].

The pushout elimination rule constructs an equivalence

Map(P,T) equivalent to Cocone(T).

The forward map restricts a global map to the two pieces and to every attachment path. The inverse assembles those data using the pushout constructors. Both round trips are proved, not taken as hypotheses.

Therefore two global maps MUST coincide if their complete constructor data coincide. Conversely a global equality gives a cocone equality by restriction. This is an internal generation law: no separately selected global comparison is required.

The dependent equality of cocones matters. Agreement on the two piece maps alone omits the attachment witness and cannot generally establish the hypothesis.

By repeating this rule at each node, a finite generated comparison reduces to comparisons on the leaves and their attachment paths. The existing normalizer supplies coherent passage between bracketings of the same chain. This recursive extension is a mathematical consequence of the one-node equivalence and the inspected implementation; this packet's new Agda modules formally check the one-node and two-slot statements, not a separate general tree theorem.

## 3. The polarized theorem is the relevant one

A Green comparison concerns a two-slot function Q:P->P->U, not merely a scalar output on one selected state. Applying the same operator twice gives complete local data:

- maps on A x A, A x B, B x A, B x B;
- attachment comparisons in each slot;
- their mixed compatibility, retained by the dependent cocone type.

The newly checked `localData` and `reconstruct` implement this iterated restriction/assembly. `forced-polarized-comparison` proves

localData(Q)=localData(R) implies Q=R.

No positive form is postulated by this theorem. Once actual forms Q and R have been constructed on the same admitted source, their equality is forced by equality of their full local data. This gives the correct necessity-first route to form preservation.

A complex Hermitian application must additionally represent conjugation, linear domains, and the real scalar target appropriately. The abstract type-theoretic theorem does not silently identify topological paths with analytic domain extensions or certify bilinearity. Those structures must be properties of the actual generated realization.

## 4. Attempt at the existing middle facet

The source already identifies the correct Waldhausen interval packages. For the middle facet, write

A=X_SA, B=X_SC, C=X_SG,

with candidate maps f:A->B and g:B->C. If the supplied faces identify

cofib(f)=X_AC, cofib(gf)=X_AG,

then the closure operation constructs the remaining common cofiber

X_CG = cofib(g) equivalent to cofib(X_AC->X_AG).

The second arrow is the induced map, including its action on attachment paths; it is not an arbitrary map between the two named quotients. `ClosureCofiberComposition.agda` constructs exactly this equivalence in its space-valued setting. The stable categorical analogue is the cofiber-composition/octahedral law used by the Waldhausen sketch.

Thus the operator supplies a candidate CG package and its comparison **from a common composable diagram**. One must not feed it three differently realized objects all named G. The prior prism inventory identifies precisely that risk: relative Wronskian, reduced cyclic, and independent Green targets have not yet been identified as evaluations of one such diagram with the same form data.

This is where the attempted arithmetic instantiation stops. The inspected records do not exhibit a common polarized cocone satisfying the two-slot local equality. I have not proven no such cocone exists; I have identified the concrete construction whose existence would make the global comparison forced.

## 5. Why the proved Xi identity does not fill that local equality

The existing bordered result is a holomorphic one-slot identity

Delta_border(z)=Xi(z) H_border(z).

On a Xi state it kills that output. The required local Hermitian comparison instead has diagonal defect

Q_minus(b_z,b_z)-Q_plus(b_z,b_z)
  = (1-p^(-2 Re z)) E_p(b_z).

The closure theorem would force this defect to vanish if the full two-slot cocones of Q_minus and Q_plus agreed. The holomorphic identity provides neither the mixed piece-pair values nor the attachment comparison of those forms. Restricting the desired global equality already encounters the displayed local difference.

This is not a reason to demand an unrelated external metric. It is the precise internal necessity obligation: derive the polarized local cocone and its reciprocal compatibility from the same closure constructors, without inserting the desired diagonal equality as a field.

The fact that the diagonal is confinement-strength means a proof of the required local equality is a substantive arithmetic theorem, not a normalization convenience. Formalizing its implication is useful only if we keep that distinction explicit.

## 6. What is now established and what was not achieved

Established:
- corrected source attribution: global finite-chain frames are already constructed;
- a fully explicit necessity-and-construction equivalence for generated maps;
- a checked two-slot version identifying the complete polarized comparison data;
- the common-cofiber construction that would generate the missing CG interval from an actual common diagram;
- localization of the arithmetic attempt to polarized constructor compatibility, rather than route observability or detector noise.

Not achieved:
- an arithmetic instantiation of the common polarized cocone;
- a proof that closure alone, without its admitted seed and attachment structure, forces the positive form;
- confinement or a derivation of primewise Haar balance.

This is the outcome of the attempted derivation, not a claim that the hard theorem has been replaced by a formal lemma. The next mathematical work must compute the actual piece-pair forms and attachment maps in the source diagram, not build another finite observer.

## Verification

New modules:
- `research/grothendieck/agda/ClosureGeneratedMapNecessity.agda`
- `research/grothendieck/agda/ClosurePolarizedMapNecessity.agda`

Fresh dependency-closure check:

`agda --ignore-interfaces --transliterate -i research/grothendieck/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/grothendieck/agda/ClosurePolarizedMapNecessity.agda`

Exit 0. Both modules use `--safe --cubical --guardedness`, without holes or postulates. The second imports and freshly checks the first. No claim is made to have freshly rerun the entire prior closure programme.

Analytical sources inspected:
- `research/voevodsky/the-middle-facet-must-be-a-waldhausen-filtration-restriction-not-a-tetrahedron-of-role-morphisms.md`
- `research/nima/the-missing-prism-sides-share-one-codomain-change-from-relative-Green-proxies-to-the-independent-global-Green-system.md`
- `research/nima/the-independent-Xi-divisible-bordered-defect-does-not-imply-the-relative-Haar-energy-cycle.md`
