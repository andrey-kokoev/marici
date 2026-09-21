# The derived terminal quotient retains the product attachment as a shift

## Result

Let S be the finite four-prime marked source path algebra, rho its typed terminal coefficient recorder, and B=S/I with I=ker rho. Put

`P_rel=I^2`, `C_rel=I/I^2`.

For the admitted source, P_rel has dimension 24 and I^3=0. The forced nonsplit source attachment is

`P_rel --mu--> I -> C_rel --delta--> P_rel[1]`.

One-sided derived quotient gives the explicit model

`B tensor_S^L C_rel = [P_rel --0--> C_rel]`,

in degrees -1 and 0. Thus it is equivalent to C_rel direct-sum P_rel[1]. Under this identification the image of delta is **projection onto P_rel[1]**, and is nonzero.

The finite prepared Clark receiver factors through B. Its further derived image has the nonzero shifted summand

`(X_s tensor_C P_rel)[1]`,

where X_s is the root carrier. Therefore this specific derived receiver does not annihilate the connecting map, even though every relation product is zero as an ordinary terminal operator.

This is not a higher Tor group over the hereditary source: the new group is Tor_1^S(B,C_rel), not Tor_2^S(B,B).

## 1. Source typing and dimensions

Inputs:

- `../grothendieck/the-four-prime-relation-layer-has-a-forced-nonsplit-attachment.md`;
- `../grothendieck/generator-to-derived-extension-with-the-clark-dual-receiver.md`;
- `../grothendieck/the-relation-to-seam-map-detects-conormal-classes-and-kills-products.md`.

Here B denotes the **quotient algebra S/I**, not the vertex-idempotent algebra used in the seam tensor formulas.

The new checker recomputes all 81 admitted endpoint blocks using exact rational sparse elimination. The global dimensions are

| Object | Full typed dimension |
|---|---:|
| S | 1040 |
| B | 582 |
| I | 458 |
| P_rel | 24 |
| C_rel | 434 |

In the root-to-terminal corner they are respectively 384,150,234,24,210. The numbers 234 and 210 must not be substituted for the entire source modules.

All products in I^2 have root source s and full terminal target t. There are six two-event middle vertices, each contributing the tensor product of its two local two-dimensional diamond relation spaces. The checker rebuilds and verifies the 24 independent product columns, including all four combinations of the local relation types.

There are no event-length-zero or event-length-one relations. Three ideal factors would require at least six events, while the source has at most four; therefore I^3=0. This is an event-length statement, not a truncation in retained-record degree.

## 2. One-sided projectivity and the quotient model

We use perfect **left** source modules. The finite acyclic free path algebra S is hereditary. Thus I, as a left submodule of S, is projective. P_rel is projective as well; in fact its only left support is the root, so it is a direct sum of 24 copies of S e_s.

Consequently

`[P_rel --mu--> I]`

is a length-one projective model of C_rel. Apply F_B=B tensor_S^L - to this model. Ordinary tensor on its terms computes the derived functor, and

`B tensor_S I = I/I^2 = C_rel`,

`B tensor_S P_rel = P_rel/(I P_rel) = P_rel`.

The second identity uses I^3=0. The induced differential is zero because mu lands in I^2, which is killed in I/I^2. This proves the displayed zero-differential model.

Both resulting modules are projective as left B-modules: extension of scalars preserves projectives, and both terms before extension were projective over S. In particular C_rel is projective over B, although it was not projective over S in the nonsplit attachment.

Thus

`Tor_1^S(B,C_rel)=P_rel`,

`Tor_0^S(B,C_rel)=C_rel`,

and higher Tor groups vanish. These statements do not contradict

`Tor_1^S(B,B)=I/I^2`, `Tor_(>=2)^S(B,B)=0`.

The second argument has changed.

## 3. What happens to the connecting morphism

In the source projective model, delta is identity on P_rel in degree -1 and zero in degree zero. After base change it remains precisely that chain map:

`C_rel direct-sum P_rel[1] -> P_rel[1]`.

It is not nullhomotopic: both differentials are zero, so the boundary of any proposed homotopy is zero, while its degree-minus-one component is the identity.

The image triangle is

`P_rel --0--> C_rel -> C_rel direct-sum P_rel[1] -> P_rel[1]`.

Do not reinterpret this as a nonzero element of Ext_B^1(C_rel,P_rel). That Ext group is zero because C_rel is projective over B. The domain of the displayed connecting map is the **derived image** F_B(C_rel), which includes P_rel[1], not just the ordinary module C_rel concentrated in degree zero.

Nor does the split image complex supply a source-linear splitting of the original sequence. The original extension was nonsplit over S. The zero differential only appears after the specified change of rings.

## 4. Factorization of the actual finite Clark receiver

Fix the prepared-source version of the receiver, capacity N>=4, and the prescribed bounded injective finite-chamber feature map

`Lhat:V->W=W0+J W0`.

After unitary trivialization of the prepared source lines, an elementary marked arrow acts by identity or right creation of Lhat(v_e), in its actual source/target block. A marked path acts by the chronological retained tensor record.

Therefore the action factors as

`S --rho--> B -> End_chronological(X)`.

Here End_chronological means the right-module action; ordinary column matrices compose in the reverse order from chronological source words.

For N>=4, the kernel of this action is exactly I. Indeed the induced map on every retained tensor degree up to four is injective, and applying the operator to the vacuum at its source vertex recovers that tensor coefficient in its target block. Endpoint blocks remain separated. Conversely, a zero coefficient tensor gives the zero creation polynomial on all input memories. Truncation creates no extra vacuum kernel at these admitted source degrees.

The use of the full spectral feature family is essential. A two-dimensional sheet vector at one point cannot inject the fifteen-dimensional chamber space. The small checker fixture tests annihilation/factorization, not this analytical injectivity theorem.

Write X for the resulting right B-module. The given exact receiver is

`E_X(M)=X tensor_S^L M`.

Derived associativity gives

`E_X(C_rel) = X tensor_B^L (B tensor_S^L C_rel)`.

Since C_rel and P_rel are projective over B, this simplifies to

`E_X(C_rel) = (X tensor_B C_rel)
                 direct-sum (X tensor_B P_rel)[1]`.

No unproved flatness of X is needed.

## 5. The shifted analytical term is nonzero

The root is a source of the chronological quiver. Hence B e_s is one-dimensional, and the left B-module P_rel has the canonical support description

`P_rel = B e_s tensor_C (e_s P_rel)`.

It follows that

`X tensor_B P_rel = X e_s tensor_C P_rel = X_s tensor_C P_rel`.

The prepared root carrier contains its nonzero vacuum. Since P_rel has dimension 24, this tensor product is nonzero. The receiver image E_X(delta) is projection onto its shift and is therefore nonzero.

This distinguishes three operations:

- interpreting a relation element as an arrow operator: zero;
- interpreting the source module P_rel under the exact receiver: 24 root-carrier copies;
- interpreting the connecting map from the derived image of C_rel: nonzero shifted projection.

It is incorrect to infer that a functor sends the module I^2 to zero merely because the ideal's elements act by zero on X.

No positive or nondegenerate Green form on the arithmetic relation subspace is inferred. The surviving term is a derived module observation, not a positive terminal realization of relation operators.

## 6. Additional exact module-size checks

The checker computes the left-projective multiplicities of I from the full typed family. Multiplication by different first marked arrows has disjoint path support, so at vertex x the number of left-projective generators is

`dim(e_x I) - sum_(unmarked edges x->y) 2 dim(e_y I)`.

For I these multiplicities are:

- root: 110;
- each of the four one-event vertices: 16;
- each of the six two-event vertices: 2;
- later vertices: zero.

They total 186. For the right-terminal summand I e_t the corresponding numbers are 58,10,2, totaling 110. Source and quotient projective dimensions reconstruct respectively dim I=458 and dim C_rel=434, with the 24-product layer removed.

If each X_x has the common finite memory dimension D_N, the derived image of the full C_rel has dimensions

`H^0:186 D_N`, `H^(-1):24 D_N`.

For C_rel e_t the degree-zero dimension is 110 D_N, with the same shifted product term. These are not the root-corner vector dimensions 210 and 24; the receiver acts on projective source objects, not by copying a corner vector space.

In the two-feature N=4 fixture, D_N=31. The shifted module dimension is therefore 744. Those are fixture dimensions, not dimensions of the actual full spectral feature space.

## 7. Opposite and dual variance

The right-module calculation is the reflected statement:

`C_rel tensor_S^L B = C_rel direct-sum P_rel[1]`.

It must use the corresponding right projective resolution. Opposite reversal exchanges the two local product factors and preserves their middle-vertex label, as in the source attachment theorem.

Cochain contragredient duality reverses the shifted projection into the corresponding inclusion. A term in degree -1 moves to degree +1 under duality. It does not turn a relation coefficient into an inverse event or prefix creation into scalar Green contraction.

These are one-sided derived calculations. They are not a claim of a faithful source-bimodule splitting or a substitute for a separately specified two-sided derived comparison.

## 8. Relation to the new seam derivative

Grothendieck's relation-to-seam note constructs D with

`D(ab)=r(a)D(b)+D(a)r(b)`.

For a,b in I this gives D(ab)=0. Hence its single-seam bridge factors through C_rel and kills P_rel. The labelled external two-seam map detects P_rel in a different target and cohomological degree.

There is no conflict with the present result:

| Operation | Product-layer behavior |
|---|---|
| Ordinary terminal operator | zero |
| First path derivative into a single seam | zero |
| Labelled joint two-seam observation | injective on the 24-product layer |
| One-sided derived quotient of C_rel | P_rel survives in degree -1 |
| Actual finite derived Clark receiver of C_rel | X_s tensor P_rel survives in degree -1 |

The nonzero connecting projection calculated here is the datum a further seam realization must match. The direct sum of the single-seam and joint-seam homology images is not already that comparison. Their shifts, outer source actions, and the image of delta must be specified before identifying the constructions.

## 9. Verification

`uv run --with sympy python research/nima/checkers/check_derived_quotient_relation_attachment.py`

Fresh exact checks:

- all 81 typed source blocks, including the four-event rank 150;
- all 24 independent actual relation products and their terminal vanishing;
- root-to-terminal support and the local source-linear splitting hostiles;
- projective multiplicities and global/corner dimensions;
- the zero-differential connecting projection and its homotopy obstruction;
- annihilation of every product relation by the finite terminal operator fixture.

Artifact: `results/derived-quotient-relation-attachment.json`.

The upstream root-corner certificate is cross-checked and its hash retained; it is not overwritten. The new rank calculation uses exact rational sparse elimination.

Hereditary projectivity, change of rings, and the actual spectral receiver factorization are mathematical proofs above, not conclusions inferred from the finite matrices. No Agda verification of these derived module categories is claimed.
