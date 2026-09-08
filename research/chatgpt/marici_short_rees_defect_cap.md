# Short-Rees selection defects, supported Gysin maps, and their actual cap images

Date: 2026-09-07  
Project: Marici  
Pinned source commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`  
Continuation of `marici_native_excess_conductor_transport.md`

## 1. Result and scope

The eight higher-wedge channels missing from the ordinary raw-to-selected comparison have now been placed in their **complete selection-defect complexes**. These are not isolated copies of the cokernel of multiplication by a Rees monomial.

For a quadratic channel, the defect is the sum of the two individual Rees-divisor modules. For a cubic channel, it is a nonsplit complex of three divisor modules and their three pair intersections. A triple-intersection class is part of this complex. The order of a Rees monomial must not be confused with codimension of its zero locus.

The canonical selected/raw cycle pair supplies a Koszul-to-defect map. Its dual followed by the extended Cech comparison is an explicit supported Gysin morphism, including its lower component. On the central short-Rees face, this lower component remains nonzero for the eight higher channels. It is a relative extension morphism, not an ordinary primitive lift through the original selection.

A separate calculation transports these exact source cycles through the already constructed native cap, with both endpoint composites retained. The six quadratic channels, including their excess-labelled copies, have **identically zero cap images**. The two cubic channels map to a specific two-term short-support chain with one opposite-endpoint boundary. The boundary has an existing marked-normal nullhomotopy; adding it gives a primitive short-support cycle. Every one of these channel maps has zero generic Q projection.

Thus the supported selection defects are real, but resolving their Rees factors does not by itself give the required physical generic/collar comparison. The current cap is the remaining restrictive operation on these channels. This conclusion concerns the fixed cap, not all possible bivariant comparisons.

All six branch/pair source relabellings were checked. The cap image is stated explicitly on the reference plus/D03 chart and its independent excess sector. No new physical reflection parity is assigned.

## 2. Source and coefficient conventions

Use the native node and its normalization, as in the source ledger [S1]:

\[
A=S[t_0,\ldots,t_5,X_0,\ldots,X_5],\qquad
B=A/\bigl((X_0,X_2,X_4)(X_1,X_3,X_5)\bigr).
\]

In words: occurrence and short-Rees parameters remain separate. The coefficient ring S contains the independent long-normal and long-occurrence parameters. The three long-Rees parameters used in the preceding proper-descent calculation are not identified with any of these short-Rees parameters.

Use the established integral excess bases:

\[
D_x=K_A(X_1,X_3,X_5,v)\otimes\Lambda(\eta_x),\qquad
D_u=K_A(t_1X_1,t_3X_3,t_5X_5,v)\otimes\Lambda(\eta_u),
\qquad v=t_0X_0.
\]

In words: this is the full selected/raw five-generator source, expressed after its checked determinant-minus-one basis change. The original selected excess is still

\[
\eta_x=t_3h_3^+-h_3^{03}.
\]

In words: eta remains an independent closed difference, with its original internal degree. The selection s sends the three branch generators to their t-multiples, keeps the partner generator h0, and sends eta-u to eta-x.

For a nonempty ordered subset T of the three odd labels, retain the conductor attachment

\[
b_{T,\epsilon}=v h_T\eta_x^\epsilon,\qquad
p_T=\prod_{i\in T}t_i,\qquad \epsilon\in\{0,1\}.
\]

In words: epsilon records the independent excess channel. These are differently graded source classes, not alternative normalized physical units. Their ordinary image ideals were computed in the preceding note.

## 3. A complete small source model, rather than a single representative

Fix the occurrence degree containing X0 once and every Xi in T once, and fix the partner-Rees degree of v and h0. Allow **all polynomial degrees in the branch-Rees parameters**. The eta sector is an independent direct summand after the source-defined basis change.

Let k be the size of T. Before adding eta, this source frame has exactly

\[
2^k+1
\]

generators. In words: they are the conductor cycle b and all complementary-occurrence normal states

\[
q_H=\left(\prod_{i\in T\setminus H}X_i\right)h_Hh_0,
\qquad H\subseteq T.
\]

In words: no source wedge in this occurrence and partner-Rees frame is omitted. A wedge without h0 must contain every odd label, since otherwise its coefficient would be a forbidden even-odd product in B. A wedge with h0 can retain any subset H.

The degrees are k for b and |H|+1 for q-H. With a-i equal to t-i in the raw frame and one in the selected frame,

\[
dq_H=\sum_{i\in H}(-1)^{\operatorname{pos}_H(i)}a_iq_{H\setminus i}
\quad(H\ne T),
\]

\[
dq_T=\sum_{i\in T}(-1)^{\operatorname{pos}_T(i)}a_iq_{T\setminus i}
       +(-1)^k b,\qquad db=0.
\]

In words: these are the literal source Koszul boundaries after the native node relations. In particular the lower q-H terms are genuine first- and higher-conormal data.

Selection is the chain map

\[
s(q_H)=\left(\prod_{i\in H}t_i\right)q_H,
\qquad s(b)=p_Tb.
\]

In words: its full cone includes all the q-H states, not only the displayed multiplier on b. Define this cone to be C-T. Tensoring the two source models with eta shifts the entire result by one and retains the eta determinant.

The small model is linear over the branch-Rees polynomial ring in this **fixed occurrence/partner-Rees frame**. It is not being substituted for the entire ambient A-linear dual. Section 7 separately constructs an ambient A-linear map in the full native free resolution.

## 4. Exact divisor geometry of the selection cone

Let R now denote the branch-Rees polynomial ring with the fixed spectator frame understood.

### One branch label

The complete cone is contractible. The existing first-conormal lift Xi h0 accounts for this. The map on the original b-representative alone would miss that lift.

### Two branch labels i,j

There is an explicit integral equivalence

\[
C_{\{i,j\}}\simeq
\bigl(R/(t_i)\oplus R/(t_j)\bigr)
\]

with the right side in homological degree two. In words: the defect retains the two separate Rees-divisor branches. It is not only R/(t-i t-j).

The primitive selected b-class enters the exact sequence

\[
0\longrightarrow R/(t_it_j)
\xrightarrow{(1,1)}R/(t_i)\oplus R/(t_j)
\xrightarrow{(1,-1)}R/(t_i,t_j)\longrightarrow0.
\]

In words: its product-divisor obstruction is the diagonal part of a larger, coupled two-divisor defect. The quotient records their intersection.

### Three branch labels

For T={1,3,5}, the complete cone is equivalent to

\[
\bigoplus_{i\in T}R/(t_i)
\xrightarrow{\delta}
\bigoplus_{i<j\in T}R/(t_i,t_j),
\qquad \delta(a)_{ij}=a_j-a_i,
\]

in homological degrees three and two. In words: both the three divisors and all three pair intersections remain. The endpoint of their augmented Cech complex is the triple intersection.

The complete module sequence is

\[
0\longrightarrow R/(p_T)
\longrightarrow\bigoplus_iR/(t_i)
\longrightarrow\bigoplus_{i<j}R/(t_i,t_j)
\longrightarrow R/(t_1,t_3,t_5)\longrightarrow0.
\]

In words: it retains a nonzero coupling between the product-divisor class and the triple-intersection class. Monomial by monomial, exactness is the augmented simplex calculation on the coordinates with zero exponent.

Consequently,

\[
H_3(C_T)=R/(p_T),\qquad
H_2(C_T)=R/(t_1,t_3,t_5),
\]

and other homology vanishes. In words: the isolated image ideal from the earlier calculation correctly found H3, but it did not describe the whole selection defect.

### Chain-level verification and nonsplitting

The code gives explicit maps from the ten-column quadratic and eighteen-column cubic cones to finite Koszul resolutions of the divisor diagrams. The maps send the native b-class to the diagonal divisor values. Their complete comparison cones contract using seven and eighteen signed-unit cancellations, respectively. This proves equivalence over the polynomial ring, not just equality of homology ranks.

For completeness, the cubic cone itself retracts to an eight-generator polynomial complex. Write a,b,c for its three Rees variables, with degree-three basis (B,E-a,E-b,E-c). Its nonzero differentials are

\[
d_3=(0,-a,-b,-c),
\qquad
d_4=
\begin{pmatrix}
0&0&bc\\
b&c&0\\
-a&0&c\\
0&-a&-b
\end{pmatrix}.
\]

In words: the top source has three generators in degree four; the bottom has one in degree two. Both the linear and quadratic terms are necessary.

At a=b=c=0 this complex has homology ranks (1,4,3) in degrees (2,3,4). A direct sum of its two homology modules, with their derived base change retained, would instead have ranks (1,4,4,1) in degrees (2,3,4,5). Therefore the cone is not formal and the displayed two-extension does not split.

## 5. The supported defect trace, including its lower component

There is a canonical chain map built from the actual selected and raw conductor cycles:

\[
[R\xrightarrow{p_T}R]_{k+1\to k}
\longrightarrow C_T,
\qquad e_k\longmapsto b_x,\quad
 e_{k+1}\longmapsto b_u.
\]

In words: in the mapping cone, the boundary of the raw b-component is p-T times the selected b-component. This supplies a genuine product-Cartier comparison, with its ordered normal frame retained.

Dualize this finite free map over R and apply the standard Koszul-to-Cech comparison. The result is

\[
\Theta_T:\operatorname{Hom}_R(C_T,R)
\longrightarrow [R\longrightarrow R[p_T^{-1}]],
\]

with the output in cohomological degrees k and k+1. In words: the output is the supported complex for the **union** of the Rees divisors, not their simultaneous intersection.

On the full cone its components are particularly simple:

\[
\Theta_T^k(\varphi)=\varphi(b_x),\qquad
\Theta_T^{k+1}(\psi)=\frac{\psi(b_u)}{p_T}.
\]

In words: the lower coefficient reads the selected cycle, and the upper supported coefficient reads its raw comparison. All other components are zero in this convention. The chain equation is checked before discarding any q-H state. Poles occur only in the declared output localization.

### Exact supported image

For k=2 or 3, the finite-frame dual has its only cohomology in degree k+1. With the ordered determinant shift retained, it is

\[
\frac{(t_i:i\in T)}{(p_T)}.
\]

In words: the supported values are the classes

\[
\left\{\left[\frac{f}{p_T}\right]:f\in(t_i:i\in T)\right\}
\subset R[p_T^{-1}]/R.
\]

In words: the numerator must vanish at the common Rees intersection. In particular the primitive product-pole class [1/p-T] is not in this image.

This is an all-covector result, not failure of one representative. For the cubic minimal complex, the top dual generators map to

\[
\frac{c}{abc},\qquad-\frac{b}{abc},\qquad\frac{a}{abc}.
\]

In words: the three allowed residues generate precisely the ideal above. The four relation rows of d4 transpose map either to zero or to the polynomial unit, which is zero in supported cohomology. Conversely, if a polynomial vector has image zero modulo abc, subtract its multiple of the product relation; the remaining vector is a syzygy of the regular row (c,-b,a). Its syzygies are exactly the three remaining Koszul rows. This proves both the image and kernel over the full polynomial ring.

### Central specialization

If any parameter in T becomes zero, the localized output disappears. The lower component does not disappear. At the full center, the map is the dual of the actual selected b-class in the specialized cone.

For k=2 and 3 this class is primitive and nonzero; for k=1 the full cone is contractible and the map is nullhomotopic. The code checks all central faces and the full-center Betti ranks. Thus the eight higher channels retain nonzero **relative Gysin extension maps**. They have not acquired ordinary primitive raw-to-selected lifts, and no fraction is evaluated by substituting zero in its denominator.

## 6. The source classes lift explicitly to the full native resolution

Let P be the established fifty-generator native free resolution. Denote its generators by p-U,V, with nonempty even U and odd V, and let p-empty be its degree-zero generator. For a fixed T, use the convention

\[
p_{0,\varnothing}=X_0p_{\varnothing}.
\]

In words: this notation retains the bottom occurrence coefficient rather than inventing a new resolution generator.

The complete selected and raw lifts are

\[
Z_T^x=t_0\sum_{V\subseteq T}
(-1)^{|V|}\operatorname{sgn}(V,T\setminus V)
\,p_{\{0\},V}\otimes h_{T\setminus V},
\]

\[
Z_T^u=t_0\sum_{V\subseteq T}
(-1)^{|V|}\operatorname{sgn}(V,T\setminus V)
\left(\prod_{i\in V}t_i\right)
 p_{\{0\},V}\otimes h_{T\setminus V}.
\]

In words: the shuffle sign is that of the ordered exterior decomposition. Each lift includes every required native resolution correction. Their augmentations are v h-T, not a freely normalized scalar.

Exact calculation gives

\[
dZ_T^x=dZ_T^u=0,\qquad
(1_P\otimes s)Z_T^u=p_TZ_T^x.
\]

In words: this realizes the product-Cartier-to-defect map **over the full ambient ring A**, before taking a homogeneous occurrence frame. Appending eta keeps its original source basis and degree.

Dualizing this actual map and using the output Cech localization gives an ambient A-linear supported map. It retains the t0 and occurrence coefficients in Z; it is not the operation of extracting a polynomial coefficient and declaring it an A-valued unit. The small-frame trace above is its explicitly normalized labelled-channel calculation. An unrestricted scalar-unit physical trace is not claimed.

## 7. Transport through the whole native cap and both endpoints

The existing cap satisfies

\[
d_KF-Fd_P=\mathcal A,\qquad
\mathcal A=a_+f_+-a_-f_-.
\]

In words: the entire generic cap and the two native endpoint composites remain coupled. Its target is the original 215-state coefficient diagram with its stipulated localizations [S3].

Apply this pair to the full selection diagram. The source cone has 3,200 generators and the target cone has 13,760. Since F lowers homological degree by two, its two cone blocks have the same sign; since the endpoint composite lowers degree by three, its raw block acquires the cone sign. The induced maps satisfy the same coupled equation on every source column.

The check retains 2,752 cap terms and 384 endpoint-composite terms. It also checks every target-cone differential square.

### The six quadratic channels

For |T|=2, with or without eta,

\[
(F\otimes1)Z_T^x=(F\otimes1)Z_T^u=0,
\qquad
(\mathcal A\otimes1)Z_T^x=(\mathcal A\otimes1)Z_T^u=0.
\]

In words: the complete cap and endpoint composites are identically zero. This includes the full native resolution corrections, not just the bottom conductor cycle.

The reason is spatial. All native columns in these lifts have even subset {0} and at most two odd labels. Their complementary short faces have four labels or a mixed three-label support; neither is an admissible noncrossing short face. The prescribed cap is therefore zero on every such column.

Consequently the product-Cartier-to-defect map followed by this cap is the zero chain map. A functorial residue, dual, or Gysin operation on this same zero composite cannot make it nonzero. This excludes this factorization for these six channels, not a different mixed-variance correspondence.

### The two cubic channels

For T={1,3,5}, set S24={x2,x4} and let U-L be the product of the three long normals. Define the two-term target chain

\[
\Omega_{24}=\frac{U_L}{u_2u_4}[S_{24},\varnothing]
+\frac{X_{D14}U_L}{u_2u_4u_{D14}}
 [S_{24}\cup\{D14\},\{D14\}].
\]

In words: it contains the short pair and its actual compatible marked long-facet correction. The apparent inverse of the marked long normal cancels against the factor U-L. The inverses of u2 and u4 occur only at unmarked states.

The exact image is

\[
(F\otimes1)Z_T^x=-t_0\Omega_{24},
\qquad
(\mathcal A\otimes1)Z_T^x
=-\frac{U_L}{u_2u_4}[v_-,\varnothing].
\]

In words: the two-term chain has one nonzero opposite-endpoint boundary. Both signs and all coefficients are computed in the existing target convention. The raw images have the additional factor p-T.

This endpoint boundary is not a nonzero endpoint residue class. It has the existing marked-normal witness

\[
L_-=-\frac{U_L}{u_2u_4}[v_-,\{x_0\}],
\qquad
dL_-=-\frac{U_L}{u_2u_4}[v_-,\varnothing].
\]

In words: marking x0 introduces no forbidden inverse of its normal. The boundary is an unmarked endpoint coefficient missing the u0 pole, so its exactness is also consistent with the endpoint Cech complex.

The corrected chain

\[
\Xi=-t_0\Omega_{24}-L_-
\]

is closed. In words: both the short-support contribution and its endpoint normal homotopy are retained.

Its **whole target frame**, including the selected source factor, has six generators, two in degree zero and four in degree one. The differential has rank two with unit Smith factors. There is no degree-two term. Thus this corrected chain is a primitive nonzero class in a rank-two H1 group. Appending eta gives the corresponding independent shifted statement.

Every term in these two cubic images is short-boundary supported:

\[
\pi_Q(F\otimes1)Z_T^x=\pi_Q(F\otimes1)Z_T^u=0.
\]

In words: their generic image is zero. The nonzero generic class of the full native cap comes from a different source channel; it is not the image of these conductor attachment cycles.

## 8. Interpretation and next required comparison

The earlier eight proper image ideals are now resolved into a precise relative geometry: individual Rees divisors, pair overlaps, and the cubic triple-intersection coupling. The full defect trace has explicit lower components and nonzero central extension values.

The subsequent cap test shows why this result cannot be promoted to a physical unit merely by normalizing a Rees residue. The fixed cap kills the six quadratic channels outright. Its two cubic channels reach a primitive **lower-support** class after an explicit endpoint normal correction, not the generic physical class or a primitive endpoint residue.

The needed physical operation must therefore supply a source-derived map from this relative divisor-incidence diagram to the required collar/generic channel. It cannot be the existing cap composed with a scalar residue normalization. Such a different correspondence is not disproved here, and no physical parity is chosen.

## 9. Reproduction and checks

Run:

```sh
python check_marici_short_rees_defect_cap.py \
  --output marici_short_rees_defect_cap_certificate.json
```

The self-contained standard-library checker performs **38,418 counted exact assertions**, with additional ordinary assertions in the integral contraction helpers. A second execution from another working directory produces the same certificate.

The checks include the literal native frame embeddings; complete polynomial cone contractions; two explicit divisor-diagram comparison cones; all relevant branch-Rees homogeneous degree patterns; derived central specialization of the whole supported trace; actual free native lifts; all 3,200 source and 13,760 target cone columns; every cap and endpoint equation; both independent eta sectors; and six source-chart relabellings.

The all-polynomial results use the exact module and Koszul arguments in this note. The finite checks are not substitutes for those arguments and are not proof-assistant certification. No repository files were written.

## Sources and earlier artifacts

[S1] Pinned Marici source: `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`; blob `840258522d45e450e4f1e8bb927d9aae58c75566`. Native node, both sheet quotients, and normalization difference.

[S2] Pinned Marici source: `src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md`; blob `d5ed0c89e804284a4bf45bfa1e0c0bc2eab6eb12`. Ordered independent excess and support/twist conventions.

[S3] Pinned Marici source: `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`; blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`. Literal target differential and permitted localization stalks.

[S4] Pinned Marici source: `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`; blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`. Conormal-valued Bockstein and the distinction between a full comparison and its collapsed scalar symbol.

[M1] Stacks Project, tag `0621`, *The Koszul complex*: exterior functoriality, tensor products, and cone conventions.

[M2] Stacks Project, tag `014D`, *Cones and termwise split sequences*: complete comparison cones and homotopy terms.

[M3] Stacks Project, tag `0952`, *Local cohomology*: the flat extended Cech model and cohomology with support.

Retained local inputs: `marici_native_excess_conductor_transport.md`, `marici_joint_triangle_rees_gysin.md`, and `marici_joint_conductor_spatial_cap_comparison.md`. The corresponding exact source/target helper routines are embedded in the new checker so it has no dependency on those files at runtime.
