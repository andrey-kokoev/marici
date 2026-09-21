# First nesting of four-presentation systems is a product diagram

## Question

Can each of four presentations itself be a four-presentation system, with comparisons of the entire inner systems? Test one nesting before asserting an infinite self-similar tower.

The prior packet `rung-four-is-the-final-boundary-forming-coherence-but-its-typed-residual-must-still-vanish.md` distinguishes presentations, pair interfaces, triangle comparisons, and tetrahedral coherence. Its four levels belong to the entire tetrahedral packet; individual vertices are not individually those four levels.

## Diagram model

Let I=[3], the ordinal category on four vertices. A diagram D:I -> Fun(I,C) is a nested system. At outer vertex a it assigns an inner diagram D_a:I -> C. An outer arrow a->b is a natural transformation between the entire diagrams D_a and D_b.

Its expanded form is a diagram E:I x I -> C, with E(a,i)=D_a(i). Thus there are sixteen presentation objects X_(a,i), not sixteen unrelated observations.

For outer comparison p:a->b and inner comparison q:i->j, the mixed square compares the two maps from X_(a,i) to X_(b,j): first inner then outer, versus first outer then inner. Naturality supplies their equation in the ordinary-category model. In a genuinely higher target, the appropriate comparison and its higher compatibility must be part of the coherent diagram.

Functor currying gives an equivalence between nested and expanded descriptions. It does NOT convert an arbitrary sixteen-object array into a coherent diagram. The interfaces and mixed compatibilities are prerequisites to either description.

## Checked implementation

`research/voevodsky/agda/NestedFourPresentation.agda`:

- defines I using Fin 4 and the natural-number order;
- defines the product category I x I;
- specializes Cubical's functor-currying isomorphism;
- exposes expand and nest and both full-functor round-trip paths;
- checks the object identification and the exact mixed naturality square;
- instantiates a nonterminal test with target I x I and its identity functor, so all sixteen ordered-pair objects occur.

This is an ordinary category with hom-sets. Composition preservation and its higher equality coherence are consequently forced at the appropriate truncation. The module does not represent arbitrary independently chosen triangle/tetrahedral homotopies or instantiate analytical maps. Its success establishes a consistent strict categorical instance of the first nesting, not the stronger analytical tower conjecture.

## Shape and dimension

The nerve of I x I is the simplicial product Delta^3 x Delta^3. Its standard geometric realization is the six-dimensional product of two tetrahedra. It is not Delta^15, and it is not merely another tetrahedron.

In the product-cell structure its faces are products sigma x tau. Their dimensions add. The cell counts by dimension 0 through 6 are the coefficients of (4+6t+4t^2+t^3)^2: 16, 48, 68, 56, 28, 8, 1. In particular there are 36 mixed edge-by-edge squares, as well as 32 triangular two-faces. These are product-cell counts, not the simplex counts after triangulation.

This provides a constraint on the proposed recursion: nesting two four-level tetrahedral shapes introduces mixed shape dimensions through six. It does not leave only four total dimensions. In the checked hom-set model those higher compatibilities carry no new independent witness choices. In a higher target their data cannot be omitted merely because each factor has four coherence levels.

## Finite iteration versus an infinite source tower

The same diagram construction can be iterated formally. With r tetrahedral factors, the indexing shape is (Delta^3)^r, with 4^r vertices and dimension 3r. Here r counts nesting factors; it is not identified with the source cutoff or the cut index k.

An infinite family still requires specified comparisons between the finite stages, their compatibility, and an appropriate limiting notion. More importantly, the actual four analytical presentations must each admit the proposed inner system with source-authorized maps. None of that follows from the currying theorem.

The present result is therefore: finite nesting is structurally consistent, its mixed squares have exact types, and nested/expanded complete strict diagrams are equivalent descriptions. Self-similarity of the analytical source, nontrivial higher residues, and an infinite tower remain conjectural.

## Verification

Fresh closure check:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/NestedFourPresentation.agda`

Exit 0 with Agda 2.8.0.1 and Cubical 0.9. The module uses --safe --cubical --guardedness, with no added holes or postulates. The first incremental check caught a mistaken name for the library identity functor; using the library's actual identity notation fixed it. No prior analytical theorem or existing Agda module was modified.
