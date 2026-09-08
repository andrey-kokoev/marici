# Boundary-to-interior extension of the explicit octagon coefficient models

Date: 2026-09-06  
Repository input: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Results and scope

For the signed primitive-coefficient model, the full octagon has 12,425 loaded generators. Its previously computed boundary is the 10,100-generator chart/overlap totalization. An explicit marked-normal extraction on each Cut, together with integral overlap homotopies, defines a map from the full complex to that boundary. The normalized primitive boundary cocycle extends, and its extension space is contractible. The relative stable complex nevertheless has five free classes in cohomological degree two.

For the separate polynomial-localization model, restriction from the full index to the boundary induces an isomorphism on degree-zero coefficients. Every fixed branch-polynomial boundary marking extends uniquely up to homotopy. Positive-degree branch terms remain distinct in the interior. The supportwise relative cohomology is free over the integers and lies in degrees two through five.

These statements concern the explicit coefficient models already constructed. They do not identify the new cellular comparison with a complete analytic period, nearby-cycle, support-PC, or physical relative comparison. In particular, a normalized coefficient extension is not a reconstruction of the eight-point amplitude. The polynomial diagram uses localization inclusions; the primitive cellular diagram uses the signed differentials and coordinate projections specified below. These two diagrams are not identified.

## 1. Source and comparison being constructed

The full signed convention is taken from `research/voevodsky/check_n8_cut_normal_mapping_cone.py`, blob `14f1a7bdd09de6c462d927334f7407d84401e3e5`, with dimension five. The loaded faces are those of `check_n8_loaded_octagon_carrier.py`, blob `50d8540992ed301cf7d222ca68a4304e293ce222`. The boundary link-chart convention is `check_n8_full_twisted_cut_cech_lift.py`, blob `de9502d39bb9501a6b2595ab858b4485c55cad7c`, with normal-sign parameter four, also on its overlaps.

An interior loaded cell is `(F,M)`, where F is any noncrossing face among all twenty octagon diagonals and M is a subset of F. The full cohomological complex I has degree

\[
q(F,M)=|F|-|M|.
\]

In words: degree counts the unmarked diagonals. Its ranks in degrees zero through five are 903, 3140, 4320, 2940, 990, 132.

Its differential is

\[
d[F,M]=\sum_a(-1)^{\#\{c\in F:c<a\}}[F\cup\{a\},M]
 +\sum_{b\in M}(-1)^{5-|F|+\operatorname{pos}_M(b)}[F,M\setminus\{b\}].
\]

In words: add a compatible diagonal or remove an existing mark, with the full source signs. Positions start at zero. The coefficient calculation does not discard the marked-normal generators.

The boundary B is the previously constructed totalization of eight link-chart complexes and twelve overlap complexes. It has ranks 1080, 3276, 3648, 1776, 320 in degrees zero through four. Its differential is

\[
D(v,e)=(dv,\Delta v-de).
\]

In words: compare the two chart restrictions on each overlap; overlaps contribute one additional cohomological degree. These coordinate-projection maps are not localization inverses. The 10,100 boundary generators count chart occurrences and overlaps, not the 7,100 objects of the different boundary index used for the polynomial diagram.

## 2. Interior contraction and normalized cocycle

Define

\[
\omega_I=\sum_F(-1)^{|F|(|F|+1)/2}[F,F].
\]

In words: sum every fully marked face with the displayed orientation. Empty-cell coefficient is one. Exact calculation gives d omega-I equal to zero.

For a nonempty F let b be its least diagonal. Set

\[
h_0[F,M]=
\begin{cases}
(-1)^{5-|F|}[F,M\cup\{b\}],&b\notin M,\\
0,&b\in M.
\end{cases}
\qquad h_0[\varnothing,\varnothing]=0.
\]

In words: restore the least missing mark. This contracts the normal differential on every nonempty fixed-face block. If a denotes the radial differential, put

\[
H=\sum_{j\ge0}(-h_0a)^j h_0.
\]

In words: correct that normal contraction by the radial differential. Every correction increases face size, so the sum terminates integrally.

With epsilon the empty-cell coefficient and i(1)=omega-I,

\[
dH+Hd=1-i\epsilon,\qquad Hi=0,\qquad H^2=0,\qquad \epsilon i=1.
\]

In words: this is a deformation retraction of the entire signed complex onto one integral unit. The checker verifies these identities on every full generator. Equivalently, conjugating the earlier dimension-four contraction by the sign `(-1)^|M|` gives this dimension-five contraction. Therefore

\[
H^0(I)=\mathbb Z,\qquad H^q(I)=0\quad(q\ne0).
\]

In words: only the normalized primitive coefficient survives in the interior model.

## 3. Marked-normal extraction and actual overlap homotopies

For a physical Cut c define rho-c on a full generator to be zero unless c is marked. If c is marked, write F'=F minus c and M'=M minus c, and set

\[
\rho_c[F,M]=
-(-1)^{\#\{a\in F':a>c\}+\#\{a\in M':a>c\}}[F',M'].
\]

In words: extract the marked Cut normal, remove its label, and retain its induced orientation in the link-chart complex. The overall minus sign normalizes its primitive coefficient to plus one.

Every resulting face lies in the Cut link. A differential cannot introduce a previously absent marked Cut; removing that mark leaves the extraction support and contributes zero. On retained arrows, the displayed permutation sign accounts for both radial and normal incidences. Consequently

\[
d\rho_c=\rho_cd,\qquad \rho_c(\omega_I)=\omega_c.
\]

In words: all eight extractions are chain maps, and they send the interior unit to the previously computed boundary-chart unit. Both equations were verified on the full generator sets.

The chart maps do not strictly agree on overlaps. With rho the tuple of the eight maps, let

\[
m=\Delta\rho,\qquad \ell=mH.
\]

In words: m is their overlap discrepancy. Apply it after the existing interior contraction to construct the comparison homotopy. No generator is adjoined.

Since m is a chain map and m(omega-I)=0,

\[
d_E\ell+\ell d=m.
\]

In words: the boundary of the comparison homotopy is exactly the difference of the two restrictions. Define

\[
\Phi:I\longrightarrow B,\qquad \Phi(a)=(\rho(a),\ell(a)).
\]

In words: retain both chart values and the overlap homotopies. The totalization sign gives

\[
D\Phi=\Phi d,\qquad
\Phi(\omega_I)=(\omega_c)_c\oplus0=\omega_\partial.
\]

In words: this is an actual chain-level extension map, and the interior cocycle has exactly the prescribed primitive boundary value.

The discrepancy m has 1,960 nonzero columns, and ell has 1,369 nonzero columns. Thus the construction does not silently assume strict overlap agreement. The checker verifies all overlap equations and the total chain-map equation on all 12,425 interior generators.

This extraction-plus-homotopy map is constructed here for the explicit cellular coefficient model. The source defines the relevant loaded generators and signs, but its full physical residue functor on arbitrary coefficients is not identified by this calculation.

## 4. Relative complex and extension space

The full interior retraction and the earlier boundary retraction reduce the comparison to

\[
\mathbb Z[0]\longrightarrow
[\mathbb Z^8\xrightarrow{\delta}\mathbb Z^{12}],
\qquad 1\longmapsto(1,\ldots,1).
\]

In words: the unit extends to the same coefficient on every boundary chart. The map Phi is homotopic to the primitive comparison because

\[
D(\Phi H)+(\Phi H)d=\Phi-\omega_\partial\epsilon.
\]

In words: the discrepancy from the primitive comparison has the displayed integral homotopy.

The relative object F is the homotopy fibre of Phi, with the cohomological cone convention [M1]. It reduces to

\[
F\simeq[\mathbb Z\xrightarrow{\mathrm{diag}}\mathbb Z^8
\xrightarrow{-\delta}\mathbb Z^{12}],
\]

in degrees zero, one, two. In words: retain the interior unit, boundary-chart coefficients, and overlap coefficients, including the map between them.

The overlap graph is connected and has twelve edges and eight vertices. Its incidence matrix has seven unit Smith factors. Thus

\[
H^2(F)=\mathbb Z^5,\qquad H^q(F)=0\quad(q\ne2).
\]

In words: the relative stable object retains five free classes in degree two and no torsion. A spanning-tree reduction gives integral, primitive coordinates for all five classes.

The connecting map is

\[
H^1(B)\xrightarrow{\ \sim\ }H^2(F).
\]

In words: none of the five nonzero degree-one boundary directions extends as a degree-one interior class. They are not ambiguities of the degree-zero unit extension.

For the fixed boundary marking define

\[
\mathcal E=\operatorname{hofib}_{\omega_\partial}
\left(\operatorname{Map}_{D(\mathbb Z)}(\mathbb Z,I)
\longrightarrow\operatorname{Map}_{D(\mathbb Z)}(\mathbb Z,B)\right).
\]

In words: objects are interior markings together with a comparison to the fixed boundary marking. Higher paths compare those extension data.

Both unshifted mapping spaces are discrete copies of the integers, and the induced map is the identity. Higher paths detect negative cohomological degrees [M2]. Hence

\[
\mathcal E\simeq *.
\]

In words: the primitive boundary extends uniquely up to homotopy, with no higher ambiguity. This does not say F is acyclic: its nonzero degree-two cohomology lies outside the unshifted marking-space calculation.

## 5. Full polynomial-localization extension

For this separate calculation use the earlier full loaded poset J and its physical-facet union J-U. The coefficient objects are the localized scalar ring R-L, node ring A-L, or normalization N-L, with their localization inclusions. Restriction from J to J-U is canonical. No marked-normal extraction is substituted for this inclusion of indices.

For each Laurent monomial, let N be its noncrossing negative support and k its size. The full-index monomial diagram is the constant integer diagram on the forward-closed locus where all N coordinates are unmarked, extended by zero elsewhere.

Its derived sections are relative cochains of the index nerve and the complementary locus. Retaining only the absent/marked/unmarked states of the k coordinates gives a product of k intervals relative to its boundary. The previously constructed mark-forgetting zigzag preserves the complementary locus. Therefore, per monomial and coefficient mode,

\[
H^q(T_{J,N})=
\begin{cases}\mathbb Z,&q=k,\\0,&q\ne k.\end{cases}
\]

In words: every negative coordinate contributes one degree, without deleting it from the object.

The preceding boundary theorem computes H-q of T-U-N. To compute the restriction, let V-N be the physical Cuts compatible with N and I-N the physical Cuts in N. If V-N minus I-N is nonempty, choose a Cut there. Restricting to that patch leaves all k relative interval directions, giving an isomorphism in degree k. Thus the global restriction into boundary cohomology in that degree is a split injection of one primitive integral class. If V-N minus I-N is empty, the boundary has no degree-k cohomology and that restriction is zero. This suffices to determine all relative ranks and torsion; arbitrary cochain homotopies are not being inferred from equality of scalar ranks.

Writing b-q for the boundary cohomology ranks for this support, in the first case the only possible relative ranks are

\[
\operatorname{rank}H^k(F_N)=b_{k-1},\quad
\operatorname{rank}H^{k+1}(F_N)=b_k-1,\quad
\operatorname{rank}H^{k+2}(F_N)=b_{k+1}.
\]

In words: remove the one primitively extending interior class from the boundary degree-k group and apply the long exact sequence. In the second case the sole possible group is

\[
H^k(F_N)\cong\mathbb Z^{1+b_{k-1}}.
\]

In words: retain the full interior class together with the shifted lower boundary classes. These integral extensions split as abelian groups because the quotients are free; no module-linear splitting is asserted.

All 903 noncrossing supports are computed in the certificate. There are 525 primitive-injection cases and 378 zero-target cases. Every nonzero relative group lies in degrees two through five. The aggregate ranks 85, 468, 878, 560 count one monomial and one coefficient mode per support, not the infinite rank of the full polynomial object. No ordinary integral torsion occurs.

In particular, for node coefficients the degree-zero restriction is

\[
R_0\oplus xR_0[x]\oplus yR_0[y]
\xrightarrow{\ \cong\ }
R_0\oplus xR_0[x]\oplus yR_0[y].
\]

In words: it preserves every unlocalized node polynomial. Each conductor-normalized boundary pair

\[
(1+xa(x),\ 1+yb(y))
\]

extends as the same pair across the full diagram. In words: there is no new freedom after a boundary pair is fixed, but different boundary pairs remain different interior markings. The extension space of each fixed pair is contractible. The same degree-zero conclusion applies to the degree-corrected, orientation-compensated supported scalar model.

The adjunction/normalization sequence of the earlier conductor-supported comparison is natural on all J, so it restricts to the corresponding boundary sequence. This does not provide the still-missing identification with the complete physical endpoint-relative functor.

## 6. Verification

Run `python check_boundary_interior_extension.py --output boundary_interior_extension_certificate.json`.

The self-contained standard-library checker passes 292,493 exact assertions. It reconstructs the interior and boundary signed complexes; verifies both integral contractions; checks all eight marked-normal maps, their overlap homotopies, the total restriction, and its homotopy to the primitive map; verifies primitive integral graph reduction; and computes all 903 polynomial-support relative groups. Arbitrary polynomial exponents are covered by the support proof, not by extrapolating finite exponent checks. This is not proof-assistant verification.

No files were written back to the repository.

## References

[M1] Stacks Project, *Cones and termwise split sequences*, tag `014D`: `https://stacks.math.columbia.edu/tag/014D`.

[M2] Stacks Project, *Hom complexes*, tag `0A8H`: `https://stacks.math.columbia.edu/tag/0A8H`.

Preceding conversation artifacts: `coefficient_marked_boundary.md`, `check_coefficient_marked_boundary.py`, `conductor_supported_comparison.md`, and `marici_eight_point_boundary_groupoid.md`. Their differing coefficient categories and source qualifications remain in force.
