# Branch C: the physical change-of-rings test

Date: 2026-09-08  
Input retained: `marici_comparison_fibre_adjunction_bar.md` and its checker.  
Target conventions: the supplied 215-state normal-localized hexagon complex at repository commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Result

For the literal source and outer `RHom_A` required in the task, the primitive endpoint column exists and has coefficient one. There is a canonical **reverse restriction-of-scalars comparison**, from native endpoint cochains to the ambient endpoint mapping problem. It sends that primitive column to the primitive column.

It does **not** identify the native operation-bearing model with the ambient physical-source Hom. All nine mixed quadratic endpoint classes become boundaries under this comparison. The eighteen cubic primitives, fifteen quartic primitives and eighty-one ordered quadratic products also become boundaries. This is checked on actual bar cochains, not inferred by replacing the native algebra with its exterior quotient.

Consequently no forward degree-zero comparison with the primitive and operation-orbit values demanded by the task exists in these fixed supports and multidegrees. A homotopy-coherent intertwiner fails at its first quadratic equation. A two-column ambient differential and a one-column native differential give an integral detector taking the required right-hand side to one and every boundary to zero.

This is a falsification of the specified change-of-rings identification, not a theorem against another genuinely native-linear bivariant physical target. The existing line-retaining adjunction comparison remains valid. Its separated operation enhancement is not the literal ambient `RHom_A` computation.

## 1. Rings, derived base change, and frames

Let

\[
C=\mathbb Z[X_{D03},X_{D14},X_{D25},t_0,\ldots,t_5,
 u_{D03},u_{D14},u_{D25}],\qquad A=C[X_0,\ldots,X_5].
\]

In words: the conductor coefficient ring retains all spectator occurrence, short-Rees and long-normal variables. The six short occurrences are the relative polynomial coordinates. Short normal equations are still \(u_i=t_iX_i\).

Put

\[
I_E=(X_0,X_2,X_4),\quad I_O=(X_1,X_3,X_5),
\qquad \mathfrak B=A/(I_EI_O).
\]

The ring maps are

\[
A\xrightarrow{q}\mathfrak B\xrightarrow{\epsilon}C,
\qquad X_i\mapsto\bar X_i\mapsto0.
\]

In words: the first quotient imposes the mixed-monomial relations; the second is the conductor zero section. Spectator coefficients are unchanged. The two branch quotients are

\[
\mathfrak B_+=A/I_E,\qquad \mathfrak B_-=A/I_O.
\]

In words: the plus sheet carries odd occurrences and the minus sheet carries even occurrences. Let \(J_+=I_E\) and \(J_-=I_O\) denote the ideals defining these branch quotients. These should not be confused with the endpoint Rees ideals.

### The mixed relations have not been imposed without their Tor terms

An A-free resolution of the native node has ranks

\[
(1,9,18,15,6,1).
\]

For positive homological degree it has generators \(p_{U,V}\), with nonempty subsets \(U\subseteq\{0,2,4\}\), \(V\subseteq\{1,3,5\}\), and degree \(|U|+|V|-1\). Its first differential is

\[
dp_{\{e\},\{o\}}=X_eX_o.
\]

For higher degrees it is the tensor differential of the truncated even and odd Koszul resolutions:

\[
\begin{aligned}
dp_{U,V}={}&
\sum_{e\in U,\ |U|>1}(-1)^{\operatorname{pos}_U(e)}X_e p_{U\setminus e,V}\\
&+\sum_{o\in V,\ |V|>1}
(-1)^{|U|-1+\operatorname{pos}_V(o)}X_o p_{U,V\setminus o}.
\end{aligned}
\]

In words: the resolution is obtained from the product of two coordinate ideals in disjoint variables, with the product inclusion appended. Each variable set is regular over the spectator ring. Tensoring the resolutions of the two ideals is exact over C and gives the product ideal; the augmentation then resolves the node. The checker verifies the polynomial differential and every degree.

After derived conductor base change every displayed differential becomes zero. Thus

\[
\operatorname{rank}_C\operatorname{Tor}^A_n(\mathfrak B,C)
=(1,9,18,15,6,1)_n.
\]

In words: all the relation and higher-syzygy Tor terms are retained. For \(n\ge1\), their occurrence weight is \(n+1\). In particular each mixed relation contributes a degree-one Tor generator of weight \(e_{X_e}+e_{X_o}\). Nothing in this calculation asserts that the resulting derived coinduced **B-action** is formal or splits into these groups.

### The complete endpoint Gysin source

For each of the four underlying T and its separately retained excess label, keep

\[
P_T=K_A(X_0,\ldots,X_5,p_T),\qquad p_T=\prod_{i\in T}t_i,
\]

\[
I_+=(1,3,5),\quad I_-=(0,2,4),\quad
D_\sigma=\operatorname{Hom}_A(K_A(t_{I_\sigma}),A),
\]

\[
\widetilde L_\sigma=A\ell_\sigma,\quad
\deg\ell_\sigma=\sum_{i\in I_\sigma}e_{t_i},\qquad
G_{\sigma,T}=(P_T\otimes D_\sigma\otimes\widetilde L_\sigma)
\langle\lambda_T\rangle[-4],
\]

\[
\lambda_T=\gamma-\sum_{i=0}^5e_{X_i}-\sum_{i\in T}e_{t_i},
\qquad \gamma=\sum_{\ell\in\{D03,D14,D25\}}e_{u_\ell}.
\]

In words: all seven coefficient equations, the ordered six-occurrence determinant, the product-Cartier line, the dual endpoint normal block, and the external endpoint conormal are present. This is exactly the previous framed source. There is no Euler evaluation. Its coefficients are polynomial.

The endpoint target \(V_\sigma\) retains its eight actual states. An inverse is permitted only at an unmarked endpoint label:

\[
(V_\sigma)_{[v_\sigma,H]}=
A[(t_iX_i)^{-1}:i\in I_\sigma\setminus H].
\]

In words: these are the original target coefficient domains. No new ambient occurrence inverse is introduced.

Every construction below is multigraded. Tensor products over C are taken in the full multigraded coefficient envelope **before** selecting a frame. A single isolated homogeneous group is not a C-module with arbitrary spectator multiplication merely because it has been named \(C_\sigma\).

## 2. The correct nested Hom and its coefficient object

Let \(P_\sigma^{\rm nat}\) be the complete native relative bar resolution supplied in the task. Put

\[
\mathcal H_\sigma=R\operatorname{Hom}_A(G_{\sigma,T},V_\sigma),
\qquad
\mathcal L_\sigma=
R\operatorname{Hom}_A(P_\sigma^{\rm nat}\otimes_A^L G_{\sigma,T},V_\sigma).
\]

Tensor-Hom adjunction and the right adjoint to restriction of scalars give

\[
\begin{aligned}
\mathcal L_\sigma
&\simeq R\operatorname{Hom}_A(P_\sigma^{\rm nat},\mathcal H_\sigma)\\
&\simeq R\operatorname{Hom}_{\mathfrak B}
\left(P_\sigma^{\rm nat},
R\operatorname{Hom}_A(\mathfrak B,\mathcal H_\sigma)\right).
\end{aligned}
\]

In words: the correct native target is the **derived coinduced coefficient object** \(R\operatorname{Hom}_A(\mathfrak B,\mathcal H_\sigma)\). It is not the conductor C, and is not replaced by the endpoint homogeneous line. In an injective model its B-action is precomposition by multiplication on B. This retains the Tor and higher change-of-rings structure.

All arrows here have cohomological and internal degree zero. Restriction of scalars is covariant; the Hom argument in the source is contravariant. The displayed adjunctions do not alter support, endpoint labels, or determinant lines.

### A valid coefficient reduction, with proof

Write \(K_X=K_A(X_0,\ldots,X_5)\), and separate it from the other factors of G. Let \(L_X\) be its ordered determinant line. Since every term of V is a flat localization of A,

\[
K_X^\vee\otimes_A V_\sigma
\longrightarrow
(C\otimes_A V_\sigma)\otimes_A L_X^\vee[-6]
\]

is a quasi-isomorphism. It is the full Koszul purity projection, not a deletion of lower coefficient terms without a comparison. Tensoring with the other finite dual source factors preserves it.

After tensoring V with C, all unmarked short-localization summands vanish; the fully marked endpoint remains. Thus this projection gives a C-complex \(W_\sigma\) and an A-linear quasi-isomorphism

\[
\mathcal H_\sigma\xrightarrow{\simeq}W_\sigma.
\]

In words: the endpoint Koszul, product-Cartier, conormal, and long-normal factors remain inside W. In its prescribed Rees/long-normal frame it has just the primitive normalized degree-zero component. All its cohomology has short-occurrence degree zero. This assertion is proved using the complete six-occurrence Koszul factor; it is not a claim of formality for the native bar algebra.

A useful explicit expression, with v treated as a degree-zero line of the fully marked endpoint weight, is

\[
W_\sigma=
K_A(p_T)^\vee\otimes_A K_A(t_{I_\sigma})\otimes_A
\widetilde L_\sigma^\vee\otimes_A Cv_\sigma\otimes_A
L_X^\vee\langle-\lambda_T\rangle[1].
\]

In words: this formula retains every shift. In the designated frame, the product-Cartier dual top state and the empty endpoint-normal wedge are the surviving row; its coefficient is \(U_L\).

The checker projects onto the fully occupied six-occurrence input and the fully marked target and verifies that its kernel is integrally acyclic. It does this for the complete physical Hom complexes, not only for their reduced cohomology.

## 3. Compute the literal derived tensor source

As an A-complex, the native bar resolution is quasi-isomorphic to its branch quotient \(\mathfrak B_\sigma\). Since G is a bounded free A-complex, its tensor preserves this quasi-isomorphism. To compute the **outer derived Hom over A**, an A-projective replacement is required; the B-free bar is not assumed A-projective.

Use

\[
Q_\sigma^A=K_A(J_\sigma),
\qquad
Q_\sigma^A\otimes_A G_{\sigma,T}.
\]

In words: Q is the actual three-equation A-free branch resolution. The complete tensor has 8,192 generators before normalization. Replacing the underlying A-complex this way is legitimate only for the stated outer \(R\operatorname{Hom}_A\); it is not an assertion that native operations are unchanged under restriction of rings. Their change is computed separately below.

After the verified endpoint purity projection,

\[
\mathcal L_\sigma\simeq
\operatorname{Hom}_A(Q_\sigma^A,W_\sigma)
\cong W_\sigma\otimes_C
\Lambda_C\langle\epsilon_j:j\in J_\sigma\rangle.
\]

Each \(\epsilon_j\) has cohomological degree one and internal occurrence degree \(-e_{X_j}\). In words: the actual ambient problem has three exterior comparison directions corresponding to the coordinates killed on that sheet. The last isomorphism follows from a finite A-free resolution with explicit module structures: the variables in its differential act as zero on W. It is not a Kunneth substitution for the original native Hom.

Consequently, in the prescribed Rees/long-normal frame,

\[
H^q(\mathcal L_\sigma)_{-\alpha}=
\begin{cases}
\mathbb Z,&\alpha=\sum_{j\in S}e_{X_j},\ S\subseteq J_\sigma,\ q=|S|,\\
0,&\text{otherwise}.
\end{cases}
\]

In words: every mixed even-odd operation weight has **zero entire physical mapping cohomology**. The primitive weight has one normalized degree-zero class. This is an all-replacement result; larger polynomial exponents cannot change a fixed fine weight.

## 4. The primitive column passes

There is a source-defined multiplication map

\[
\mu_\sigma:
Q_\sigma^A\otimes_A G_{\sigma,T}\longrightarrow G_{\sigma,T}.
\]

On the two occurrence-Koszul factors it sends

\[
e_J\otimes e_I\longmapsto e_J\wedge e_I,
\]

and it is the identity on the product-Cartier, dual-normal and conormal factors. In words: the branch-resolution generators map to the matching occurrence generators already in G. The differential and internal degrees agree because both copies have differential \(X_j\). Repeated wedges give zero, with the usual ordered signs. No parameter is evaluated.

If \(\nu_\sigma\) is the established eight-row endpoint cocycle, then

\[
\nu_\sigma^{A}=\nu_\sigma\mu_\sigma
\]

is a closed **64-row** representative in the actual ambient derived Hom. Its empty branch-Koszul column is exactly \(\nu_\sigma\), and its top framed coefficient is one. The same coefficient is an integral detector annihilating every incoming boundary. The primitive map is therefore \([1]\), not zero or a nonunit multiple.

All four underlying T, both endpoints, and the original/full central short-Rees fibres were computed. The two excess labels remain distinct external lines and pass through identically; they are not identified as source objects.

## 5. The primitive forward map and the canonical reverse change-of-rings arrow

There is an elementary forward comparison which passes the primitive test. The unit of the branch resolution is the chain map

\[
\iota_\sigma:G_{\sigma,T}\longrightarrow Q_\sigma^A\otimes_A G_{\sigma,T},
\qquad g\longmapsto1\otimes g.
\]

In words: its differential is compatible because the empty branch-Koszul wedge is closed. Precomposition followed by the native augmentation cochain gives

\[
\chi^0_\sigma(f)=(f\iota_\sigma)\otimes m_\sigma.
\]

Its matrix is identity on empty branch-Koszul input columns and zero on nonempty input columns, tensored with the closed native degree-zero cochain. Since \(\mu_\sigma\iota_\sigma=1\),

\[
\chi^0_\sigma(\nu^A_\sigma)=\nu_\sigma\otimes m_\sigma.
\]

In words: the demanded primitive value is obtained without Euler evaluation, a determinant mismatch or a support change. This forward map does **not** intertwine the native mixed operations; Section 6 proves that no homotopic or higher-coherent replacement with this primitive value can do so in the required frames.

Let

\[
N_\sigma=R\operatorname{Hom}_{\mathfrak B}(\mathfrak B_\sigma,C),
\qquad N_\sigma^A=R\operatorname{Hom}_A(\mathfrak B_\sigma,C).
\]

Restriction of scalars gives a canonical degree-zero map

\[
\operatorname{res}_\sigma:N_\sigma\longrightarrow N_\sigma^A.
\]

It is constructed at chain level from the normalized ambient-to-native bar map

\[
A\otimes_C\bar A^{\otimes n}\otimes_C\mathfrak B_\sigma
\longrightarrow
\mathfrak B\otimes_C\overline{\mathfrak B}^{\otimes n}\otimes_C\mathfrak B_\sigma.
\]

In words: apply the quotient A to B to each bar entry. An entry containing a mixed monomial maps to zero. Precomposition extends a native cochain by zero on those ambient slots. Both actual differentials and the endpoint tail actions are retained.

Using W gives the correctly varianced derived arrow

\[
W_\sigma\otimes_C N_\sigma
\xrightarrow{1\otimes\operatorname{res}_\sigma}
W_\sigma\otimes_C N_\sigma^A
\simeq \mathcal L_\sigma.
\]

In words: this is a genuine reverse comparison, and the primitive maps to \(\nu_\sigma^A\). It is a **quotient on operation cohomology**, not a physical identification of the two operation-bearing objects. In the original models the verified purity projections give the corresponding derived zigzag. No strict inverse of a nontrivial chain map is assumed.

The separated construction does have a correctly typed interpretation, but over the **native ring**:

\[
W_\sigma\otimes_C N_\sigma\simeq
R\operatorname{Hom}_{\mathfrak B}(\mathfrak B_\sigma,W_\sigma),
\]

with B acting on W through its conductor augmentation. Here W is bounded and C-perfect, and each retained graded bar weight is finite, so the evaluation/tensor map is checked with matching module structures. In contrast, the literal ambient problem is

\[
\mathcal L_\sigma\simeq
R\operatorname{Hom}_{\mathfrak B}
\left(\mathfrak B_\sigma,R\operatorname{Hom}_A(\mathfrak B,W_\sigma)\right).
\]

In words: the reverse comparison is induced by the coinduction unit
\(W_\sigma\to R\operatorname{Hom}_A(\mathfrak B,W_\sigma)\). The two coefficient targets are not interchangeable. This unit cannot have a retraction on the prescribed primitive native operation orbit, as the next calculation proves. Keeping native linearity gives a different, well-defined coefficient mapping problem; its physical identification is not supplied by the requested outer A-Hom.

## 6. The first unsolvable equation is explicit

Work on the plus sheet. Set \(x=X_1\) and \(y=X_0\). Thus x survives on the sheet and y is killed. In occurrence weight \(e_x+e_y\), the ambient endpoint bar cochains have bases

\[
C_A^1=\mathbb Z\{a=[xy]^*,\ b=([y]\mid x)^*\},
\qquad
C_A^2=\mathbb Z\{c=[y\mid x]^*,\ d=[x\mid y]^*\}.
\]

Their differential is

\[
\delta_A=
\begin{pmatrix}-1&1\\-1&0\end{pmatrix}.
\]

In words: the mixed ambient monomial supplies the first column. This matrix is unimodular, so the whole mixed-weight ambient block is acyclic.

In the native node, xy is zero. The cochain a does not exist, while b remains. Its differential is

\[
\delta_{\mathfrak B}=\begin{pmatrix}1\\0\end{pmatrix}.
\]

In words: the native block has a primitive degree-two class detected by its d-coordinate. The mixed operation on the native endpoint unit is

\[
r_{00}m_+=c+d,
\qquad
\delta_A(-a)=c+d.
\]

In words: the **same operation is nonzero natively and explicitly exact in the actual ambient comparison**. The primitive native detector \(\ell(c)=0,\ell(d)=1\) takes it to one and kills every native boundary. Reversing the sheet gives the same calculation with the surviving and killed variables interchanged.

The bar cochains use the standard transposed homological bar boundary. To compare to \(\partial f=d_Yf-(-1)^{|f|}fd_X\), multiply degree-n bar cochains by \((-1)^{n(n+1)/2}\). This is a diagonal signed-unit change, and leaves the obstruction and all integral ranks unchanged. In degree one the displayed nullhomotopy equation already has the stated sign.

Suppose a forward \(\chi_\sigma\) had the requested primitive value and intertwined the mixed operation up to a homotopy. The physical mixed operation class is exact, so the chain-map and intertwiner equations would imply

\[
\partial k=\nu_\sigma\otimes r_{00}m_\sigma.
\]

The tensor of the fully marked endpoint detector with \(\ell\) gives

\[
0=1.
\]

In words: no such comparison homotopy exists. This proves failure for every replacement representative and every higher-coherent extension with the same first operation equation. Equivalently, the entire physical homogeneous Hom at this mixed weight is acyclic, whereas the demanded separated target has a primitive nonzero class.

An arbitrary chain map forgetting the operation requirement is not ruled out. The reverse quotient above is also not ruled out. Neither supplies the requested primitive-and-orbit physical identification.

## 7. All required operation classes and reflection terms

For all nine quadratics, let \(\psi_{ij}\) be the ambient one-bar cochain evaluating the mixed monomial. Then

\[
\delta(-\psi_{ij})=\xi_i\smile\eta_j+\eta_j\smile\xi_i.
\]

In words: each first obstruction has an explicit ambient homotopy. These cochains do not exist in the native bar.

The higher homotopies are also explicit. If \(\delta h=r\) and \(a\) is an odd, closed letter cochain, then

\[
\delta(-[a,h])=[a,r].
\]

For two closed quadratics \(r,s\),

\[
\delta(h_rs)=rs,\qquad h_{rs}=h_r\smile s.
\]

In words: the same formula constructs the homotopies for all nested cubic and quartic primitives and all ordered quadratic products. They are verified in the complete ambient bar differential, including the endpoint action. The native cochains are not replaced by a zero-differential cohomology presentation.

Per endpoint, the computed results through occurrence weight four are:

| Operation family | Independent native classes | Ambient images | Explicit nullhomotopies |
|---|---:|---:|---:|
| Quadratic primitives | 9 | 0 | 9 |
| Cubic primitives | 18 | 0 | 18 |
| Quartic primitives | 15 | 0 | 15 |
| Ordered quadratic products | 81 | 0 | 81 |

The ambient and native endpoint cohomology ranks are respectively

\[
(1,3,3,1,0),\qquad (1,3,12,46,177).
\]

In words: the difference is not a missing orientation unit. The two rings give different comparison modules. Through degree four the positive relative unit orbit has native ranks 9, 18 and 96 and zero image. The canonical restriction retains the exterior three-generator quotient and the primitive unit.

The literal six labelled permutations commute with both bar differentials and the restriction map. In the operation labels used by the retained checker, \((\xi_0,\xi_1,\xi_2)\) correspond to \((X_1,X_3,X_5)\), and \((\eta_0,\eta_1,\eta_2)\) to \((X_0,X_4,X_2)\). Reflection exchanges these triples. The complete equation

\[
s(W)=-W+[r_{11},r_{00}],\qquad W=[\xi_1,[\eta_1,r_{00}]]
\]

is verified on actual cup cochains. Its decomposable term is nonzero at both native endpoints and is ambient-exact. It has not been discarded by passing to indecomposables. Thus labelled transport cannot repair the change-of-rings failure.

## 8. What can and cannot be exported as a physical square

There is a true naturality square for the line-retaining counit and restriction of scalars. In reduced framed models it is the square with horizontal maps the identity, vertical maps \(\operatorname{res}_\sigma\), and zero boundary homotopy. On unreduced models it is represented by the natural bar restriction and the complete purity quasi-isomorphisms; the line-retaining counit is never Euler-evaluated.

This square is a **restriction-of-scalars square**, not the required physical square with a primitive operation-preserving forward b. On its primitive column the vertical matrix is \([1]\). On the 123 nonunit relative orbit columns it is zero on cohomology, with all corresponding ambient homotopies supplied in the certificate.

For a forward square whose b is required to send the physical primitive orbit to the native primitive orbit, its first quadratic column would have to solve the equation in Section 6. It has no solution. Therefore the requested a,p,b,c matrices cannot all be supplied with those values and the specified rings. No extra cone is introduced to force them.

The existing candidate \(H^1=0\), \(H^0=\mathbb Z^2\), and negative automorphism groups are **not** reassigned to the physical problem. A complete physical control complex with the demanded b has not been defined because that b fails the first operation equation. The Q-morphism gate and derived cyclic constructions therefore have not been reached.

### The minimal missing structural datum

The first missing information is the native action of the mixed relation classes, already recorded by the nine degree-one Tor terms of \(\mathfrak B\otimes_A^L C\). The correctly nested Hom with **coinduced coefficients** retains this structure, but it is adjoint to the same ambient problem and does not remove the obstruction.

To obtain a different answer requires a genuinely native-linear supported endpoint coefficient object and a typed bivariant comparison to it, or another specified operation using those change-of-rings classes while altering the present Hom problem. It cannot be obtained by simply declaring the coinduced coefficient object to be C, using Euler evaluation, or giving the ambient exterior quotient the nonzero native mixed action by hand. No new physical cells or parity choice are justified by this calculation.

## 9. Executable verification

Run:

```sh
python check_marici_physical_change_of_rings.py --output marici_physical_change_of_rings_certificate.json
```

The self-contained standard-library checker passes **1,735,966 exact assertions**. Its new finite calculations include:

- the complete fifty-generator ambient resolution and all native Tor degrees;
- 80 complete homogeneous physical Hom calculations: four T, two endpoints, the primitive and all nine mixed weights (123,336 columns in total);
- explicit 64-row primitive endpoint cochains, their stalk domains and full differential equations;
- original and full central primitive calculations and all 64 face coefficient-admissibility checks;
- all monomial multidegrees of total occurrence weight at most four, at every bar length, for both rings and endpoints;
- 5,161 native and 7,624 ambient endpoint cochain columns per endpoint;
- the literal restriction-of-scalars chain map, integral contractions, all 246 endpoint orbit nullhomotopies, and the decomposable reflection equation.

A second complete run with a different Python hash seed reproduced all substantive matrices, classes, ranks and homotopies; its additional source-unit checks are included in this count.

The small bar matrices are exported explicitly, as are representative full endpoint cochains and every requested ambient orbit homotopy. Larger polynomial exponents cannot affect the tested homogeneous bar weights. The all-degree physical vanishing follows from the proved Koszul purity reduction, not extrapolation from these finite counts.

This is executable exact verification together with the algebraic arguments above, not proof-assistant certification. No repository files were modified.

## References and provenance

1. Supplied `marici_comparison_fibre_adjunction_bar.md`, especially Sections 1, 4 and 10: actual coefficients, native bar, and the unresolved tensor-Hom comparison. Its helper code is reproduced inside the new self-contained checker; no old certificate counts are imported.
2. Supplied target rules originating in `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`; native normalization ring from ledger entry 93.
3. Stacks Project, *Hom complexes*, tag `0A8H`, especially the tensor-Hom chain adjunction and signs: https://stacks.math.columbia.edu/tag/0A8H.
4. Stacks Project, *The Koszul complex*, tag `0621`: https://stacks.math.columbia.edu/tag/0621.
5. Stacks Project, regular sequences are Koszul regular, tag `062F`: https://stacks.math.columbia.edu/tag/062F.

The reverse comparison, primitive lift and mixed obstruction in this note are new calculations for the exact task. No external theorem identifying the physical collar with the ambient Hom is assumed.
