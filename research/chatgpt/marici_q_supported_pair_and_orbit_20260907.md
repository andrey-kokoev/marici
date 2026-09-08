# Supported duality on the filtered Q lifting problem

Date: 2026-09-07  
Lane: fixed 215-state target and coefficient-linear lifting; Branch B  
Repository inputs: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The already supplied ordered `(t04,t35)` dual comparison has a computable action on the six coefficient-linearity defects. Each old defect becomes a boundary in the actual dual tensor complex, with an explicit polynomial primitive. This statement retains endpoint terms and is stronger than simply observing that a coefficient vanishes after substitution.

It does not solve the supported lifting problem. Recomputing the target after this non-flat change gives different answers for the absolute and PC/Cech coefficient models. In the absolute model no nonzero generic multiple lifts. In the PC model the exact lifting ideal has four, rather than six, remaining Rees factors. Its new lifting module still has a nonzero coefficient-linearity extension class.

There is also a constructive positive result. The three labelled rotations of the supplied pair give a well-defined composite supported-duality functor. On the full PC target its generic seven-state quotient becomes an actual direct summand, with a strict coefficient-linear section. This composite has codimension six, its corresponding duality shift, and the tensor product of the three ordered normal/endpoint lines. It is not identified here with the native physical normalization kernel. In particular, success after the three-pair operation does not show that one pair already succeeds, or that the native source carries permission to apply the composite.

These results concern actual complexes and their coefficient maps, not a numerical amplitude or a claim about RH. No new cell is attached to make a class exact. No Rees parameter is replaced by one or inverted outside a source-prescribed localized summand.

## 1. Retained ring, target and generic class

The short and long labels are

\[
 S_+=\{13,35,15\},\qquad S_-=\{02,24,04\},\qquad
 S=S_+\sqcup S_-,\qquad L=\{03,14,25\}.
\]

In words: the alternating sheets have three short labels each; the three long labels remain independent normal directions.

Put

\[
 \mathcal C=\mathbb Z[t_s\ (s\in S),X_l,u_l\ (l\in L)],\qquad
 \mathcal B=\mathcal C[X_s:s\in S]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: products of positive-degree occurrences from opposite sheets vanish. The Rees parameters and long parameters remain polynomial spectator variables. The ring is free over the spectator ring, with the constant and the two single-sheet monomial families as basis.

Let the two branch ideals be

\[
 I_+=(X_p:p\in S_+),\qquad I_-=(X_m:m\in S_-),\qquad I=I_++I_-.
\]

In words: positive branch functions remain legal coefficients. For a short label the normal is the actual product `u_s=t_s X_s`; long occurrences and normals are still independent.

Use the supplied loaded generators `[F,H]`, with noncrossing F and H a subset of F. Their homological degree and absolute differential are

\[
 |[F,H]|=3-|F|+|H|,
\]

\[
 d[F,H]=\sum_a(-1)^{\#\{b\in F:b<a\}}X_a[F+a,H]
 +\sum_{h\in H}(-1)^{3-|F|+\operatorname{pos}_H(h)}u_h[F,H-h].
\]

In words: add an allowed face label or remove a normal mark, with the source incidence and exterior signs. The PC realization instead has cell ring

\[
 \mathcal B[u_a^{-1}:a\in F\setminus H],
\]

radial coefficient `X_a/u_a`, and normal-removal coefficient one. In words: inverses belong to the indicated summands; they are not global inverses on the base. The diagonal finite-to-PC map multiplies the cell by the inverse product of its unmarked normals.

Retain the complete support sequence

\[
 0\longrightarrow A_\partial=F_B/F_V\longrightarrow
 E=F_K/F_V\xrightarrow{\pi}Q=F_K/F_B\longrightarrow0.
\]

In words: the sixteen endpoint states are retained before taking the stated quotients. The full carrier has 215 states, and Q has seven. Every sequence is split on the underlying graded summands, so its derived coefficient changes retain the triangle even when the coefficient change is not flat.

Write

\[
 U_L=\prod_{l\in L}u_l,\qquad
 \theta=U_L[\varnothing,\varnothing]
 -\sum_{l\in L}X_l\prod_{j\in L\setminus\{l\}}u_j[\{l\},\{l\}].
\]

In words: theta is the genuine top polynomial cycle in Q. The long-normal equations show `H_3(Q)=B theta`, both before and after the short-Rees supports used below. This is not the earlier degree-one exact Morse roof or the conductor-common-value marking.

Its four-term lift has boundary beta in the supported part. Before imposing the pair support beta has eighteen terms. The previous exact results were

\[
 \operatorname{Ann}_{\mathcal B}[\beta]
 =\mathfrak a=(\tau_+\tau_-,\tau_+I_+,\tau_-I_-),\qquad
 \tau_\pm=\prod_{s\in S_\pm}t_s,
\]

\[
 \operatorname{Ann}_{\mathcal B}(\mathfrak e)=I+(\tau_+\tau_-).
\]

In words: the first obstruction tests an individual generic lift, and the second tests a coefficient-linear choice of all already-liftable multiples. The latter is the extension class of the top lifting module. Its explicit six defects and the full target presentation are the input to this calculation [A1].

## 2. Use the actual supported-dual operation

The supplied comparison from the parallel source calculation uses

\[
 s=t_{04},\qquad t=t_{35},\qquad Z=\{04,35\},\qquad
 \overline{\mathcal B}=\mathcal B/(s,t).
\]

In words: these are independent spectator Rees coordinates even though the labelled diagonals cross. No face containing both is postulated. The ring's freeness over its spectator variables makes the pair a regular sequence.

Its ordered resolution P has homological ranks `(3,4,1)` in degrees `(0,1,2)` and matrices

\[
 P_2=\mathcal Bz,\quad P_1=\mathcal B^4,\quad P_0=\mathcal B^3,
 \qquad
 d_2=\begin{pmatrix}t\\s\\t\\s\end{pmatrix},\quad
 d_1=\begin{pmatrix}0&-t&s&0\\1&0&-1&0\\0&1&0&-1\end{pmatrix}.
\]

In words: this is the source's four-column conductor comparison, not an invented resolution chosen from the new obstruction. Its integral contraction onto ordered `K(s,t)` is given in [A2]. In those frames the dual normal unit is `eta=-z^vee`.

Use the cohomological dual with differential `-d_1^T,d_2^T`. The purity map, with the source's endpoint and determinant lines retained, is

\[
 \mathcal G_E:P^\vee\otimes_{\mathcal B}E
 \longrightarrow
 (E\otimes_{\mathcal B}^{L}\overline{\mathcal B})[-2]
 \otimes L_\partial^\vee\otimes([s]\wedge[t])^\vee,
\]

\[
 \mathcal G_E(z^\vee\otimes v)=-\overline v.
\]

In words: extract the dual top coefficient with its ordered sign, then restrict to the supported base. Other dual columns map to zero. The corresponding counit selects the first degree-zero dual column. The two arrows constitute the supported roof; there is no asserted direct scalar trace on native gamma or on an unrestricted coefficient polynomial. Cartier duality supplies the degree and line placement [M1, M2].

The checker verifies the full tensor differential, purity, counit, endpoint/Q projections and the finite-to-PC square on all `8*215` tensor columns in both coefficient models. The induced maps retain both endpoint cubes until the stated supported coefficient rings or endpoint quotients make a summand zero. Their compatibility is with the actual support diagram, not a newly assigned primitive signature.

The independent long normal `u03` is not set to one, paired away, or identified with the physical channel orientation. Where the native packet also includes an external `K(u03)^vee`, tensor every map here with its identity. The chain equations remain valid, and both external grades on its derived resonance fibre remain present. The calculation below works before that further resonance restriction and does not rename the specialized theta as a different primitive generator.

## 3. Explicit primitives for all six old defects

Write the old lifts as Lambda-zero and Lambda-plus/minus. A positive defect is

\[
 D_p=X_p\Lambda_0-\tau_-\Lambda_+(X_p).
\]

In words: compare the two ways to lift the old common-to-branch coefficient relation. The negative version uses the opposite sheet. It has 24 terms in E and 25 when its endpoint term is retained in the full carrier.

Every face in Lambda-zero misses at least one member of Z, because the members cross. The coefficient for such a missing label contains its Rees factor. Consequently Lambda-zero is zero on the pair support. Each second summand also contains one supported Rees factor. Thus all six old defects have coefficients in the ideal `(s,t)`.

The following supplies actual primitives before specialization. Split the polynomial terms, assigning terms divisible by s first, to obtain

\[
 D=sA+tB,\qquad dA=tC,\qquad dB=-sC,\qquad dC=0.
\]

In words: divide only terms known to belong to the indicated principal ideals. Regularity of s and t proves the second set of identities from closedness of D. This is division on an ideal, not inversion of a base parameter.

Let the ordered Koszul dual have bases `1; alpha_s,alpha_t; Omega`, with

\[
 d1=-s\alpha_s-t\alpha_t,\qquad
 d\alpha_s=-t\Omega,\qquad d\alpha_t=s\Omega.
\]

In words: these are the dual signs inherited from the source's ordered resolution. With the dual degree supplying the tensor sign,

\[
 W=\alpha_t\otimes A-\alpha_s\otimes B-1\otimes C,
 \qquad dW=\Omega\otimes D.
\]

In words: the two first primitives and their comparison term cancel every unwanted boundary. Under the source projection dual, Omega maps to eta. In its original dual-column bases this becomes

\[
 W_P=-e_1^\vee\otimes A-e_2^\vee\otimes B-r_0^\vee\otimes C,
 \qquad dW_P=\eta\otimes D.
\]

In words: each old defect is now a boundary in the supplied dual tensor object. All six original-coordinate primitives are exported in the certificate. They have 25 or 28 terms in the full carrier, including endpoint terms. Projecting to E and applying the legal localization maps preserves the equations.

This proves the vanishing of these six transformed cycles. It does not assert that the entire derived base change of the old extension sequence is split, that all higher relations among the chosen primitives have disappeared, or that a stronger frozen-endpoint homotopy condition is satisfied. In particular, all seven old generic coefficients specialize to zero. A new unit lift cannot be inferred from their vanishing.

## 4. Recompute the supported target, not just its old homology

### 4.1 The absolute target

Suppose a closed top chain in the absolute supported E projects to `k theta`. Its empty-face coefficient is `k U_L`. The singleton-face equations for 04 and 35 give

\[
 X_{04}kU_L=0,\qquad X_{35}kU_L=0.
\]

In words: the two corresponding normal differentials now vanish, but their radial equations do not. The first equation forces k into the positive branch ideal; the second forces it into the negative branch ideal. Their intersection is zero and the long product is a non-zero-divisor. Hence

\[
 \operatorname{im}(H_3(E_{\mathrm{abs},Z})\to H_3(Q_Z))=0,
 \qquad
 \operatorname{Ann}_{\overline{\mathcal B}}[\beta_{\mathrm{abs},Z}]=(0).
\]

In words: the absolute supported primary class is faithful. This is not the PC answer.

### 4.2 The PC target and its actual support decomposition

If a PC summand inverts `u04=s X04`, it also inverts s. Its restriction to s equal to zero is the zero module. The same holds for 35. Since the original summands are flat localizations, termwise coefficient restriction computes their derived restriction [M3]. One must not evaluate a Laurent inverse at zero, or silently retain the absolute singleton equations on a zero PC summand.

The original alternating PC diagram already has 15 zero stalks. This pair creates 52 additional zero stalks. Its 148 nonzero full-carrier stalks divide into three strict subcomplexes by

\[
 T=F\cap Z=H\cap Z\in\{\varnothing,\{04\},\{35\}\}.
\]

In words: any surviving supported label must still be marked. Adding it unmarked or removing its mark goes into a zero summand, so the differential never changes T. There are 86, 31, and 31 nonzero stalks in these three blocks. Both endpoint blocks are retained; together they have eight nonzero supported endpoint stalks before taking E.

The generic quotient lies in the empty-T block, denoted `E_Z^0`. The other two blocks remain as direct summands of the complete target and cannot cancel a defect in this block. Before accounting for its five pre-existing zero rings, this block has 91 loaded labels and 23 top labels. No endpoint lies in this block.

Set

\[
 \sigma_+=t_{13}t_{15},\qquad \sigma_-=t_{02}t_{24}.
\]

In words: these are the unremoved parameters on the two sheets. The exact new lifting ideal is

\[
 \mathfrak a_Z=(\sigma_+\sigma_-,\sigma_+I_+,\sigma_-I_-),
 \qquad
 \operatorname{Ann}_{\overline{\mathcal B}}[\beta_{\mathrm{PC},Z}]=\mathfrak a_Z.
\]

In words: common coefficients require all four remaining Rees factors; positive branch functions require their own remaining two. The unit still does not lift. The explicit PC representative of beta now has twelve terms.

For necessity, on a remaining active short label the PC singleton equation expresses the fully marked coefficient as the negative branch projection of `k U_L/t_s`. Since that fully marked coefficient is still polynomial, its branch projection must be divisible by t_s. Applying every active singleton gives divisibility by sigma-plus or sigma-minus. Taking the common conductor value makes it divisible by both disjoint products. The decomposition into a common constant and the two positive-degree branch parts then gives exactly the stated ideal.

For sufficiency, construct new cycles in the actual empty-T subcomplex. Let `epsilon_F=(-1)^(|F|(|F|+1)/2)` and write

\[
 \Lambda_0^Z=\sum_{F\cap Z=\varnothing}\epsilon_F
 \left(\prod_{s\in(S\setminus Z)\setminus F}t_s\right)
 \left(\prod_{l\in F\cap L}X_l\right)
 \left(\prod_{l\in L\setminus F}u_l\right)[F,F].
\]

In words: use actual noncrossing faces avoiding the supported labels. For the positive lift, restrict the sum to faces in `(S_plus minus Z) union L`, replace the short product by that positive subset, and multiply by any positive branch function. Do the same on the negative side.

These seven cycles have respectively 23 terms and six times 12 terms. Their generic coefficients are the seven ideal generators. Direct differential cancellation proves their closedness in the supported PC target. They are not absolute supported cycles, and they are not obtained by dividing the seven old classes by s or t. In particular the old common cycle is zero on the support, while this newly reconstructed common cycle is nonzero.

## 5. The new coefficient-linearity obstruction

The new seven generators still have six common-to-branch relations. On the positive side their lift defect is

\[
 D^Z_p=X_p\Lambda_0^Z-\sigma_-\Lambda_+^Z(X_p).
\]

In words: the first supported operation removed two normal factors, not the need for these coefficient multiplication squares to commute. Each new defect is a nonzero eleven-term top cycle in the empty-T boundary block. Its terms are not the specialized old defect, which was zero.

The complete ambiguity module in that block is

\[
 M_Z^0=H_3(A_{\partial,Z}^0)
 \cong I_+^{\oplus3}\oplus I_-^{\oplus3}.
\]

In words: the labels are the nonempty subsets of the two remaining opposite-sheet short labels. These are ideal-valued families, not six free lines over the whole alternating ring.

Here is an explicit all-degree decomposition. For a nonempty subset N of the remaining negative short labels, let P_N be the remaining positive labels compatible with all of N, and let L_N be the compatible long labels. Define

\[
 \Gamma^Z_{+,N}=\sum_{N\subseteq F\subseteq N\cup P_N\cup L_N}\epsilon_F
 \left(\prod_{p\in P_N\setminus F}t_p\right)
 \left(\prod_{l\in F\cap L}X_l\right)
 \left(\prod_{l\in L_N\setminus F}u_l\right)[F,F].
\]

In words: multiplying this displayed vector by a positive branch function gives a boundary-supported top cycle. The three choices of N have disjoint negative-support labels. The reflected vectors give the three negative families.

To prove completeness, decompose each top coefficient into its common, positive, and negative polynomial parts. If its generic coefficient is zero, the common part and the active-sheet-only faces vanish by the singleton recurrences. For each fixed nonempty inactive set N, the remaining long and active-short equations force precisely the products displayed in Gamma. Different inactive sets never mix. This gives a direct sum of the six stated ideals. It is an integral divisibility argument; it does not require that the alternating ring itself be a domain.

The defect decomposes in these actual independent families as

\[
 D^Z_p=\sum_{\varnothing\ne N\subseteq S_-\setminus Z}
 c^Z_{+,N}X_p\Gamma^Z_{+,N},
\]

\[
 c^Z_{+,N}=
 \left(\prod_{m\in(S_-\setminus Z)\setminus N}t_m\right)
 \left(\prod_{q\in(S_+\setminus Z)\setminus P_N}t_q\right)
 \left(\prod_{l\in L\setminus L_N}u_l\right).
\]

In words: all three opposite-subset components appear. The certificate checks their sum against the eleven-term target vector, not merely against its homology class. For example,

\[
 \operatorname{coeff}_{[\{02\},\{02\}]}D^Z_{13}
 =-X_{13}\,t_{13}t_{15}t_{24}\,U_L.
\]

In words: the first occurrence symbol lacks t02. It cannot be absorbed by the full opposite product `sigma_minus=t02*t24`.

Consider arbitrary changes of lifts. Their defect correction is

\[
 (D^Z_p)' - D^Z_p=X_pm_0-\sigma_-m_p,
 \qquad m_0,m_p\in M_Z^0.
\]

In words: this accounts for every correction within the relevant block, including ungraded and nonequivariant ones. Other T-block corrections have zero projection to this block. Reducing to `M_Z^0/(I M_Z^0+sigma_minus M_Z^0)` kills both possible correction terms but retains the nonzero first-occurrence symbol of the defect.

The exact monomial colon calculations are

\[
 ((\sigma_-):c^Z_{+,N})=\left(\prod_{n\in N}t_n\right),\qquad
 \bigcap_{\varnothing\ne N\subseteq S_-\setminus Z}
 \left(\prod_{n\in N}t_n\right)=(\sigma_-).
\]

In words: the complete positive symbol is annihilated exactly by the remaining negative product. The negative symbol has the positive product as its annihilator. No conductor evaluation that loses first occurrence order is substituted for this calculation.

Consequently the new top lifting sequence has class

\[
 0\longrightarrow M_Z^0\longrightarrow H_3(E_Z^0)
 \longrightarrow\mathfrak a_Z\longrightarrow0,
 \qquad \mathfrak e_Z\in\operatorname{Ext}^1_{\overline{\mathcal B}}
 (\mathfrak a_Z,M_Z^0),
\]

\[
 \operatorname{Ann}_{\overline{\mathcal B}}(\mathfrak e_Z)
 =I+(\sigma_+\sigma_-),\qquad
 \overline{\mathcal B}\,\mathfrak e_Z
 \cong\mathcal C/(s,t,\sigma_+\sigma_-).
\]

In words: a nonzero conductor-supported four-normal extension class remains. It has infinite additive order and remains nonzero over the rationals. It obstructs even an ungraded coefficient-linear choice of all already-liftable multiples, not just an invariant choice of representatives.

The reverse inclusion in this annihilator has explicit witnesses. Use the free seven-generator presentation of the ideal, with relation-image map kappa. For each short occurrence a, map the common free generator to its defect D-a and the other six to zero. On all thirty ideal relations this equals `X_a kappa`. For the product `sigma_plus sigma_minus`, map the common generator to zero, each positive generator to `-sigma_plus D_p`, and each negative one to `-sigma_minus D_m`. On the entire relation module this is the product times kappa. The first-symbol calculation proves that no other conductor coefficient annihilates the extension.

The seven ideal generators have thirty defining relations: six common-to-branch relations, six same-sheet Koszul relations and eighteen opposite-sheet annihilator relations. Each of the six ambiguity ideals has three generators and twelve relations. Therefore the new generic-block lifting module has a complete presentation with **25 generators and 102 relations**. Completeness follows by projecting any relation to the ideal and then using the direct ambiguity decomposition; all 102 relation vectors are verified as exact zeros in the target. The certificate exports them and all 25 actual cycles.

This is the precise sense in which the boundary relations have now been retained rather than thrown away. It is not a constructed morphism from the native normalization source into this presentation.

## 6. A constructive completion on the full rotated support

### 6.1 Independently define the composite functor

Rotate the *given labelled pair*, rather than choosing divisors from the desired answer. The three pairs are

\[
 Z_{03}=(04,35),\qquad Z_{25}=(02,15),\qquad Z_{14}=(24,13).
\]

In words: rotations by two and four hexagon vertices give the other two copies of the supplied normal-pair comparison. These are six disjoint polynomial parameters. Each pair has its transported ordered resolution, determinant line and endpoint frame.

Let P-i be these three comparison resolutions, and define

\[
 \mathcal F_{\rm orb}(E^{\rm PC})=
 (P_{03}^\vee\otimes P_{25}^\vee\otimes P_{14}^\vee)
 \otimes_{\mathcal B}E^{\rm PC},
\]

\[
 \mathcal F_{\rm orb}(E^{\rm PC})\simeq
 (E^{\rm PC}\otimes_{\mathcal B}^{L}\mathcal B_6)[-6]
 \otimes\mathscr L_{\rm orb},
 \qquad \mathcal B_6=\mathcal B/(t_s:s\in S).
\]

In words: compose all three supplied types of supported-dual operation, retaining their tensor product of orientation lines. The line `L_orb` is the product of the three endpoint-dual lines and three ordered conormal determinant duals. The degree-six support placement is not reset to degree zero without acknowledgement.

This equivalence follows by tensoring the three explicit regular-pair purity maps; bounded flat target summands justify each derived tensor [M2, M3]. It is a composition of operations, not a product of three already evaluated scalar answers. The uncollapsed resolutions remain the source of its comparison roof.

Interchanging two degree-two normal blocks has sign plus one. Under the physical reflections `v -> 3-v mod6` and their two rotations, the total conormal determinant and the product of endpoint lines have compensating signs. The checker verifies this labelled orientation calculation and the six orders of support restriction on every target cell. All long-normal modules, including u03, remain unchanged; any independently retained external normal complex is tensored by the identity. There is no additional normal-to-channel identification.

### 6.2 The entire Q complex now has a strict section

After all six supports, every PC summand with an unmarked short label is zero. Thus each surviving summand satisfies

\[
 F\cap S=H\cap S.
\]

In words: its entire short-face support must remain marked. The differential preserves that support. The empty-short-support summand is precisely the seven-state Q complex, with its original long-normal differentials and coefficient localizations.

Consequently, putting the common support shift and orientation line aside only for the following unshifted notation,

\[
 E^{\rm PC}\otimes_{\mathcal B}^{L}\mathcal B_6
 =Q_{\mathcal B_6}^{\rm PC}\oplus A_{\partial,\mathcal B_6}^{\rm PC},
\]

\[
 j_Q:Q_{\mathcal B_6}^{\rm PC}\longrightarrow
 E^{\rm PC}\otimes_{\mathcal B}^{L}\mathcal B_6,
 \qquad dj_Q=j_Qd,\qquad \pi j_Q=1.
\]

In words: include all seven generic states with their existing coefficients. Every outgoing short-radial term has a zero coefficient module, so this is an actual chain map and a strict section of the quotient. No mixed face was erased while leaving a nonzero boundary behind. The differential and the stalkwise support condition prove the section.

In particular,

\[
 d(j_Q\theta)=0,\qquad \pi(j_Q\theta)=\theta.
\]

In words: the generic unit finally lifts, coefficient-linearly, in the triple-transformed PC target. Both the individual lifting obstruction and the linear-selection obstruction vanish there.

The full supported carrier has 72 nonzero coefficient summands: 7 generic and 65 with nonempty marked short support. Both endpoint summands survive in their top normal grade; the other fourteen original endpoint summands have zero supported stalks. After the defined endpoint quotient, E has 70 summands and its boundary part has 63. These are counts of nonzero coefficient summands, not free ranks of localization rings. The endpoint diagrams and their natural maps have not been replaced by two prescribed numbers.

The absolute complex does not acquire this section under the same support: its nonzero short-radial equations remain. The PC localization/supported-fibre combination is essential to the result.

### 6.3 What this positive completion does not prove

The composite above acts on a different supported coefficient object and has an explicit degree-six duality placement. The native physical normalization packet has **not** been shown to admit a comparison through its triple-dualized domain, with the required generic leg and both fixed endpoint connectors. A global source can assemble its three local objects by descent rather than tensoring all three into one object; this distinction cannot be inferred from the existence of their rotations.

Therefore the result is a concrete candidate target-side completion, not a proof that the physical problem is solved. It also does not identify the generic theta with the physical endpoint unit z, or show that every lift in the ungraded full supported moduli problem is unique. The strict section proves existence and a canonical support-defined choice; other boundary summands remain.

What changed is nevertheless substantive: the required coefficient-linear completion is no longer just an abstract desired map. Its explicitly defined triple-supported target, strict generic section, full endpoint diagram and orientation placement are now available for a source comparison to test.

## 7. The all-support control calculation

For any set Z of short Rees coordinates, let the remaining products be

\[
 \sigma_\pm(Z)=\prod_{s\in S_\pm\setminus Z}t_s.
\]

In words: only parameters not placed on the chosen support enter these products. The same singleton argument and explicit new cycles give the exact PC lifting ideal

\[
 \mathfrak a_Z^{\rm PC}=
 (\sigma_+(Z)\sigma_-(Z),\sigma_+(Z)I_+,\sigma_-(Z)I_-).
\]

In words: this gives the target-side progression for every one of the 64 coordinate supports. It is a theorem about these explicit coefficient diagrams; it does not authorize an arbitrary support operation on a native geometric source.

For the absolute model, if Z meets both sheets the image ideal is zero. If Z is a nonempty subset of the positive sheet, the image is `tau_minus I_minus`; the negative version is symmetric. For empty Z it is the previous six-factor ideal. These statements follow because a zeroed absolute normal imposes annihilation by its occurrence variable, whereas its zeroed localized PC row disappears. They are independently checked against exact top kernels, including supports other than the physical pair.

Along the three-pair orbit the PC common factor has successively six, four, two, and zero remaining Rees factors. After the third pair its product is one, consistent with the strict seven-state section just constructed.

## 8. Reproduction, exact checks and qualifications

Run:

```sh
python check_marici_q_supported_pair_20260907.py --output marici_q_supported_pair_certificate_20260907.json
```

The checker is standalone and uses Python's standard library. The full run passes **446,156 exact assertions**. It checks the complete dual tensor equations and their coefficient/support maps; exports all six old-defect primitives; computes the 25-generator/102-relation supported lifting presentation; performs 439 integral fine-degree presentation/kernel comparisons; computes 10,206 exact top kernels covering all 64 supported-normal patterns; and checks labelled covariance and the strict seven-state section after the rotated composite.

The top-kernel calculations are integral, not ranks modulo a sample prime. After the explicit top-face orientation rebase, every nonzero row has either one unit entry or two opposite unit entries. Connected components give the entire integer kernel, while singleton rows force components to zero. The presentation calculations also verify that every nonzero Smith factor of the tested relation/image matrices is one. The arbitrary-polynomial conclusions come from the divisibility, direct-sum and presentation proofs above, not extrapolation from test degrees.

The preceding 43-generator/174-relation checker was independently rerun and passed its **138,416** assertions. Source artifact hashes are recorded in the new certificate. No claim is made that the parallel branch's entire native computation or all of its geometry was re-executed. This is executable exact verification plus algebraic proof, not proof-assistant certification. No repository file was changed.

## References and precise source boundary

[A1] `marici_q_graded_lift_naturality_20260907.md` and `check_marici_q_lift_naturality_20260907.py`: old seven-generator ideal, 43-generator lifting module, six top-cycle defects and non-splitting. Input hashes are in the certificate.

[A2] `supported_gysin_proof.md`, uploaded library version 1, 2026-09-07: ordered `(t04,t35)` comparison matrices, Koszul reduction, dual purity sign, endpoint determinant lines, retained independent resonance normal, and tensor naturality on the complete native/retained/old-target diagrams. Its source qualification is retained: the operation is on the dual comparison resolution, not a direct native scalar trace.

[A3] Marici at the pinned commit: `check_ringed_alexandrov_pc_target.py`, Entry 93's alternating normalization ring, Entry 115's short Rees graph, and Entry 400's ordered ray/sheet frame. The present checker uses the previously supplied full target formulas and does not infer an unrecorded source-to-target arrow from a signature match.

[M1] Stacks Project, Koszul complexes, tag 0621: https://stacks.math.columbia.edu/tag/0621 . Ordered exterior signs, tensor products and Koszul homotopies.

[M2] Stacks Project, Cartier duality, tag 0B4B: https://stacks.math.columbia.edu/tag/0B4B . The supported dualizing shift and normal line, iterated for independent regular parameters.

[M3] Stacks Project, Derived tensor product, tag 06XY: https://stacks.math.columbia.edu/tag/06XY . Bounded flat/free models and derived coefficient changes.
