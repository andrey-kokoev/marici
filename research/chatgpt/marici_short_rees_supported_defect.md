# Short-Rees supported defects and their central native-conductor extensions

Date: 2026-09-07  
Project: Marici  
Source input: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`  
Continuation of `marici_native_excess_conductor_transport.md`

## 1. Result and precise scope

All eight previously obstructed quadratic/cubic short-Rees conductor channels now have explicit supported comparison morphisms. Their complete Koszul inputs, rather than their isolated pole representatives, have nonzero primitive central values. Those central values are the native normalization-conductor extension, with the residual pair normal, product-Cartier degree, and independent excess retained.

This does **not** construct eight ordinary primitive lifts from the selected complex into the raw complex. The new sources resolve the actual obstruction modules. The old image-ideal theorem remains true. These are supported morphisms out of those modules, not an inversion of the original source selection on the polynomial base.

There are three distinct constructions in this note:

1. A canonical morphism from the selection cone to a localization cone. It detects eight nonzero conductor defects and has explicit nullhomotopies on the six already-liftable first-conormal channels.
2. Complete 128-generator Koszul maps representing the eight defects, and their supported compositions. After central Rees base change, these compositions retain primitive derived extensions even though the selected-to-residue map alone becomes zero.
3. Polynomial lifts into the full native resolution, followed by the previously constructed cap. These satisfy the complete two-endpoint equation. Their equality with the independently framed physical collar operators is not asserted.

All short-Rees parameters below are independent of the long-Rees parameters in the completed proper-descent calculation. Occurrence variables, normal equations, Rees conormals, and physical normal lines remain distinct.

## 2. The actual source and its selection

Let S be the existing polynomial spectator ring over the integers, and set

\[
R=S[t_0,\ldots,t_5],\qquad A=R[X_0,\ldots,X_5],
\]

\[
I_E=(X_0,X_2,X_4),\qquad I_O=(X_1,X_3,X_5),\qquad B=A/(I_EI_O).
\]

In words: B is the actual normalization node. The plus sheet is A/I_E, the minus sheet is A/I_O, and their conductor is C=R. Their difference map is unchanged.

Use the split bases of the actual raw and selected five-generator Koszul sources:

\[
D_u=K_A(t_1X_1,t_3X_3,t_5X_5,v)\otimes\Lambda(\eta_u),
\]

\[
D_x=K_A(X_1,X_3,X_5,v)\otimes\Lambda(\eta_x),
\qquad v=t_0X_0.
\]

In words: both complexes have 32 generators. The residual opposite-pair equation v remains. The independent excess factors have zero differential, but retain their original internal degree.

These bases come from the integral changes

\[
\eta_u=h_3^+-h_3^{03},\qquad
\eta_x=t_3h_3^+-h_3^{03}.
\]

In words: the excess is the difference between the two copies of the shared normal, not multiplication of a target class by that normal.

Write U=B tensor D_u and X=B tensor D_x. The prescribed selection is

\[
\sigma:U\longrightarrow X,\qquad
h_i\longmapsto t_ih_i\ (i=1,3,5),\quad
h_0\longmapsto h_0,\quad\eta_u\longmapsto\eta_x.
\]

In words: this is the complete source map, before taking homology. Its restrictions to both sheets and the conductor commute with the normalization difference.

For a nonempty ordered subset T of {1,3,5}, put t_T equal to the product of its Rees parameters. For epsilon equal to zero or one, the previously computed conductor class is

\[
b_{T,\epsilon}=[v h_T\eta_x^\epsilon].
\]

In words: the fourteen classes have different homological and internal degrees. The six classes with one odd wedge have primitive first-conormal raw lifts; the other eight have exact image ideals t_T C.

The proof of the image statement is retained from the preceding report. In particular, the selected homology has no torsion with respect to t1, t3, or t5. This fact is used below; it is not inferred merely from the displayed representatives.

## 3. One supported comparison for the whole selection triangle

Set tau=t1 t3 t5 and Z=V(tau) in Spec R. It is the **union** of the three branch Rees divisors. On the complement of Z, sigma is an actual chain isomorphism. Its inverse is

\[
\alpha(h_T h_0^a\eta_x^\epsilon)
=t_T^{-1}h_T h_0^a\eta_u^\epsilon.
\]

In words: the inverse is used only in a specified localized output U_tau. It changes neither the polynomial input ring nor the original target coefficient domains.

We use homological complexes. For a chain map f, the cone has terms and differential

\[
\operatorname{Cone}(f)_n=Y_n\oplus U_{n-1},\qquad
 d(y,u)=(d_Yy+f(u),-d_Uu).
\]

In words: the shifted raw summand retains the comparison data. The sign is the homological version of [M2].

Define

\[
\mathcal C_\sigma=\operatorname{Cone}(\sigma),\qquad
\mathcal L_\tau=\operatorname{Cone}(U\longrightarrow U_\tau).
\]

In words: the first cone measures failure of selection to be an equivalence; the second is the supported localization cone. Both have 64 source-basis positions. The second cone has different coefficient domains on its two arms.

There is an explicit morphism of complete triangles

\[
\Phi:\mathcal C_\sigma\longrightarrow\mathcal L_\tau,
\qquad \Phi(x,u)=(\alpha x,u).
\]

In words: the selected arm uses the localized inverse, and the raw comparison arm is retained by the identity. The chain equation follows from alpha sigma equal to the localization map, and is checked on every basis position.

Since U is termwise flat over R and has injective localization, there is a quasi-isomorphism

\[
\mathcal L_\tau\simeq U\otimes_R(R[\tau^{-1}]/R)
\simeq R\Gamma_Z(U)[1].
\]

In words: the quotient is a convenient computation model for this supported output. The complete cone, not that nonflat quotient alone, must be used for derived specialization. The support construction and its base-change rule are [M1].

The selected-to-supported map is the restriction of Phi to the selected arm:

\[
\beta:X\longrightarrow\mathcal L_\tau,\qquad
\beta(x)=(\alpha x,0).
\]

In words: in the residue quotient it is simply the localized inverse modulo the original raw module. It is not a raw-source lift.

The construction commutes with both sheet restrictions and their difference. The checker also constructs all eight partial selections, their 27 comparable maps including identities, and all 64 composable triples including identities. Local inverses compose strictly after the indicated coefficient refinements. There is no independently chosen residue for each wedge.

## 4. Exact supported images and their lower pole terms

On the conductor classes, beta gives

\[
r_{T,\epsilon}
=\left[\frac{v}{t_T}h_T\eta_u^\epsilon\right].
\]

In words: these are cycles in the supported raw complex. Multiplying by an occurrence variable is treated using the original node and Koszul relations, not by evaluation of that variable.

The exact answer is

\[
[r_{T,\epsilon}]=0\quad(|T|=1),
\]

\[
\operatorname{Ann}_A[r_{T,\epsilon}]
=(X_0,\ldots,X_5,t_T)\quad(|T|=2,3).
\]

In words: the six first-conormal defects vanish. The other eight generate copies of C/(t_T), with no integer torsion. Their support is the union of the divisors in T, intersected with the occurrence conductor.

**All-polynomial proof.** The long exact sequence of U to U_tau to L_tau identifies the kernel of the supported map on a selected conductor line with the raw selection image on that line. Localization on the complete selected homology is injective in the branch Rees variables. The preceding exact image computation therefore gives C for one wedge and t_T C for two or three wedges. Occurrence annihilators are the existing native relations and their explicit Koszul homotopies. Thus no additional scalar or higher-degree polynomial can enlarge the kernel.

There is also a direct chain explanation. Put k=|T| and

\[
W_{T,\epsilon}=\frac{h_T h_0\eta_u^\epsilon}{t_T}.
\]

Then

\[
dW_{T,\epsilon}
=\sum_{i\in T}(-1)^{\operatorname{pos}_T(i)}
 \frac{X_i}{t_{T\setminus\{i\}}}
 h_{T\setminus\{i\}}h_0\eta_u^\epsilon
 +(-1)^k r_{T,\epsilon}.
\]

In words: the comparison has lower, partially localized terms. They are forced by the source differential.

For one wedge the first term is polynomial, hence zero in the residue quotient. This gives the explicit nullhomotopy for the six first-conormal defects. For two wedges the two partial-pole terms are actual single-divisor cycles; they must not be erased. For three wedges the three partial-pole terms retain the pairwise comparison data.

### A top-residue shortcut fails

For the individual T-channel, one can project the product-divisor residue module to the highest local-cohomology module of the simultaneous intersection:

\[
R[t_T^{-1}]/R\longrightarrow
H^{k}_{(t_i:i\in T)}(R).
\]

In words: this is the quotient that forgets every fraction missing any one of the k poles. It compares these output modules; it is not an unshifted identification of their full support functors.

Under this projection every partial-pole term in the previous equation disappears. The image of r is therefore a boundary, with witness (-1)^k W. All eight nonzero product-divisor classes are lost by this shortcut. A pair or triple of denominator factors does not, by itself, specify a primitive codimension-two or codimension-three trace of this coupled source.

## 5. Complete supported Koszul inputs for the eight missing channels

The annihilator calculation supplies an actual support module C/(t_T). Resolve it by

\[
\mathcal K_T=K_A(X_0,X_1,X_2,X_3,X_4,X_5,t_T).
\]

In words: this is the 128-generator Koszul resolution of the occurrence conductor intersected with the product Cartier divisor. The six occurrence equations followed by t_T are a regular sequence on the stated polynomial ring. These are coefficient-resolution generators, not new physical filling cells.

Let e_i denote its six occurrence generators and z_T its product-Cartier generator. Set n=|T|+epsilon. An explicit degree-n map

\[
 j_{T,\epsilon}:\mathcal K_T\longrightarrow\mathcal C_\sigma
\]

represents the conductor defect. To give its signs without ambiguity, first define the following uncorrected components:

\[
\begin{aligned}
\widetilde j(1)&=(v h_T\eta_x^\epsilon,0),\\
\widetilde j(e_j)&=((-1)^kX_j h_T h_0\eta_x^\epsilon,0),
 &&j\in\{0,2,4\},\\
\widetilde j(z_T)&=(0,v h_T\eta_u^\epsilon),\\
\widetilde j(e_j\wedge z_T)&=(0,(-1)^{k+1}X_j h_T h_0\eta_u^\epsilon),
 &&j\in\{0,2,4\}.
\end{aligned}
\]

In words: all other source components are zero. There are eight nonzero source columns. The first arm contains selected-source values; the second contains raw comparison values.

On a source wedge a of length p set

\[
 j(a)=(-1)^{np}\widetilde j(a).
\]

Then

\[
 d j=(-1)^n j d.
\]

In words: this is a homogeneous chain map, or equivalently an ordinary degree-zero map after the stated source shift. Its internal frame is the degree of v h_T eta^epsilon; every occurrence and Rees determinant is retained.

The equations use the existing mixed-product relations. For example, the product-Cartier row fills t_T times the selected class. The even-occurrence/product-Cartier rows compare this filling with the already existing occurrence-annihilator homotopies. Odd occurrence products vanish by the native node relation, and the higher mixed Koszul equations cancel with their ordered signs.

The induced map from C/(t_T) to the corresponding cone homology is injective. This is a complete supported morphism, not just the observation that t_T annihilates one cohomology class. All 128 columns are checked for each of the eight maps. The six labelled transports preserve the maps with the explicit wedge-orientation sign.

## 6. Why the whole supported map survives central specialization

Compose the complete input with the supported triangle map:

\[
\Psi_{T,\epsilon}=\Phi j_{T,\epsilon}.
\]

In words: the localized residues and their raw comparison rows remain part of a single map.

Set t1=t3=t5=0, but retain t0 and all independent spectator parameters. Write a subscript zero for this derived base change. The localized arm becomes zero, while the original raw arm remains:

\[
(\mathcal L_\tau)_0\simeq U_0[1],\qquad
U_0=B_0\otimes K(0,0,0,v)\otimes\Lambda(\eta_u).
\]

In words: the isolated selected-to-residue map beta specializes to zero. The full cone map specializes to the projection onto the shifted raw summand. This was verified on all eight central Rees faces. It follows from the flat cone model, not from substituting zero into fractions.

The complete source specializes to K(X0,...,X5) tensor the exterior generator z_T with zero differential. Its original product-Rees internal degree is not erased.

The specialized Psi has four nonzero columns: z_T and the three even-occurrence/product-Cartier pairs. Its z_T value is a boundary. Removing that boundary by the explicit homotopy

\[
 H(z_T)=(-1)^{\epsilon+1}(0,h_T h_0\eta_u^\epsilon)
\]

leaves exactly three columns:

\[
\Theta_{T,\epsilon}(e_i\wedge z_T)
=(-1)^k(0,X_i h_T h_0\eta_u^\epsilon),
\qquad i\in\{1,3,5\}.
\]

In words: the surviving coefficient cocycle is the odd-sheet normalization cocycle, with the residual h0 direction, independent eta, and product-Cartier input still present. The complete identity is

\[
\Psi_{T,\epsilon,0}-\Theta_{T,\epsilon}
=dH-(-1)^{n+1}Hd.
\]

In words: this is the actual comparison between the specialized supported map and its three-row native representative. The lower rows cannot be dropped.

### Primitive nonvanishing, including all homotopies

The scalar three-row pattern is the native normalization class

\[
\nu(e_i)=\begin{cases}X_i,&i\in\{1,3,5\},\\0,&i\in\{0,2,4\},\end{cases}
\qquad
[\nu]\in\operatorname{Ext}^1_{A_0}(C_0,B_0).
\]

In words: it is the connecting class of the original two-sheet normalization sequence. In Theta it occurs in a higher comparison with the residual normal and the product-Cartier factor, not as an unshifted identification of these modules.

There is a direct obstruction to nullhomotopy. Project the central raw complex onto the fixed odd wedge h_T and the prescribed eta factor; this is a chain projection because the remaining differential changes only h0. A hypothetical nullhomotopy would require a coefficient f on its z_T row satisfying

\[
 vf=0,\qquad X_i f=cX_i\quad(i=1,3,5)
\]

for the scalar multiple c of the proposed conductor class. The first equation forces f into I_O. On the odd sheet, the second equation forces the constant coefficient of f to be c. Since an element of I_O has zero conductor value, c must be zero. Therefore no nonzero spectator/Rees scalar multiple can be a boundary.

Every occurrence coordinate annihilates the class: even coordinates do so by the node relation; odd coordinates have explicit source homotopies. Thus the distinguished class is a primitive conductor line over C0, with no integer or spectator-Rees torsion.

The checker independently constructs each **complete homogeneous derived Hom complex**, including all 32 raw target states and all 128 input states permitted in the frame. Four frames have a rank-one group and four have a rank-two group in the relevant map degree. The designated Theta is primitive in every case. No uniqueness claim is made for an unconstrained choice of central map in a rank-two frame.

This is the main positive result: all eight full supported comparison maps have primitive central derived values. Their bare selected-cycle residue maps nevertheless specialize to zero. The nonzero information survives as a native conductor extension, not as eight ordinary raw-source cycle lifts.

## 7. Lift through the actual native resolution before applying the cap

The maps j above have native B coefficients. Simply replacing the ambient target by its underived B quotient would destroy some localization stalks and is not used to establish a physical comparison.

Instead, let P be the existing fifty-generator free A-resolution of B, and let C_A be the raw-to-selected cone before tensoring with B. There is a quasi-isomorphism

\[
 P\otimes_A C_A\longrightarrow B\otimes_A C_A=\mathcal C_\sigma.
\]

In words: the source retains every native resolution relation. Since each K_T is finite free, its derived mapping space carries this quasi-isomorphism to an equivalence. A fixed j therefore has a contractible space of lifts through it; this does not assert uniqueness of every possible normalization of j itself.

I constructed polynomial lifts

\[
\widetilde j_{T,\epsilon}:\mathcal K_T\longrightarrow P\otimes_A C_A
\]

and verified their full chain equations over A. Each two-wedge lift contains 382 polynomial terms, of which 374 are resolution corrections. Each three-wedge lift contains 580 terms, of which 572 are corrections. Across all eight maps there are 3,452 terms. No source coefficient has a negative exponent.

**Construction of the corrections.** For every one of the 64 occurrence-support sets, contract the homogeneous native resolution using signed-unit pivots. Extend this contraction to P tensor C_A by a finite perturbation series. The series terminates because every right-hand differential lowers the cone degree. Lift the free source one wedge degree at a time: the discrepancy from the already lifted boundary is a cycle in the kernel of the native augmentation, and the explicit contraction supplies its correction. Every correction is checked, not inferred from rank equality.

Now use the preceding complete native cap F and its endpoint composite

\[
 d_KF-Fd_P=a,\qquad a=a_+f_+-a_-f_-.
\]

In words: both native endpoints remain in the same equation. Tensor the cap with the supported cone map Phi and compose with the free lift. Denote the results by F_T and A_T. Their degrees are n-2 and n-3, and

\[
 dF_T-(-1)^{n-2}F_Td=A_T,
\qquad dA_T-(-1)^{n-3}A_Td=0.
\]

In words: all eight supported inputs participate in the **whole cap and both endpoint equations**, before taking any scalar readout or underived node quotient.

The eight compositions contain 4,400 cap terms and 488 endpoint terms. A two-wedge channel has 20 plus-endpoint and 32 minus-endpoint terms; a three-wedge channel has 24 plus-endpoint and 64 minus-endpoint terms. These are counts of coefficient terms, not multiplicities of physical states. Both endpoint supports are explicitly present.

Every added inverse belongs to the distinguished localized output arm. The original target states retain their own occurrence/normal localization domains. There is no ambient occurrence inversion.

This is a verified map into the supported, derived-source target of the comparison. The calculation does not prove that these cochains are the independently prescribed physical collar operators, nor that each composed endpoint cohomology class equals a physical unit. Nonzero matrix entries are not used as a substitute for that missing class-level identification.

## 8. What remains and what is no longer missing

The eight quadratic/cubic short-Rees channels no longer lack explicit supported input maps. Their localization triangle, complete product-Cartier/conductor resolutions, central native extension classes, and free-resolution compositions with both endpoints are all constructed.

Three claims have **not** been made:

* the original raw-to-selected map has acquired eight ordinary primitive lifts;
* a highest-pole residue on a simultaneous parameter intersection represents these complete maps;
* the physical collar framing or reflection parity has been fixed by the existence of these supported extensions.

The remaining comparison is now between explicit objects: transport these eight native-conductor extensions, with their product-Cartier source degrees and the actual free-resolution endpoint cochains, to the prescribed physical collar frame. Its test must compare the whole maps, not just eta, a residue coefficient, or an endpoint term count.

The source maps respect the six labelled branch/pair transports with their ordered orientations. The chosen free-resolution representatives use auxiliary contractions; their derived lifting class is independent of that choice through the augmentation equivalence. This statement is not an uncomputed assertion of strict equivariance of every displayed representative.

## 9. Verification

Run:

```sh
python check_marici_short_rees_supported_defect.py \
  --output marici_short_rees_supported_defect_certificate.json
```

The checker passes **96,832 exact assertions**. It checks the full selection/localization triangle, all normalization restrictions, all fourteen residue channels and their parameter-annihilator domains, all eight product-Cartier Koszul maps, their central homotopies and primitive complete Hom classes, six oriented transports, 64 native contraction blocks, all free-resolution correction equations, and the complete cap/endpoint compositions.

The comparison before inserting the individual Koszul inputs has 3,200 source basis positions, 13,760 target positions, 2,752 cap terms, and 384 endpoint terms. These counts refer to finite basis positions with their declared coefficient rings; a localization module is not being counted as a finite-rank free A-module.

The all-polynomial claims follow from the proofs above. Integer matrices at fine degrees are exact checks of those complexes, not extrapolation from numerical samples. This is executable verification, not proof-assistant certification. No repository files were written.

## Sources

[S1] Pinned Marici normalization node and its two sheet augmentations: `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`.

[S2] Original/reciprocal normal convention, independent repeated-normal excess, and the distinction between finite Koszul and supported Cech outputs: `src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md`, blob `d5ed0c89e804284a4bf45bfa1e0c0bc2eab6eb12`. The relevant passage was re-read for this calculation.

[S3] Original 215-state target incidence and coefficient domains: `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`.

[M1] Stacks Project, tag `0952`, Local cohomology: extended Cech models, exactness, and derived base change.

[M2] Stacks Project, tag `014D`, Cones and termwise split sequences: cone maps with their comparison homotopies.

[M3] Stacks Project, tag `0621`, The Koszul complex: exterior basis maps, multiplication homotopies, and tensor signs.

Locally retained inputs: `marici_native_excess_conductor_transport.md` and its executable; `marici_joint_conductor_spatial_cap_comparison.md`; `marici_joint_triangle_rees_gysin.md`. Their distinctions between a coefficient correspondence, a class-level physical trace, and a physical collar identification remain in force.
