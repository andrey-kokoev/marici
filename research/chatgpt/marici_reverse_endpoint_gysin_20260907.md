# The reverse endpoint comparison: a nonzero conductor attachment and two supported Gysin lifts

Date: 2026-09-07  
Lane: Branch B — coefficient descent, the actual endpoint extension, and reverse comparison maps  
Pinned model: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The full derived dual of the previously constructed endpoint sequence now has an explicit normalization–Gysin presentation, including its generic coefficient arrow, all twelve proper-subset channels, and both endpoint channels. Its connecting morphism is nonzero in the **global** derived category but induces zero on every cohomology sheaf. The complete cone differential and its descent data are consequently indispensable.

On the two opposite triple-normal supports, a different, precisely typed result holds. The normalization coordinates supply a splitting of the extraordinarily restricted reverse sequence. Adjunction turns it into two actual supported Gysin lifts into the full reverse endpoint object. They lift the supported counits, not the identity of the unrestricted endpoint object. Their ungraded lifting spaces are nonempty discrete torsors with seven coefficient families on each support.

These are constructions for the target-residue-selected sheaves S12 and S14 on the previously fixed test open V. They do not identify either sheaf with the native physical source, identify V with a physical deformation parameter, construct a new seven-state Q source, or establish the missing spatial normalization/logarithmic correspondence. No target carrier cell has been added. The source, support, variance and degree of every new map are specified below.

## 1. Fixed coefficient geometry

Use the ordered labels

\[
S_+=(13,15,35),\qquad S_-=(02,04,24),\qquad L=(03,14,25).
\]

In words: these orders fix the exterior signs. The short symbols label two occurrence sheets; the long symbols remain independent coefficient directions.

Put

\[
\mathcal C_0=\mathbb Z[X_l,u_l:l\in L],\qquad
\mathcal C=\mathcal C_0[t_s:s\in S_+\cup S_-],
\]

\[
\mathcal B=\mathcal C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: opposite-sheet occurrence products vanish. No relation identifies a long normal with a short normal or an occurrence coordinate.

Keep the previous ideals, products and open:

\[
I_+=(X_p:p\in S_+),\quad I_-=(X_m:m\in S_-),\quad
\tau_+=\prod_{p\in S_+}t_p,\quad \tau_-=\prod_{m\in S_-}t_m,\quad T=\tau_+\tau_-,
\]

\[
V=D(T,\tau_+I_+,\tau_-I_-),\qquad
\mathfrak n_+=(t_p:p\in S_+),\quad \mathfrak n_-=(t_m:m\in S_-),\quad K=\mathfrak n_+\mathfrak n_-.
\]

In words: V has the same common chart and six occurrence charts as before. The normal ideal K is not an occurrence ideal.

The finite normalization maps are \(\nu_\pm:V_\pm\to V\). Their common conductor is

\[
i:D=\operatorname{Spec}\mathcal C[T^{-1}]\hookrightarrow V.
\]

In words: all six short normal parameters are invertible on this conductor **inside V**. This does not invert them globally in the original physical coefficient ring.

Let \(\Gamma_{\sigma,N}\) denote the actual previously computed top boundary family for a nonempty subset N of the opposite short set. The fourteen conductor residues are

\[
r_{\sigma,N}=
\frac{\prod_{l\in L\setminus L_N}u_l}
 {\left(\prod_{n\in N}t_n\right)\left(\prod_{p\in P_N}t_p\right)},
\]

where P_N and L_N are the active short and long labels noncrossing with every element of N. In words: these are the existing target residues, not new chosen functions. They are regular on D. The checker rebuilds their coefficient vectors from all fourteen full target families and retains their long-normal numerators.

For the two endpoints, write

\[
r_+=\frac{U_L}{\tau_-},\qquad r_-=\frac{U_L}{\tau_+},\qquad U_L=u_{03}u_{14}u_{25}.
\]

In words: the endpoint on an active sheet has all three opposite normal poles. Neither numerator is replaced by one.

The input endpoint sequence is

\[
0\longrightarrow\mathcal N\longrightarrow\mathcal S_{14}
\xrightarrow{q}\mathcal S_{12}\longrightarrow0,
\qquad
\mathcal N=\mathcal I_+\Gamma_{+,S_-}\oplus\mathcal I_-\Gamma_{-,S_+}.
\]

In words: q forgets the two endpoint normalization coordinates. The preceding proof establishes its nonzero global extension class \(\varepsilon\) and

\[
\operatorname{Ann}_{\mathcal B}(\varepsilon)=I_++I_-+K.
\]

In words: this is an inherited exact obstruction, not a new assumption that scalar normalizations determine an extension. The predecessor checker was independently rerun for this calculation.

## 2. Present the actual source sheaves using one normalization matrix

For q equal to twelve or fourteen, let \(\Lambda_q\) be its set of channels. Each sheet has q/2 channels. Define

\[
\mathcal F_q=
\nu_{+*}\mathcal O_{V_+}^{\,1+q/2}
\oplus\nu_{-*}\mathcal O_{V_-}^{\,1+q/2},
\qquad
\mathcal C_q=i_*\mathcal O_D^{\,q+1}.
\]

In words: the branch coordinates are \(a_+,a_-\) and their normalization functions z. The conductor coordinates consist of the common-value relation and one relation for every channel. These displayed ranks use the fixed channel frames; the named channel lines are retained under transport.

The actual evaluation matrix is

\[
\begin{aligned}
(A_q(a_+,a_-,z))_0&=\epsilon_+(a_+)-\epsilon_-(a_-),\\
(A_q(a_+,a_-,z))_{+,N}&=\epsilon_+(z_{+,N})-r_{+,N}\epsilon_+(a_+),\\
(A_q(a_+,a_-,z))_{-,N}&=\epsilon_-(z_{-,N})-r_{-,N}\epsilon_-(a_-).
\end{aligned}
\]

In words: require the two generic branch coefficients to agree at the conductor, and require every normalization coordinate to have its prescribed residue there. Multiplication by r occurs on the conductor module; it is not an extension of r as a regular function on an entire branch.

There is an exact sequence of coherent sheaves

\[
0\longrightarrow\mathcal S_q\longrightarrow\mathcal F_q
\xrightarrow{A_q}\mathcal C_q\longrightarrow0.
\]

In words: this is the previously constructed pullback sheaf written without first forming the node module. Evaluation is surjective on stalks; the displayed matrix supplies the same kernel as the original normalization pullback. On an occurrence chart the conductor and the other branch are empty, so S_q is a free module of rank \(1+q/2\) on the surviving branch. On the common chart the original generic coefficient and ideal-valued channels are retained.

Forgetting endpoints is a morphism between these two exact sequences. Keeping only \(a_+,a_-\) and the first conductor row is the actual generic coefficient map to the normalization presentation of \(\mathcal O_V\). No new Q arrow is defined by a rank argument.

## 3. Dualize the normalization matrix, including its attachment

Let

\[
\mathcal A=\mathcal C[X_s:s\in S_+\cup S_-],\qquad
\mathscr D_V=
R\mathcal Hom_{\mathcal A}(\mathcal B,\Omega^6_{\mathcal A/\mathcal C}[6])|_V,
\]

\[
\mathbb D(M)=R\mathcal Hom_V(M,\mathscr D_V).
\]

In words: use the entire six-occurrence ambient volume, rather than ordinary Hom into the singular coefficient ring. The base is regular; this is a dualizing complex with the specified relative normalization. Coherent biduality and its compatibility with finite maps apply [M1].

Let \(\omega_\pm=\Omega^3_{V_\pm/\mathcal C}\), with their ordered determinant identifications. Then

\[
\mathbb D(\nu_{\sigma*}\mathcal O_{V_\sigma})
\simeq\nu_{\sigma*}\omega_\sigma[3],\qquad
\mathbb D(i_*\mathcal O_D)\simeq i_*\mathcal O_D.
\]

In words: a normalization branch contributes its three-dimensional occurrence volume, while the conductor contributes its six-coordinate supported dual. The factors from the full ambient volume and the conormal determinant cancel in the latter identification. The common-difference row remains orientation-odd under sheet exchange; channel rows transform with their channel labels.

Denote the dual of the actual evaluation \(\epsilon_\sigma\) by

\[
g_\sigma:i_*\mathcal O_D\longrightarrow\nu_{\sigma*}\omega_\sigma[3].
\]

In words: g is the codimension-three **occurrence-conductor** Gysin morphism. It is not evaluation of a scalar polynomial. Locally, the ordered Koszul resolution in the three occurrence equations represents it; its top projection is the primitive determinant class [M2, M3].

Put \(\mathcal W_q=\mathbb D(\mathcal F_q)[-3]\) and \(\mathcal E_q=\mathbb D(\mathcal C_q)\). Then

\[
\mathfrak D_q:=\mathbb D(\mathcal S_q)
\simeq\operatorname{Cone}\left(G_q:\mathcal E_q\longrightarrow\mathcal W_q[3]\right).
\]

In words: the dual source is an actual cone of Gysin maps. Replacing it by an unrelated direct sum of its cohomology sheaves discards its attachment.

In the chosen frames, the complete derived matrix is

\[
\begin{aligned}
(G_q(v))_{a_+}&=g_+\left(v_0-\sum_Nr_{+,N}v_{+,N}\right),\\
(G_q(v))_{z_{+,N}}&=g_+(v_{+,N}),\\
(G_q(v))_{a_-}&=g_-\left(-v_0-\sum_Nr_{-,N}v_{-,N}\right),\\
(G_q(v))_{z_{-,N}}&=g_-(v_{-,N}).
\end{aligned}
\]

In words: this is the transpose of the actual normalization matrix, with each evaluation replaced by its supported Gysin. Every long coefficient and every proper-subset or endpoint pole remains. The displayed entries are morphisms in the derived category. The checker replaces them by full finite Koszul resolutions, not by a scalar matrix between degree-zero modules.

Its cohomology sheaves are

\[
\mathcal H^{-3}(\mathfrak D_q)=\mathcal W_q,\qquad
\mathcal H^{-1}(\mathfrak D_q)=\mathcal E_q,
\qquad
\mathcal H^j(\mathfrak D_q)=0\quad(j\notin\{-3,-1\}).
\]

In words: there are two cohomological layers with a nontrivial degree-three attachment between them. Explicitly:

| Object | Degree minus three | Degree minus one |
|---|---|---|
| D(S12) | seven volume copies on each branch | thirteen conductor channels |
| D(S14) | eight volume copies on each branch | fifteen conductor channels |
| D(N) | one endpoint volume on each branch | two endpoint conductor channels |

These are ranks on the indicated supports, not ranks of free O_V-modules. Named channel duals, branch volumes and determinant orientations are implicit in the numerical entries, but not discarded from the construction.

## 4. The complete reverse endpoint triangle

Duality gives

\[
\mathfrak D_{12}\longrightarrow\mathfrak D_{14}
\xrightarrow{v}\mathbb D(\mathcal N)
\xrightarrow{\kappa}\mathfrak D_{12}[1].
\]

In words: reversing the exact endpoint sequence constructs a genuine connecting morphism, rather than a section of the original covariant comparison.

Order the common and proper channels first and the two endpoint channels last. The attaching map has block form

\[
G_{14}=
\begin{pmatrix}
G_{12}&H\\0&G_{\rm end}
\end{pmatrix},\qquad
G_{\rm end}=\operatorname{diag}(g_+,g_-),
\]

\[
H(v_+,v_-)=
\left(-g_+(r_+v_+),\,-g_-(r_-v_-)\right)_{a_+,a_-}.
\]

In words: the only new coupling into the old complex occurs in the two generic branch-volume coordinates. It has precisely the two triple-normal endpoint coefficients. The sign of the resulting connecting map is fixed by the cone convention, not independently fitted to these entries.

### Complete common-chart matrices and local primitives

On D(T), resolve a branch by the Koszul complex in the three opposite occurrence equations, and resolve the conductor by the Koszul complex in all six occurrence equations. Exterior inclusion of the opposite-coordinate wedges lifts each actual evaluation map. Multiplying this lift by the displayed r gives every entry of A_q.

The homological fibre resolution has states F of degree \(|A|\) and conductor states C of degree \(|A|-1\), with differential

\[
d(f,c)=(d_Ff,A_qf-d_Cc).
\]

In words: both the branch resolutions and the conductor resolutions are present. These finite free complexes resolve S_q over the smooth ambient polynomial ring on this chart; their exactness follows from Koszul exactness and the surjectivity of the sheaf sequence. They have 944 and 1088 basis columns for S12 and S14 respectively. These are deliberately nonminimal coefficient resolutions, not new cells of the 215-state target.

Taking the signed Hom differential and the ambient shift gives actual dual matrices. Their degreewise endpoint quotient has 144 columns. The connecting map has sixteen nonzero columns: eight occurrence-wedge columns for each endpoint.

For an endpoint conductor-dual wedge A contained in the opposite occurrence triple, its coefficient in the common generic branch column is

\[
\kappa(C_{\sigma,A}^{\vee})
=(-1)^{|A|+1}r_\sigma F_{a_\sigma,A}^{\vee}.
\]

In words: this is the complete connecting coefficient on that column. The remaining columns have zero off-diagonal component.

On the common chart an explicit degree-zero local primitive is

\[
L_0(F_{\sigma,\mathrm{end},A}^{\vee})
=r_\sigma F_{a_\sigma,A}^{\vee},\qquad
L_0(C_{\sigma,A}^{\vee})=0,
\qquad
\kappa=dL_0-L_0d.
\]

In words: the local comparison is nullhomotopic there. These residue denominators are allowed on D(T), but the same formula is not legal as a global normal-parameter inversion.

### Gluing retains the obstruction

On an occurrence sheet the primal normalization coordinates change from the common-chart ideal coordinates by

\[
(a,m)\longmapsto(a,m+r_\sigma a).
\]

In words: the actual normalization function is its ideal part plus its required conductor residue. The reverse transition is the inverse transpose. Its endpoint-to-generic coefficient is \(-r_\sigma\).

Pure occurrence-chart transitions are identities in these coordinates. The checker verifies all triple-overlap identities and denominator legality on the actual cover, with 7, 12, 8 and 2 nonempty terms in the four successive Čech columns. This retains both endpoint transition functions; it does not infer gluing from one locally exact matrix.

Coherent duality identifies \(\kappa\) with the dual of \(\varepsilon\), with the canonical connecting shift. Hence

\[
\kappa\ne0,\qquad
\operatorname{Ann}_{\mathcal B}(\kappa)=I_++I_-+K.
\]

In words: it is the same nonzero global endpoint class in the reverse comparison, with the same coefficient annihilator. This is not a new independent obstruction. Nonvanishing follows from biduality applied to the proven endpoint extension, not from counting the sixteen nonzero entries of a locally nullhomotopic matrix.

Nevertheless,

\[
\mathcal H^j(\kappa)=0\qquad(j\in\mathbb Z).
\]

In words: the morphism is zero on every **cohomology sheaf**. Its source has degrees minus three and minus one, whereas its target has degrees minus four and minus two. This says nothing about replacing global derived Hom by a stalk calculation. In particular, it does not assert that all global hypercohomology tests vanish.

The endpoint fractions give the previous direct nonzero detector: in the top Čech quotient for the three opposite normal variables, every proper-subset residue vanishes, but \(U_L/(t_1t_2t_3)\) does not. Independent long-normal numerators are not zero divisors in that quotient. The full global correction classification and exact annihilator are inherited from the earlier endpoint proof and transferred by faithful duality [M1, M4].

## 5. Relate this calculation to the preceding normal-residue triangle

The preceding ideal calculation used different closed supports:

\[
W_+=V\cap V(I_-,\mathfrak n_-),\qquad
W_-=V\cap V(I_+,\mathfrak n_+),\qquad W=W_+\sqcup W_-.
\]

In words: on a positive occurrence chart, set the three negative **normal parameters** to zero; the other component is its conjugate. These are not the occurrence conductor D. Indeed

\[
W\cap D=\varnothing.
\]

In words: D inverts all six normal parameters, whereas W sets one of their triples to zero. The assertion is checked on every named chart. No expression with an inverse normal coordinate is specialized to zero.

Let \(j:W\hookrightarrow V\). Locally this is a regular codimension-three immersion, and \(\mathcal K\) is its ideal. The earlier triangle was

\[
\mathcal T[-3]\longrightarrow\mathcal N
\longrightarrow R\mathcal Hom(\mathcal K,\mathcal N)
\longrightarrow\mathcal T[-2],
\]

with both endpoint lines and their opposite-normal determinant duals in T.

Since K is perfect on V, dualizing that **entire triangle** identifies it with

\[
\mathcal K\otimes^L\mathbb D(\mathcal N)
\longrightarrow\mathbb D(\mathcal N)
\longrightarrow j_*Lj^*\mathbb D(\mathcal N)
\longrightarrow(\mathcal K\otimes^L\mathbb D(\mathcal N))[1].
\]

In words: the exact dual of that ideal-dual triangle is the usual derived restriction triangle. It is not an unshifted residue map guessed from its cohomology. The determinant and degree identities follow from regular-immersion duality and perfect tensor–Hom adjunction [M3, M5].

Every arrow of the reverse endpoint triangle is compatible with this restriction triangle. The resulting restricted endpoint sequence splits: on W_sigma the conductor module is zero and the actual normalization coordinates are independent. Omitting one endpoint coordinate is just a projection of free modules. Its specified dual section is insertion into that coordinate.

## 6. Construct the supported reverse endpoint lift

Now apply the **extraordinary** restriction along each \(j_\sigma:W_\sigma\hookrightarrow V\). This is distinct from the ordinary derived restriction in the preceding paragraph.

Let \(\ell_{\mathrm{opp}}\) denote the determinant of its ordered normal conormal bundle. Keep the endpoint family line and define

\[
\Theta_\sigma=
\omega_\sigma|_{W_\sigma}\otimes\Gamma_{\sigma,S_{-\sigma}}^\vee
\otimes\ell_{-\sigma}^{\vee}.
\]

In words: the supported target is the branch occurrence volume, the actual endpoint dual, and the opposite normal determinant dual. It is not an unrestricted scalar line.

Regular-immersion duality cancels the two different shifts here:

\[
j_\sigma^!\mathbb D(\mathcal N)\simeq\Theta_\sigma[0].
\]

In words: the branch dual has its occurrence-volume placement in degree minus three; the normal extraordinary restriction contributes plus three. Their cancellation is derived from the two operations, not an added external grading.

The same operation on the full sequence, in its fixed labelled frames, is

\[
0\longrightarrow\Theta_\sigma^{\,7}
\longrightarrow\Theta_\sigma^{\,8}
\longrightarrow\Theta_\sigma\longrightarrow0.
\]

In words: on each support, one generic branch coordinate, six old channels and the endpoint coordinate remain. Relative channel dual lines and grading shifts distinguish the seven summands; the notation displays their ungraded ranks in the given frames. The projection onto the last coordinate has a specified section. The three surviving occurrence charts have identity transitions, so this section glues on all of W_sigma, not just on separate stalks.

Let that section be \(s_\sigma\). Adjunction constructs

\[
\mathcal R_\sigma=j_{\sigma*}\Theta_\sigma,
\qquad
\lambda_\sigma:
\mathcal R_\sigma
\xrightarrow{j_{\sigma*}s_\sigma}
 j_{\sigma*}j_\sigma^!\mathfrak D_{14}
\xrightarrow{\mathrm{counit}}\mathfrak D_{14}.
\]

In words: first insert the supported endpoint coordinate, then use the actual extraordinary counit. No coefficient is divided by a normal parameter.

Its defining comparison is

\[
v\lambda_\sigma=c_\sigma:
\mathcal R_\sigma\longrightarrow\mathbb D(\mathcal N),
\qquad
\kappa c_\sigma=0.
\]

In words: the new map lifts the supported endpoint Gysin counit through the full reverse object. It does **not** split v over its whole unrestricted domain. The specified splitting supplies the compatible nullhomotopy of the composite with kappa.

### Explicit local roof and its nonzero value

On an occurrence neighborhood of W_sigma, use the full ordered Koszul dual in the three opposite normal parameters:

\[
\mathcal P_\sigma=K(t_{-\sigma})^\vee
\otimes\omega_\sigma\otimes\Gamma_{\sigma,S_{-\sigma}}^\vee[3].
\]

In words: its ranks are one, three, three, one, in cohomological degrees minus three through zero. Both the ordinary and top supported coefficients are present.

The purity map from P to R selects the top dual coefficient and reduces it modulo the three normal parameters. Its other columns are zero. The comparison from P into D14 selects the empty dual coefficient and inserts it in the endpoint branch-volume column. Thus the local roof is

\[
\mathcal R_\sigma\xleftarrow{\simeq}\mathcal P_\sigma
\longrightarrow\mathfrak D_{14}.
\]

In words: this is a supported-dual map, not a map from the original native cycle to a scalar. The purity map kills every boundary because those coefficients lie in the normal ideal. The counit is a chain map, and its composition with v is exactly the ordered codimension-three Gysin generator. That generator is nonzero in local third Ext, so lambda is nonzero. The natural adjunction formulation glues this locally displayed roof without requiring its free resolution to extend as a chosen global free complex.

This is the positive construction obtained in this step. The two endpoint lifts fit one reverse normalization diagram and preserve its previously fixed generic **coefficient** inclusion. They are not a construction of a nonzero native seven-state Q leg from endpoint support alone.

## 7. Compute the supported lifting space rather than claiming uniqueness

For the fixed counit, define

\[
\mathscr L_\sigma=
\operatorname{hofib}_{c_\sigma}
\left(\operatorname{Map}(\mathcal R_\sigma,\mathfrak D_{14})
\longrightarrow\operatorname{Map}(\mathcal R_\sigma,\mathbb D(\mathcal N))\right).
\]

In words: objects are supported reverse endpoint lifts together with the required comparison to the Gysin counit. The constructed lambda supplies a basepoint.

The difference space is the mapping space into D12. Adjunction identifies its mapping complex with seven labelled copies of \(R\Gamma(W_\sigma,\mathcal O_{W_\sigma})\), in the fixed ungraded frames. Therefore

\[
\pi_n(\mathscr L_\sigma)=0\quad(n\ge1),
\qquad
\pi_0(\mathscr L_\sigma)\cong
\Gamma(W_\sigma,\mathcal O_{W_\sigma})^{7}.
\]

In words: the lifting space is nonempty and discrete, but not rigid. The displayed identification uses the specified endpoint-coordinate lift as the origin; without it the set is a torsor. The seven labelled factors include the generic branch-coordinate direction and six old channel directions. Additional physical grading or framing restrictions have not been imposed on these variations.

Explicitly,

\[
\Gamma(W_+,\mathcal O_{W_+})=
\mathcal C_0[t_p^{\pm1}:p\in S_+][X_p:p\in S_+],
\]

with the conjugate formula for W-. In words: W+ is the punctured three-occurrence affine space over this normal-localized base. Functions extend across its omitted regular codimension-three zero section; the coordinate Čech complex or regular-sequence calculation proves the formula. Positive sheaf cohomology in that punctured space is not asserted to vanish, but it contributes no negative Ext and hence no positive homotopy groups in this unshifted lifting space [M4].

The two supports are disjoint, so the simultaneous endpoint lifting space is the product of these two spaces. There are fourteen ungraded coefficient families of ambiguity, with the corresponding determinant and endpoint labels retained. This is not a claim of fourteen additional physical states.

## 8. Why the supported success does not remove the global obstruction

The normal support W is disjoint from the occurrence conductor D which carries the normalization attachment. Every supported projection used above therefore kills that conductor input. This explains the new splitting without contradicting the nonzero global kappa.

In particular, both statements hold:

\[
\kappa\ne0,\qquad j^!\kappa=0.
\]

In words: the full reverse comparison retains the endpoint-coherence obstruction, while its specified supported restriction admits the new lift. A calculation that records only the latter cannot recover the former.

The generic coefficient inclusion is explicit throughout:

\[
\mathbb D(\mathcal O_V)\longrightarrow\mathfrak D_{12}
\longrightarrow\mathfrak D_{14}.
\]

In words: in normalization–Gysin cones it is the inclusion of the two a-volume coordinates and the common-difference conductor row. It is the dual of the existing map \(\mathcal S_q\to\mathcal O_V\theta\). It does not identify that top coefficient map with an independently constructed native physical source or with the entire Q complex.

The missing physical comparison has consequently become a more concrete matching problem: carry the native generic data into this fixed generic arrow, match the complete Gysin attachment G14 (including both triple-normal endpoint coefficients), and supply the necessary selection among supported lifts using native grading, support and endpoint constraints. Matching only the supported unit values or the cohomology-sheaf ranks is insufficient. No such native identification is claimed here.

## 9. Verification and reproduction

Run:

```sh
python check_marici_reverse_endpoint_gysin_20260907.py \
  --output marici_reverse_endpoint_gysin_certificate_20260907.json
```

The standard-library checker is standalone. It passes **49,961 exact assertions**. The checks include:

- all absolute and PC differential identities of the existing 215-state target and closure of all fourteen target families;
- the full common-chart ambient resolutions and signed dual differentials for the base, S12, S14 and N;
- the complete reverse endpoint and generic coefficient maps, all sixteen connecting columns and their explicit local primitives;
- every labelled dihedral transport with exterior and ambient-volume signs;
- actual normalization inverse-transpose transitions, all triple comparisons and denominator legality across the twenty-nine-intersection cover;
- 512 exact integral occurrence-Koszul multidegree/localization calculations, including empty strands;
- the opposite-normal support chart test, the ordered normal purity and counit maps, the supported endpoint lift and its seven local variation directions.

The preceding endpoint-multiplier checker was independently rerun and passed **73,866 exact assertions**. Its rerun certificate hash is recorded in the new certificate. Source model filenames and the pinned repository commit retain their previous scope. No current repository-head audit or repository write was performed.

The checker does not infer global nonvanishing from a local matrix, infer infinite exactness from bounded exponents, or infer sheaf gluing from an index contraction. Global nonvanishing is proved by coherent biduality of the already established extension. Arbitrary-polynomial exactness is proved by the actual normalization sequence and the regular Koszul resolutions. Sheaf gluing is given by the explicit normalization matrices and supported adjunction. This is executable algebra with a mathematical proof, not proof-assistant certification.

## References

[P1] `marici_normalization_endpoint_extension_20260907.md`: S12, S14, the fourteen residue functions, the full target map and the original endpoint class.

[P2] `marici_endpoint_multiplier_coherence_20260907.md`: the exact endpoint annihilator, codimension-three normal support triangle and all-power multiplier obstruction.

[P3] `marici_descent_duality_20260907.md`: the full occurrence-relative dualizing complex and the distinction from scalar coefficient Hom.

[P4] `supported_gysin_proof.md` (Branch A): the independently constructed ordered pair supported dual, its actual counit and the exclusion of a direct native scalar trace. The present three-normal construction concerns different supports and is not identified with that native pair.

[M1] Stacks Project, *Dualizing complexes*, tag `0A7A`, especially coherent biduality and finite-map dualizing complexes: https://stacks.math.columbia.edu/tag/0A7A.

[M2] Stacks Project, *The Koszul complex*, tag `0621`: https://stacks.math.columbia.edu/tag/0621.

[M3] Stacks Project, Cartier-immersion duality, tag `0B4B`, iterated in an ordered regular triple: https://stacks.math.columbia.edu/tag/0B4B.

[M4] Stacks Project, *Global derived Hom*, tag `0B6A`: https://stacks.math.columbia.edu/tag/0B6A.

[M5] Stacks Project, *Properties of upper shriek functors*, tag `0ATZ`: https://stacks.math.columbia.edu/tag/0ATZ.
