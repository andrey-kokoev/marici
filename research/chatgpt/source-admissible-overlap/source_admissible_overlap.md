# Source-local audit of the octagon overlap homotopy

Date: 2026-09-06. Repository input remains pinned to `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

## Result and scope

The previous homotopy `(Delta rho)H` is correct over integer coefficients. Its chosen contraction, however, restores marks on unrelated diagonals and is not strictly dihedrally equivariant. Some resulting columns cannot be promoted to the identity on the prescribed localized coefficient modules.

A replacement is constructed below. It changes only the two Cut coordinates, preserves every spectator face and mark, uses integer coefficients, and is strictly dihedrally equivariant. It preserves the old normalized boundary extension. With the mandatory Cut coordinates retained in the boundary coefficient rings, every coefficient map is a permitted localization inclusion.

A separate, explicitly declared independent-normal test restores a polynomial weight to each normal differential. In that test, the original unweighted chart restrictions are not homotopic on overlaps. A nonzero value on a global cocycle proves the obstruction. Multiplying each chart restriction by its own normal factor, and correcting the pair homotopy by the same rule, solves the polynomial and multigraded equations without division.

The weighted test is not asserted to reconstruct the complete physical PC/Rees complex. It tests a specific extension of the audited cellular differential, motivated by the source's retained one-normal Koszul factors. The corrected polynomial map does not establish the still-missing physical Gysin or endpoint-relative comparison.

## 1. Inputs and admissibility conditions

An interior generator is a pair `(F,M)` of noncrossing octagon diagonals and a marked subset. Its cohomological degree is

\[
q(F,M)=|F|-|M|.
\]

In words: degree counts unmarked diagonals. The full differential has radial incidence terms and normal mark-removal terms, with the dimension-five signs from the preceding construction. Link charts and overlaps retain the dimension-four normal signs. There are 12,425 interior generators, eight Cut charts, and twelve compatible Cut pairs.

For a compatible pair `c<d`, let `E_cd` denote its existing link-overlap complex and let

\[
m_{cd}=P_{d,cd}\rho_d-P_{c,cd}\rho_c.
\]

In words: compare the two marked-normal extractions after their coordinate projections to the common overlap. These are the same maps as in `boundary_interior_extension.md`.

The pair-local condition tested here is exact: a homotopy is zero unless both Cut diagonals are in `F` and exactly one is in `M`; its only allowed output deletes the two Cut labels and leaves all other face and mark coordinates unchanged. This condition is stronger than retaining one fixed spectator facet. It does not confuse the scalar occurrence coefficient `X_d` in source entry 83 with a normal mark or with `q_d-1`. Scalar coefficients remain separate.

## 2. The old filler fails a coefficient test

On the pair `03,05`, the old filler has a nonzero coefficient-one term

\[
[\{04\},\varnothing]\longmapsto[\{04\},\{04\}].
\]

In words: it restores the mark on diagonal `04`, which is not one of the two Cuts.

The source localization rule is

\[
L(F,M)=F\setminus M,
\qquad
R_L=R_0[v_a^{-1}:a\in L].
\]

In words: precisely the unmarked coordinates are inverted. Include the mandatory Cut coordinates `03,05` in the overlap coefficient ring. The displayed old column would still require a coefficient-identity map from a module allowing `v_04^{-1}` to one that does not allow it. An `R_0`-linear map sending one to one would imply

\[
v_{04}\,f(v_{04}^{-1})=1,
\]

which is impossible in the target polynomial/Laurent ring: only `v_03` and `v_05` are inverted there. This invalidates that coefficientwise promotion of the old formula, not its earlier integer-linear chain identity.

The full audit finds 3,408 old nonzero terms, of which 1,308 add a spectator face, 2,652 add a spectator mark, and 1,816 fail this coefficient-identity localization condition. These are overlapping term counts. A strict dihedral covariance counterexample is also included in the certificate; it does not prove that the old map lacks a homotopy-coherent equivariant enhancement.

## 3. Pair-local replacement

For a mixed pair input write

\[
\{c,d\}\subseteq F,\quad M\cap\{c,d\}=\{s\},\quad
\{t\}=\{c,d\}\setminus\{s\},\quad
F'=F\setminus\{c,d\},\quad M'=M\setminus\{c,d\}.
\]

In words: `s` is the marked Cut, `t` the unmarked Cut, and primes denote the untouched spectator coordinates.

Define

\[
\ell^{\mathrm{pair}}_{cd}[F,M]
=-(-1)^{\#\{a\in F':a>s\}+\#\{a\in M':a>s\}+\#\{a\in F':a<t\}}
[F',M'],
\]

and define it to be zero on all other inputs.

In words: remove the pair with its induced orientation and change no spectator coordinate.

The verified equation is

\[
d_E\ell^{\mathrm{pair}}+\ell^{\mathrm{pair}}d_I=m.
\]

In words: it fills the same overlap discrepancy as the previous homotopy.

### Proof by pair states

If exactly one Cut is present and marked, the only differential term on which the homotopy is nonzero is radial insertion of the missing Cut. Its sign forces the displayed coefficient to equal the corresponding signed extraction. If both Cuts are marked, their two mark-removal contributions cancel. If both are unmarked, both sides vanish. On a mixed-pair input, the spectator radial and normal terms cancel with the overlap differential using the degree-minus-one sign. Other pair states contribute zero.

Every nonzero coefficient is therefore forced within the specified pair-local ansatz. There are 250 allowed inputs per overlap and 3,000 across all twelve overlaps. The checker verifies the complete equation on every interior generator for every overlap; it also checks that each coefficient is forced by its unique precursor.

The interior primitive cocycle is fully marked. Hence the replacement vanishes on it, so the extension still satisfies

\[
\Phi_{\mathrm{pair}}=(\rho,\ell^{\mathrm{pair}}),\qquad
D\Phi_{\mathrm{pair}}=\Phi_{\mathrm{pair}}d_I,\qquad
\Phi_{\mathrm{pair}}(\omega_I)=\omega_\partial.
\]

In words: the old unit-coefficient boundary value is unchanged.

The new and old fillers are higher-homotopic in the original integer complexes. With

\[
\delta=\ell^{\mathrm{pair}}-\ell^{\mathrm{old}},\qquad K=-\delta H,
\]

one has

\[
d_EK-Kd_I=\delta.
\]

In words: the old contraction compares the two ordinary fillers. This comparison itself is not claimed to satisfy the new coefficient-localization restriction.

## 4. Symmetry and coefficient locality

Dihedral relabelling acts with the permutation signs on `F` and `M`, and the overlap edge acquires the sign of its endpoint permutation. With these source orientation conventions, `ell_pair` commutes strictly with every one of the sixteen group elements. The formula is determined by the two Cut labels and spectator orientations; there is no choice of least spectator diagonal and no averaging by the group order. The group law for permutation signs supplies higher compatibility automatically.

For coefficient-localization compatibility, retain the Cut set `S` as part of the boundary metadata and use

\[
R_{S\cup(F\setminus M)}
\]

on a link generator.

In words: coordinates belonging to the prescribed Cut stratum remain localized even though they are omitted from its link-coordinate list. This is the same forced-unmarked Cut rule used by the earlier boundary index.

For every nonzero pair-local column,

\[
F\setminus M\subseteq\{c,d\}\cup(F'\setminus M').
\]

In words: no allowed input inverse is lost. The new coefficient map is the actual inclusion of the two localized rings. It preserves each monomial and therefore all the coordinate-exponent filtrations of this formal ring model. Chart extractions satisfy the analogous inclusion with their one mandatory Cut.

These coefficient inclusions commute with the conductor differential on both polynomial branches, since that differential only evaluates the branch coordinate at zero and subtracts. Thus the maps extend to the corresponding cellular/conductor bicomplex. This is not an identification with the earlier derived-section object `T_Q`, nor with the full physical coefficient target.

## 5. Independent normal factors: a separate lifting test

Source entry 115 retains the one-normal complex with differential `t_i x_i`, as well as the independent conormal factors. Entry 38 likewise distinguishes the normal Koszul factor from scalar occurrence weights. To test whether the unit-coefficient extension survives a literal restoration of such factors, define

\[
P=\mathbb Z[w_a:a\in\mathcal D],\qquad
d_w=a+\sum_b w_b n_b.
\]

In words: keep the existing radial incidences and replace each unit normal mark-removal coefficient by its independent polynomial factor. `mathcal D` is the set of twenty diagonals. This is a declared polynomial lift of the audited differential, not a source identification of the entire PC/Rees complex. Its consecutive differentials still compose to zero.

The original `rho_c` remain chain maps, but their overlap discrepancy is no longer null-homotopic. An explicit global cycle is

\[
\Omega_w=
\sum_F(-1)^{|F|(|F|+1)/2}
\left(\prod_{a\notin F}w_a\right)[F,F],
\qquad d_w\Omega_w=0.
\]

In words: each fully marked face carries the product of weights for its missing diagonals. The radial and weighted-normal contributions cancel termwise.

Let `epsilon_cd` read the empty-cell coefficient of the overlap. Then

\[
\epsilon_{cd}m_{cd}(\Omega_w)
=(w_c-w_d)\prod_{a\notin\{c,d\}}w_a\ne0.
\]

In words: the two original restrictions disagree on a closed class. Since empty-cell evaluation is a chain map, the value would be zero for a null-homotopic discrepancy. Consequently **no polynomial-linear homotopy whatsoever** fills this fixed discrepancy in this independent-normal model. The obstruction is not restricted to the old contraction or the pair-local ansatz.

The conclusion persists after the substitution `w_a=t_a x_a` into the integral polynomial ring with the units `1+t_a x_a` inverted: the displayed polynomial remains nonzero. This statement does not replace the physical Gysin operation by that substitution.

### Two-Cut calculation

The minimal two-Cut block has degree-zero basis consisting of the empty cell, the two singly marked cells, and the doubly marked cell. With degree-one basis consisting of the two singly unmarked cells followed by the two mixed-pair cells, its matrix is

\[
d_0=
\begin{pmatrix}
1&w_c&0&0\\
1&0&w_d&0\\
0&-1&0&w_d\\
0&0&1&-w_c
\end{pmatrix},\qquad
m_0=(0,1,-1,0).
\]

In words: the original mismatch reads the difference of the singly marked coefficients. The vector `(-w_c w_d,w_d,w_c,1)` is a cycle and its mismatch is `w_d-w_c`. The global calculation above extends this obstruction to the entire octagon, without relying on a spectator quotient.

## 6. Polynomial repair with retained factors

Define

\[
\sigma_c=w_c\rho_c,
\qquad
\ell^w_{cd}[F,M]=w_s\ell^{\mathrm{pair}}_{cd}[F,M]
\]

on each mixed-pair input, and zero otherwise.

In words: retain the factor of the Cut removed by each extraction; the pair filler carries the factor of its marked Cut.

The polynomial identity is

\[
d_{E,w}\ell^w+\ell^w d_{I,w}
=P_{d,cd}\sigma_d-P_{c,cd}\sigma_c.
\]

In words: the factor-corrected maps admit an exact pair-local homotopy. All normal variables remain independent; none is divided out.

The two contributions from a doubly marked pair now have the same product `w_c w_d` with opposite signs. The other pair-state checks are the weighted versions of Section 3. The checker proves the equation on every generator using symbolic polynomial coefficients, not sampled values. It also checks all eight weighted chart maps and all dihedral actions, including permutation of normal parameters.

Give `w_c` multidegree `e_c` and `[F,M]` multidegree equal to the sum of `e_m` over its marked diagonals. Then `d_w`, `sigma_c`, and `ell_w` have multidegree zero. The original `rho_c` has degree `-e_c`; forgetting that degree is precisely what the unweighted comparison failed to retain in this test. Degree-zero maps preserve the induced multigraded Rees filtrations.

Setting every normal factor to one recovers the repaired unit-coefficient extension. That specialization is not an operation allowed without justification in the physical filtered problem. In the unlocalized polynomial lift, a degree-zero cocycle with empty-cell coefficient one would already require

\[
1+w_c b_c=0
\]

at every singleton unmarked Cut. In words: its singly marked coefficient would need an inverse of a nonunit normal factor. Thus the previous primitive normalization cannot simply be retained as the same coefficient condition in this lift. A source-defined Gysin/normal-line comparison is needed to state the physical normalized boundary problem correctly.

## 7. Verification and conclusion

Run the standalone standard-library program:

```sh
python check_source_admissible_overlap.py --output source_admissible_overlap_certificate.json
```

The completed run passes **756,370 exact assertions**. It reconstructs the signed cells, the old contraction and filler, the replacement, their higher comparison, all restriction equations, strict dihedral covariance, coefficient-localization inclusions, independent-normal polynomial differentials, weighted chart maps, the factor-corrected homotopy, and all twelve global obstruction evaluations. The certificate records the explicit old counterexamples.

The integer extension is repaired within a smaller, source-local class of maps. The literal independent-normal lift with unchanged restrictions is obstructed, and a factor-retaining polynomial comparison is supplied. Neither result identifies this comparison with the complete physical residue/Gysin functor or proves a normalized extension in that stronger category. The computed mismatch is a polynomial normal-parameter obstruction, not an ordinary prime-torsion class and not an RH criterion.

## Sources

Source repository paths at the pinned commit:

- `src/ledger/20260813-83 Fixed-Mark PC Descent and the Vanishing Loaded Octagonal Contact Class.md`: scalar fixed-mark facet support and its distinction from normal loading; blob `d28b849aca2f332495a546c6b83527f816bd210c`.
- `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`: independent `t_i x_i` normal factors and retained conormal symbols; blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`.
- `src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md`: normal Koszul factors, nonresonant localization, and source-versus-normal coefficient distinctions; blob `40504f31e8bbc9e984f97d5eef73b5cadf4bda95`.
- `research/voevodsky/check_n8_multirees_conductor_stalk_kernel.py`: coefficient exponents, allowed localizations, and conductor evaluation; blob `adc1f08b8882f15bef05bec59afe5e119b67512c`.
- `boundary_interior_extension.md` and its checker: the preceding integer construction and exact source sign conventions.
- Stacks Project, tag `0A8H`, Hom complexes: differential on comparison maps, including degree-minus-one and degree-minus-two signs. `https://stacks.math.columbia.edu/tag/0A8H`
- Stacks Project, tag `012K`, Spectral sequences: filtered complexes. `https://stacks.math.columbia.edu/tag/012K`
