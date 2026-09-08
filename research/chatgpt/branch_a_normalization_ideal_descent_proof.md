# Branch A — normalization-ideal descent of the conductor symbol

Date: 2026-09-07.

## Result and scope

The previous calculation classified degree-three target cycles separately in six first-conductor occurrence weights. Those independent target cycles do not automatically define a comparison from the normalization source. The actual conductor ideal has relations between its six generators, and relations between those relations.

This calculation uses that ideal, not a free six-generator replacement. It constructs the entire degree-zero derived mapping group from the shifted conductor ideal into the previously specified full endpoint/Q-framed coefficient kernel, at occurrence-map degree zero and output regulator-normal grade three.

The results are:

| Data | Integral lattice rank |
| --- | ---: |
| Previous independent generator-image cycles | 60 |
| Generator-image assignments extending over the source resolution | 34 |
| Full source comparisons, including relation homotopies | 40 |
| Comparisons with zero image on all six source generators | 6 |
| Strict comparisons factoring directly through the ideal, with all relation homotopies zero | 16 |
| Full comparisons invariant under the checked reflection and transported over the three occurrence labels | 13 |
| Their distinct values on the actual six-term scalar conductor element | 11 |
| Invariant comparisons invisible on that element, supported only on source relations | 2 |

All ranks refer to lattices, not to finite numbers of maps. The exact maps, equations, integral kernel bases, reflection matrices, and scalar-symbol evaluations are supplied by the standalone checker and certificate.

This is a coefficient-level comparison from the normalization ideal in the previously selected primitive degree. It is not an identification of this shifted ideal with the physical Yoneda/Morse source, and does not assign the physical conductor–Morse difference. The additional spatial correspondence, Gysin placement, and its comparison cells are not inferred from the existence of these coefficient maps.

## 1. Source and target

Use the ordered diagonal labels

\[
\mathcal D=(02,03,04,13,14,15,24,25,35),
\]

and coefficient ring

\[
R=\mathbb Z[\beta,X_d:d\in\mathcal D]/
(X_eX_o:e\in\{02,04,24\},\ o\in\{13,15,35\}).
\]

Write

\[
I_+=(X_{13},X_{15},X_{35}),\qquad
I_-=(X_{02},X_{04},X_{24}),\qquad
I=I_+\oplus I_-.
\]

The sum is direct as an R-module. The two summands have zero product. This is the conductor ideal of the actual alternating normalization algebra, rather than an ideal inferred from a target-side homology calculation. The independent long coordinates and regulator are coefficients throughout.

The 430-state target has basis

\[
[F,H,\varepsilon],\qquad H\subseteq F,\qquad\varepsilon\in\{0,1\},
\]

with homological degree

\[
3-|F|+|H|+\varepsilon.
\]

Its radial differential adds a noncrossing diagonal with the signed coefficient X_d. Its native-normal differential removes a mark with signed coefficient beta X_d. The separate occurrence partner has differential X_35, without beta. The checker reconstructs every column and verifies square-zero.

Retain the full endpoint supports

\[
V_-=\{02,04,24\},\qquad V_+=\{13,15,35\},
\]

the short-boundary subcomplex, and the complete fourteen-state quotient Q. Let v be graded projection to both complete endpoint packets and q the actual chain projection to Q. The framed target is

\[
N_n=\{c\in(IC_\beta)_n:q(c)=0,\ v(c)=0,\ v(dc)=0\}.
\]

The last condition is required because v alone is not a chain map. N is the maximal subcomplex lying in the graded endpoint/Q kernel. The quotient by N is a genuine frame map; its homotopy fibre is equivalent to N through the explicitly reconstructed termwise-split cone contraction. Thus using N retains the previous coherent boundary frame rather than silently converting an invalid endpoint projection into a chain map.

The mapping problem is

\[
\operatorname{RHom}_R(I[3],N).
\]

Here I[3] puts the coefficient ideal in homological degree three. The occurrence degree of its generator a_i is epsilon_i, and the map has occurrence degree zero. The common internal shift is declared by requiring generator and relation images to have regulator-normal weight three, matching the primitive slot previously studied. This is a placement convention for this coefficient test, not a newly derived geometric Gysin shift.

After the primary and its comparison homotopy have been fixed, the usual source-cofibre construction reduces a K(beta)-supported deformation problem to a mapping problem with its top source placed in degree three. Replacing that free coefficient source by the actual ideal requires resolving I; it does not permit treating its six generators as independent.

## 2. An explicit resolution of the actual conductor ideal

Let P_0 have basis a_i for the six short labels, with augmentation

\[
a_i\longmapsto X_i.
\]

For each sheet and each ordered same-sheet pair i<j, introduce k_ij. For every pair with n and i on opposite sheets, introduce m_ni. Set

\[
d_1k_{ij}=X_i a_j-X_j a_i,
\qquad
 d_1m_{ni}=X_n a_i.
\]

There are six same-sheet relations and eighteen ordered mixed-sheet relations, so P_1 has rank 24. Their occurrence degrees are epsilon_i+epsilon_j and epsilon_n+epsilon_i.

For each sheet with labels i<j<k, the next relations are:

\[
X_i k_{jk}-X_j k_{ik}+X_k k_{ij};
\]

\[
X_n k_{ij};
\]

\[
X_a m_{ni};
\]

\[
X_n m_{mi}-X_m m_{ni}.
\]

Here i, j, k, and a belong to the selected sheet; n and m belong to the opposite sheet, with n preceding m. In words: take the internal three-variable Koszul relation, opposite-sheet multiples of the internal relations, same-sheet multiples of the mixed relations, and commutativity relations among the opposite-sheet coefficients.

Their counts per sheet are 1, 9, 27, 9. Thus P_2 has rank 92, and the resolution begins

\[
\cdots\longrightarrow R^{92}\xrightarrow{d_2}R^{24}
\xrightarrow{d_1}R^6\longrightarrow I\longrightarrow0.
\]

The checker verifies both displayed differential composites and every multidegree. No target data were used to choose these source relations.

### Exactness for arbitrary polynomial coefficients

Set A=Z[beta,X03,X14,X25]. Every element of R has a unique expression as a common A coefficient plus a positive-sheet augmentation polynomial and a negative-sheet augmentation polynomial.

Consider I_+. A relation between its three generators separates into a relation in A[X13,X15,X35] and arbitrary opposite-sheet augmentation coefficients. The first part is generated by the ordinary Koszul pair relations; the second is generated by the nine m_ni. This proves that the displayed P_1 resolves the augmentation kernel without a polynomial-degree bound. The argument for I_- is identical with the labels exchanged.

For a relation between those twelve first relations of I_+, decompose the coefficient of each internal k_ij into its positive-sheet polynomial and its negative-sheet augmentation part. Decompose the coefficient of each m_ni into its negative-sheet polynomial and its positive-sheet augmentation part. The positive part of the resulting equation is an internal Koszul syzygy, generated by the single triple relation. For each fixed i, the negative part is a Koszul syzygy of the three negative variables, generated by the three negative pair relations. The remaining arbitrary coefficient parts are generated by X_n k_ij and X_a m_ni. These are exactly the four families above. This proves exactness at P_1. It also explains the count 46 per sheet.

Append free modules resolving the remaining kernel in higher degrees. Their matrices are unnecessary for this calculation: after shifting by three, P_2 lies in degree five and higher terms lie above it, while the target is concentrated in degrees at most four.

This direct proof is over the integral coefficient ring. It does not assume that the conductor is a field. It is consistent with the established free-resolution construction for fibre-product rings, but no field-only result is being used to replace the integral argument.

## 3. Complete chain-map equations

A degree-zero map from P[3] to N is specified by

\[
Y_i=F(a_i)\in N_3,
\qquad
V_r=F(r)\in N_4
\]

on the six generators and twenty-four first relations. Its value on P_2 and all later terms is zero for degree reasons. The complete equations are

\[
dY_i=0,
\qquad dV_r=F(d_1r),
\qquad F(d_2s)=0.
\]

The first equations reproduce the sixty previously calculated generator-image directions. The second equations impose actual source linearity up to the retained relation homotopies. The third equations impose compatibility of those homotopies with every relation among source relations. Checking only the second equations would not construct a map from a resolution of I.

For a source generator of occurrence weight m, the coefficient on a target state is forced to have exponents

\[
m+\mathbf1_F-\mathbf1_H-\varepsilon\mathbf1_{35}.
\]

All exponents must be nonnegative; mixed-sheet coefficient monomials must vanish; the coefficient must belong to I. The beta exponent is fixed to 3-|H|. These equations determine the complete finite integral component. No coefficient cutoff is introduced.

Only eight source relations have weight containing epsilon_35. Each has 36 possible degree-four framed target values. The other sixteen have none. Together with the sixty generator-image coordinates, there are 348 unknown integer coefficients.

The full map equations have 1,101 nonzero polynomial coefficient rows. Each is extracted from an actual chain-map equation in R. A sequence of 308 signed-unit eliminations gives a kernel of rank 40. The operation log and all forty full polynomial maps are exported. Every resulting map is checked independently on all six generators, all twenty-four first relations, and all ninety-two second relations.

All images have zero complete endpoint and Q components. Their endpoint incoming boundaries vanish as well. No target state or lower correction is discarded to obtain these equations.

## 4. Homotopy classification and the six relation-only classes

There is no degree-plus-one map homotopy in this component. A possible homotopy on a_i would land in N_4 at occurrence weight epsilon_i. Such a degree-four target state has all native marks and the occurrence partner, so its coefficient would have occurrence weight epsilon_i-epsilon_35. For i unequal to 35 this has a negative exponent; for i=35 it has no conductor factor and is excluded from IN. Homotopies on higher source generators would land in target degrees at least five, which are absent.

The bounded-above free resolution computes derived Hom, and the degree-plus-one Hom group is zero. Therefore the rank-forty solution lattice is also the complete derived map-class group in this component. There is no unaccounted quotient by map homotopies.

Projection onto the six generator-image slots gives a saturated exact sequence

\[
0\longrightarrow\mathbb Z^6\longrightarrow\mathbb Z^{40}
\longrightarrow L_I\longrightarrow0,
\qquad L_I\cong\mathbb Z^{34}\subset\mathbb Z^{60}.
\]

The rank-six kernel consists of maps that vanish on all a_i and are nonzero only on the source relation homotopies V_r. They solve all ninety-two compatibility equations. They are not zero derived maps: no degree-plus-one homotopy exists in the specified component.

Setting every V_r to zero gives a rank-sixteen sublattice. These maps factor strictly through I as a module. Thus eighteen additional generator-image directions can be realized only with nonzero relation homotopies. The source decomposition gives rank 31 for I_+ and rank 9 for I_-; their sum is 40. The asymmetry reflects the retained occurrence-35 factor, not a new sheet symmetry assumption.

The old target-side statement that a compatible first symbol has a unique full target cycle remains correct. It does not assert uniqueness of a map from a source with nontrivial syzygies. Here six distinct source-comparison classes can have identical values on every source generator.

## 5. A closed target assignment that does not descend from the source

Let

\[
L_{03}=[\{03,13,35\},\{03,13,35\},0]
-\beta[\{13,35\},\{13,35\},0],
\]

and

\[
Y_{02}=X_{02}L_{03}.
\]

The full target differential kills Y_02 by the mixed-sheet relations. It has zero complete endpoint and Q components.

Nevertheless the assignment

\[
a_{02}\longmapsto Y_{02},\qquad
 a_i\longmapsto0\quad(i\ne02)
\]

does not extend to a map from I[3]. The actual source relation

\[
k_{02,04}\longmapsto X_{02}a_{04}-X_{04}a_{02}
\]

would require a degree-four chain with boundary

\[
-X_{02}X_{04}L_{03}\ne0.
\]

The coefficient is a same-sheet product and survives in R. No degree-four target exists at this source weight: its occurrence partner would require a negative X35 exponent. Thus no relation homotopy can repair the assignment. The global integral map equations independently detect this failure.

There is a source-compatible extension of the same local pattern. Use the actual module projection I to I_- and define

\[
\Phi_-(f_++f_-)=f_-L_{03}.
\]

The differential of L_03 lies in I_+C_beta, so multiplication by any f_- in I_- kills it. Hence this is a strict R-linear map I[3] to N. In generator coordinates,

\[
\Phi_-(a_i)=X_iL_{03}\quad(i\in\{02,04,24\}),
\qquad
\Phi_-(a_i)=0\quad(i\in\{13,15,35\}).
\]

Every source relation is now satisfied. This map is an explicit example in the computed lattice, not a declaration that physical geometry selects it.

## 6. Source-compatible symmetry

Use the same published cellular action as before:

\[
r(v)=v+2\pmod6,\qquad s(v)=2-v\pmod6,
\]

with top signs +1 and -1, and the ordered native-mark signs. Source ideal generators are transported by their coordinate labels. Same-sheet relation generators acquire the sign of reordering their two labels; mixed relation generators are transported without an additional sign.

Reflection fixes the occurrence label 35. Rotation transports it through 35,15,13. Thus full D3 transport uses all three corrected target complexes. The same source orientation convention as the preceding calculation is retained; no additional one-step sheet-exchange action is imposed within the fixed 35 component.

The exact invariant lattices are

\[
\operatorname{rank}\mathcal H^{\langle s\rangle}=13,
\qquad
\operatorname{rank}L_I^{\langle s\rangle}=11,
\qquad
\operatorname{rank}\ker(\mathcal H\to L_I)^{\langle s\rangle}=2.
\]

Here H denotes the rank-forty map-class group, not a Morse homotopy. The strict-source sublattice has five invariant directions.

In this source-descent sequence, taking invariants remains surjective onto the invariant generator-image lattice:

\[
0\longrightarrow\mathbb Z^2\longrightarrow\mathbb Z^{13}
\longrightarrow\mathbb Z^{11}\longrightarrow0.
\]

All eleven nonzero diagonal factors in the invariant projection are one. There is no residual index-two preimage obstruction for this map. This does not contradict the preceding index-two result: that concerned the different map from first symbols to nonzero quadratic target defects.

Every invariant map is transported over the three occurrence labels, and its generator, relation, relation-of-relations, endpoint, and Q equations are verified there. This gives thirteen-dimensional families with the specified D3 transport. It is not a construction of a geometric or six-functor equivariance structure.

## 7. Evaluate the actual normalization-derived scalar element

In the present zero-based coordinates, the supplied conductor symbol is the first grade of

\[
f_\sigma=
X_{25}X_{13}+X_{14}X_{35}+X_{03}X_{15}
-X_{14}X_{02}-X_{25}X_{04}-X_{03}X_{24}\in I.
\]

Its signs and long-coordinate coefficients are fixed by the normalization square. Evaluating a source map F requires no separate marked-state assignment once F is given:

\[
F(f_\sigma)=
X_{25}Y_{13}+X_{14}Y_{35}+X_{03}Y_{15}
-X_{14}Y_{02}-X_{25}Y_{04}-X_{03}Y_{24}.
\]

The checker evaluates this element on every full map basis vector, retaining all polynomial factors. Each result is a closed degree-three chain with zero endpoint and Q components.

This evaluation has rank 34 on the full rank-forty map lattice. Its kernel is precisely the six relation-only maps. It has rank 11 on the rank-thirteen equivariant lattice, with kernel rank two. The scalar element cannot detect the source relation homotopies.

The six occurrence weights after multiplying by the long coordinates are distinct, and each long variable acts injectively on the coefficient ring. Hence no additional cancellation occurs between different source-generator images. There are no degree-four conductor-relative target states at those six resulting weights, so the nonzero evaluation classes are not hidden boundaries.

For the explicit strict map Phi_-, put

\[
p_-=X_{14}X_{02}+X_{25}X_{04}+X_{03}X_{24}.
\]

Then

\[
\Phi_-(f_\sigma)=-p_-L_{03}.
\]

The reflection-invariant map Phi_-+sPhi_- has the twelve-term evaluation

\[
(\Phi_-+s\Phi_-)(f_\sigma)=-p_-(L_{03}+sL_{03}).
\]

Both the equation and all twelve marked coefficients are exported. The conductor factors and long-coordinate factors remain part of the result. No division produces a scalar unit.

This supplies explicit source-compatible placements of the actual scalar conductor element and classifies their possible values in the tested category. It does not select one of them as the physical Delta_J. Selection requires a source-defined spatial comparison and its lower comparison cells, beyond R-linearity, the checked frame, and D3 transport.

## 8. Reproduction and verification

Run:

```bash
python branch_a_normalization_ideal_descent_checker.py \
  --output branch_a_normalization_ideal_descent_certificate.json
```

The checker uses only the Python standard library. It has no companion-file, network, archive, or optional-library dependency. It reconstructs the target and source matrices, solves the actual integer equations with signed-unit eliminations, verifies every exported chain map against the source resolution, and calculates the symmetry and scalar-evaluation maps.

The source exactness argument covers all polynomial coefficients. The finite matrix computations exhaust the prescribed homogeneous component because all monomials there are forced by their multidegrees, not because a search was stopped at a degree cutoff.

The generated certificate reports 301,266 exact checks and includes an SHA-256 hash of its mathematical payload. A separate clean-directory execution verifies deterministic reproduction.

### Source provenance

Repository: andrey-kokoev/marici.

Pinned commit: d1947b67a60d3e88ba77f4ca60ea02c2a306ee61.

- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`: coefficient ring, branch decomposition, normalization sequence, and six-term conductor symbol.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`, blob `b967151cb0ee822e2361b9334a4ab26082c12682`: full radial/native differential, support flags, and cellular symmetry conventions.
- `research/voevodsky/check_d03_formal_support_purity.rs`, blob `acaabf367b24029d9dbfa371ee1983d392b393fa`: fixed-nonzero-regulator physical graph and its limited geometric scope. The beta-zero family here is a coefficient construction, not an extension of that geometric theorem.
- The preceding `branch_a_conductor_symbol_lifting_and_symmetry_checker.py`: target component and exact integer algebra routines, included and rerun in the new standalone checker. Its rank-sixty statement is used only after reconstructing its cycles and checking their complete differentials.

General conventions: Stacks Project Tags 0A8H (Hom complexes), 064B (bounded-above projective resolutions and derived maps). W. Frank Moore, *Cohomology over Fiber Products of Local Rings*, arXiv:0704.3631, provides the general fibre-product resolution context; the integral exactness used here is proved directly in Section 2.
