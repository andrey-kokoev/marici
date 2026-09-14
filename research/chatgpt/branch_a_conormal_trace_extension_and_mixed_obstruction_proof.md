# Branch A: the conormal trace extension and its quadratic continuation obstruction

## Result and scope

The difference of the two **fully normalized trace diagrams**, including their
specified branch homotopies, has first-conormal readout

\[
\mathfrak r_1(\widehat\nu_E-\widehat\nu_R)
=\beta\eta_{35}\otimes\ell_{35}
\in\operatorname{Ext}^1_R(A,A\otimes\mathcal L_{35}),
\]

where \(\eta_{35}=[X_{35}]^\vee\), and \(\mathcal L_{35}\) is the separately
retained occurrence-normal line. This is not a second scalar value. It is the
class of the explicit two-step module

\[
0\longrightarrow A v\longrightarrow E_{\beta,35}
\longrightarrow A\longrightarrow0,
\qquad
X_{35}u=\beta v,\quad X_{35}v=0,
\]

with every other short variable acting by zero. Its two underlying
\(A\)-basis vectors are \(u,v\). At invertible \(\beta\), this is the
first infinitesimal thickening in the labelled \(35\)-direction. At
\(\beta=0\), this particular module extension splits.

The next composition is not free. The full conductor resolution gives

\[
\operatorname{Ext}^1_R(A,A)\cong A^6,
\quad
\operatorname{Ext}^2_R(A,A)\cong A^{24},
\quad
\operatorname{Ext}^3_R(A,A)\cong A^{92}.
\]

Right multiplication by \(\eta_{35}\) has rank five and kernel
\(A\eta_{35}\). Consequently a three-layer ordinary module with rank-one
successive conductor quotients can continue this extension only in the same
normal direction. In particular, composing with the reflected \(04\)-normal
has a nonzero mixed-relation obstruction.

This calculation starts **after** the previously verified reciprocal reduction.
It reconstructs the entire ten-state trace target, all its endpoint terms,
and the conductor source resolution. It does not reconstruct or replace the
430-state pre-pairing complex. It does not identify the result with the physical
\(\Delta_J\), and it does not claim that every higher physical comparison must
be an ordinary three-layer module.

## 1. Coefficients, normal lines, and complete trace target

Use

\[
A=\mathbb Z[\beta,X_{03},X_{14},X_{25}],
\qquad
R=A[X_{02},X_{04},X_{24},X_{13},X_{15},X_{35}]/(I_-I_+),
\]

\[
I_-=(X_{02},X_{04},X_{24}),
\qquad I_+=(X_{13},X_{15},X_{35}),
\qquad I=I_-+I_+.
\]

The coordinate ordering is the negative triple followed by the positive triple.
The coefficients and the two-sheet normal form come from Entry 93 of
`andrey-kokoev/marici`, commit
`d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

Put \(x=X_{03}\), \(v=X_{25}\), and \(z=X_{35}\). Retain

\[
T=(P_E\otimes K_R(z))\otimes\mathfrak o_{02,35}[2],
\]

\[
dg=xp_{03}+vp_{25},\qquad
 dh_{03}=\beta xp_{03},\qquad dh_{25}=\beta vp_{25},\qquad dk=z.
\]

The ten generators are

\[
p_{03},p_{25};\quad
 g,h_{03},h_{25},p_{03}k,p_{25}k;\quad
 gk,h_{03}k,h_{25}k
\]

in homological degrees \(2,3,4\). Every tensor sign is retained; in particular

\[
d(gk)=xp_{03}k+vp_{25}k-zg,
\]

and similarly for the two native endpoint normals. The interval cycle is

\[
\xi=h_{03}+h_{25}-\beta g,
\qquad d\xi=0,\qquad d(\xi k)=-z\xi.
\]

The actual relative quotient removes the eight complete edge-endpoint states:

\[
q:T\longrightarrow\mathcal O=K_R(z)[3],
\qquad q(g)=e_0,\quad q(gk)=e_1,\quad de_1=-ze_0.
\]

Its endpoint connecting map remains

\[
\kappa(e_0)=xp_{03}+vp_{25},\qquad
\kappa(e_1)=(xp_{03}+vp_{25})k.
\]

The checker verifies this quotient and both endpoint connecting equations on
every source column. The local endpoints here are \(W_{03},W_{25}\), not the
original physical endpoint packets \(V_\pm\). The external ordered native-pair,
interval, and polarity lines remain those of the preceding trace; this step
does not assign new physical signs to them.

## 2. Reconstruct the source resolution and the two trace maps

A convenient free resolution \(P_A\to A\) has a basis in degree \(n\) consisting
of words of nonempty exterior blocks from the two triples. Adjacent blocks
belong to opposite sheets, and the total number of letters is \(n\).
The differential applies the Koszul differential to the **first** block. When
that block has length one, it is removed and its coordinate multiplies the
remaining word.

The first ranks are

\[
1,6,24,92,354.
\]

For singleton generators and the first relations,

\[
d e_i=X_i,\qquad
 d k_{ij}=X_i e_j-X_j e_i,\qquad
 d m_{j,i}=X_j e_i.
\]

The first formula for relations uses \(i<j\) on one sheet; the last uses
opposite sheets. Thus there are six same-sheet exterior relations and eighteen
ordered mixed annihilation relations.

### All-degree exactness

The resolution has an explicit \(A\)-linear contraction on the augmented
complex. For a coefficient monomial \(c\) and a word \(w\):

- If \(c\) has no short-variable factor, set the contraction to zero.
- If the short variables of \(c\) lie on the sheet opposite to the first block
  of \(w\), or \(w\) is empty, take the smallest variable dividing \(c\),
  remove one copy from \(c\), and prepend that singleton block.
- Otherwise use the usual ordered polynomial Koszul contraction on the first
  block: choose the smallest variable appearing in the coefficient or the
  block; insert it and remove it from the coefficient when it is not already
  a mark, with the exterior insertion sign; give zero when it is already marked.

The identities \(dh+hd=1\) on positive augmented degree, and
\(dh+hd=1-\iota\epsilon\) at degree zero, follow from the ordinary Koszul
cancellation and the vanishing of mixed products. The formula is valid for
arbitrary exponents and arbitrary later blocks. This proves exactness over the
integral base \(A\); it is not an application of a residue-field theorem to a
nonfield without justification. The checker tests the formula on all words
through degree three and monomial coefficients covering both branches,
squarefree and repeated variables. These are implementation checks of the
all-degree formula, not a substitute for the proof.

Every differential entry lies in \(I\). Therefore
\(\operatorname{Hom}_R(P_A,A)\) has zero differential. The ranks above give the
stated \(\operatorname{Ext}\) modules, with no integer torsion.

Place \(P_A\) in degree two. The two retained traces are

\[
\nu_E(p_A)=0,\qquad
\nu_E(e_i)=X_i\xi\quad(i=13,15,35),
\]

\[
\nu_R(p_A)=0,\qquad
\nu_R(e_i)=X_i\xi\quad(i=13,15),\qquad\nu_R(e_{35})=0,
\]

\[
\nu_R(k_{i,35})=X_i\xi k\quad(i=13,15).
\]

Every other column is zero. The checker verifies the maps through all 354
fourth-resolution states, not just on the six initial generators.

The homotopy \(U(e_{35})=-\xi k\) has the retained residual

\[
\nu_E-\nu_R-\delta U=\kappa_{\rm rel},\qquad
\kappa_{\rm rel}(m_{n,35})=X_n\xi k\quad(n=02,04,24).
\]

This sign convention uses \(\delta U=dU+Ud\) for a homological degree-one
homotopy. Both the raw difference and the residual relation map remain in the
calculation.

## 3. The first-conormal readout has a specified domain

Let \(\widetilde R=R_-\oplus R_+\). A normalized trace diagram is a point of

\[
\mathscr L=\operatorname{fib}\!\left(
R\operatorname{Hom}_R(A[2],T)
\longrightarrow
R\operatorname{Hom}_R(A[2],\widetilde R\otimes_R T)
\right).
\]

Such a point includes the trace and its branch nullhomotopies. The refined
readout is defined on this diagram, **not** on a trace with unspecified
normalization homotopies.

The supplied homotopies are polynomial on the whole positive sheet:

\[
H_E^+(p_A)=\xi,
\qquad H_R^+(p_A)=\xi,
\qquad H_R^+(e_{35})=\xi k.
\]

Their other columns and both negative-sheet homotopies are zero. Direct
calculation gives \(\delta H_i^+=\nu_i|_{R_+}\).

The normalization fibre has thirty summands with differential

\[
D(t,h_-,h_+)=(dt,t_--dh_-,t_+-dh_+).
\]

The normalization difference and the actual relative quotient give the chain map

\[
(t,h_-,h_+)\longmapsto
q(\bar h_+-\bar h_-)
\in (A\otimes_R\mathcal O)[-1].
\]

Its target is

\[
Ae_0[2]\oplus(A\otimes\mathcal L_{35})e_1[3]
\]

with zero differential. Thus the induced map on the relevant derived-map group
lands in

\[
A\oplus\operatorname{Ext}^1_R(A,A\otimes\mathcal L_{35}).
\]

On the recorded two maps, its matrix is

\[
\begin{pmatrix}
-\beta&-\beta\\
0&-\beta\eta_{35}\otimes\ell_{35}
\end{pmatrix}.
\]

Equivalently the second coordinate of the difference is
\(+\beta\eta_{35}\otimes\ell_{35}\). This sign follows from the positive-minus-negative
normalization difference, \(q\xi=-\beta e_0\), and the order \(\nu_E-\nu_R\).
It is not selected by imposing a positive final answer.

The relation-only map has negative-sheet homotopy
\(e_{35}\mapsto\xi k\); it gives the **same** positive conormal output. Hence the
readout retains the source-relation correction rather than accidentally
subtracting it away.

The checker proves the map on the full normalization fibre and checks all
source equations and both endpoint connecting equations. This makes the
readout invariant under homotopies of the complete normalized diagrams.
Changing their specified branch homotopies is a different input problem.

The preceding tangential-duality checker was separately rerun. It reproduced
its certificate exactly and confirmed that all ordinary scalar pairings have
equal columns. The present construction changes the output retained from the
normalized diagram; it does not assert an ordinary map from \(T\) that escapes
that scalar obstruction.

## 4. Represent the retained coordinate by an actual first-order module

The identification

\[
\operatorname{Ext}^1_R(A,A)
\cong\operatorname{Hom}_A(I/I^2,A)
\]

is immediate from the explicit free resolution. Define
\(\eta_i(e_j)=\delta_{ij}\).

The readout \(\beta\eta_{35}\otimes\ell_{35}\) is represented by

\[
0\longrightarrow A v\longrightarrow E_{\beta,35}
\longrightarrow A u\longrightarrow0,
\]

where

\[
X_{35}u=\beta v,\quad X_{35}v=0,\quad
X_i u=X_i v=0\quad(i\ne35).
\]

The quotient sends \(u\mapsto1\), \(v\mapsto0\); the injection sends the
normal-line generator to \(v\). Lifting the quotient unit to \(u\) and applying
\(de_i=X_i\) produces exactly the cocycle \(\beta\eta_{35}\).

This is an exact sequence of underlying \(R\)-modules, free of rank two over
\(A\). A replacement \(u\mapsto u+c v\) cannot change
\(X_{35}u=\beta v\). Therefore it is nonsplit over the displayed base. Its
extension class has exact \(R\)-annihilator \(I\); there is no additional
annihilator from \(A\), since \(A\) is a domain and \(\beta\ne0\) there.

The regulator grading must not be hidden. The raw cocycle has regulator degree
one. With \(u\) in degree zero, a degree-zero graded module presentation places
\(v\) in occurrence degree \(\epsilon_{35}\) and regulator degree \(-1\).
Equivalently keep \(\beta\) as an explicit homogeneous degree-one multiplier
of the unshifted first-conormal extension. Neither convention evaluates the
occurrence-normal line or changes a physical homological shift.

At invertible \(\beta\), rescaling the kernel basis by \(\beta\) identifies the
underlying module with

\[
R/(X_i:i\ne35,\ X_{35}^2)
\cong A[z]/(z^2).
\]

At \(\beta=0\), all short actions on this two-basis module vanish and this
particular extension splits. The entire regulator family is still free over
\(A\); the splitting of its central fibre is not a proof that the family
extension is zero.

## 5. Compute the complete quadratic composition law

To compute products, lift \(\eta_i\) to a degree-minus-one chain map
\(\Phi_i:P_A\to P_A\). It satisfies

\[
d\Phi_i+\Phi_i d=0,\qquad
\Phi_i(e_j)=\delta_{ij}.
\]

On the first relations the signs are

\[
\Phi_i(k_{a b})=\delta_{ia}e_b-\delta_{ib}e_a,
\qquad
\Phi_i(m_{a,b})=-\delta_{ib}e_a.
\]

The checker constructs the next components on all ninety-two degree-three
states and verifies the chain equation exactly. Product order is fixed by
\(\eta_a\eta_b=\eta_a\Phi_b\).

The complete \(24\times36\) product matrix has rank twenty-four and a signed
unit maximal minor. Its kernel has the twelve generators

\[
\eta_i^2=0\quad(i=02,04,24,13,15,35),
\]

\[
\eta_i\eta_j+\eta_j\eta_i=0
\quad(i,j\text{ on the same sheet},\ i<j).
\]

There are no additional quadratic relations. In particular, for opposite-sheet
labels,

\[
\eta_a\eta_b=-m_{a,b}^{\vee},\qquad
\eta_b\eta_a=-m_{b,a}^{\vee}
\]

are independent primitive classes. Their conormal-dual tensor factors are
retained when the coordinate bases are not evaluated.

The 216 triple products span the entire rank-ninety-two third Ext group, and
all left and right consequences of the displayed quadratic relations are
verified on the complete degree-three resolution. These calculations give a
consistency check on product signs and the source relations among relations.
They do not identify a nonlinear physical higher homotopy group with Ext.

This integral computation is consistent with the fibre-product Ext-algebra
construction of W. Frank Moore. The resolution contraction above supplies the
needed proof over the nonfield base used here; the residue-field statement is
not applied beyond its hypotheses.

## 6. The next rank-one-layer continuation has five obstructions

Let

\[
\alpha=\sum_i c_i\eta_i\in\operatorname{Ext}^1_R(A,A).
\]

The map

\[
\alpha\longmapsto\alpha\eta_{35}
\]

has rank five and exact kernel \(A\eta_{35}\). Its five nonzero columns have
disjoint, unit relation coordinates: two are same-sheet exterior relations,
and three are mixed-sheet ordered relations. For the raw trace class, the
map is multiplied by \(\beta\). Since \(\beta\) is a nonzero-divisor in
\(A\), its kernel remains the same.

This gives a concrete module-lifting test. Consider a three-layer module with
basis \(u,v,w\), with successive quotients annihilated by the conductor. Fix
its first extension by

\[
X_{35}u=\beta v\pmod{Aw}.
\]

A proposed next extension has \(X_i v=c_iw\), and arbitrary higher corrections
may be added to \(X_i u\) in \(Aw\). For every \(i\ne35\), either same-sheet
commutativity or a mixed-product relation forces

\[
\beta c_i=0.
\]

Thus \(c_i=0\) for all \(i\ne35\). The higher corrections to \(X_i u\) cannot
change these equations because every short variable kills \(w\).

A same-direction continuation does exist. For example

\[
X_{35}u=\beta v,\quad X_{35}v=\beta w,\quad X_{35}w=0,
\]

with every other short action zero is an explicit rank-three module. At
invertible \(\beta\), it is the usual \(35\)-axis second infinitesimal
neighborhood after the corresponding basis rescaling.

For the physical coefficient-label reflection \(v\mapsto3-v\), the label
\(35\) is sent to \(04\). A proposed successive \(04\)-extension instead gives

\[
X_{04}v=\beta w,
\qquad X_{04}X_{35}u=\beta^2w\ne0.
\]

This contradicts the exact source relation \(X_{04}X_{35}=0\). In the computed
Yoneda convention its obstruction is

\[
\beta^2\eta_{04}\eta_{35}
=-\beta^2m_{04,35}^{\vee}\ne0.
\]

This is a composition of two conormal extensions. It is **not** the square of
the reflection action; the coefficient-label involution itself still squares
to the identity. This test does not prohibit a larger middle layer or a
specified derived comparison with additional homotopies.

For comparison, the full ordinary first and second conductor thickenings have
ranks \(7\) and \(19\) over \(A\): one constant, six linear directions, and
twelve same-sheet quadratic monomials. The nine mixed quadratic monomials are
absent. A proposed higher trace object must not restore them by treating the
six normals as one regular six-dimensional polynomial chart.

## 7. Consequence and remaining physical scope

The scalar-blind difference now has a concrete first-order module
representative. Its nontriviality can be checked by the action of the single
labelled occurrence coordinate, without fitting a second scalar functional.
The next normal-extension test has five explicit independent obstructions.
The reflected mixed direction is one of them.

The output remains a readout of the already specified normalized trace maps,
including their branch and source-relation homotopies. It is not an
independently constructed physical normalization/Morse comparison. A physical
identification must transport those maps and their comparison cells into the
same diagram and account for the required higher conormal products. No value
of \(H_{\rm cond}\) or \(\Delta_J\) is assigned.

## Verification and references

Run:

```sh
python branch_a_conormal_trace_extension_and_mixed_obstruction_checker.py \
  --output branch_a_conormal_trace_extension_and_mixed_obstruction_certificate.json
```

The checker is standalone and uses only the Python standard library. It
reconstructs the source resolution, all local target differentials, both full
traces, their source-relation difference, the normalization fibre, the two-grade
readout, the exact extension action matrices, and every quadratic and cubic
product used above. It does not import a preceding checker or insert desired
Ext classes as unverified chain-map answers.

The run performed 13,549 counted checks. The source resolution ranks are
\(1,6,24,92,354\); the pair and triple product ranks are \(24,92\). A separate
replay of `branch_a_tangential_duality_scalar_pairing_checker.py` reproduced its
7,458 checks and its preceding certificate byte-for-byte.

References:

- Marici Entry 93, `Alternating Fusion Normalization-Conductor Square`, pinned
  commit above: ring, augmentation, ordered sheet difference, and polarity.
- The preceding `branch_a_tangential_duality_scalar_pairing_proof.md` and
  `branch_a_full_normalization_duality_and_two_grade_trace_proof.md`: the
  explicitly restated trace target, maps, and scalar-obstruction context.
- Stacks Project, tags `06XP` and `06XU`: Yoneda extension classes and their
  equivalence with derived Ext.
- Stacks Project, tag `0A8H`: Hom differentials and composition conventions.
- W. Frank Moore, *Cohomology of Fiber Products of Local Rings*,
  arXiv:0704.3631: alternating resolutions and fibre-product cohomology. The
  nonfield integral exactness needed here is proved separately above.
