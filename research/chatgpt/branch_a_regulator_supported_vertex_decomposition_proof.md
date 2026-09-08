# Branch A: regulator-supported vertex decomposition, primary framing, and the two-normal obstruction

Date: 2026-09-07.

## Result and scope

The supported difference constructed in the previous regulator-zero calculation has an explicit decomposition into nine vertex-local maps. The complete occurrence-weight-zero supported comparison group has fourteen independent classes. They are not fourteen choices of a primitive of the same primary chain: fixing that primary leaves a rank-two polynomial module, and the two endpoint-top coefficients detect it by a unimodular matrix.

After quotienting the two endpoint packets, the original supported difference remains nonzero on eight other vertices. Its proposed two-normal extension still fails there. Removing endpoint objects does not solve the compatibility equation.

This calculation concerns the unit-normalized regulator coefficient family with beta retained. It does not extend the source's fixed-nonzero-beta geometric purity theorem to beta zero, and it does not identify the physical conductor–Morse class.

## 1. Coefficients, degrees, and the complete support diagram

Let

\[
R=\mathbb Z[\beta,X_{02},X_{03},X_{04},X_{13},X_{14},X_{15},X_{24},X_{25},X_{35}]
 /(X_eX_o:e\in S_-,\ o\in S_+),
\]

where

\[
S_-=(02,04,24),\qquad S_+=(13,15,35).
\]

The formal exponential graph has

\[
u_d=e^{\beta X_d}-1=\beta X_dv_d,\qquad v_d(0)=1.
\]

Only the invertible factors \(v_d\) have been absorbed into native normal frames. Thus the retained native and occurrence equations are

\[
dh_d=\beta X_dp_d,\qquad dh_{\mathrm{occ}}=X_{35}p_{\mathrm{occ}}.
\]

No beta or occurrence coordinate is inverted in any constructed comparison. The integer polynomial model verifies the coefficient identities; returning to exponential frames is performed by the recorded unit changes over characteristic-zero formal coefficients.

The full complex \(C_\beta\) has 430 states

\[
[F,H,\epsilon],\qquad H\subset F,\quad\epsilon\in\{0,1\},\qquad
\deg[F,H,\epsilon]=3-|F|+|H|+\epsilon.
\]

The ordered diagonals are \((02,03,04,13,14,15,24,25,35)\). The face \(F\) is an actual noncrossing dissection. Its differential has radial coefficients \(X_a\), native coefficients \(\beta X_h\), and the separately signed occurrence coefficient \(X_{35}\). Both complete endpoint packets \(V\), the short-boundary subcomplex \(B_{\mathrm{sh}}\), and the quotient \(Q\) remain:

\[
\#C_\beta=430,\qquad\#V=32,\qquad\#B_{\mathrm{sh}}=416,\qquad\#Q=14.
\]

These are restrictions of the complete differential, not projections onto a selected generic edge. The checker verifies every differential column and all subcomplex identities.

All computations called “weight zero” fix the nine occurrence multidegrees at zero and leave arbitrary polynomial beta powers. A state's required occurrence coefficient is

\[
X^{F-H-\epsilon\{35\}}.
\]

It contributes precisely when these exponents are nonnegative and the monomial survives the mixed-sheet ideal. Consequently the complete component has ranks

\[
(8,59,108,56)
\]

in homological degrees zero through three and has no degree-four term. This is a free complex over \(\mathbb Z[\beta]\), not a finite beta-jet approximation.

## 2. Fourteen explicit supported vertex maps

Let \(\mathfrak T\) be the fourteen maximal triangulations. For \(F=(a_1<a_2<a_3)\in\mathfrak T\), put

\[
E_F=[F,F,0],\qquad
B_F=\sum_{j=1}^3(-1)^{j-1}X_{a_j}[F,F\setminus\{a_j\},0].
\]

Because a maximal face has no further radial coface,

\[
dE_F=\beta B_F,\qquad dB_F=0.
\]

Place the regulator source in degrees three and two:

\[
S_\beta=[Re\xrightarrow{\beta}Rp].
\]

Define

\[
\Gamma_F(p)=B_F,\qquad\Gamma_F(e)=E_F.
\]

These are genuine maps of complexes. Each remains on one actual vertex and contains all three native-normal lower terms. The fourteen maps have 56 nonzero entries in total.

For every maximal face the two rows

\[
E_F=[F,F,0],\qquad E_{F,\mathrm{occ}}=[F,F,1]
\]

form a quotient complex

\[
Q_F=[R\xrightarrow{-X_{35}}R]
\]

in degrees four and three. No discarded radial or native differential enters a fully marked maximal face. The checker verifies this for all 430 source columns, separately for all fourteen faces.

In cohomological degrees minus two, minus one, and zero,

\[
\operatorname{Hom}(S_\beta,Q_F)=
\left[R\xrightarrow{(-X_{35},-\beta)^T}R^2
\xrightarrow{(\beta,-X_{35})}R\right].
\]

Hence

\[
H^0\operatorname{Hom}(S_\beta,Q_F)=R/(\beta,X_{35}).
\]

The image of \(\Gamma_G\) is \(\delta_{FG}\). Conversely, the homotopy sending \(p\) to \(E_F\) kills \(\beta\Gamma_F\). Composing with the occurrence multiplication homotopy kills \(X_{35}\Gamma_F\). Therefore these maps determine an explicitly split submodule

\[
\bigoplus_{F\in\mathfrak T}R/(\beta,X_{35})[\Gamma_F]
\hookrightarrow H^0\operatorname{RHom}_R(S_\beta,C_\beta).
\]

Every indicated annihilator is exact. This is a classification of the displayed full-ring summand, not a claim that it exhausts all occurrence degrees of the entire Hom complex.

The native ordered normal wedges and the source beta-normal generator fix the signs. Returning to unnormalized formal normal frames retains the corresponding invertible determinant factors.

## 3. The homogeneous supported comparison group is exhausted by these maps

For a cochain of degree \(k\), write its two components as

\[
f=(a,b),\qquad a\in C_{\beta,2-k},\quad b\in C_{\beta,3-k}.
\]

The complete Hom differential is

\[
\delta f=(da,db-(-1)^k\beta a).
\]

The checker constructs all 462 columns of this homogeneous polynomial Hom complex. Its ranks in degrees \((-1,0,1,2,3)\) are

\[
(56,164,167,67,8).
\]

Reduction \((a,b)\mapsto\bar b\) is a cochain comparison to the reindexed central complex, with differential inherited from \(d\). The usual cohomological shift is obtained by the conventional degree-dependent sign isomorphism. Since beta acts injectively on every target module, this comparison is a quasi-isomorphism. Equivalently, it is the one-parameter Koszul/Cartier duality calculation retaining the source normal basis.

The complete central component has

\[
H_1(C_0)_{(0)}=\mathbb Z^6,\qquad
H_2(C_0)_{(0)}=\mathbb Z^{21},\qquad
H_3(C_0)_{(0)}=\mathbb Z^{14}.
\]

All fourteen degree-three basis cycles are exactly \(E_F\). There are no degree-four states in this weight, so the degree-three kernel itself is their integral span.

Consequently

\[
H^0\operatorname{RHom}_R(S_\beta,C_\beta)_{(0)}
=\bigoplus_{F\in\mathfrak T}\mathbb Z[\Gamma_F].
\]

This assertion also has a direct polynomial normal-form proof. If \(f=(A,H)\) is a closed homogeneous map, then

\[
H\bmod\beta=\sum_Fc_FE_F.
\]

Define the polynomial chain

\[
U_f=(H-\sum_Fc_FE_F)/\beta.
\]

The numerator is termwise divisible by beta; this is not localization. The chain equation gives

\[
f-\sum_Fc_F\Gamma_F=\delta(U_f,0).
\]

Thus the coordinates \(c_F\) are complete invariants. This normal-form homotopy generally changes the primary component \(A\) by a boundary. It is not automatically a homotopy in a problem fixing the primary chain pointwise.

## 4. Decompose the previously computed difference and retain its comparison cells

The inherited maps are

\[
F_{03}(p)=F_\mu(p)=A_\beta,\qquad
F_{03}(e)=H_\beta,\quad F_\mu(e)=G_\beta,
\]

with

\[
dH_\beta=dG_\beta=\beta A_\beta,\qquad
Z_\beta=G_\beta-H_\beta,\qquad dZ_\beta=0.
\]

The checker embeds the labelled fifteen-term \(H_\beta\), reconstructs its 21-term primary, and recovers the thirty-term \(G_\beta\) and forty-five-term \(Z_\beta\). It verifies all equations independently.

The complete structural formula is

\[
\Psi_\beta=\sum_F(-1)^{|F|(|F|+1)/2}\beta^{3-|F|}[F,F,0],
\qquad Z_\beta=P_\beta\Psi_\beta,
\]

where \(P_\beta\) replaces a native 35-mark by beta times its distinct occurrence partner, kills states carrying both, and otherwise acts as the identity.

Let \(\mathfrak T_0=\{F\in\mathfrak T:35\notin F\}\). Its nine elements are

```text
02 03 04
02 04 24
02 24 25
03 04 13
04 13 14
04 14 24
13 14 15
14 15 24
15 24 25
```

The exact polynomial identity is

\[
F_\mu-F_{03}-\sum_{F\in\mathfrak T_0}\Gamma_F
=\delta(U,0),
\qquad
U=(Z_\beta-\sum_{F\in\mathfrak T_0}E_F)/\beta.
\]

The chain \(U\) has 36 terms. Its lower equation is

\[
dU=-\sum_{F\in\mathfrak T_0}B_F.
\]

The endpoint component is the original positive occurrence top

\[
U_V=E_{+,\mathrm{occ}}=[\{13,15,35\},\{13,15\},1].
\]

The Q-comparison is

\[
\pi_QU=\beta^2T-\beta(h_{03}+h_{14}+h_{25}),
\qquad
\pi_QZ_\beta=\beta\,\pi_QU.
\]

Its endpoint-quotient component has the required six connecting terms:

\[
\kappa(U_E)+d_VU_V=-B_{V_-},
\qquad V_-=(02,04,24).
\]

These are checked identities in the full complex. They show precisely how the normal-form homotopy moves lower and endpoint comparison data. Discarding them would falsely turn this ordinary supported-map equivalence into a frame-preserving equivalence.

Both original maps have explicit individual normal forms. \(F_{03}\) has coefficients \(-1\) on the two faces \(\{02,03,04\}\), \(\{03,04,13\}\), zero elsewhere. \(F_\mu\) has coefficient \(+1\) on the other seven faces of \(\mathfrak T_0\). Their difference is the nine-face indicator above. Their primary Bockstein values agree, as required by their identical primary chain.

## 5. Fixing the primary leaves two directions, detected by the endpoints

If two maps have exactly the same primary chain, their top difference must be a closed degree-three chain in \(C_\beta\). The complete polynomial cycle module in the tested weight is

\[
Z_3(C_\beta)_{(0)}
=\mathbb Z[\beta]\Psi_\beta\oplus\mathbb Z[\beta]Z_\beta.
\]

Proof: after beta is inverted for the purpose of this proof, native normal rescaling identifies the component with its beta-one model. The complete integral contraction of that model gives rank two in degree three, and \(\Psi_1,Z_1\) are a unimodular basis. The rescaling sends \(\Psi_\beta,Z_\beta\) to \(\beta^3\Psi_1,\beta^3Z_1\). For an original polynomial cycle, its coefficients in this Laurent basis are polynomial, because they are recovered by the two endpoint-top coefficients. Beta has no torsion on the original chain modules, so the equality descends without localization. No constructed primitive or map uses beta inverse.

The endpoint-top matrix, with columns \((\Psi_\beta,Z_\beta)\) and rows the negative and positive fully native-marked tops, is

\[
\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]

Its determinant is \(-1\). Therefore a homogeneous degree-three cycle with both endpoint-top coefficients zero is the zero chain.

It follows that two primitives of the same primary with the same full endpoint coefficients are equal in this polynomial homogeneous component. There is no degree-four term in the component, so no hidden degree-four representative ambiguity is being suppressed.

The fourteen supported-map classes from Section 3 are therefore not fourteen ambiguities of a fixed primary-and-endpoint problem. Most change the primary class.

## 6. The first Bockstein gives the exact separation

The first beta-Bockstein is

\[
\mathcal B_1:H_3(C_0)_{(0)}\longrightarrow H_2(C_0)_{(0)},
\qquad [E_F]\longmapsto[B_F\bmod\beta].
\]

Its complete matrix is \(21\times14\). The checker supplies unimodular row and column matrices reducing it to twelve unit Smith factors and zero elsewhere.

Every nonzero row is the oriented difference on an actual flip edge of the triangulation graph. Of the twenty-one flip edges, precisely the five changing the distinguished 35-diagonal have zero row. The remaining sixteen edges form two connected components, on nine triangulations without 35 and five triangulations containing 35.

Thus

\[
\ker\mathcal B_1
=\mathbb Z\mathbf1_{35\notin F}\oplus\mathbb Z\mathbf1_{35\in F}.
\]

Both kernel vectors have the full polynomial closed lifts \(Z_\beta\) and \(\Psi_\beta-Z_\beta\). Hence this first obstruction is a complete lifting test for central degree-three cycles in this weight; neither vector has a later beta obstruction.

The negative endpoint belongs to the nine-vertex component; the positive endpoint belongs to the five-vertex component. Fixing one coefficient in each therefore fixes both components.

The coefficient exact sequence for beta gives

\[
0\longrightarrow\mathbb Z^2
\longrightarrow H^0\operatorname{RHom}(S_\beta,C_\beta)_{(0)}
\longrightarrow H_2(C_\beta)_{(0)}[\beta]
\longrightarrow0,
\]

with

\[
H_2(C_\beta)_{(0)}[\beta]\cong\mathbb Z^{12}.
\]

The first map consists of differences admitting a closed top lift; the last map records the primary class. This distinguishes the mapping problem fixing the primary from unrestricted homotopy of supported maps.

In particular, subtracting just the negative endpoint from the central chain does not give an endpoint-free closed family:

\[
\mathcal B_1[Z_0-E_{V_-}]=-[B_{V_-}]\ne0.
\]

The obstruction is already first order in beta.

## 7. Quotienting endpoints leaves eight detected components

As a separate, explicitly changed target problem, form \(\bar C_\beta=C_\beta/V\). Its full homogeneous supported comparison group is

\[
H^0\operatorname{RHom}(S_\beta,\bar C_\beta)_{(0)}\cong\mathbb Z^{12}.
\]

The twelve basis classes are the maximal vertices other than the two physical endpoints. This follows from the complete central quotient reduction; its central homology is \((4,17,12)\) in degrees one, two, three.

The original difference projects to

\[
[\bar F_\mu-\bar F_{03}]
=\sum_{F\in\mathfrak T_0\setminus\{V_-\}}[\bar\Gamma_F]\ne0.
\]

These are eight nonendpoint vertices. The sum has a strict representative supported only on those vertices and hence zero endpoint and Q coefficients. However, obtaining that representative uses the explicit comparison of Section 4 and occurs in the endpoint-quotient problem. It does not remove the original full-target endpoint discrepancy by a frame-preserving homotopy, nor does it keep the original primary chain pointwise fixed.

## 8. The two-normal equation still fails after this quotient

The attempted \(K(\beta,\beta)\) assignment retaining the two original primitives requires

\[
dY=\beta\bar Z_\beta.
\]

For any of the eight nonendpoint faces in Section 7, the corresponding fully marked vertex quotient remains a valid quotient of \(\bar C_\beta\). It sends the right side to beta, while the only degree-four boundary is multiplication by \(-X_{35}\). Therefore it forces

\[
-X_{35}y=\beta.
\]

Modulo \((X_{35},\beta^2)\), the left side is zero and the right side is nonzero. This gives eight separately recorded nonzero coordinates of the one proposed lifting obstruction. They are not eight independent obstructions for independently chosen input pairs.

Thus the failed two-normal extension is not explained solely by the negative endpoint. It persists on the interior-of-the-short-boundary vertex packets after both endpoint packets have been removed.

## 9. Interpretation and next admissible question

The calculation separates the following facts:

- The ordinary regulator-supported difference has a source-defined nine-vertex normal form.
- The entire tested homogeneous supported comparison group has fourteen coordinates.
- Fixing the primary leaves two polynomial cycle directions, both detected by the endpoint frame.
- An endpoint quotient retains a nonzero eight-vertex image, but it changes the comparison problem and does not solve the two-normal top equation.

All displayed vertex-local maps lie in the short-boundary subcomplex. They have zero Q projection. The Q component of the original supported difference is removed only through its recorded Q homotopy, not through a declaration that the isolated generic-edge coefficient is a homology class.

No physical \(\Delta_J\) is selected here. In this homogeneous coefficient family, a nonzero difference retaining the same primary and both endpoint coefficients is excluded. A proposed physical construction must explicitly change or refine a specified input—such as the coefficient degree or the support-changing correspondence—and supply its actual comparison maps. The number of supported classes alone does not supply such a construction.

## 10. Verification and provenance

Run the self-contained checker:

```sh
python branch_a_regulator_supported_vertex_decomposition_checker.py \
  --output branch_a_regulator_supported_vertex_decomposition_certificate.json
```

The checker uses only the Python standard library. It reconstructs all 430 states, every family differential, fourteen complete vertex maps and their target quotient detectors, the entire 462-state homogeneous Hom complex, all central support reductions, the generic degree-three calculation, and the complete Bockstein matrix with unimodular Smith witnesses. It also reconstructs both original packet maps and all normal-form homotopies and endpoint/Q corrections.

It verifies 20,223 exact identities. Selected high-beta monomial examples are only controls; the unbounded assertions use the polynomial normal-form proof, the exact homogeneous components, and the unimodular kernel calculation. No truncated search is used as proof of all-degree nonexistence.

Repository inputs, pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: radial/native differential, face labels, and support subcomplexes.
- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: separate occurrence-Koszul correction.
- `research/voevodsky/check_d03_formal_support_purity.rs`: the normal graph and fixed-nonzero-beta scope of geometric purity.
- Entry 93, *Alternating Fusion Normalization-Conductor Square*: mixed-sheet coefficient relations.
- Previous local artifact `branch_a_d03_beta_zero_excess_and_endpoint_checker.py`: the fifteen-term packet primitive embedded here in labelled form; all relevant equations are reverified.

Conventions and general facts:

- Stacks Project, tag 0A8H, Hom complexes: https://stacks.math.columbia.edu/tag/0A8H
- Stacks Project, tag 0621, Koszul complexes: https://stacks.math.columbia.edu/tag/0621
- Stacks Project, tag 0B4B, effective-Cartier duality: https://stacks.math.columbia.edu/tag/0B4B

The finite integer matrices and polynomial witnesses prove the statements of this document. The general references fix the categorical and sign conventions; they do not independently state these new computations.
