# Branch C: relative adjunction comparison and the native operation kernel

Date: 2026-09-08  
Pinned target input: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`  
Task: `Pasted text(3).txt`  
Baseline: `marici_physical_endpoint_pullback.md`

## Result and scope

The line-retaining endpoint upper-shriek counit has a new, explicitly calculated relative comparison. Its precomposition map carries a primitive line-framed endpoint cocycle to the primitive Gysin endpoint cocycle. The cone of that actual adjunction map therefore makes the endpoint cocycle comparable to zero, while its homotopy fibre retains the cocycle as a nonzero primitive class. No Euler evaluation is used, and the class is not made a boundary in the original endpoint complex.

A native normalized-bar calculation constructs an operation-retaining enhancement of this endpoint-facing comparison. The smallest operation-stable submodule containing the primitive class is its entire relative-operation orbit, not a ten-dimensional list consisting of one class and nine quadratics. Through operation weight four its ranks are 1, 9, 18, and 96 in degrees zero, two, three, and four. The 96 degree-four classes include all 81 ordered products of quadratics. They are independent and integrally saturated in each native endpoint module.

For this explicitly defined coefficient/native-bar comparison model, the two-endpoint fibre has H0 of rank two and zero H-minus-one, H-minus-two, and H1. The affine discrepancy of the two prescribed primitive endpoint differences is explicitly a boundary in the comparison object. Selecting their primitive components gives a contractible component of this candidate fibre.

This does not identify the model with the full physical-collar totalization requested in the task. In particular, an ambient coefficient Hom complex tensored with a native conductor-bar cochain module is not silently identified with the Hom complex of their actual source tensor product. The missing mixed bivariant/source-action comparison is stated precisely in Section 10. Physical road-Cech descent, the Branch A conormal readout, and physical reflection parity are not claimed.

## 1. Fixed sources, coefficients, and degrees

Use the baseline ambient ring

\[
A=\mathbb Z[X_0,\ldots,X_5,X_{D03},X_{D14},X_{D25},
 t_0,\ldots,t_5,u_{D03},u_{D14},u_{D25}].
\]

In words: all occurrence coordinates, the six short-Rees parameters, and the three long normal parameters remain distinct. Short normal equations are u_i=t_i X_i. No ambient occurrence inverse or integer denominator is admitted.

The target has 215 states [F,H], with homological degree 3-|F|+|H|. Its stalk is

\[
A[u_a^{-1}:a\in F\setminus H].
\]

In words: only unmarked normal labels may be inverted. After the short Rees substitution, 1/X_i=t_i/u_i is legal inside an unmarked-i stalk; this does not invert X_i on the base. There are 16 endpoint states, 208 short-boundary states, 199 states in E=K/V, and seven in Q=K/B_short.

For a channel T, with |T|=2 or 3 and T contained in {1,3,5}, retain

\[
P_T=K_A(X_0,\ldots,X_5,p_T),\qquad p_T=\prod_{i\in T}t_i,
\]

\[
\lambda_T=\gamma-\sum_{i=0}^5 e_{X_i}-\sum_{i\in T}e_{t_i},
\qquad \gamma=\sum_{\ell\in\{D03,D14,D25\}}e_{u_\ell}.
\]

In words: the complete source has 128 generators and keeps its seventh, product-Cartier generator. The degree records all six occurrence conormals, that product-Cartier line, and the long-normal frame. The two excess-trace labels over each T remain separate labelled lines, although the coefficient source is the same.

We use cohomological Koszul complexes in degrees -n through zero. Internal shift <lambda> raises source internal degrees by lambda. Thus the normalized coefficient source is P_T<lambda_T>[-4]. Hom differential is

\[
\partial f=d_Y f-(-1)^{|f|}f d_X.
\]

In words: ordinary Hom degree and internal degree are separate. This is the standard Hom-complex convention [M1].

For endpoint sigma, let I_+=(1,3,5), I_-=(0,2,4). Set

\[
J_\sigma=(t_i:i\in I_\sigma),\quad
\widetilde L_\sigma=A\ell_\sigma,\quad
|\ell_\sigma|_{\rm int}=\beta_\sigma=\sum_{i\in I_\sigma}e_{t_i}.
\]

The line is the prescribed ambient frame of det(J_sigma/J_sigma^2). It is not the support quotient itself. For the regular closed immersion V(J_sigma) into Spec A, retain

\[
D_\sigma=R\operatorname{Hom}_A(K_A(t_{I_\sigma}),A)
\cong K_A(t_{I_\sigma})\otimes\widetilde L_\sigma^\vee[-3].
\]

In words: the three-normal upper-shriek factor contains its dual determinant and its shift. Its ordered tensor construction is iterated Cartier duality [M2]. The framed Gysin source is

\[
\mathsf P^G_{\sigma,T}
=(P_T\otimes D_\sigma\otimes\widetilde L_\sigma)
\langle\lambda_T\rangle[-4].
\]

Before normalization it has 1,024 free generators in cohomological degrees -7 through 3, supported on V(X_0,...,X_5,p_T,J_sigma). Nothing identifies the redundant product-Cartier equation or its excess with the separately labelled eta.

## 2. Candidate A: the relative line-retaining counit

The adjunction counit, with its line retained, is

\[
c_\sigma^L:P_T\otimes D_\sigma\otimes\widetilde L_\sigma
\longrightarrow P_T\otimes\widetilde L_\sigma.
\]

In words: it is covariant and has degree zero and internal degree zero. It sends the empty dual-normal subset to the same source coefficient and sends nonempty dual-normal subsets to zero. Its variance is the closed-immersion counit j_*j^! -> identity. It preserves every occurrence, product-Cartier, determinant, and excess label. It does not pair ell_sigma with the Euler section.

Define actual homogeneous endpoint mapping complexes

\[
A_\sigma=R\operatorname{Hom}_A
((P_T\otimes\widetilde L_\sigma)\langle\lambda_T\rangle[-4],V_\sigma)_0,
\]

\[
C_\sigma=R\operatorname{Hom}_A(\mathsf P^G_{\sigma,T},V_\sigma)_0,
\qquad a_\sigma=(c_\sigma^L)^*:A_\sigma\longrightarrow C_\sigma.
\]

In words: the map is contravariant in its source through precomposition, but is a degree-zero covariant arrow of mapping complexes. The target V_sigma and its localization domains have not changed. The subscript zero means internal degree zero after the specified source shifts.

The new calculation gives

\[
H^q(A_\sigma)=H^q(C_\sigma)=
\begin{cases}\mathbb Z,&q=0,\\0,&q\ne0,\end{cases}
\qquad \operatorname{Cone}(a_\sigma)\simeq0.
\]

The comparison cone is reduced directly, not inferred to be acyclic from agreement of the two endpoint ranks.

### Explicit primitive preimage

Let I_all=(0,1,2,3,4,5,6), with 6 denoting z_T. For J contained in I_sigma, write e_(I_all minus J) for the ordered remaining source wedge and H_sigma(J) for the endpoint marks whose labels are in I_sigma minus J. Put U_L equal to the product of the three long normals. There is an eight-row cocycle

\[
w_\sigma(e_{I_{\rm all}\setminus J}\otimes\ell_\sigma)
=\epsilon_\sigma(J)\,\frac{U_L}{\prod_{j\in J}X_j}
[v_\sigma,H_\sigma(J)].
\]

In words: removing an endpoint occurrence from the source wedge also unmarks that endpoint coordinate in the target. Its inverse is then legal in exactly that stalk. Every row still contains z_T.

The signs are completely specified as follows. Set epsilon(empty)=1. If j is not in J, let pos_s be its zero-based position in the remaining source order, and pos_h its zero-based position in the lexicographically ordered remaining target marks. Then

\[
\epsilon_\sigma(J\cup\{j\})
=(-1)^{\operatorname{pos}_s(j)+\operatorname{pos}_h(j)}\epsilon_\sigma(J).
\]

This recurrence is path-independent. The two possible removal orders change source and target signs together. It proves the normal/source cancellation term by term.

The checker independently derives w by signed-unit reduction and verifies

\[
\partial w_\sigma=0,\qquad
\nu_\sigma=a_\sigma(w_\sigma),\qquad
\nu_\sigma(e_{I_{\rm all}}\otimes1^\vee\otimes\ell_\sigma)
=U_L[v_\sigma,I_\sigma].
\]

In words: precomposition produces the primitive endpoint Gysin class already identified in the baseline. No incoming differential can change its top fully marked coefficient. That coefficient is an integral detector proving that nu_sigma is not a boundary in C_sigma.

The certificate records every coefficient of w and nu in representative frames. For T={1,3}, the unreduced plus calculation has 55 line-source Hom columns, 285 Gysin-source Hom columns, a 340-column comparison cone, and a 625-column relative fibre. The minus calculation has 43, 253, 296, and 549 respectively.

## 3. Relative comparison and the first obstruction

Use the cone of the actual adjunction-induced map:

\[
Z_\sigma^{\rm adj}=\operatorname{Cone}(a_\sigma),\qquad
\pi_\sigma:C_\sigma\longrightarrow Z_\sigma^{\rm adj},\qquad
J_\sigma^{\rm adj}=\operatorname{fib}(\pi_\sigma).
\]

The cochain formulas are

\[
(Z_\sigma^{\rm adj})^n=C_\sigma^n\oplus A_\sigma^{n+1},\qquad
 d_Z(c,a)=(d_Cc+a_\sigma a,-d_Aa).
\]

In words: the new comparison coordinate is the shifted line-source Hom complex already supplied by the counit. No independent target generator is added to kill a chosen class [M3].

The primitive discrepancy has the explicit comparison homotopy

\[
d_Z(0,w_\sigma)=(\nu_\sigma,0).
\]

In words: nu_sigma becomes comparable to zero in Z, but remains nonzero in C and in the relative fibre. The two original endpoint differences remain (1,1); their images in comparison cohomology are now (0,0).

There is an explicit deformation retraction of the whole fibre. Write its coordinates in degree n as

\[
(c,c',a')\in C^n\oplus C^{n-1}\oplus A^n,
\qquad
D(c,c',a')=(d_Cc,c-d_Cc'-a_\sigma a',d_Aa').
\]

Then projection, section, and homotopy are

\[
p(c,c',a')=a',\quad i(a)=(a_\sigma a,0,a),\quad H(c,c',a')=(c',0,0),
\]

\[
p\circ i=1,\qquad DH+HD=1-i\circ p.
\]

In words: J retracts onto A, with all comparison coordinates retained. This is checked on every constructed fibre column.

### Other requested candidates

**Candidate B.** Inclusion of V_sigma into the actual short boundary sends nu_sigma to a nonzero class. The existing quotient B_short -> B_short/V does send the endpoint cochain to zero, and its mapping fibre retains the original endpoint Hom complex. This is a second valid support-relative mechanism. Its extra lower-degree short-boundary classes are retained in the certificate; it is not substituted for Candidate A's simpler adjunction cone.

**Candidate C.** The native endpoint augmentation sends m_sigma to 1. Its kernel contains positive mixed operations but not m_sigma. Therefore this augmentation alone cannot put the primitive endpoint unit into the required relative kernel. It remains useful as a quotient in a larger diagram.

**Candidate D.** No augmented pyramid is needed for the successful adjunction-cone test. None was manufactured.

## 4. The literal native supported bar source

Let C denote the conductor coefficient ring with all spectator variables retained. The native node is

\[
\mathfrak B=C[X_0,\ldots,X_5]/(X_eX_o:e\in\{0,2,4\},\ o\in\{1,3,5\}).
\]

The requested source is exactly

\[
(P_\sigma^{\rm nat})^{-n}
=\mathfrak B\otimes_C\overline{\mathfrak B}^{\otimes_C n}\otimes_C\mathfrak B_\sigma.
\]

Its differential, on elements of the ungraded polynomial algebra, is

\[
\begin{aligned}
d(b_0|a_1|\cdots|a_n|m)
={}&b_0a_1|a_2|\cdots|a_n|m\\
&+\sum_{i=1}^{n-1}(-1)^i b_0|\cdots|a_ia_{i+1}|\cdots|m\\
&+(-1)^n b_0|a_1|\cdots|a_{n-1}|a_nm.
\end{aligned}
\]

In words: a mixed even-odd monomial product is zero in the native ring; the last product uses the actual branch quotient. Neither operation is replaced by a formal exterior relation.

For finite verification, retain every monomial multidegree of total occurrence weight at most four and every bar length in those weights. This is a subcomplex, not a truncation cutting off a possible boundary of the same internal weight. There are 10,287 literal free-left bar columns for each endpoint. Applying Hom over the native ring to the conductor gives

\[
N_\sigma=\operatorname{Hom}_{\mathfrak B}(P_\sigma^{\rm nat},C).
\]

There are 5,161 cochain columns per endpoint, and 3,441 in the conductor algebra bar cochains. Signed-unit contractions in each multidegree give

| Cohomological degree | Native algebra | Each native endpoint |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 6 | 3 |
| 2 | 24 | 12 |
| 3 | 92 | 46 |
| 4 | 354 | 177 |

These are independently calculated native-bar groups. The cochain differential was not replaced by zero.

The coefficient C can be extended by the spectator Rees and determinant frames. For the finite homogeneous results below the scalar coefficients are integers, while the occurrence and Rees degrees remain separately recorded. Tensoring a labelled excess line retains its label and introduces no identification with another channel.

## 5. Native chain operations and the minimal stable orbit

Degree-one conductor cochains read the six individual occurrence generators. Choose xi indices for occurrences (1,3,5) and eta indices for (0,4,2). Deconcatenation gives their cup action on N_sigma, with

\[
d(f\smile h)=df\smile h+(-1)^{|f|}f\smile dh.
\]

In words: this is an action on the actual native bar cochains, including nonclosed cochains. The checker verifies the equation on every elementary pair of combined occurrence weight at most four.

The quadratic mixed cochains are

\[
r_{ij}=\xi_i\smile\eta_j+\eta_j\smile\xi_i.
\]

All eighteen endpoint images are nonzero and primitive. In contrast, same-sheet exterior relations are actual bar boundaries. For distinct same-sheet i,j, if lambda_(X_i X_j) reads the one-bar monomial X_i X_j, then

\[
d(-\lambda_{X_iX_j})=\lambda_{X_i}\smile\lambda_{X_j}
+\lambda_{X_j}\smile\lambda_{X_i}.
\]

For i=j the corresponding one-bar cochain has boundary lambda_i squared. Mixed monomials are absent in the native ring, so this contraction is unavailable for r_ij. In the regular ambient occurrence ring the mixed monomial exists, which explains why forgetting the native structure can kill the relative operations. This is a change-of-rings issue, not an extra physical cell.

All 49 primitive types are given by explicit nested commutators of the six closed cochains. For nonempty index subsets I,J, start with r_(min I,min J), bracket by the remaining eta generators and then the remaining xi generators in the declared order. Their operation degrees have multiplicities 9,18,15,6,1. Since the relative algebra is free associative on these supplied primitive types, choosing closed cochain representatives defines its action by composition. This does not assert formality of the entire native endpoint complex. Full reductions are performed only through operation weight four; the higher formulas are not passed off as full degree-five/six matrix audits.

The smallest stable submodule containing the endpoint class must include every iterated operation on it. At tested weights its ranks are

\[
(\operatorname{rk}\mathcal R^0,\operatorname{rk}\mathcal R^1,
\operatorname{rk}\mathcal R^2,\operatorname{rk}\mathcal R^3,
\operatorname{rk}\mathcal R^4)=(1,0,9,18,96).
\]

In words: degree four contains 15 new primitive types and 81 ordered products. The checker proves all 124 displayed orbit classes independent and saturated at each endpoint.

The orbit cannot be finite as a coefficient module: for example, the alternating native normal form of (r_00)^n m_+ contains (xi_0 eta_0)^n with unit coefficient for every n. Higher products therefore cannot be removed merely by listing the nine quadratic generators. This is an operation-module assertion, not an identification with a physical state space or moment-angle fibre.

## 6. Minimal endpoint-facing comparison with the native orbit retained

The actual native bar supplies a cochain m_sigma, its conductor augmentation. Free-module adjunction gives the map

\[
\alpha_\sigma:\mathcal R\longrightarrow N_\sigma,
\qquad r\longmapsto r\,m_\sigma.
\]

In words: the source is the free relative-operation module, not the augmentation module. Thus this is not the prohibited equivariant map from an augmentation unit to the native endpoint unit.

For the endpoint-facing candidate define

\[
\mathbb A_\sigma=A_\sigma\otimes\mathcal R,
\qquad
\mathbb P_\sigma=C_\sigma\otimes N_\sigma,
\qquad
\iota_\sigma=a_\sigma\otimes\alpha_\sigma.
\]

Tensor products here are of the displayed homogeneous conductor-coefficient complexes, with all internal line labels retained. This is a definition of the candidate comparison model, not an assertion that these factors commute through an arbitrary physical derived Hom.

Set

\[
\mathbb Z_\sigma=\operatorname{Cone}(\iota_\sigma),
\qquad b_\sigma:\mathbb P_\sigma\longrightarrow\mathbb Z_\sigma,
\qquad \mathbb J_\sigma=\operatorname{fib}(b_\sigma).
\]

In words: the cone is now induced by the line-retaining adjunction and the native free-orbit map. It retains every endpoint mode outside the chosen orbit in the comparison quotient. It does not replace the endpoint module by a scalar.

The universal cone-fibre retraction of Section 3 gives

\[
\mathbb J_\sigma\simeq\mathbb A_\sigma.
\]

The discrepancy for every retained operation has the explicit filler

\[
d_{\mathbb Z}(0,w_\sigma\otimes r)
=(\nu_\sigma\otimes r m_\sigma,0).
\]

In words: this resolves the primitive comparison discrepancy, all nine quadratic discrepancies, and all 81 ordered-product discrepancies without changing their nonzero endpoint classes.

After the verified coefficient retraction, the full native cochains are still retained. The numerical complexes at operation weight at most four have, per endpoint:

| Complex | Columns |
|---|---:|
| Free relative orbit | 124 |
| Native endpoint bar cochains | 5,161 |
| Comparison cone | 5,285 |
| Comparison fibre | 10,446 |

Their computed cohomology is

| Degree | Comparison object | Fibre |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 3 | 0 |
| 2 | 3 | 9 |
| 3 | 28 | 18 |
| 4 | 81 | 96 |

In words: the unused native endpoint modes remain in the comparison object. The primitive class and its relative-operation orbit are retained in the fibre. Negative fibre cohomology is zero.

## 7. The totalized deformation model and its scope

Fix the complete bare generic class and the established coefficient lift, including its endpoint nullhomotopies. Their relative deformation complex has the already established acyclic model U=0. This uses the fixed coefficient problem; it does not discard unknown physical action deformations.

For the constructed endpoint-facing candidate, take the two-endpoint sums of the P and Z of Section 6. The total comparison is

\[
\mathbb F_{\rm cand}=
\operatorname{fib}(\mathbb U\oplus\mathbb P
\xrightarrow{u_*-b_*}\mathbb Z),
\qquad u_*=0.
\]

In words: the coefficient point is the chosen origin of the endpoint difference spaces. Replacing -b by b changes only the sign of the path coordinate, so the fibre calculation above applies.

For a prescribed primitive pair p=(nu_+ tensor m_+,nu_- tensor m_-), the affine discrepancy is -b(p). An explicit cochain with that differential is minus the sum of (0,w_sigma tensor 1). The two primitive endpoint normalizations are not varied to achieve this cancellation. The chosen point stays in their nonzero components.

The five cohomological directions are ordinary Hom, presentation-Cech, normal cube, group bar, and operation bar. If their degrees are p,c,n,g,r, the total differential uses

\[
D=d_H+(-1)^p d_C+(-1)^{p+c}d_N
+(-1)^{p+c+n}d_G+(-1)^{p+c+n+g}d_R.
\]

In words: every later differential receives the sum of preceding degrees. The checker verifies each constituent square and the cross-term signs. Internal occurrence, Rees, determinant, and excess degrees remain separate and are not added to cohomological total degree.

This sum is the differential on each constituent multi-complex. When forming the comparison cone after group totalization, its off-diagonal map is the complete coherent comparison, with components i, H_g, K_(g,h), and L_(g,h,k) from Section 8. It is not the bare i treated as a strictly equivariant map. The checked homotopy equations are exactly the off-diagonal square-zero conditions. Through weight four the only positive-degree operation products are products of two quadratics; their transports are already strict on raw cup cochains. Higher primitive transports require H and K, as recorded below. No mixed physical action differential is silently set to zero.

The native bar term changes ordinary cochain degree and preserves total occurrence weight. The additional operation-bar direction resolves the free R orbit and must not be counted as a second copy of the native bar differential. Its explicit normalized two-sided resolution has 694 columns through weight four and bar length at most two. Appending the nonempty right word, with sign (-1)^(n+1), gives an R-linear contracting homotopy. Thus it contributes no spurious lower-degree automorphisms.

For the constructed normal-presentation diagram, the three presentation indices form the full simplex. Its augmented complex contracts integrally. There are no normalized quadruple intersections of four distinct presentation indices. This is not a claim about an unspecified physical multi-road cover.

Every coefficient T/end-point pair was computed on all 64 central short-Rees faces, with 192 arrows, 240 squares, and 160 three-cubes per pair. All complete Hom comparison cones are acyclic and each fibre retains one primitive class. This gives 512 independently computed face instances over the four underlying T and both endpoints. The equations are actual specialization maps, not a substitution into fractions on a stalk that has become zero.

Dihedral transport acts on the entire orbit of labelled sources. A quadratic T has trivial stabilizer; a cubic branch triple has stabilizer C3. The primitive coefficient is trivial under these stabilizers. Their degree-zero invariant is Z and their H1 is zero. Reflection transports to the other labelled branch, not to a supposedly identical source in the same degree. For the two endpoint orbits,

\[
H^{-2}(\mathbb F_{\rm cand})=H^{-1}(\mathbb F_{\rm cand})=0,
\qquad H^0(\mathbb F_{\rm cand})=\mathbb Z^2,
\qquad H^1(\mathbb F_{\rm cand})=0.
\]

In words: the comparison is inhabited, with integral components indexed by the two endpoint values and no automorphisms or higher automorphisms in these fixed frames. Prescribing the two primitive components selects a contractible component. The bare Q coefficient does not, by itself, choose those additional endpoint normalizations.

This H1 calculation is for the constructed candidate totalization, not for the unconstructed full physical endpoint/road/normal diagram. Positive higher cohomology, including finite-group cohomology in degree two and above, is not identified with reflection parity.

## 8. Explicit coherence data

### Endpoint and normalization differences

Write theta_sigma=h_sigma c_sigma+nu_sigma in a common endpoint path complex whenever the boundary comparison has already been typed. The new comparison arrow is b_sigma, not the identity on that endpoint Hom complex. Its path comparison is supplied by w_sigma:

\[
\partial\theta_\sigma=a_\sigma^{\rm bdry},\qquad
\partial h_\sigma=a_\sigma^{\rm coef},\qquad
 d_Z k_\sigma=b_\sigma(\nu_\sigma),\quad k_\sigma=(0,w_\sigma).
\]

The symbols a_bdry and a_coef in this paragraph denote the actual endpoint boundaries of the supplied paths, not the precomposition map a_sigma of Section 2. The original boundary-typing comparison remains part of the path tuple. Taking plus minus minus uses the native normalization orientation in the direct sum of the two endpoint complexes; it is not an identification of their different conormal lines.

### Cech and normal directions

For a closed complete tuple Theta, presentation comparisons satisfy

\[
\partial k_{ab}=\Theta_b|_{ab}-\Theta_a|_{ab},\quad
\partial k_{abc}=k_{bc}-k_{ac}+k_{ab},
\]

\[
\partial k_{abcd}=k_{bcd}-k_{acd}+k_{abd}-k_{abc}.
\]

The adjunction map and primitive preimage are globally defined on the constructed coefficient diagram, so their presentation versions agree through the actual restrictions. The normalized degree-three Cech condition is vacuous for its three presentation indices. No unknown physical quadruple intersection has been assigned a filler.

For central-face restriction s_J and a new vanishing parameter i, the checked identities are

\[
s_J a=a_J s_J,\quad s_Jw=w_J,\quad
s_{J\cup\{i,j\}}=s_i s_j s_J=s_j s_i s_J.
\]

In words: all stalk vanishings, frame shifts, and normal cube square and triple routes are included.

### Operation multiplication

The raw bar-cup action is associative and satisfies the Leibniz rule on all cochains. The free-orbit map is strict for products in its chosen generator presentation. In a general Hom notation its coherent-intertwiner equations are

\[
\partial H_a=\rho_Y(a)f-f\rho_X(a),
\]

\[
\partial K_{a,b}=H_{ab}-H_a\rho_X(b)-(-1)^{|a|}\rho_Y(a)H_b.
\]

For even quadratic operations the next equation is

\[
\partial L_{a,b,c}=K_{ab,c}-K_{a,bc}
+K_{a,b}\rho_X(c)-\rho_Y(a)K_{b,c}.
\]

In words: strict cup associativity supplies these product equations in the tested model. Same-sheet word normalization requires the explicit bar homotopies, rather than imposing exterior relations at chain level.

### Dihedral transport, including decomposables

Use the generator labelling

\[
r\xi_i=\xi_{i+1},\quad r\eta_j=\eta_{j-1},\quad
s\xi_i=\eta_i,\quad s\eta_i=\xi_i.
\]

For W=[xi_1,[eta_1,r_00]], raw cup expressions satisfy

\[
s(W)=-W+[r_{11},r_{00}].
\]

In words: the decomposable term is nonzero in the algebra and on both endpoint modules. It is retained, not discarded modulo indecomposables.

For the selected free-R cochain representatives i and their full relative-algebra transport phi_g, the checker constructs

\[
dH_g=g i-i\varphi_g,
\]

\[
dK_{g,h}=gH_h+H_g\varphi_h-H_{gh},
\]

\[
dL_{g,h,k}=gK_{h,k}-K_{gh,k}+K_{g,hk}-K_{g,h}\varphi_k.
\]

There are 104 nonzero transport homotopies and 208 nonzero pair homotopies through weight four. All 26,784 triple equations close; their chosen triple fillers are zero. The proof of closure uses actual native-bar contractions below the diagonal cohomology degree. No averaging is performed. The 4,464 pair equations and all six semilinear target actions are also checked.

These are the operation and group coherences of the constructed native coefficient model. No chain action of this presentation on an independently specified physical collar is asserted.

## 9. Cross-branch interfaces

For Branch B, the exposed kernel is the free relative-operation orbit generated by each line-retained endpoint preimage, with its actual native-bar inclusion. Through weight four it retains every quadratic, cubic primitive, quartic primitive, and quadratic product. All 49 closed generator formulas are available. It is not the six-generator exterior quotient; its transport contains decomposable corrections. The generic coefficient class remains the fixed augmentation-detected input, while operation-bearing data are retained in the relative endpoint kernel.

For Branch A, no supplied map identifies w_sigma or nu_sigma with beta eta_35, nor does one identify the next kernel degree with beta^2 eta_04 eta_35. Their homological degrees, occurrence labels, regulator factors, and conormal lines differ. A map into the first-conormal layer would have to specify all of these transitions and intertwine the operation action. An ordered Yoneda product eta_04 eta_35 is not the mixed anticommutator by declaration. The supplied scalar tangential projection kills Branch A's conormal difference, but no image of the present kernel under that projection has been constructed. No Whitehead, Samelson, or physical homotopy identification is inferred.

## 10. The exact remaining physical arrow

The literal operation-retaining tensor source requested in the task is

\[
\mathsf S^{\rm nat,G}_{\sigma,T}
=P_\sigma^{\rm nat}\otimes_A^L
(P_T\otimes D_\sigma\otimes\widetilde L_\sigma)
\langle\lambda_T\rangle[-4].
\]

Its coefficient factors, support, variance, and lines are now explicit. There is also a literal tensor of the line-retaining counit with P_nat. What has not been supplied is a physical native-linear target/action comparison identifying the resulting complete endpoint path diagram with the tested separated conductor model.

In particular, no identification is asserted between

\[
\begin{gathered}R\operatorname{Hom}_A(\mathsf S^{\rm nat,G}_{\sigma,T},V_\sigma),\\ C_\sigma\otimes_C N_\sigma.\end{gathered}
\]

These are different constructions. A usual tensor-Hom adjunction gives a nested Hom, not the displayed separated tensor [M1]. Over the regular ambient occurrence ring, mixed monomials supply bar nullhomotopies which are absent over the native node. Forgetting the native structure before comparison can therefore erase precisely the operations the task requires retaining.

The remaining degree-zero bivariant arrow must compare those actual source/target path diagrams, retaining the native B-module or homotopy-coherent B-action, endpoint Gysin conormal, product-Cartier line, all six occurrence degrees, and the two labelled excess frames. Its images must reproduce the nonzero primitive and mixed-operation classes in the relative kernel, not merely the scalar generic value. This is a specific mixed change-of-rings/support-action comparison, not another scalar normalizing choice.

Thus Candidate A supplies a successful minimal endpoint-facing relative comparison; the native bar supplies its operation-orbit enhancement. Their identification with the full physical comparison remains unproved. The physical H1 obstruction and physical automorphism space cannot be assigned the candidate's computed values until that arrow and the physical Cech diagram are constructed.

## 11. Reproduction, finite completeness, and provenance

Run

```sh
python check_marici_comparison_fibre_adjunction_bar.py --output marici_comparison_fibre_adjunction_bar_certificate.json
```

The standalone checker uses the Python standard library. It reconstructs the signed target, sources, relative comparison maps, native bar differential, native cup actions, and all tested totalization components. It does not import previous checkers; an optional hash of the baseline checker is recorded solely for provenance.

The run passed **1,177,323 exact assertions**. A run from another directory with PYTHONHASHSEED=17 produced an identical certificate byte for byte. Counts include 16 original/full-central adjunction cases, eight complete 64-face normal cubes, all native monomial weights through four, the endpoint relative fibres, all tested operation-orbit discrepancies, group and product coherence, and the signed total differential tests.

The bar truncation is exhaustive in every retained internal occurrence weight. Higher-weight bar columns cannot alter a lower-weight answer because the differential preserves that weight. For the reported low-degree candidate cohomology, the verified coefficient deformation retractions and free-orbit bar contraction reduce the calculation to nonnegative native and group cochains. Thus the uncomputed operation weights five and above cannot contribute to H-minus-two, H-minus-one, H0, or H1 in this candidate. This argument does not apply automatically to an unconstructed mixed physical totalization with different shifts or structure maps.

Exact integer verification is not proof-assistant certification. No repository files were changed. No physical reflection parity is assigned.

## References

[S1] User task, `Pasted text(3).txt`, and established baseline `marici_physical_endpoint_pullback.md`.

[S2] Pinned target: `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`; native normalization source: ledger entry 93, `Alternating Fusion Normalization-Conductor Square`.

[S3] Supplied Branch B relative-operation theorem and Branch A conormal-extension task briefs. Their claims are retained as inputs where explicitly indicated; the present code independently computes the native bar and operation modules through weight four.

[M1] Stacks Project, Hom complexes, tag 0A8H: https://stacks.math.columbia.edu/tag/0A8H.

[M2] Stacks Project, Effective Cartier divisors and duality, tag 0B4B: https://stacks.math.columbia.edu/tag/0B4B. The three-parameter construction is its ordered Koszul tensor iteration.

[M3] Stacks Project, Cones and termwise split sequences, tag 014D: https://stacks.math.columbia.edu/tag/014D.
