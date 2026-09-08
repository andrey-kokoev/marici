# Branch-selected excess: primitive endpoint residues and the actual derived Q obstruction

Date: 2026-09-07  
Repository input: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and exact scope

The next calculation uses the actual repeated-normal source, not another internal normal multiple of a target state.

There are two positive constructions and one decisive negative result. The branch Koszul complex has an explicit residue map into the actual endpoint Čech stalk. Applying the existing complementary-normal trace gives nonzero primitive derived endpoint classes in both source excess channels. Their generic counterparts, however, have primitive nonzero short-support transgressions. In the Tor-one channel the full derived Hom complex into the endpoint quotient is acyclic, while its generic quotient has one nonzero class. Thus no direct R-linear derived lift of that generic class exists in the specified coefficient frame. This includes all replacement cochains and homotopies, not just a failed strict representative.

This does not falsify an extraordinary/logarithmic correspondence. It rules out substituting an ordinary covariant R-linear map into the Borel–Moore coefficient target for that correspondence. The full normalization–conductor diagram, its supported-dual variance, physical normal-line comparison, and two coupled geometric endpoint connector cells are not constructed here. No physical reflection parity is assigned.

The endpoint residues below are **normal-coefficient derived maps**, not the already sought geometric endpoint connector 2-cells. The names Tor-zero and Tor-one refer to the two summands of the source excess complex, with their actual homological and normal degrees retained.

## 1. Fix the source and the target

Let R be the polynomial ring over the integers in the nine independent occurrence variables and nine independent normal variables. The short normal u-i belongs to the short diagonal x-i, while the three long normals belong to D03, D14 and D25. These are not branch-function coordinates, external Cartier parameters, or the independently framed physical normal.

The plus-branch/D03 source supplied by the repository is

\[
D=K_R(u_1,u_3,u_5)\otimes_R K_R(u_0,u_3).
\]

In words: use the 32-generator tensor Koszul complex of the two actual, nonnested normal ideals. Its homological degrees are zero through five. Each Koszul generator for u-i has normal degree e-i as well as homological degree one.

Write the ordered generators as

\[
(h_1^+,h_3^+,h_5^+,h_0^{03},h_3^{03}),\qquad
\eta=h_3^+-h_3^{03},\qquad
J=(u_0,u_1,u_3,u_5).
\]

In words: eta is the difference of the two copies of the shared normal. Its differential vanishes, but its normal degree is still e-3.

Keeping the plus-branch generators and replacing the last generator by eta gives an integral unimodular change of basis. It yields

\[
D\cong K_R(u_1,u_3,u_5,u_0)\otimes\Lambda_R(\eta),\qquad
H_0(D)=R/J,\qquad H_1(D)=(R/J)\eta.
\]

In words: both excess channels are retained, and the second has an independent degree-one generator. This is an analysis of the existing source, not a new shifted cell adjoined to the target. The displayed splitting uses the selected branch. Its transport to the other five branch/pair charts keeps the ordered frames rather than averaging them.

The target is the same 215-generator complex as before. A generator is a pair (S,H), with S a compatible set of diagonals and H a subset of S. Its coefficient module and homological degree are

\[
R[u_a^{-1}:a\in S\setminus H]\,[S,H],\qquad
\deg_{
m hom}[S,H]=3-|S|+|H|.
\]

In words: inverses are legal only on the unmarked normals occurring in that particular face. Radial coefficients are the signed X-a/u-a and normal-removal coefficients are signed localization inclusions equal to one. All 215 generators and all coefficient domains are retained before taking a homogeneous component.

Use the established support notation

\[
V=F_V,\quad B=F_B,\quad K=F_K,\quad E=K/V,\quad W=B/V,\quad Q=K/B.
\]

In words: V contains both endpoint complexes, B the whole short boundary, K the whole target, E the endpoint quotient, and Q the generic quotient.

The previous relative calculation gives the target-side deformation complex B shifted by one. Applying derived Hom from D is therefore the appropriate coefficient test of that relative problem. Unlike a scalar readout, it retains the complete source differential and every target endpoint and support term.

## 2. Two gradings, neither of which may be suppressed

Put

\[
U=u_{D03}u_{D14}u_{D25},\qquad \gamma=\deg U.
\]

In words: gamma is the previously computed three-long-normal degree. It admits the four-term generic top cycle without globally localizing any module.

The forced target generator degree is

\[
\deg_{
m fine}[S,H]= -\sum_{a\in S}e_{X_a}+\sum_{a\in S}e_{u_a}.
\]

In words: this grading makes every actual target differential homogeneous. It does not depend on H, although legality of a coefficient does depend on H.

For a source wedge with mask A and a target generator (S,H), a homogeneous map of fine degree lambda has its unique possible coefficient monomial of exponent

\[
\lambda+\sum_{i\in A}e_{u_i}+\sum_{a\in S}(e_{X_a}-e_{u_a}).
\]

In words: add the source wedge degree and subtract the target generator degree. The pair contributes one integer basis element to the mapping complex precisely when this monomial is legal in the target stalk. Its coefficient can be any integer. This describes every homogeneous polynomial map, not a bounded-degree sample.

The mapping complex is formed in homological notation by

\[
\operatorname{Hom}_n(D,T)=\prod_p\operatorname{Hom}_R(D_p,T_{p+n}),\qquad
\partial f=d_Tf-(-1)^nf d_D.
\]

In words: degree n maps shift chain degree by n, and their differential measures failure to commute with the two chain differentials. Since D is bounded and free, this computes derived Hom without an additional source resolution.

For readable cohomology statements below, define

\[
\operatorname{Ext}^j_R(D,T)_\lambda
=H_{-j}\bigl(\operatorname{Hom}_*(D,T)_\lambda\bigr).
\]

In words: Ext-degree j here refers to derived maps between the full complexes; it is not merely an Ext group between their degree-zero homology modules.

A negative value of lambda is a normal-line frame shift. It does **not** authorize an inverse in a marked target stalk or invert a source coefficient.

## 3. Construct the primitive endpoint residue

Let

\[
X_+=X_{x_1}X_{x_3}X_{x_5},\qquad v_+=\{x_1,x_3,x_5\}.
\]

In words: keep the actual occurrence factor and the labelled plus endpoint.

For a wedge H of the ordered plus normals, define

\[
\kappa_+(e_H)=
\varepsilon(H)\frac{UX_+}{\prod_{i\in\{1,3,5\}\setminus H}u_i}\,[v_+,H].
\]

In words: place the inverse of a normal only on the corresponding unmarked endpoint state. The sign epsilon converts the branch wedge order to the target's lexicographic normal order. Every one of these eight coefficient monomials is legal.

The target normal differential removes a mark with coefficient one. The source Koszul differential removes it with coefficient u-i. The extra target inverse cancels that factor term by term, giving

\[
d_V\kappa_+=\kappa_+d_{K(u_1,u_3,u_5)}.
\]

In words: this is an actual chain map on all eight Boolean normal states, not a homology-level choice of a residue.

Its bottom class is

\[
\kappa_+(1)=\frac{UX_+}{u_1u_3u_5}[v_+,\varnothing].
\]

In words: it is the old nonzero primitive endpoint class, represented in the legal Čech localization. It has not been multiplied into a boundary. The annihilator of its homology class is the plus ideal, since a Laurent monomial survives in the endpoint quotient exactly when all three branch normal exponents are negative.

Set c equal to the complementary generator h-zero. In the branch-selected source basis define two cochains, zero on all other wedges:

\[
F_0(e_H\wedge c)=(-1)^{|H|}\kappa_+(e_H),\qquad
F_1(e_H\wedge c\wedge\eta)=\kappa_+(e_H).
\]

In words: the complementary normal supplies the existing Koszul dual trace; the second cochain also retains the independent excess factor. Their signs account for their different cohomological degrees.

Direct calculation gives

\[
\partial F_0=0,\quad\partial F_1=0,
\]

\[
[F_0]\in\operatorname{Ext}^1_R(D,V)_{\gamma-e_0}\cong\mathbb Z,
\qquad
[F_1]\in\operatorname{Ext}^2_R(D,V)_{\gamma-e_0-e_3}\cong\mathbb Z.
\]

In words: each excess channel has a primitive nonzero derived endpoint class. Both maps are converted back to the original repeated-normal source basis and checked there. This does not identify a degree-one source homology class with a degree-zero endpoint without a shift: the displayed Ext and fine degrees are essential.

Relabelling produces the corresponding normal-coefficient maps on the other five branch/pair charts, including the minus endpoint. All six transported mapping differentials and coefficient frames commute exactly. Reflection exchanges the branches; it is not declared to fix one branch chart.

## 4. The generic excess classes and the necessary determinant shift

The actual generic marked-normal cycle is

\[
\omega=UT-\sum_{i=0}^2 X_{D_i}\frac{U}{u_{D_i}}M_i,
\qquad d_Q\omega=0.
\]

In words: all three marked-long terms cancel the chamber boundary, using polynomial coefficients in their marked stalks. This is the previously established generic class, not a detached top-coordinate detector.

In the selected source frame put

\[
\zeta_0=h_1^+\wedge h_3^+\wedge h_5^+\wedge c,
\qquad\zeta_1=\zeta_0\wedge\eta.
\]

In words: these are the top wedges of the regular four-normal part and its excess suspension.

Define G-zero and G-one by sending their respective zeta to omega and all other source wedges to zero. Then

\[
\partial G_0=\partial G_1=0,
\]

\[
[G_0]\in\operatorname{Ext}^1_R(D,Q)_{\lambda_0}\cong\mathbb Z,
\qquad
[G_1]\in\operatorname{Ext}^2_R(D,Q)_{\lambda_1}\cong\mathbb Z,
\]

where

\[
\lambda_0=\gamma-e_0-e_1-e_3-e_5,
\qquad\lambda_1=\lambda_0-e_3.
\]

In words: the excess channel needs the additional dual frame of its repeated normal. Neither map uses a forbidden inverse.

The generic and endpoint frames differ by the same amount in both channels:

\[
\lambda_0-(\gamma-e_0)=
\lambda_1-(\gamma-e_0-e_3)=-(e_1+e_3+e_5).
\]

In words: a comparison between them must account for the **dual determinant of the three branch normals**. This is exactly the normal-degree data lost by treating the external excess class as an internal product of target normals. Merely tensoring a named line does not construct the missing support comparison; the equation specifies the frame that such a comparison must actually carry.

## 5. Compute the actual obstruction, including every replacement homotopy

Lift each G cochain from Q to E using its same four target terms. It is not closed there. Its differential is supported in B and gives the cochain

\[
\beta=d_K\widetilde\omega,\qquad
(\partial\widetilde G_1)(\zeta_1)=\beta.
\]

In words: the entire 18-term short-support boundary of the actual generic cycle is the obstruction. Its source argument is the full excess top wedge. The endpoint projection has not been used to declare the boundary zero.

At the excess frame lambda-one the exact calculation is

\[
\operatorname{Ext}^j_R(D,V)_{\lambda_1}=0,
\qquad
\operatorname{Ext}^j_R(D,E)_{\lambda_1}=0,
\qquad
\operatorname{Ext}^j_R(D,K)_{\lambda_1}=0
\quad(j\in\mathbb Z),
\]

\[
\operatorname{Ext}^2_R(D,Q)_{\lambda_1}\cong\mathbb Z,
\qquad
\operatorname{Ext}^3_R(D,B)_{\lambda_1}\cong\mathbb Z.
\]

In words: the generic source class exists, but the complete source-to-endpoint-quotient mapping complex is acyclic. The short-support mapping complex has exactly the obstruction group required by the long exact sequence.

The connecting map from the triangle B to K to Q is

\[
\operatorname{Ext}^2_R(D,Q)_{\lambda_1}
\xrightarrow{\ \partial\ }
\operatorname{Ext}^3_R(D,B)_{\lambda_1},
\qquad [G_1]\longmapsto[\beta],
\]

and is an integral isomorphism. In words: the obstruction is primitive, not twice or three times a smaller class. Because the endpoint Hom complex is acyclic in this frame, the same obstruction decides lifting into E, not only into K.

The complete source Hom complexes have respectively 18 generators for V, 202 for E, 7 for Q, 213 for B, and 220 for K. These are mapping-complex generator counts, not new target cells. Full signed-unit deformation retractions were constructed and checked on all of them.

It follows that no nonzero integer multiple of G-one lifts, even up to derived homotopy. The homotopy fibre of the corresponding derived mapping-space map over that class is empty. A nonhomogeneous polynomial cochain cannot help: the differential preserves fine degree, so its lambda-one component would solve the same impossible lifting equation.

This is not an order-two or order-three group-cohomology defect. It has infinite additive order and remains nonzero rationally. Equivariance cannot repair a lifting problem that already fails after forgetting the group action.

### Ordinary-channel control

At lambda-zero the source-to-E mapping complex has one Ext-degree-two class, but no Ext-degree-one class. The generic mapping complex has one Ext-degree-one class and the short-support mapping complex has two Ext-degree-two classes. The connecting image of G-zero is a primitive vector in that rank-two group. Therefore the ordinary generic channel also has no lift with its prescribed nonzero generic class.

### Multiplication is not a remedy preserving the prescribed class

Each source normal acts nullhomotopically on the Koszul source. Precomposing by its wedge homotopy gives

\[
u_iG_j=\partial H_{i,j},\qquad u_i\beta_j=\partial L_{i,j},\qquad i\in\{0,1,3,5\}.
\]

In words: multiplying into the source ideal kills the generic class as well as its obstruction. The checker supplies these homotopies with legal stalk coefficients. This operation changes the prescribed nonzero generic datum to zero; it does not construct a lift of that datum.

## 6. A complete 24-frame calculation and an independent small model

The exact finite Hom calculations cover all short-normal map degrees that can have nonzero cohomology when the following are fixed: occurrence map degree zero, all three long-normal degrees one, and the two short normals outside J at degree zero. The three nonrepeated normals have degrees zero or minus one, and the repeated normal has degree zero, minus one, or minus two. Thus there are 24 potentially nonzero frames.

Here is an independent reduction explaining both this bound and every homology group.

For the regular four-normal source K(J), at a fixed target face S a selected normal behaves in one of two ways. When its label lies in S, its endpoint Čech normal factor contributes one primitive Koszul-Hom class only at map degree zero. When its label is absent from S, its polynomial coefficient factor contributes one Koszul-Hom class only at map degree minus one. All other degrees contract. Every long normal has positive map degree, so faces containing a long normal contract in this reduction.

For a four-normal frame let A be the selected labels of degree minus one. The remaining target faces are precisely the short faces satisfying

\[
S\cap\{x_0,x_1,x_3,x_5\}
=\{x_0,x_1,x_3,x_5\}\setminus A.
\]

In words: selected zero-degree labels must be present; selected negative-degree labels must be absent. The other two short labels may occur when noncrossing permits them. Each surviving face has mapping-chain degree three minus its size minus the size of A. The residual differential only adds an unselected short label, with the actual incidence sign.

This reduction respects the endpoint, boundary and generic support predicates. A discarded radial path cannot return to the same selected-label condition by adding more diagonals. Higher radial transfers also have the wrong degree between surviving faces. Consequently no hidden higher differential has been inferred away.

For the full source D, add the regular answer in frame lambda to the regular answer in frame lambda plus e-three, shifted down one homological degree. This is the branch-selected unimodular excess decomposition, still checked against the original source matrices. It gives every entry below.

The checker reconstructs and reduces all 120 full Hom complexes, one for each frame and each of V, E, Q, B and K. Each result agrees with this independent face calculation. Every nonzero elementary reduction coefficient is a signed unit, so the results include integral torsion, not just ranks over a field. No integer torsion occurs. An independent SymPy Smith decomposition of every differential in the five critical Tor-one mapping complexes agrees with the integral retractions.

The table uses E^j for Ext-degree j, with a superscript rank after a colon. A dash means zero cohomology in every degree. Rows list the four source-normal degrees relative to the fixed gamma.

| (u0,u1,u3,u5) | V | E | Q | B | K |
|---|---|---|---|---|---|
| (0, 0, 0, 0) | — | — | — | — | — |
| (0, 0, -1, 0) | — | — | — | — | — |
| (0, 0, -2, 0) | — | — | — | — | — |
| (0, 0, 0, -1) | — | — | — | — | — |
| (0, 0, -1, -1) | — | — | — | — | — |
| (0, 0, -2, -1) | — | — | — | — | — |
| (0, -1, 0, 0) | — | — | — | — | — |
| (0, -1, -1, 0) | — | — | — | — | — |
| (0, -1, -2, 0) | — | — | — | — | — |
| (0, -1, 0, -1) | — | E^1: 1 | — | E^1: 1 | E^1: 1 |
| (0, -1, -1, -1) | E^3: 1 | E^2: 2 | — | E^2: 1 | E^2: 1 |
| (0, -1, -2, -1) | E^4: 1 | E^3: 1 | — | — | — |
| (-1, 0, 0, 0) | E^1: 1 | — | — | E^1: 1 | E^1: 1 |
| (-1, 0, -1, 0) | E^2: 1 | E^1: 1 | — | E^1: 1, E^2: 1 | E^1: 1, E^2: 1 |
| (-1, 0, -2, 0) | — | E^2: 1 | — | E^2: 1 | E^2: 1 |
| (-1, 0, 0, -1) | — | E^1: 1 | — | E^1: 1 | E^1: 1 |
| (-1, 0, -1, -1) | — | E^2: 1 | — | E^2: 1 | E^2: 1 |
| (-1, 0, -2, -1) | — | — | — | — | — |
| (-1, -1, 0, 0) | — | E^1: 1 | — | E^1: 1 | E^1: 1 |
| (-1, -1, -1, 0) | — | E^2: 1 | — | E^2: 1 | E^2: 1 |
| (-1, -1, -2, 0) | — | — | — | — | — |
| (-1, -1, 0, -1) | — | E^1: 1 | — | E^1: 1 | E^1: 1 |
| (-1, -1, -1, -1) | — | E^2: 1 | E^1: 1 | E^2: 2 | E^2: 1 |
| (-1, -1, -2, -1) | — | — | E^2: 1 | E^3: 1 | — |

## 7. What has changed in the research problem

The calculation no longer substitutes a freely chosen target normal multiple for the external excess generator. The actual repeated-normal source has been inserted into the actual target restriction. Its two endpoint residue classes and both generic classes are explicitly specified, including their independent source degrees, coefficient domains and transported branch frames.

Three facts must now be preserved by a genuine physical construction:

1. The primitive endpoint uses a Koszul-to-Čech residue, not multiplication by branch normals into an endpoint boundary.
2. The generic and endpoint components carry different branch determinant frames, in addition to the independent excess suspension.
3. The direct covariant R-linear generic lift has the displayed primitive nonzero short-support obstruction. It cannot be repaired by another homotopy inside that same derived Hom complex.

The next constructive problem is therefore the support-directed logarithmic/duality comparison acting on these explicit classes. Its target and variance must be derived from the normalization–conductor square. It must explain why its image is not the forbidden direct covariant lift. Choosing a parity, inserting a formal filler for beta, or claiming the supported-dual comparison from a matching scalar signature would not do this.

No conclusion is made about other logarithmic targets, other long-normal profiles, arbitrary physical period evaluations, or a fully assembled source infinity-groupoid. The obstruction is a theorem of the explicitly specified polynomial coefficient problem, not a no-go theorem for Marici.

## 8. Reproduction and provenance

Run:

```sh
python check_marici_branch_excess_endpoint_q_obstruction.py \
  --output marici_branch_excess_endpoint_q_obstruction_certificate.json
```

The self-contained checker uses Python 3.10+ and only the standard library. It performs **1,092,368 exact assertions**. Critical reductions retain projection, inclusion and chain-homotopy matrices and verify their full deformation-retraction identities. The 24-frame table is independently checked by the surviving-face calculation; six source transports are checked on all relevant Hom generators and actual coefficient monomials. The generic obstruction has primitive integral coordinates, not merely a numerically nonzero representative.

The checker does not use proof-assistant verification. Assertion counts are not a substitute for the algebraic proofs above. No repository file was changed.

Pinned repository source paths and blob hashes:

- `research/voevodsky/check_d03_plus_excess_beck_chevalley.rs`: `df8448271089910a90c8e641af5b8ae95f1472dd`. Actual source ideals, repeated normal, excess generator and ordered orientations.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`: `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`. Actual target stalk domains, differential and support filtration.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`: `0147e2e42dafac0da7289c571cb0331b51338be1`. Endpoint labels and transported physical carrier orientation.

Preceding calculation: `marici_endpoint_normal_cube_relative_fibre.md`. Its distinction between internal normal continuation and independent external Tor data remains in force.

General mathematical conventions, checked against the Stacks Project:

- *The Koszul complex*, tag `0621`: the exterior differential and functoriality of a change of generator frame.
- *Hom complexes*, tag `0A8H`: the Hom differential, shifts and derived mapping interpretation with a bounded free source.
- *Local cohomology*, tag `0952`: supported Čech coefficients and the distinction between their target localizations and global localization.

The particular endpoint maps, 24-frame table and nonlifting calculation are derived here; they are not attributed to those general references.
