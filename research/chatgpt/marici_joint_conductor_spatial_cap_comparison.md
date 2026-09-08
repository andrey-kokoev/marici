# Joint conductor to spatial target: a complementary-face cap comparison

Date: 2026-09-07  
Project: Marici  
Pinned input: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and scope

The full normalization node, rather than either individual normalization sheet, admits an explicit polynomial-linear comparison to the actual endpoint quotient of the 215-state target. The map retains its generic marked-normal class and both endpoint comparison maps in one chain equation. It has 43 nonzero terms on 16 source columns.

The new ingredient is a complementary-face map from the six-occurrence Koszul complex. Composing it with the source's previously constructed joint normalization homotopy produces the comparison. This is not the fivefold, single-sheet Gysin factorization that was shown to vanish on the node conductor class.

There is also an explicit spatial identification of the **entire homogeneous source-Hom diagram** with cochains on the existing complementary-support cubes. In this identification the new map is the constant cochain one on all 43 vertices of the endpoint-complement space. Its generic restriction is nonzero, and its two endpoint transgressions are primitive. The compatible normalized comparison space is contractible in the specified frame.

These are finite occurrence/coefficient and cubical-incidence results. They do not prove that the constructed comparison is the prescribed ringed supported-Verdier or logarithmic six-functor. The source here is the complete occurrence-normalization node. Identification of this source channel with the required independent excess/Rees channel and with the previously constructed spatial collar operators in their own frames remains to be checked. No physical reflection parity is assigned.

## 2. Fixed source, target, and coefficient frame

Use independent short occurrences, long occurrences, and normal parameters. A convenient ambient ring is

\[
A=\mathbb Z[X_0,\ldots,X_5,X_{D03},X_{D14},X_{D25},u_0,\ldots,u_5,u_{D03},u_{D14},u_{D25}].
\]

In words: the occurrence and normal families are separate polynomial coordinates. Additional spectator variables can be restored by flat extension. No identification with external Rees coordinates is made in this definition.

Let

\[
E_0=\{0,2,4\},\qquad O_0=\{1,3,5\},\qquad
\mathcal B=A/(I_{E_0}I_{O_0}),\qquad I_J=(X_j:j\in J).
\]

In words: the source is the actual two-sheet normalization node, extended by spectator coefficients [S1]. Its plus sheet is the quotient by the even ideal; its minus sheet is the quotient by the odd ideal. The conductor ideal internal to a sheet is the opposite triple. These roles are not interchanged.

Its fifty-generator free resolution P has

\[
P_0=A,\qquad
P_n=\bigoplus_{\substack{\varnothing\ne U\subseteq E_0,\ \varnothing\ne V\subseteq O_0\\|U|+|V|=n+1}}A\,p_{U,V},
\qquad
(\operatorname{rk}P_n)_{n=0}^5=(1,9,18,15,6,1).
\]

In words: retain all mixed resolution generators and the source unit. The differential is the one verified in `marici_joint_conductor_dual_endpoints.md`: singleton pairs map to their mixed product; higher wedges have the two ordered Koszul differentials. That note proves polynomial exactness by all support types. The new checker reconstructs and rechecks the complete differential.

Write K for the actual 215-state target, V for its two endpoint subcomplexes, and B for its full short-boundary subcomplex. Set

\[
E=K/V,\qquad Q=K/B.
\]

In words: E retains the endpoint-relative target, and Q retains the generic quotient. We also keep B/V; no endpoint is first replaced by a scalar readout.

The target state [S,H] has homological degree 3 minus the number of diagonals in S plus the number of marks in H. Its coefficient module permits negative normal powers only for diagonals in S without a mark. Its differential has radial coefficients X_a/u_a and signed normal localization inclusions [S2].

Let

\[
U_L=u_{D03}u_{D14}u_{D25},\qquad
\gamma=e_{u_{D03}}+e_{u_{D14}}+e_{u_{D25}},\qquad
\lambda=\gamma-\sum_{i=0}^5e_{X_i}.
\]

In words: the comparison is in the previously studied symmetric long-normal degree, with **all six** occurrence conormal degrees retained. Negative entries in the degree of a map do not authorize negative occurrence powers in its coefficients.

The map constructed below is linear over A, with output in the stated localized target modules. Its uniqueness is proved in degree lambda, not in every possible occurrence or normal degree.

## 3. Decorate each actual short face by its forced long-normal corrections

Let \(\mathcal N\) be the set of actual noncrossing faces. For a compatible short face T, write u_T for the product of its short normals. Define

\[
\Omega_T=
\frac{U_L}{u_T}[T,\varnothing]
-\sum_{\substack{\ell\in\{D03,D14,D25\}\\T\cup\{\ell\}\in\mathcal N}}
(-1)^{\#\{a\in T:a>\ell\}}
\frac{U_LX_\ell}{u_Tu_\ell}[T\cup\{\ell\},\{\ell\}].
\]

In words: start with the unmarked short face and include each compatible marked long-normal state with its required sign. The condition in the summation is the actual noncrossing-face predicate. For incompatible T define the value to be zero.

Every short normal inverse occurs on an unmarked short state. In a marked long term, U_L/u_ell is the product of the other two long normals, so no inverse occurs on the marked long state. Thus all terms belong to their original target stalks.

The full differential gives

\[
d\Omega_T=\sum_{\substack{a\notin T\\T\cup\{a\}\in\mathcal N\\a\in\{x_0,\ldots,x_5\}}}
(-1)^{\#\{b\in T:b<a\}}X_a\Omega_{T\cup\{a\}}.
\]

In words: the radial long-facet terms cancel against their marked-normal boundaries. What remains is the actual occurrence-weighted short-face incidence. The checker verifies every radial and normal contribution, rather than replacing the differential by the displayed reduced form without a map.

For the empty face, the generic component is

\[
\omega=U_LT-\sum_{\ell}X_\ell\frac{U_L}{u_\ell}M_\ell,
\qquad d_Q\omega=0.
\]

In words: this is exactly the corrected generic marked-normal cycle previously computed, not a bare chamber and not a detached norm coordinate.

At the two endpoint faces there is no compatible long diagonal, so

\[
\Omega_{O_0}=\frac{U_L}{u_1u_3u_5}[v_+,\varnothing],\qquad
\Omega_{E_0}=\frac{U_L}{u_0u_2u_4}[v_-,\varnothing].
\]

In words: both endpoint classes remain in their original unmarked, legally localized target states in this normal frame. This does not identify them with the fully marked endpoint classes in a different purity/Rees frame.

## 4. A six-direction complementary-face map

Let K_6 be the homological Koszul resolution on the six short occurrences, in order

\[
(0,2,4,1,3,5).
\]

In words: this is the same determinant order used in the source normalization calculation, not the lexicographic order of diagonals in the target.

For an exterior subset I, let T be its complement in these six labels. Let pi_T reorder T from the source order into the target diagonal order, and put

\[
s(I)=(-1)^{|T|+\sum_{t\in T}\operatorname{pos}(t)}\operatorname{sgn}(\pi_T),
\qquad
c(e_I)=s(I)\Omega_T.
\]

In words: complement the actual exterior subset, use the actual target face if it exists, and retain the ordered cap sign. The positions are zero-based. No map is assigned to an incompatible face.

This has degree minus three and satisfies

\[
d_Kc=-c\,d_{K_6}.
\]

In words: it is the signed degree-three complementary-face operation. Removing a source wedge coordinate adds the same target face coordinate with its incidence coefficient. Incompatible faces stay incompatible when enlarged, so declaring them zero respects the equation.

The signs are verified on all 64 source wedges. In particular,

\[
c(e_{E_0})=\Omega_{O_0},\qquad
c(e_{O_0})=-\Omega_{E_0},\qquad
c(e_{E_0\cup O_0})=\omega.
\]

In words: the endpoint signs and generic orientation follow together from one ordered complement map. They are not fitted separately.

## 5. Compose with the actual joint normalization homotopy

Keep the source maps

\[
f_+:P\longrightarrow K_{E_0},\qquad
f_-:P\longrightarrow K_{O_0},
\]

and the source comparison

\[
H(p_{U,V})=(-1)^{|U|}e_U\wedge e_V,\qquad
 dH+Hd=\iota_Ef_+-\iota_Of_-.
\]

In words: these are the full node-to-sheet maps and their conductor homotopy from the preceding source calculation. Both endpoint maps are used. The formula does not factor through one normalized sheet.

Define

\[
F=-cH,\qquad a_+=c\iota_E,\qquad a_-=c\iota_O.
\]

In words: the new comparison is the complementary-face image of the joint source homotopy. This gives its coefficients before imposing any desired scalar endpoint value.

The complete endpoint equation is

\[
d_KF-Fd_P=a_+f_+-a_-f_-.
\]

In words: the only failure of F to be a closed map into the absolute target is exactly the difference of its two specified endpoint composites. The right-hand side lies in V. Therefore the endpoint quotient gives a genuine degree-two derived map

\[
F_E:P\longrightarrow E,
\qquad d_EF_E=F_Ed_P,
\]

where F_E lowers homological degree by two. In words: it represents a class in Ext squared with the full endpoint comparison retained by the displayed lifted equation.

There are 43 terms in F on 16 source columns. In the raw target frame the endpoint equation has six terms:

\[
(d_KF-Fd_P)(p_{E_0,\{j\}})=X_j\Omega_{O_0}\quad(j\in O_0),
\]

\[
(d_KF-Fd_P)(p_{\{i\},O_0})=X_i\Omega_{E_0}\quad(i\in E_0).
\]

In words: both endpoints occur with positive coefficients in this target orientation. The minus sign in the source conductor difference is still present; it combines with the negative cap sign on the odd exterior triple.

The generic value is

\[
F_E(p_{E_0,O_0})=\omega\pmod V.
\]

In words: the source's top comparison wedge goes to the actual generic marked-normal class with coefficient one in its framed normal line. No integer, occurrence variable, or newly forbidden normal is inverted.

This map is linear on arbitrary polynomial coefficients. The chain identities are identities of monomials in the original stalks. The finite matrices below use their homogeneous monomial bases; they are **not** obtained by setting occurrence variables to one or by using coefficient extraction as an A-linear trace.

## 6. Identify the complete mapping diagram with actual spatial cochains

For a target T define

\[
C_T=\operatorname{Hom}^{\bullet}_A(P,T)_\lambda.
\]

In words: keep every homogeneous source-to-target cochain, including all possible comparison homotopies, in the specified coefficient frame [M1].

The coefficient monomial on a column p_(U,V) to [S,H] is forced by its degree. The exponent inequalities imply that H contains only long labels and that every short label missing from U union V belongs to S. Set

\[
N=\{x_i:i\notin U\cup V\},\qquad
\mathcal C(U,V;S,H)=\square(N\cup H,S).
\]

In words: this is an actual cell of the previously constructed complementary-support cube space W. Missing source coordinates become its fixed-one coordinates; source coordinates shared with the target face become its variable coordinates.

This gives a bijection between the basis of C_K and all 215 cubes of W except the two endpoint vertices. Its cohomological degree is two plus the cube dimension. Every target radial arrow, target mark-removal arrow, and transposed source-Koszul arrow becomes the corresponding cubical coface incidence. The checker constructs the signs from the ordered chamber orientation and verifies the complete chain isomorphism, including all group actions.

The entire support diagram becomes

\[
C_K\cong C^\bullet(W,\{v_+,v_-\};\mathbb Z)[-2],\qquad
C_E\cong C^\bullet(W_E;\mathbb Z)[-2],
\]

\[
C_Q\cong C^\bullet(W_Q;\mathbb Z)[-2],\qquad
C_{B/V}\cong C^\bullet(W_E,W_Q;\mathbb Z)[-2],
\]

\[
C_B\cong C^\bullet(W,W_Q\cup\{v_+,v_-\};\mathbb Z)[-2],
\]

\[
C_V\cong C^\bullet(W,W_E\cup\{v_+,v_-\};\mathbb Z)[-2].
\]

In words: the source normalization resolution supplies precisely the relative endpoint conditions that were absent from a detached target detector. These are identities of complete signed coefficient complexes in the frame, not merely matching Betti numbers.

Here W_E consists of cubes whose upper face is neither endpoint, and W_Q is the origin plus the three long-coordinate edges. The endpoint points are outside W_E. Coordinate scaling toward the origin contracts W, W_E, and W_Q and preserves the inclusion of W_Q into W_E. These contractions are equivariant under all relabellings.

Thus the cohomology is obtained independently from the topology of these pairs:

| T | Basis columns in C_T | Nonzero cohomology |
|---|---:|---|
| K | 213 | degree 3: Z |
| V | 14 | degree 3: Z squared |
| B | 206 | degree 3: Z squared |
| B/V | 192 | none |
| E | 199 | degree 2: Z |
| Q | 7 | degree 2: Z |

The checker also gives explicit signed-unit deformation retractions of all six complexes. There is no integral torsion.

Under this spatial identification, F_E is exactly the constant cochain one on every one of the 43 vertices of W_E. Its restriction to the generic tree is the same constant cochain. This proves nonvanishing without relying on the coefficient of one generic flag. Unlike the earlier nullhomotopic degree-one roof, the present object includes the source's six-direction comparison wedge and its complementary degree shift.

## 7. Both endpoint values and the generic value are forced together

The complete target restriction is

\[
r:C_E\longrightarrow C_V[1]\oplus C_Q.
\]

In words: its first component is the actual off-diagonal endpoint boundary; its second is the actual generic quotient. No endpoint terms are omitted.

On the primitive classes it is

\[
\mathbb Z\longrightarrow\mathbb Z^2\oplus\mathbb Z,
\qquad k\longmapsto(k,k,k).
\]

In words: generic coefficient one forces both endpoint coefficients to one in the stated target orientation. A different prescribed triple does not admit a normalized lift in this frame.

The restriction C_E to C_Q is a quasi-isomorphism because its complete kernel C_(B/V) has an explicit 96-pivot contraction. For the restriction retaining all three values, the full 220-generator mapping fibre has

\[
H^3(\operatorname{fib}r)=\mathbb Z^2,\qquad
H^j(\operatorname{fib}r)=0\quad(j\ne3).
\]

In words: the stable relative object is not zero, but it has no classes in degrees two or below. Mapping-space paths for degree-two maps read degrees below two [M1]. Accordingly, with matching prescribed endpoint and generic comparisons, the normalized extension space is contractible. This uses the full fibre with both endpoint comparison variables, not only the equality of three integers [M2].

For dihedral transport the raw map has the source's sheet-polarity character:

\[
gF(p)=\chi(g)F(gp).
\]

In words: rotation preserves it and reflection supplies the prescribed orientation reversal. After tensoring the source by the polarity line, the complete map is strictly equivariant. The spatial cochain identification is equivariant with the ordinary action on cubes after exactly this twist. All six transports are verified on every Hom column. There is no averaging or division by two or three.

Consequently there is no residual twofold comparison ambiguity **in this particular joint-source homogeneous problem**. This does not identify it with the physical parity problem in other normal/Rees frames.

## 8. Reverse generic pairing with the actual joint conductor class

Take the framed normal-degree slice as a complex over the full occurrence polynomial ring. Its generic chamber covector reads the coefficient of the basis U_L T. Let that covector be ell_Q. Pulling it back through F_Q gives

\[
F_Q^\vee(\ell_Q)=p_{E_0,O_0}^\vee=-\kappa.
\]

In words: the reverse generic covector lands in the node's genuine degree-five conductor class, with the minus sign dictated by the preceding source convention kappa equals minus the top comparison covector. This is not a fivefold single-sheet Gysin class.

Pairing with the preceding source gluing cocycle Lambda therefore gives

\[
\left\langle F_Q^\vee(\ell_Q),\Lambda\right\rangle
=-\left[\frac1{X_0X_2X_4X_1X_3X_5}\right].
\]

In words: the reverse pairing has the correct sixfold supported conductor value and its explicit orientation. The value is not an ordinary unit in the polynomial ring. The occurrence denominator is in the previously specified output local-cohomology module, not in an original target stalk. The new checker verifies the pullback covector on every source column; the complete gluing cocycle and its residue evaluation were constructed and checked in the preceding joint-source artifact.

The independent excess exterior factor can be retained by tensoring this entire diagram, including both endpoint terms. That formal tensor compatibility is checked in both channels. It is not a construction of the still-required source map from the selected/raw normal excess complex into this joint occurrence channel.

## 9. What has changed, and the remaining physical comparison

The earlier single-sheet and factorized blowdown no-go results remain valid. Their maps do not carry the joint normalization homotopy. Here the map is built from that homotopy, uses its sixth occurrence determinant direction, and acts in a different derived source channel. The generic class now lifts into E; its absolute boundary is exactly the coupled endpoint pair rather than an unaccounted short-support obstruction.

The finite source-to-spatial coefficient identification is now explicit: the actual source Hom diagram is identified with the existing cubical pair diagram, and the comparison is its normalized constant class. It is no longer merely an integer functional declared to stand for a physical trace.

What remains unproved is the identification with the complete requested physical operation. In particular:

- the source-to-target normal/Rees comparison must carry the independent excess class into this six-occurrence conductor channel, with the correct shifts and determinant lines;
- the resulting endpoint comparison morphisms must be matched to the previous spatial collar 2-cells in their own occurrence/normal frames, not only in their scalar or topological shadows;
- equality to the ringed supported-Verdier or logarithmic pull-push, including its supported specialization and readout, still requires a functorial comparison.

No physical reflection parity is inferred from the existence of the unique map in this narrower frame. The next decisive test is the full Rees/Gysin specialization of this already coupled diagram, rather than another isolated generic or endpoint normalization.

## 10. Reproduction and source records

Run:

```sh
python check_marici_joint_conductor_spatial_cap_comparison.py \
  --output marici_joint_conductor_spatial_cap_comparison_certificate.json
```

The self-contained standard-library checker passes **20,522 exact assertions**. It reconstructs the node and Koszul resolutions, all 215 target states, the complete cap and 43-term map, all endpoint columns, all allowed coefficient exponents, polynomial and normal multiplication, six transports, the complete 213-column spatial dictionary, six integral Hom contractions, and the full 220-column endpoint/generic mapping fibre. The note's formulas prove the arbitrary-polynomial extension; this is not extrapolation from a polynomial degree cutoff. No proof-assistant certification or repository write is claimed.

[S1] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`.

[S2] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`.

[S3] `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`.

Local prerequisite derivations: `marici_joint_conductor_dual_endpoints.md`, `marici_cubical_supported_dual_kernel.md`, and the earlier marked-normal and occurrence-supported notes. Their distinctions among target incidence, physical six-functor provenance, normal frames and source channels remain in force.

[M1] Stacks Project, *Hom complexes*, tag `0A8H`.

[M2] Stacks Project, *Cones and termwise split sequences*, tag `014D`.

[M3] Stacks Project, *The Koszul complex*, tag `0621`, for ordered exterior differentials, functoriality and multiplication homotopies.
