# A normalization-pullback source and the obstruction to restoring both endpoints

Date: 2026-09-07  
Lane: Branch B — the fixed target, coefficient descent, and endpoint compatibility  
Pinned repository inputs: `andrey-kokoev/marici`, commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Results and scope

The preceding calculation produced twelve explicit Laurent-residue coordinates for a nontrivial generic-Q lifting torsor. Here those coordinates are realized by a pullback of the **actual alternating occurrence normalization**, rather than by freely adjoining a cell to kill their cocycle. Restoring both endpoint cubes supplies two additional coordinates. The resulting fourteen-coordinate source has an explicit, coefficient-linear map to the full 215-state target, with its genuine generic cycle and all endpoint coefficients retained.

This is a construction over the test open V from the preceding note. Its residue vector is selected by the already computed target transition chains. It is not an independent identification of the native scalar, logarithmic, or normalization-sheet physical source. The constructed comparison concerns the top-degree generic class, not a section of the entire seven-state Q complex or a replacement for the lower degrees of the physical source.

The new result beyond this realization is an exact endpoint-extension obstruction. The twelve-coordinate source cannot be lifted coefficient-linearly to the fourteen-coordinate source while fixing its generic and boundary maps. Its obstruction has annihilator

\[
I_++I_-+(t_p t_m:p\in S_+,\ m\in S_-).
\]

In words: occurrence tails and products of one normal from each polarity annihilate the new obstruction. Neither a single normal nor the identity does so. Nine explicit polynomial maps realize the nine normal-product annihilators. No parameter division, averaging, or new geometric carrier cell is used.

Its cyclic module is a second alternating normalization ring, now in the Rees coordinates. This is a computed repetition of a coefficient geometry, not a theorem that the full research object is an iterated or universal infinity-groupoid.

## 1. Fixed geometry and preceding inputs

Keep

\[
S_+=\{13,35,15\},\quad S_-=\{02,24,04\},\quad L=\{03,14,25\},
\]

\[
\mathcal C_0=\mathbb Z[X_l,u_l:l\in L],\qquad
\mathcal C=\mathcal C_0[t_s:s\in S_+\cup S_-],
\]

\[
\mathcal B=\mathcal C[X_s:s\in S_+\cup S_-]/(X_pX_m:p\in S_+,m\in S_-).
\]

In words: the occurrence sheets meet along their common conductor. The short normal factorization is u_s=t_s X_s. Long occurrence and normal variables are independent. Write

\[
I_+=(X_p:p\in S_+),\quad I_-=(X_m:m\in S_-),\quad
p=\prod_{S_+}t_s,\quad m=\prod_{S_-}t_s,\quad T=pm,\quad U_L=u_{03}u_{14}u_{25}.
\]

In words: p and m here are products, not primes or morphisms. Do not confuse occurrence ideals I with the normal ideals introduced in Section 7.

The open under consideration is

\[
V=D(T,pI_+,mI_-)\subset\operatorname{Spec}\mathcal B.
\]

In words: it is the complement of the full previously computed first-obstruction support. Its seven named principal opens are V_0=D(T), V_{+,s}=D(pX_s), and V_{-,s}=D(mX_s). They have 29 nonempty finite intersections. These inverses describe this mathematical open only; they are not newly admitted poles of the physical source.

The occurrence normalization restricts to finite maps

\[
\nu_\pm:V_\pm\longrightarrow V,\qquad
i:D\hookrightarrow V,\qquad D=\operatorname{Spec}\mathcal C[T^{-1}].
\]

In words: V_+ and V_- are the two inverse-image sheets, and D is their conductor on V. This is the three-occurrence-variable normalization on each sheet, not the different one-variable node used in the earlier local conductor-road comparison.

The actual target contains the support sequence and endpoint quotient

\[
0\longrightarrow F_B\longrightarrow F_K\longrightarrow Q\longrightarrow0,
\qquad E=F_K/F_V,\qquad A_\partial=F_B/F_V.
\]

In words: F_V consists of the two genuine endpoint cubes. F_K has 215 loaded states, Q has seven, and all target complexes are bounded above by homological degree three. There are no hidden degree-four target boundaries.

The preceding work [P1] proves the top kernel and twelve-family ambiguity after the endpoint quotient. The new checker repeats the full top-kernel computation with both endpoints present in all 960 occurrence/normal support grades used in that proof.

## 2. The two endpoint families must be added to the twelve boundary families

For an active sheet sigma and a nonempty subset N of its opposite sheet, define

\[
P_N=\{s\in S_\sigma:s\text{ is noncrossing with every }n\in N\},\qquad
L_N=\{l\in L:l\text{ is noncrossing with every }n\in N\}.
\]

In words: these are compatible diagonal sets in the actual hexagon. They are not an unlabelled Boolean replacement.

The full top chain is

\[
\Gamma_{\sigma,N}=
\sum_{N\subseteq F\subseteq N\cup P_N\cup L_N}
(-1)^{|F|(|F|+1)/2}
\left(\prod_{s\in P_N\setminus F}t_s\right)
\left(\prod_{l\in F\cap L}X_l\right)
\left(\prod_{l\in L_N\setminus F}u_l\right)[F,F],
\]

where only noncrossing F occur. In words: keep the signed, fully marked target faces with their actual coefficients. Unlike the preceding twelve-family formula, this one does not omit the endpoint faces.

If N is a proper subset, this recovers an old family. If N is the whole opposite sheet, the formula is its single fully marked endpoint. Consequently, on V,

\[
\mathcal M_{14}:=H_3(F_B)|_V
\cong\bigoplus_{\varnothing\ne N\subseteq S_-}\mathcal I_+\Gamma_{+,N}
\oplus\bigoplus_{\varnothing\ne N\subseteq S_+}\mathcal I_-\Gamma_{-,N},
\]

\[
\mathcal M_{14}=\mathcal M_{12}\oplus\mathcal N_{\rm end},\qquad
\mathcal N_{\rm end}=H_3(F_V)|_V
=\mathcal I_+\Gamma_{+,S_-}\oplus\mathcal I_-\Gamma_{-,S_+}.
\]

In words: there are seven ideal-valued families on each sheet, with the two new ones precisely the endpoint kernels. These are not fourteen free copies of the coefficient ring. The notation \(\mathcal I_\sigma\) denotes the ideal sheaf supported on its normalization sheet.

**Proof of the endpoint terms.** In an endpoint top state the three outgoing absolute coefficients are t_s X_s. Their common annihilator is the opposite occurrence ideal. In the PC version the outgoing maps are localizations at those products; their kernels are the same opposite ideal. There is no degree four. Thus each endpoint contributes exactly the asserted ideal. Proper-subset Gamma chains already avoid endpoint faces, and multiplying by their active ideal kills every outgoing opposite-sheet term, including terms entering an endpoint. They are genuine full cycles. Combining this with the preceding complete twelve-family theorem proves the displayed decomposition. The independent integral fine-degree checks verify this directly.

## 3. Fourteen normalization residues

The seven closed local lifts from [P1] were already constructed before quotienting F_V. Their differences satisfy

\[
\ell_j-\ell_i=c_{ij},\qquad dc_{ij}=0,\qquad
c_{jk}-c_{ik}+c_{ij}=0.
\]

In words: these are differences of actual full target cycles. On a common-to-positive chart the coefficients in the Gamma basis are minus

\[
r_{+,N}=
\frac{\prod_{l\in L\setminus L_N}u_l}
{\left(\prod_{n\in N}t_n\right)\left(\prod_{a\in P_N}t_a\right)},
\]

and the negative formula is its polarity conjugate. In words: every r is a regular section of the conductor D, where T is invertible. It need not extend to its normalization sheet.

The twelve proper-subset values are unchanged. The new endpoint values are

\[
r_{+,S_-}=\frac{U_L}{t_{02}t_{04}t_{24}}=\frac{U_L}{m},\qquad
r_{-,S_+}=\frac{U_L}{t_{13}t_{15}t_{35}}=\frac{U_L}{p}.
\]

In words: the opposite endpoint carries the full opposite-sheet triple pole. Both were present as endpoint discrepancies in the previous computation; here they are included as coordinates of a single full comparison.

The checker verifies the complete fourteen-coordinate overlap equality, the triple-overlap identities, and dihedral covariance on the actual absolute and PC differentials. The old twelve-coordinate equality is recovered by the literal endpoint quotient.

## 4. Construct a normalization-provenanced coefficient source

The actual normalization ideal sequences on V are

\[
0\longrightarrow\mathcal I_\sigma
\longrightarrow\nu_{\sigma*}\mathcal O_{V_\sigma}
\xrightarrow{\epsilon_\sigma}i_*\mathcal O_D\longrightarrow0.
\]

In words: retain a branch function, its conductor value, and the ideal of functions with zero value. These maps are supplied by the normalization, not chosen after computing a matrix rank.

For q=12 or 14 let Lambda_q be the corresponding set of labelled channels and put

\[
\mathcal L_q=\bigoplus_{(\sigma,N)\in\Lambda_q}\nu_{\sigma*}\mathcal O_{V_\sigma}\,\Gamma_{\sigma,N},
\qquad
\mathcal D_q=\bigoplus_{(\sigma,N)\in\Lambda_q}i_*\mathcal O_D\,\Gamma_{\sigma,N}.
\]

In words: these are normalization functions and conductor values with every grading label retained. Evaluation gives a surjection \(\epsilon_q:\mathcal L_q\to\mathcal D_q\) with kernel \(\mathcal M_q\).

The residue vector defines an O_V-linear map

\[
r_q:\mathcal O_V\longrightarrow\mathcal D_q,
\qquad a\longmapsto (a|_D\,r_{\sigma,N})_{(\sigma,N)}.
\]

In words: multiply the fixed conductor residue vector by the coefficient restricted to the conductor. Occurrence tails act by zero on its target; they are not evaluated at illegal localized values.

Define the source by the actual sheaf pullback

\[
\mathcal S_q=
\mathcal O_V\times_{\mathcal D_q}\mathcal L_q
=\{(a,z):\epsilon_q(z)=r_q(a)\}.
\]

In words: an input contains a generic coefficient and normalization functions whose conductor values match all its required residues. This is a coherent sheaf. Because evaluation is surjective, it also computes the derived pullback without additional cohomology. The standard extension/pullback construction is [M1, M2].

It has the exact sequence

\[
0\longrightarrow\mathcal M_q\longrightarrow\mathcal S_q
\xrightarrow{\rho_q}\mathcal O_V\longrightarrow0.
\]

In words: the source carries the nontrivial connecting boundary rather than asking that boundary to vanish. The extension class is precisely the connecting image of r_q. Its residue vector is target-selected input; the normalization operation itself is geometric.

### Explicit local comparison, not only an abstract Ext classification

On V_0 lift r_q to the same Laurent polynomials in the normalization and call that lift b_0. On an occurrence chart the conductor is empty, so choose b_i=0. A local element is written as (a,m_i), with normalization coordinates a b_i+m_i. The overlap transition is

\[
m_j=m_i-a(b_j-b_i),\qquad
(b_j-b_i)\Gamma=c_{ij}.
\]

In words: the normalization gluing is exactly the previously computed target cocycle, with its sign fixed by the cover order.

Set

\[
\Phi_{14,i}(a,m_i)=a\ell_i+\sum_{\Lambda_{14}}(m_i)_{\sigma,N}\Gamma_{\sigma,N}.
\]

In words: combine the actual local generic lift with its allowed ideal-valued correction. Every summand is a closed full target chain. The overlap equations imply equality of these formulas on intersections, not merely equality on homology.

Thus

\[
\Phi_{14}:\mathcal S_{14}[3]\longrightarrow F_K|_V,
\qquad
\pi\Phi_{14}(a,z)=a\theta.
\]

In words: this is a global coefficient-linear chain map with the genuine nonzero generic-Q cycle. Homological degree three is indicated by [3]. It retains both endpoint cubes, and applying their quotient gives the corresponding map \(\Phi_{12}:\mathcal S_{12}[3]\to E|_V\).

On every chart the source has the same top kernel and unit lift as the target. Hence

\[
\mathcal S_{14}\cong H_3(F_K)|_V,\qquad
\mathcal S_{12}\cong H_3(E)|_V.
\]

In words: this geometrically describes the top lifting sheaves. It does not identify the whole target with its top homology or discard lower target degrees.

The exact sequence for S_14 and the support sequence for F_K form a commutative diagram, with the bottom generic map a to a theta. Consequently their connecting morphisms agree in the derived category. This is the constructed boundary-carrying comparison. It does not produce a global element of S_14 whose coefficient is one: the non-split source still has the previously proved nonzero unit torsor.

## 5. A new lifting question: restore endpoints for the entire twelve-coordinate source

Forgetting the last two normalization coordinates gives

\[
0\longrightarrow\mathcal N_{\rm end}
\longrightarrow\mathcal S_{14}
\xrightarrow{q}\mathcal S_{12}\longrightarrow0,
\qquad
\varepsilon_{\rm end}\in\operatorname{Ext}^1_{\mathcal O_V}(\mathcal S_{12},\mathcal N_{\rm end}).
\]

In words: this extension tests whether the complete twelve-coordinate source comparison can be lifted through the full endpoint-preserving target. It is not the older question of lifting a single coefficient to E.

Let e_12 be the old extension of O_V by M_12, and let e_end be the extension of O_V by N_end given by the two endpoint fractions. Then epsilon_end is the pullback of e_end along rho_12. The long exact Ext sequence gives

\[
\operatorname{Hom}(\mathcal M_{12},\mathcal N_{\rm end})
\longrightarrow H^1(V,\mathcal N_{\rm end})
\longrightarrow\operatorname{Ext}^1(\mathcal S_{12},\mathcal N_{\rm end}).
\]

In words: endpoint data can be removed from this lifting problem only when they are the pushout of the old twelve-channel cocycle under an allowed sheaf-linear map. This permits every such correction, not merely a preferred choice.

## 6. Compute all allowed corrections and detect the missing triple poles

There are no cross-polarity maps between the two ideal sheaves, and

\[
\mathcal Hom(\mathcal I_+,\mathcal I_+)\cong\nu_{+*}\mathcal O_{V_+},
\qquad
\mathcal Hom(\mathcal I_-,\mathcal I_-)\cong\nu_{-*}\mathcal O_{V_-}.
\]

In words: every endomorphism is multiplication by a function on the relevant normalization sheet. These facts do not assume that I is a free line.

**Proof.** On the positive polynomial sheet the ideal is generated by three independent occurrence coordinates and has rank one. An endomorphism is multiplication by an element of the fraction field. Every height-one localization sees the ideal as the unit ideal; normality of the polynomial sheet forces that element to be regular. The argument commutes with the chart localizations. A map from the negative ideal to the positive one is zero because the positive occurrence coordinates annihilate its source and are non-zero-divisors on its target. The other cases follow by polarity.

The preceding normalizations give global coefficient rings B_+[p^{-1}] and B_-[m^{-1}]. Their action on first cohomology factors through conductor constants

\[
\mathcal C_+=\mathcal C[p^{-1}],\qquad
\mathcal C_-=\mathcal C[m^{-1}],\qquad
\mathcal C_T=\mathcal C[T^{-1}].
\]

In words: a correction on one sheet cannot introduce a new opposite-sheet normal pole. The relevant endpoint-cohomology coordinates are C_T/C_+ and C_T/C_-.

For the positive endpoint define the further quotient

\[
\mathcal P_+=
\frac{\mathcal C_T}
{\displaystyle\sum_{a\in S_-}\mathcal C_+\left[\left(\prod_{b\in S_-\setminus\{a\}}t_b\right)^{-1}\right]}
\cong H^3_{(t_{02},t_{04},t_{24})}(\mathcal C_+).
\]

In words: discard every fraction missing at least one of the three opposite normal poles. This is the explicit top term of the three-variable local-cohomology Čech complex [M3]. It is a detector of the endpoint extension; no isomorphism between the entire Ext group and this local-cohomology module is asserted.

Every proper-subset residue r_{+,N} maps to zero in P_+. Multiplying such a residue by any allowable coefficient in C_+ cannot introduce its missing opposite pole. However,

\[
\left[\frac{U_L}{t_{02}t_{04}t_{24}}\right]\ne0\quad\text{in }\mathcal P_+.
\]

In words: the endpoint has all three poles, with independent nonzero long-normal numerator. The polarity-conjugate detector is equally nonzero. Therefore epsilon_end is nonzero, and there is no sheaf-linear section of q. A derived lift of the fixed map from S_12[3] would induce such a section on top homology, so higher homotopies in the unchanged comparison problem cannot supply it.

This is different from claiming every individual global section is unliftable. Its coefficient is already in the old global lifting image, and those coefficients annihilate the two raw endpoint residue classes. Individual global sections can be lifted. What fails is one sheaf-linear choice for the entire source.

### First-pole meaning

The distinguished triple-pole class is annihilated by each of its three normal coordinates. Its first-pole, ordered-conormal evaluation is

\[
\operatorname{res}_{02,04,24}
\left(\frac{U_L\,dt_{02}\wedge dt_{04}\wedge dt_{24}}
{t_{02}t_{04}t_{24}}\right)=U_L,
\]

with the reflected expression on the other sheet. In words: after the supported first-pole quotient and its determinant line are retained, the coefficient is the actual long-normal product, not an artificially normalized scalar one. This is the elementary Koszul/generalized-fraction identification on the first-pole submodule. It is not a C-linear scalar trace on arbitrary Laurent functions, nor a constructed physical Gysin map. Permuting the normal order permutes the determinant orientation.

## 7. Exact annihilator and nine explicit lifted maps

Write

\[
\mathfrak n_+=(t_{13},t_{15},t_{35}),\qquad
\mathfrak n_-=(t_{02},t_{04},t_{24})\subset\mathcal C.
\]

In words: these are ideals of normal parameters, not the occurrence ideals I_+ and I_-.

Multiplying the positive endpoint fraction by any one negative parameter turns it into a known double-pole coordinate. For example,

\[
t_{02}r_{+,S_-}=u_{14}r_{+,\{04,24\}},\qquad
t_{13}r_{-,S_+}=u_{25}r_{-,\{15,35\}}.
\]

In words: these are exact identities of conductor fractions, with no division or change of source module. All six analogous identities are checked.

For each p_0 in S_+ and m_0 in S_-, put f=t_{p_0}t_{m_0}. Define the map

\[
F_f:\mathcal S_{12}\longrightarrow\mathcal S_{14}
\]

by multiplying its generic coefficient and twelve old normalization coordinates by f and setting the two new normalization coordinates to

\[
z'_{+,S_-}=t_{p_0}u_{\lambda(m_0)}z_{+,S_-\setminus\{m_0\}},
\qquad
z'_{-,S_+}=t_{m_0}u_{\lambda(p_0)}z_{-,S_+\setminus\{p_0\}}.
\]

In words: use the existing opposite double-subset coordinate and its missing long-normal factor. The dictionary is

\[
\lambda(02)=\lambda(35)=14,\quad
\lambda(04)=\lambda(13)=25,\quad
\lambda(24)=\lambda(15)=03.
\]

In words: these labels come from the actual noncrossing diagram and the residues already computed.

The conductor identities verify directly

\[
qF_f=f\,\operatorname{id}_{\mathcal S_{12}}.
\]

In words: all nine normal-product multiples of the fixed source comparison admit actual endpoint-preserving lifts. The formulas commute with all cover transitions. The checker verifies their values in the full target, not just in the two scalar residue groups.

For an occurrence f in I_++I_-, set both new normalization coordinates to zero and multiply the old data by f. This is valid because f restricts to zero on the conductor. In local split coordinates the necessary endpoint correction is minus f times the local conductor lift b_i; it is not obtained by pretending f times a Laurent fraction is a globally regular scalar.

These constructions prove sufficiency. For necessity, the positive first-pole detector shows that a spectator polynomial killing epsilon_end must belong to n_-; the negative one requires n_+. Distinct monomials cannot cancel, and the independent factor U_L is a non-zero-divisor. Since the two normal-variable sets are disjoint,

\[
\mathfrak n_+\cap\mathfrak n_-=\mathfrak n_+\mathfrak n_-.
\]

In words: a surviving common-conductor coefficient must contain at least one parameter from each polarity. Together with the explicit corrections, this proves

\[
\operatorname{Ann}_{\mathcal B}(\varepsilon_{\rm end})
=I_++I_-+\mathfrak n_+\mathfrak n_-,
\qquad
\mathcal B\varepsilon_{\rm end}\cong\mathcal C/(\mathfrak n_+\mathfrak n_-).
\]

In words: the annihilator has nine minimal normal-product generators, besides the occurrence ideals. It is not the preceding six-factor principal ideal (T). Extending the scalar action to the actual global-section ring replaces I_+ and I_- by their previously allowed branch-localized ideals and gives the same spectator quotient.

## 8. A second alternating conductor appears in the normal variables

The new cyclic module has the canonical coefficient-ring presentation

\[
\mathcal C/(\mathfrak n_+\mathfrak n_-)
\cong
\mathcal C_0[t_{13},t_{15},t_{35}]
\times_{\mathcal C_0}
\mathcal C_0[t_{02},t_{04},t_{24}].
\]

In words: its coefficients consist of two normal-polynomial branches with a common constant term. Every monomial involving normal variables from both branches vanishes; every monomial contained in one branch survives. The 64 possible normal-support patterns verify the finite combinatorial classification; the normal-form argument proves it in all degrees.

The original alternating geometry involved occurrences X. The endpoint-restoration obstruction has the same fibre-product form in the Rees variables t. This repetition is derived from the endpoint comparison and its allowed corrections. It is not imposed by relabelling levels of an infinity-groupoid.

The module has infinite additive order and remains nonzero after tensoring with the rationals. This is a coefficient/supported obstruction, not integer-prime torsion.

## 9. Consequences and exclusions

What is now constructed is a normalization-based, boundary-carrying source over the actual coefficient open, its strict local-to-global map into the fixed target, and the exact obstruction to removing its two endpoint coordinates. The generic map is the genuine theta class in the honest seven-state quotient.

What is not constructed is an independent map from the native scalar or logarithmic source into S_14, a physical identification of V with a generic deformation, or the two spatial endpoint connector cells required by the complete six-functor correspondence. The source here is selected by the target residue vector. It is a concrete comparison target for the native-source work, not a replacement for that provenance.

The two-endpoint obstruction does not say that the normal first-pole residue should vanish. A supported-dual physical operation may transport that nonzero residue into its proper degree and determinant line. The calculation specifies the exact two triple-pole classes such an operation must match. Discarding the endpoint coordinates or checking only the twelve proper-subset residues misses them.

## 10. Reproduction and verification

Run:

```sh
python check_marici_normalization_endpoint_extension_20260907.py \
  --output marici_normalization_endpoint_extension_certificate_20260907.json
```

The standalone standard-library checker performs 120,909 exact assertions. It reconstructs all 215 target states; the fourteen full top-cycle families; the seven full local lifts and all 29 nonempty cover terms; actual gluing maps and generic projection; both endpoint differences; the nine polynomial source maps and occurrence corrections; all six dihedral coefficient actions; two new integral endpoint Čech calculations; 729 normal-power reductions; and 960 independent integral full-endpoint top-kernel calculations. It does not use floating-point rank tests.

The preceding `check_marici_obstruction_complement_descent_20260907.py` was independently rerun and passed 78,779 assertions. The new checker records its hash when that file is present but does not require or automatically execute it. Its own mathematical kernels and coefficient routines are embedded.

The exact-annihilator proof uses the sheaf Hom calculation, first-pole detector, and explicit correction maps above. Finite assertion counts do not replace these proofs or constitute proof-assistant certification. No repository files were modified.

## References

[P1] `marici_obstruction_complement_descent_20260907.md` and its standalone checker: the test open, twelve labelled residues, seven local full chains, top module before endpoint restoration, and normalization cohomology. Both files are present in the current computation environment.

[P2] `marici_q_graded_lift_naturality_20260907.md` and `marici_filtered_q_alternating_rees_update_20260907.md`: original lifting ideal, complete top-kernel decomposition, and coefficient-linearity obstruction over the alternating ring.

[P3] Source model embedded by the preceding work: `research/voevodsky/check_ringed_alexandrov_pc_target.py`, Git blob `7c993d05837fbe2ba29ba30e5b665b5429ab940b`, and the Entry-143 support sequence at the pinned commit. They fix the actual differential, allowed coefficient localizations, support quotient, and endpoints. No current-repository re-audit is claimed in this note.

[M1] Stacks Project, Section 12.6, Extensions, tag `010I`: `https://stacks.math.columbia.edu/tag/010I`.

[M2] Stacks Project, Section 20.5, First cohomology and extensions, tag `0B39`: `https://stacks.math.columbia.edu/tag/0B39`.

[M3] Stacks Project, Section 47.9, Local cohomology, tag `0952`: `https://stacks.math.columbia.edu/tag/0952`.
