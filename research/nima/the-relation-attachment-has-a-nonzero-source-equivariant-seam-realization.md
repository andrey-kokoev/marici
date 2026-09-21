# The relation attachment has a nonzero source-equivariant seam realization

## Result

The existing single and joint derivatives assemble into a chain-level comparison from the actual relation resolution. Its joint-seam component represents the forced connecting morphism, not merely an independently retained product vector space.

That component is nonzero in the derived category of left source modules, of right source modules, and hence of source bimodules. It becomes nullhomotopic if the source actions are forgotten. After the canonical derived quotient it is exactly the injective joint derivative following the shifted-product projection. Under the finite prepared Clark receiver its product component remains nonzero.

This closes the requested attachment comparison at the finite source-equivariant level. No signed isometry of the relation images is asserted.

## 1. Inputs and conventions

Use:

- `../grothendieck/the-four-prime-relation-layer-has-a-forced-nonsplit-attachment.md`;
- `../grothendieck/the-relation-to-seam-map-detects-conormal-classes-and-kills-products.md`;
- `derived-terminal-quotient-retains-the-product-attachment-as-a-shift.md`.

Let S be the free four-prime marked source algebra, I its typed terminal-record kernel, B_rec=S/I, P_rel=I^2, and C_rel=I/I^2. The product inclusion is mu:P_rel->I. P_rel is supported only at the root s and full terminal t, and has dimension 24.

The source projective model of C_rel is

`K^(-1)=P_rel`, `K^0=I`, `d_K=mu`.

The source is hereditary, so this is a projective model on either the left or the right. It is also a bimodule complex quasi-isomorphic to C_rel, although no projectivity over the enveloping algebra is assumed.

We use cohomological shifts: `(T[-1])^n=T^(n-1)`, and shifting by -1 negates the differential.

## 2. Keep the outer source actions

The endpointwise seam spaces must be packaged before claiming source linearity. One explicit finite package is as follows.

Let R_N be the prescribed truncated memory algebra on W, at common capacity N>=4, and let

`R_typed=direct_sum_(x<=y) E_(x,y) R_N`

be the upper-incidence record algebra, with chronological multiplication and the actual vertex idempotents. This is an auxiliary record algebra, not a declaration of new arithmetic transitions. The analytical refinement A and S act through their typed coefficient maps into R_typed. The map from S factors through B_rec.

The two-term global analytical seam complex is

`T1^(-1)=R_typed tensor_(B_vert) K_A tensor_(B_vert) R_typed`,

`T1^0=R_typed tensor_(B_vert) R_typed`,

with differential `p k tensor q - p tensor k q`. Here B_vert is the vertex-idempotent algebra, distinct from B_rec, and K_A is the elementary analytical arrow space. Its outer S actions factor through B_rec. Taking an outer endpoint corner gives the previously used local seam complex.

The path derivative D restricts to an S-bimodule map

`D:I -> Z^(-1)(T1)`.

Indeed the product rule and r(I)=0 give D(a x)=r(a)D(x) and D(x a)=D(x)r(a) for x in I. Also D mu=0, so D factors through an injective conormal map

`j1:C_rel -> Z^(-1)(T1)`.

The injection is the previously proved resolution comparison; it is not deduced merely from the present matrix rank.

## 3. The labelled joint target and its degrees

For each two-event middle vertex m, retain the external tensor of the local seam complexes. Set

`T2=direct_sum_m T1_(s,m) tensor_C T1_(m,t)`.

Its degrees are -2,-1,0. The product comparison is

`j2:P_rel -> Z^(-2)(T2)`,

`j2(a b)=D_(s,m)(a) tensor D_(m,t)(b)`

on the canonical product summands. The unique source splitting at event position two and the retained m make this well-defined. The local injections imply j2 is injective.

T2 has outer source s and target t throughout. Since there is no nonidentity arrow into s or out of t, its outer S actions are just the corresponding vertex characters. In particular I acts by zero. This is an actual source-module structure, not a silent identification of different outer endpoint blocks.

For degree-minus-one local elements u and v, the external differential is

`d(u tensor v)=d u tensor v - u tensor d v`.

Hence j2 lands in cycles. There is no preceding degree-minus-three term, so these cycles are already nonzero homology classes. Shifting T2 by -1 places them in degree -1, matching P_rel[1]. This is an external two-seam construction, not Tor_2 over S.

## 4. The attachment chain map

Put

`Z=T1[-1] direct-sum T2[-1]`.

Define F:K->Z by

`F^(-1)(p)=(0,j2(p))`,

`F^0(i)=(D(i),0)`.

These formulas preserve the source actions. The chain equations are exactly

`D mu=0`, `d j2=0`, and `d D=0`.

No unmarked middle-vertex sum or degree-forgetting map is used.

Its joint component is the derived morphism

`phi:C_rel -> T2[-1]`.

Equivalently, let `i2:P_rel[1]->T2[-1]` be the chain map induced by j2. Then

`phi=i2 delta`.

This equality holds already on the displayed projective model: both maps are j2 in degree -1 and zero in degree zero.

The target being a direct sum does not by itself retain the attachment. The additional datum is the specified morphism F, and in particular its nonzero derived component phi. Discarding that component would return to the insufficient unconnected pair of homology images.

## 5. Source-linear nullhomotopy is impossible

Suppose phi were nullhomotopic as a map from K to T2[-1]. The target has no degree below -1. Therefore its degree-minus-one homotopy equation would require

`j2=H^0 mu`,

where `H^0:I->T2^(-2)` is source-linear.

For a,b in I, left linearity gives

`H^0(a b)=a H^0(b)=0`,

because I acts by zero on the target. Thus H^0 mu=0, contradicting injectivity and nonvanishing of j2. Right linearity gives the reflected contradiction.

Since K is bounded projective as a left source complex, non-nullhomotopy proves nonzero derived morphism, not merely nonzero coordinates. The same holds on the right. If the bimodule morphism were zero in its derived category, its image after forgetting one action would be zero, which is impossible. Hence the bimodule class is nonzero as well.

This argument does not require the relation image to have a nondegenerate restricted Green form.

## 6. Forgetting source actions really does lose this information

Over the scalar field, choose any linear extension of j2 from P_rel along the injective mu:P_rel->I. It supplies H^0 with H^0 mu=j2. Choose its range in j2(P_rel), which consists of cycles; then d H^0=0. It is a scalar nullhomotopy of phi.

The checker constructs such a homotopy explicitly using 24 selected coordinates of the actual 384 root-to-terminal marked paths. Its extraction matrix is a left inverse of the 24 product columns. Composing that extraction with j2 gives H^0 on the root corner, extended by zero to other endpoint blocks.

For a nonzero product a b, this homotopy has H^0(a b)=j2(a b), whereas source linearity would require a H^0(b)=0. The failed action equation is explicit.

Thus a scalar matrix rank alone cannot certify that the original nonsplit source attachment has been retained. The source-equivariant comparison is essential.

## 7. Match with the derived quotient

From the preceding quotient calculation,

`B_rec tensor_S^L C_rel = [P_rel --0--> C_rel]`.

The unit of change of rings is represented by

`eta^(-1)=id_(P_rel)`, `eta^0=q:I->C_rel`.

Because Z has a B_rec action, the adjunction gives a comparison from this derived quotient to Z. Its components are

`bar F^(-1)=(0,j2)`, `bar F^0=(j1,0)`.

Strictly on the chosen models,

`F=bar F eta`.

The product component is precisely j2 after the projection to P_rel[1], as predicted. This is an adjunction statement; it does not assume that derived base change fixes the entire T1 complex.

For the joint target alone, there is a stronger simplification: every term of T2 is supported at the source root on the left. It is therefore a sum of copies of S e_s, and base change fixes it as a left complex. Consequently the product-component calculation also directly describes its one-sided base-changed chain map.

## 8. Further finite Clark realization

Let X be the prepared finite right source receiver, factoring through B_rec, as in the preceding note. Its derived image of C_rel is

`(X tensor_(B_rec) C_rel) direct-sum (X_s tensor_C P_rel)[1]`.

Since the joint target is termwise root-supported projective,

`E_X(T2[-1]) = X_s tensor_C T2[-1]`.

Applying the receiver to phi therefore gives, on the shifted component,

`id_(X_s) tensor j2`.

The root carrier is nonzero. Tensoring over C preserves the injection into the lowest-degree cycle space. There are still no incoming boundaries at that degree. Hence this component remains nonzero after the actual finite derived receiver.

This differs from simply forgetting the S action on the original projective model: tensoring the source-linear resolution changes its differential to zero, while the scalar-only nullhomotopy from section 6 is not source-linear and cannot be tensor-transferred.

No equality between module duality and scalar Green contraction is inferred. Nor is this an isometry statement for D or j2. A full opposite-polarity chain comparison is a separate sign check: exchanging two seam factors of cohomological degree -1 introduces a Koszul minus sign, unlike reversal of feature words living in cohomological degree zero.

## 9. Recovering the source attachment on its precise images

Let

`C_seam=j1(C_rel)`, `P_seam=j2(P_rel)`.

The injections identify these with the prescribed source layers. The source extension transfers to

`0 -> P_seam --mu j2^(-1)--> I --D--> C_seam -> 0`.

Its connecting class is the transported delta, and is nonsplit. Here j2^(-1) means the inverse on its image, not a chosen inverse on the whole ambient seam space.

This does not say that the fiber of phi into the **entire** T2[-1] equals I: the ambient joint seam complex can contain additional classes. Reconstruction of I uses the exact product image and the retained connecting morphism. The construction uses the admitted source ideal and its action; it does not derive that action from two bare vector spaces.

## 10. Verification

`uv run --with sympy python research/nima/checkers/check_relation_attachment_seam_chain_map.py`

Fresh exact checks passed:

- telescoping on all 1,040 marked source paths;
- the typed product rule at all 4,176 cut positions;
- all 24 actual products have zero first derivative;
- all joint images are lowest-degree cycles, with a rank-24 selected minor;
- the external tensor differential and its shifted sign, including a wrong-sign hostile on noncycles;
- the explicit scalar-only nullhomotopy on the actual product columns;
- the left/right source-linearity obstruction;
- the shifted-projection component of the quotient comparison.

Artifact: `results/relation-attachment-seam-chain-map.json`.

The coefficient fixture retains all fifteen chamber directions. Analytical transfer uses the existing finite source-feature injection. The derived nonvanishing and receiver statements use the projectivity and module-action arguments above; they are not inferred solely from the finite minor. No Agda verification of the new derived comparison is claimed.
