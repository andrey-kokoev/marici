# A source-relative excess trace from the supported maps to the bare target

Project: Marici  
Date: 2026-09-08  
Pinned repository input: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`  
Immediate input: `marici_supported_endpoint_class_test.md` and its executable construction.

## 1. Result and scope

All eight previously constructed complete supported maps have a primitive image in the **bare** seven-state generic quotient Q, without a remaining raw-normal/excess tensor factor. The image is a degree-four derived morphism from the complete seven-equation supported Koszul source. It is not a degree-zero augmentation of the auxiliary factor, and it is not yet an identification with an independently prescribed physical collar source.

The operation is defined on the **entire source-target Hom complex**, not only on the eight distinguished cohomology classes. For a quadratic channel, a partial exterior trace fails to be a chain map on the auxiliary factor. The existing occurrence-Koszul multiplication homotopy supplies its precise correction. This correction is necessary on general cochains even though it evaluates to zero on the particular closed representatives constructed previously.

After their ordered determinant signs are retained, all eight output matrices are the same 45-term complementary-face map on 18 source columns. Their source Cartier equations and their trace degrees are different; equality of the coefficient matrices does not identify those different input objects.

Both endpoint composites remain exact. The unclosed map has 43 terms and its endpoint differential has six terms. Two explicit endpoint-supported correction terms close it, leaving 45 terms. The full pair and triple comparisons between endpoint nullhomotopies are transported as well.

In every prescribed output frame, the Hom complexes to K, E, and Q have exactly one integral class in degree four, while the complexes to the short support B and endpoint support V are acyclic. Consequently, fixing the whole resulting generic class gives a contractible relative lift space. This remains a statement about the specified source and frame, not an assignment of physical reflection parity.

## 2. Fixed source, auxiliary factor, and coefficients

Work on the same polynomial graph chart as the preceding calculation:

\[
A=\mathbb Z[X_0,\ldots,X_5,X_{D03},X_{D14},X_{D25},
 t_0,\ldots,t_5,u_{D03},u_{D14},u_{D25}].
\]

In words: short occurrences, short Rees parameters, long occurrences, and long normals remain separate. For the short directions only, the graph equation is \(u_i=t_iX_i\). No long-Rees specialization or nonhomogeneous monodromy specialization is made here.

Set \(O=(1,3,5)\), \(\tau=t_1t_3t_5\), and use the checked split basis of the actual repeated-normal source:

\[
D_u=K_A(t_1X_1,t_3X_3,t_5X_5,t_0X_0)\otimes\Lambda(\eta_u).
\]

In words: there are four ordinary normal generators and one independent excess generator with zero differential. Their order is \((h_1,h_3,h_5,h_0,\eta_u)\). This is an integral change of basis of the prescribed five-normal complex, not a new source generator. The weight of \(\eta_u\) is the weight of the repeated third normal, \(e_{X_3}+e_{t_3}\).

The auxiliary output used previously is

\[
L=\operatorname{Cone}(D_u\longrightarrow D_u[\tau^{-1}]).
\]

In words: retain both the localized arm and the shifted unlocalized arm. In homological grading,

\[
L_n=(D_u[\tau^{-1}])_n\oplus(D_u)_{n-1},\qquad
 d_L(v,w)=(d_uv+w,-d_uw).
\]

In words: the off-diagonal localization inclusion and the minus sign on the raw arm are part of the differential.

For \(T\subseteq O\) with \(|T|=2\) or \(3\), let

\[
t_T=\prod_{i\in T}t_i,\qquad S_T=A/(X_0,\ldots,X_5,t_T),\qquad
\mathcal K_T=K_A(X_0,\ldots,X_5,t_T).
\]

In words: use the full 128-generator free resolution, including its product-Cartier generator \(z_T\). The seven equations are a regular sequence in the stated polynomial ring; their product equation need not be irreducible to be a non-zero-divisor after the six occurrence equations.

The previous maps, indexed by \(\epsilon=0,1\), were

\[
F_{T,\epsilon}:\mathcal K_T\longrightarrow K\otimes L,
\qquad |F_{T,\epsilon}|=|T|+\epsilon-2,
\qquad \mathsf D F_{T,\epsilon}=A_{T,\epsilon}.
\]

In words: the last symbol is the coupled signed endpoint composite, not the coefficient ring A. The prior calculation constructed endpoint homotopies and a closed representative \(\widetilde F_{T,\epsilon}\).

The target K retains all 215 original states, their differential and their individual coefficient domains. The support filtration is \(V\subset B\subset K\), with \(E=K/V\) and \(Q=K/B\). On a marked short state, the corresponding inverse is forbidden. On an unmarked state its allowed normal localization also allows the corresponding factors on the Rees graph. None of these domains is enlarged by the new operation.

## 3. Why an ordinary factor counit is the wrong operation

Let \(J=(t_1X_1,t_3X_3,t_5X_5,t_0X_0)\), let \(N\) be the ordered four-normal line bundle of the first four source generators, and let \(E_\eta\) be the independent excess line. The four equations form a regular sequence. Ordered Koszul self-duality therefore gives two cohomology modules for the raw dual, in degrees four and five.

The cone L is the support complex of \(D_u\), shifted by one. The Čech description of derived completion gives

\[
R\operatorname{Hom}_A(L,A)
\simeq
R\operatorname{Hom}_A(D_u,A)\otimes_A\widehat A_{(\tau)}[-1].
\]

In words: the complete factor-dual problem includes the actual derived localization contribution. Since A is Noetherian, its completion is flat, so the perfect four-equation dual may be tensored with ordinary completion. This formula follows from the support-completion adjunction in [M3]; it is not inferred from a finite normal-order sample.

Consequently,

\[
\begin{aligned}
\operatorname{Ext}^5_A(L,A)&\cong
\widehat{A/J}_{(\tau)}\otimes\det(N)^\vee,\\
\operatorname{Ext}^6_A(L,A)&\cong
\widehat{A/J}_{(\tau)}\otimes\det(N)^\vee\otimes E_\eta^\vee,
\end{aligned}
\]

and every other Ext group vanishes. In words: factor traces require the full ordinary normal wedge, with or without the independent excess, and the support-cone shift. In particular there is no degree-zero scalar counit.

The two primitive polynomial representatives read the raw-cone coefficients of \(h_1h_3h_5h_0\) and \(h_1h_3h_5h_0\eta_u\), respectively. They vanish on the localized arm. The checker composes both with each complete previous map: both give zero on the six quadratic channels; each gives the matching cubic channel and kills the opposite excess channel. This tensor-factor result is **not** a no-go for a source-dependent operation.

For comparison, after all three branch Rees parameters vanish, the primitive factor-dual classes occur in degrees two through six with ranks \((1,4,6,4,1)\). The new lower-degree traces at this special fibre do not automatically extend to the full family. The central table is obtained from \(K(t_0X_0)\) and the four closed exterior generators; all eight partial central faces are checked. No central-only trace is used to define the construction below.

## 4. Construct the source-relative trace on all cochains

For the selected channel let I denote the ordered raw wedge \(h_T h_0\eta_u^\epsilon\), and set

\[
\ell=-|I|-1=-|T|-\epsilon-2.
\]

In words: its trace degree includes both the raw exterior degree and the one-degree shift of the support cone. The dual exterior line is retained, so evaluating the excess-labelled channel is not an assertion that \(\eta_u\) was a scalar.

Let \(\lambda_I\) be the A-linear coefficient functional on L that reads precisely the raw I component, sends it to one, and is zero on all other components and the entire localized arm. This is extraction of a **specified module basis coefficient**, not extraction of a monomial from A. It is A-linear.

For a cubic channel, this is a closed graded morphism. For a quadratic channel, let m be the omitted branch label, put \(J'=I\cup\{h_m\}\) in the original raw order, and define

\[
c=(-1)^{\ell+\operatorname{pos}_{J'}(h_m)},\qquad
\mathsf D\lambda_I=c\,t_mX_m\lambda_{J'}.
\]

In words: the single omitted normal is exactly the chain defect of the partial trace. The position is numbered from zero. The defect is nonzero on the full polynomial source; it cannot be ignored because the distinguished map happens to avoid its test row.

The input \(\mathcal K_T\) supplies left wedge multiplication \(w_m\) by its occurrence generator. Its intrinsic Koszul identity is

\[
dw_m+w_md=X_m\operatorname{id}.
\]

In words: the full occurrence source already provides the required multiplication homotopy [M1]. No new filling cell or inverse is introduced.

For a homogeneous map f of homological degree n into \(K\otimes L\), write \(T_I=1_K\otimes\lambda_I\), including the tensor sign \((-1)^{\ell|k|}\). Define

\[
\mathscr R_n(f)=
T_If+c(-1)^{\ell+n}t_m\,T_{J'}f w_m.
\]

In words: add the exactly prescribed source-wedge correction to the partial trace. For a cubic channel, the second term is absent. Its coefficient is polynomial. Its fine degree is the same as the first term, because the missing raw normal has weight \(e_{X_m}+e_{t_m}\), precisely compensated by \(w_m\) and \(t_m\).

The complete Hom-complex equation is

\[
\mathsf D\mathscr R_n(f)=(-1)^\ell\mathscr R_{n-1}(\mathsf Df).
\]

In words: this is a graded chain operation on the **whole mapping complex**, hence it transports morphisms, homotopies and their higher comparisons. It is natural in the untouched target and preserves each target support subcomplex.

Proof: expand the Hom differential using [M2]. The differential of the first term contributes \(ct_mX_mT_{J'}f\). The differential of the source-wedge term contributes its negative, because \(\mathsf Dw_m=X_m\). The remaining terms have coefficient \((-1)^\ell\) and are exactly the operator applied to \(\mathsf Df\). Tensor signs cancel the untouched target differential independently. This proves the identity for arbitrary polynomial coefficients and all allowed localization terms.

The executable checks all 16,384 monomial-free elementary source/raw Hom rows for each channel, including both target parities. In every quadratic channel the uncorrected operation fails on 256 rows; the corrected operation passes on all rows. The correction is nonzero on 128 elementary rows per quadratic channel. On the particular previously constructed closed maps, the correction itself evaluates to zero. Keeping it is nevertheless essential for a valid operation on their entire comparison complexes.

## 5. The resulting map has no auxiliary target factor

Apply \(\mathscr R\) to the closed supported cap, with the sign fixed by the ordered top wedge:

\[
\mathcal G_{T,\epsilon}
=(-1)^{|T|+1}\mathscr R(\widetilde F_{T,\epsilon}).
\]

In words: this is now a map into K itself. The raw normal, the excess exterior factor, and the shifted localization-cone arm have been evaluated in their recorded trace degree; they are not left tensored with Q.

Every channel has homological map degree minus four, and fine degree

\[
\lambda_T=
\gamma-\sum_{i=0}^5e_{X_i}-\sum_{i\in T}e_{t_i},
\qquad
\gamma=e_{u_{D03}}+e_{u_{D14}}+e_{u_{D25}}.
\]

In words: all six occurrence conormals, the product-Cartier degree and the three-long-normal frame are still present. The two excess sectors reach this common frame through trace degrees differing by one and through different dual excess factors.

The top source value is

\[
\mathcal G_{T,\epsilon}(e_0\wedge\cdots\wedge e_5\wedge z_T)
=\omega,
\qquad
\omega=U_LT-\sum_{\ell\in\{D03,D14,D25\}}
X_\ell\frac{U_L}{u_\ell}M_\ell.
\]

In words: the image is the actual corrected generic cycle with coefficient plus one in its fixed normal frame. Each displayed quotient \(U_L/u_\ell\) is a polynomial product of the other two long normals. This is not an unrestricted scalar trace taking the polynomial coefficient U to one.

The full output has 45 terms on 18 of the 128 source columns. The unclosed output has 43 terms. Its six-term endpoint differential is removed by two endpoint-supported terms, one on each actual endpoint. The checker stores every coefficient and source/target label.

After these ordered signs, all eight coefficient matrices agree exactly. They vanish on every source wedge not containing \(z_T\). Equivalently, they factor through the canonical cone projection onto the shifted six-occurrence Koszul source, followed by the same 45-term degree-three complementary-face Gysin map. The latter map is independently checked against all six occurrence differentials. This factorization explains the matrix equality without identifying the different Cartier equations \(t_T\).

It also supplies a negative control: deleting the product-Cartier input does not leave a primitive ordinary marking; the restricted map is zero.

### The operation is a trace, not a faithful equivalence

In four earlier frames, the raw repeated-normal generator and \(\eta_u\) had the same fine weight, producing a rank-two group of generic classes. The source-relative operation retains the designated exterior mode and annihilates the other mode. The old-to-new purity maps are checked on every column. Their ranks are one; their kernel ranks are zero or one as appropriate.

This neither makes two distinct source states homotopic nor creates an order-two parity. It is the ordinary information loss of a labelled trace. The excess-labelled sector is evaluated against its own dual line, not replaced by the repeated normal.

## 6. Complete bare-target mapping spaces

The seven input equations are regular, and every target term is flat over A. Ordered Koszul purity identifies the complete Hom complex with top evaluation into the derived support restriction, retaining the seven-degree shift and determinant.

After setting the six short occurrences and \(t_T\) to zero, a target state with any unmarked short coordinate disappears because it inverts that occurrence. A fully marked nonempty short face would require a negative short-Rees coefficient in the prescribed output degree, which its stalk forbids. Thus the surviving homogeneous quotient contains exactly the seven generic states.

Their three signed-unit marked-normal-to-facet differentials contract onto the line generated by \(\omega\). Hence

\[
\operatorname{Ext}^j_A(S_T,K)_{\lambda_T}
\cong\operatorname{Ext}^j_A(S_T,E)_{\lambda_T}
\cong\operatorname{Ext}^j_A(S_T,Q)_{\lambda_T}
\cong
\begin{cases}\mathbb Z,&j=4,\\0,&j\ne4,
\end{cases}
\]

while the Hom complexes to B and V are acyclic. In words: the bare target has one primitive class and no hidden short-support or endpoint ambiguity in this exact frame.

These conclusions are independently verified by full integral cancellation, not only by the purity proof. Before specialization, the full K Hom complex has 235 columns for a quadratic channel and 223 for a cubic channel. Their endpoint subcomplex has 24 columns and is acyclic. The actual Q Hom complex has seven columns and three cancellations. Full reductions are performed for every channel before specialization, on the branch Rees center, and on the full six-short-Rees center. In total, 2,560 full K Hom columns and all their subquotient complexes are constructed and reduced.

The map is nonzero and primitive in each reduction. Naturality of top evaluation identifies the maps induced by K to E to Q with the identity on this primitive line. Thus the homotopy fibre at a specified complete generic morphism is contractible. This is a degree-four **derived morphism** statement, not a claim about an unshifted scalar state.

On central faces where \(t_T\) becomes zero, its Koszul generator is retained. The six-occurrence purity argument applies with that remaining exterior input. The source arm without \(z_T\) requires negative Rees degree and contributes nothing. This proves the same class statement there without incorrectly treating a zero equation as regular.

## 7. Endpoints, specialization and labelled transport

The source-relative operator is a Hom-chain map and does not change target support. Applying it to the unclosed cap, the endpoint composites and the endpoint nullhomotopies therefore gives

\[
\mathsf D\mathcal G^{\mathrm{raw}}_{T,\epsilon}
=\mathcal A'_{T,\epsilon},\qquad
\mathsf D\mathcal H'_{T,\epsilon}
=\mathcal A'_{T,\epsilon},\qquad
\mathcal G_{T,\epsilon}
=\mathcal G^{\mathrm{raw}}_{T,\epsilon}-\mathcal H'_{T,\epsilon}.
\]

In words: both endpoint composites are retained in the equation, and both remain exact. The new operator does not turn a previously nullhomotopic endpoint morphism into a nonzero one.

All pair and triple comparison homotopies are transported with the graded sign dictated by \(\mathsf D\mathscr R=(-1)^\ell\mathscr R\mathsf D\). Their full polynomial chain equations are checked. The complete bare cap, its endpoint equation and its chosen two-term correction are checked on all 64 central faces of the six short-Rees parameters. The generic top column remains exactly \(\omega\) on every face.

At the full central short-Rees face only the top generic source column survives. Its nonzero degree-four class does not disappear, because neither the source Cartier generator nor its determinant is discarded. The long normals remain unchanged throughout this test.

The common bare matrix is also strictly compatible with all six labelled transformations generated by rotation of hexagon vertices by two and reflection \(v\mapsto3-v\). The source carries the induced exterior signs on the six occurrence generators. The target carries its top orientation sign and the permutation signs on the face and mark sets. The checker verifies all 768 map columns and all 1,290 target differential columns. Reflection transports a plus-labelled frame to its corresponding minus-labelled frame; this is not a proof that every such frame is a fixed physical object.

## 8. What has and has not been identified

The former primitive generic maps landed in \(Q\otimes L\). Their complete source-relative traces now land in **Q itself**, with the correct degree-four source, conormal frame and polynomial-linear comparison maps. This closes the auxiliary-factor-removal problem for these eight specific supported inputs.

No universal degree-zero map \(L\to A\) has been manufactured. The operation depends on the actual source occurrence-Koszul homotopies, as a bivariant operation should. The source remains \(K(X_0,\ldots,X_5,t_T)\), not a replacement free line. Its conormals and Cartier state cannot be deleted while preserving this map.

The bare endpoint Hom complexes are still acyclic in the displayed frame. Thus identifying an independently prescribed nonzero endpoint morphism with these endpoint composites is still impossible without a specifically defined change of source, support or conormal degree. A separately framed geometric collar 2-cell is not determined merely by the class of an endpoint morphism. Its comparison to the transported nullhomotopies remains to be constructed.

There is no new same-degree physical state theorem, no equality with the complete ringed supported-Verdier functor, and no assignment of physical reflection parity. The operation constructed here is a concrete coefficient-linear Gysin morphism to the existing target, with all its comparison data explicit.

## 9. Reproduction and references

Run:

```sh
python check_marici_source_relative_excess_trace.py \
  --output marici_source_relative_excess_trace_certificate.json
```

The self-contained standard-library checker passes **423,648 exact assertions**, comprising 27,059 inherited reconstruction checks and 396,589 new checks. It reconstructs the eight supported inputs and their native polynomial lifts, constructs the source-relative Hom operation, checks its full elementary-row identity and negative controls, transports all endpoint comparison homotopies, computes every bare homogeneous Hom complex and its integral reductions, checks 64 Rees central faces, and verifies six labelled transports. The certificate contains the complete new cochains.

The all-polynomial chain identity is proved in Section 4. The all-replacement class calculation follows from regular Koszul purity and independent full homogeneous reductions in Section 6. The infinite completion assertion of Section 3 follows from the derived-completion formula and Noetherian flatness, not finite testing. No proof assistant or repository write is claimed.

[S1] `src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md`, blob `d5ed0c89e804284a4bf45bfa1e0c0bc2eab6eb12`: ordered repeated-normal/excess convention and the distinction between a labelled local trace and the global physical collar comparison.

[S2] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: original target states, signs and allowed localization domains. Lines 285–354 were re-read in this continuation.

[S3] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: normalization source used in the inherited fifty-generator polynomial resolution.

[M1] Stacks Project, tag `0663`, multiplication by a Koszul equation is nullhomotopic; tag `0621`, exterior Koszul differential and cone convention.

[M2] Stacks Project, tag `0A8H`, Hom complexes and graded composition differential.

[M3] Stacks Project, tag `091N`, especially Lemmas 15.93.10 and 15.93.13: derived completion as Hom from the extended Čech complex and its compatibility with derived Hom. Tag `0952`: local cohomology and the supported Čech complex.

The web sources used for these general facts are primary Stacks Project pages. All new Marici conclusions above are established by the explicit formulas and checker in this note, not asserted by those general references.
