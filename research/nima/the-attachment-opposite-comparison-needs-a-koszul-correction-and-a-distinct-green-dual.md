# The attachment opposite comparison needs a Koszul correction and a distinct Green dual

## Result

The source-equivariant seam attachment admits the requested opposite-history comparison, but **the bare graded swap has the wrong sign on every product channel**. With the single-seam normalization fixed by the path derivative, the joint comparison must be the negative of the graded braided reversal.

The corrected comparison is an involutive chain map and commutes with the actual attachment map. Separately, the prescribed paired Green carriers give the contragredient square for its finite derived realization. The dual connecting projection is an inclusion, and the dual joint observation is surjective onto the shifted product observation space.

These are two distinct squares. Opposite-history creation is not Green contraction, and reversing a source bimodule is not its perfect-module dual. No identification between those operations is needed or justified.

## 1. Input and notation

Use `the-relation-attachment-has-a-nonzero-source-equivariant-seam-realization.md` and its notation:

`K=[P_rel --mu--> I]`, in degrees -1,0;

`F:K -> T1[-1] direct-sum T2[-1]`,

with `F^(-1)=(0,j2)` and `F^0=(D,0)`.

The joint target T2 keeps all six middle vertices. Its unshifted degrees are -2,-1,0. Its joint component represents

`phi=i2 delta:C_rel -> T2[-1]`.

All source scalars are conjugated under passage to the conjugate opposite algebra. No real structure on the actual feature space W is assumed: conjugate features live in the conjugate space. Real chamber labels in the finite checker are coordinate labels, not an identification of complex conjugation with the fundamental symmetry J.

## 2. Single-seam reversal fixes the normalization

Write r1 for raw reversal of a seam record:

`(x->y; u,k,v) -> (y->x; reverse(v),k,reverse(u))`,

with conjugation of coefficients and conjugate feature labels. Write r0 for raw reversal of a cut state, interchanging and reversing its two memory words while preserving the cut vertex.

The differential satisfies

`d_op r1 = -r0 d`.

The minus sign is the reversal of the two endpoint contributions. Therefore the derivative-compatible chain comparison is

`R1^(-1)=r1`, `R1^0=-r0`.

It satisfies

`R1^(-1) D(a)=D_op(a^op)`.

It is involutive. Shifting this chain map by -1 does not change its components; both complexes' differentials acquire the usual shift sign.

## 3. The joint correction is forced

The canonical graded exchange of two degree-minus-one seam factors introduces a minus sign. Let tau denote the graded tensor swap. The uncorrected chain comparison is

`B2=tau (R1_left tensor R1_right)`.

On the bottom degree,

`B2(Da tensor Db)=-D(b^op) tensor D(a^op)`.

But source product reversal is `(a b)^op=b^op a^op`, with no minus sign: a and b are source algebra elements in cohomological degree zero. Hence B2 does not commute with j2.

The required normalized comparison is

`R2=-B2`.

After the raw exchange of the two factors, its signs are:

| Unshifted degree of T2 | Sign |
|---|---:|
| -2 | +1 |
| -1 | +1, exchanging the two mixed summands |
| 0 | -1 |

Then

`R2 j2(a b)=j2_op(b^op a^op)`.

The middle vertex m is unchanged as a label; the two local factors exchange their roles. This is not a sum over unlabelled seams.

Both joint chain equations hold, including on noncycles, and R2 is involutive. The checker verifies these statements with complex coefficients. The uncorrected braided comparison has residual `-2 j2_op`, of rank 24. Thus the correction cannot be omitted or hidden by restricting attention to dimensions.

## 4. The actual attachment square

Let sigma_K denote conjugate opposite reversal on the source bimodule complex. It preserves cohomological degrees and satisfies

`sigma_I mu=mu_op sigma_P`.

The connecting map on K is identity in degree -1, so its opposite-history square also commutes with no added source sign.

With R1 and R2 as above,

`(R1[-1] direct-sum R2[-1]) F = F_op sigma_K`.

In degree zero this is the path-derivative identity. In degree -1 it is precisely the corrected joint-product identity. Thus the normalization is fixed by the original inclusion and derivative, rather than fitted to a metric.

## 5. Contragredient duality is a different operation

For a cochain complex V, use the conjugate dual convention

`(V^h)^n=(V^(-n))^h`,

`d_(V^h)^n=(-1)^(n+1) (d_V^(-n-1))^vee`.

This reverses cohomological degrees. In contrast, the opposite-history comparisons in sections 2–4 preserve them.

For source modules the relevant operation is the perfect-module dual D_S^h, obtained from conjugate source-linear Hom into S, not merely path reversal of the underlying ideal. For example, the dual of a left vertex projective S e_s is the corresponding right projective e_s S. It is not obtained by treating a root-supported product vector space as a new opposite root-supported vector space.

Consequently no equation identifying the opposite-history attachment with the contragredient attachment is asserted. The naturality square below is the correctly typed replacement.

## 6. The prescribed Green presentation of the dual complex

On an existing nondegenerate ambient carrier, write

`beta_V(y)(x)=q_V(x,y)`.

For d:V->W its Green mate satisfies

`beta_V d^sharp=d^vee beta_W`.

Thus the Green presentation of the dual cochain differential is

`d_G^n=(-1)^(n+1) (d_V^(-n-1))^sharp`.

The beta maps commute with these differentials. For T=T2[-1], if the unshifted joint differentials are d2 and d1, then the ordinary conjugate dual differentials are

`-d1^vee`, then `+d2^vee`.

The signs combine the shift and the cochain dual; neither can be discarded. The checker verifies both beta squares and d_G squared equals zero using non-real differentials and nondegenerate signed tensor forms. These are algebraic fixtures, not evaluations of the spectral Clark Gram matrix.

For the actual finite receiver, nondegeneracy and the tensor/vertex beta maps are already provided by the prescribed ambient memory and seam pairings. The same coordinate-free identities therefore apply. No form on I or P_rel is chosen.

## 7. Naturality for the finite derived attachment

Let X be the prepared receiver and Y its prescribed Green-mate representation over conjugate(S)^op. Write T=T2[-1]. Both K and T are perfect left source complexes: K has the projective ideal resolution, and every term of T is root-supported projective.

The existing generator-to-derived duality theorem supplies natural vertical equivalences in

```
E_Y(D_S^h T)  --E_Y(D_S^h phi)-->  E_Y(D_S^h C_rel)
      | beta_T                              | beta_C
      v                                     v
(E_X T)^h     --(E_X phi)^vee-->    (E_X C_rel)^h .
```

This is a square of the actual perfect objects and their paired observation carriers. It follows from finite-projective tensor–Hom evaluation and the prescribed generator beta maps, not from identifying opposite creation with a mate.

Let

`A0=X tensor_(B_rec) C_rel`, `U=X_s tensor_C P_rel`.

The preceding computation gives

`E_X(C_rel)=A0 direct-sum U[1]`,

with connecting map the projection onto U[1]. Its conjugate dual is the inclusion

`U^h[-1] -> A0^h direct-sum U^h[-1]`.

The realized joint component is j_X=id_(X_s) tensor j2 on the shifted term. Its dual is

`(E_X phi)^vee = (dual connecting inclusion) composed with j_X^vee`.

Because j_X injects into the lowest-degree cycle space, its dual induces a surjection onto U^h in degree +1. This explicitly matches the shifted product observation, with the correct contravariant direction.

## 8. Paired observations do not require a relation metric

For the unshifted joint coefficient inclusion j2:P_rel->T2^(-2), the prescribed ambient pairing gives the observation map

`j2^vee beta_(T2^(-2)) : T2^(-2) -> P_rel^h`.

In coordinates this is `J2^* G`, where G is the existing ambient Gram matrix. Its target is the conjugate dual P_rel^h, **not** P_rel equipped with a newly chosen Hermitian form.

This map is surjective: beta is an isomorphism and the finite-dimensional dual of j2 is surjective. Its kernel is the ambient orthogonal annihilator of j2(P_rel). Equivalently, the observation quotient is canonically P_rel^h. Restricting the form to j2(P_rel) need not be nondegenerate.

The chain identity d j2=0 implies that the observation annihilates the corresponding Green-dual boundaries, so it descends to the dual homology. Tensoring with the existing root-carrier beta gives the same statement for U.

The checker includes an isotropic image whose restricted Gram matrix is zero but whose ambient paired observation is surjective. This rejects the invalid inference that a nonzero derived attachment must have a nondegenerate self-pairing on its primal relation image.

## 9. The forbidden identification has an explicit residual

On the vacuum, opposite prefix creation by a nonzero feature is nonzero. The scalar Green mate of creation is contraction and vanishes there. The checker retains this hostile with a complex feature and a signed memory form.

Thus:

- the corrected opposite-history square commutes;
- the paired contragredient square commutes;
- identifying their receiver actions is false.

No positive relation metric, Green isometry for j2, or equivalence between the two duality operations follows.

## 10. Higher critical packets and the new refinement boundary

The new input `../grothendieck/packet-refinement-preserves-the-relation-tower-but-coarse-seams-lose-higher-products.md` supplies the uniform tower and the critical 2r-prime joint-seam maps. The normalization above extends to those retained r-factor joint complexes:

`R_r = (-1)^(r(r-1)/2) tau_reverse (R1 tensor ... tensor R1)`.

The prefactor cancels the graded reversal sign on r degree-minus-one local cycles, so the product comparison agrees with ordinary source product reversal. If q local factors occupy degree zero, the sign after raw reversal is

`(-1)^(r(r-1)/2 + q + (r-q)(r-q-1)/2)`.

For three seams the raw degree -3,-2,-1,0 signs are respectively +,-,-,+. The required attachment shift is [-2], as in the new note; it moves the bottom product class to degree -1. Thus the 720-channel critical stage also requires the overall minus correction to graded reversal. No new 720-column rank computation is claimed here.

The phase satisfies

`c_(a+b)=c_a c_b (-1)^(a b)`, where `c_r=(-1)^(r(r-1)/2)`.

This is the compatibility of the orientation phases when retained factors are regrouped. The checker tests the differential signs and involutivity for all degree patterns through six factors. The general identity follows from splitting the pairs counted by the binomial coefficient into within-block and cross-block pairs.

This does **not** construct refinement from compressed conormal blocks. If D(a b)=0 while D(a) tensor D(b) is nonzero, no sign correction can recover the discarded record. The next construction must retain the internal derived relation layers before changing cuts, and establish descent through nonminimal product factorizations. The present result supplies the opposite and dual conventions for that construction, not its missing refinement maps.

## 11. Verification

`uv run --with sympy python research/nima/checkers/check_attachment_opposite_and_dual.py`

Passed:

- opposite derivative identities on all 1,040 actual marked paths;
- corrected reversal on all 24 labelled product channels;
- rank-24 failure of the uncorrected braided reversal;
- both joint chain squares and involutivity in every degree;
- higher reversal differential signs through six retained seam factors;
- conjugation and transpose hostiles with complex coefficients;
- cochain Green-dual beta squares and annihilation of dual boundaries;
- isotropic-image and creation-versus-contraction hostiles.

Artifact: `results/attachment-opposite-and-dual.json`.

The actual source/chamber data are used for the reversal checks. The signed matrices used to check universal Green identities are explicitly fixtures, not sampled or fitted analytical pairings. Analytical transfer uses the existing finite nondegenerate beta maps and perfect-module duality theorem. No new Agda verification or numerical spectral Gram computation is claimed.
