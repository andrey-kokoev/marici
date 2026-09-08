# Occurrence-preserving normalization comparison and its supported dual

Date label: 2026-09-07. Source baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## 1. Correction and scope

The preceding note `marici_native_vs_universal_punctured_overlap_20260907.md` does not establish the claimed obstruction to retaining the native occurrence directions. Entry 434 uses a coefficient base containing the occurrence variables. Comparing its extra-coordinate ideal `(z_sigma)` with the native three-occurrence conductor compares different closed subschemes and different relative bases. Likewise, puncturing only `z_sigma` is not the occurrence puncture used by the native branch.

The dimension calculation for a map factoring through a single auxiliary tangent is correct for that restricted problem, but the source does not require all occurrence information to factor through that tangent. The previous small checker tests that restricted problem; its assertions are not a certificate of the stronger source nonfactorization claim. Also, equality of coefficients under cyclic transport requires a trivial action on those coefficients. It cannot be assumed for the source's separately transported long-coordinate coefficients.

This note supplies the actual augmentation-based comparison, preserving all six occurrence coordinates. It also constructs its normalization-sheet Gysin comparisons, their punctured restrictions, and the complete native relative dualizing attachment. It does not identify this operation with the physical mixed-variance kernel.

The construction is a quotient, not an equivalence of the coefficient algebras. We compute two real derived defects: a nine-dimensional quadratic comparison cokernel, and the non-Tor-independent pullback of the auxiliary normalization. These replace the previous invalid first-order argument.

All module shifts below are cohomological. The bar calculation has separately indicated homological and internal degrees.

## 2. Put both diagrams over the actual occurrence base

Let C be the retained polynomial/Laurent spectator ring, including any already specified Rees parameters and independent long occurrence/normal parameters. Use the ordered triples

\[
x=(X_{13},X_{15},X_{35}),\qquad
y=(X_{02},X_{04},X_{24}),\qquad
S=C[x_1,x_2,x_3,y_1,y_2,y_3].
\]

In words: x and y label the two native occurrence sheets; the auxiliary branch coordinate is not substituted for either triple.

Set

\[
I_+=(x_1,x_2,x_3),\quad I_-=(y_1,y_2,y_3),\quad
B=S/(I_+I_-),\quad B_+=S/I_-,\quad B_-=S/I_+.
\]

In words: B is the native alternating fiber-product ring, and its normalizations retain their three occurrence variables. This is the source construction in Entry 93 [S1].

The auxiliary node and its normalization are

\[
U=S[z_+,z_-]/(z_+z_-),\qquad
N_U=S[z_+]\oplus S[z_-].
\]

In words: U is the one-normal model of Entry 434 before the permitted localizations [S2]. Its base S already carries all six occurrences.

Define the maps

\[
\begin{aligned}
\psi:U&\longrightarrow B,&\psi(x_i)&=x_i,&\psi(y_j)&=y_j,&\psi(z_\pm)&=0,\\
\chi_+:S[z_+]&\longrightarrow B_+,&f&\longmapsto f(x,0,0),\\
\chi_-:S[z_-]&\longrightarrow B_-,&g&\longmapsto g(0,y,0),\\
\chi_c:S&\longrightarrow C,&h&\longmapsto h(0,0).
\end{aligned}
\]

In words: use the declared auxiliary zero sections and the native branch/conductor quotients. These definitions use no target residue or fitted value. They are an available comparison determined by those operations; physical selection or uniqueness is not claimed.

They form a morphism of exact normalization sequences:

\[
\begin{array}{ccccccccc}
0&\longrightarrow&U&\longrightarrow&S[z_+]\oplus S[z_-]&\xrightarrow{\delta_U}&S&\longrightarrow&0\\
&&\downarrow\psi&&\downarrow\chi_+\oplus\chi_-&&\downarrow\chi_c\\
0&\longrightarrow&B&\longrightarrow&B_+\oplus B_-&\xrightarrow{\delta_B}&C&\longrightarrow&0.
\end{array}
\]

In words: both rows use the difference of conductor evaluations. The square is an actual coefficient identity on arbitrary polynomials.

Explicitly,

\[
\delta_B(\chi_+f,\chi_-g)
=f(0,0,0)-g(0,0,0)
=\chi_c\delta_U(f,g).
\]

The comparison thus defines a chain map between the two conductor-difference complexes in degrees zero and one. It is U-linear when the lower diagram is regarded as a U-module diagram through psi.

### Exact kernel and failure of equivalence

The induced degree-zero map has kernel

\[
\ker\psi=(z_+,z_-,I_+I_-)\subset U.
\]

In words: it removes the auxiliary tails and mixed opposite-sheet products. It does not remove a positive-degree polynomial confined to one native occurrence sheet.

As an S-module, its unique monomial normal form is

\[
\ker\psi\cong I_+I_-\oplus z_+S[z_+]\oplus z_-S[z_-].
\]

For the chain comparison chi of conductor-difference complexes,

\[
\operatorname{Cone}(\chi)\simeq(\ker\psi)[1].
\]

In words: the comparison is not a quasi-isomorphism, and its nonzero cone is completely identified. This follows either from the exact kernel complex or from the quasi-isomorphisms of the two difference complexes with U and B.

The degree-zero kernel complex has terms

\[
\bigl((I_-,z_+)S[z_+]\bigr)\oplus
\bigl((I_+,z_-)S[z_-]\bigr)
\longrightarrow I_++I_-.
\]

The displayed map is surjective: positive occurrences can be supplied on the negative auxiliary sheet with the appropriate sign, and negative occurrences on the positive sheet. Its kernel is the ideal above. This proves the cone computation without a scalar-rank inference.

The normal-form inclusion of B into S, followed by S into U, is only additive. It is not a ring section: a positive occurrence times a negative occurrence vanishes in B and does not vanish in U.

## 3. Correct first-order and quadratic comparison

Let

\[
\mathfrak m_U=(x_1,x_2,x_3,y_1,y_2,y_3,z_+,z_-),\qquad
\mathfrak m_B=(x_1,x_2,x_3,y_1,y_2,y_3).
\]

In words: these ideals now define the same retained spectator conductor C on both sides. Their conormal sequence is

\[
0\longrightarrow C\,dz_+\oplus C\,dz_-
\longrightarrow\mathfrak m_U/\mathfrak m_U^2
\longrightarrow\mathfrak m_B/\mathfrak m_B^2
\longrightarrow0.
\]

In words: the map is a split surjection from eight directions to six. It kills exactly the two auxiliary directions and preserves all six native directions. The relations in either algebra are quadratic, so none adds a linear relation.

For arbitrary spectator coefficients a, alpha-i, beta-j, the common-base polynomial

\[
a+\sum_i\alpha_i x_i+\sum_j\beta_j y_j
\]

maps to the native pair with those independent branch-linear coefficients. Its oriented first symbol is

\[
\sum_i\alpha_i\,dx_i-\sum_j\beta_j\,dy_j.
\]

In words: the six separately labelled source symbols are retained. This includes the Entry-93 symbol by choosing its source coefficients; no cyclic-diagonal restriction has been imposed.

### A genuine higher discrepancy

Write \(\operatorname{Tor}_{p,q}\) for homological degree p and internal polynomial degree q of the conductor Tor calculation. The normalized relative bar construction is valid because the augmented algebras are free as C-modules. In internal degree two it has only

\[
V\otimes_C V\xrightarrow{\mu}A_2.
\]

In words: take ordered pairs of linear coordinates and multiply them. A three-fold bar term cannot have internal degree two, so its kernel is the full Tor group in this bidegree.

For U, there are 64 ordered pairs, 35 independent allowed quadratic monomials, and kernel rank 29. An integral basis consists of the 28 commutators plus \([z_+|z_-]\).

For B, there are 36 ordered pairs, 12 same-sheet quadratic monomials, and kernel rank 24. An integral basis consists of six within-sheet commutators and the eighteen ordered opposite-sheet pairs. These ranks were recomputed from the integer multiplication matrices.

Under psi the image has rank fifteen. The nine functionals

\[
\ell_{ij}(c)=c_{x_i|y_j}+c_{y_j|x_i}
\]

vanish on that image and send \([x_i|y_j]\) to the corresponding unit. Therefore

\[
\operatorname{coker}\bigl(
\operatorname{Tor}^{U}_{2,2}(C,C)
\longrightarrow\operatorname{Tor}^{B}_{2,2}(C,C)
\bigr)\cong C^9.
\]

In words: all first occurrence directions survive, but the native mixed quadratic relations supply nine further comparison classes. The cokernel has no integer torsion. This is a calculation in the specified bidegree, not a classification of every higher Tor operation.

These mixed-relation classes must not be identified merely by counting with other branches' higher-wedge attachment channels. No such identification is part of this computation.

## 4. Construct the punctured supported comparison

On the positive auxiliary normalization branch, put

\[
A_+=S[z_+],\qquad
j_+:\operatorname{Spec}B_+\hookrightarrow\operatorname{Spec}A_+,\qquad
\mathfrak r_+=(y_1,y_2,y_3,z_+).
\]

In words: the native positive branch is a regular codimension-four closed subscheme of the full positive auxiliary branch. It removes the opposite occurrences and the auxiliary coordinate, not the three active occurrences. The negative comparison uses \(\mathfrak r_-=(x_1,x_2,x_3,z_-)\).

The ordered Koszul resolution has ranks

\[
(1,4,6,4,1).
\]

Its differential is

\[
d(e_{i_1}\wedge\cdots\wedge e_{i_q})
=\sum_{a=1}^q(-1)^{a-1}\rho_{i_a}
 e_{i_1}\wedge\cdots\widehat{e_{i_a}}\cdots\wedge e_{i_q}.
\]

In words: every equation and every exterior comparison degree is retained. Exactness follows from the regular coordinate sequence [M1].

Let \(\omega_{A_+/C}=\bigwedge^7\Omega^1_{A_+/C}\) and \(\omega_{+/C}=\bigwedge^3\Omega^1_{B_+/C}\). The Koszul dual gives

\[
j_+^!(\omega_{A_+/C}[7])\simeq\omega_{+/C}[3].
\]

In words: the four normal-dual degrees and their determinant cancel exactly four ambient volume directions. This is the supported comparison supplied by a regular immersion; it is not a same-degree scalar trace [M2]. The top-dual coefficient modulo the four equations is the residue map. Every incoming top boundary is divisible by one of those equations.

Define the occurrence punctures

\[
U_+^{\mathrm{aux}}=\bigcup_{i=1}^3D(x_i)\subset\operatorname{Spec}A_+,
\qquad U_+=\bigcup_{i=1}^3D(x_i)\subset\operatorname{Spec}B_+.
\]

In words: both sides use the same three active occurrence opens. Puncturing only z-plus would be a different construction.

The Koszul comparison commutes with all seven occurrence localizations because its four equations are disjoint from the three active coordinates. On every such chart, the endpoint Čech object restricts to \(\mathcal O[2]\), so

\[
j_+^! R\mathcal Hom(\mathcal O[2],\omega_{A_+/C}[7])
\simeq R\mathcal Hom(\mathcal O[2],\omega_{+/C}[3])
\simeq\omega_{+/C}[1].
\]

In words: the correct punctured reverse line is obtained with its actual degree. These are sheaf-Hom calculations on punctured charts, where the input is perfect; completed affine Hom of the original noncoherent localized object is not substituted for them.

The common occurrence Čech complex carries

\[
\frac{dx_1\wedge dx_2\wedge dx_3}{x_1x_2x_3}
\longmapsto
\frac{dx_1\wedge dx_2\wedge dx_3}{x_1x_2x_3}.
\]

In words: after evaluating the ordered normal-dual determinant, the native top occurrence residue is preserved with coefficient one. The full three-open Čech complex has cohomology in degrees zero and two before the reverse shift; after shifting by one, those are degrees minus one and one [M3]. All 128 combinations of four normal support degrees and three occurrence-pole support patterns are checked integrally in the tensor model.

The actual labelled reflection is vertex reflection \(i\mapsto1-i\), together with rotation by two vertices. It sends the ordered positive triple to \((04,02,24)\), whose permutation against \((02,04,24)\) has sign minus one. Thus the odd volume sign is derived from the labels; it is not inferred just from the number three. The conormal determinant transforms compatibly, and all six labelled actions are checked.

## 5. Restore the full conductor attachment

The affine map psi defines a finite closed immersion

\[
i:\operatorname{Spec}B\hookrightarrow\operatorname{Spec}U.
\]

Let \(\mathscr D_{U/C}\) and \(\mathscr D_{B/C}\) be the relative dualizing objects. The auxiliary hypersurface is Gorenstein relative to C, so its object is an invertible hypersurface volume line shifted by seven. Transitivity of extraordinary pullback gives

\[
i^!\mathscr D_{U/C}\simeq\mathscr D_{B/C}.
\]

In words: this is a genuine supported comparison of the coherent coefficient objects [M2, M4]. The total immersion is not declared regular; the regular four-equation constructions above take place on the separate normalization branches.

Dualizing the complete native normalization sequence yields

\[
C_{\mathrm{or}}
\xrightarrow{\Gamma}
(\omega_+\oplus\omega_-)[3]
\longrightarrow\mathscr D_{B/C}
\longrightarrow C_{\mathrm{or}}[1].
\]

In words: two branch-volume contributions are attached to the oriented conductor contribution by the actual codimension-three Gysin maps. The map is not deleted when punctured restrictions are formed.

There is an explicit finite model over S. Resolve C by \(K(x,y)\), resolve the positive volume term by \(K(y)[3]\), and the negative one by \(K(x)[3]\). In the ordered x-then-y exterior basis, set

\[
\begin{aligned}
\gamma_+(e_A\wedge e_D)&=
\begin{cases}e_D,&A=\{1,2,3\},\\0,&A\ne\{1,2,3\},\end{cases}\\
\gamma_-(e_A\wedge e_D)&=
\begin{cases}(-1)^{|A|}e_A,&D=\{1,2,3\},\\0,&D\ne\{1,2,3\},\end{cases}\\
\Gamma&=(\gamma_+,-\gamma_-).
\end{aligned}
\]

Here A indexes selected x-generators and D selected y-generators. In words: the positive map extracts the full x-normal exterior block; the negative map extracts the full y-normal block with the Koszul reordering sign. The final minus is the normalization difference orientation.

The checker verifies every chain-map equation, the entire cone differential, and covariance on every conductor-resolution basis element. The cone uses eighty coefficient-resolution generators. It has

\[
\mathcal H^{-3}(\mathscr D_{B/C})=\omega_+\oplus\omega_-,\qquad
\mathcal H^{-1}(\mathscr D_{B/C})=C_{\mathrm{or}},
\]

with all other cohomology sheaves zero. This is not a splitting of the object.

An independent negative control confirms that the attachment is essential. The derived occurrence fibre of the cone has ranks

\[
(1,9,18,15,6,1)
\]

in degrees minus six through minus one. In particular its degree-minus-seven homology is zero. The artificial direct sum of its cohomology sheaves has a nonzero degree-minus-seven class after the same derived restriction. The cone map kills that spurious class.

On any positive occurrence open, the conductor Koszul resolution and the opposite branch resolution contract using the now-invertible occurrence. The remaining restriction is exactly \(\omega_+[3]\); the negative case is its labelled counterpart. This constructs the conductor-to-puncture restriction of the coefficient dualizing object, with the attachment retained before restriction.

For the already defined coherent fourteen-channel module, restrict the immersion and its ambient space to the existing test open before applying derived adjunction. It gives

\[
R\mathcal Hom_U(i_*\mathcal S_{14},\mathscr D_{U/C})
\simeq i_*R\mathcal Hom_B(\mathcal S_{14},\mathscr D_{B/C}).
\]

In words: the previous reverse source can be expressed through this supported ambient comparison without treating it as perfect. This identity does not make the target-selected module into an independently constructed native physical source, and is not used to extend coherent biduality to the noncoherent PC target.

## 6. Normalization still does not commute with this base change

The normalization diagram above is a morphism of diagrams, not a Cartesian or Tor-independent square.

Indeed,

\[
B\otimes_U N_U\cong B\oplus B,
\qquad N_B=B_+\oplus B_-.
\]

In words: ordinary pullback of the auxiliary normalization gives two copies of the entire singular native space. Native normalization gives its two separate smooth branches. The map from the former to the latter has kernel \(I_-\oplus I_+\), with the ideals viewed in B.

The derived discrepancy is unbounded. As a U-module, the positive auxiliary branch is \(U/(z_-)\), with exact periodic resolution

\[
\cdots\xrightarrow{z_-}U\xrightarrow{z_+}U\xrightarrow{z_-}U
\longrightarrow U/(z_-)\longrightarrow0.
\]

Exactness follows from

\[
\operatorname{Ann}_U(z_-)=(z_+),\qquad
\operatorname{Ann}_U(z_+)=(z_-).
\]

After tensoring with B both auxiliary coordinates act as zero, so

\[
\operatorname{Tor}^{U}_n(B,S[z_+])\cong B,
\qquad
\operatorname{Tor}^{U}_n(B,S[z_-])\cong B
\quad(n\ge0).
\]

In words: one copy of B survives in every homological degree on each pulled-back auxiliary sheet. The proof covers all degrees; the checker samples the differential/annihilator equations only as verification of those symbolic formulas.

Thus the constructed quotient and shriek maps must not be advertised as an identification of the two normalization constructions. The comparison has a concrete derived-normalization defect, rather than the previous alleged absence of native first-order directions.

## 7. Rees localization and the actual generic quotient

The coefficient map is compatible with the retained relations

\[
u_s=t_sX_s
\]

because each short normal and its occurrence are specialized together. A quotient that kills an occurrence also kills its product with its Rees parameter. If that product was inverted at a target stalk, the resulting quotient stalk is zero. No inverse is evaluated at zero in a nonzero ring.

The checker reconstructs the source's 215 loaded states and 522 covering incidences [S3]. Under the native sheet quotients, 72 localizations contain no inverted short occurrence, 64 retain only the positive sheet, 64 only the negative sheet, and 15 become zero because they invert opposite-sheet factors. Every coefficient comparison square is checked; this is not a contraction of the nonconstant coefficient diagram.

All independent long coefficients are preserved. In the honest seven-state quotient, the genuine cycle

\[
\theta=U_L\,t-\sum_{l\in L}X_l
\left(\prod_{k\in L\setminus\{l\}}u_k\right)h_l,
\qquad U_L=\prod_{l\in L}u_l
\]

therefore maps to the same cycle. The projection used in this check is the actual quotient by short-boundary support, not the invalid mixed-flag erasure.

Its lift to the full target still has an eighteen-term short-boundary differential. All eighteen terms remain nonzero under the native specialization in their allowed localization modules. Preserving theta's coefficients does not construct a closed full-target lift, does not kill its connecting boundary, and does not supply the endpoint connector cells.

On the central spectator localization where the earlier endpoint residues are defined, the comparison fixes their constants \(U_L/\tau_-\) and \(U_L/\tau_+\). It does not extend those fractions to a sheet on which the required normal denominator is unavailable. Their global gluing obstruction has not been removed.

Flat completed base change can be applied to the finite Koszul and conductor-cone models before taking the actual punctured opens. This statement is not an interchange between occurrence completion and localization of arbitrary noncoherent modules, nor between local sheaf-Hom and completed affine Hom.

## 8. What is established

The comparison preserves every native first conormal direction and the full three-occurrence punctured residue. The ordered regular-immersion construction provides the correctly shifted local reverse maps. The whole nonregular closed immersion supplies the native coefficient dualizing cone with its nonzero conductor attachment. The coefficient transformations are compatible with the source's actual permitted localizations and labelled transport.

What is not established is that the auxiliary zero-section/occurrence quotient is the physical mixed-variance operation. It lies on the auxiliary conductor; its occurrence puncture must not be identified with an unspecified auxiliary or physical generic deformation. Its raw normalization pullback has the explicit infinite Tor defect above. The full cap, seventeen target closure equations, generic source-to-Q morphism and both endpoint connector 2-cells remain additional comparison data. No integer-prime torsion or RH conclusion follows from the calculations here.

## 9. Reproduction

Run:

```sh
python check_marici_occurrence_preserving_bridge_20260907.py \
  --output marici_occurrence_preserving_bridge_certificate_20260907.json
```

The run performs 81,667 exact assertions. Tests include the polynomial diagram map and kernel, the common-conductor first-symbol map, the integer quadratic bar kernels and primitive cokernel, all four-equation Koszul differentials, 128 complete Koszul–Čech degree-domain complexes, the eighty-generator conductor cone, its actual labelled covariance, the periodic normalization resolution, all 215 loaded states and 522 coefficient squares, and the genuine Q-cycle with its eighteen retained connecting terms.

All matrix reductions use integral unit pivots and reject any remaining nonunit matrix. The proofs above establish arbitrary-polynomial and all-degree claims in their stated scopes. Counts are executable assertions, not proof-assistant certification. No repository file was modified; the preceding nonfactorization artifact is superseded only where explicitly corrected here.

## Source record

[S1] Entry 93, `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`.

[S2] Entry 434, `src/ledger/20260817-434 The Conductor Kernel Extends over Every Loaded Multi-Rees Stalk.md`, blob `0946218ae456f2c423801873432076f86fa2c171`.

[S3] `research/voevodsky/check_ringed_alexandrov_pc_target.py`, blob `7c993d05837fbe2ba29ba30e5b665b5429ab940b`. The loaded differential is independently reconstructed in the checker.

[M1] Stacks Project, *The Koszul complex*, tag `0621`; regular sequences are Koszul regular, tag `062F`.

[M2] Stacks Project, *Properties of upper shriek functors*, tag `0ATZ`, especially open restriction, closed-immersion derived Hom and local-complete-intersection properties; Cartier normal-dual placement, tag `0B4B`. The four-equation formula is also proved directly by its Koszul dual here.

[M3] Stacks Project, *Local cohomology*, tag `0952`: the extended Čech model and the punctured-open comparison.

[M4] Stacks Project, transitivity of upper shriek, tag `0ATX`. Relative dualizing objects are composed with the actual closed immersion, not compared by ranks.

Earlier local artifacts used for the scope and endpoint/puncture interpretation: `marici_punctured_residue_blocks_and_duality_20260907.md`, `marici_punctured_reverse_gluing_20260907.md`, `marici_descent_duality_20260907.md`. The present note does not independently replay all assertions of those artifacts.
