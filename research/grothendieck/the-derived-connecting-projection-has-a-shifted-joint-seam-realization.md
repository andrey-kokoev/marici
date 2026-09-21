# The derived connecting projection has a shifted joint-seam realization

## Result

The derived terminal image of the product attachment and the labelled joint two-seam construction now have an explicit chain-level comparison. It retains the prepared root carrier, all six middle-vertex labels, and the required cohomological shift.

On the canonical source-product cycle subcomplex, the comparison is an isomorphism and carries the derived image of delta exactly. Into the full joint-seam complex it is an injection on the relevant homology, not an equivalence with that larger complex.

This compares the derived base-changed attachment. It does not contradict the obstruction to descending the original nonsplit source extension as an ordinary terminal-quotient module extension.

## 1. Correct derived domain

Keep S, B=S/I, P=I^2 and C=I/I^2. Use LEFT source modules and the finite prepared right receiver X, which factors through B. The source projective model of C is

[P -> I], in degrees -1 and 0.

Nima's change-of-rings computation gives

B tensor_S^L C = [P --0--> C].

Both terms are projective as left B-modules. Thus, writing

U=X tensor_B C,

V=X_s tensor_C P,

one obtains the explicit receiver model

E_X(C)=U direct_sum V[1],

E_X(delta)=pi:U direct_sum V[1] -> V[1].

The map pi is identity in degree -1 and zero in degree zero. The root factor X_s is essential: this is not a comparison involving only the abstract 24-dimensional vector space P. It follows from the root support of P as a left module.

The displayed model is induced by the specified source projective resolution, not a selected vector-space splitting of the original source extension.

## 2. Actual joint-seam complex

For each two-event middle vertex m, take the two local seam complexes

C_(s,m), C_(m,t),

each in degrees -1 and 0. Retain the label m and put

J=direct_sum_m C_(s,m) tensor_C C_(m,t).

This complex has degrees -2,-1,0. On degree-minus-two tensors its differential is

d_J(a tensor b)=d a tensor b-a tensor d b.

The minus sign is cohomological: both local seam elements have degree -1. It has nothing to do with the retained-letter grading.

The local relation derivatives are actual closed vectors, not merely chosen homology representatives. Consequently the previous map of product relations defines a literal chain map

j:P[2] -> J,

j(a b)=D_(s,m)(a) tensor D_(m,t)(b),

using the canonical isomorphism P=direct_sum_m R_(s,m) tensor R_(m,t). No factorization of a general product vector into one decomposable tensor is required; the formula extends linearly through that isomorphism.

The map is injective in degree -2. There is no preceding degree -3 term in J, so it is also injective on homology. Its 24 independent source directions were checked with their actual coefficient maps.

## 3. The required shift and comparison map

Use the convention (K[r])^n=K^(n+r). Therefore J[-1] places its raw degree-minus-two cycles in degree -1, exactly where V[1] lives.

Set

T=X_s tensor_C J[-2].

The chain map j gives

iota=1_(X_s) tensor j[-2] : V -> T.

Now define

Theta=iota[1] composed pi
 : E_X(C) -> T[1]=X_s tensor_C J[-1].

This is the desired comparison. Its only nonzero source component is

Theta^(-1)(x tensor p)=x tensor j(p).

The target differential vanishes on this image because j(p) is a joint seam cycle. Its degree-zero source component on U is zero, exactly as for E_X(delta).

Thus the square

E_X(C) --pi--> V[1]

  | Theta          | iota[1]

T[1] -----------> T[1]

commutes as a chain-map identity, with the bottom map the identity. The equation is not inferred from dimensions or from a fitted change of basis.

For every finite root-carrier dimension D, the induced degree-minus-one map has rank 24D. It remains nonzero without specifying a basis of X_s.

## 4. Identification on the canonical source-product image

Let T_src be the image of iota, regarded as a subcomplex of T. It is concentrated in degree zero and consists of closed vectors. Since iota is injective, it gives a canonical isomorphism

V -> T_src.

No ambient projection, orthogonal complement, or inverse Green matrix is selected. The comparison restricted to this image is precisely

U direct_sum V[1] --pi--> V[1]

transported to

U direct_sum V[1] --Theta_src--> T_src[1].

This is an isomorphism of the corresponding derived attachment triangles. The middle receiver object is U, and the map from V to U is zero after the specified derived base change.

For the full target T, the induced enlargement is the homotopy pushout of V->U along iota:V->T. Its connecting map is Theta. Extra joint-seam classes remain extra target data; they are not declared part of the source product module.

This distinguishes two valid statements:

- the source-product cycle subcomplex realizes exactly the shifted connecting projection;
- the complete joint-seam complex is a larger receiver into which that realization embeds.

## 5. Contragredient duality

Apply finite cochain conjugate duality to

Theta=iota[1] pi.

Functoriality gives

D(Theta)=D(pi) D(iota[1]).

The projection pi becomes the inclusion of D(V)[-1] into D(E_X(C)); its nonzero component is in cohomological degree +1. The map D(iota[1]) is restriction of dual observations along the actual product-cycle inclusion, with the corresponding shifts.

Thus the dual comparison square also commutes, and the connecting projection/inclusion pair is preserved with its correct variance. On the canonical source-product image it is an isomorphism of dual pairs.

This does not assert that the restriction of the ambient signed Green form to the product-cycle image is nondegenerate. Canonical vector-space duality is sufficient for the comparison. Identifying it with a particular signed mate requires the already specified pairing identifications, not inversion of a potentially degenerate pullback Gram matrix.

## 6. What is natural and what remains separate

The construction is determined by:

- the source relation multiplication and its typed middle-vertex decomposition;
- the actual local path derivatives;
- the given prepared-root carrier;
- the source projective model used for derived base change.

It is compatible with changes of presentation that preserve these maps. It does not require a chosen basis of relations, a splitting of I, or removal of the root carrier. Tensoring a root vector with fixed source-derived cycle templates is linear; no copying of an unknown root state is asserted.

The result lives after one-sided derived evaluation. It is not a B-linear realization of the original source sequence 0->P->I->C->0 with the original ordinary C as its domain. The domain here is the enlarged derived object U direct_sum V[1]. That distinction is why the earlier ordinary quotient descent obstruction and the present nonzero connecting projection are compatible.

The raw joint cycle degree -2 also does not assert Tor_2 over the hereditary source. J is an external tensor of two local seam complexes, and J[-1] is the deliberately shift-correct comparison target.

Terminal composition followed by the first path derivative still kills every product relation. The comparison here succeeds by retaining the joint seam and its derived shift rather than performing that compression first.

## 7. Verification

`uv run --with sympy python research/grothendieck/checkers/check_shifted_joint_seam_attachment.py`

The checker reruns the actual 24 product-cycle construction, then verifies:

- closure under the joint tensor differential;
- d_J squared equals zero;
- rejection of the wrong tensor sign on a basis element;
- the actual 24-dimensional product injection;
- its tensor with an illustrative two-dimensional root carrier, of rank 48;
- the connecting projection square and its conjugate-dual square;
- the cohomological shift taking raw degree -2 to degree -1.

The 24 actual coefficient columns occupy 6,464 joint degree-minus-two coordinates. That coordinate count is not an analytical feature dimension. The illustrative root dimension two is not substituted for the actual finite Clark carrier dimension.

The chain construction and image restriction are proved above. The finite tests do not formally implement all perfect-module categories or establish a Green isometry.

References:

- `research/nima/derived-terminal-quotient-retains-the-product-attachment-as-a-shift.md`;
- `the-relation-to-seam-map-detects-conormal-classes-and-kills-products.md`;
- `the-four-prime-relation-layer-has-a-forced-nonsplit-attachment.md`.
