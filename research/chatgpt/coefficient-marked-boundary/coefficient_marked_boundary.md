# Coefficient-marked octagon boundary

Date: 2026-09-06

## Result and scope

Two distinct coefficient objects must be retained.

The source's integer loaded-cell Cech complex in its framed primitive-coefficient sector has an explicit integral deformation retraction onto the incidence complex of the eight-Cut, twelve-overlap graph. Its normalized marking space is contractible. The proof checks actual signed loaded-cell matrices, rather than assigning zero deformation ranks or inferring a coefficient contraction from an index contraction.

The earlier nonconstant conductor/localization diagram is larger. Its unshifted marking space is discrete, with objects given by unlocalized branch-polynomial pairs having a common conductor value. Fixing that value to one leaves independent positive-degree branch polynomials. That normalized space is not contractible.

The repository is pinned to commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`. The physical interpretation remains in the source's cellular fs/Kato primitive sector. This calculation does not reconstruct its upstream geometric six-functor construction or identify the nonconstant diagram with its complete physical relative system.

## 1. Signed primitive-coefficient complexes

The source `check_n8_full_twisted_cut_cech_lift.py` supplies eight chart complexes with 1,075 generators each, twelve overlap complexes with 125 generators each, and coordinate-projection restrictions. These projections are different from the earlier indexing inclusions.

A loaded cell is (F,M), with F a noncrossing face in the appropriate Cut link and M a subset of F. Set

\[
q(F,M)=|F|-|M|.
\]

In words: cohomological degree counts unmarked link diagonals. This places the primitive unit in degree zero. The source uses the same normal-sign convention on overlaps as on charts.

For allowed additions a and marks b, the differential is

\[
\begin{aligned}
d[F,M]={}&\sum_a(-1)^{|\{c\in F:c<a\}|}[F\cup\{a\},M]\\
&+\sum_{b\in M}(-1)^{4-|F|+\operatorname{pos}_M(b)}[F,M\setminus\{b\}].
\end{aligned}
\]

In words: add a compatible diagonal or remove a mark with the specified incidence and normal signs. Positions are numbered from zero. Both operators raise cohomological degree by one.

Write d=a+n, where a is the radial operator and n removes marks. Chart ranks in degrees zero through four are 135, 369, 375, 168, 28. Overlap ranks in degrees zero through three are 27, 54, 36, 8.

Restriction projects onto cells built only from diagonals compatible with both Cuts. Every other cell is sent to zero. The checker verifies every such map on every generator. Across all restrictions it finds 7,320 escaping radial arrows, all killed by projection, and no arrow entering the retained set from outside it. Therefore the projections commute with the differentials.

## 2. Explicit integral contractions

Let epsilon read the coefficient of the empty cell. On each chart and overlap define

\[
\omega=\sum_F(-1)^{|F|(|F|-1)/2}[F,F],\qquad d\omega=0,\qquad\epsilon(\omega)=1.
\]

In words: sum fully marked faces with those signs. This is a normalized degree-zero cocycle, not an assignment of coefficient one to all generators in every degree.

For nonempty F, let b be its least diagonal. Define

\[
h_0[F,M]=
\begin{cases}
(-1)^{4-|F|}[F,M\cup\{b\}],&b\notin M,\\
0,&b\in M.
\end{cases}
\]

In words: restore the least missing mark, with the inverse normal sign. On the empty face h0 is zero. On each nonempty fixed-face block it contracts n.

Correct for radial arrows by the finite sum

\[
H=\sum_{j\ge0}(-h_0a)^j h_0.
\]

In words: each successive correction increases face size, so the series terminates. Its coefficients are integers; it introduces no denominators.

On every generator, the checker verifies

\[
dH+Hd=1-i\epsilon,\qquad \epsilon i=1,\qquad i(1)=\omega.
\]

In words: the complete loaded complex retracts integrally onto the primitive line. This proves all its cohomology and the absence of torsion.

The contraction and cocycle commute with every coordinate restriction P:

\[
PH=HP,\qquad P\omega_i=\omega_{ij},\qquad\epsilon P=\epsilon.
\]

In words: the local reductions retain the actual comparison maps. A discarded face cannot become retained by enlarging it or changing its marks; on retained faces the chosen least diagonal is unchanged. Thus the full diagram of loaded primitive complexes is equivalent to the integral-unit diagram with identity restrictions.

## 3. Full loaded totalization

Let V be the direct sum of the eight chart complexes, E the direct sum of the twelve overlap complexes, and Delta the difference of their restrictions. The total complex is

\[
T_{\mathrm{cell}}^q=V^q\oplus E^{q-1},\qquad D(v,e)=(dv,\Delta v-de).
\]

In words: overlaps contribute one additional Cech degree. The minus sign on their internal differential makes the total differential square to zero.

Its 10,100 generators have degree ranks

\[
(1080,3276,3648,1776,320).
\]

In words: these are the complete cochain-group ranks, including every loaded degree.

Use H on vertex summands and minus H on edge summands. The mixed terms vanish because the contraction commutes with restriction. This gives an explicitly checked integral deformation retraction

\[
T_{\mathrm{cell}}\simeq S,
\qquad S=\left[\mathbb Z^8\xrightarrow{\delta}\mathbb Z^{12}\right].
\]

In words: the full loaded totalization reduces to the primitive coefficient incidence complex in degrees zero and one.

Each row of delta is minus one at the first endpoint and plus one at the second. Its seven nonzero Smith factors are one. Hence

\[
H^0(T_{\mathrm{cell}})=\mathbb Z,\qquad
H^1(T_{\mathrm{cell}})=\mathbb Z^5,\qquad
H^q(T_{\mathrm{cell}})=0\quad(q\ne0,1).
\]

In words: one primitive global coefficient and five free derived edge classes remain; there is no integer torsion. The four full differential ranks are 1,079, 2,192, 1,456, and 320.

Let r be empty-cell evaluation on a chosen chart. On global degree-zero cycles, overlap agreement makes the value independent of that choice. Define

\[
X_{\partial}=\operatorname{hofib}_1\left(
\operatorname{Map}_{D_\infty(\mathbb Z)}(\mathbb Z,T_{\mathrm{cell}})
\xrightarrow{r}\mathbb Z\right).
\]

In words: take normalized coefficient markings and retain their homotopies.

With these grading conventions,

\[
\pi_n\operatorname{Map}(\mathbb Z,T_{\mathrm{cell}})=H^{-n}(T_{\mathrm{cell}})
\quad(n\ge1).
\]

In words: higher paths detect negative cohomological degrees. The five positive-degree classes are not paths between unshifted markings.

Therefore

\[
\operatorname{Map}(\mathbb Z,T_{\mathrm{cell}})\simeq\mathbb Z_{\mathrm{disc}},
\qquad X_{\partial}\simeq *.
\]

In words: unnormalized markings form a discrete integer set; normalized markings form a contractible space. Fixing the entire primitive graph readout also gives a contractible fibre, since the loaded-to-graph augmentation is an equivalence. Its stable relative fibre is acyclic.

### Signs and relabelling

The source's odd Thom-normal factor cancels the scalar minus sign on each edge. Without it, the signless incidence matrix has seven unit Smith factors and one factor two: degree-zero cohomology is zero and degree-one cohomology is a free group of rank four plus one order-two class. Both matrices are checked independently.

A dihedral relabelling acts on a loaded generator with the product of the permutation signs on F and M. This commutes with d. Those signs cancel on fully marked faces, making omega equivariant. All sixteen actions are checked on every chart and overlap generator. The chosen contraction need not be equivariant: the equivariant augmentation is already an objectwise equivalence.

Consequently, for the admitted octagon relabellings,

\[
X_{\partial}//D_8\simeq BD_8.
\]

In words: its transport quotient retains the dihedral group of order sixteen and has no higher homotopy groups. Other Marici transports are not included.

## 4. The unreduced conductor diagram

Return to the earlier boundary index J_U with 7,100 objects and coefficient-localization inclusions. Write D for the twenty octagon diagonals, and define

\[
R_0=\mathbb Z[u_d,v_d\mid d\in D],\qquad
R_L=R_0[v_d^{-1}\mid d\in L].
\]

In words: retain all polynomial variables and invert only the prescribed second-family coordinates.

The supplied conductor row is

\[
Q_L=\left[R_L[z_+]\oplus R_L[z_-]\xrightarrow{e}R_L\right],
\qquad e(f_+,f_-)=f_+(0)-f_-(0).
\]

In words: compare the branch values at the conductor, in cohomological degrees zero and one. The differential is surjective and its kernel is

\[
K_L\cong R_L\oplus z_+R_L[z_+]\oplus z_-R_L[z_-].
\]

In words: choose their common constant value and independently choose the positive-degree part of each branch polynomial. The kernel inclusion is a natural quasi-isomorphism for every localization map. It does not discard the polynomial coefficients.

Define

\[
T_Q=\operatorname*{lim}_{J_U}Q_{F\setminus M}.
\]

In words: take derived sections of this nonconstant diagram. It is not identified with the coordinate-projection Cech object of Section 3.

### Exact Laurent-support calculation

For a Laurent monomial m, let N be the set of v-coordinates having negative exponent. Only N affects its diagram of integral copies. Crossing supports are absent everywhere. There are 903 noncrossing support sets, including the empty set.

On an intersection indexed by a nonempty compatible Cut set S, this monomial occurs only if the union of N and S is noncrossing. When it does,

\[
H^q(T_{S,m})\cong
\begin{cases}
\mathbb Z,&q=|N\setminus S|,\\
0,&q\ne |N\setminus S|.
\end{cases}
\]

In words: each negative coordinate not already forced unmarked by S contributes one degree.

Proof: the monomial diagram is the constant integral diagram on the forward-closed locus where all coordinates in N are inverted, extended by zero elsewhere. Its derived sections are the relative cochains of the index nerve and the sub-nerve where at least one negative coordinate is not inverted. This follows directly from the normalized cochain formula for a covariant diagram: a cochain on a chain of objects takes values at its last object. Forward closure makes the chains with zero coefficient exactly those wholly in the complementary subcategory.

Project onto the three states (absent, marked, unmarked) of the coordinates in N outside S. Forgetting other marks gives a natural zigzag contracting the remaining directions; the zigzag preserves the complementary subcategory. More explicitly, retain F on one side and only the selected marks, and on the other side retain S together with the selected coordinates present in F. Both objects map naturally to the first, and the projection followed by this section is the identity on selected states. The resulting pair of nerves is a product of intervals relative to its boundary. Its integral relative cohomology is one copy of the integers in top degree.

When a new Cut is not in N, restriction is the identity on the common top-degree group. When the new Cut lies in N, the nonzero cohomology groups occur in different degrees, so restriction on cohomology is zero. There are no triple Cut intersections. The long exact sequence of the assembly fibre computes the global answer from these degreewise vertex-to-edge matrices.

To make that calculation explicit, let V_N be the physical Cuts compatible with N, let I_N be the physical Cuts contained in N, and let E_N be the compatible pairs in V_N. Set k equal to the size of N. The vertex corresponding to d contributes in degree k minus the size of its intersection with N; the edge corresponding to a pair contributes in degree k minus the size of that pair's intersection with N. In any fixed degree the restriction matrix has the ordinary signed incidence entries whenever source and target degrees agree, and zero otherwise.

The equal-degree matrices are graph incidence blocks and disjoint signed-star blocks. Their nonzero Smith factors are one. The checker independently constructs and reduces every degree for all 903 support sets, and compares the result with the graph kernel/cokernel formula.

Examples, for one monomial and one branch basis vector:

| Negative support | Nonzero global cohomology |
|---|---|
| Empty | one free generator in degree zero; five in degree one |
| One physical Cut | five free generators in degree one |
| Two compatible physical Cuts | three free generators in degree one |

All 903 support sets and their ranks are in the certificate. Arbitrarily large exponents and branch degrees are covered by the support proof, not by a bounded polynomial test. The finite index nerve allows the monomial direct sums to commute with its derived-section calculation.

In particular,

\[
H^0(T_Q)\cong R_0\oplus z_+R_0[z_+]\oplus z_-R_0[z_-],
\qquad H^q(T_Q)=0\quad(q\notin\{0,1,2,3,4\}).
\]

In words: degree-zero markings retain unlocalized polynomial coefficients and independent branch terms. Negative Laurent supports contribute only positive degrees. All cohomology groups are free as abelian groups; the polynomial-module structure still has nontrivial support relations. Ordinary integral Bockstein differentials and their higher versions therefore produce no prime torsion in this model.

The certificate's aggregate support counts are not finite ranks of the entire polynomial model. They count one formal monomial per support and one branch basis mode. Every actual admissible exponent and branch mode must still be included.

## 5. Normalized markings of the unreduced diagram

The common conductor-value map on degree-zero markings is

\[
c(f_+,f_-)=f_+(0)=f_-(0)\in R_0.
\]

In words: read the shared branch value, including its polynomial dependence on source variables.

The unshifted mapping space is discrete, so the fibre at the polynomial unit is

\[
X_Q=\{(1+z_+a(z_+),\ 1+z_-b(z_-)):
 a\in R_0[z_+],\ b\in R_0[z_-]\}_{\mathrm{disc}}.
\]

In words: fixing conductor value one leaves arbitrary positive-degree polynomials on both branches. Distinct choices give different components. Every component has zero higher homotopy groups. For example, the branch pairs (1,1) and (1+z_+,1) are distinct normalized markings.

Constant diagonal coefficients give a natural inclusion of the primitive integral sector into K_L. Extracting the unit-monomial coefficient of the common branch value gives an additive, localization-natural retraction. These operations exhibit the constant incidence complex as a summand of the formal conductor model. They do not send an invertible ring variable to zero: coefficient extraction is additive, not a ring homomorphism. This also does not prove that coefficient extraction is the source's complete physical readout.

The two marking spaces computed here consequently have different normalizations. The framed primitive problem fixes its coefficient packet and leaves one marking. Conductor normalization in the unreduced polynomial problem leaves the displayed discrete family. A source-defined comparison with the full physical relative complex is still needed before any extra branch direction can be discarded physically.

## 6. Reproduction and provenance

Run:

```sh
python check_coefficient_marked_boundary.py --output coefficient_marked_boundary_certificate.json
```

The run performs 485,307 exact assertions. It checks explicit contractions on all 10,100 total generators, every coordinate restriction, differential identities, normalized cocycles, dihedral chain equivariance, integral incidence reductions, and all 903 Laurent-support cases. The proofs establish the infinite polynomial and homotopy conclusions. This is not proof-assistant verification.

The source rigidity checker assigns zero deformation ranks after referring to earlier claims. This computation does not use those assignments as proof: its loaded contraction and normalized cocycle are constructed explicitly.

Source paths at the pinned commit; exact blob hashes are in the certificate:

- `research/voevodsky/check_n8_full_twisted_cut_cech_lift.py`: signed loaded generators and coordinate projections.
- `research/voevodsky/check_n8_twisted_cut_cech_totalization.py`: Thom-sign choice and primitive coefficient incidence.
- `research/voevodsky/check_n8_multirees_conductor_stalk_kernel.py`: nonconstant exponent rule and conductor row.
- `research/voevodsky/check_physical_derived_pullback_after_transform.py`: six-point primitive integral line and road normalization.
- `research/voevodsky/check_n8_framed_physical_line_rigidity.py`: stated framing and rigidity, recalculated here for the explicit primitive loaded model.
- Ledger entries 536 and 537: positive Cech cohomology versus framed physical sections.
- Stacks Project, *Hom complexes*, tag `0A8H`: mapping-complex grading.
- Stacks Project, *Dold-Kan*, tag `019D`; Kerodon, *Comparison with the Homotopy Coherent Nerve*, tag `00SC`: complexes and mapping spaces.
