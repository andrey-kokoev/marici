# PDF search: nested arity, two-sided paths, and objective inversion

## Search and evidence

Used `pnpm pdf:search` for enrichment, interchange, properads, 2-Segal spaces, decomposition spaces, path spaces, decalage, edgewise subdivision, iterated constructions, and convolution inversion. Read the extracted pages behind the substantive hits, not just search snippets. Page numbers below are PDF pages; inferred printed-page metadata in the local index is unreliable for some volumes.

This is a literature comparison with the operator's nested-closure conjectures. It does not instantiate those conjectures on the analytical source or assign simplex dimensions from the row count of an arity table.

## 1. Exact two-sided index: 2n+1

Gálvez-Carrillo–Kock–Tonks, arXiv:1512.07580v3, PDF p. 32, Lemma 6.15, explicitly uses edgewise subdivision with degree-n term K_(2n+1), mapping to K x K^op. The opposing restrictions extract two degree-n parts.

The standard ordinal description is the join [n]^op star [n], of dimension n+n+1. At n=3 the indexing simplex is degree 7 with eight vertices. This gives a genuine construction behind the numerical pattern 3+3+1, rather than dimension arithmetic alone.

This is NOT an identification with the repository's uniform seventh edgewise subdivision of a tetrahedron. The twisted-arrow/ordinal-join construction and an edge lattice of subdivision length seven must be compared explicitly. Nor does an original degree-seven simplex used to represent a new degree-three simplex imply that the subdivided geometric object has acquired seven dimensions.

The same page uses this construction to calculate mapping spaces between diagrams as limits. Thus it is directly relevant to comparisons between structured systems, not merely to geometric pictures.

## 2. Both directional path spaces characterize coherent decomposition

Dyckerhoff–Kapranov, *Higher Segal spaces I*, arXiv:1212.3563v1, PDF pp. 103 and 107:

- initial and final simplicial path constructions both have degree-n object X_(n+1);
- their face maps differ, respectively omitting the initial or final face;
- Theorem 6.3.2 says X is 2-Segal exactly when both associated path spaces are 1-Segal, in the stated model-categorical setting.

These are two structures derived from the SAME X, not an assertion that any two independently chosen streams can be glued. The construction is simplicial decalage, not the ordinary topological path-space operation.

The theorem supplies a precise connection between one-directional composition and coherent decomposition. PDF p. 5 explicitly describes independence of polygon triangulation through a coherent system of weak equivalences.

## 3. Nested systems: flags of flags

Penney, *The universal Hall bialgebra of a double 2-Segal space*, arXiv:1711.10194v1:

- PDF p. 3: S_(n,k)A is described as the moduli space of length-n flags of length-k flags.
- PDF p. 13, Definition 3.6: a double 2-Segal object is a 2-Segal object in the category of 2-Segal objects.
- PDF p. 16, Lemma 3.15: augmented proto-exact infinity-categories are cartesian closed, using exact functor categories with their pointwise structure.
- PDF p. 18, Corollary 3.18: the iterated Waldhausen S-construction is double 2-Segal. The proof uses preservation of limits by S to apply it objectwise.

This is a rigorous instance of structured objects whose constituents are themselves similarly structured objects. It is more specific than the informal phrase 'arity of arities', and supplies an actual mechanism for iteration within the declared exact categorical setting.

## 4. Compatibility lives in a higher comparison, not an extra scalar

Penney, PDF pp. 3 and 32, Theorem 5.2: a double 2-Segal object gives a lax bialgebra on X_(1,1) in an (infinity,2)-category of bispans. Its product and coproduct are coherently associative/coassociative, while their mutual compatibility is lax.

The comparison has the schematic form Delta mu => mu_2 Delta_2. It is not automatically an invertible comparison. A bispan can carry the compatibility data before linearization into numerical algebra.

Here (1,1) is a simplicial BIDEGREE. It is not automatically the unary/unary arity label from the repository. The notation coincides but the types must not be equated on that basis.

## 5. A non-scalar analogue of 'cancellation leaves the initial part'

Gálvez-Carrillo–Kock–Tonks, arXiv:1512.07577v4, PDF pp. 16–17:

For a complete decomposition space, define Phi_n from the space of nondegenerate n-simplices; Phi_0 is the convolution unit epsilon. Proposition 3.7 proves zeta * Phi_n equivalent-to Phi_n + Phi_(n+1) equivalent-to Phi_n * zeta. Theorem 3.8 then gives the objective Mobius identities:

- zeta * Phi_even equivalent-to epsilon + zeta * Phi_odd;
- Phi_even * zeta equivalent-to epsilon + Phi_odd * zeta.

The sums are sums of space-valued linear functors, not scalar addition of measured residues. The theorem is deliberately sign-free: general subtraction is unavailable at this level. Additional finiteness conditions permit passage to homotopy cardinality and ordinary numerical inversion.

This closely resembles the operator's proposed residual identity, but the two families here are EVEN/ODD decomposition lengths, not positive/negative directional streams. It supplies a candidate mathematical pattern, not their identification. One cannot infer equivalence of remaining objects by informal cancellation of arbitrary common summands.

## 6. Why gluing data matter

Gálvez-Carrillo–Kock–Tonks, arXiv:1512.07573v4, PDF pp. 3–5: a tree with a cut need not be reconstructible from the two layers alone. The decomposition-space axiom replaces unique reconstruction with specified homotopy-pullback compatibility. The paper works with infinity-groupoids before taking cardinalities.

Thus the complete decomposed object includes the attachment information. This directly supports using functional/structured closure data rather than scalar residues, but rules out silently treating all pairs of pieces as uniquely gluable.

## Synthesis

The strongest candidate family now consists of:

- decomposition/2-Segal objects for coherent cutting and joining;
- initial and final decalages for the two one-directional descriptions;
- iterated S-constructions for nested structured systems;
- bispans for the comparison of composition and decomposition;
- twisted-arrow edgewise indexing for paired opposite restrictions;
- objective Mobius inversion as a concrete sign-free residual law.

These mechanisms address different parts of the intuition. They neither select the current 36/72-row enumeration nor establish an 8- or 9-simplex realization. No code or numerical experiment was substituted for a source comparison in this search.
