# The relation-to-seam map detects conormal classes and kills products

## Result

There is a canonical comparison from the source conormal relation module into Nima's analytical-refinement seam homology, for each fixed pair of outer endpoints. It is induced by the path derivative, not by matching dimensions.

The same derivative kills I^2 identically. Hence the ordinary one-seam bridge does not carry the full nonsplit attachment 0->I^2->I->I/I^2->0 faithfully. All 24 four-event product relations vanish under it.

Retaining two seam records jointly, with their actual middle vertex, detects all 24 products. This supplies a precise required enrichment: the product layer lives in the joint two-seam construction, not in another homology group of the single original-source tensor product.

The comparison also identifies the previously separate counts: Nima's five three-prime forgotten incidence cycles are exactly the retained-degree-zero part of the conormal bridge.

## 1. Sources and targets

Let S be the free two-mark source algebra. Let A=T_B(K) be the typed analytical refinement from Nima's balanced-counit construction, with K_e=C Omega_e direct_sum W_e and the same source vertices and elementary transitions. There is a generator map

j:S->A, e^0->Omega_e, e^1->g_e.

The two generator images are independent because they occupy different retained degrees and g_e is nonzero. Thus the marked generator map into each K_e is injective.

Fix the packet-wide memory capacity at least as large as every admitted source route. Use the right memory module P and opposite prefix-action module Q from the common-capacity construction. Their degree-minus-one seam term is

C_A^(-1)=P tensor_B K tensor_B Q,

with differential partial(p tensor k tensor q)=p k tensor q-p tensor k q.

Only the existing marked generator directions are used to define the bridge. Additional dual-observation directions in W remain in the target; they are not declared new arithmetic generators.

## 2. Canonical path derivative

For w=e_1...e_n, let r(e_i) be its emitted memory element, either 1 or g_e. Define

D(w)=sum_(i=1)^n
 r(e_1...e_(i-1)) tensor j(e_i) tensor r(e_(i+1)...e_n),

with each summand in the typed edge block of e_i. Outer endpoint labels are fixed throughout the comparison.

Its boundary telescopes:

partial D(w)=(target;r(w),1)-(source;1,r(w)).

All intermediate cut contributions cancel with their actual vertex labels. Consequently if w is replaced by any typed linear source relation a with r(a)=0, then D(a) is a seam cycle.

The derivative satisfies the two-sided product rule

D(ab)=r(a) D(b)+D(a) r(b),

where the outer memory actions retain the appropriate endpoint types.

## 3. The product layer is necessarily killed

Let I be the kernel of the typed terminal recorder. If a,b lie in I, the product rule gives

D(ab)=0.

Therefore D factors canonically through

I/I^2 -> H^(-1)(C_A).

This is a structural consequence of evaluating both external memory factors through the same recorder. It does not depend on choosing a basis, on a metric, or on numerical feature values.

For the four-event packet, all 24 nonzero products in I^2 have zero single-seam derivative. Thus this particular bridge cannot faithfully carry the full relation attachment or its product subobject. A nonzero image of I^2 cannot be obtained merely by reinterpreting D as a map from I rather than I/I^2.

## 4. Why the conormal map is injective

Put B_rec=S/I and fix outer vertices s,t. The source-generated prefix and suffix modules are

M=e_s B_rec, N=B_rec e_t.

Their elements are actual memory records, so their vertex components embed into the corresponding P and Q components. They are modules for the marked source S; they need not be closed under every additional analytical generator of A.

The two free-source resolutions nevertheless have a direct comparison:

M tensor_B K_marked tensor_B N -> P tensor_B K tensor_B Q,

M tensor_B N -> P tensor_B Q.

It uses the two memory embeddings and the injective generator map K_marked->K. Both maps are injective over the scalar field, and their differentials commute by the admitted source actions.

Both complexes are concentrated in cohomological degrees -1 and 0, since both source algebras are free typed path algebras. Thus degree-minus-one homology is a kernel with no preceding boundaries. The degree-minus-one injection restricts to a homology injection.

Combining with Tor_1^S(M,N)=e_s(I/I^2)e_t yields the claimed canonical injection into the analytical seam homology. The standard path-derivative description of the source Tor class gives precisely D above.

This is an endpointwise statement. Combining different outer endpoint pairs requires retaining those extra labels; they are not silently identified in one unlabelled seam space. Also, if extra source relations are imposed on A, a longer resolution may be needed and this injectivity proof must be revisited.

## 5. The five incidence cycles now have a comparison map

In retained degree zero, every marked event is forgotten, its memory is vacuum, and its seam letter is Omega_e. The differential is the ordinary edge-incidence map of the admitted graph.

For the three-prime cube, the five independent differences between its six full routes map under D to the five-dimensional graph-cycle space. The map is an isomorphism on that sector. This identifies Nima's five forgotten seam classes with the degree-zero conormal classes, rather than merely observing that the numbers agree.

The finite checks give:

| Prime count | Forgotten full-route relations | Incidence cycles | First-derivative kernel |
| --- | ---: | ---: | ---: |
| 2 | 1 | 1 | 0 |
| 3 | 5 | 5 | 0 |
| 4 | 23 | 17 | 6 |

At four primes the six lost forgotten-sector combinations are exactly the forgotten-relation-by-forgotten-relation products, one per two-event middle vertex. They are the retained-degree-zero portion of the full 24-dimensional I^2.

The two three-prime marginal ghosts are still not the whole seam space. Their all-forgotten generator maps into one direction of the five-dimensional incidence sector; their other generator has retained degree one. The new comparison preserves these distinctions.

## 6. Joint seams recover the product subobject

For each two-event middle vertex m, apply the local derivative to the two local relation spaces:

D_(s,m):R_(s,m)->H^(-1)(C_(s,m)),

D_(m,t):R_(m,t)->H^(-1)(C_(m,t)).

These maps are injective. Retain m and tensor them to obtain

j_2:direct_sum_m R_(s,m) tensor R_(m,t)
 -> direct_sum_m H^(-1)(C_(s,m)) tensor H^(-1)(C_(m,t)).

Tensor products over C and the labelled direct sum preserve injectivity. The source is canonically I^2 in the four-event packet. The checker constructs an explicit nonzero 24-by-24 minor for these joint images.

Equivalently, the target is the degree-minus-two part of the EXTERNAL tensor of the two local seam complexes, via the field-valued Kunneth identification. This does not assert a nonzero Tor_2 over the original hereditary source algebra. The external two-seam object is a different derived construction.

The joint record is essential: composing first and then applying D gives zero, whereas keeping the two local seam cycles and their middle label gives a faithful product-layer observation.

## 7. What this establishes about the nonsplit attachment

The comparison now has two explicit pieces:

- the conormal quotient embeds into a single-seam cycle space;
- the product subobject embeds into a labelled joint two-seam space.

They are not yet a replacement for the connecting morphism

delta:I/I^2 -> I^2[1].

The source sequence is nonsplit, so taking an unconnected direct sum of those two receiver images would discard its attachment. To realize the whole extension in seam terms one must carry delta between the corresponding joint receiver objects, with its source-module compatibility. The ordinary first derivative cannot do that by itself because it kills the entire product term.

This is the exact failure requested by the comparison test, and it specifies the needed enrichment rather than proposing another scalar observer.

No signed-isometry statement is proved for D or j_2. The ambient seam pairings and their Green mates remain those of the existing construction; a relation kernel is not automatically their radical.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_relation_to_seam_bridge.py`

Passed exact checks:

- telescoping boundaries on marked paths;
- all local diamond relations give nonzero seam cycles;
- all 24 product relations have zero first derivative;
- their labelled joint two-seam images have rank 24;
- the degree-zero incidence comparison for two, three, and four primes.

The checker retains the fifteen chamber coordinates, so it introduces none of the earlier two-feature compression relation. Analytical transfer uses the already proved finite source-feature injectivity. The general conormal injection is the chain-level argument in section 4, not an inference from a finite rank match.

References:

- `research/nima/all-state-clark-sewing-is-a-balanced-counit-with-derived-seam-data.md`;
- `research/nima/three-prime-balanced-counit-relation-filtration.md`;
- `the-four-prime-relation-layer-has-a-forced-nonsplit-attachment.md`.
