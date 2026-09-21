# The four-prime relation layer has a forced nonsplit attachment

## Result

The missing layer is an explicit, source-generated attachment

0 -> P --mu--> I -> C -> 0,

where I is the typed terminal-record kernel, C=I/I^2, and P is the direct sum of the actual prefix/suffix diamond relation products. The map mu identifies P with the 24-dimensional I^2.

This sequence splits after forgetting to vector spaces, but does not split as a right source module, as a left source module, or as a source bimodule. Its nonzero connecting morphism is therefore genuine attachment data. Stable closure constructs that morphism from mu; no fitted splitting is needed or source-compatible.

The corresponding triangle reconstructs I as the fiber of the connecting map C->P[1]. This is a reconstruction from the admitted source kernel and its composition, not a claim that the abstract vector space C alone determines the source.

## 1. Canonical product object

Use the four-prime marked path algebra S, its typed terminal representation rho, I=ker rho, and B=S/I. Let s be the root and t the full terminal vertex. For each of the six vertices m reached after two events, put

R_(s,m)=e_s I e_m,

R_(m,t)=e_m I e_t.

Each is the actual two-dimensional marked-diamond kernel: the forgotten-route difference and the single-retained-record additivity difference. Define

P=direct_sum_(|m|=2) R_(s,m) tensor_C R_(m,t).

Its factors and middle labels are prescribed by the source. Define mu(a tensor b)=a b using chronological source composition.

Only the degree-two-by-degree-two products can occur in I^2: relations begin at event length two and the entire packet has length at most four. Hence mu has image exactly I^2. Unique path splitting at event position two proves injectivity, including the direct-sum separation of the six middle vertices. Thus

P is isomorphic to I^2, dim P=6 times 2 times 2=24.

All of I^2 is supported in the root-to-terminal corner. Its outer S actions are consequently fixed by the source idempotents, with nonidentity incoming/outgoing actions zero. The inclusion mu:P->I is a source-bimodule map.

## 2. The product layer is determined by conormal multiplication

Since I^3=0, multiplication descends canonically to

mbar:C tensor_B C -> I^2.

Changing a representative by I^2 changes its product by I^3=0. Changing a representative of a B-action also produces a triple ideal product, so the balanced tensor is well-defined.

In this four-event packet, the only composable factors in C tensor_B C both have event length two. Higher-length factors cannot compose within the packet. Positive-length B balancing terms would have total length at least five and vanish. Therefore the tensor decomposes into exactly the six summands defining P, and mbar is an isomorphism.

So the product layer itself can be recovered canonically from the typed conormal B-bimodule. This does not yet reconstruct the S-module extension I: its action across the two layers still matters.

## 3. A source-compatible splitting is impossible

Choose nonzero local relations

a in R_(s,m), b in R_(m,t).

Their product ab is nonzero, because multiplication on this tensor summand is injective. Let q:I->C be the quotient.

Suppose sigma:C->I were a right S-linear section. Since I^2 has right endpoint t, it has no component with right endpoint m. Therefore

sigma(q(a))=a.

But q(a)b=q(ab)=0, since ab lies in I^2. Right linearity would give

0=sigma(q(a)b)=sigma(q(a))b=ab,

a contradiction. The reflected argument rules out a left S-linear section. A bimodule section is therefore also impossible.

Equivalently, on the local relation span (a,b,ab), right multiplication by b sends a to ab, while the induced action on the conormal classes kills q(a). A linear lift of q(a) cannot make those actions agree.

The contradiction uses the full typed family, including the shorter relation a and its action by b. At the single root-to-terminal corner alone, the sequence is merely a sequence of vector spaces and does admit noncanonical splittings. One must not infer the nonsplitting theorem from its dimensions alone.

## 4. The forced extension class

The exact sequence defines

delta:C -> P[1]

in the derived category of S-bimodules, and also after forgetting either one of the two S actions. The nonsplitting result proves that delta is nonzero. In particular it is a nonzero element of the corresponding Ext^1(C,P).

As right S-modules, I is projective: it is a submodule of the hereditary source algebra S. P is also projective, being supported at the sink. Thus

[P --mu--> I]

in cohomological degrees -1 and 0 is an actual length-one projective model of C. In this model delta is represented by the identity on the degree-minus-one P component and zero on I.

This is explicit connecting data. A nullhomotopy for delta would supply a source-linear retraction of mu and hence split the exact sequence, contradicting section 3.

There is no conflict with the vanishing of higher Tor over the free source. This attachment is an Ext^1 class linking two relation layers, not a proposed Tor_2 class.

## 5. Stable reconstruction without selecting a section

The source-generated triangle is

P --mu--> I -> C --delta--> P[1].

It gives

I equivalent to Fib(delta).

An explicit fiber model, after the usual harmless sign change in the shifted P coordinate, is

P --(id,-mu)--> P direct_sum I

in degrees -1 and 0. Its projection to I is

(p,i) -> mu(p)+i,

its section is i -> (0,i), and its contracting homotopy is

H(p,i)=p.

The identities are

projection section=id,

id-section projection=dH+Hd.

All maps are source-linear, because they use the actual bimodule map mu. This deformation retract does not split 0->P->I->C->0: the extra P summand belongs to the fiber model, not to a chosen complement inside I.

The construction is the same stable cut-and-attachment mechanism already used for interval cones. Here its nonzero attaching map is forced by the composition of actual source relations. No independent global comparison is introduced.

## 6. Current exact dimensions

The current source-relation checker also computes the four-event terminal rank as 150 out of 384 marked paths. Consequently the root-to-terminal corner of the attachment has dimensions

0 -> C^24 -> C^234 -> C^210 -> 0.

The vector-space sequence is split, while the full typed module attachment is not. The missing information is therefore not another scalar dimension; it is the nontrivial compatibility with source composition.

The explicit product map uses all four combinations of the two local diamond relations at each middle vertex. Nima's forgotten-diamond boundary realization illuminates the forgotten component, but is not silently equated with the entire 24-dimensional product layer or with the other local relation. Their typing and comparisons remain explicit.

## 7. Naturality, reversal, and limits of the reconstruction claim

Every isomorphism of the admitted typed source representation sends I, I^2, mu, and the quotient to their corresponding objects. The connecting morphism is natural under that exact-sequence comparison.

Opposite reversal sends a product a b to b^op a^op and exchanges the two local relation factors. It therefore transports the entire attachment to its opposite. Derived contragredient duality reverses the triangle with its usual shift; it does not identify a relation coefficient with an inverse source arrow.

What is constructed is the attachment generated by the full source map rho and its ideal I. If only the abstract conormal space and the number 24 were supplied, delta would not be determined. Retaining the typed B-bimodule gives the product layer in this cutoff; retaining its source action and ideal embedding supplies the extension.

The exact analytical receiver may annihilate these relation arrows by definition of I. The source attachment remains meaningful before that quotient. No claim is made that terminal observation becomes faithful, that a quotient signed form is nondegenerate, or that Nima's distinct all-state seam modules have these same dimensions.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_relation_layer_attachment.py`

The command reruns the actual source product checker, verifies the 24 independent products, tests the local right/left nonsplitting obstruction symbolically for every linear section of that local quotient, and verifies the general fiber-model deformation-retract identities.

The global module nonsplitting and extension-class statements are proved above. The finite symbolic checks are not an Agda formalization of Ext or derived bimodules.

Artifacts: `results/relation-layer-attachment.json` and the freshly regenerated source-relation certificate.
