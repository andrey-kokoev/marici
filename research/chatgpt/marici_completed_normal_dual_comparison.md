# The actual normal-derived dual and the coupled Rees symbol of the native comparison

Date: 2026-09-07  
Project: Marici — continuation of the native spatial three-extension  
Repository inputs pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and precise scope

The complete native comparison admits compatible polynomial representatives in a finite-free resolution system of the **original 215-state normal-localized target**. Their colimit is the already constructed target map, with both endpoint comparison composites retained. Dualizing this system and taking its derived inverse limit constructs a map from the actual derived Hom over the ambient coefficient ring into the entire native normalization dual. The latter is the seven-module spatial three-extension from the preceding calculation. This is not the integer transpose of a single fine degree.

The generic part can be calculated for every order, including its inverse limit. Its reverse map to the native conductor has exact image

\[
J=(u_0u_1u_2,\ X_0u_1u_2,\ X_1u_0u_2,\ X_2u_0u_1).
\]

In words: in this display only, indices zero, one and two label the **three long directions**. The image is a proper ideal in the conductor coefficient ring. Completion does not enlarge it. A previously observed coefficient-one value after fixing a normal frame is not an unrestricted polynomial-linear unit trace.

On the explicitly declared product-Rees chart for these three long directions, this ideal factors as their principal occurrence line times

\[
J_t=(t_1t_2,t_0t_2,t_0t_1).
\]

In words: after pairing the actual common occurrence line with its dual, the remaining trace image is the pair-product Rees ideal. Its zero locus is the union of the three coordinate axes, not a prime-integer torsion locus.

The whole map has 27 terms of total long-Rees order two and 16 terms of order three. Both endpoint composites first appear in order three. Their chain equation includes the quadratic-to-cubic correction. On a face where one long Rees parameter vanishes, nine comparison terms survive but both endpoint composites vanish. On any face where two long Rees parameters vanish, the **entire ordinary comparison** is zero.

This constructs an ambient-ring derived-dual comparison and its full filtered coefficient test. It does not identify that dual with the full ringed supported-Verdier six-functor. It does not evaluate a filtered Gysin symbol into an ordinary scalar, identify the independent excess with an internal marked state, or assign physical reflection parity.

## 2. Keep the ambient ring and the native source separate

Let

\[
R=\mathbb Z[X_a,u_a\mid a\in\mathscr D],\qquad
\mathscr D=\mathscr S\sqcup\mathscr L,
\]

where the short and long diagonals are

\[
\mathscr S=\{x_0,\ldots,x_5\},\qquad
\mathscr L=\{D03,D14,D25\}.
\]

In words: there are nine occurrence variables and nine normal variables. They are independent until an explicitly stated Rees substitution. Further polynomial spectator variables can be adjoined. No occurrence or normal variable is inverted in the ambient ring.

The normalization source is

\[
\mathfrak B=R/(J_EJ_O),\qquad
J_E=(X_0,X_2,X_4),\qquad J_O=(X_1,X_3,X_5),
\]

\[
B_+=R/J_E,\qquad B_-=R/J_O,\qquad
C=R/(J_E+J_O).
\]

In words: the source is the actual two-sheet normalization node. Here short subscripts retain their original meaning. Throughout Sections 3–6, a long direction is denoted by a diagonal label or by a lower-case generic index accompanied by an explicit declaration.

Let P be its fifty-generator free resolution. It has ranks

\[
(1,9,18,15,6,1)
\]

in homological degrees zero through five. In words: P retains the native source, not merely its conductor module.

Write E-index and O-index for the even and odd short triples. Apart from the bottom generator, its generators are \(p_{U,V}\), for nonempty \(U\subseteq E\) and \(V\subseteq O\), in degree \(|U|+|V|-1\). The differential deletes a member of U or V with its Koszul coefficient and ordered sign; when both sets are singletons it maps to the bottom generator with coefficient \(X_eX_o\).

Its actual sheet maps and joint homotopy are

\[
f_+(p_{U,V})=X_o e_U\quad(V=\{o\}),\qquad
f_-(p_{U,V})=X_e e_V\quad(U=\{e\}),
\]

\[
H(p_{U,V})=(-1)^{|U|}e_U\wedge e_V,
\qquad
\partial H+H\partial=\iota_Ef_+-\iota_Of_-.
\]

In words: these maps use the two native branch resolutions and the six-occurrence conductor Koszul resolution. No branch attachment is split off. The standard bottom augmentations complete the formulas on the degree-zero generator.

The preceding spatial calculation gives an equivalence of **complete** complexes

\[
R\operatorname{Hom}_R(\mathfrak B,\omega_{A/S}\otimes_A R)[6]
\simeq\mathcal P_{\mathrm{sp},R},
\]

where \(A=S[X_0,\ldots,X_5]\) and \(\mathcal P_{\mathrm{sp}}\) is the seven-module spatial three-extension. In words: the six-occurrence determinant and its shift remain in this comparison. Working over the ambient polynomial ring is not working over the intrinsic singular ring \(\mathfrak B\); perfection over one does not imply perfection over the other.

## 3. Resolve every permitted localization without changing the spatial target

An original target state is \((S,H)\), with S noncrossing and \(H\subseteq S\). It has homological degree

\[
\deg(S,H)=3-|S|+|H|.
\]

In words: H records marked normals. Its original coefficient module is

\[
R_{S,H}=R[u_a^{-1}:a\in S\setminus H].
\]

In words: only the unmarked normals of that state can be inverted. The source differential has radial coefficient \(\epsilon X_a/u_a\) and normal-deletion coefficient a signed localization inclusion. These are the pinned source rules [S1].

For an independent vector \(\mathbf n=(n_a)\), with every \(n_a\ge1\), define a finite-free complex \(K_{\mathbf n}\) on the **same 215 states**, with differential

\[
\begin{aligned}
\partial_{\mathbf n}[S,H]
={}&\sum_{a\ \mathrm{addable}}\epsilon(S,a)X_a u_a^{n_a-1}[S\cup\{a\},H]\\
&+(-1)^{3-|S|}\sum_{h\in H}(-1)^{\operatorname{pos}_H(h)}u_h^{n_h}[S,H\setminus\{h\}].
\end{aligned}
\]

In words: at order one this is the original finite absolute normal complex. Higher orders resolve the actual localization, rather than setting its coefficient to one. The two possible orders of every radial/radial, normal/normal, or radial/normal square have identical monomials and opposite signs, so the differential squares to zero for every order vector.

For \(\mathbf m\ge\mathbf n\), put

\[
j_{\mathbf n,\mathbf m}[S,H]
=\left(\prod_{a\in S\setminus H}u_a^{m_a-n_a}\right)[S,H],
\]

\[
\kappa_{\mathbf n}[S,H]
=\left(\prod_{a\in S\setminus H}u_a^{-n_a}\right)[S,H]_{\check C}.
\]

In words: j is a polynomial transition map; kappa maps into the original, individually permitted localization stalk. Neither changes spatial support.

The exact identities are

\[
\partial_{\mathbf m}j_{\mathbf n,\mathbf m}=j_{\mathbf n,\mathbf m}\partial_{\mathbf n},
\qquad
\partial_{\check C}\kappa_{\mathbf n}=\kappa_{\mathbf n}\partial_{\mathbf n},
\qquad
\kappa_{\mathbf m}j_{\mathbf n,\mathbf m}=\kappa_{\mathbf n}.
\]

In words: this is one compatible system of complete complexes. On each coefficient module its colimit is precisely its original localization. Hence

\[
\operatorname*{colim}_{\mathbf n}K_{\mathbf n}\cong K_{\check C}.
\]

In words: the system recovers the given target, not another target with a similar signature. Diagonal orders are cofinal, so a single integer n is enough when taking the derived inverse limit below. This is a face-compatible version of the standard Koszul presentation of the extended Cech complex [M1].

The same construction preserves the actual support filtration

\[
V_{\mathbf n}\subset B_{\mathbf n}\subset K_{\mathbf n},\qquad
E_{\mathbf n}=K_{\mathbf n}/V_{\mathbf n},\qquad
Q_{\mathbf n}=K_{\mathbf n}/B_{\mathbf n}.
\]

In words: both endpoint complexes, short support, the endpoint quotient, and the generic quotient are present before any colimit or duality. Every sequence is degreewise split on the labelled free modules. All six labelled transports permute the independent order coordinates and commute with the maps, with the inherited polarity convention.

## 4. Lift the whole native comparison, not its generic coefficient alone

Let \(F_{\check C}=-cH\) be the previously constructed complementary-face map. It satisfies

\[
\partial F_{\check C}-F_{\check C}\partial_P
=a_+f_+-a_-f_-.
\]

In words: the discrepancy is exactly its two source-derived endpoint composites. It has 43 terms on sixteen source columns; its endpoint discrepancy has six terms.

There is a unique coefficient lift of this representative defined by

\[
F_{\mathbf n}(p)_{S,H}
=\left(\prod_{a\in S\setminus H}u_a^{n_a}\right)
F_{\check C}(p)_{S,H}.
\]

In words: clear only the denominators of that very target state. Every resulting coefficient is a polynomial. This is not a claim that an arbitrary target cochain can be cleared at order one; it is a verified property of this specific source-defined map.

For a short face S, the order-one lift of the building block is

\[
\Omega_1(S)=U_L[S,\varnothing]
-\sum_{\ell\ \mathrm{compatible\ with}\ S}
\varepsilon_{S,\ell}X_\ell\frac{U_L}{u_\ell}
[S\cup\{\ell\},\{\ell\}],
\qquad U_L=\prod_{\ell\in\mathscr L}u_\ell.
\]

In words: the quotient \(U_L/u_\ell\) is a polynomial product of the other two long normals. The ordered signs are exactly those of the existing complement map. At higher orders this block is multiplied by \(\prod_{a\in S}u_a^{n_a-1}\). Its complete radial differential is the short-occurrence Koszul differential, so it composes with the same native H.

All orders satisfy

\[
\partial_{\mathbf n}F_{\mathbf n}-F_{\mathbf n}\partial_P
=a_{+,\mathbf n}f_+-a_{-,\mathbf n}f_-,
\]

\[
j_{\mathbf n,\mathbf m}F_{\mathbf n}=F_{\mathbf m},\qquad
\kappa_{\mathbf n}F_{\mathbf n}=F_{\check C}.
\]

In words: both endpoint maps and their comparison survive in the same system. These equations, with the endpoint maps included, are stronger than a tower of generic residue values.

At order one the individual endpoint maps are

\[
a_{+,1}(e_E)=U_L[v_+,\varnothing],\qquad
a_{-,1}(e_O)=-U_L[v_-,\varnothing],
\]

with the other branch-resolution columns zero. In words: their signs and coefficients are forced by the single complement map. Higher-order representatives multiply them by the endpoint's unmarked short-normal factors; localization gives exactly the previous endpoint poles.

Projection to E and Q gives closed degree-two derived maps. Dualizing **complete complexes** therefore gives

\[
R\operatorname{Hom}_R(E_{\check C},R)
\longrightarrow R\operatorname{Hom}_R(\mathfrak B,R)[2],
\]

and the corresponding map from the generic dual. In words: this reverse map reaches the entire native dual, not an independently split conductor line.

After tensoring the occurrence canonical line and shifting, it is a comparison

\[
R\operatorname{Hom}_R(E_{\check C},\omega_{A/S}\otimes_A R)[4]
\longrightarrow\mathcal P_{\mathrm{sp},R}.
\]

In words: the codomain is the seven-module spatial source from the preceding result. This explicitly states the variance and degree of the comparison.

## 5. The genuine coefficient-ring dual requires an inverse limit

Because each finite-order complex is bounded free,

\[
R\operatorname{Hom}_R(K_{\check C},R)
\simeq R\!\lim_n\operatorname{Hom}_R(K_n,R).
\]

In words: replace the localizations by their finite-free system, dualize, and retain the derived inverse limit. Ordinary integral duality of one monomial degree is a different operation. The Hom and derived-limit conventions are [M2–M3].

All support triangles and all endpoint comparison identities pass to this limit. The formula already gives a fully specified model for the ambient R-linear derived dual on all 215 states. It makes no claim that this ambient dual is the as-yet-unidentified full supported-Verdier functor of the physical correspondence.

### Complete calculation of the seven-state generic dual

In this subsection indices \(i=0,1,2\) label \(D03,D14,D25\), respectively. Write \(T,M_i\) for its four degree-three states and \(F_i\) for its degree-two facets. At diagonal order n,

\[
\partial_n T=\sum_i X_i u_i^{n-1}F_i,\qquad
\partial_n M_i=u_i^nF_i.
\]

In words: the marked states have unlocalized coefficients at every order. The dual differential is injective, since each column has its own nonzero \(u_i^nM_i^\vee\) entry. Its only cohomology is in degree three:

\[
M_n=R^4/N_n,\qquad
N_n=\bigoplus_i R\,u_i^{n-1}\nu_i,\qquad
\nu_i=X_iT^\vee+u_iM_i^\vee.
\]

In words: a common Hom sign on the differential has no effect on this presentation. The three vectors \(\nu_i\) are R-linearly independent.

The transition \(M_{n+1}\to M_n\) is the quotient of the identity on \(R^4\), hence surjective. Therefore no extra cohomology comes from a first derived inverse limit. The complete generic dual has

\[
H^3R\operatorname{Hom}_R(Q_{\check C},R)=\widehat M_Q:=\lim_n M_n,
\qquad H^j=0\quad(j\ne3).
\]

In words: its completion is part of the genuine ring-linear answer. It is not optional additional topology imposed on the fixed-degree calculation.

An explicit presentation is

\[
\widehat M_Q\cong
\frac{R^4\oplus\bigoplus_i\widehat R_{(u_i)}}
{\langle(\nu_i,-1_i):i=0,1,2\rangle}.
\]

In words: three one-normal completions are glued to the four polynomial covectors through their actual generic incidence vectors. Here the denominator means the R-submodule generated by those pairs.

To verify this presentation, choose a polynomial representative of the order-one class. The successive differences lie in

\[
N_1/N_n\cong\bigoplus_i R/(u_i^{n-1}).
\]

In words: their compatible coefficients form exactly the three indicated completions. A different polynomial representative changes the completed coordinates by the displayed three relations. This proves the presentation for the whole inverse limit, not a finite-order approximation.

## 6. Exact image of the reverse trace

Let \(\xi=[p_{E,O}^\vee]\in H^5\operatorname{Hom}_R(P,R)\cong C\) in the current top-wedge frame. Relative to the older convention that called the opposite generator kappa, \(\xi=-\kappa\). Then the raw polynomial covectors act by

\[
T^\vee\longmapsto U_L\xi,\qquad
M_i^\vee\longmapsto-X_i\frac{U_L}{u_i}\xi.
\]

In words: the chamber coefficient is its full normal product. Reading the coefficient of that monomial as the integer one would not be an R-linear map on arbitrary inputs.

Write \(\psi\) for the displayed row. It kills every \(\nu_i\), and hence every \(N_n\). Its exact image in C is

\[
J=(U_L,\ X_0u_1u_2,\ X_1u_0u_2,\ X_2u_0u_1)C.
\]

In words: the ideal includes all four polynomial covectors and all their possible cochain representatives. It is not just a necessary bound on the image.

There is a direct all-polynomial syzygy proof. If

\[
U_La-\sum_iX_i\frac{U_L}{u_i}b_i=0,
\]

reduce modulo \(u_i\). Independence of the variables forces \(b_i=u_ic_i\). Cancelling the nonzero product U-L then gives \(a=\sum_iX_ic_i\). Thus

\[
\ker\psi=N_1.
\]

In words: at order one the generic dual cohomology is exactly the image ideal, with no additional kernel. The checker independently verifies the full syzygy calculation in every squarefree support of the six relevant variables.

For the completed source, the kernel becomes the three completion directions:

\[
0\longrightarrow\bigoplus_i\widehat R_{(u_i)}
\longrightarrow\widehat M_Q\xrightarrow{\psi}J_R\longrightarrow0,
\]

where \(J_R\) is the same ideal before imposing the six short conductor equations. In words: completion adds comparison data killed by this reverse trace; it does not add a covector with value one. After the short-conductor quotient, the image is precisely J above. We do not identify the entire kernel after that nonflat quotient with its underived tensor product.

A simpler image argument avoids any completion convention: the map factors through the order-one projection, so its image is contained in J. Conversely every polynomial covector is constant in the generic top tower and therefore supplies a compatible lift, so every generator of J is obtained. This accounts for all inverse-limit classes and rules out an unobserved unit contribution from them.

There is no contradiction with the earlier primitive fixed-frame calculation. The latter pairs a selected normal line with its dual. The **whole** polynomial map does not land only in the principal line \((U_L)\): its three marked covectors have the smaller complementary products. Dividing the entire map by U-L would introduce forbidden normal inverses or change the module.

## 7. Rees specialization exposes a quadratic generic symbol and a cubic endpoint attachment

Make the explicit product-Rees substitution on the three long directions:

\[
u_i=t_iX_i,\qquad W_L=X_0X_1X_2.
\]

In words: these are the three long occurrences and their three independent Rees parameters. The six short variables retain their separate labels. The checker also verifies the formulas on the full independent product chart for all nine normals. This is a declared coefficient base change, not a claim that a global physical logarithmic span has been constructed.

The trace image becomes

\[
J_{\mathrm{Rees}}=W_L(t_1t_2,t_0t_2,t_0t_1).
\]

In words: every trace value contains the same principal long-occurrence factor. Therefore **this** factor may be paired with its actual dual line without inverting a variable in the base ring.

After that line pairing the row is

\[
\psi_t(T^\vee)=t_0t_1t_2,\qquad
\psi_t(M_i^\vee)=-\prod_{j\ne i}t_j.
\]

In words: the generic chamber begins in total Rees order three, while the marked-normal covectors begin in order two. A scalar normalization that keeps only the chamber misses the lower terms.

The remaining image ideal has the exact polynomial resolution

\[
0\longrightarrow R_t^2
\xrightarrow{\begin{pmatrix}t_0&t_0\\-t_1&0\\0&-t_2\end{pmatrix}}
R_t^3
\xrightarrow{(t_1t_2,\ t_0t_2,\ t_0t_1)}
R_t\longrightarrow R_t/J_t\longrightarrow0.
\]

In words: no denominator or integer division occurs. Reducing a syzygy modulo each t-i forces its i-th entry to contain t-i; the remaining three coefficients sum to zero. This proves exactness for arbitrary polynomials.

Also

\[
J_t=(t_0,t_1)\cap(t_0,t_2)\cap(t_1,t_2).
\]

In words: the trace fails to be a unit along the union of the three long-Rees coordinate axes, including their common origin. This is a parameter-support defect, not an order-two or order-three abelian torsion class.

### The completed Rees generic module

Completion still does not repair the image. After the substitution the independent syzygies of the normalized row are

\[
\nu_i'=T^\vee+t_iM_i^\vee,
\]

and the finite generic relations are \(X_i(t_iX_i)^{n-1}\nu_i'\). In words: the completed kernel has changed from the un-substituted presentation; one must not simply identify those polynomial relation lattices.

The ideals \((X_i(t_iX_i)^{n-1})\) are cofinal with the powers of \((t_iX_i)\). Thus the corresponding completed kernel is again the sum of the three indicated one-normal completions. The normalized trace has exact image J-t at every order and in the inverse limit. The statement is obtained by constructing the Rees tower itself, not by assuming that an underived tensor product commutes with every inverse limit.

## 8. Specialize the whole comparison and both endpoint cells

At finite order one, grade by total degree in the three long normals. Write

\[
\partial_1=d_0+d_1,\qquad F_1=F^{(2)}+F^{(3)},
\qquad A^{(3)}=a_{+,1}f_+-a_{-,1}f_-.
\]

In words: d-zero has long-normal order zero; d-one has order one. The full map has only quadratic and cubic long-normal terms, and both endpoint composites are cubic. Equivalently, introduce a single bookkeeping parameter z multiplying all three long normals while keeping them independent: the full differential is \(d_0+zd_1\) and the map is \(z^2F^{(2)}+z^3F^{(3)}\).

The complete coefficient identities are

\[
d_0F^{(2)}-F^{(2)}\partial_P=0,
\]

\[
d_0F^{(3)}+d_1F^{(2)}-F^{(3)}\partial_P=A^{(3)},
\]

\[
d_1F^{(3)}=0.
\]

In words: the earliest generic symbol is closed, but its next comparison is coupled to both endpoints. The quadratic-to-cubic correction is nonzero. Dropping the quadratic map breaks the cubic endpoint equation; keeping only the quadratic map loses both endpoint attachments.

The term counts are 27 in \(F^{(2)}\), 16 in \(F^{(3)}\), and six in \(A^{(3)}\). These are complete maps on the fifty-column source, not selected matrix entries.

All eight closed long-Rees faces were checked with the entire target differential:

| Zero long-Rees parameters | Full comparison terms | Endpoint-composite terms |
|---|---:|---:|
| None | 43 | 6 |
| Any one | 9 | 0 |
| Any two | 0 | 0 |
| All three | 0 | 0 |

In words: a single central face can retain a marked generic channel while erasing both prescribed endpoint maps. Two central parameters erase this ordinary comparison entirely.

This last vanishing is at chain level in its finite-free representative, not only on a cohomological scalar. The comparison into the localization target is already born at order one. Therefore its ordinary derived base change is zero on those two-parameter faces, and so is the base-changed reverse map obtained by factoring through its finite-free dual. No hidden inverse-limit cochain can change this particular zero morphism into a unit.

A filtered Gysin operation may use the nonzero symbols and connecting degrees above. That is a different morphism. This note does not equate extracting a symbol with ordinary specialization, nor identify a later Gysin value with an unshifted physical coefficient.

## 9. Independent excess and both endpoint frames

The selected five-normal source remains

\[
D_x=K(X_1,X_3,X_5,t_0X_0,t_3X_3),\qquad
\eta_x=t_3h_3^+-h_3^{03}.
\]

In words: the two copies of the shared normal are distinct. The change of basis to the four regular generators and eta-x has determinant minus one and gives

\[
D_x\cong K(X_1,X_3,X_5,t_0X_0)\otimes\Lambda(\eta_x),
\qquad d\eta_x=0.
\]

In words: no normal inverse or multiplicative replacement of eta is needed. All 32 exterior components of this change of basis are checked, and on the selected central Rees face eta becomes the negative pair generator, not zero.

The comparison system and the endpoint identity can be tensored with this independently identified factor. This preserves the equations. It **does not** prove that the physical exceptional/excess functor identifies that factor with an internal target marked normal or with a normal-completion direction.

Likewise the endpoint maps retained here are the native occurrence-resolution maps derived from H. The known spatial collar operators have their own occurrence/normal frames. The present calculation does not replace them by scalar endpoint values, but does not yet identify their fully framed two-cells with these maps after a Gysin operation.

## 10. Verification and sources

Run:

```sh
python check_marici_completed_normal_dual_comparison.py \
  --output marici_completed_normal_dual_comparison_certificate.json
```

The self-contained standard-library checker passes **2,595,690 exact assertions**. It checks the complete finite-free target and native comparison at 49 independent order vectors; all 512 vertices, 2,304 transition arrows, and 4,608 squares of the two-level nine-normal cube; actual dual Hom signs; both endpoint composites; six semilinear transports; all eight central long-Rees faces; the adjacent-order comparison identities; exact generic syzygies in all 64 relevant supports; the three-axis ideal resolution; and the actual selected excess basis change.

The count is an execution statistic, not a replacement for proof. The formulas in Sections 3–8 prove the assertions for arbitrary polynomial degrees, arbitrary normal orders, and the full inverse limit. There was no proof-assistant check. The preceding 19,809-assertion native spatial construction was separately rerun successfully.

No repository files were changed.

### Pinned project inputs

[S1] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: actual target states, coefficients and localization domains.

[S2] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: native source and two-sheet difference.

[S3] `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: fixed labels, support triple and endpoint carriers.

Preceding local artifacts: `marici_joint_conductor_spatial_cap_comparison.md`, `marici_native_spatial_three_extension.md`, and their complete executable checkers. Their scope restrictions remain in force.

### Primary mathematical references

[M1] Stacks Project, *The extended alternating Cech complex*, Lemma 15.30.6, tag `0913`: https://stacks.math.columbia.edu/tag/0913 . The general construction is specialized to the stated face-compatible matrices here.

[M2] Stacks Project, *Hom complexes*, tag `0A8H`: https://stacks.math.columbia.edu/tag/0A8H . The checker uses the actual degree-dependent Hom differential signs.

[M3] Stacks Project, *Rlim of abelian groups*, tag `07KV`: https://stacks.math.columbia.edu/tag/07KV . Surjectivity of the generic cohomology transitions is proved directly above, so the Mittag-Leffler vanishing applies without an assumed completion comparison.
