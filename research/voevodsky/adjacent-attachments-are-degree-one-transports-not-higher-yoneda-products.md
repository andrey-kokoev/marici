# Adjacent attachments are degree-one transports, not higher Yoneda products

## Result and correction of interpretation

The adjacent cubic and quartic attachment roofs are nonzero, but they are NOT higher Yoneda products of the earlier adjacent classes.

In the SAME declared strict completed source category:

1. Every adjacent class is a degree-one morphism e_r:G_r->G_(r+1)[1].
2. Every consecutive Yoneda composite e_(r+1)[1] e_r is ZERO. The existing three-step filtered object supplies an explicit roof refinement on which the composite is strictly zero.
3. On each finite hereditary path source, the adjacent extension at depth r is the exact tensor transport of the first extension by the right-flat ideal power I^(r-1).
4. The corresponding multiplication comparisons extend to the specified native/inherited expanded-path presentation completions. This is not a theorem about arbitrary completed projective tensor products or an exact tensor functor on all completed modules.

Thus the presently constructed higher-seam witnesses detect nonzero ADJACENT Ext1 data propagated through the source filtration. Their nonvanishing and reassociation do not establish independent higher-Ext classes or new secondary operations.

Inputs:
- `the-first-two-completed-filtered-attachments-form-a-compatible-comparison.md`
- `two-residual-gaps-detect-the-adjacent-cubic-attachment.md`
- `three-residual-gaps-detect-a-pentagon-coherent-four-seam-attachment.md`
- `../nima/theta-tail-dominance-controls-actual-letter-factorization-lifts.md`

## 1. Put the classes in their actual degrees

Work in one of the already admitted common completed source domains and write J_r for its closed ideal powers. Set

    G_r=J_r/J_(r+1),
    E_r=J_r/J_(r+2).

The strictly exact adjacent sequence is

    0 -> G_(r+1) -> E_r -> G_r -> 0.

Its connecting class is

    e_r:G_r -> G_(r+1)[1].

The binary, cubic and quartic adjacent witnesses concern e_1, e_2 and e_3 respectively. Their different numbers of receiver seams do NOT change the cohomological degree of this source extension.

A consecutive Yoneda composition instead has type

    e_(r+1)[1] e_r : G_r -> G_(r+2)[2].

It has a different target degree and a different source/target pair from e_(r+1). Therefore equality of a new adjacent roof with that composition was never a type-correct claim without extra maps and shifts.

## 2. The actual three-step filtration kills the composite

Use the abbreviations

    B=G_(r+2), A=G_(r+1), G=G_r,
    F=J_(r+1)/J_(r+3),
    T=J_r/J_(r+3),
    E=J_r/J_(r+2).

All maps below are the actual source inclusions and quotients. There are strictly exact rows

    0 -> B -> F -> A -> 0,
    0 -> F -> T -> G -> 0,
    0 -> A -> E -> G -> 0.

Pushing the middle row along F->A gives the bottom row. This already says that e_r lifts to an extension by F, so its obstruction under the next connecting morphism is zero. Here is the explicit complex calculation, avoiding an appeal to an unspecified projective resolution.

## 3. Explicit roof refinement and zero chain composite

Use cochain conventions C[1]^n=C^(n+1), with shifted differential negated. The old roof model for G is

    K_old=[A -> E],  degrees -1,0.

Refine it by

    K=[F -> T],      degrees -1,0.

The quotient map K->K_old has kernel [B --identity--> B], with its bounded identity contraction. It is therefore a strict quasi-isomorphism. The connecting map e_r, represented on K, is the degree-minus-one quotient F->A into A[1].

The next extension has roof model

    K_next=[B -> F] -> A.

Shift it once. K_next[1] has B in degree -2, F in degree -1, and differential -i:B->F. There is a chain map

    g:K -> K_next[1]

whose only nonzero component is the IDENTITY F->F in degree -1. Its composite with K_next[1]->A[1] is exactly the representative F->A of e_r.

The shifted connecting map K_next[1]->B[2] is the projection from degree -2. Since K has no degree -2 term, its composite with g is STRICTLY ZERO. This proves

    e_(r+1)[1] e_r=0

in the same strict localization.

Only bounded inclusions, quotient maps and an identity contraction were used. The argument is valid in the completed source category and does not infer global hereditary dimension for that category. All longer consecutive Yoneda products containing such a pair also vanish by associativity.

## 4. A different factorization: finite exact tensor transport

Now restrict to a finite convex path packet and let S denote its hereditary path algebra. Its one-sided ideal powers are projective; in particular I^(r-1) is flat as a RIGHT S-module. Keep this finite hypothesis explicit.

For ideal powers, multiplication gives

    I^a tensor_S I^b -> I^(a+b).

It is an isomorphism. Indeed tensor the injection I^b->S with the right-flat I^a. The resulting injection into I^a tensor_S S=I^a has image exactly I^(a+b).

Apply the exact functor I^(r-1) tensor_S - to the FIRST adjacent row

    0 -> I^2/I^3 -> I/I^3 -> I/I^2 -> 0.

Multiplication and the quotient maps identify the resulting row with

    0 -> I^(r+1)/I^(r+2)
      -> I^r/I^(r+2)
      -> I^r/I^(r+1) -> 0.

Thus on the finite source,

    e_r=(I^(r-1) tensor_S -)(e_1),

under these specified identifications. This is degree-preserving application of an exact functor, NOT multiplication of Ext classes. It explains why nonzero adjacent classes coexist with zero consecutive Yoneda products.

The bimodule I^(r-1), its source actions, and its multiplication maps are part of this statement. It does not claim that an abstract Ext1 class e_1 alone, stripped of the source ideal and filtration, determines every possible filtered algebra.

Tensoring instead with the graded quotient G_(r-1) over S/I is not a substitute: the middle extension term is not generally an S/I-module, and such a substitution would discard the action that makes the extension nonsplit.

## 5. Exactly what transports to the completed presentations

Do NOT infer right-flatness of independently completed ideals from section 4. The established source comparison uses expanded marked-path tuples and their specified quotient norms, not a blanket exactness theorem for completed projective tensor products.

For fixed r and j=1,2,3, start algebraically with

    I^(r-1) tensor_S I^j.

Present it using finite expanded relation-path tuples and the actual coefficient-balancing relations. In each finite corner, the multiplication isomorphism of section 4 identifies it with I^(r+j-1). Give this balanced presentation its inherited native tuple quotient norm, and take the already declared all-radius completion.

The theta-tail factorization theorem supplies, uniformly in corners and at each fixed total depth, the exponential lifting bound and the contractive multiplication bound. Consequently the multiplication identifications extend to mutually inverse continuous maps on these PRESENTATION completions, with the stated radius losses. They respect the inclusions for j=1,2,3. Passing to their nested quotients gives the completed adjacent row above, strictly and compatibly.

This is a presentation-completed transport of the displayed extension diagram. It is enough to compare the constructed roofs. It is not asserted to define an exact functor on arbitrary completed modules, nor to identify those presentations with an unspecified completed tensor product of ideal Banach spaces.

On common-path domains retain their separate established norm comparisons or the common intersection. A change of source completion is not concealed in the tensor notation.

## 6. Receiver tensors and pentagons do not change Ext degree

The ordered receiver identity

    D_(r+1)(a_1 ... a_(r+1))
       =D(a_1) tensor_bal ... tensor_bal D(a_(r+1))

is a multiplicative/graded-layer identity. Postcomposing e_r with its admitted cycle observation gives the residual or rigged attachment already constructed. It remains an observation of a degree-one source extension.

The balanced pentagon verifies compatibility of the product presentations and their canonical reassociations. It is valuable coherence, but it does not identify the product of receiver states with a Yoneda product of connecting maps. Sections 1--3 give the explicit reason that conflation would be incorrect.

The cubic and quartic observers still prove their individual adjacent roofs nonzero: their finite hereditary restrictions detect e_2 and e_3. Nothing in the zero-product calculation contradicts those non-nullhomotopy proofs.

## 7. What is now established, and what is not

Established:
- the exact degree of every constructed adjacent attachment;
- zero consecutive Yoneda products in the actual strict completed category;
- finite exact generation of the adjacent rows from the first row by ideal-power tensor transport;
- compatible multiplication transport on the specific completed path-tuple presentations.

Not established:
- independent higher-Ext invariants detected by the existing higher-seam scalar witnesses;
- a general exact completed tensor functor;
- classification of all filtered objects from one abstract binary Ext class;
- nontrivial Toda/Massey or other secondary operations arising from choices of nullhomotopies.

Accordingly, the present evidence supports coherent nonzero adjacent extension data under source multiplication, not a claim of newly independent higher derived degrees. Any secondary-invariant claim would need its own typed definition and an obstruction to the relevant compatible nullhomotopies; the pentagon calculation alone does not supply one.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_adjacent_yoneda_comparison.py

The checker verifies a concrete three-step module diagram, the identity-complex kernel, the shifted chain lift and its zero composite, and the ideal-power degree bookkeeping. Its finite matrices illustrate the proof; completed zero-product vanishing follows from the actual strict filtration maps above, not from a finite numerical rank claim.
