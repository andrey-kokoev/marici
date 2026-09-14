# PDF clues for the reciprocal bulk-coherence cell

## Question

What established higher-categorical construction could type the missing comparison between reciprocal transport of the positive schedule bulk and direct construction of the negative schedule bulk?

## Claim boundary

The cited pages identify a candidate formalism: a symmetric monoidal infinity-2-category of correspondences with Beck--Chevalley base-change cells and canonical anti-involution. They do not identify the Marici carriers with schemes, IndCoh, or any geometric correspondence category, and they do not construct the required Marici functor.

## Search evidence

Search command family:

```text
pnpm --silent pdf:search -Query <query> -Book dag1 -Limit <n> -Context <n>
```

### Correspondences encode bivariant composition

Derived Algebraic Geometry, volume 1, PDF page 32 states that Corr(C) is designed to encode compatibility of the relevant isomorphisms with compositions of vertical and horizontal morphisms. This matches the role assigned to the missing cell: it compares reciprocal transport of an already assembled composition with assembly after reciprocal transport.

PDF page 215, printed page 178, states that base change is extra structure and motivates the category of correspondences. Thus a pointwise equality of positive and negative rows cannot replace a base-change witness.

PDF page 357, printed page 320, gives the extension criterion: horizontal images admit right adjoints and those right adjoints satisfy base change against vertical morphisms. This suggests that the Marici cell should be tested as an invertible Beck--Chevalley mate, not invented as an unconstrained higher homotopy.

### Anti-involution is dualization

PDF page 321, printed page 284, and PDF pages 426 and 433 state that Corr(C) carries a canonical anti-involution swapping vertical and horizontal arrows, canonically identified with dualization under the symmetric monoidal structure.

PDF page 433 describes the action on a span explicitly: the two legs are exchanged. This is a formal counterpart of reciprocal transport between positive and negative variance directions.

PDF page 434 states that every object of the Cartesian-monoidal correspondence category is self-dual. Evaluation and coevaluation are supplied by correspondences built from the diagonal map and the terminal map. This gives a candidate origin for pairings that does not require identifying a Hilbert carrier with its algebraic dual.

### Fibration model for adjoints

PDF pages 62 and 68 state that a functor and its adjoint are jointly encoded by a bi-Cartesian fibration, including diagramwise passage to adjoints. This suggests replacing two independently postulated schedule sheets by one bi-Cartesian total object when the required lifts exist.

## Candidate retyping

Let C carry declared vertical and horizontal morphism classes, and let

\[
\Phi:\operatorname{Corr}(C)\longrightarrow S
\]

be a proposed symmetric monoidal functor into the target infinity-2-category of Marici realizations.

Then:

- positive transport is the horizontal leg of a correspondence;
- negative or reciprocal transport is obtained by the canonical anti-involution exchanging the two legs;
- the pairing is the image of the correspondence self-duality data;
- each transport square carries a Beck--Chevalley mate;
- compatibility with schedule composition is supplied only if these mates satisfy the correspondence extension theorem.

The previously named 4-cell

\[
\Xi_W:W\Omega_+\Rrightarrow\Omega_-W
\]

should therefore be retyped as the top compatibility of a family of Beck--Chevalley mates under composition and anti-involution. If Phi is already defined on Corr(C), Xi_W is not arbitrary extra data: it is induced by functoriality. If only the vertical and horizontal restrictions are given, the invertible mate and its composition coherence are precisely the missing extension data.

## Strongest falsifier

A reciprocal map W with W squared equivalent to the identity can still fail Beck--Chevalley. Likewise, separate positive and negative bulk fillers can exist while the mate from pull--then--push to push--then--pull is noninvertible. Either failure prevents extension to Corr(C) and blocks profile-level simplification.

## Revised acceptance test

1. Declare the base square or span whose horizontal and vertical legs represent source and reciprocal transport.
2. Construct the relevant adjoints rather than formal transposes.
3. Form the Beck--Chevalley mate by units and counits.
4. Prove that mate invertible on every generating square.
5. Verify compatibility under horizontal and vertical composition.
6. Verify that the anti-involution carries each positive mate to the corresponding negative mate.
7. Only then identify the induced top compatibility with Xi_W.

## Disposition

The best current clue is not a new analytic Green identity. It is a correspondence-extension theorem: Xi_W is likely a Beck--Chevalley composition coherence generated by a bivariant functor on a correspondence infinity-2-category. The first missing typed object is the Marici base square/span from which its mate could be formed.
