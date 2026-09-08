# Removing the true obstruction support exposes a nontrivial descent torsor

Date: 2026-09-07  
Lane: Branch B — the fixed 215-state target, its coefficient operations, and lifting spaces  
Repository inputs remain pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Result

The last calculation showed that removing the three pair supports does not change either obstruction. This note removes the **entire actual support of the first obstruction**, constructs a unit lift on every member of its seven-open affine cover, and computes the obstruction to gluing those lifts.

Every local unit lift exists. There is nevertheless **no global unit lift on this open**. Their transition differences represent the restriction of the old module-extension class as a nonzero first-cohomology class. Its cyclic module is exactly the spectator ring modulo the six-factor Rees product.

This is not simply another support-placement failure. The primary obstruction sheaf is zero on the new open, but the global connecting class survives in the first Čech degree of the top boundary module. The computation identifies that class by twelve explicit residue coordinates and by actual differences of target cycles.

There is also a positive change: all positive-degree branch multiples, including their branch-allowed normal Laurent coefficients, now have global closed lifts. Only the common-conductor coefficient still requires the full six-factor product. The classification includes an explicit lift for every admissible global coefficient.

No native physical source, new spatial endpoint connector, or identification of this coefficient-open set with a physical generic deformation is asserted. In particular, the coordinate inverses used to describe open subsets are not being admitted as new global physical poles.

## 1. Fixed target and coefficient notation

Retain the labelled sets

\[
S_+=\{13,35,15\},\quad S_-=\{02,24,04\},\quad L=\{03,14,25\},
\]

\[
\mathcal C=\mathbb Z[t_s\ (s\in S_+\cup S_-),X_l,u_l\ (l\in L)],
\quad
\mathcal B=\mathcal C[X_s\ (s\in S_+\cup S_-)]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: the two occurrence sheets meet at their common conductor; all six short Rees parameters and all long occurrence and normal parameters remain independent. Put

\[
I_+=(X_p:p\in S_+),\quad I_-=(X_m:m\in S_-),\quad
p=\tau_+=\prod_{s\in S_+}t_s,\quad m=\tau_-=\prod_{s\in S_-}t_s.
\]

In words: in this note the upright letter choices p and m abbreviate two products, not a prime and not a morphism. Write

\[
\mathcal B_+=\mathcal C[X_s:s\in S_+],\quad
\mathcal B_-=\mathcal C[X_s:s\in S_-],\quad
\mathcal B=\mathcal B_+\times_{\mathcal C}\mathcal B_-.
\]

In words: the canonical normalization of the occurrence ring is the pair of polynomial sheets; their zero-section values agree on the conductor. No arbitrary quotient of branch coefficients is chosen.

The fixed support sequence is

\[
0\longrightarrow A_\partial\longrightarrow E\xrightarrow{\pi}Q\longrightarrow0.
\]

In words: use the existing endpoint quotient, boundary-relative subcomplex, and honest seven-state generic quotient. Both the absolute and specified PC targets are bounded above by homological degree three. The preceding full-target calculations [P1–P3] establish

\[
H_3(Q)=\mathcal B\theta,\quad
\operatorname{im}(H_3(E)\to H_3(Q))=\mathfrak a\theta,
\quad
\mathfrak a=(pm,pI_+,mI_-),
\]

\[
0\longrightarrow M\longrightarrow H\xrightarrow{\rho}\mathfrak a\longrightarrow0,
\quad H=H_3(E),\quad
M=\bigoplus_{\varnothing\ne N\subsetneq S_-}I_+\Gamma_{+,N}
\oplus\bigoplus_{\varnothing\ne N\subsetneq S_+}I_-\Gamma_{-,N}.
\]

In words: twelve labelled branch ideals comprise the complete top boundary ambiguity module. Their explicit target cycles are recalled below. The extension class \(e\) satisfies

\[
\operatorname{Ann}_{\mathcal B}(e)=I_++I_-+(pm).
\]

In words: this is the previously proved coefficient-linearity obstruction, not an assumption that local lifts cannot glue on every open.

## 2. The actual obstruction support and its canonical cover

Set

\[
W=V(\mathfrak a),\qquad V=\operatorname{Spec}\mathcal B\setminus W=D(\mathfrak a).
\]

In words: unlike the preceding open complement of the three pair supports, V removes all of the actual first-obstruction support. This open is selected by an already computed annihilator, not declared to be a physical operation.

The branch-divisor quotient has the exact gluing description

\[
\mathcal B/\mathfrak a
\cong (\mathcal B_+/(p))\times_{\mathcal C/(p,m)}(\mathcal B_-/(m)).
\]

In words: the obstruction support consists of the positive sheet's three normal divisors and the negative sheet's three normal divisors, glued along their conductor intersection. The two displayed branch divisor rings are not being called normal; their further normal-crossing decompositions remain present.

**Proof.** Write any coefficient uniquely as \(c+f_++f_-\), with \(c\in\mathcal C\) and \(f_\pm\in I_\pm\). Its two images are zero precisely when \(c\in(p)\cap(m)=(pm)\), \(f_+\in pI_+\), and \(f_-\in mI_-\). Those conditions are exactly membership in \(\mathfrak a\). A compatible pair of conductor values modulo p and m lifts to a common value modulo pm: if two lifts differ by \(pa+mb\), subtract pa from the first and add mb to the second. Branch tails lift independently. This proves surjectivity as well.

Use the seven principal opens

\[
V_0=D(pm),\quad V_{+,s}=D(pX_s)\ (s\in S_+),\quad
V_{-,s}=D(mX_s)\ (s\in S_-).
\]

In words: these are the seven generators of the actual lifting ideal. Every cross-sheet intersection of a positive and a negative occurrence chart is empty, since it would invert a zero product. The nonempty Čech intersections have counts

\[
(7,12,8,2).
\]

In words: seven opens, twelve double intersections, eight triple intersections, and two quadruple intersections. They form two full three-simplices sharing the common-open vertex. The indexing nerve is contractible. The coefficient diagram is not constant, and the result below does not contract it.

## 3. Compute sections and first cohomology from the normalization

Let \(V_\pm\) denote the inverse images of V on the two normalization sheets, not individual members of the seven-open cover. Pulling back the defining ideal gives

\[
V_+=\operatorname{Spec}(\mathcal B_+[p^{-1}])\setminus V(m,I_+),
\quad
V_-=\operatorname{Spec}(\mathcal B_-[m^{-1}])\setminus V(p,I_-).
\]

In words: on each sheet its own three normal parameters are invertible, but the intersection of the opposite product divisor with that sheet's conductor is removed. The conductor inverse image is \(\operatorname{Spec}\mathcal C[(pm)^{-1}]\).

The four elements consisting of the opposite Rees product and the three active occurrence coordinates form a regular sequence on the relevant polynomial sheet. An extended Čech/Koszul calculation gives

\[
\Gamma(V_+,\mathcal O)=\mathcal B_+[p^{-1}],\quad
H^1(V_+,\mathcal O)=H^2(V_+,\mathcal O)=0,
\]

and the reflected result for the negative sheet. In words: deleting this codimension-four locus does not add regular functions or low-degree cohomology on the polynomial sheet. The argument works integrally: each fine-degree extended Čech complex contracts except in its full negative-support degree. References [M1, M2] give the local-cohomology/open-complement conventions.

Apply the normalization exact sequence on V. Its global-section kernel and cokernel give

\[
\widehat{\mathcal B}:=\Gamma(V,\mathcal O_V)
=\mathcal C\oplus I_+[p^{-1}]\oplus I_-[m^{-1}],
\]

\[
H^1(V,\mathcal O_V)
=\mathcal C[(pm)^{-1}]/(\mathcal C[p^{-1}]+\mathcal C[m^{-1}]).
\]

In words: branch tails acquire their own branch's allowed normal inverses, while their common constant remains in the unlocalized spectator ring. A double-pole conductor quotient survives in first cohomology. These are additive direct-sum descriptions with the natural fibre-product multiplication, not three independent rings.

For clarity, the common constant remains unlocalized because

\[
\mathcal C[p^{-1}]\cap\mathcal C[m^{-1}]=\mathcal C
\quad\text{inside}\quad\mathcal C[(pm)^{-1}].
\]

In words: the two normal products have disjoint sets of independent prime factors; a Laurent polynomial regular in both complementary normal directions has no negative normal exponent.

For a positive boundary-ideal summand, use its actual ideal sequence on \(V_+\). Its first cohomology is

\[
\Gamma(V,I_+)=I_+[p^{-1}],\qquad
H^1(V,I_+)=\mathcal C[(pm)^{-1}]/\mathcal C[p^{-1}],
\]

with the reflected formula for \(I_-\). In words: positive branch ideal sections extend, but a conductor value having an opposite-branch pole need not lift to a global ideal section. The identification of the quotient with first cohomology is the connecting map of the ideal sequence.

Consequently

\[
\Gamma(V,M)=\widehat I_+^{\oplus6}\oplus\widehat I_-^{\oplus6},
\quad \widehat I_+=I_+[p^{-1}],\quad\widehat I_-=I_-[m^{-1}],
\]

\[
H^1(V,M)=
\bigl(\mathcal C[(pm)^{-1}]/\mathcal C[p^{-1}]\bigr)^{\oplus6}
\oplus
\bigl(\mathcal C[(pm)^{-1}]/\mathcal C[m^{-1}]\bigr)^{\oplus6}.
\]

In words: all twelve labelled boundary families remain, and each has its own precise Laurent-residue quotient. Short occurrence ideals act trivially on these first-cohomology quotients; the full spectator action remains.

The new checker independently reconstructs the actual seven-open coefficient complex in all 3,392 sign/support types for \(\mathcal O_V\), and the two branch-ideal complexes in all 432 sign/support types. It checks the integer incidence matrices, differential squares, and saturation of every image. Since allowed Laurent modes depend only on these signs and supports, the accompanying monomial proof covers arbitrary exponents. This is not a polynomial-degree truncation.

## 4. Construct all seven local unit lifts in the actual target

For any compatible face F, put \(\epsilon_F=(-1)^{|F|(|F|+1)/2}\). The existing common cycle is

\[
\Lambda_0=\sum_F\epsilon_F
\left(\prod_{s\in S\setminus F}t_s\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L\setminus F}u_l\right)[F,F].
\]

In words: sum actual fully marked faces, including both endpoint faces before quotienting, with all inherited signs and coefficients.

Let \(L_+\) denote the same sum restricted to faces in \(S_+\cup L\), with only the positive short factors in its first product; define \(L_-\) by reflection. The unmultiplied \(L_+\) need not be a cycle on the glued affine ring. Multiplication by an element of \(I_+\) kills its outgoing opposite-sheet terms. The source cycles are

\[
\Lambda_{+,s}=X_sL_+,\quad \Lambda_{-,s}=X_sL_-.
\]

In words: these are exactly the prior six branch lifts, not newly added relation cells.

On the actual seven opens define

\[
\ell_0=\Lambda_0/(pm),\quad
\ell_{+,s}=\Lambda_{+,s}/(pX_s),\quad
\ell_{-,s}=\Lambda_{-,s}/(mX_s).
\]

In words: the denominator is invertible on the specific named open. An occurrence chart has already selected its sheet, so its local lift is \(L_+/p\) or \(L_-/m\). There is no use of these fractions as forbidden global coefficients.

The checker verifies, in both the absolute and PC target,

\[
d\ell_i=0,\qquad \pi(\ell_i)=\theta.
\]

In words: every chart has a genuine closed lift of the same nonzero generic generator. The full polynomial differential is checked on all 215 target states over all 29 nonempty cover intersections.

The differences on overlaps are

\[
c_{ij}=\ell_j-\ell_i\in\Gamma(V_i\cap V_j,M),\qquad
c_{jk}-c_{ik}+c_{ij}=0.
\]

In words: they are actual boundary-supported top cycles and satisfy every triple-overlap equation. Same-sheet differences vanish; opposite-sheet charts do not intersect. Only the six common-to-branch overlaps contribute.

The first cohomology class \([c]\) is the restriction of the prior module extension e:

\[
e_V\in\operatorname{Ext}^1_{\mathcal O_V}(\mathcal O_V,\widetilde M|_V)
=H^1(V,\widetilde M|_V).
\]

In words: the lifting ideal is the unit ideal locally on V, so its extension becomes a torsor of local unit lifts. The Čech class vanishes precisely when local choices can be corrected to glue. This is the standard first-cohomology/torsor correspondence [M3], applied to the explicitly computed additive coefficient sheaf, not an assumption of a locally free ambiguity module.

## 5. Twelve explicit residue coordinates for the descent class

For \(\varnothing\ne N\subsetneq S_-\), write \(a\sim b\) for the noncrossing relation and let

\[
P_N=\{s\in S_+:\forall n\in N,\ s\sim n\},\quad
L_N=\{l\in L:\forall n\in N,\ l\sim n\}.
\]

In words: these are actual compatible extensions of the inactive marked face. Equivalently they may be defined using the noncrossing relation on diagonals; their labels are retained throughout.

The associated top boundary generator is

\[
\Gamma_{+,N}=\sum_{N\subseteq F\subseteq N\cup P_N\cup L_N}\epsilon_F
\left(\prod_{s\in P_N\setminus F}t_s\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L_N\setminus F}u_l\right)[F,F].
\]

In words: only noncrossing faces in the indicated range occur, and endpoint faces are removed in the endpoint quotient. Multiplication by \(I_+\) makes this the corresponding ideal-valued summand of M.

The previously computed relation defect is

\[
X_s\Lambda_0-m\Lambda_{+,s}
= X_s\sum_N c_{+,N}\Gamma_{+,N},
\]

\[
c_{+,N}=
\left(\prod_{r\in S_-\setminus N}t_r\right)
\left(\prod_{s\in S_+\setminus P_N}t_s\right)
\left(\prod_{l\in L\setminus L_N}u_l\right).
\]

In words: this is an identity of the actual top target cycles. The new checker recomputes it after localization, rather than taking formal generator relations on trust.

Thus the overlap cocycle has coordinates

\[
c_{0,+s}=-\sum_N r_{+,N}\Gamma_{+,N},\qquad
r_{+,N}=\frac{c_{+,N}}{pm}
=\frac{\prod_{l\in L\setminus L_N}u_l}
{\left(\prod_{n\in N}t_n\right)\left(\prod_{a\in P_N}t_a\right)}.
\]

In words: its relative poles consist of the inactive marked subset and its compatible active normals; the independent long-normal numerator is not erased. The negative formula exchanges the sheets. Under the connecting-map identification of Section 3, the class is represented by the positive fraction \(r_{+,N}\); the overlap representative has its displayed minus sign because the common-open lift occupies Čech position zero.

The twelve coordinates are:

| Active sheet | Inactive subset N | Residue coordinate |
|---|---|---|
| + | 02 | \(u_{14}/(t_{02}t_{35})\) |
| + | 04 | \(u_{25}/(t_{04}t_{13})\) |
| + | 24 | \(u_{03}/(t_{24}t_{15})\) |
| + | 02,04 | \(u_{14}u_{25}/(t_{02}t_{04})\) |
| + | 02,24 | \(u_{03}u_{14}/(t_{02}t_{24})\) |
| + | 04,24 | \(u_{03}u_{25}/(t_{04}t_{24})\) |
| − | 13 | \(u_{25}/(t_{13}t_{04})\) |
| − | 15 | \(u_{03}/(t_{15}t_{24})\) |
| − | 35 | \(u_{14}/(t_{35}t_{02})\) |
| − | 13,15 | \(u_{03}u_{25}/(t_{13}t_{15})\) |
| − | 13,35 | \(u_{14}u_{25}/(t_{13}t_{35})\) |
| − | 15,35 | \(u_{03}u_{14}/(t_{15}t_{35})\) |

In words: repeated rational expressions in opposite rows are elements of different labelled residue quotients, so they cannot be identified or canceled merely because their printed fractions agree.

For the positive coordinates,

\[
\operatorname{Ann}_{\mathcal C}[r_{+,N}]
=\left(\prod_{n\in N}t_n\right),\qquad
\bigcap_{\varnothing\ne N\subsetneq S_-}\operatorname{Ann}_{\mathcal C}[r_{+,N}]=(m).
\]

In words: the active denominators are already units in \(\mathcal C[p^{-1}]\), but each inactive denominator must be canceled. The independent long numerator has no short-normal factor. Monomial independence proves necessity and sufficiency for arbitrary polynomials, not just monomials.

The negative coordinates have combined annihilator (p). Therefore

\[
\operatorname{Ann}_{\widehat{\mathcal B}}(e_V)
=\widehat I_++\widehat I_-+(pm),\qquad
\widehat{\mathcal B}e_V\cong\mathcal C/(pm).
\]

In words: the gluing class is nonzero, has infinite additive order, and retains the full six-factor divisor on its conductor coefficient. Every branch-tail section acts by zero, but no additional common-conductor coefficient does.

### Why this is not contradicted by local vanishing

The first obstruction sheaf \(\mathcal B/\mathfrak a\) is zero on V. The extension class e is also split on every one of the seven affine opens. A global Ext class need not vanish on an arbitrary union just because its localizations vanish separately: its local-to-global first-cohomology contribution may be nonzero. Here the displayed twelve fractions calculate that contribution exactly.

The original connecting class restricted to the derived sections over V is the image of \(e_V\) under

\[
H^1(V,H_3(A_\partial))\hookrightarrow H_2(R\Gamma(V,A_\partial)).
\]

In words: the unit lifts as a local cycle, while their differences supply its global connecting boundary. This edge map is injective because the target has no homology above degree three: no differential can enter or leave this lowest-row, first-column term of the hypercohomology spectral sequence. Thus the global primary connecting obstruction survives precisely as the computed descent class, even though all of its sheaf-level stalk obstructions have disappeared.

## 6. Complete classification of global generic coefficients that now lift

Taking sections of the top module extension gives

\[
\Gamma(V,H)\xrightarrow{\rho}\widehat{\mathcal B}
\xrightarrow{k\mapsto k e_V}H^1(V,M).
\]

In words: a global generic coefficient lifts exactly when it kills the explicit descent class. Consequently

\[
\operatorname{im}\rho
=pm\mathcal C\oplus\widehat I_+\oplus\widehat I_-.
\]

In words: every branch tail now lifts, but a common conductor coefficient still needs all six Rees factors. This is larger than the old affine ideal; it is not obtained merely by extending that ideal to the global-section ring.

There is an explicit lift. For

\[
k=pm c+f_++f_-,\quad c\in\mathcal C,\quad f_+\in\widehat I_+,\quad f_-\in\widehat I_-,
\]

set

\[
s(k)=c\Lambda_0+(f_+/p)L_++(f_-/m)L_-.
\]

In words: each denominator multiplies a positive-degree term of its own branch. Every resulting coefficient lies in the actual global-section ring described in Section 3. It need not be a polynomial on the original affine ring, and it is not a scalar trace. Directly \(ds(k)=0\) and \(\pi s(k)=k\theta\).

For example, \(X_{13}\theta\) did not lift on the original affine target but now lifts through \(\Lambda_{+,13}/p\). The unit \(\theta\) still has no global lift. The exact quotient of all global generic coefficients by those that lift is

\[
\widehat{\mathcal B}/\operatorname{im}\rho\cong\mathcal C/(pm).
\]

In words: the earlier distinction between individual-lifting and coefficient-selection obstructions has acquired a precise bridge: after removing the true local obstruction support, the remaining individual global obstruction is the restriction of the old coefficient-extension class.

For completeness, the boundedness of the targets gives

\[
H_3(R\Gamma(V,E))=\Gamma(V,H_3(E)),\qquad
H_3(R\Gamma(V,Q))=\widehat{\mathcal B}\theta.
\]

In words: there is no unexamined higher-cohomology contribution to the highest homological degree. Every nonempty lifting space for a fixed coefficient in the displayed image is a discrete torsor for

\[
\Gamma(V,M)=\widehat I_+^{\oplus6}\oplus\widehat I_-^{\oplus6}.
\]

In words: the ambiguity is fully classified; there are no higher homotopy groups in this particular top-degree marking problem. The unit lifting space is empty globally but nonempty on every cover member.

## 7. Endpoint and physical scope controls

All seven local cycles are constructed before quotienting the endpoint cubes. On a positive occurrence chart, comparison with the common-open cycle changes the negative fully marked endpoint coefficient by

\[
-U_L/m,\qquad U_L=u_{03}u_{14}u_{25}.
\]

In words: this nonzero endpoint term is retained in the certificate before passage to E. The negative chart has the reflected positive-endpoint term \(-U_L/p\). The calculation does not pretend these endpoint changes are newly constructed endpoint connector 2-cells.

The no-global-lift result already holds after passing to the specified endpoint quotient, with no additional endpoint framing imposed. Requiring stricter endpoint equalities cannot supply the missing global lift in that same problem. A native mixed-variance source can instead carry its own boundary data; the theorem does not force such a source to be a closed lift of \(\mathcal O_V[3]\).

The computed overlap classes provide explicit target data for a source comparison to match. Merely selecting the seven individually normalized local cycles is insufficient. A source-defined complementary-support or logarithmic construction may change the comparison problem or send its own connecting boundary to these residues. No conclusion about that unconstructed identification, about the native Morse roof, about parity, or about RH follows here.

## 8. Verification

Run:

```sh
python check_marici_obstruction_complement_descent_20260907.py \
  --output marici_obstruction_complement_descent_certificate_20260907.json
```

The standalone standard-library checker passes **78,779 exact assertions**. It rebuilds the source target cells and both absolute/PC differentials; checks them on every nonempty open intersection; constructs all seven local unit lifts and every overlap; verifies the twelve residue-coordinate decompositions and all triple cocycle identities; computes **3,824 independent integral fine-degree Čech complexes**; verifies all squarefree annihilator patterns and the exact branch-divisor kernel; and tests explicit Laurent branch lifts while checking their actual gluing domains.

The two independently rerun prerequisites pass **4,001** and **138,416** assertions. The reproducibility manifest records hashes of all inputs and replay outputs. No prerequisite is silently run by the new checker. All-degree statements depend on the proofs above and the declared earlier top-module theorem, not on promoting finite tests to a proof assistant certificate.

## References and inherited artifacts

[P1] `marici_filtered_q_alternating_rees_update_20260907.md`: honest target, first lifting ideal, and top boundary module.

[P2] `marici_q_graded_lift_naturality_20260907.md`: full top lifting extension, 43-generator/174-relation presentation, seven actual lifts, twelve labelled ambiguity ideals, six explicit relation defects, and their exact annihilator. Its checker was rerun for this note.

[P3] `marici_union_recollement_20260907.md`: all-thickenings pair-support recollement, exact support decomposition, and persistence on the smaller pair-support complement. Its checker was rerun for this note.

[M1] Stacks Project, Section 47.9, *Local cohomology*, tag `0952`: https://stacks.math.columbia.edu/tag/0952 .

[M2] Stacks Project, Section 51.2, *Generalities*, tag `0DWQ`: https://stacks.math.columbia.edu/tag/0DWQ .

[M3] Stacks Project, Section 21.4, *First cohomology and torsors*, tag `03AG`: https://stacks.math.columbia.edu/tag/03AG .
