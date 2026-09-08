# Class-level endpoint and generic test of the eight supported short-Rees maps

Project: Marici  
Date: 2026-09-07  
Pinned source: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`  
Input calculation: `marici_short_rees_supported_defect.md`

## 1. Result and scope

The eight previously constructed supported maps have primitive, nonzero generic classes. Their displayed plus and minus endpoint composites, however, are nullhomotopic in their actual coefficient domains. This note constructs the endpoint nullhomotopies, their pair and triple coherences, and a closed representative of each cap in the full target. It then computes the complete prescribed homogeneous mapping problems, rather than interpreting nonzero endpoint matrix entries as nonzero endpoint classes.

In each of the eight prescribed frames, the mapping complexes to the endpoint support and to the full short boundary are acyclic. Consequently the restrictions from the full target to the endpoint quotient and then to the generic quotient are quasi-isomorphisms. A fixed entire generic class has a contractible space of lifts with compatible endpoint comparison data in this frame.

This is not an identification with the independently framed physical collar operators. A homotopy to zero of an endpoint morphism does not imply that every separately prescribed geometric 2-cell is zero. The result says precisely which classes and comparisons are available for these particular free supported inputs and these coefficient frames. It neither supplies ordinary raw-source lifts nor assigns physical reflection parity.

There is no contradiction with the older vanishing of cap composites on bare quadratic attachment cycles. The new nonzero generic classes use the complete seven-equation Koszul inputs, including their occurrence-annihilator homotopies and their product-Cartier generator. They are different derived morphisms with different source degrees.

## 2. Fixed objects and grading conventions

Let

\[
A=\mathbb Z[X_0,\ldots,X_5,X_{D03},X_{D14},X_{D25},
 t_0,\ldots,t_5,u_{D03},u_{D14},u_{D25}].
\]

In words: the six short-Rees parameters, the six short occurrences, and the long occurrence and normal parameters remain separate. Polynomial spectators may be adjoined. The short graph equations are \(u_i=t_iX_i\); the long normals are not specialized in this calculation.

For \(T\subseteq\{1,3,5\}\), with \(|T|=2\) or \(3\), set

\[
t_T=\prod_{i\in T}t_i,\qquad
\tau=t_1t_3t_5,\qquad
S_T=A/(X_0,\ldots,X_5,t_T),
\]

\[
\mathcal K_T=K_A(X_0,\ldots,X_5,t_T).
\]

In words: retain the actual 128-generator free resolution of the support module, not a free line representing its residue. Its last exterior generator is denoted by \(z_T\). All complexes in the executable use homological grading; the Hom differential lowers degree.

The raw excess complex, in its checked split basis, is

\[
D_u=K_A(t_1X_1,t_3X_3,t_5X_5,t_0X_0)\otimes\Lambda(\eta_u).
\]

In words: the independent excess remains a separate exterior factor with zero differential and its original weight. This is the integral basis change of the actual repeated-normal source, not an extra generator adjoined to force a result.

Let \(K\) be the 215-state target, \(V\) its two-endpoint subcomplex, \(B\) its short-boundary subcomplex, \(E=K/V\), and \(Q=K/B\). For any of these targets define

\[
W_Z=W\otimes_A\operatorname{Cone}\bigl(D_u\longrightarrow D_u[\tau^{-1}]\bigr).
\]

In words: use the entire supported localization cone. Its localized and unlocalized arms retain distinct coefficient domains. This is the same output as the preceding supported calculation, up to its stated tensor/cone sign convention.

Write \(n=|T|+\epsilon\), where \(\epsilon=0,1\) specifies the excess factor. The previous construction gives maps

\[
F_{T,\epsilon}:\mathcal K_T\longrightarrow K_Z,
\qquad |F_{T,\epsilon}|=n-2,
\]

\[
\mathsf D F_{T,\epsilon}=A_{T,\epsilon},\qquad
\mathsf D A_{T,\epsilon}=0,
\qquad |A_{T,\epsilon}|=n-3.
\]

In words: the cap and its coupled endpoint composite already satisfy the full source-target chain equation. The new calculation determines their classes and comparisons.

All maps have the inherited fine degree

\[
\lambda_{T,\epsilon}
=\gamma-\sum_{i=0}^5 e_{X_i}
+e_{X_0}+e_{t_0}
+\sum_{i\in T}e_{X_i}
+\epsilon(e_{X_3}+e_{t_3}),
\qquad
\gamma=\sum_{\ell\in\{D03,D14,D25\}}e_{u_\ell}.
\]

In words: this is the actual degree of the constructed supported maps. A negative map degree is not permission to place a pole in a forbidden stalk.

## 3. Explicit endpoint nullhomotopies

Every coefficient term of \(A_{T,\epsilon}\) lands on an unmarked endpoint state. This is verified directly on all eight free-resolution compositions. Such a state at \(v_+\) inverts precisely its three short normals \(u_1,u_3,u_5\); the analogous state at \(v_-\) inverts \(u_0,u_2,u_4\). On the graph \(u_i=t_iX_i\), these declared localizations make both \(t_i\) and \(X_i\) invertible in that stalk. No ambient inversion is performed.

Let \(A_\pm\) be the restrictions of the signed endpoint composite to the two endpoints, and let \(k=n-3\) be their homological map degree. For an endpoint label \(i\), let \(w_i\) denote left exterior multiplication by the occurrence-Koszul generator \(e_i\) in \(\mathcal K_T\). The original Koszul differential gives

\[
dw_i+w_id=X_i\operatorname{id}.
\]

In words: multiplication by the occurrence coordinate is nullhomotopic on the complete free input. This is the standard Koszul multiplication homotopy [M1].

Define

\[
H_{\pm,i}=(-1)^kX_i^{-1}A_\pm w_i.
\]

In words: use only an inverse already allowed on that endpoint output. The source remains polynomial. Direct application of the Hom differential yields

\[
\mathsf D H_{\pm,i}=A_\pm.
\]

In words: both displayed endpoint morphisms are exact, including all their native-resolution corrections. This is not merely a rank argument or a special-fibre test.

The three possible endpoint labels come with complete coherent comparisons. For an ordered nonempty subset \(I\) of the relevant endpoint triple, put

\[
H_{\pm,I}=(-1)^{k|I|}
\left(\prod_{i\in I}X_i^{-1}\right)A_\pm w_I.
\]

In words: retain the iterated source exterior operation and the prescribed output localization. Set \(H_{\pm,\varnothing}=A_\pm\). Then

\[
\mathsf D H_{\pm,I}
=\sum_{a=0}^{|I|-1}(-1)^aH_{\pm,I\setminus\{i_a\}}.
\]

In words: the single-label terms nullhomotope the endpoint map; the two-label terms compare those choices; the three-label term supplies their coherence. Every equation is checked on all 128 source columns. They also specialize on all eight central faces of the branch short-Rees cube, deleting only summands whose declared localization becomes empty.

Choose one of these homotopies at each endpoint and define

\[
\widetilde F=F-H_{+,i}-H_{-,j}.
\]

In words: this is a representative in the full target, corrected only inside endpoint support. It satisfies

\[
\mathsf D\widetilde F=0,\qquad
\pi_Q\widetilde F=\pi_QF.
\]

In words: the endpoint correction closes the cap without changing its generic projection. The label choices are auxiliary; the displayed higher homotopies compare them.

## 4. The generic classes really are primitive

Let

\[
e_{\mathrm{top}}=e_0\wedge\cdots\wedge e_5\wedge z_T,
\qquad
U_L=u_{D03}u_{D14}u_{D25},
\]

\[
\omega=U_LT-\sum_\ell X_\ell\frac{U_L}{u_\ell}M_\ell.
\]

In words: the first symbol is the full supported-source wedge, and the second is the existing corrected generic cycle, with all three marked-normal corrections. The quotient \(U_L/u_\ell\) is a polynomial product of the other long normals.

The constructed closed map has the exact top column

\[
\widetilde F(e_{\mathrm{top}})
=(-1)^{\epsilon+1}\omega\otimes
[h_T h_0\eta_u^\epsilon].
\]

In words: the bracket records the shifted unlocalized arm of the support cone. This is a literal four-term generic column, not a monomial coefficient extracted from an unrelated matrix. Its independent excess label and the residual opposite-pair normal are retained.

The endpoint composite has zero top column. In particular, nonzero endpoint entries on lower input columns cannot be used as proof of nonzero endpoint cohomology.

The generic target in this assertion is the supported, derived-source target \(Q_Z\), not bare \(Q\). The raw normal wedge and the shifted cone arm in the displayed formula are essential. No counit forgetting them has been constructed. In particular, the projection from a Koszul complex onto the ambient coefficient ring is not a chain map with unit bottom coefficient when its normal equations are nonzero: it would send \(d h_i=t_iX_i\) to \(t_iX_i
e0\). The ordinary augmentation instead lands in the quotient by the normal equations; replacing it by a different Gysin trace requires its own degree and support data.

### All-replacement proof by regular Koszul purity

The seven equations defining \(S_T\) are a regular sequence in the ambient polynomial ring. All target terms in \(W_Z\) are flat over that ring. Thus the full Hom complex from \(\mathcal K_T\) is naturally computed by its top-Koszul evaluation into the derived support restriction, with the ordered determinant and seven-degree shift retained [M2, M3].

Concretely, after imposing the six occurrence equations and \(t_T=0\):

* the \(\tau\)-localized arm vanishes because \(t_T\) is a unit there;
* any target state with an unmarked short coordinate vanishes because that state inverts the corresponding \(X_i\);
* every raw source differential becomes zero, but all exterior generators, including \(\eta_u\), remain;
* the exact fine degree forces the remaining raw wedge to have the occurrence multiset of \(h_T h_0\eta_u^\epsilon\).

For such a raw wedge, a fully marked nonempty short face would require a negative short-Rees coefficient in a stalk where that normal is marked. This is forbidden by the original domain rule. Consequently the entire surviving homogeneous purity quotient contains only the seven generic states, once or twice, and contains no short-boundary or endpoint state.

Each seven-state block has the same three signed-unit marked-normal-to-facet differentials. It contracts onto the primitive line generated by \(\omega\). This proves nonvanishing, primitivity, and the absence of hidden torsion, while accounting for every replacement cochain in the prescribed degree. The executable constructs this small quotient independently, and verifies the natural top-evaluation chain map on every column of each large Hom complex.

At the full central short-Rees face, the last source equation becomes zero and its Koszul generator must not be deleted. Apply the six-occurrence version of the preceding purity argument and retain the two Cartier input states. The state without \(z_T\) would require negative short-Rees degree \(-\sum_{i\in T}e_{t_i}\), so it contributes nothing in this frame. The state with \(z_T\) gives precisely the same generic blocks. The same argument applies to the intermediate central faces; the maps and endpoint coherence equations are independently checked on all eight.

## 5. Complete mapping spaces and the apparent extra class

Let

\[
\mathcal H_W=
\underline{\operatorname{Hom}}_A(\mathcal K_T,W_Z)_{\lambda_{T,\epsilon}}.
\]

In words: this is the complete integral homogeneous mapping complex, not a selected list of source rows. It includes every target wedge, every allowed monomial, and every higher comparison in this degree.

The result is

\[
H_*(\mathcal H_V)=H_*(\mathcal H_B)=0,
\]

\[
H_j(\mathcal H_K)\cong H_j(\mathcal H_E)
\cong H_j(\mathcal H_Q)
\cong
\begin{cases}
\mathbb Z^{r_{T,\epsilon}},&j=|T|+\epsilon-2,\\
0,&j\ne |T|+\epsilon-2.
\end{cases}
\]

In words: all short-support and endpoint comparisons are acyclic in this frame. The generic, endpoint-quotient, and full-target mapping problems have the same remaining class group.

The ranks are:

| Odd wedge | No excess factor | One excess factor |
|---|---:|---:|
| \(\{1,3\}\) | 2 | 1 |
| \(\{1,5\}\) | 1 | 2 |
| \(\{3,5\}\) | 2 | 1 |
| \(\{1,3,5\}\) | 2 | 1 |

The reason is explicit: the raw branch generator \(h_3\) and the independent \(\eta_u\) have the same fine weight. When the required occurrence multiplicity in that weight is one, there are two distinct exterior choices after support restriction. When it is zero or two, there is only one. The designated map retains the originally specified excess wedge. No physical equivalence or permission to exchange these generators is inferred.

The additional group in four frames therefore is not an order-two parity and not a second arithmetic unit. Nor does the computation prove uniqueness if only one scalar readout is fixed. It proves uniqueness of the lift of a fixed **entire generic class**, including its excess label.

Because the support filtration and the purity projection are natural, the maps

\[
\mathcal H_K\longrightarrow\mathcal H_E\longrightarrow\mathcal H_Q
\]

are quasi-isomorphisms. In words: restriction preserves the complete comparison spaces in this degree. The homotopy fibre at any specified generic class is contractible. Adding the endpoint comparison component leaves that conclusion unchanged because its full mapping complex is acyclic.

This is the precise infinity-groupoid consequence. It does not transfer an independently framed geometric collar into this coefficient problem without a map of its source, support, and determinant data.

## 6. What the endpoint result rules out

The preceding report proved that the cap composites contained many endpoint coefficient terms and satisfied the coupled chain equation. That statement remains correct. The present calculation proves that those endpoint terms represent zero classes in these frames. They cannot be cited as primitive physical endpoint morphisms merely because both supports occur.

There are two different requirements:

1. An endpoint morphism into the stated \(V_Z\), out of this \(\mathcal K_T\), in this fine degree. Its mapping complex is acyclic.
2. A framed physical collar 2-cell with its prescribed normal/Gysin source and conormal transitions. Its identification with the first problem has not been supplied.

A class-level identification carrying a prescribed nonzero endpoint morphism to the displayed \(A_\pm\) is impossible under unchanged source and frame. A genuinely shifted support operation or a comparison of geometric 2-cells may ask a different question; this calculation does not rule it out. Such a change must be a defined morphism of the complete diagram, not an unlabelled shift or an independent declaration of endpoint values.

The eight maps do carry primitive generic supported extensions. Their existence does not create eight ordinary raw lifts through selection and does not turn the old zero cap on a bare quadratic cycle into a nonzero morphism. The extra complete Koszul input is essential.

## 7. Reproduction and evidence

Run:

```sh
python check_marici_supported_endpoint_class_test.py \
  --output marici_supported_endpoint_class_test_certificate.json
```

The checker is self-contained and uses only the Python standard library. It reconstructs the previous 50-generator native resolution, eight supported input maps, polynomial lifts, 215-state target and supported cone; constructs all endpoint homotopies and their higher coherences; checks the closed cap on all eight central Rees faces; constructs the entire homogeneous Hom complex for each input before and after full central specialization; and verifies the natural purity projection on every such Hom column.

The small purity quotients are reduced integrally. Independent signed-unit reductions of the unreduced generic and endpoint Hom complexes are also performed in the first representative frame, before and after specialization. For the other full Hom complexes, the quasi-isomorphism proof is the regular-sequence argument in Section 4, not an assumed equality of ranks. The certificate distinguishes those checks. It does not claim independent full Smith reductions of every large mapping complex.

The clean self-contained run passed **4,858,482 exact assertions**, including **4,831,423 new assertions**. It constructed **614,976 full homogeneous Hom columns** across the eight frames before and after central specialization. Complete endpoint homotopy coefficients and the separate verification categories are stored in the certificate. The algebraic proof covers arbitrary polynomial degrees contributing to these fixed frames. No proof assistant, global occurrence inversion, repository write, or full physical-parity assignment is involved.

## Sources

[S1] Marici normalization source, `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`.

[S2] Marici support-directed excess convention and local collar scope, `src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md`, blob `d5ed0c89e804284a4bf45bfa1e0c0bc2eab6eb12`.

[S3] Actual target incidence and localization domains, `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`. Its coefficient-domain rule and full boundary were re-read for this continuation.

[M1] Stacks Project, tag `0621`, *The Koszul complex*, especially the multiplication homotopy.

[M2] Stacks Project, tag `0A8H`, *Hom complexes*, for the source-target differential and its composition signs.

[M3] Stacks Project, tag `0B4B`, regular-immersion purity with the determinant line and codimension shift. The proof here can equivalently be read directly from ordered Koszul self-duality and flatness of each target term.
