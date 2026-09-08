# Branch A: independent coefficient rings, two-branch dilation, and retained occurrence trace

## Result and scope

This calculation constructs the derived incidence induced by the two existing branch gradings of the normalization ring, using independent target occurrence coordinates. It computes its entire coefficient kernel, transports the complete occurrence complex and both endpoint connectors, and constructs finite free representatives of the two preceding excess-trace maps.

Both trace classes remain independent. Their images are supported at the intersection of the two dilation divisors. The incidence is zero where both dilation parameters are invertible. Equating the two parameters produces a nonflat thickening and additional derived terms; it does not give the flat Rees deformation on the chosen mixed-direction chart.

These conclusions concern the specified affine derived incidence. They do not assert that it is the physical tangential Pochhammer–Cousin kernel, a Gysin counit, or the conductor–Morse comparison. In particular, no value of the physical Delta_J is assigned.

## 1. Separate the coefficient rings

Put

\[
A=\mathbb Z[\beta,X_{03},X_{14},X_{25}],
\]

\[
S=A[x_{02},x_{04},x_{24},x_{13},x_{15},x_{35}],
\qquad
R=S/(J_-J_+),
\]

\[
J_-=(x_{02},x_{04},x_{24}),
\qquad
J_+=(x_{13},x_{15},x_{35}).
\]

In words: S is the polynomial ambient ring; R is the actual glued normalization ring. Its conductor quotient is A. The source coefficients x_i satisfy the mixed-sheet relations only after passage to R.

Use a distinct target ring

\[
B=A[Y_{02},Y_{04},Y_{24},Y_{13},Y_{15},Y_{35},Y_{02}^{-1},Y_{35}^{-1}],
\qquad
D=B[t_-,t_+].
\]

In words: the target coordinates Y_i are independent. Only Y02 and Y35 are inverted. This is already enough to test the mixed-direction open needed by the preceding tangential-localization proposal; further target localization does not reverse the obstruction below.

The existing two-sheet bigrading defines the ambient dilation map

\[
\gamma:S\longrightarrow D,
\qquad
x_a\longmapsto t_-Y_a\ (a\in J_-),
\qquad
x_b\longmapsto t_+Y_b\ (b\in J_+).
\]

In words: scale the two branch coordinate triples independently. Neither t_- nor t_+ is the regulator beta or one of the previously prescribed graph slopes.

There is no ring map R to D with these formulas: a mixed product would map to t_-t_+Y_aY_b, which is nonzero in D. The appropriate object is the derived fibre product, whose coefficient complex is

\[
\mathcal K=D\otimes_S^{\mathbb L}R.
\]

For an R-complex M the corresponding operation is

\[
\mathfrak T(M)=D\otimes_S^{\mathbb L}\operatorname{Res}^{R}_{S}M.
\]

In words: forget to the ambient polynomial ring and perform derived base change. This is an actual derived correspondence. It is not an ordinary tensor product over R pretending that the forbidden ring map exists.

The minimal free complexes below are models as D-complexes. Their direct-sum normal forms are not asserted to be splittings of the complete derived R-algebra action. The explicitly required source maps and comparison maps are transported separately and checked.

## 2. A fifty-state free resolution

Order the negative indices as (02,04,24), and the positive indices as (13,15,35). Let P_0=S. For n at least one, use basis states e_{U,V} with nonempty subsets U of the negative triple and V of the positive triple, satisfying

\[
|U|+|V|=n+1.
\]

The differential from degree one is

\[
d e_{\{a\},\{b\}}=x_ax_b.
\]

In higher degrees it is

\[
\begin{aligned}
d e_{U,V}={}&
\sum_{a\in U,\ |U|>1}(-1)^{\operatorname{pos}(a,U)}x_a e_{U\setminus a,V}\\
&+(-1)^{|U|-1}
\sum_{b\in V,\ |V|>1}(-1)^{\operatorname{pos}(b,V)}x_b e_{U,V\setminus b}.
\end{aligned}
\]

In words: tensor the two truncated Koszul resolutions of the branch ideals, then attach their multiplication map to S. Positions start at zero.

Its ranks in homological degrees zero through five are

\[
(1,9,18,15,6,1).
\]

This resolves R over S. To see exactness for arbitrary coefficients, resolve the negative ideal over its three-variable polynomial ring and the positive ideal over its separate three-variable polynomial ring. The truncated Koszul resolutions have free homology over A and remain exact on extension to S. Their tensor product resolves the product ideal because the two variable sets are disjoint. Multiplication identifies the tensor product of the two ideals with their product: both have the same independent monomial basis consisting of monomials containing at least one variable of each type. Attaching S gives the displayed resolution of R.

The checker verifies the universal polynomial square-zero equations before imposing any mixed relation, and then verifies the independently dilated equations.

## 3. Exact two-parameter kernel

A target-unit change of basis turns the two Koszul rows into

\[
(t_-,0,0),\qquad(t_+,0,0).
\]

For example, the negative basis is

\[
\frac{e_{02}}{Y_{02}},\qquad
 e_{04}-\frac{Y_{04}}{Y_{02}}e_{02},\qquad
 e_{24}-\frac{Y_{24}}{Y_{02}}e_{02}.
\]

The positive basis uses e35/Y35 first, followed by e13-(Y13/Y35)e35 and e15-(Y15/Y35)e35. Both basis matrices and their inverses are exported. No source occurrence or dilation parameter is inverted.

Each truncated three-variable Koszul complex now splits into a free bottom generator, two copies of K(t) starting in degree zero, and one copy starting in degree one. Tensoring these decompositions gives the following direct blocks of the fifty-state kernel:

| Block | Bottom degree | Multiplicity |
|---|---:|---:|
| K(t_-t_+) | 0 | 1 |
| K(t_-) | 1 | 2 |
| K(t_+) | 1 | 2 |
| K(t_-) | 2 | 1 |
| K(t_+) | 2 | 1 |
| K(t_-,t_+) | 1 | 4 |
| K(t_-,t_+) | 2 | 4 |
| K(t_-,t_+) | 3 | 1 |

Here K(f) is the two-term complex with differential f; K(f,g) is the ordered four-state Koszul complex. The table specifies placement rather than suppressing shift signs. All orientation signs of the block basis are included in the certificate.

The pair t_-,t_+ is regular over D. Therefore

\[
H_0(\mathcal K)=D/(t_-t_+),
\]

\[
H_1(\mathcal K)=
(D/(t_-))^2\oplus(D/(t_+))^2\oplus(D/(t_-,t_+))^4,
\]

\[
H_2(\mathcal K)=
D/(t_-)\oplus D/(t_+)\oplus(D/(t_-,t_+))^4,
\]

\[
H_3(\mathcal K)=D/(t_-,t_+),\qquad H_{n>3}(\mathcal K)=0.
\]

In words: the ordinary incidence is the union of the two dilation axes. Its higher derived terms include both axis-supported and intersection-supported pieces. Keeping only D/(t_-t_+) is not derived base change.

## 4. Transport the complete occurrence object and conductor source

The preceding relative interval output was

\[
\mathcal O_R=K_R(x_{35})[3],
\qquad d e_1=-x_{35}e_0.
\]

Its source was A[2], resolved over R in the preceding calculation. After restriction to S, use the finite S-projective resolution

\[
Q=K_S(x_{02},x_{04},x_{24},x_{13},x_{15},x_{35})[2].
\]

It has sixty-four states. A free S-model for the whole target is

\[
\widetilde{\mathcal O}=P\otimes_S K_S(x_{35})[3],
\]

with one hundred states. Its augmentation to the original two-state R-complex is a quasi-isomorphism because the additional Koszul factor is bounded free.

Thus

\[
\mathfrak T(A[2])=D\otimes_S Q,
\qquad
\mathfrak T(\mathcal O_R)=D\otimes_S\widetilde{\mathcal O}.
\]

In words: neither source nor target is replaced by its homology before the new base change. The original nonsplit occurrence extension is represented by its complete complex.

## 5. Explicit finite free lifts of both excess maps

Let e_W denote an exterior generator of Q, with negative subset U and positive subset V. The degree of e_W before the common source shift is |U|+|V|. In the target write e_{U,V} for a state of P and k for the occurrence partner.

The first map F_E has the following nonzero columns:

\[
F_E(e_b)=x_b e_0\quad(b\text{ positive}),
\]

\[
F_E(e_U\wedge e_V)=(-1)^{|V|-1}e_{U,V}\otimes e_0
\quad(U\ne\varnothing,\ V\ne\varnothing).
\]

The second map F_R has:

\[
F_R(e_b)=x_b e_0\quad(b=13,15),\qquad F_R(e_{35})=0,
\]

\[
F_R(e_b\wedge e_{35})=x_b e_1\quad(b=13,15),
\]

\[
F_R(e_U\wedge e_V)=(-1)^{|V|-1}e_{U,V}\otimes e_0
\quad(U,V\ne\varnothing,\ 35\notin V),
\]

\[
F_R(e_U\wedge e_V)=(-1)^{|V|-2}e_{U,V\setminus35}\otimes e_1
\quad(U\ne\varnothing,\ 35\in V,\ |V|>1).
\]

Every unspecified column is zero. In the formulas with e_{U,V}, the extra e0/e1 specifies the occurrence factor; it is not a second copy of the conductor unit.

These have respectively fifty-two and forty-six nonzero entries. The checker verifies their full chain equations over S, before the mixed relations are imposed. Composing with the augmentation P to R recovers exactly the preceding epsilon_E and epsilon_R on all relevant source columns.

For clarity about source resolutions, the comparison from the ambient Koszul resolution to the R-free conductor resolution is the identity on its six degree-one generators. A same-sheet wedge maps to its Koszul relation. A mixed wedge e_a wedge e_b maps to m_{ab}-m_{ba}. The comparison extends in higher degrees by exactness and projectivity. The old two-state target sees only these displayed degrees. Thus the two finite free lifts represent the restricted old morphisms, not newly fitted source maps.

Substitute the two independent dilation formulas into every coefficient. The same full equations hold over D.

## 6. Two trace classes survive as a split supported submodule

All entries of the new source and target differentials belong to (t_-,t_+). Consequently, reducing any chain-homotopy boundary modulo that ideal gives the zero map.

Define two coefficient functionals on degree-zero cochain maps:

\[
\ell_1(F)=
[e_{\{02\},\{35\}}\otimes e_0]
F(e_{02}\wedge e_{35})\bmod(t_-,t_+),
\]

\[
\ell_2(F)=
[e_{\{02\},\{13\}}\otimes e_0]
F(e_{02}\wedge e_{13})\bmod(t_-,t_+).
\]

In words: evaluate two explicitly specified mixed-relation columns and retain their coefficients on two specified resolving target states. Both functionals annihilate every Hom boundary for arbitrary polynomial coefficients.

Their matrix on the transported maps is

\[
\begin{pmatrix}
\ell_1(F_E)&\ell_1(F_R)\\
\ell_2(F_E)&\ell_2(F_R)
\end{pmatrix}
=
\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

In words: the two maps remain independent with a unit determinant. Their difference is nonzero; it is not enough to read only the scalar quotient.

Both parameters annihilate both map classes. On the source Koszul complex, exterior multiplication by e02/Y02 gives a homotopy for t_-, and exterior multiplication by e35/Y35 gives one for t_+. Composing either source homotopy with F_E or F_R gives the full map homotopies. They are exported and checked column by column.

Therefore the generated submodule is exactly

\[
D[F_E]\oplus D[F_R]\cong(D/(t_-,t_+))^2.
\]

In words: it is a split rank-two module over B, supported on the intersection of the two dilation divisors. This is a statement about the two identified classes; the entire new Hom group is not claimed to have rank two.

The regulator beta is untouched. In particular, the previously recorded full trace continues to have relative image -beta F_E, whereas its native/occurrence-collapsed version has zero image.

## 7. Both endpoint connectors remain part of the transformation

The pre-quotient local interval output was

\[
T_R=(P_E\otimes K_R(x_{35}))[2],
\]

\[
dg=X_{03}p_{03}+X_{25}p_{25},\qquad
 dh_{03}=\beta X_{03}p_{03},\qquad
 dh_{25}=\beta X_{25}p_{25}.
\]

Its free S-model has five hundred states after tensoring P. Four hundred belong to the two complete edge-endpoint packets; the quotient has the one hundred occurrence states from Section 4.

Let u be a degree-m state of P. The connecting map is

\[
\kappa(u\otimes e_j)
=(-1)^m u\otimes(X_{03}p_{03}+X_{25}p_{25})k^j,
\qquad j=0,1.
\]

In words: the original two endpoint coefficients and the coefficient-resolution sign remain. The checker verifies the full differential and the connecting-map equation on every state.

Writing xi=h03+h25-beta g, the complete trace maps are obtained by replacing the quotient generator by xi. If tilde F_i is the graded lift using g, and B_i uses h03+h25, then

\[
a_i=\delta\widetilde F_i,\qquad
\delta B_i=\beta a_i,\qquad
\nu_i=B_i-\beta\widetilde F_i,\qquad
q\nu_i=-\beta F_i.
\]

In words: both excess maps retain the entire endpoint-lifting equation and its native-normal correction. These identities are checked before and after diagonal specialization, including all source-resolution columns. The endpoint states here are W03 and W25, not the original physical endpoint packets V_plus and V_minus.

The common ordered reciprocal-normal orientation line is carried externally as in the preceding calculation. It is not evaluated, and no new scalar residue or shift is inferred.

## 8. Equating the dilation parameters is a derived operation

Set t_-=t_+=t, with D_delta=B[t]. Since all coefficient models are bounded free, substitute into the complete complexes and maps, not into their homology groups.

The kernel has a polynomial block decomposition

\[
\mathcal K_\Delta\cong
K(t^2)\oplus K(t)[1]^8\oplus K(t)[2]^{10}
\oplus K(t)[3]^5\oplus K(t)[4].
\]

This formula suppresses only unit shift-sign changes, which are included in the exported bases. No t-power is inverted. The exact homology is:

| Degree | Homology |
|---:|---|
| 0 | D_delta/(t^2) |
| 1 | (D_delta/(t))^8 |
| 2 | (D_delta/(t))^10 |
| 3 | (D_delta/(t))^5 |
| 4 | D_delta/(t) |
| 5 | 0 |

The new upper terms are explained by the independent two-normal blocks. On the diagonal,

\[
K(t_-,t_+)\otimes D_\Delta=K(t,t)
\cong K(t)\otimes\Lambda(\eta),
\qquad \eta=e_+-e_-,\qquad d\eta=0.
\]

In words: identifying the two dilation parameters creates a retained excess generator. Its ordered determinant satisfies e_- wedge eta = e_- wedge e_+.

The complete transformed conductor source has homology multiplicities

\[
(1,5,10,10,5,1)
\]

in degrees two through seven, all over B=D_delta/(t).

The complete transformed occurrence target has homology multiplicities

\[
(1,9,18,15,6,1)
\]

in degrees three through eight, also all over B. Thus the original upper occurrence information has not been replaced by a scalar.

The checker gives a chain homotopy for multiplication by t on the full one-hundred-state occurrence target. Together with the same unit detector matrix, this proves

\[
D_\Delta[F_{E,\Delta}]\oplus D_\Delta[F_{R,\Delta}]
\cong(D_\Delta/(t))^2.
\]

Every complex, both maps, their full endpoint lifts, and their connecting maps were checked against direct diagonal substitution.

## 9. Generic support and the flat Rees test

Since Y02 and Y35 are target units,

\[
(t_-Y_{02})(t_+Y_{35})/(Y_{02}Y_{35})=t_-t_+.
\]

The derived incidence is zero after inverting both t_- and t_+. Each block in Section 3 is then contractible. Its two supported trace classes are already zero after inverting either parameter because both annihilate them.

On the common diagonal the ordinary incidence is B[t]/(t^2), and its higher derived terms are the ones listed above. It is not flat over B[t].

For the source's homogeneous conductor ideal, the flat Rees deformation embeds in R[t,t^{-1}]. In the Y-coordinate presentation, saturation removes the t-torsion. On the chosen target open,

\[
(t^2):t^\infty=(1).
\]

In words: the flat strict-transform chart is empty. Equivalently, the normal-cone relation Y02 Y35=0 is incompatible with inverting both Y02 and Y35. The raw nonflat incidence cannot be relabelled as that flat Rees chart.

The two-parameter version has the same limitation when both dilation parameters are required to be invertible: saturation by t_-t_+ makes the chart empty. The axes retained by the derived incidence are special-parameter data, not a generic mixed-sheet overlap.

Therefore this canonical two-branch ambient dilation does not supply the physical generic tangential trace. Its complete derived boundary and its two nonzero trace maps are explicit inputs for a separately justified supported operation. A physical correspondence must differ from this common affine-dilation mechanism or must state a boundary-supported operation with its actual source shift, coefficient actions, and endpoint comparisons. No such identification is assumed here.

## 10. Reproducibility and sources

The standalone checker requires only the Python standard library. It constructs the universal polynomial resolution, both independent and diagonal derived incidences, the source and target projective models, all matrix inverses and retained nonunit blocks, both trace maps and their scalar-annihilating homotopies, the full five-hundred-state endpoint diagram, and every diagonal compatibility equation.

The new calculation performs 20,685 exact checks. Its semantic certificate hash is

`572744c48e186108de771a68517d7a7eaef4997f1b6573c47b62e5a90e663a6e`.

The immediately preceding relative-interval checker was separately replayed. It returned 11,724 checks and semantic hash

`f55f83ddbf172370dd945b895d1880fa0f47f7218f59988f851c68dba70dd609`.

Run:

```sh
python branch_a_separated_coefficients_derived_dilation_checker.py --output branch_a_separated_coefficients_derived_dilation_certificate.json
```

Pinned source repository: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

Source inputs:

- Ledger Entry 93, `20260814-93 Alternating Fusion Normalization-Conductor Square.md`: the two branch rings, mixed-product ideal, and conductor grading.
- Ledger Entry 97, `20260814-97 Reciprocal-Twist D03 Bivariant Road Trace.md`: the independent tangential Laurent ring and the support/twist distinction.
- The preceding file `branch_a_w03_relative_interval_occurrence_extension_proof.md`: the two trace maps, occurrence complex, and endpoint equations; replayed independently.

General constructions:

- Derived tensor products and bounded free models: Stacks `https://stacks.math.columbia.edu/tag/06XY`.
- Koszul change of generators: Stacks `https://stacks.math.columbia.edu/tag/0621`.
- Regular-sequence exactness: Stacks `https://stacks.math.columbia.edu/tag/062F`.
- Hom differentials: Stacks `https://stacks.math.columbia.edu/tag/0A8H`.
- Conormal algebra and normal cone: Stacks `https://stacks.math.columbia.edu/tag/062Z`.
- Rees blowup charts: Stacks `https://stacks.math.columbia.edu/tag/01OF`.

No auxiliary source normal, regulator, or physical channel has been identified with a dilation parameter. No ordinary tangent Laurent trace, physical Gysin map, or physical Delta_J is asserted by this coefficient test.
