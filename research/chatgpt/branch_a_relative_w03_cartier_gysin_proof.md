# Branch A: relative W03 Cartier Gysin comparison and its retained opposite-endpoint attachment

Date: 2026-09-07.

## Result and scope

The closed opposite edge E={02,35} has two endpoints W03={02,03,35} and W25={02,25,35}. Quotienting its complete W25 packet produces an actual 24-state relative complex. This is not deletion of D25 terms in a graded map: the W25 packet is a subcomplex, and its connecting morphism remains recorded.

The new calculation constructs the Cartier costalk of that relative complex and applies it to the previously constructed conductor map. It gives:

* an explicit signed tensor factorization of the 40-state edge and the 24-state relative complex;
* an integral splitting of the relative normal factor into a Cartier Koszul factor and a separate radial/native-normal cycle;
* the complete 48-state Cartier Hom complex, its counit, its purity map, and a contraction of the purity kernel;
* a nonzero induced supported map with the source derived from applying the same Cartier functor, not by assigning a desired shift;
* a proof that the original, unmodified conductor source cannot lift through this Cartier counit;
* the opposite-endpoint connecting equations, both original physical endpoint restrictions, and the physical f3 reflection on the correctly paired complexes.

The relative conductor map lies entirely in the extra radial/native-normal summand. After inverting beta, the normal-graph retraction onto W03 kills the map. The correctly retyped Cartier map is nonzero, but its unit image retains the conductor and regulator coefficients. No scalar residue or physical Delta_J is assigned.

This is an affine coefficient/relative-support calculation. It does not construct the entire logarithmic six-functor correspondence from the scalar normalization geometry.

## 1. Coefficients and the genuine relative support sequence

Use

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]/(I_-I_+),
\]

\[
I_-=(X_{02},X_{04},X_{24}),\qquad
I_+=(X_{13},X_{15},X_{35}),\qquad A=R/(I_-+I_+).
\]

The coefficient X03 is a polynomial variable independent of the mixed-sheet relations; it is a nonzero-divisor on R and A. Write

\[
x=X_{03},\qquad y=X_{02},\qquad z=X_{35},\qquad v=X_{25}.
\]

The target has the same 430 states [F,H,e], the differential coefficients X_d in the radial direction and beta X_d on native circles, and the separate occurrence differential X35. Its homological degree is

\[
3-|F|+|H|+e.
\]

The normal-graph form follows after extracting the invertible formal factors from u_d=exp(beta X_d)-1. The polynomial extension to beta=0 is a coefficient model. The project source's geometric purity assertion is still restricted to fixed nonzero beta in characteristic-zero completion.

The actual closed edge C_E contains 40 states. Its vertex packets C03 and C25 each contain 16. There is a termwise-split exact sequence

\[
0\longrightarrow C_{25}\longrightarrow C_E\xrightarrow{q}C_{\mathrm{rel}}\longrightarrow0,
\qquad C_{\mathrm{rel}}=C_E/C_{25}.
\]

The relative complex has 24 states. Every native normal subset and every occurrence partner on the retained edge and vertex remain.

The original physical vertices V+={13,15,35} and V-={02,04,24} are different from W03 and W25. The conductor maps considered here have zero values on all 32 original physical endpoint states and on the complete fourteen-state Q quotient. Quotienting W25 is not a quotient of either original physical endpoint.

For the graded lift j of the relative basis, write

\[
\kappa_{25}=\operatorname{pr}_{C_{25}}d_Ej.
\]

For the full conductor map G_E, let G_rel=qG_E and G25=pr_C25 G_E. Then

\[
d_{25}G_{25}+\kappa_{25}G_{\mathrm{rel}}=G_{25}d_{P_A}.
\]

All source columns of this equation are checked. The certificate retains G25 and kappa25; they are not set to zero.

## 2. Factor the complete edge without suppressing any normal

Let M be the ordered three-factor Koszul complex

\[
M=K_R(\beta y,\beta z,z).
\]

Its degree-one generators a,b,k satisfy

\[
da=\beta y,\qquad db=\beta z,\qquad dk=z.
\]

Here a and b are the native 02 and 35 normals; k is the distinct occurrence-35 partner. The equal occurrence label does not identify b with k.

Define the five-state normal/interval packet P_E by

\[
(P_E)_1=R\langle g,h_{03},h_{25}\rangle,
\qquad
(P_E)_0=R\langle p_{03},p_{25}\rangle,
\]

\[
dg=xp_{03}+vp_{25},\qquad
dh_{03}=\beta xp_{03},\qquad
dh_{25}=\beta vp_{25}.
\]

The explicit chain isomorphism is

\[
C_E\cong P_E\otimes_R M.
\]

The orientation convention is g=-[E,empty,0], while p_l and h_l use the positive native vertex bases. For a common subset H of {02,35} and occurrence value e, the tensor-to-native map is

\[
g\otimes(H,e)\longmapsto-[E,H,e],
\]

\[
p_l\otimes(H,e)\longmapsto[W_l,H,e],
\]

\[
h_l\otimes(H,e)\longmapsto
(-1)^{\mathbf1_{02\in H}}[W_l,H\cup\{l\},e].
\]

This specifies all forty columns and the inverse signed permutation. The sign in the last equation reorders the long normal past the common 02 normal. Tensor differential signs include the separate occurrence partner.

After quotienting C25,

\[
C_{\mathrm{rel}}\cong P_x\otimes_R M,
\qquad
P_x=[R\langle g,h\rangle\xrightarrow{(x,\beta x)}Rp].
\]

Define

\[
\zeta=h-\beta g,\qquad d\zeta=0.
\]

Then the determinant-one basis change h=zeta+beta g gives the exact integral splitting

\[
P_x=K_R(x)\oplus R\zeta[1],
\qquad
C_{\mathrm{rel}}=(K_R(x)\otimes_R M)\oplus(R\zeta[1]\otimes_R M).
\]

No coefficient has been inverted. The factor R zeta[1] is part of the actual relative packet, not an added generator.

The first Cartier Bockstein of P_x/xP_x has the normal incidence

\[
g\longmapsto p,\qquad h\longmapsto\beta p,\qquad\zeta\longmapsto0.
\]

This is the same radial-plus-native graph pattern as the scoped edge packet in project Entry 131. Its presence does not identify the earlier x3 edge source with this marked X03 coefficient divisor.

## 3. Evaluate the conductor map in the split packet

The conductor source is its free resolution P_A[2]. The relevant ranks are 1,6,24,92 in homological degrees 2,3,4,5. The first generator differential is

\[
de_i=X_i p_A.
\]

The preceding edge map uses

\[
L_E=\beta[E,E,0]-[W_{03},W_{03},0]-[W_{25},W_{25},0],
\]

\[
dL_E=U_++U_-.
\]

Its positive map G_E^+ sends p_A to U_+, sends e_i to X_i L_E for i in I_+, and is zero on negative generators and all first relations. Every one of the 92 next compatibility equations is retained.

The relative projection has the exact tensor formulas

\[
qL_E=\zeta\otimes(a\wedge b),
\]

\[
G_{\mathrm{rel}}^+(p_A)=\zeta\otimes\beta z a,
\]

\[
G_{\mathrm{rel}}^+(e_i)=X_i\zeta\otimes(a\wedge b)
\quad(i\in\{13,15,35\}).
\]

Every negative-sheet generator and every relation column remains zero. The differential in the shifted zeta summand is minus the common differential; this gives exactly the required annihilator homotopies.

The entire map, including the source-generator homotopies, factors through R zeta[1] tensor M. Its component in K_R(x) tensor M is zero. This is a literal chain identity, not just an assertion about its primary image.

The primary has exact annihilator I in the relative target homology. Each generator of I annihilates it through the displayed source map. For the converse, define a conductor-linear coefficient functional on M_1 by

\[
\ell(v)=\beta[z]v_a+\beta[y]v_b+[y]v_k,
\]

with values in Z[beta,X03,X14,X25]. Brackets extract exactly the stated single short-variable monomial, removing the other short variables. The function kills every boundary and every polynomial multiple of a boundary. Indeed,

\[
d(a\wedge b)=\beta yb-\beta za,
\quad
d(a\wedge k)=\beta yk-za,
\quad
d(b\wedge k)=\beta zk-zb.
\]

Each has functional value zero. Higher conductor-degree terms cannot contribute to the linear coefficient. For the primary,

\[
\ell(\beta za)=\beta^2.
\]

If r times the primary is a boundary, the detector gives epsilon(r) beta^2=0 in the domain R/I. Thus r belongs to I. In particular, x does not annihilate the primary.

The detector is a coefficient functional used for nonvanishing. It is not asserted to be an unrestricted R-linear scalar trace. At beta=1, its value is one.

## 4. The discarded endpoint is an explicit attaching term

In the full five-state packet, the lift of zeta satisfies

\[
d(h_{03}-\beta g)=-\beta v p_{25}.
\]

Thus the raw relative lift, taken without its W25 component, has unit-column defect

\[
(dG_{\mathrm{cut}}-G_{\mathrm{cut}}d)(p_A)
=-\beta^2X_{25}X_{35}[W_{25},\{02\},0].
\]

The missing unit component is

\[
G_{25}(p_A)=-\beta X_{35}[W_{25},\{02,25\},0].
\]

Its native 25 differential cancels the displayed defect. Its other terms, and the source-generator components G25(e_i), satisfy the complete block equation of Section 1. The certificate exports those components and the connecting map on every relative state.

Consequently the relative quotient is a valid localization of the comparison problem, but lifting it back to the full edge requires the original opposite endpoint data. The quotient does not prove that a D03-only absolute map exists.

## 5. Construct the actual Cartier costalk and purity map

Put D=R/(x), and retain the conormal line

\[
\mathfrak n_x=(x)/(x^2),\qquad\mathfrak n_x^\vee=\operatorname{Hom}_D(\mathfrak n_x,D).
\]

For any of the free complexes C used here, define the signed Cartier Hom complex

\[
\mathscr H_x(C)_n=C_n\oplus C_{n+1},
\qquad
D(a,b)=(da,xa-db).
\]

It is a signed model of Hom_R(K_R(x),C), hence of Ri_*i_x^!C. Its counit is

\[
\operatorname{Tr}_x(a,b)=a.
\]

The explicit purity comparison is

\[
\mathscr H_x(C)\longrightarrow
(C\otimes_R D)\otimes_D\mathfrak n_x^\vee[-1],
\qquad
(a,b)\longmapsto\bar b\otimes[x]^\vee.
\]

The target differential has the minus sign of the displayed shift. The program checks this on every column.

Purity is proved here by an explicit kernel contraction as well as by the Cartier theorem. An element of its kernel is (a,xc), whose differential in coordinates (a,c) is

\[
(a,c)\longmapsto(da,a-dc).
\]

The homotopy (a,c) maps to (c,0) contracts this kernel. The only factor extraction is from a coefficient already known to belong to the principal ideal (x); x is not inverted.

For C_rel, the Cartier Hom target has 48 states. The purity target has 24 shifted states. The source calculation applies the same functor to P_A[2], producing 246 indexed states through all relevant source relations. The induced map is simply blockwise application of G_rel^+ and satisfies every chain equation. The program checks both naturality squares, with the counit and with purity.

Since x is regular on A, the source is identified without a fitted shift as

\[
i_x^!(A[2])\simeq(A/(x))[1]\otimes\mathfrak n_x^\vee.
\]

After purity, the resulting supported map is G_rel^+ modulo x, shifted by minus one, with the dual conormal line on both source and target. Its unit image is the shifted class of zeta tensor beta z a. The coefficient detector from Section 3 still gives beta^2 at x=0. Thus this retyped supported map is nonzero.

Its source is not the original A[2]. In particular, the canonical cycle on the source Cartier Hom side is the b-copy of p_A, and its image is (0,G_rel^+(p_A)). The counit sends that cycle to zero. A nonzero costalk class and a nonzero unrestricted trace image are different assertions.

## 6. No same-source Cartier lift; the corner retraction also kills the map

A closed element (a,b) of the Cartier Hom complex obeys xa=db. Its counit homology image is therefore annihilated by x.

But the relative primary has exact annihilator I, and x is not in I. It cannot be the counit image of a closed Cartier-supported class. Consequently there is no derived map with the original source whose counit composite equals G_rel^+.

An independent negative control sets beta=1 and x=1, keeps y=X02 and z=X35, and sets the other short occurrences to zero. The common ring contains Z[y,z]/(yz). The primary detector is one, so G_rel^+ remains nonzero. K_R(x) becomes contractible at x=1, so the Cartier costalk is contractible there. The program verifies its contraction (a,b) maps to (b,0).

At fixed invertible beta, there is also the normal-graph retraction onto the retained corner:

\[
r_x(p)=p,\qquad r_x(h)=h,\qquad r_x(g)=\beta^{-1}h.
\]

Its polynomial regularization beta r_x is checked without adjoining beta inverse. It fixes the corner after beta is inverted and satisfies

\[
r_x(\zeta)=0,\qquad r_xG_{\mathrm{rel}}^+=0.
\]

The equality holds on the entire resolved map, not only on the unit component. This identifies precisely which part of the relative complex the nonzero conductor class occupies: the extra radial/native-normal line, rather than the native corner Koszul packet.

These conclusions do not exclude a logarithmic correspondence with a different independently supplied source and comparison cells. They exclude interpreting this particular relative map as the output of the ordinary Cartier counit with its source left unchanged.

## 7. Reciprocal pairing and physical reflection

The native reciprocal factor is retained with

\[
u=\beta x,\qquad u^\vee=-q^{-1}u.
\]

The original/reciprocal Koszul pairing has

\[
\langle p,h^\vee\rangle=1,\qquad
\langle h,p^\vee\rangle=-q.
\]

The tensor boundary of h tensor h-dual evaluates to u+q u-dual=0. Its determinant is the unit q. The checker verifies these Laurent-unit identities. In the formal physical graph q is 1+u; no occurrence pole is introduced. This pairing supplies the normal-duality convention, not a new projection selecting a scalar from the radial/native pair.

Under a unit coordinate change x'=a x, the conormal basis multiplies by a and its dual by a inverse. The purity value therefore transforms with the required normal line. No beta-dependent scalar is silently evaluated.

The physical reflection f3(v)=3-v fixes X03 and sends

\[
\{02,35\}\longmapsto\{04,13\},\quad
W_{03}\longmapsto\{03,04,13\},\quad
W_{25}\longmapsto\{04,13,14\}.
\]

It also sends occurrence 35 to occurrence 04. The program reconstructs the reflected 430-state target, checks its full chain action and involution square, and descends the map to the paired 24-state relative complexes. Applying Cartier Hom commutes with this semilinear action because X03 is fixed.

The positive-sheet map is sent to the reflected negative-sheet map. Their positive-sheet representatives differ by the already specified full-edge homotopy H_E(p_A)=L_E. Since f3 L_E=-L_E', the reflection-square correction is zero. The W25 term is transported to its W14 counterpart, not erased.

## 8. What is established

The actual relative support, its Cartier source and target, the unit-source degree shift, and both comparison squares are explicit. The new supported map is nonzero. Its primary coefficient remains beta X35 in the excess tensor factor; it is not an unrestricted scalar unit.

The full-edge comparison still contains the companion endpoint, its normal packet, and the connecting map. The original physical endpoint components and the complete Q component remain zero. This local construction therefore does not manufacture the missing generic Q leg or identify a physical conductor–Morse difference.

The next identification would have to explain, from the logarithmic normalization correspondence, whether its source is the retyped A/(X03)[1] costalk source or another normal-dual object, and how it retains the radial/native excess line. Treating the normal-graph retraction as that operation would kill the computed map.

## Reproduction

Run the standalone file:

```sh
python branch_a_relative_w03_cartier_gysin_checker.py --output branch_a_relative_w03_cartier_gysin_certificate.json
```

The checker reads no companion files and makes no network requests. It reconstructs the target states and relevant conductor resolution. Its certificate contains the full local differentials, tensor identifications and inverses, source maps, endpoint attaching maps, Cartier Hom differentials, purity and counit matrices, contractions, and physical reflection matrices.

The run checks 10,632 exact identities. A separate run containing only the checker, with a different Python hash seed, is compared byte-for-byte against the certificate. No assertion count from an earlier computation is included as though it were rerun here.

## Primary source inputs

Project repository: andrey-kokoev/marici, pinned commit d1947b67a60d3e88ba77f4ca60ea02c2a306ee61.

- research/voevodsky/check_absolute_unlocalized_support_pc.rs: signed radial and native differential.
- src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md: the two-sheet ring and conductor module.
- src/ledger/20260814-96 Factorization-Marked Normal-Crossing Span and the Pair-Local Relation Obstruction.md: W03 marking.
- src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md: the actual gallery and scoped physical-normal comparison.
- src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md: the separately typed radial/native packet and Cartier Bockstein.
- src/ledger/20260814-140 Physical-Reflection Naturality of the D03 Edge Purity.md: the physical reflection and pairing conventions.

External mathematical references: Stacks Project tags 0621 (Koszul functoriality), 0A8H (Hom-complex signs), 0A74 (closed-immersion right adjoint and counit), and 0B4B (Cartier duality and the dual conormal line). These justify the affine coefficient constructions, not an unproved physical spatial equivalence.
