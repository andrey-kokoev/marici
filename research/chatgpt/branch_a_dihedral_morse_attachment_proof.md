# Dihedral splitting of the homogeneous Morse support attachment

Date: 2026-09-07  
Research lane: Marīci Branch A  
Repository input: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The fine-degree-zero support attachment is split exact as an integral module
sequence for the actual reflection stabilizing the occurrence label `35`.
The full three-label orbit is split exact for the source's six-element
dihedral group. Its rank-six filling module is the regular group module.
No positive-degree group-cohomology obstruction, including a two- or
three-primary obstruction, occurs in that filling module.

This is a theorem about the specified linear support complex, its coefficient
ring, and its source-defined group action. It does not construct the missing
physical conductor homotopy, assign a value to the physical conductor–Morse
difference, or produce a nonlinear geometric correspondence. A splitting of
homology modules is not being represented as a support-local geometric map.
The checker verifies the full polynomial action before extracting the entire
homogeneous component. It uses no polynomial-degree cutoff or averaging.

The earlier nonzero strict-unit obstruction on the conductor–road packet is
not a contradiction: it uses a different module and a different lifting
problem. The result here does not identify the two group actions merely
because their abstract groups are isomorphic.

## 1. Recovered parallel inputs

The available saved records, rather than an asserted complete recovery of the
latest Branch B/C chat turns, were:

- `prime_differentiation.md` (2026-09-05): the three-cycle augmentation
  differential has an actual nonzero modulo-three Bockstein. Prime effects
  must be computed from the full action and differential.
- `equivariant_physical_lift.md` (2026-09-06): the endpoint-coefficient packet
  has an order-six strict-representative obstruction while its complete
  homotopy-coherent normalized-state space is contractible. Strictness,
  invariance of homology, and coherent lifting are distinct requirements.
- `deck_sphere_retraction_falsification.md` (2026-09-05): the tested
  coefficient retraction does not lift to a deck-equivariant,
  stratum-preserving map of the actual point strata. Linear calculations
  alone do not identify a geometric realization.

The new calculation therefore checks the actual action on Branch A's filling
and attachment modules, without identifying that action with either of those
parallel problems.

## 2. Coefficient ring, cellular source, and grading

Let

\[
\begin{aligned}
\mathcal D&=\{02,03,04,13,14,15,24,25,35\},\\
\mathcal S_+&=\{13,15,35\},\qquad
\mathcal S_-=\{02,04,24\},\\
\mathcal L&=\{03,14,25\}.
\end{aligned}
\]

Use the unlocalized polynomial lattice

\[
R=\mathbb Z[X_d,t_s,u_l\mid d\in\mathcal D,
 s\in\mathcal S_+\cup\mathcal S_-,l\in\mathcal L]
 /(X_eX_o\mid e\in\mathcal S_-,o\in\mathcal S_+).
\]

The short-normal graph is \(u_s=t_sX_s\). The long normals are independent.
No occurrence or normal coordinate, or integer, is inverted. In particular
this homogeneous calculation does not replace this polynomial lattice by a
localization at nonhomogeneous monodromy units.

The finite support complex has one generator \([F,H]\) for every noncrossing
face \(F\) and mark set \(H\subseteq F\). Its degree is
\(3-|F|+|H|\), and its differential is

\[
\begin{aligned}
d[F,H]={}&
\sum_a(-1)^{|\{b\in F:b<a\}|}X_a[F\cup\{a\},H]\\
&+\sum_{j=0}^{|H|-1}(-1)^{3-|F|+j}u_{h_j}[F,H\setminus\{h_j\}].
\end{aligned}
\]

The first sum runs over the compatible additions. These are the differential
and orientation rules in source [S1]. There are 215 states.

For a distinguished occurrence label \(c\in\mathcal S_+\), tensor with

\[
K_{\rm occ}(X_c)=[Re_c\xrightarrow{X_c}Rp_c].
\]

Call the resulting 430-state complex \(C_c\). It has complete endpoint
subcomplex \(E_c\), short-boundary subcomplex \(B_c\), and quotient
\(Q_c=C_c/B_c\). The extra occurrence factor is not one of the monodromy
normal factors.

Give the independent polynomial variables independent fine degrees. The
basis weight of \([F,H]\otimes e_c^k\), for \(k=0,1\), is

\[
-\sum_{a\in F}\epsilon_{X_a}
+\sum_{h\in H\cap\mathcal S}(\epsilon_{X_h}+\epsilon_{t_h})
+\sum_{h\in H\cap\mathcal L}\epsilon_{u_h}
+k\epsilon_{X_c}.
\]

Here \(e_c^0\) denotes \(p_c\), and \(\mathcal S=\mathcal S_+\cup\mathcal S_-\).
A degree-zero term requires exactly the opposite coefficient weight. Any
mark would require a negative Rees or long-normal exponent, so no marked
state contributes to this particular component. For \(H=\varnothing\),
\(k=1\) requires \(c\in F\). Its required coefficient is

\[
\left(\prod_{a\in F}X_a\right)/X_c^k.
\]

This denotes exact cancellation in a divisible monomial, not inversion in the coefficient ring. For \(k=0\), take the product over all of \(F\); for \(k=1\),
remove the distinguished factor. Keep the term only when this monomial does
not contain both an even-sheet and an odd-sheet coordinate. The test is
exhaustive because fine weights specify at most one coefficient monomial.

For each \(c\), the complete degree-zero component has 47 generators, of
ranks \((8,23,14,2)\) in homological degrees zero through three. The short
boundary has 43 generators and the quotient has four. Both endpoint packets
are retained in the original complex; their degree-zero component has three
generators. The positive endpoint's occurrence pair is an actual unit pair
in this component, not a deleted normal state.

## 3. The exact homology sequence

Integral unit cancellations give

| Complex | Nonzero homology in fine degree zero |
|---|---|
| \(C_c\) | \(H_1=\mathbb Z^3\) |
| \(B_c\) | \(H_1=\mathbb Z^5\) |
| \(Q_c\) | \(H_2=\mathbb Z^2\) |
| \(E_c\) | \(H_0=\mathbb Z\) |

All other homology vanishes in this component. Every cancellation includes
projection, inclusion, and homotopy matrices satisfying

\[
p i=1,\qquad dh+hd=1-ip.
\]

The checker exports these matrices, not just their ranks.

In \(Q_c\), the degree-three top has boundary
\(\lambda_{03}+\lambda_{14}+\lambda_{25}\), where
\(\lambda_l=X_l p_l\). Thus the filling-difference module is

\[
U=H_2(Q_{35})_0
=\mathbb Z^3/\mathbb Z(1,1,1).
\]

Set \(V=H_1(B_{35})_0\) and \(W=H_1(C_{35})_0\). The short exact sequence
of complexes gives the exact sequence

\[
0\longrightarrow U\xrightarrow{A}V\xrightarrow{P}W\longrightarrow0.
\]

The map \(A\) is computed by lifting an actual quotient cycle and applying
the original differential, then applying the boundary contraction. It is not
chosen from its desired rank.

Use the quotient basis \((\lambda_{14},\lambda_{25})\); all other bases and
their explicit cycle representatives are recorded in the certificate. The
computed matrices are

\[
A=\begin{pmatrix}
-1&0\\-1&0\\0&1\\0&-1\\0&-1
\end{pmatrix},\qquad
P=\begin{pmatrix}
1&-1&0&0&0\\
0&0&1&1&0\\
0&0&1&0&1
\end{pmatrix}.
\]

This reconstructs the rank-two saturated attachment from the earlier
barycentric calculation in a smaller cellular basis. The previous
pulled-back-normal support equivalence explains that change of model [S3].
No equivalence to the different 245-state native-normal packet is asserted.

## 4. Use the group action on the whole transported family

The source group action is

\[
r(v)=v+2\pmod6,\qquad s(v)=2-v\pmod6,
\qquad G=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle.
\]

Source [S1] fixes the top-cell signs as \(+1\) for \(r\) and \(-1\) for
\(s\). On a marked state, multiply the top sign by the permutation signs of
\(F\) and \(H\). Coefficient variables and the distinguished occurrence
label are transported by the same permutation.

The reflection \(s\) fixes `35`, whereas rotation moves it through

\[
35\xrightarrow r15\xrightarrow r13\xrightarrow r35.
\]

Accordingly the single corrected complex \(C_{35}\) carries the stabilizer
\(H=\langle s\rangle\), not an artificial full \(G\)-action fixing `35`.
The complete \(G\)-object is the direct sum of all three label complexes.
The checker verifies the differential, support, grading, and all group
composition laws on the 1,290 states of this family.

This reflection preserves the two alternating occurrence sheets separately.
It is not silently identified with an abstract sheet-exchange involution in
a different coefficient model. Also, it need not fix the individual
blowup center used to describe one Morse gallery. The computation is on the
original cellular target and its transported occurrence factors.

On the calculated bases of \(U,V,W\), the stabilizer matrices are

\[
S_U=\begin{pmatrix}-1&1\\0&1\end{pmatrix},\qquad
S_W=\begin{pmatrix}-1&0&1\\0&1&0\\0&0&1\end{pmatrix},
\]

\[
S_V=\begin{pmatrix}
-1&0&0&0&1\\
0&-1&-1&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}.
\]

They square to the identity and satisfy
\(S_VA=AS_U\) and \(S_WP=PS_V\).

## 5. An integral equivariant splitting

Define

\[
X=\begin{pmatrix}
0&0&0\\-1&0&0\\0&0&1\\0&1&-1\\0&0&0
\end{pmatrix},\qquad
L=\begin{pmatrix}
-1&0&0&0&0\\0&0&0&0&-1
\end{pmatrix}.
\]

The exact identities are

\[
PX=1,\qquad LA=1,\qquad AL+XP=1,
\]

\[
S_VX=XS_W,\qquad LS_V=S_UL.
\]

Thus both a section of the inclusion map on homology and a retraction of the
attachment are integral and equivariant. In particular, taking invariants,
coinvariants, or any derived group-cohomology functor does not introduce an
extension defect into this sequence. The same matrix identities persist
after arbitrary scalar base change. This says nothing about whether the
homology-level section itself has a separately prescribed local geometric
realization.

For completeness, put

\[
B_U=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
B_W=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},
\qquad B_V=(AB_U\mid XB_W).
\]

All three matrices have determinant \(\pm1\). In these bases the actions
are, respectively, one transposition block, a transposition plus a fixed
line, and two transpositions plus a fixed line. Hence

\[
U\cong\mathbb Z[H],\qquad
V\cong\mathbb Z[H]^2\oplus\mathbb Z,\qquad
W\cong\mathbb Z[H]\oplus\mathbb Z.
\]

The final \(\mathbb Z\) is trivial for the source's displayed orientation
convention. The sequence is the standard inclusion of the first regular
summand and projection onto the remaining regular and trivial summands.

The splitting is not claimed unique. Its existence suffices for the
vanishing of this equivariant extension obstruction.

## 6. The full dihedral orbit and every prime

Transport \(X\) and \(L\) by the actual rotation matrices. Stabilizer
equivariance proves independence of the choice of coset representative;
the checker verifies every resulting square explicitly.

The three-label orbit modules are induced from the stabilizer. Direct
integral orbit bases, exported and checked against both generators of
\(G\), give

\[
U_{\rm orb}\cong\mathbb Z[G],
\]

\[
V_{\rm orb}\cong\mathbb Z[G]^2\oplus\mathbb Z[G/H],\qquad
W_{\rm orb}\cong\mathbb Z[G]\oplus\mathbb Z[G/H].
\]

They have ranks six, fifteen, and nine. The attachment is again the
inclusion of the first regular summand. It stays split after reduction
modulo two or three; no integer is divided out.

For \(H=C_2\), the cochain resolution has alternating operators
\(S-1\) and \(1+S\). On the regular two-dimensional module these are

\[
S-1=\begin{pmatrix}-1&1\\1&-1\end{pmatrix},\qquad
1+S=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

The kernel of \(S-1\) is the primitive diagonal, which is the image of
\(1+S\). The kernel of \(1+S\) is the primitive anti-diagonal, which is the
image of \(S-1\). These equations are valid over any coefficient ring,
including characteristic two. Therefore

\[
H^n(H,U)=0\quad(n>0).
\]

On the residual trivial line, the operators are zero and multiplication by
two. Over the integers the resulting cohomology is \(\mathbb Z/2\) in
positive even degrees and zero in odd degrees. The projection \(P\) is an
isomorphism on these residual groups because the same line occurs on both
sides.

Induced-module cohomology, or equivalently Shapiro's lemma [M1], now yields

\[
H^n(G,U_{\rm orb})=0\quad(n>0),
\]

\[
H^n(G,V_{\rm orb})\xrightarrow{\ P_*\ }
H^n(G,W_{\rm orb})
\]

as an isomorphism for every positive degree. Both sides are
\(\mathbb Z/2\) in positive even degrees and zero in odd degrees. There is
no three-primary group-cohomology class in these orbit modules.

Tensoring all modules by the reflection sign changes only the last
one-dimensional stabilizer character up to integral isomorphism: a negative
swap is conjugate to a swap by \(\operatorname{diag}(1,-1)\). The residual
\(\mathbb Z/2\) then occurs in odd rather than even degrees on both sides.
The attachment remains split. This is an optional twist control, not a
change silently made to the source.

This explains why the parallel three-cycle augmentation example cannot be
substituted for this computation. Its rank-two lattice carries a rotation
on one fixed packet. Here rotation changes the occurrence correction; the
complete orbit filling module is regular, not that isolated augmentation
module.

## 7. Consequence for the filling problem

A difference between two quotient fillings gives a class in \(U\). Its
change of lower attachment is \(A\) of that class. Since \(LA=1\), the
only such difference with zero attachment is zero, before or after imposing
this group symmetry. A nonempty affine filling problem whose translation
module is the computed \(U_{\rm orb}\) has no additional first
group-cohomology obstruction to an invariant homology-class choice.
This last assertion is about homology-class choices, not a claim that all
chain representatives or geometric lifts are strictly equivariant.

The residual two-primary ambient groups are not a new \(\Delta_J\): they
map isomorphically from the boundary module to the full module. In
particular they do not lie in the kernel detected by the filling attachment.

The following questions remain outside the proved scope:

- construction of an independently specified physical conductor
  nullhomotopy in the same mapping object as the corrected Morse map;
- additional chain-level endpoint, Rees, or spatial constraints not encoded
  by this homogeneous attachment sequence;
- other coefficient multidegrees and the native exceptional-normal model;
- the nonlinear geometric realizations and deck-stratum problems of Branch C.

A new physical secondary class cannot be justified by an unseen two- or
three-primary equivariant defect of this already split sequence.

## 8. Reproduction and evidence

Run:

```sh
python branch_a_dihedral_morse_attachment_checker.py \
  --output branch_a_dihedral_morse_attachment_certificate.json
```

The checker uses Python's standard library and exact integers. `Fraction`
is used only for inversion of matrices whose resulting inverse is checked
integral and whose determinant is a unit. This introduces no localized
coefficient or averaged group action.

The run passes 80,917 exact checks. It exports all three homogeneous
complexes, their integral contractions, group actions on homology, attaching
and inclusion matrices, equivariant splittings, and regular-module bases.
The all-degree cohomology conclusion follows from those explicit module
isomorphisms and the two-periodic resolution; it is not extrapolated from a
finite sequence of checked degrees.

Matrix data SHA-256:

```text
fee9a90d512187414bd967948362e829d11e862e9064650fa06c98e32135fd10
```

### Source references

[S1] `research/voevodsky/check_absolute_unlocalized_support_pc.rs`, pinned
commit above; blob `b967151cb0ee822e2361b9334a4ab26082c12682`. Supplies the
loaded differential, subcomplexes, group permutations and top orientation.

[S2] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor
Square.md`, same pin; blob `840258522d45e450e4f1e8bb927d9aae58c75566`.
Supplies the polynomial sheet fibre product and mixed-product relations.

[S3] Prior Branch A artifacts
`morse_pulledback_normal_support_equivalence_proof.md` and
`morse_q_filling_torsor_and_attachment_proof.md`. These distinguish the
pulled-back-normal source from the native-normal source and record the
ordinary support-equivalence and filling-attachment computations. The new
checker independently recomputes the cellular complex and its homogeneous
attachment; it does not rerun those full barycentric checkers.

### Mathematical references

[M1] Kiran S. Kedlaya, *Notes on class field theory*, Section 3.2,
induced modules and Shapiro's lemma:
`https://kskedlaya.org/cft/sec_cohom2.html`.

[M2] The same notes, Section 3.4, cyclic periodicity:
`https://kskedlaya.org/cft/sec_cohom-cyclic.html`.

[M3] Stacks Project, group cohomology as a derived invariants functor,
tag `0A2H`: `https://stacks.math.columbia.edu/tag/0A2H`.
