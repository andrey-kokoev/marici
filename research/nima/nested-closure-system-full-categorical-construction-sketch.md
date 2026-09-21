# Nested closure systems: full categorical construction sketch

## Aim

Construct a mathematical model in which nested structures have two directional descriptions, cuts can be changed through coherent comparisons, and composition/decomposition compatibility is itself structured data. Relate this to the four arity presentations without equating arity, cut position, and homotopy degree.

This sketch provides an actual abstract construction and an explicit first comparison. The correspondence with the repository's analytical realization system is a separate named part of the construction, not an assumed identification.

All formulas are inline. No temporal interpretation is attached to an ordering or a filtration.

## 1. Base category and an explicit model

Let C be a small stable infinity-category. A concrete example is Perf(Q): perfect rational chain complexes with their derived mapping spaces. This example supplies objects, maps, chain homotopies, and further coherent comparisons; it is not the ordinary hom-set category used in the earlier Agda currying check.

Stable means that C has a zero object, finite limits and colimits, and a square is a pullback exactly when it is a pushout. Consequently each map has a cofiber and cofiber constructions are functorial in the infinity-categorical sense.

For analytical application, one would instead use an appropriate source-derived exact or stable category, or the previously proposed formal stable envelope. Passing to that envelope does not prove positivity, preserve an unspecified physical domain, or construct an independently prescribed analytical map. These requirements belong to the realization functors in section 9.

## 2. A closure object is a complete interval diagram

Let Ar[n] be the arrow category of the ordinal [n]. Define S_n(C) as the full infinity-category of diagrams F:Ar[n]->C satisfying:

- F(i,i) is a zero object;
- for i<=j<=k, the square with rows F(i,j)->F(i,k) and 0->F(j,k) is bicartesian.

Equivalently, an object is a filtration 0=F_0->F_1->...->F_n together with all interval quotients F(i,j) equivalent to cofib(F_i->F_j) and their coherent comparison data. The interval diagram, rather than only a sequence of quotient values, is the closure package.

Taking maximal infinity-groupoids gives X_n=(S_n(C))^core. Restriction along ordinal maps gives a simplicial space X. The Waldhausen theorem supplies its unital 2-Segal structure. In this stable example the zero-object inclusion also makes X complete as a decomposition space, the completeness needed for the objective inversion construction below.

S_0(C) is the zero category and S_1(C) is equivalent to C. This identifies the actual initial/unit part of this model; it does not identify it with the operator's realization rung zero without an additional comparison.

## 3. Cutting is restriction; joining is reconstruction with attachment data

For a triangulation T of an (n+1)-gon, let Mem_T(X) be the homotopy limit of the triangle and edge data attached to T. Restriction gives c_T:X_n->Mem_T(X).

The 2-Segal theorem says c_T is an equivalence. Thus a complete closure and its decomposition along T are equivalent descriptions, with the shared edges and gluing witnesses included.

For two triangulations T and U, the comparison is rho_(T,U)=c_U composed with an inverse of c_T. The inverse is taken with equivalence data, whose choice is contractible. All comparisons are organized through the same X_n. This supplies coherent independence of triangulation rather than separately chosen pairwise bijections.

This is not the assertion that an arbitrary pair of independent pieces determines a unique whole. The homotopy limit includes their specified attachment data. Nor is the general 2-Segal condition a replacement by X_k times X_(n-k) over X_0: that simpler path-composition formula would impose a different Segal requirement.

### First explicit comparison: a quadrilateral

Take a filtration 0->A->B->C and abbreviate its cofibers by B/A, C/A, and C/B.

The diagonal 02 describes two triangles:

- (A, B/A, B), a cofiber sequence;
- (B, C/B, C), a cofiber sequence.

They share B.

The diagonal 13 describes:

- (A, C/A, C), a cofiber sequence;
- (B/A, C/B, C/A), a cofiber sequence.

They share C/A. In each triple the first object maps to the third and the second is its cofiber.

Both descriptions come from the same filtration. The substantive compatibility is the cofiber sequence B/A -> C/A -> C/B. It is the stable octahedral/cofiber-composition law.

The two membrane spaces are the two appropriately indexed homotopy fiber products of X_2 with X_2 over X_1, each equivalent to X_3. This gives the first concrete cut-and-rejoin comparison. For a pentagon, the five decompositions and their comparisons have the coherent compatibility supplied by X_4.

This is an explicit model of the requested comparison, not an assertion that the unresolved conductor–Morse routes are these cofiber maps.

## 4. Two directions of the SAME closure system

Define the initial and final decalages P_initial(X) and P_final(X). Both have degree-n space X_(n+1), but their boundary operators differ: one omits the initial face, the other the final face.

The path-space criterion states that X is 2-Segal precisely when both these directional path objects are 1-Segal, under the source theorem's hypotheses. They therefore organize composable routes extracted from the same closure data.

These are simplicial path constructions, not a claim that the two directional spaces are automatically equivalent, or that either direction is the inverse of the other. Their common origin is X.

## 5. Actual nesting: flags of flags

The categories S_n(C) are again stable in this model: the defining zero and bicartesian conditions are preserved by the relevant pointwise finite limits and colimits. Define the nested object X^(r)_(n1,...,nr)=(S_n1(S_n2(...S_nr(C)...)))^core.

Equivalently, it is the space of diagrams on Ar[n1] times ... times Ar[nr] that satisfy the S-construction exactness conditions separately in each coordinate. For r=2 these are flags of flags, not merely sixteen named vertices.

Exact functor currying identifies the nested and expanded descriptions. The r-fold diagram has coherent decomposition in each simplicial direction. Permuting coordinates reindexes the same multidiagram, with its induced coherent equivalences.

Inserting an index 1 gives an equivalence with the lower-nesting object because S_1 is equivalent to the identity. Hence there are specified unit slices relating the finite nesting constructions. Inserting general indices adds flag structure instead; it is not identified with a canonical k-successor of the analytical source.

The finite constructions exist for every r. A single 'infinite tower' would additionally specify whether it means the compatible multisimplicial family, a limit along selected restriction maps, or another completion. The construction here already supplies the finite family and its unit/restriction structure without inventing that choice.

## 6. Interchange is a cell between operations

For r=2, Penney's theorem applies to the double 2-Segal object X^(2). Its space A=X^(2)_(1,1) carries a lax bialgebra in the infinity-2-category of bispans.

This gives a multiplication mu, a comultiplication Delta, and a comparison beta:Delta composed with mu => mu_2 composed with Delta_2. The notation on the right includes the pairing/permutation required by the bialgebra law.

The product and coproduct have their own coherent associativity and coassociativity. Their mixed compatibility is a higher cell; it need not be invertible. Consequently this construction supplies a structured comparison but not automatically the reversible homotopy demanded by a stronger commutation conjecture.

The compatible construction at X^(2)_(2,2) contains the two-dimensional filtration data used for this cell. Separate one-directional strings alone do not replace those data.

IMPORTANT NOTATION: the (1,1) in X^(2)_(1,1) is simplicial bidegree. The (1,1) in the four-arity square is unary input/unary output. These are separate labels even where a future interpretation relates them.

## 7. Opposite direction, polarity, and edgewise indexing

A contravariant exact equivalence D:C^op->C, with a specified coherent involution, supplies a duality. In Perf(Q), derived linear duality provides a concrete example. It acts on an S_n diagram by F(i,j) mapping to D(F(n-j,n-i)). This reverses the flag and preserves the requisite bicartesian structure.

Such a duality is extra structure, not supplied by arbitrary decomposition spaces. In the analytical source it corresponds to the separately constructed dagger/polarity operation, whose compatibility with beta must be checked by the appropriate realization functor.

Independently, twisted-arrow edgewise subdivision is defined by the ordinal operation Q([n])=[n]^op star [n]. Thus esd(X)_n=X_(2n+1). Opposing restrictions give a map to X^op times X, up to the convention for ordering the two factors.

At n=3 the index is 3+3+1=7, with eight vertices. The central join connects two oppositely ordered four-vertex lists. This is the precise candidate behind that numerical pattern. It is NOT a theorem identifying this construction with the uniform sevenfold edge subdivision of the earlier analytical tetrahedron.

The index degree 7 here is not the geometric dimension of a newly enlarged realization tower. A degree-three simplex in esd(X) is represented by degree-seven data in X. The degree change is part of the indexing functor.

## 8. Structured residual identity without subtraction

Use the complete decomposition space X from section 2. Its incidence comultiplication is the span X_1 <- X_2 -> X_1 times X_1, with left leg the composite/long-edge map and right leg the two-edge map. This induces convolution on space-valued linear functors out of the slice over X_1.

Let zeta be represented by X_1 <- X_1 -> point. Let Phi_n be represented by X_1 <- effective X_n -> point, where effective simplices have nondegenerate principal edges. Phi_0=epsilon is the unit, represented using X_0.

The decomposition theorem gives zeta * Phi_n equivalent to Phi_n + Phi_(n+1), also equivalent to Phi_n * zeta. Summing separately over even and odd n gives:

- zeta * Phi_even equivalent to epsilon + zeta * Phi_odd;
- Phi_even * zeta equivalent to epsilon + Phi_odd * zeta.

Here plus is coproduct, NOT the earlier gluing operation along a shared closure. These identities preserve the spaces of decompositions and work before numerical cardinality. They do not assert a subtraction operation or unrestricted cancellation of common summands.

This supplies a precise residual-unit law in the model. The interpretation that even/odd families are the operator's two opposite closure streams is a separate conjecture. Likewise, epsilon must be compared with the intended rung-zero realization rather than identified by the subscript alone.

## 9. The four presentations and their realization maps

Write V={(1,1),(1,*),(*,1),(*,*)} for the source arity labels. They describe unary/unary, unary/many, many/unary, and many/many roles. They do not enumerate simplicial degrees.

For each v in V, the proposed analytical realization is a diagram-valued functor E_v on the nested exact-diagram system. To represent the SAME complete system, the comparisons between E_v and E_w must account for the full chosen source structure, the face and degeneracy maps, and the cut-and-rejoin equivalences.

The analytical program must provide these E_v, their comparison maps, and compatibility with the two operations, duality, and completions. The earlier common-source chart construction is relevant input; merely choosing four copies of the abstract model would not test an independent analytical comparison.

For nested arities, each internal node must be labelled by its operation (substitution, coaction, or an explicitly defined composite), and leaves by their actual source/target types. An unlabelled parenthesized word does not record this. The present 36-row list is a useful selection of signatures, not a list of homotopy dimensions or all possible exact diagrams.

## 10. The coherence tower and the indices

At each fixed nested diagram shape:

- objects are complete structured realizations;
- 1-morphisms compare realizations;
- 2-cells compare parallel 1-morphisms;
- higher cells compare the corresponding parallel higher data.

Three indices have separate jobs: cut position k, number r of nested flag directions, and homotopy degree d. The multi-index (n1,...,nr) gives flag lengths. Arity labels give input/output roles. Establishing relations among these indices is part of the proposed analytical interpretation, not accomplished by enumeration.

The mathematical model now contains all finite nesting depths and coherent cut-change maps. It supplies a candidate framework for the operator's recursion rather than proving the proposed 8-simplex geometry.

## 11. First informative Cubical Agda target

Do not repeat functor currying in a hom-set category. Formalize the quadrilateral cofiber-composition comparison from section 3, including both maps between its two decomposition presentations and the required boundary identifications. Then formalize compatibility of two adjacent cut changes as the first higher test.

If working in finite rational complexes, use actual chain maps, cones, and chain homotopies with the shifts and signs explicit. If working in abstract stable infinity-categories, the stable cofiber universal properties are the inputs, not the desired cut-change equivalence as a record field.

The model-level theorem is independent of the missing analytical adapter. Proving it cannot certify that a physical positivity requirement or an independently specified conductor route has been supplied.

## References and strength

The construction uses the following literature results, read in the local PDF corpus:

- Dyckerhoff–Kapranov, arXiv:1212.3563, PDF pp. 5, 103, 107, and the Waldhausen discussion: 2-Segal reconstruction, the two decalages, and the path-space criterion.
- Penney, arXiv:1711.10194, PDF pp. 3, 13, 16, 18, 32: iterated S-construction, exact functor currying, double 2-Segal structure, and lax bialgebra compatibility.
- Gálvez-Carrillo–Kock–Tonks, arXiv:1512.07577, PDF pp. 16–17: the objective residual identities.
- Gálvez-Carrillo–Kock–Tonks, arXiv:1512.07580, PDF p. 32: edgewise indexing and mapping-space calculations.

This is a categorical construction sketch, not a fresh proof-assistant verification. No analytical source comparison or infinite limiting realization is claimed to have been constructed by this document.
