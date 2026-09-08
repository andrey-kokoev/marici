# The actual marked-normal sector restores a relative order-two ambiguity

Date: 2026-09-06  
Repository input: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The previous unit-multidegree result does not extend unchanged to the marked-normal degrees of the **same actual target**. In the first degree in which all three long marked normals are legal, the actual generic quotient has an equivariant closed top-normal line. Its coherent marking space has three components and an order-two loop group in each component. The endpoint-normalized coherent source is still contractible, so its homotopy fibre over matching, independently prescribed generic comparison data has **two contractible components**.

Nothing is added to the target. All generators, stalk localizations, differential signs, and the physical dihedral action are retained. Multiplication by the three long normal parameters connects this calculation to the previous unit-degree calculation by an explicit commutative cube of chain maps.

The new closed generic class has a nonzero, primitive connecting boundary in the actual short-boundary support: an explicit 18-term chain. This identifies a target-side datum which an eventual sheet/endpoint comparison must account for.

The full normalization-sheet mixed-variance map and its two physical endpoint connector 2-cells are **not** constructed here. In particular, a marked long-normal state is not silently identified with the independent external Cartier or Rees Tor-one state. No value of the full physical parity is assigned.

## 1. Actual target and its first symmetric marked-normal degree

The source target is the 215-generator complex described in the preceding note `actual_q_graded_restriction.md`. Its coefficient ring is

\[
R=\mathbb Z[X_a,u_a:a\in\mathcal D].
\]

In words: occurrence and normal parameters remain independent, with no integer or occurrence inversions. The generator associated to a noncrossing face S and marked subset H has homological degree and stalk

\[
|[S,H]|=3-|S|+|H|,
\qquad R[u_a^{-1}:a\in S\setminus H]\,[S,H].
\]

In words: a marked normal does not admit its own inverse. Each localization is local to its specified generator.

Keep the source filtration and quotients

\[
F_V\subset F_B\subset F_K,
\qquad E=F_K/F_V,
\qquad Q=F_K/F_B.
\]

In words: V is the two-endpoint support; B is the union of short facets; K is the full hexagon associahedron. The target E and its generic quotient Q are not replaced by their endpoint or norm readouts.

Write the three long diagonals as D-zero, D-one, D-two, in the order D03, D14, D25. Let

\[
U=u_0u_1u_2,
\qquad \gamma=e_{u_0}+e_{u_1}+e_{u_2}.
\]

In words: U is the product of the three **long normal parameters**, and gamma is its fine multidegree. These parameters are not the occurrence variables or external first-Rees parameters.

The generator degrees forced by the source differential and the chamber normalization are

\[
\deg[S,H]= -\sum_{a\in S}e_{X_a}+\sum_{a\in S}e_{u_a}.
\]

In words: this is the same fine grading as in the previous computation. In multidegree gamma, the unique possible coefficient on a generator is

\[
U\prod_{a\in S}\frac{X_a}{u_a}.
\]

In words: the previous unit weight is multiplied by U. This monomial is legal precisely when every mark in H is a long diagonal. Because the long diagonals cross pairwise, a noncrossing face contains at most one long diagonal and there are no hidden double-long marked generators.

Thus this homogeneous summand has 72 generators in K, 70 in E, and all seven in Q. Its chain-group ranks, ordered by homological degrees zero through three, are

\[
\operatorname{rk}E_\gamma=(12,33,21,4),
\qquad
\operatorname{rk}Q_\gamma=(0,0,3,4).
\]

In words: the marked normals are present in their actual degrees; they are not tensor factors adjoined after the calculation.

## 2. All-polynomial generic top cycles

Let T be the chamber, F-i an unmarked long facet, and M-i its marked normal. In the actual generic quotient,

\[
d_QT=\sum_{i=0}^{2}\frac{X_i}{u_i}F_i,
\qquad d_QM_i=F_i.
\]

In words: the first map has the prescribed localized facet coefficients. The second is a localization inclusion, not an invertible map of the full stalk modules.

A degree-three chain has the form

\[
aT+\sum_i b_iM_i,
\qquad a,b_i\in R.
\]

In words: none of these four top coefficients admits an inverse normal parameter. It is closed exactly when

\[
a\frac{X_i}{u_i}+b_i=0\quad(0\le i\le2).
\]

In words: every facet coefficient must vanish in its own localization. Since u-i and X-i are independent polynomial variables, these equations require u-i to divide a, for every i. Hence U divides a. Conversely, that divisibility supplies all three legal polynomial b-i.

Consequently

\[
\omega=UT-\sum_{i=0}^{2}X_i\frac{U}{u_i}M_i,
\qquad d_Q\omega=0,
\qquad H_3(Q)=R\omega.
\]

In words: every generic top cycle is a unique polynomial multiple of the displayed cycle. Each apparent quotient U/u-i is the product of the other two normals, so its marked coefficient is polynomial. The target has no degree-four generators, so this kernel is already degree-three homology.

This is an all-polynomial proof, not an extrapolation from bounded exponent tests. It also proves that gamma is the least fine normal degree of a nonzero closed top class. Any additional occurrence factor does not remove the required normal divisibility.

## 3. The exact generic complex at gamma

Normalize the legal weighted basis in degree gamma by

\[
T_\gamma=UT,
\quad F_{i,\gamma}=U\frac{X_i}{u_i}F_i,
\quad M_{i,\gamma}=X_i\frac{U}{u_i}M_i.
\]

In words: these are the actual coefficient-weighted generators, not a specialization of all parameters to one.

Then

\[
d_QT_\gamma=F_{0,\gamma}+F_{1,\gamma}+F_{2,\gamma},
\qquad d_QM_{i,\gamma}=F_{i,\gamma},
\]
\[
\omega=T_\gamma-M_{0,\gamma}-M_{1,\gamma}-M_{2,\gamma}.
\]

In words: the three marked-normal pairs contract, while one corrected chamber survives.

Define a projection p by taking the T-gamma coefficient, a section i by sending one to omega, and a homotopy h by sending F-i-gamma to M-i-gamma and all degree-three generators to zero. Direct calculation gives

\[
d_Qh+hd_Q=1-ip,
\qquad pi=1.
\]

In words: this is an explicit integral deformation retraction onto the surviving degree-three line.

Use the source-labelled dihedral action already checked in the preceding artifact: rotation adds two to every hexagon vertex, reflection sends a vertex v to 3-v, and the chamber reflection sign is minus one. This is the physical endpoint-swapping reflection, not the endpoint-fixing reflection of the older target-promotion script. The existing loaded action is preserved in the present computation.

Both the displayed contraction and projection are equivariant. The surviving line has character

\[
r\omega=\omega,
\qquad s\omega=-\omega.
\]

In words: rotation fixes the cycle and reflection reverses it. Therefore Q-gamma is equivariantly equivalent to one integral sign line in homological degree three.

## 4. A complete normal-multiplication cube

The checker computes every subset P of the three long normals, using the multidegree with normal exponent one on P and zero elsewhere. Exactly the marked generators indexed by P are legal in Q. The complete homology table is

| Number of positive long normals | Generic degree-two homology | Generic degree-three homology |
|---:|---|---|
| 0 | rank two, free | zero |
| 1 | rank one, free | zero |
| 2 | zero | zero |
| 3 | zero | rank one, free |

The row with three positive normals is the gamma sector above. The row with no positive normals is the preceding unit-degree result. The intermediate sectors have smaller stabilizer groups; they are not separately treated as full dihedral representations. The full group acts on the whole cube, permuting its vertices.

Multiplication by a newly positive normal includes the old legal weighted basis in the new one. All twelve cube edges are actual chain maps. All six squares commute with the original coefficient monomials, not only after taking homology. Group covariance is checked on every source generator of every cube vertex.

The homology transition is not monotone: after one or two normal directions contract the facet homology, the third direction permits a new closed top class. This is why extending a unit-degree rigidity argument by deleting the marked states would give the wrong answer.

## 5. The new class has a nonzero short-support boundary

Use the same 70-generator endpoint quotient E-gamma, and regard omega as a chain there before projecting to Q. It is not a cycle in E. Instead,

\[
b=d_E\omega\in(F_B/F_V)_{\gamma,2},
\qquad db=0.
\]

In words: the generic cycle has a connecting boundary in the actual short-facet support. The checker constructs all 18 nonzero terms of b. The facet terms left over from the chamber combine with the radial boundaries of the marked long normals; no new source cell is inserted.

Exact integral contractions compute

\[
H_3(E_\gamma)=H_2(E_\gamma)=0,
\quad H_1(E_\gamma)=\mathbb Z^4,
\]
\[
H_2((F_B/F_V)_\gamma)=\mathbb Z,
\qquad
H_3(Q_\gamma)\xrightarrow{\ \partial\ }H_2((F_B/F_V)_\gamma)
\]

with the last map an isomorphism. In words: b is primitive and generates the short-support degree-two group. It is not an exact short-boundary correction.

On the explicit chains,

\[
gb=\chi(g)b.
\]

In words: its orientation character is the same sign character as the generic cycle. The certificate supplies b in the literal labelled basis and its integral homology coordinate, which is a unit.

Thus the marked-normal loop below has an actual attached support class. It is not the disconnected norm detector used in the earlier auxiliary calculation.

## 6. The endpoint-normalized coherent source

The endpoint quotient has only its four degree-one homology generators, and all its higher homology vanishes. The two endpoint connecting maps on this homology are integrally surjective. In the explicit integral basis used by the checker, their matrix is

\[
A=\begin{pmatrix}
1&1&0&0\\
1&0&1&-1
\end{pmatrix}.
\]

In words: fixing both endpoint values leaves a rank-two affine family of ordinary, nonequivariant homology classes. It does not leave four arbitrary directions.

The computed action on the same basis is

\[
R=\begin{pmatrix}
1&1&1&0\\
0&0&-1&0\\
0&0&0&-1\\
0&1&0&0
\end{pmatrix},
\qquad
S=\begin{pmatrix}
1&1&1&-1\\
0&-1&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}.
\]

In words: these matrices are derived from the full loaded action and the explicit integral retraction, not chosen from a matching character.

They satisfy the dihedral relations, and direct integral solution gives

\[
\ker(R-I)\cap\ker(S-I)=\mathbb Z(1,0,0,0),
\qquad A(1,0,0,0)^T=(1,1)^T.
\]

In words: there is exactly one invariant class with both endpoint values one. The rank-two ordinary variation has no invariant subdirection. Since the reindexed marking complex has homology only in degree zero, its normalized homotopy-fixed marking space is contractible.

The unit is the preceding source-labelled four-edge corridor multiplied by U. Its original facet and chamber transport witnesses remain legal in this degree and satisfy all 36 pair and 216 triple equations. Thus existence of the invariant unit is exhibited at chain level, not inferred solely from invariant matrix ranks.

## 7. Complete cohomology of the generic sign line

Reindex Q-gamma by subtracting one from its homological degrees, so that a physical one-cycle is a marking object, degree-two coefficients are paths, and degree-three coefficients compare paths. Its marking complex is equivalent to the sign line in degree two. Let Y-gamma be its homotopy-fixed Dold-Kan space.

For the sign module, a group one-cocycle has value zero on rotation: the rotation-cube relation forces three times that value to be zero in the integers. Its reflection value is an arbitrary integer. Coboundaries change that value by an even integer. Therefore

\[
H^0(D_3,\mathbb Z_\chi)=0,
\qquad H^1(D_3,\mathbb Z_\chi)=\mathbb Z/2.
\]

In words: there are no invariant top cycles but there is one nontrivial reflection one-cocycle class.

Here is also a full classification of the degree-two group, without assigning a finite rank from samples. A group extension with this action has an infinite-cyclic kernel generated by a, with rotation commuting with a and reflection inverting a. Choose lifts R and S of rotation and reflection. Write

\[
R^3=a^m,
\quad S^2=a^n,
\quad SRS^{-1}=a^tR^{-1}.
\]

In words: m,n,t record the defects of the lifted group relations. Reflection of its own square forces n=0. Conjugating the rotation-cube relation forces 3t=0, hence t=0. Changing the rotation lift to a-power times R changes m by a multiple of three; changing the reflection lift does not introduce any other invariant. Every m is realized by the resulting presented extension. Thus

\[
H^2(D_3,\mathbb Z_\chi)=\mathbb Z/3.
\]

In words: the rotation-cube defect modulo three completely classifies these extensions.

Equivalently, for g=(i,e), h=(j,f), with i,j represented by 0,1,2, the extension cocycle for m is

\[
k_m(g,h)=m\frac{i+(-1)^ej-((i+(-1)^ej)\bmod3)}{3}.
\]

In words: it is the carry generated by multiplying the chosen rotation lifts. The quotient is always an integer, including for negative signed sums. The checker verifies every associativity equation for these cocycles; the classification argument proves completeness.

The Dold-Kan mapping convention and derived invariants now give

\[
\pi_0Y_\gamma=\mathbb Z/3,
\qquad
\pi_1Y_\gamma=\mathbb Z/2,
\qquad
\pi_nY_\gamma=0\quad(n\ge2).
\]

In words: each of the three components is a classifying space of the order-two group. This differs from the three **contractible** generic components at unit degree.

## 8. The actual unit and the explicit order-two loop

The multiplied corridor's facet comparisons project to Q-gamma, and its chamber two-cochain projects to the surviving sign line. Summing its rotation-cube defect gives residue one modulo three. This is computed from the existing integral corridor witnesses. It agrees with the preceding nonzero unit Q component transported through the normal-multiplication cube.

Define

\[
\eta(r^i)=0,
\qquad\eta(r^is)=1,
\qquad\ell_g=\eta(g)\omega.
\]

In words: the comparison loop is zero on rotations and uses the full corrected marked-normal cycle on reflections.

The equations are

\[
d_Q\ell_g=0,
\qquad g\ell_h-\ell_{gh}+\ell_g=0,
\qquad2\ell_g=g(-\omega)-(-\omega).
\]

In words: it is an actual generic loop, and its double has an explicit coboundary. It cannot itself be a coboundary because projection to the equivariant sign line would require an even reflection difference to equal one. The explicit equivariant contraction in Section 3 ensures that adding facet homotopies cannot defeat this nontriviality argument.

At unit degree, using the chamber alone failed because its differential was the nonzero facet norm. Here the three legal marked terms cancel that exact boundary. The earlier exclusion and the present loop therefore coexist in different coefficient degrees of the same target.

## 9. Relative fibres and the role of coefficient-linearity

Keep both endpoint values fixed to one, and independently prescribe a generic target object with its comparison path retained. The coherent normalized endpoint source is contractible, and its generic image lies in the nonzero residue-one component of Y-gamma. Consequently the matching relative fibre has

\[
\pi_0\mathcal R_\gamma\cong\mathbb Z/2,
\qquad
\pi_n\mathcal R_\gamma=0\quad(n\ge1).
\]

In words: there are two contractible components of ways to identify the same coherent unit with matching fixed generic data. An incompatible generic component, or incompatible endpoint values, gives an empty fibre. These are not two different unit classes.

There is a separate, more restrictive question: require the comparison at gamma to be the U-multiple of the already fixed comparison at unit degree. The explicit multiplication cube induces a map from the unit-degree relative fibre, which is contractible, into this two-component fibre. It lands in just one component. The order-two loop is not in that image, since the source comparison-loop group is zero.

Thus a comparison which is supplied as a specified U-multiple inherits one component; an **independently framed** marked-normal comparison permits two. Requiring a path to the inherited comparison leaves a contractible compatible space. This is a statement about an explicitly specified relative square, not a universal normalization of the physical parity.

For an actual degree-preserving module-linear source map, values on true U-multiples cannot be chosen independently. However, the source's retained external Tor-one generator is not known to be a U-multiple of its unshifted generator. Making that identification would erase precisely the source distinction still needing construction.

## 10. What the physical comparison must now determine

The completed target calculation supplies a concrete test rather than another detached detector. A proposed normalization-sheet comparison must identify where its retained shifted state lands relative to omega and the attached 18-term class b. It must do so with the actual fine-degree shifts, supported-dual variance, generic Q restriction, and both endpoint comparison cells.

The source distinguishes the occurrence, normal, external Rees, and Cartier directions. In particular, entry 117 warns that an external Thom tensor does not generate the missing extraordinary endpoint maps, and that central base change makes their coefficient equations too weak to determine them. The present computation does not replace those maps by an endpoint scalar, a chosen parity, or the multiplication U.

The positive result is exact and limited: **marked-normal retention restores the order-two relative ambiguity in the actual target, and its source-support transgression is explicit.** The previous unit-degree rigidity result remains valid. A full physical comparison must decide whether the shifted comparison is inherited through a specified multiplication square or is independently framed. No physical parity is inferred merely from either target-sector computation.

## Reproduction

Run:

```sh
python check_marked_normal_q_extension.py --output marked_normal_q_extension_certificate.json
```

The checker is self-contained, uses the Python standard library, and passes **49,754 exact assertions**. It reconstructs the coefficient domains; computes all eight long-normal support grades; checks the twelve multiplication arrows, six squares, and dihedral covariance; retains and verifies full integral projection/section/homotopy maps for its signed-unit reductions; computes the actual endpoint homology actions; constructs the coherent unit and the marked-normal parity loop; and verifies the primitive 18-term connecting class.

The polynomial-divisibility theorem and all-cocycle classifications are algebraic proofs in this note, not consequences of the number of assertions. The computation is not proof-assistant certification. No repository files were modified.

## Provenance

Pinned repository inputs:

- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: all stalks, differentials, and support quotients.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: labelled endpoint-swapping reflection and the actual corridor.
- `src/ledger/20260814-117 D03 Thom Endpoint Koszul Hull and the Missing Road Generizations.md`, blob `af6874dc6928614a824a14105fa8e4ba37d96306`: independent external Tor and endpoint requirements.
- `research/voevodsky/check_dp6_endpoint_q_mapping_fiber.rs`, blob `592811b138855554c921dcf4269581632e8f0050`: conditional status of the full physical restriction.

Preceding artifacts: `actual_q_graded_restriction.md`, `check_actual_q_graded_restriction.py`, and `relative_physical_admissibility.md`. Their target-sector versus physical-comparison distinctions remain in force.

General conventions: Stacks Project, Group cohomology, tag `0A2H`; Dold-Kan, tag `019D`; Hom complexes, tag `0A8H`. Specific cohomology values and relative-fibre results here are derived above rather than attributed to those general references.
