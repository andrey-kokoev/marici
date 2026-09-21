# Checked cofiber composition: the first cut-and-rejoin comparison

## Constructed theorem

For arbitrary small types A, B, C and functions f:A->B and g:B->C, the added Cubical Agda module constructs the induced map h:cofib(f)->cofib(gf), and proves cofib(h) equivalent-to cofib(g).

Writing cofib(f)=B/A and cofib(gf)=C/A, this is (C/A)/(B/A) equivalent-to C/B. Slashes denote homotopy cofibers, not set quotients or arithmetic division.

`research/voevodsky/agda/ClosureCofiberComposition.agda` exports:

- `induced`, with its action on B, the base point, and the full A-attachment paths;
- `cofiberComposition`, the constructed equivalence;
- `rejoin` and `cut`, the actual functions in both directions;
- `rejoin-cut` and `cut-rejoin`, their pointwise round-trip homotopies;
- `quotientIdentification`, the type equality supplied by univalence.

The desired equivalence is an output, not a field or an existence parameter.

## Construction

The proof instantiates the Cubical library's homotopy-pushout 3-by-3 theorem with three span rows:

- Unit <- A -> C, using gf;
- Unit <- A -> B, using f;
- Unit <- Unit -> Unit, using identities.

The middle row maps to the first by identities and g, and to the third by terminal maps. All four source squares commute by the explicitly defined maps.

Computing column pushouts first produces two identity-leg pushouts and the cofiber C/B (with the pushout legs initially reversed). The identity-leg pushouts are explicitly contracted, including their path constructors. Computing row pushouts first produces C/A, B/A, and a contractible terminal-row pushout, hence the cofiber of h.

The library 3-by-3 equivalence compares these two actual colimit constructions. Homotopy-natural equivalences of spans implement the contractions. Composing these proved equivalences gives the required cut-and-rejoin equivalence.

No hom-set truncation is imposed on A, B, C or their cofibers. The inverse and its round trips are obtained from the complete equivalence, not verified only on point constructors.

## Regressions

`research/voevodsky/agda/ClosureCofiberCompositionRegression.agda` proves two contrasting cases:

- With A empty, B=Bool, C=Unit, the iterated quotient is equivalent to the circle. Both attachment paths matter: the result is not a terminal set.
- For arbitrary f:A->B and g the identity of B, the iterated quotient is equivalent to Unit.

The circle case is a regression for this constructed cofiber comparison, not the earlier hypothetical circle obstruction to a physical tetrahedral filler.

## Scope relative to the full sketch

This formalizes the homotopy-pushout/cofiber-composition ingredient of the quadrilateral comparison. The implementation uses spaces rather than Perf(Q) or a formalized stable infinity-category. The theorem already holds in this setting, so stability and chain-complex signs are not needed for this ingredient.

It does not yet formalize equivalence of the full moduli spaces of exact filtrations, the pentagon comparing multiple cut changes, or the analytical realization functors. The displayed maps on source cells identify the induced map h; full naturality of the resulting cut-change equivalence under maps of triples is not separately exported as a theorem here.

The next substantive target is the compatibility of this comparison for three composable maps, with the induced maps between intermediate cofibers included. It should compare independently assembled instances of the constructed equivalence, not assume their equality as a record field.

## Verification

Fresh dependency closure was checked using:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureCofiberCompositionRegression.agda`

Agda 2.8.0.1, Cubical 0.9, exit 0. Both added modules use `--safe --cubical --guardedness`, with no holes or postulates. Initial incremental runs caught a missing `idfun` import and an extra argument to the already specialized library `3x3-Iso`; both were repaired before the fresh passing check.

No existing source module was modified and no analytical positivity or source-identification claim was added.
