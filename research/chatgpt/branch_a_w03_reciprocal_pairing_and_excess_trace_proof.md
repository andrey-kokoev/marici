# Branch A: reciprocal normal pairing detects the W03 excess and its source relations

## Result and scope

The prescribed reciprocal/original pairing, applied only to the two common native normals 02 and 35, gives a chain isomorphism by currying. It retains the separate occurrence-35 factor and the complete opposite-edge factor, including W25.

Evaluation at the closed reciprocal basepoint then defines a smaller chain map. On the established local supported-map basis its matrix is

\[
\mathcal T_{0*}:
(\beta\mathcal P,\mathcal E,\mathcal R)
\longmapsto
\begin{pmatrix}0&1&0\\0&0&1\end{pmatrix}
\]

in the target basis \((\nu_E,\nu_R)\). Both target classes are primitive and independent. Thus

\[
\mathcal T_0(\mathcal G_E^+)=\nu_E\ne0,
\qquad
\mathcal T_0(\Pi_0\mathcal G_E^+)=0.
\]

In words: reciprocal evaluation distinguishes the original conductor map from the operation that deletes its native/occurrence excess. The original primary readout, together with this two-coordinate evaluation, detects all three local class coordinates.

This is the unlocalized normal-factor part of the project's bivariant construction. It is not the full tangential Pochhammer--Cousin trace, an unrestricted scalar residue, a nonzero generic Q-leg, or an identification with the physical Delta_J. The complete spatial six-functor comparison remains separate.

## 1. Coefficients and the full local source

Use

\[
R=\mathbb Z[\beta,X_d:d\in\{02,03,04,13,14,15,24,25,35\}]/(I_-I_+),
\]

\[
I_-=(X_{02},X_{04},X_{24}),\qquad
I_+=(X_{13},X_{15},X_{35}),\qquad A=R/(I_-+I_+).
\]

The full ambient coefficient complex has 430 states, including all 32 physical endpoint states and the actual fourteen-state Q-quotient. Native normal differentials are beta X_d; the independent occurrence-35 differential is X35. This is the unit-normalized polynomial normal-graph model. Its extension across beta=0 is algebraic, not an extension of a fixed-nonzero-beta geometric purity theorem.

The source is the free conductor resolution P_A[2], with ranks 1,6,24,92 in degrees 2,3,4,5. Its first equations are

\[
de_i=X_i p_A,
\qquad
dc_{ij}=X_i e_j-X_j e_i
\]

for same-sheet i<j, and

\[
dm_{ni}=X_n e_i
\]

for opposite-sheet n,i. All 92 compatibility equations among the 24 relations are included. Exactness of the continued resolution follows from the alternating-word construction: splitting coefficients into constant, positive-sheet, and negative-sheet pieces decomposes the augmented complex into shifted polynomial-sheet Koszul resolutions. The target ends in degree four, so the displayed source terms suffice for every map and homotopy equation used here.

The opposite edge and its endpoints are

\[
E=\{02,35\},\quad W_{03}=\{02,03,35\},\quad W_{25}=\{02,25,35\}.
\]

Write x=X03, v=X25, y=X02, and z=X35. Its complete 40-state packet factors as

\[
C_E=P_E\otimes K_R(\beta y,\beta z)\otimes K_R(z).
\]

The five-state interval factor has

\[
dg=xp_{03}+vp_{25},\quad
dh_{03}=\beta xp_{03},\quad
dh_{25}=\beta vp_{25}.
\]

In words: both edge endpoints remain. The closed combination is

\[
\xi=h_{03}+h_{25}-\beta g.
\]

Let a,b be the native 02 and 35 generators and k the separate occurrence generator:

\[
da=\beta y,\quad db=\beta z,\quad dk=z,
\qquad \eta=b-\beta k,\quad d\eta=0.
\]

The prior supported classes, reconstructed in this checker, are

\[
\mathcal P(p_A)=z\xi a,
\qquad \mathcal P(e_i)=X_i\xi ak,
\]

\[
\mathcal E(p_A)=0,
\qquad \mathcal E(e_i)=X_i\xi a\eta,
\]

for positive-sheet i, with negative-sheet generator and relation values zero. The map R agrees with E on e13 and e15, is zero on e35, and has

\[
\mathcal R(c_{i,35})=X_i\xi abk,\qquad i=13,15.
\]

Every source equation holds. The original map is the literal sum

\[
\mathcal G_E^+=\beta\mathcal P+\mathcal E.
\]

## 2. Use the actual reciprocal pairing, with its units

For native normal i, the source prescribes

\[
u_i^\vee=-q_i^{-1}u_i,
\qquad
\mathcal B_i(p_i,h_i^\vee)=1,
\qquad
\mathcal B_i(h_i,p_i^\vee)=-q_i.
\]

In words: reciprocal and original support/twist types remain distinct. Only the monodromy units q_i are inverted. No u_i, occurrence coordinate, or beta inverse is used.

The checker first works over the Laurent-unit extension of R with q02,q35. The native differentials are u02=beta y and u35=beta z; reciprocal differentials are -q_i^{-1}u_i. The formulas specialize to the actual graph monodromies because their identities do not require treating q_i as a new occurrence parameter.

For integral coefficient calculations use the invertible reciprocal frame

\[
\bar p_i^\vee=-q_i^{-1}p_i^\vee,
\qquad \bar h_i^\vee=h_i^\vee.
\]

Then

\[
d\bar h_i^\vee=u_i\bar p_i^\vee,
\qquad
\mathcal B_i(p_i,\bar h_i^\vee)
=\mathcal B_i(h_i,\bar p_i^\vee)=1.
\]

This is a change of basis in the reciprocal object, not an identification of support variances. In particular the reciprocal test vector below is

\[
\bar p_{02}^\vee\bar p_{35}^\vee
=(q_{02}q_{35})^{-1}p_{02}^\vee p_{35}^\vee.
\]

The raw two-normal complementary-degree pairing has determinant -q02^2 q35^2. The normalized matrix, in the basis 1,a,b,ab and the corresponding reciprocal basis, is

\[
\begin{pmatrix}
0&0&0&1\\
0&0&1&0\\
0&-1&0&0\\
1&0&0&0
\end{pmatrix},
\]

with determinant -1. The ordered native-normal orientation (02,35) remains explicit. Reordering both factors changes the orientation by -1; the code verifies every complementary pairing entry under that reordering.

## 3. The full reciprocal transformation is invertible

Let D_N denote the four-state normalized reciprocal native pair. Retain its entire differential. Let

\[
T=(P_E\otimes K_R(z))\otimes\mathfrak o_{02,35}[2].
\]

In words: T has ten states. It retains the interval and occurrence factor, with the ordered native-pair orientation and its homological shift. The orientation line has occurrence weight eps02+eps35 and regulator-normal weight two.

The bilinear map is

\[
\mathcal B:C_E\otimes D_N\longrightarrow T.
\]

For native occupancy bits n02,n35, reciprocal bits r02,r35, and occurrence bit e, it vanishes unless n_i+r_i=1. Its normalized coefficient when nonzero is

\[
(-1)^{n_{35}r_{02}+e(r_{02}+r_{35})}.
\]

In the raw reciprocal basis multiply this by

\[
(-q_{02})^{n_{02}}(-q_{35})^{n_{35}}.
\]

In words: the occurrence partner contributes its actual tensor-interchange sign even though it is not paired or removed.

The checker verifies this map against all 160 input differential columns. Currying yields

\[
\mathcal D:C_E\xrightarrow{\cong}\operatorname{Hom}(D_N,T).
\]

The matrix and its inverse each have 40 states. Both are checked with the full Hom differential, in the raw reciprocal basis and the normalized basis. Thus no class of the original local mapping complex is lost by currying itself.

The source maps P,E,R are curried on the full conductor resolution. All six annihilator equations and all relation equations survive. No scalar evaluation on a single nonclosed reciprocal normal generator is substituted for this map.

## 4. Evaluation at a closed reciprocal basepoint detects two classes

The vector bar p02^vee bar p35^vee is closed. Evaluate the curried map on it:

\[
\mathcal T_0:C_E\longrightarrow T.
\]

In the normalized coefficient basis, T0 selects the double-native-mark component while retaining the edge and occurrence components. This is a genuine chain map.

It gives

\[
\mathcal T_0\mathcal P=0,
\qquad
\mathcal T_0\mathcal E=\nu_E,
\qquad
\mathcal T_0\mathcal R=\nu_R.
\]

The two nonzero maps have exact formulas

\[
\nu_E(p_A)=0,
\qquad \nu_E(e_i)=X_i\xi\quad(i=13,15,35),
\]

and

\[
\nu_R(p_A)=0,
\quad \nu_R(e_i)=X_i\xi\quad(i=13,15),
\quad \nu_R(e_{35})=0,
\]

\[
\nu_R(c_{i,35})=X_i\xi k\quad(i=13,15).
\]

Their other columns are zero. They contain nine and twelve polynomial terms, respectively, in the factored target basis.

The complete Hom matrices, with the two normal-orientation weights temporarily suppressed, are:

| Reduced regulator grade | Hom dimensions (+1,0,-1) | Differential ranks | H0 rank |
|---:|---|---|---:|
| 0 | (2,18,50) | (2,16) | 0 |
| 1 | (6,46,94) | (6,38) | 2 |
| 2 | (6,46,94) | (6,38) | 2 |

The six homotopy-boundary columns together with nu_E and nu_R form an integral basis of the grade-one cycle lattice, with determinant +1 in the exported free-coordinate basis. This proves independence and exhaustiveness, not just nonvanishing of sample columns.

No output state has more than one native mark. Multiplication by beta identifies the entire homogeneous Hom complexes in every successive reduced grade from one onward. Consequently the trace target is free on nu_E,nu_R over Z[beta]. Restoring the paired orientation weight places both in the original regulator grade three.

The original source map therefore gives nu_E, whereas its collapsed beta P gives zero. Using the unrescaled reciprocal basepoint multiplies both trace coordinates by the prescribed unit q02 q35; it does not change nonvanishing.

The original primary readout is nonzero on P and zero on E,R. Together with T0 it gives the identity coordinate matrix on the three established local basis classes. A fixed primary alone cannot distinguish E and R; the reciprocal test can.

The component at the reciprocal b35-bar generator is not separately a chain map, since that reciprocal vector is not closed. For the original G it has unit-source image beta z xi and zero first-generator images. Its complete Hom differential is beta z times nu_E. This verifies where the primary data are retained by the full curried transform even though the closed-basepoint trace kills P.

## 5. Their difference is a source-relation class

Let U be the degree-one map homotopy with

\[
U(e_{35})=-\xi k,
\]

and every other value zero. Define kappa_rel on the three mixed relation generators by

\[
\kappa_{\mathrm{rel}}(m_{n,35})=X_n\xi k,
\qquad n\in\{02,04,24\},
\]

and zero elsewhere. The checker verifies

\[
\nu_E-\nu_R-\delta U=\kappa_{\mathrm{rel}},
\qquad \delta\kappa_{\mathrm{rel}}=0.
\]

In words: trying to equate the two traces by changing the e35 homotopy leaves three mixed-source relation columns. They cannot be discarded.

The integral class detectors evaluate kappa_rel to (1,-1) in the basis (nu_E,nu_R). It is a primitive nonzero relation-only map. Its six source-generator values and its conductor-unit value are all zero.

## 6. Retain W25 and apply the same Cartier functor to source and target

The full output factor retains h25 and p25. Quotienting their two occurrence-completed states gives the six-state relative target. Its connecting map has

\[
\kappa_{25}(g)=X_{25}p_{25}.
\]

Every trace map satisfies

\[
d_{25}F_{25}+\kappa_{25}F_{\mathrm{rel}}=F_{25}d_{P_A}.
\]

For example, nu_E(e_i) has W25 component Xi h25 and relative component Xi(h03-beta g). Their native and radial boundary terms cancel. They remain in the certificate separately.

Apply i_x^! for x=X03 to both source and relative target. The signed Cartier Hom model is

\[
\mathscr H_x(C)_n=C_n\oplus C_{n+1},
\qquad D(a,b)=(da,xa-db).
\]

The counit is (a,b) maps to a; purity sends (a,b) to b modulo x, with the homological shift -1 and the dual conormal line. The source is therefore

\[
i_x^!(A[2])\simeq A/(x)[1]\otimes\mathfrak n_x^\vee.
\]

The checker verifies the trace-map chain equations in these full Cartier Hom models and both the counit and purity naturality squares. It never leaves the source unchanged while changing the target.

The complete relative-divisor homogeneous Hom has dimensions (4,28,44), differential ranks (4,20), and H0 rank four. The two transported trace classes, together with all homotopy boundaries, have a saturated unit minor of determinant -1. Hence both nu_E and nu_R survive the correctly source-shifted Cartier operation as a saturated rank-two submodule. The two additional relative-divisor classes are not claimed to come from the full edge.

All constructions stay on the opposite-edge support and retain the physical endpoint and Q frames. The physical reflection transports (02,35) to the ordered pair (13,04), moves W25 to W14, and takes the occurrence-35 factor to occurrence-04. Re-sorting the transported native pair requires the explicit determinant sign above. It is not an automorphism silently fixing the 35-corrected complex.

## 7. Consequence for the remaining physical identification

The normal-factor reciprocal pairing does not erase the native/occurrence excess. Full currying is invertible. The closed-basepoint evaluation detects both zero-primary local classes and distinguishes the source-specified G from the collapsed map.

This gives three independent coefficient tests for a proposed realization: its original primary coordinate, its nu_E coordinate, and its nu_R coordinate, including the mixed source-relation components. The recorded map passes with coordinates (1,1,0) in (beta P,E,R).

The calculation does not construct the complete tangential/occurrence trace of Entry 97, which has its own support type and nonresonant localization. It does not select a generic Q-leg or identify a physical conductor--Morse difference. A spatial Gysin comparison must realize these computed normal-factor and source-relation values with its own endpoint comparison cells.

## Reproduction

Run the standalone checker:

```sh
python branch_a_w03_reciprocal_pairing_and_excess_trace_checker.py --output branch_a_w03_reciprocal_pairing_and_excess_trace_certificate.json
```

Only the Python standard library is required. No other artifact, network call, or package is read. This execution verifies 20,513 counted exact identities. A clean-directory rerun with PYTHONHASHSEED=41881 reproduced the certificate byte-for-byte.

The semantic certificate SHA-256 is

```text
d8450d695a6f8a4aaee727ee82ba9529b0c72424af943bbcfbe27f2460337597
```

The certificate contains the raw and normalized reciprocal differential, frame transformation, currying and inverse, full bilinear evaluation, complete resolved maps, mixed-relation comparison, original and traced integral Hom matrices, class detectors, relative W25 components, and Cartier maps.

## Sources and conventions

Project repository andrey-kokoev/marici, commit d1947b67a60d3e88ba77f4ca60ea02c2a306ee61:

- Entry 93, `Alternating Fusion Normalization-Conductor Square`: the two-sheet coefficient ring and conductor ideal.
- Entry 97, `Reciprocal-Twist D03 Bivariant Road Trace`: the reciprocal/original normal pairing, complementary-degree values 1 and -q, and its scope limitation to the stated boundary costalk.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: cellular supports and signed radial/native differential.
- Entry 131, `D03 Cartier Edge Purity and the Scoped PC Promotion`: radial/native separation, retained excess, and scoped Cartier comparison.
- Entry 140, `Physical-Reflection Naturality of the D03 Edge Purity`: physical reflection and transported normal frames.

The immediately preceding independently replayed data are in `branch_a_w03_native_occurrence_excess_proof.md` and its standalone checker. The new checker reconstructs those needed matrices instead of importing them.

Mathematical references: Stacks Project 0621 (Koszul differentials and invertible generator changes), 0A8H (Hom differential and tensor--Hom adjunction), 064B (derived maps from projective resolutions), 0A74 (closed-immersion right adjoint), and 0B4B (Cartier purity and normal determinant). The homological degree placements are written explicitly to avoid relying on unstated shift conventions.
