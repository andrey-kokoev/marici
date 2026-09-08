# The complete reverse normalization cone and its two endpoint attachments

Date: 2026-09-07  
Lane: Branch B — fixed coefficient target, normalization descent, and reverse comparison  
Source baseline: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The previous calculation dualized the alternating coefficient ring and its finite cyclic obstruction module. This calculation instead constructs the derived dual of the **whole fourteen-residue normalization-pullback source**, including its generic projection, twelve boundary coordinates, two endpoint coordinates, and their extension maps.

The result is an explicit cone of a fifteen-by-sixteen normalization comparison, transposed through the actual codimension-three conductor Koszul maps. Its cohomology contains eight branch-volume lines on each normalization sheet and fifteen labelled conductor lines. These are not independent summands: their degree-three attaching map is specified on every coordinate.

The two endpoint contributions are off-diagonal entries in that attaching map. Their coefficients are the actual triple-normal residues. Duality preserves, rather than cancels, the previously computed obstruction to restoring the endpoints. Its exact annihilator is unchanged.

There is a useful independent negative control. Replacing the reverse complex by the direct sum of its cohomology sheaves creates fifteen spurious classes in degree minus seven of the **smooth-ambient** derived conductor fibre. Conversely, merely deleting the two endpoint off-diagonal blocks still gives a square-zero complex with the same local fibre ranks; the nonzero global endpoint extension distinguishes it. Thus neither a rank match nor a square-zero test suffices to identify the intended comparison.

This is a coefficient-side realization for the coherent sheaf previously called S14 on the test open V. That sheaf was constructed from the target residue vector and the actual normalization. It has **not** been independently identified with the native physical normalization, logarithmic, or supported source. No interchange of derived global sections with duality is used. No new geometric carrier cell, global occurrence inverse, integer division, or physical endpoint connector is introduced.

## 1. Fixed coefficients and the actual normalization source

Keep

\[
S_+=\{13,35,15\},\qquad S_-=\{02,24,04\},\qquad L=\{03,14,25\},
\]

\[
\mathcal C=\mathbb Z[t_s\ (s\in S_+\cup S_-),X_l,u_l\ (l\in L)],
\qquad
\mathcal B=\mathcal C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: the two occurrence sheets are glued at their conductor; their opposite-sheet occurrence products vanish. All Rees and independent long parameters remain present.

Let

\[
I_+=(X_p:p\in S_+),\quad I_-=(X_m:m\in S_-),\quad
\tau_\pm=\prod_{s\in S_\pm}t_s,\quad T=\tau_+\tau_-,\quad U_L=u_{03}u_{14}u_{25}.
\]

In words: the occurrence ideals are different from the normal ideals used later. The two products of three normal parameters are not identified or inverted on the original base.

The already constructed test open and its conductor are

\[
V=\operatorname{Spec}\mathcal B\setminus V(T,\tau_+I_+,\tau_-I_-),
\qquad D=\operatorname{Spec}\mathcal C[T^{-1}].
\]

In words: V is the seven-chart local lifting locus, not an independently identified physical generic fibre. Its conductor is the open where T is invertible. The cover retains 7, 12, 8, and 2 nonempty intersections in its four Cech degrees.

Write nu-plus and nu-minus for the two finite normalization maps over V. Write B-plus and B-minus for their pushforward structure sheaves, and C-D for the conductor structure sheaf pushed into V. These sheaves come with the actual evaluation maps epsilon-plus and epsilon-minus.

Index the fourteen channels by pairs j=(sigma,N), where N is a nonempty subset of the opposite short set. For each channel retain its existing target generator Gamma-j and residue

\[
r_{\sigma,N}=
\frac{\prod_{l\in L\setminus L_N}u_l}
{\left(\prod_{n\in N}t_n\right)\left(\prod_{a\in P_N}t_a\right)}.
\]

In words: P-N and L-N are the short and long labels compatible with every member of N in the actual hexagon. These are the same residues as in the preceding full-chain overlap calculation. They are regular on D, although some do not extend to an entire normalization sheet.

There are seven channels on each sheet. The full inactive subsets are the two endpoint channels. Their residues are

\[
r_{+,S_-}=\frac{U_L}{\tau_-},\qquad
r_{-,S_+}=\frac{U_L}{\tau_+}.
\]

In words: each endpoint retains all three opposite-sheet normal poles and the independent long-normal product.

For q equal to 12 or 14, the preceding source is

\[
\mathcal S_q=\{(a,z):\epsilon_j(z_j)=r_j\,a|_D\ (j\in\Lambda_q)\}.
\]

In words: a source section contains a generic coefficient and normalization sections with the required conductor values. The twelve-channel version omits the two endpoint channels. This is the coherent pullback constructed in the prior note; its residue vector is still target-selected input.

The notation in this display uses a set of equations, not an assertion that the physical source has already been identified. The precise equivalent module presentation follows next.

## 2. Present the entire source by one normalization matrix

Replace a node section a by its two normalization sections b-plus and b-minus. The exact presentation of S14 is

\[
0\longrightarrow\mathcal S_{14}
\longrightarrow \mathcal B_+^{\oplus8}\oplus\mathcal B_-^{\oplus8}
\xrightarrow{A_{14}}\mathcal C_D^{\oplus15}
\longrightarrow0.
\]

In words: keep one generic branch section and seven channel sections on each sheet. The fifteen equations are the original normalization difference and the fourteen channel constraints. All channel grading lines are understood in these framed rank displays.

On an input consisting of b-plus, b-minus, and the z-j, the rows are

\[
\begin{aligned}
(A_{14})_0&=\epsilon_+(b_+)-\epsilon_-(b_-),\\
(A_{14})_j&=\epsilon_{\sigma(j)}(z_j)-r_j\epsilon_{\sigma(j)}(b_{\sigma(j)}).
\end{aligned}
\]

In words: the first row makes the two generic branch values agree; each other row compares a channel value with its required multiple of that common value.

The kernel is exactly the preceding pullback. The map is surjective as a map of sheaves: conductor values lift locally to normalization functions; after choosing the first row, the remaining rows can be supplied independently by the z-columns. This uses the actual normalization evaluations. It does not presume that every r-j extends globally to a branch.

The twelve-channel source has fourteen branch columns and thirteen conductor rows. The q=0 presentation is the original normalization exact sequence for B.

In the fixed eighteen-coordinate fine grading, the generic columns and first conductor row have shift zero. Channel column j and conductor row j have shift minus the degree of r-j. These assignments make every entry homogeneous. The checker substitutes the actual Laurent degrees and verifies every primal and dual differential in that grading. Thus the framed rank notation has not thrown away the labels or their degrees.

## 3. Dualize the matrix through the genuine conductor Gysin maps

Use the smooth six-occurrence ambient ring

\[
\mathcal A=\mathcal C[X_{13},X_{35},X_{15},X_{02},X_{24},X_{04}],
\qquad
\Omega_{\mathcal A/\mathcal C}=\bigwedge^6\Omega^1_{\mathcal A/\mathcal C}.
\]

In words: the ambient occurrence coordinates are ordered in their two labelled triples. This volume is not the independent physical channel conormal.

The coefficient dual is

\[
\mathbb D_V(-)=R\mathcal Hom_{\mathcal B}
\left(-,\mathscr D_{\mathcal B/\mathcal C}|_V\right),
\qquad
\mathscr D_{\mathcal B/\mathcal C}
=R\operatorname{Hom}_{\mathcal A}(\mathcal B,\Omega_{\mathcal A/\mathcal C}[6]).
\]

In words: use the previously computed full dualizing object, not ordinary Hom into B. The ambient polynomial ring is regular and the objects here are bounded coherent, so coherent biduality and localization of dualizing complexes apply [M1].

Let lambda-plus and lambda-minus denote the pushforward branch occurrence-volume lines. Duality gives

\[
\mathbb D_V(\mathcal C_D)\simeq\mathcal C_D,
\qquad
\mathbb D_V(\mathcal B_\sigma)\simeq\lambda_\sigma[3].
\]

In words: the conductor is in degree zero after the six ambient volume factors cancel; each smooth three-dimensional branch contributes its own volume in degree minus three. The first conductor row carries the dual of the original difference-orientation line; all other channel lines are likewise dualized, rather than assigned new signs.

The dual of evaluation is the canonical map

\[
\gamma_\sigma:=\mathbb D_V(\epsilon_\sigma):
\mathcal C_D\longrightarrow\lambda_\sigma[3].
\]

In words: gamma is a codimension-three conductor Gysin morphism. It is an Ext-degree-three map, not a degree-zero scalar coefficient map between the two displayed sheaves.

An explicit model is obtained by resolving a branch by the Koszul complex on the opposite three occurrence coordinates and resolving the conductor by the full six-coordinate Koszul complex. Inclusion of the first exterior subcomplex into the second resolves evaluation. Its transpose, with the ambient volume and the ordinary Hom signs, represents gamma. This keeps all three normal comparisons [M2].

The defining construction is B-linear derived duality. The displayed free Koszul matrices are its smooth-ambient models after forgetting to A-modules; a free A-resolution is not falsely given a strict B-action by imposing the quotient on each free term. On the central chart all residue coefficients lie in C[T^-1], so this is a literal free matrix model. On the other charts the intrinsic sheaf maps and the explicit contractions of Section 6 supply descent.

The complete reverse source is

\[
\mathbb D_V(\mathcal S_{14})\simeq
\operatorname{Cone}\!\left(
\chi_{14}:\mathcal C_D^{\oplus15}
\longrightarrow (\lambda_+^{\oplus8}\oplus\lambda_-^{\oplus8})[3]
\right).
\]

In words: the attaching map is the transpose of the actual fifteen-equation normalization matrix, realized by these Gysin morphisms.

With conductor coordinates c-zero and c-j, its branch outputs are

\[
\begin{aligned}
(\chi_{14})_{+,0}
 &=\gamma_+\!\left(c_0-\sum_{\sigma(j)=+}r_jc_j\right),\\
(\chi_{14})_{-,0}
 &=\gamma_-\!\left(-c_0-\sum_{\sigma(j)=-}r_jc_j\right),\\
(\chi_{14})_j&=\gamma_{\sigma(j)}(c_j).
\end{aligned}
\]

In words: each residue appears in the generic branch component, while its own channel retains the conductor Gysin map. This specifies the entire attachment, not just its value on a unit. Multiplication by r-j occurs on the conductor before gamma; it does not require a nonexistent global branch extension of r-j.

The two nonzero cohomology sheaves are

\[
\mathcal H^{-3}\mathbb D_V(\mathcal S_{14})
\cong\lambda_+^{\oplus8}\oplus\lambda_-^{\oplus8},
\qquad
\mathcal H^{-1}\mathbb D_V(\mathcal S_{14})
\cong\mathcal C_D^{\oplus15}.
\]

In words: there are sixteen branch-volume summands and fifteen conductor summands, joined by chi. Cohomology in every other degree is zero. The twelve-channel object has seven volume summands on each sheet and thirteen conductor summands.

These cohomology descriptions follow from the cone triangle. They are **not** a splitting of that triangle. In particular, an Ext-degree-three attaching map cannot be read off by treating the cohomology sheaves as a two-term complex with zero differential.

## 4. Both endpoint attachments remain nonzero

Order the old twelve channels first and the two endpoint channels last. The attaching map has a block form

\[
\chi_{14}=
\begin{pmatrix}
\chi_{12}&R_{\mathrm{end}}\\
0&\operatorname{diag}(\gamma_+,\gamma_-)
\end{pmatrix}.
\]

In words: the quotient retains both endpoint-ideal duals. The off-diagonal block couples them to the generic branch components already present in the twelve-channel source.

Its two nonzero branch entries are

\[
(R_{\mathrm{end}})_+
=-\gamma_+\circ\frac{U_L}{\tau_-},
\qquad
(R_{\mathrm{end}})_-
=-\gamma_-\circ\frac{U_L}{\tau_+}.
\]

In words: these are the full triple-pole endpoint residues, acting on the conductor before the codimension-three Gysin map. No scalar trace, branch erasure, or endpoint identity column has been substituted for them.

For N-end equal to I-plus times the negative endpoint plus I-minus times the positive endpoint, the reverse exact triangle is

\[
\mathbb D_V(\mathcal S_{12})\longrightarrow
\mathbb D_V(\mathcal S_{14})\longrightarrow
\mathbb D_V(\mathcal N_{\mathrm{end}})
\xrightarrow{\epsilon_{\mathrm{end}}^\dagger}
\mathbb D_V(\mathcal S_{12})[1].
\]

In words: restoring endpoints has become a reversed extension with a concrete nonzero connecting morphism. In the free Koszul model, the two off-diagonal blocks have sixteen entries, eight per endpoint. They are coefficient-resolution entries, not sixteen newly added target states.

The previous endpoint calculation proved the exact annihilator of its covariant extension. By the faithful, coefficient-linear coherent duality [M1],

\[
\operatorname{Ann}_{\mathcal B}(\epsilon_{\mathrm{end}}^\dagger)
=
I_++I_-+\mathfrak n_+\mathfrak n_-,
\qquad
\mathfrak n_\pm=(t_s:s\in S_\pm).
\]

In words: exactly the same occurrence tails and mixed-polarity normal products annihilate the reversed endpoint obstruction. This is a theorem about the action of the original ring on a global morphism of coherent complexes. It is not a claim that the extension is nonsplit at every stalk. In fact the original locally split extension can remain globally nontrivial.

Proof of the equality: for each original coefficient b, multiplication commutes with duality. The dual of b times the original connecting morphism is b times its reverse, up to the uniform conventional triangle sign. Faithful biduality makes one zero exactly when the other is zero. The earlier exact annihilator proof and nine polynomial lifting maps therefore transfer without either averaging or introducing a new inverse. Its checker was independently replayed in this calculation.

The explicit residue block is also important when distinguishing two kinds of negative control. Deleting R-end produces the split endpoint extension and still gives a square-zero complex. It has the same local conductor ranks as the actual complex. Thus local ranks alone do not detect this particular global extension. The nonzero global class, and not a dimension count, establishes that the endpoint-compatible reverse triangle does not split.

## 5. Generic-Q and endpoint squares reverse together

The existing source map into the coherent absolute target is

\[
\Phi_{14}:\mathcal S_{14}[3]\longrightarrow F_K|_V,
\qquad
\pi\Phi_{14}=\alpha\rho_{14},
\qquad
\alpha(1)=\theta.
\]

In words: the degree-three source maps into the full 215-state target, and its generic coefficient maps to the actual top Q-cycle. The shift is written in cohomological conventions, so a sheaf shifted by three occupies degree minus three. There is no global unit section of the nonsplit source being silently assumed.

On chart i, the original comparison is the actual formula

\[
\Phi_{14,i}(a,m_i)=a\ell_i+\sum_j(m_i)_j\Gamma_j.
\]

In words: combine the known local Q-lift and its allowed ideal-valued corrections. The new checker re-verifies this local chain equation and the full fourteen-coordinate overlap equality, including both endpoint cells. It checks the corresponding primal equations in the specified PC localizations as well.

For a local dual cochain psi, the transpose is evaluation on these same chains:

\[
\psi\longmapsto
\left(\psi(\ell_i),\quad
m_i\longmapsto\psi\!\left(\sum_j(m_i)_j\Gamma_j\right)\right).
\]

In words: the generic and all fourteen boundary functionals are kept together. The target is the derived ideal dual, not the ring B with the ideals forgotten.

The resulting reverse generic square is

\[
\begin{matrix}
\mathbb D_V(Q)&\longrightarrow&\mathbb D_V(F_K)\\
\downarrow&&\downarrow\\
\mathbb D_V(\mathcal O_V)[-3]&\longrightarrow&
\mathbb D_V(\mathcal S_{14})[-3].
\end{matrix}
\]

In words: the generic projection becomes the upper reversed arrow, and the source generic map becomes the lower reversed arrow. The square commutes because it is the dual of the actual primal square, not because four primitive signatures agree.

Likewise the literal endpoint quotient F-K to F-K/F-V and the source projection S14 to S12 give a compatible reversed endpoint square. Both endpoint factors occur in its relative cone. The checker verifies the normalized free projections and their transposed inclusions, not just maps on cohomology.

This does not assert biduality for the entire noncoherent direct-image PC complex or move duality through derived global sections on the nonproper open. Coherent biduality is used for the coherent source and absolute target. On an individual admitted localized coefficient ring the corresponding coherent construction localizes normally. An identification with the full physical supported PC functor still requires its actual variance-sensitive comparison.

## 6. Explicit chart homotopies, higher compatibility, and grading

On an occurrence chart where X-i is invertible, use the actual conductor Koszul contraction

\[
h_i(\xi)=X_i^{-1}e_i\wedge\xi,
\qquad dh_i+h_id=1.
\]

In words: the conductor becomes empty on that chart, and its resolved coefficient object contracts. The inverse belongs to that chart only, not to the original physical base.

For an ordered list J of available occurrence labels, let h-J be their ordered product. Its complete comparison identity is

\[
dh_J-(-1)^{|J|}h_Jd
=
\sum_{a=1}^{|J|}(-1)^{a-1}h_{J\setminus j_a}.
\]

In words: products of the actual contraction operators supply the homotopies between chart contractions and the higher comparisons between those homotopies. No arbitrary filler is added. Applying the operators to the normalization-resolution map supplies its nullhomotopy on each occurrence chart and its pair/triple compatibility.

The checker verifies 1,792 such attachment-homotopy equations through all three occurrence-chart levels on each sheet. Transposition gives the reversed comparison equations with the Hom and cone signs. The operators do not alter the channel labels, so the endpoint and generic projection squares remain compatible.

All six labelled dihedral actions are checked on the whole ambient free fibre and its reverse, including the determinant of the six-occurrence volume. The first difference row acquires its required sign when the sheets exchange. Each of the fourteen actual residue monomials is transported to its labelled partner. The code also verifies the full eighteen-coordinate fine grading on every differential entry, with dual channel degrees reversed and the ambient volume retained.

## 7. An independent test of the non-split conductor attachment

This section tests an explicitly specified fibre. Let j embed the conductor into the **smooth ambient** occurrence space over the central chart:

\[
j:\operatorname{Spec}\mathcal C[T^{-1}]
\hookrightarrow\operatorname{Spec}\mathcal A[T^{-1}].
\]

In words: set all six short occurrence coordinates to zero while retaining the conductor's allowed normal inverses and the independent long parameters. This is derived tensor product over A, not over the singular ring B. The intrinsic B-conductor fibre would have different, generally unbounded Tor data.

Resolve each of the sixteen branch columns by its three-variable Koszul complex and each of the fifteen conductor rows by its six-variable Koszul complex. The free mapping fibre resolving S14 has ranks

\[
(15,106,273,348,241,90,15)
\]

in homological degrees minus one through five. In words: these 1,088 generators resolve coefficients. The target still has its original 215 geometric loaded states.

After taking the ambient conductor fibre, all occurrence Koszul differentials vanish, but the normalization-comparison maps do not. Their ranks in degrees zero through six are

\[
(15,48,48,16,0,0,0).
\]

In words: the actual comparison supplies nontrivial unit entries even though the coordinate differentials have vanished.

These ranks and saturation are proved over the entire conductor ring, not just a field. In degree zero, choose the positive generic column and all fourteen extra columns; the associated square minor is unit triangular. In positive Koszul degree, the opposite-triple exterior subsets of the two sheets are disjoint. Each column therefore has its own unit pivot row, again with a unit triangular minor. All remaining cokernel coordinates are free. The proof is independent of the numerical residue values and works in every characteristic.

It follows that the cohomology ranks of the **complete reverse complex's ambient derived fibre** are

\[
\left(\operatorname{rk}H^{-6},\operatorname{rk}H^{-5},
\operatorname{rk}H^{-4},\operatorname{rk}H^{-3},
\operatorname{rk}H^{-2},\operatorname{rk}H^{-1}\right)
=(43,177,284,225,90,15).
\]

In words: those are the exact six fibre ranks; there is no degree-minus-seven class. They are not cohomology ranks of the original target or numbers of physical states.

For a negative control, replace the reverse object by

\[
(\lambda_+^{\oplus8}\oplus\lambda_-^{\oplus8})[3]
\oplus\mathcal C_D^{\oplus15}[1].
\]

In words: this has the same two cohomology sheaves but discards their attaching morphism. Its ambient derived fibre has ranks

\[
(15,106,273,348,241,90,15)
\]

in cohomological degrees minus seven through minus one. In words: the comparison differentials that should cancel these extra Tor classes are absent.

In particular,

\[
H^{-7}(Lj^*\mathbb D_V(\mathcal S_{14}))=0,
\qquad
H^{-7}\!\left(Lj^*\bigl(
(\lambda_+^{\oplus8}\oplus\lambda_-^{\oplus8})[3]
\oplus\mathcal C_D^{\oplus15}[1]\bigr)\right)
\cong\mathcal C[T^{-1}]^{\oplus15}.
\]

In words: omitting the full conductor attachment creates fifteen spurious classes in a definite degree. This proves that the full reverse object is not the direct sum of its cohomology sheaves. It is a separate test from the global endpoint-extension obstruction in Section 4.

The q=0 control recovers the earlier alternating-ring Betti sequence (1,9,18,15,6,1). The q=12 source gives (37,153,246,195,78,13). These checks confirm the expected additions of two actual endpoint ideal modules.

## 8. What a physical comparison must now match

The coefficient-side reverse construction now specifies the generic-Q square, both endpoint-relative maps, the full normal-determinant placement, the fifteen conductor constraints, their codimension-three attaching maps, and chart homotopies among their local models.

A proposed identification with this coefficient source must reproduce the endpoint residue block, not merely its scalar image. A map selecting a smaller physical sector is not excluded, but its selection and compatibility with the source differential remain additional mathematical data.

The construction is still the dual of a source selected by the target residue vector. It does not provide an independent spatial correspondence from the native scalar or logarithmic source. The global endpoint obstruction remains nonzero; duality has put it in the correct reversed triangle, not made it disappear. The native comparison must explain how its prescribed supported operation maps to this triangle with the endpoints fixed.

## 9. Verification and provenance

Run:

```sh
python check_marici_endpoint_complete_reverse_cone_20260907.py \
  --output marici_endpoint_complete_reverse_cone_certificate_20260907.json
```

The standalone checker passes **51,635 exact assertions**. It reconstructs the original 215-state absolute and PC differential; rechecks the actual fourteen-family target residues and overlap equations; constructs the 15-by-16 normalization presentation; verifies the full free resolution and transposed cone signs; checks both generic and endpoint reverse maps; verifies the unit-minor fibre calculation; tests all six labelled dihedral actions and the complete fine grading; and supplies explicit occurrence-chart homotopies and their pair/triple compatibility.

The earlier descent-duality checker was independently replayed and passed **50,010** assertions. The earlier normalization-endpoint-extension checker was also independently replayed and passed **120,909** assertions. Their logs and replay certificates were produced in the current runtime. The new checker is standalone and does not execute those prerequisites automatically.

The unbounded polynomial assertions follow from the exact normalization sequence, the complete regular Koszul resolutions, unit-minor arguments, and coherent duality. Residues are treated as independent scalar symbols in the resolution checks before substituting their actual Laurent degrees. No cutoff in polynomial degree is used to define the algebra. This is executable exact verification with mathematical proofs, not proof-assistant certification.

No repository file was modified and no newer repository revision is claimed to have been inspected. The comparison uses the pinned source model already materialized in the previous checked artifacts.

### Preceding checked artifacts

[P1] `marici_normalization_endpoint_extension_20260907.md`: the coherent source S14, its full target comparison, the exact endpoint extension, and its annihilator proof.

[P2] `marici_descent_duality_20260907.md`: the full alternating-ring dualizing complex, scalar-test limitation, fourteen endpoint-sensitive residues, and the cyclic obstruction's supported dual.

[P3] `marici_divisor_complement_descent_20260907.md`: the seven-open local lifts, their genuine target chains, and the labelled residue formulas.

### Mathematical references

[M1] Stacks Project, Section 47.15, tag `0A7A`, especially Lemma 47.15.3: bounded coherent biduality. Lemma 47.15.6, tag `0A7G`: localization of dualizing complexes. These are used for coherent sheaves and their derived morphisms, not to assert duality commutes with nonproper global sections.

[M2] Stacks Project, Section 15.29, tag `0621`: ordered Koszul differential, tensor signs, and exterior insertion identities.

[M3] Stacks Project, Section 13.9, tag `014D`: cone and termwise-split complex conventions. The checker verifies the explicit sign isomorphism between the dual free fibre and the displayed reverse cone.
