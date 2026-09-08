# Mixed 03/13 normal comparison and the surviving secondary coefficient operator

Date: 2026-09-06  
Branch: A  
Marici source: `andrey-kokoev/marici` at `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Results and limitations

The following calculations use the actual finite and legal Čech differentials of the loaded hexagon, not a replacement by its homology.

1. The two-circle cochain packet has an explicit monodromy-dependent comparison with the source's two-normal Koszul complex. It reduces to the earlier exterior packet when both monodromies equal one. All lower terms and reflection homotopies are retained.
2. The primary Chern product becomes zero under derived augmentation. Its ordered Koszul comparison between nullhomotopies supplies a degree-two exterior operator. There is an explicit extension of this operator to the finite and Čech normal packets.
3. The Čech operator is locally nullhomotopic on the 20-cell closed mixed-face subcomplex. Extending that nullhomotopy to the full loaded diagram produces a nonzero, explicitly computed radial correction with five columns.
4. The resulting secondary operator is genuinely nonzero in the derived coefficient category: a bounded-free-source Hom calculation gives a primitive copy of Z in degree two, and an integral covector evaluates the operator to one while annihilating every potential homotopy.
5. The operator and local homotopy have zero quotient and endpoint components. This does not calculate their composite with the distinguished normalization-to-physical connector, nor does it identify the result with a homotopy group of the proposed infinity-groupoid.

The stabilizer-cochain interpretation of the Chern polynomial model is rational. The Laurent-polynomial identities, normal-circle comparison, and coefficient Hom calculation are integral. No integral E-infinity formality or equivalence of the full Artin and finite coefficient categories is asserted.

## 1. What the linked Stacks Project chapter supplies

The inspected file `stacks/stacks-project/constructions.tex` is the source of the chapter *Constructions of Schemes*. The relevant constructions are relative gluing, relative spectrum and its compatibility with base change, vector bundles, cones, and projective bundles. The file was read with blob SHA `7bad94eb5f6b6a02c6054e23aeeca18de3b0da35`.

On a transverse normal-crossing chart of the source, let the two labelled divisors be D_a and D_b, with a=03 and b=13, and let Z=D_a intersect D_b. Write C_a and C_b for their conormal line bundles restricted to Z. In the Stacks convention the normal line spaces are

\[
V_a=\underline{\operatorname{Spec}}_Z\operatorname{Sym}(\mathcal C_a),
\qquad
V_b=\underline{\operatorname{Spec}}_Z\operatorname{Sym}(\mathcal C_b).
\]

Their punctured product is

\[
\mathcal T_Z=(V_a\setminus Z)\times_Z(V_b\setminus Z).
\]

It is a principal two-dimensional multiplicative-group torsor. This construction requires the actual normal line bundles, not only an array of labelled finite cells. Over a trivializing complex-analytic chart its oriented compact fibre is a product of two circles.

The same conormal data give the projective bundle

\[
\mathbf P_Z(\mathcal C_a\oplus\mathcal C_b),
\]

with its two coordinate quotient sections. For a regular codimension-two immersion this is the projectivized normal cone, with the projectivization convention fixed. This constructs the candidate exceptional geometry with its normal lines retained; identifying a selected real interval or its trace with the entire physical connector still requires the relevant correspondence.

Relative spectrum commutes with base change. Gluing applies once the line bundles and their transition isomorphisms are supplied and satisfy the overlap cocycle. A collection of differential arrows is not, by itself, a proof that those gluing hypotheses hold.

The geometric normal coordinates of V_a,V_b, the monodromies q_a,q_b, the coefficient parameters u_i=q_i-1, and the Chern classes c_i remain distinct.

## 2. Universal monodromy comparison

Suppress spectator coefficients and set

\[
R_q=\mathbb Z[q_a^{\pm1},q_b^{\pm1}],
\qquad u_i=q_i-1.
\]

The source uses the homological normal complex with boundary d ell_i=u_i p_i. After separating the fixed face's chain-degree shift, its cochain dual is

\[
K_u=\left[
R_q\xrightarrow{(u_a,u_b)^T}R_q^2
\xrightarrow{(-u_b,u_a)}R_q
\right]
\]

in degrees zero, one, and two. Its ordered basis is 1, epsilon_a, epsilon_b, epsilon_a epsilon_b, with

\[
d_u=u_a\,\epsilon_a\wedge-+u_b\,\epsilon_b\wedge-.
\]

This is obtained from the product of two universal circle local systems, not by identifying u_i with a Chern class.

### One circle with the endpoint model retained

Take the graph with vertices (h,b) and two edges (e_D,e_1). Its cochain differential is

\[
\delta_q=\begin{pmatrix}-1&1\\-1&q\end{pmatrix}.
\]

The two edge transport choices are 1 and q. This fixes the positive cycle and coefficient convention. Let K_q=[R_q --(q-1)--> R_q]. Define

\[
J^0(a)=(a,a),\qquad J^1(t)=(0,t),
\]

\[
P^0(a,b)=a,\qquad P^1(v,w)=w-qv,
\]

\[
H^1(v,w)=(0,v).
\]

Direct multiplication gives

\[
PJ=1,\qquad \delta_qJ=Jd_q,\qquad P\delta_q=d_qP,
\qquad \delta_qH+H\delta_q=1-JP.
\]

Tensoring the two contractions retains all sixteen graph-product states and retracts them to the four Koszul states. The tensor contraction is

\[
H_{12}=H_1\otimes1+(J_1P_1)\otimes H_2,
\]

with the standard graded tensor sign in the second summand. It does not add an extra copy of the source normal directions.

At q_a=q_b=1, the minimal differential is zero and the result is the full exterior complex of ranks (1,2,1). Away from resonance this constant exterior complex is not a comparison model: its differential omits the actual monodromy.

### Reflection

Let sigma invert q. On graph cochains use the semilinear maps

\[
R_G^0(a,b)=(\sigma a,q^{-1}\sigma b),\qquad
R_G^1(v,w)=(\sigma w,\sigma v).
\]

On the minimal complex use

\[
R_K^0(a)=\sigma a,\qquad R_K^1(t)=-q\sigma t.
\]

They square to the identity and commute with their differentials. The failure of J to commute strictly is the explicit homotopy

\[
\eta^1(t)=(0,\sigma t),\qquad
R_GJ-JR_K=\delta\eta+\eta d,
\qquad R_G\eta+\eta R_K=0.
\]

Thus the one-circle endpoint model and orientation comparison are retained, including the reflection-square relation. This is a local-system calculation on the stated graph; it is not an identification of that graph with the full global spatial correspondence.

### Supported residue

Projection epsilon_i to one is not a scalar cochain map off resonance: its defect is u_i. The double top projection becomes a cochain map to

\[
R_q/(u_a,u_b)[-2].
\]

It sends epsilon_a epsilon_b to the supported unit. The two partial projections are the exterior contractions, with the appropriate one-coordinate quotient and shifted signs. Reversing their order reverses the double orientation. A scalar residue on the absolute universal-monodromy complex cannot be inferred from the untwisted calculation; the source's relative/Cousin trace must be retained.

## 3. Chern product and its ordered two-homotopy

Over rational stabilizer coefficients put A=Q[c_a,c_b], with |c_i|=2, and resolve the augmentation by

\[
K_c=A\otimes\Lambda(\epsilon_a,\epsilon_b),
\qquad d_c\epsilon_i=c_i.
\]

Multiplication by c_a c_b has the two nullhomotopies

\[
N_a=c_b(\epsilon_a\wedge-),\qquad
N_b=c_a(\epsilon_b\wedge-).
\]

They satisfy

\[
[d_c,N_a]=[d_c,N_b]=c_ac_b\,1,
\qquad
N_b-N_a=[d_c,\epsilon_a\epsilon_b\wedge-].
\]

Here all brackets are graded commutators. After augmentation the primary operation and these two degree-three homotopies vanish, but the degree-two comparison epsilon_a epsilon_b wedge - is still a nonzero linear map. It takes the unit to the ordered top exterior state.

This is a specified Koszul comparison between nullhomotopies. It is not the claim that the original degree-four Chern operation remains nonzero after augmentation. Relating its image to a physical operation requires the coefficient comparison, which is tested next.

### A restriction on simultaneous twisting

There is no naive four-state differential combining independent universal Chern and monodromy parameters. On the same exterior module set

\[
D=d_c+d_u.
\]

Then the exterior anticommutation relations give

\[
D^2=(c_au_a+c_bu_b)\,1.
\]

This polynomial is nonzero over the independent coefficient base. More generally, corrections vanishing when either all c's or all u's are zero have parameter order at least two. Their contribution to the square starts in order three, so they cannot remove the displayed order-two term. This excludes a square-zero deformation on these same four minimal states with both prescribed specializations. It does not exclude a larger geometric construction with extra objects, relations, or a different base.

## 4. Extension to the source's loaded target

Use

\[
R_0=\mathbb Z[X_d,u_d:d\in\mathcal D],
\]

where D is the set of nine hexagon diagonals. For a loaded generator [F,H], H subset F, use homological degree 3-|F|+|H|. Let P be the source's 215-generator finite complex. Let C be its legal Čech version, whose summand at [F,H] has coefficients

\[
R_0[u_d^{-1}:d\in F\setminus H].
\]

Its radial differential has coefficient X_d/u_d, and its normal mark-removal coefficient is one, with the original incidence and tensor signs. The finite-to-Čech comparison is

\[
\Lambda[F,H]=\left(\prod_{d\in F\setminus H}u_d^{-1}\right)[F,H].
\]

Write iota_d for signed contraction of mark d in the fixed diagonal order. The secondary operation extends as

\[
T^{\mathrm{fin}}_{ab}=\iota_b\iota_a,
\qquad
T^{\check C}_{ab}=\frac{1}{u_au_b}\,\iota_b\iota_a.
\]

Each operation is zero unless both marks occur. The Čech coefficient belongs to the target summand because both marks have been removed. No inverse is placed on a source state that forbids it. These maps have homological degree minus two, hence cohomological mapping degree two, and satisfy

\[
dT^{\mathrm{fin}}=T^{\mathrm{fin}}d,
\qquad dT^{\check C}=T^{\check C}d,
\qquad \Lambda T^{\mathrm{fin}}=T^{\check C}\Lambda.
\]

The double normal comparison is insensitive to the simultaneous sign adjustment needed when separating a face's fixed odd cellular shift from its normal Koszul factor. The checker uses the full source signs directly.

## 5. Local nullhomotopy and global radial defect

For a=03, b=13 the closed mixed-face subcomplex consists of F containing both a,b, with all allowed marks. It has twenty generators; the only maximal faces are {03,13,04} and {03,13,35}. Its degree ranks are (2,7,8,3).

Define a degree-minus-one homotopy by

\[
H_{ab}[F,H]=
\frac{(-1)^{3-|F|}}{u_au_b}\,\iota_b[F,H]
\]

when a is present and unmarked and b is marked, and define it to be zero otherwise. On the mixed-face subcomplex,

\[
dH_{ab}+H_{ab}d=T^{\check C}_{ab}.
\]

This local primitive is coefficient-legal. It retains the radial cofaces as well as the normal square.

On the full loaded target the same formula instead gives

\[
dH_{ab}+H_{ab}d=T^{\check C}_{ab}+\mathcal R_{ab}.
\]

The additional operator occurs only when a is absent, b is marked, and adding a is allowed. Its column is

\[
\mathcal R_{ab}[F,H]
=(-1)^{\nu(F,H)}\frac{X_a}{u_a^2u_b}
[F\cup\{a\},H\setminus\{b\}],
\]

\[
\nu(F,H)=\#\{d\in F:d<a\}+3-|F|-1+
\#\{d\in H:d<b\}.
\]

The smallest nonzero column is

\[
\mathcal R_{03,13}[\{13\},\{13\}]
=-\frac{X_{03}}{u_{03}^2u_{13}}
[\{03,13\},\varnothing].
\]

There are exactly five nonzero columns in each of T, H, and R. The certificate exports every coefficient and support.

### Endpoint and Q restrictions

Let V contain the complete eight-state packets on each of v_+={13,15,35} and v_-={02,04,24}; let Q be the seven-state quotient by the short boundary. Neither endpoint contains a long diagonal, and no Q state contains both a long and a short diagonal.

All three operators T,H,R vanish on the retained endpoint and Q representative states. Their outputs contain both a and b, so quotient projection to Q is zero. Moreover, no coface of such a face is either endpoint. If kappa_+,kappa_- are the actual differential terms landing in the endpoint packets, then

\[
\pi_QT=\kappa_+T=\kappa_-T=0,
\]

and the same equalities hold for H and R. These are chain equalities, not evaluations of an endpoint permutation matrix. They permit the operations to descend to E=P/V and its Čech counterpart. They do not supply an independently missing normalization-source connector homotopy.

## 6. Genuine derived nonvanishing

A nonzero map in an ordinary Hom complex with localized source terms need not survive in the derived category. We therefore test the composite with a bounded free source:

\[
\Psi_{ab}=T^{\check C}_{ab}\Lambda:
E^{\mathrm{fin}}\longrightarrow E^{\check C}[2].
\]

The finite endpoint-relative source is bounded and termwise free over R_0. Its ordinary Hom complex computes derived Hom against the Čech target.

### Full homogeneous mapping slice

Give X_d and u_d their independent fine degrees. Use generator shifts

\[
\operatorname{wt}_{\mathrm{fin}}[F,H]
=-\sum_{d\in F}\mathbf e_{X_d}+
\sum_{d\in H}\mathbf e_{u_d},
\]

\[
\operatorname{wt}_{\check C}[F,H]
=-\sum_{d\in F}\mathbf e_{X_d}+
\sum_{d\in F}\mathbf e_{u_d}.
\]

Both differentials and Lambda are homogeneous. The operation has weight

\[
w=-\mathbf e_{u_a}-\mathbf e_{u_b}.
\]

For a source state (F,H) and target state (G,J), any coefficient in this weight has the forced exponents

\[
\deg_{X_d}=1_{d\in G}-1_{d\in F},
\qquad
\deg_{u_d}=1_{d\in H}-1_{d\in G}-1_{d\in\{a,b\}}.
\]

A homogeneous entry exists exactly when all occurrence exponents are nonnegative and every negative normal exponent is permitted by G minus J. Each admitted coefficient module in this weight is one copy of Z. This enumerates all R_0-linear homogeneous maps, not only an ansatz of incident maps. It forces every target state to contain a,b unmarked.

The complete degree-zero through degree-three mapping slice is

\[
\mathbb Z^5\longrightarrow\mathbb Z^{24}
\longrightarrow\mathbb Z^{36}\longrightarrow\mathbb Z^{16},
\]

with differential ranks (5,19,16). All nonzero Smith factors are one. Thus

\[
H^2\!\left(\operatorname{RHom}_{R_0}
(E^{\mathrm{fin}},E^{\check C})\right)_w\cong\mathbb Z,
\]

and all other cohomology in this weight is zero.

### Integral detection of the specified operator

For any degree-two map in this slice, consider its four coefficients into the unmarked target ({a,b},empty), normalized by these forced monomials:

| Source | Monomial |
|---|---|
| (empty,empty) | X_a X_b/(u_a^2 u_b^2) |
| ({a},{a}) | X_b/(u_a u_b^2) |
| ({b},{b}) | X_a/(u_a^2 u_b) |
| ({a,b},{a,b}) | 1/(u_a u_b) |

Call the four integer coordinates t_0,t_a,t_b,t_ab and put

\[
\ell(f)=-t_0+t_a+t_b+t_{ab}.
\]

The exact matrix calculation verifies

\[
\ell(\delta H')=0
\]

for every degree-one map in the full twenty-four-dimensional space, while

\[
\ell(\Psi_{ab})=1.
\]

This proves that Psi is a primitive nonzero derived class. If T itself were zero in the derived category, composing it with Lambda would be zero, contradicting this detector. Thus the Čech endomorphism T is genuinely nonzero as well. The frame cannot nullify a class already nonzero after forgetting that frame.

The result persists after adjoining the monodromy units (1+u_d)^{-1}. If a homotopy existed there, its finitely many coefficients could be cleared of those denominators. It would give a polynomial homotopy for g Psi, where g is a product of powers of (1+u_d). Since g has constant term one, the homogeneous weight-w component would give a homotopy for Psi itself. The integral detector excludes this. This persistence argument does not claim a fine grading on the inhomogeneously localized ring.

## 7. Interpretation and remaining physical calculation

The primary product beta_03 beta_13 is sent to zero by derived Chern augmentation. The ordered Koszul comparison between its two nullhomotopies has an explicit normal-circle extension, and this secondary coefficient operation is not null after including all radial maps. Its local primitive fails precisely by the five computed radial columns.

This shows that trivializing the Chern action while discarding the coherent normal data loses a nonzero operation of the full coefficient target. It does not show that the distinguished primitive physical line admits this operation: the relevant calculation is the composite T_ab kappa with the actual normalization-derived connector kappa, including its prescribed homotopies. A nonzero endomorphism of a target can annihilate a particular mapped object.

The linked constructions chapter supplies the normal torus and exceptional projective-bundle geometry on an actual transverse chart. It does not identify all monodromy, stabilizer, and Cartier complexes merely from their exterior ranks, and it does not prove a six-functor equivalence or determine T_ab kappa.

## Verification

Run `python check_mixed_normal_chern_comparison.py` with Python 3.10 or later. No third-party packages are required. The script writes `mixed_normal_chern_comparison_certificate.json` beside itself.

The 2,755 exact checks include the universal one- and two-circle contractions; reflection and its homotopy coherence; primary and secondary Koszul identities; the supported-residue defect; the joint differential curvature; all 215 finite and Čech differential squares; locality and coefficient legality; endpoint connecting maps; the complete homogeneous Hom differential; integral unit-pivot reductions; and the covector detecting the specified class. The certificate contains the full Hom matrices and all operator columns.

## Sources

Marici, pinned to the commit above:

- `src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md`: normal-circle local systems, q-1 differential, ordered tensor factors, and the stated limits of the facewise comparison.
- `research/voevodsky/check_ringed_alexandrov_pc_target.py`: loaded-cell incidence and legal Čech differential.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`: finite-to-Čech diagonal comparison.
- `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`: complete endpoint and Q support packets.
- `src/ledger/20260817-424 The Exceptional Interval Carries the Primitive Thom Trace.md`: oriented relative interval.

Stacks Project:

- `https://github.com/stacks/stacks-project/blob/master/constructions.tex`
- Section 27.3, Relative spectrum via gluing: `https://stacks.math.columbia.edu/tag/01LL`
- Section 27.4, Relative spectrum as a functor; the lemma labelled `lemma-spec-properties` in constructions.tex gives base change.
- Section 27.6, Vector bundles: `https://stacks.math.columbia.edu/tag/01M1`
- Section 27.21, Projective bundles: `https://stacks.math.columbia.edu/tag/01OA`
- Section 31.20, The normal cone of an immersion: `https://stacks.math.columbia.edu/tag/062Z`
- Section 15.29, The Koszul complex: `https://stacks.math.columbia.edu/tag/0621`
- Section 15.31, Koszul regular sequences: `https://stacks.math.columbia.edu/tag/062D`
- Section 15.75, Derived hom: `https://stacks.math.columbia.edu/tag/0A5W`

Prior calculations in this session are recorded in `derived_inertia_descent.md`. Its Chern-operation interpretation is used only with the rational and objectwise-framing qualifications stated there.
