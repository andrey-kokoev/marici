# Branch-supported purity, the dual transgression, and the Rees excess test

Date: 2026-09-07  
Project: Marici  
Source repository: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Results and exact scope

The previous calculation supplied two primitive endpoint residue classes and two generic classes from the actual repeated-normal Koszul source. Their ordinary covariant gluing failed by a primitive short-support transgression. This note computes three operations on that problem rather than replacing it by another unspecified comparison.

**Regular branch-supported purity is constructed on the complete coefficient diagram.** It retains the branch dual determinant, the excess normal, the endpoint complexes and all generic states. Under this operation the eighteen-term generic obstruction becomes a primitive nine-term obstruction. The ordinary lifting problem remains obstructed: purity here is an adjoint description of the same derived mapping complex.

**The finite homogeneous dual reverses the computed support triangle.** Its reverse connecting map sends an explicit one-row short-support functional to an explicit one-row generic functional. Both pairings with the original classes equal one. This is a calculation in the integral graded dual of a finite mapping complex. It is not identified with the ringed supported Verdier dual of the full localization diagram.

**The product-Rees branch selector preserves the actual excess generator.** Its canonical complementary-minor return map does not: the return multiplies that generator by the product of the three Rees parameters, although its coefficient on the full top wedge is one. On the central Rees face the excess class survives on the selected source but its return is zero. This rules out that return as a primitive-excess-preserving replacement for the missing physical comparison; it does not rule out a different logarithmic or bivariant construction.

No physical reflection parity, complete normalization-sheet butterfly, or identification of these operations with a full six-functor correspondence is asserted.

## 2. Source, coefficients, support and grading

Let the nine diagonals of the labelled hexagon be the six short labels `x0,...,x5` and the three long labels `D03,D14,D25`. A short label `xi` means the diagonal joining vertices i and i+2 modulo six; it is not itself a scalar parameter in this notation. Let

\[
R=\mathbb Z[X_d,u_d:d\in\mathcal D].
\]

In words: every diagonal has an independent occurrence variable and an independent normal variable. In formulas below, `X_i` and `u_i` abbreviate the variables of the short label `xi`. The occurrence variables are not identified with normals, external Cartier parameters or physical channel coordinates.

The source supplied by the plus-branch/opposite-pair intersection is

\[
D=K_R(u_1,u_3,u_5)\otimes_R K_R(u_0,u_3).
\]

In words: retain both Koszul complexes and both copies of the shared normal. Their ordered degree-one basis is

\[
(h_1^+,h_3^+,h_5^+,h_0^{03},h_3^{03}),\qquad
\eta=h_3^+-h_3^{03},\qquad d\eta=0.
\]

In words: the excess generator is the difference of the two copies. Replacing the last generator by this difference is an integral unimodular change of exterior basis. It gives a regular four-normal factor and an independent exterior excess factor. The excess has homological degree one and normal degree `e3`; neither degree is forgotten.

The target has all 215 states `[F,H]`, where F is a noncrossing face and H is a subset of F. Its coefficient at this state, homological degree and fine generator degree are

\[
R_F^H=R[u_a^{-1}:a\in F\setminus H],\qquad
|[F,H]|=3-|F|+|H|,
\]

\[
\deg[F,H]=-\sum_{a\in F}e_{X_a}+\sum_{a\in F}e_{u_a}.
\]

In words: only unmarked normals in the face may be inverted. The degree compensates the radial coefficient `X_a/u_a`. A marked-normal inclusion with coefficient one is a localization map, not an invertible map between identical modules.

The differential adds an allowed diagonal with its lexicographic incidence sign and coefficient `X_a/u_a`, or removes a mark with sign `(-1)^(3-|F|+position)` and coefficient one. This is exactly the pinned target convention. All support calculations retain this differential.

Write K for the full target, B for the subcomplex with at least one short label, and V for the sixteen states over the two endpoint faces. Set

\[
E=K/V,\qquad Q=K/B.
\]

In words: E is the endpoint quotient and Q is the generic quotient. The latter contains the chamber, three unmarked long facets and three marked long states. The support inclusions are strict subcomplex inclusions, not replacements by homology lines.

The code uses homological mapping degree n for maps from source degree i to target degree i+n. The Hom differential lowers n by one. Thus Ext degree j is mapping homology degree minus j. Mathematical statements about the mapping complexes below use cohomological grading, consistently with [M1].

## 3. Construct regular branch-supported purity

Put

\[
I_+=(u_1,u_3,u_5),\qquad S_+=R/I_+,
\qquad i_+:\operatorname{Spec}S_+\hookrightarrow\operatorname{Spec}R,
\]

\[
L_+=\det(I_+/I_+^2).
\]

In words: the plus normal branch is a regular codimension-three closed immersion. Its determinant is ordered by the displayed three normal parameters. This is the independent-normal coefficient branch; it is not yet selection of a scalar branch in the reducible equations `u_i=t_i x_i`.

For any of the six target complexes T equal to K, B, V, E, Q or B/V, regular-immersion purity gives

\[
i_*i^!T=\operatorname{RHom}_R(S_+,T)
\simeq i_*\left((T\otimes_R^L S_+)\otimes_{S_+}L_+^\vee[-3]\right).
\]

In words: the supported object is derived restriction together with the dual branch determinant and a cohomological shift by three. The determinant line lives on its support. It is not naively inserted into the unspecialized source by an additional non-flat tensor operation. In the displayed parameter frame a free determinant lift may be used to write matrices, followed by restriction to the support.

Here is a direct proof suited to the actual modules. Resolve S+ by the ordered branch Koszul complex. Its dual has only the top cohomology S+ with the dual determinant in degree three. Tensor this dual resolution with T. Each term of T is a localization of R and hence flat; T is bounded. Tensoring preserves the quasi-isomorphism. The resulting projection selects the top dual branch component and reduces its coefficients modulo the branch ideal. This proves the complete all-polynomial statement, not only its values on the two chosen classes. It is the three-variable version of the one-divisor calculation [M2], with the exterior signs of [M3].

### Which target summands meet the support?

If `F minus H` contains a plus-branch label, that target summand inverts a function vanishing on the support. Its tensor product with S+ is zero. Otherwise it survives with the other allowed localizations unchanged. Thus

\[
R_F^H\otimes_R S_+=0
\quad\Longleftrightarrow\quad
(F\setminus H)\cap\{x_1,x_3,x_5\}\ne\varnothing.
\]

In words: a stalk disappears precisely when its open localization is disjoint from the chosen closed branch. This is an exact base-change statement, not a new pole rule.

The surviving summand counts are:

| Complex | K | B | V | E | Q | B/V |
|---|---:|---:|---:|---:|---:|---:|
| Summands after branch base change | 136 | 129 | 9 | 127 | 7 | 120 |

The plus endpoint contributes its fully marked state; the minus endpoint contributes all eight of its states. Every generic state survives. The restricted endpoint connecting maps and the generic connecting map are still the actual blocks of the target differential.

### Retain the excess and construct the map on full Hom complexes

Tensor-Hom adjunction gives

\[
\operatorname{RHom}_R(D,T)\simeq
\operatorname{RHom}_{S_+}\left(
K_{S_+}(u_0,0),\,
(T\otimes_R^L S_+)\otimes L_+^\vee[-3]\right).
\]

In words: resolve the plus branch by supported purity, while keeping the opposite pair. Its shared generator now has zero differential, not zero value. The original excess maps under branch augmentation to the negative of this retained pair generator. Its coefficient is primitive.

Let b be the ordered branch top wedge, let c be a wedge in the residual pair, and let f have homological Hom degree n. In the explicit conventions of the checker the comparison is

\[
(\Pi f)(c)=(-1)^{n+3}\overline{f(b\otimes c)}.
\]

In words: select the full branch wedge, restrict only its allowed coefficient, and include the sign required by the odd shift. Equivalently the sign is `(-1)^(q+|c|)` when the output target state has degree q. The formula kills all other branch-wedge components. Direct substitution in the Hom differential proves it is a chain map. Tensor-Hom adjunction and the regular Koszul proof establish that it is a quasi-isomorphism.

The checker verifies this map and its entire comparison cone in 24 normal frames for all six support complexes: 144 cones in total. Each cone cancels integrally through signed-unit pivots. It also verifies the off-diagonal E-to-V, Q-to-B and B/V-to-V connecting blocks before contraction. All six transported branch/pair charts satisfy the corresponding chain equations. Reflection transports one labelled branch to the other; it is not asserted to be an automorphism of the fixed plus branch.

## 4. Images of the endpoint and generic classes

Let

\[
U=u_{D03}u_{D14}u_{D25},\qquad
\gamma=\deg U,\qquad X_+=X_1X_3X_5.
\]

In words: U involves the three long normals only; X+ involves the three plus-endpoint occurrences only.

The earlier endpoint maps have degrees `gamma-e0` and `gamma-e0-e3`. Under the complete purity comparison their only nonzero residual-pair components are

\[
(\Pi F_0)(h_0^{03})=UX_+[v_+,v_+],
\]

\[
(\Pi F_1)(h_0^{03}\wedge h_3^{03})=-UX_+[v_+,v_+].
\]

In words: both endpoint residue classes survive primitively on the fully marked endpoint, with the stated determinant line and shift. The minus sign in the excess channel is forced by the original excess basis and the ordered target marks, not chosen to fit an answer. Their mapping cohomology groups remain rank-one in Ext degrees one and two, respectively.

This is not the same as setting branch normals to zero in the earlier bottom pole representative. That bottom representative belongs to a localization disjoint from the branch and its ordinary base change is zero. The nonzero image above comes from the complete Koszul-to-Cech residue map, including all of its higher components.

The generic cycle is

\[
\omega=UT-\sum_{D\in\{D03,D14,D25\}}
X_D\frac{U}{u_D}M_D.
\]

In words: the legal marked-long terms cancel the chamber's three generic boundaries. Every coefficient U/uD is a polynomial in the other long normals.

Define

\[
\lambda_0=\gamma-e_0-e_1-e_3-e_5,
\qquad \lambda_1=\lambda_0-e_3.
\]

In words: these are the ordinary and excess generic frames, including the repeated normal twice in the excess frame. The purity images of the original generic maps satisfy

\[
(\Pi G_0)(h_0^{03})=\omega,\qquad
(\Pi G_1)(h_0^{03}\wedge h_3^{03})=\omega.
\]

In words: both prescribed generic classes survive with positive unit coefficient in their own frames. The difference between endpoint and generic frames remains the negative branch determinant degree. Purity accounts for that line; it does not identify different coefficient frames by decree.

## 5. The transformed nine-term obstruction

Lift the last generic cochain to the full transformed target and apply the Hom differential. Call its short-support value beta-plus. The original eighteen-term cochain maps exactly to this nine-term cochain. Both channels have the same output terms; only their residual-pair input and Ext degree differ.

On the appropriate pair input its three short-facet terms are

\[
-\sum_{j\in\{0,2,4\}}\frac{UX_j}{u_j}[\{x_j\},\varnothing].
\]

In words: only the three even short labels meet the plus branch with these unmarked coefficients.

Its remaining six terms have coefficient

\[
\varepsilon_{j,D}\frac{X_jX_D}{u_j}\frac{U}{u_D}
[\{x_j,D\},\{D\}].
\]

In words: the short normal is legally inverted on an unmarked state; the quotient U/uD is a polynomial, so the marked long state receives no forbidden inverse. The sign and support list is

| j | D | Sign |
|---:|---|---:|
| 0 | D03 | +1 |
| 0 | D25 | +1 |
| 4 | D03 | -1 |
| 4 | D14 | +1 |
| 2 | D14 | -1 |
| 2 | D25 | +1 |

Let C-T denote the complete transformed cohomological mapping complex in the indicated frame. The calculated groups are:

| Generic channel | C-V | C-E | C-Q | C-B | C-K |
|---|---|---|---|---|---|
| Ordinary, frame lambda-zero | 0 | H2 = Z | H1 = Z | H2 = Z squared | H2 = Z |
| Excess, frame lambda-one | 0 | 0 | H2 = Z | H3 = Z | 0 |

All omitted cohomology is zero and none of these groups has integer torsion. In the excess frame the complete mapping complexes have 2, 42, 7, 37 and 44 generators, respectively. These are counts of homogeneous maps, not new target cells.

In particular,

\[
H^2(C_Q)\xrightarrow[\cong]{\partial}H^3(C_B),
\qquad \partial[G_{1,+}]=[\beta_+].
\]

In words: the primitive generic class still has a primitive nonzero obstruction. Here G-one-plus denotes its purity image. Since C-V and C-K are acyclic in this frame, the same obstruction excludes a lift into the endpoint quotient. No different homogeneous cochain or endpoint comparison homotopy removes it.

### Independent explanation by a four-face complex

The unimodular excess decomposition reduces this frame to the regular four-normal problem with each selected normal degree minus one, shifted by the excess. Normal Koszul-Hom blocks contract unless the selected short labels are absent. Positive long-normal degrees similarly contract faces containing long labels. The only surviving faces are

\[
\varnothing,\quad\{x_2\},\quad\{x_4\},\quad\{x_2,x_4\}.
\]

In words: x2 and x4 are compatible, so these are the empty face, two vertices and their edge. The remaining differential is their actual incidence, up to integral sign choices. The total mapping complex reduces to

\[
\mathbb Z\xrightarrow{(1,1)^T}\mathbb Z^2
\xrightarrow{(-1,1)}\mathbb Z
\]

in cohomological degrees two, three and four. In words: this is the exact augmented cochain complex of an interval. Removing the empty-face term gives the short-support line in degree three; retaining only the empty face gives the generic line in degree two. The connecting class is the primitive diagonal vector. This independently proves the ranks, integrality and nonvanishing above.

In the ordinary frame the same interval occurs one degree earlier, together with one isolated surviving face `x3` in Ext degree two. That extra face is present in B, E and K but absent from Q and V. This explains the first table row. The checker compares the surviving-face calculation with every one of the 144 complete mapping calculations, not just the critical two rows.

The normal contractions are within the fixed homogeneous coefficient frames. They do not authorize global localization or contraction of an arbitrary unframed polynomial diagram.

## 6. The actual reverse dual connecting map

Now dualize the finite homogeneous mapping complexes over the integers:

\[
C_T^\#=\operatorname{RHom}_{\mathbb Z}(C_T,\mathbb Z).
\]

In words: this is the integral graded dual of a finite complex of free abelian groups. It is an exact calculation with the full differential of this slice. It is not being substituted for an unspecified ringed supported Verdier dual of the infinite polynomial/localization object.

The support triangle reverses:

\[
C_Q^\#\longrightarrow C_K^\#\longrightarrow C_B^\#
\longrightarrow C_Q^\#[1].
\]

In words: the contravariant operation reverses the actual support arrows. Its connecting map goes from the dual short-support class to the dual generic class, not in the direction of the ruled-out covariant lift.

Here are literal one-row representatives. In the excess frame, a homogeneous map into the target cell `[{x2,D25},{D25}]` on the residual pair top has the uniquely prescribed monomial coefficient

\[
\frac{X_2X_{D25}u_{D03}u_{D14}}{u_2}.
\]

In words: only u2 is inverted, on an unmarked short-normal state. Define beta-dual to read the integer multiplying this homogeneous basis map. Extend the functional by zero to the full C-K. Its dual boundary is minus the functional reading the pair-top map into the marked `D25` state with coefficient

\[
X_{D25}u_{D03}u_{D14}.
\]

In words: it is the negative marked-long coordinate, with no normal inverse. Call this second functional G-dual. Direct use of the shifted target incidence gives

\[
d_{C_B^\#}\beta^\#=0,\qquad
 d_{C_K^\#}\widetilde\beta^\#=G^\#,
\qquad d_{C_Q^\#}G^\#=0.
\]

In words: the first functional is closed on the short boundary, but its extension to the full target has precisely the required generic boundary. The only relevant incoming row is the actual radial incidence from marked D25 to `{x2,D25}`. No detached norm variable has been introduced.

The pairings are

\[
\langle\beta^\#,\beta_+\rangle=1,
\qquad
\langle G^\#,G_{1,+}\rangle=1.
\]

In words: both functionals evaluate the corresponding primitive classes positively. Consequently

\[
H^{-3}(C_B^\#)\xrightarrow[\cong]{\partial^\#}
H^{-2}(C_Q^\#),\qquad
\partial^\#[\beta^\#]=[G^\#].
\]

In words: dualization turns the previously computed connecting obstruction into a primitive reverse connecting pairing. It does not turn a nonzero class into zero. The checker verifies the complete dual differential, every dual group, both evaluations and all six transported versions of these equations.

This functional is deliberately defined on one finite graded slice. It is not an R-linear map sending an arbitrary polynomial target class to the integer one. Such a scalar trace would require a different domain, coefficient action and support specification. Likewise, identifying this slice dual with a geometric supported dual requires a comparison not proved here.

## 7. Product-Rees branch selection and its adjugate return

The source's multi-Rees normal blocks have differential `t_i x_i`. To test their actual effect on the excess, make this declared coefficient change for the three branch normals, leaving the opposite pair's repeated equation equal to `t3*x3`:

\[
D_u=K(t_1x_1,t_3x_3,t_5x_5,u_0,t_3x_3),
\]

\[
D_x=K(x_1,x_3,x_5,u_0,t_3x_3).
\]

In words: D-x selects the scalar plus branch in the first three equations only. It does not replace the opposite pair by another pair. These are calculations over the polynomial ring in the displayed variables and arbitrary independent flat spectators. The source monodromy units `1+t_i x_i` may also be retained; no t or x is inverted.

The diagonal exterior map F from D-u to D-x multiplies the first three degree-one generators by `t1,t3,t5` and fixes both pair generators. On an ordered wedge indexed by A,

\[
F(e_A)=\left(\prod_{i\in A\cap\{1,3,5\}}t_i\right)e_A.
\]

In words: each included branch generator contributes its own Rees factor. The index set refers to branch-generator positions, not to a second copy in the pair.

Its complementary-minor return G from D-x to D-u is

\[
G(e_A)=\left(\prod_{i\in\{1,3,5\}\setminus A}t_i\right)e_A.
\]

In words: each omitted branch generator contributes its Rees factor. This is the tensor product of the one-normal return with components `(t_i,1)` in homological degrees zero and one. Both maps commute with the complete Koszul differentials, with their ordered exterior signs. They satisfy

\[
GF=FG=(t_1t_3t_5)\operatorname{id}.
\]

In words: they are inverse only on the generic open where the Rees product is a unit, not on the central face.

The two closed primitive excess generators are

\[
\eta_u=h_3^+-h_3^{03},\qquad
\eta_x=t_3h_3^+-h_3^{03}.
\]

In words: the selected source still has an independent repeated-normal direction; its primitive coefficient on the pair copy is minus one. The four remaining normal equations are regular in each source, so the unimodular change of basis proves that these are genuine nonzero excess homology classes over the corresponding quotient rings.

Exact computation gives

\[
F(\eta_u)=\eta_x,
\qquad G(\eta_x)=t_1t_3t_5\eta_u.
\]

In words: branch selection retains the excess primitively, while the adjugate return multiplies it by the entire branch Rees determinant.

At the central Rees face,

\[
\eta_x\big|_{t_1=t_3=t_5=0}=-h_3^{03},\qquad
G(\eta_x)\big|_{t_1=t_3=t_5=0}=0.
\]

In words: the selected excess still survives, but its image under this return vanishes. The source complexes are bounded free over the polynomial ring, so these substitutions compute their derived coefficient change. Nonzero survival follows also directly from the residual regular four-normal factor and its zero-differential pair generator.

At the same time G has coefficient one on the full five-generator top wedge. This proves that a primitive top-volume comparison is insufficient to certify preservation of the required Tor-one class. Checking only the top determinant or the generic trace would miss the failure.

These are canonical maps of the declared source Koszul complexes, not a new physical endpoint/Q map and not a proof that every extraordinary or logarithmic functor must act like G. In particular a conormal-symbol pairing or a logarithmic excess operation cannot be replaced by multiplication of ordinary coefficients without proving that comparison.

## 8. What the construction now requires

The results separate three statements that must not be merged.

Regular branch i-shriek is now an explicit operation on the actual target coefficient diagram. Its adjunction retains both endpoint residue classes and both generic classes, with correct normal determinant degrees. It preserves the nonlifting theorem because it re-expresses the same mapping problem.

The finite graded dual of its support triangle supplies a primitive reverse pairing with a literal support row and a literal generic row. A successful supported-dual construction must specify whether and how its geometric object realizes this reversed relation. Equality of a scalar signature does not provide that comparison.

The scalar-branch selector in the product-Rees source preserves the independent excess. Returning by complementary minors destroys that primitive excess on the central face, despite unit top normalization. A candidate logarithmic comparison must therefore be tested on the excess generator itself, the endpoint comparisons and the generic row, not only on a determinant or a trace value.

The remaining physical task is to construct the source-defined logarithmic/supported-dual map into the actual endpoint/Q diagram, including its two connector homotopies, and identify its action with the required primitive classes in their correct frames. This note provides computed maps and explicit tests for that identification. It does not choose either parity of an unconstructed physical fibre.

## 9. Reproduction, checks and provenance

Run:

```sh
python check_marici_branch_purity_dual_transgression.py \
  --output marici_branch_purity_dual_transgression_certificate.json
```

The checker is self-contained, uses Python 3.10+ and the standard library, and performs **1,646,495 exact assertions** in the recorded run. It verifies complete source and target Hom differentials, all 144 integral purity comparison cones, every support connecting block, critical full deformation retractions, an independent surviving-face cohomology calculation, the explicit endpoint and generic class images, the dual one-row functionals, six-chart covariance, and both product-Rees maps on all 32 source wedges.

The all-polynomial purity theorem follows from the regular Koszul/flat-localization argument, not from extrapolating a finite sample of exponents. The finite homogeneous computations include complete complexes and integer torsion through unit cancellations. This is not proof-assistant verification, nor a reconstruction of an unsupplied geometric six-functor map. No repository write was made.

The certificate exports the class coefficients as exponent vectors in the order `X_x0,...,X_x5,X_D03,X_D14,X_D25,u_x0,...,u_x5,u_D03,u_D14,u_D25`. It also records the full source blob hashes and the SHA-256 of the standalone checker.

Pinned source files:

- `research/voevodsky/check_d03_plus_excess_beck_chevalley.rs`, blob `df8448271089910a90c8e641af5b8ae95f1472dd`: actual source ideals, repeated normal and ordered excess orientation.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: complete target differential and localization domains.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: source-labelled endpoint carrier and transported orientation.
- `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`: product-Rees coefficient blocks and separation of branch support from external normal data.

Preceding proof: `marici_branch_excess_endpoint_q_obstruction.md`. The distinctions between occurrence degrees, independent normals, external Cartier lines, source excess and physical normal orientation remain in force.

Primary mathematical conventions:

[M1] Stacks Project, *Hom complexes*, tag `0A8H`, especially the differential and tensor-Hom adjunction: https://stacks.math.columbia.edu/tag/0A8H

[M2] Stacks Project, *Right adjoint of pushforward for effective Cartier divisors*, Lemma 48.14.1, tag `0B4B`: https://stacks.math.columbia.edu/tag/0B4B

[M3] Stacks Project, *The Koszul complex*, tag `0621`, for the ordered exterior differential and functorial comparison of sequences: https://stacks.math.columbia.edu/tag/0621

The particular purity projections, class images, nine-term transgression, graded-dual rows and product-Rees excess test are derived in this note and checker; they are not claims attributed to those general references.
