# A supported Rees-branch residue trace and the independent excess channel

Date: 2026-09-07  
Project: Marici, Branch B  
Pinned repository input: `andrey-kokoev/marici` at `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and scope

The failed adjugate return was not merely an unfortunate choice of matrix. **Every degree-zero derived polynomial return from the selected repeated-normal source to the raw source kills the selected excess on the central Rees fibre.** This follows from an exact annihilator calculation, not an enumeration of candidate maps.

There is, however, a different source-defined operation: the inclusion-of-support map from the selected scalar branch to the product-Rees zero locus, composed with the ordered Koszul-to-Cech residue. Its complete Cech matrix is explicit. On the central Rees face it does not become the zero derived morphism: it becomes the primitive codimension-three Gysin extension. The independent excess factor is carried identically in this *shifted residue channel*. It is not replaced by a normal multiplier.

The distinction is essential. The central map does not send the degree-one source excess to a nonzero degree-one target homology class. It retains a nonzero Ext/Gysin morphism, including the corresponding excess-labelled channel. The checker explicitly tests this distinction.

Tensoring this supported trace with the preceding, actual finite-grade reverse support pairing gives a primitive Gysin-valued reverse pairing on the nine-term obstruction. It does not turn that obstruction into a covariant filler.

This constructs a genuine affine normal-support operation and its endpoint **normal factors**. It does not identify the operation with the full spatial normalized-log/supported-Verdier correspondence. In particular, the two coupled spatial endpoint connector 2-cells and the physical reflection parity are not constructed here.

## 2. The declared normal chart and its actual repeated-normal source

Use the ordered branch indices `1,3,5`. Over the polynomial coefficient chart put

\[
 A=B[t_1,t_3,t_5,x_1,x_3,x_5,u_0],\qquad u_i=t_ix_i\quad(i=1,3,5).
\]

In words: `B` carries the independent spectator coefficients. The displayed `x_i` are the scalar branch-section coordinates in the declared product-Rees change. This normal calculation does not identify them with a physical channel coordinate, or silently specialize the target occurrence factors. The source monodromy units `1+t_i x_i` can also be inverted: the constructions below extend by that coefficient localization.

All support and Ext claims below use this declared chart. Any further geometric identification between its coordinates and another coefficient presentation must be supplied separately.

The raw and selected sources are

\[
 D_u=K_A(t_1x_1,t_3x_3,t_5x_5,u_0,t_3x_3),
\]
\[
 D_x=K_A(x_1,x_3,x_5,u_0,t_3x_3).
\]

In words: select the first three branch equations; leave the opposite pair's repeated equation unchanged. Both complexes retain all 32 exterior generators.

Their excess cycles are

\[
 \eta_u=h_3^+-h_3^{03},\qquad
 \eta_x=t_3h_3^+-h_3^{03}.
\]

In words: the selected excess still has primitive coefficient minus one on the pair copy. Replacing the pair copy by this expression is an invertible integral exterior basis change, even at `t3=0`.

In the selected basis,

\[
 D_x\cong K_A(x_1,x_3,x_5,u_0)\otimes_A\Lambda_A(\eta_x),\qquad d\eta_x=0.
\]

In words: the regular four-normal factor and the independent excess factor are both retained. The checker verifies the basis change, its inverse and the full differential on every exterior generator. The ordered splitting uses the source's already distinguished branch copies; no projection chosen from an unlabelled one-dimensional quotient is involved.

The usual selector sends `eta_u` to `eta_x`. The previous complementary-minor return sends it to `(t1 t3 t5) eta_u`. The next section shows that this multiplier reflects the source support, not just the complementary-minor formula.

## 3. Every ordinary return has the same excess obstruction

Set

\[
 S_x=A/(x_1,x_3,x_5,u_0),\qquad
 S_u=A/(t_1x_1,t_3x_3,t_5x_5,u_0),\qquad
 \tau=t_1t_3t_5.
\]

In words: these are the degree-zero coefficient modules of the two regular factors. Their degree-one homology modules are respectively `S_x eta_x` and `S_u eta_u`.

The exact annihilator is

\[
 \operatorname{Ann}_{S_u}(x_1,x_3,x_5)=\tau S_x\subset S_u.
\]

In words: a raw-source coefficient annihilated by all three selected branch equations must contain every Rees parameter.

**Proof.** The monomial basis of `S_u` consists of monomials containing neither `u0` nor both `t_i` and `x_i` for any branch index. Multiplication by `x_i` kills a nonzero basis monomial precisely when that monomial contains `t_i`. Distinct surviving monomials do not cancel under multiplication by a variable. An element killed by all three `x_i` therefore has a factor `tau`. Conversely, every `tau` multiple is killed by the three `x_i`. Multiplication by `tau` identifies its coefficient quotient with `S_x`. This proves the identity over the entire polynomial ring, not just a bounded monomial truncation.

Consequently every degree-zero derived map satisfies

\[
 f\in\operatorname{Hom}_{D(A)}(D_x,D_u)
 \quad\Longrightarrow\quad
 H_1(f)(\eta_x)\in\tau S_x\eta_u.
\]

In words: every ordinary derived return has the same divisibility restriction on its excess image. Because `D_x` is a bounded free complex, every such derived map is represented by a chain map; no additional higher replacement changes this conclusion.

This also proves actual central vanishing, not just vanishing of an underived map on a displayed quotient. For a chain representative,

\[
 f(\eta_x)=\tau a\eta_u+db.
\]

In words: its excess image differs from a determinant multiple by a boundary. On `t1=t3=t5=0`, the first term vanishes and the second remains a boundary. The specialized selected source still has its primitive excess generator `-h3_pair`; its classes are obtained by specializing the displayed source cycles. Thus its induced degree-one homology map is zero.

This theorem excludes ordinary degree-zero returns into `D_u`. It does not exclude a shifted supported trace or a correspondence with a different, correctly typed target.

## 4. Construct the support operation instead

Let

\[
 I=(x_1,x_3,x_5),\qquad
 J=(t_1x_1,t_3x_3,t_5x_5).
\]

In words: the selected branch is one component of the product-Rees zero locus. The actual containment is `V(I) subset V(J)`.

For one equation `a`, write

\[
 \mathcal C(a)=[A\longrightarrow A[a^{-1}]]
\]

in cohomological degrees zero and one. In words: this is the extended Cech complex computing cohomology with support in the zero locus of `a`. The tensor products below compute the corresponding multi-equation support functors [M1].

The support containment gives

\[
 j:\mathcal C(x_1,x_3,x_5)\longrightarrow
       \mathcal C(u_1,u_3,u_5).
\]

In words: on each Cech component, the map is the localization inclusion. It is the identity on the lower coefficient copy and sends the `x_i`-localized copy into the `u_i=t_ix_i`-localized copy. This is the natural inclusion of smaller support into larger support, not a fitted trace coefficient.

Let `K^bullet(x)` denote the ordered cohomological Koszul dual of the branch resolution. Its degree-one differential is wedge multiplication by the ordered equation vector. The selected residue map is

\[
 \rho:K^\bullet(x_1,x_3,x_5)
 \longrightarrow\mathcal C(u_1,u_3,u_5),
 \qquad
 \rho(e_H)=\left(\prod_{i\in H}\frac{t_i}{u_i}\right)e_H.
\]

In words: a localized Cech direction receives its selected-branch residue coefficient. The formula uses `t_i/u_i` only in a target summand already allowed to invert `u_i`.

In that summand,

\[
 \frac{t_i}{u_i}=\frac1{x_i}.
\]

In words: this is an equality in the indicated localized module. It does not invert `x_i` or `t_i` in the coefficient ring. All comparisons are written using the permitted normal localization and a polynomial Rees numerator.

For one factor, the chain equation is simply `x_i(t_i/u_i)=1`. Tensoring the three factors with their Koszul signs proves the full map. It is equivalently the usual selected-branch residue followed by `j`.

There is also a useful duality square. Let `F` be the diagonal branch selector on the homological Koszul complexes. Its cohomological dual `F^vee` multiplies the `H` component by the product of the included `t_i`. Then

\[
 \rho=\rho_u\circ F^\vee,
 \qquad
 \rho_u(e_H)=\left(\prod_{i\in H}u_i^{-1}\right)e_H.
\]

In words: the supported comparison is the dual selector followed by the raw normal residue. This is not the complementary-minor return applied as an ordinary map to the same homology degree.

### Primitive selected support class

In top local cohomology, the selected class is represented by

\[
 \left[\frac{1}{x_1x_3x_5}\right]
 =\left[\frac{\tau}{u_1u_3u_5}\right].
\]

In words: the numerator `tau` is paired with the full supported denominator; it is not an isolated polynomial multiplier. The class is nonzero: every lower Cech summand omits at least one localized pair, whereas this Laurent monomial has a negative `x_i` exponent in every pair. Its coefficient is a primitive integer. The inclusion of this selected-support class cannot be assessed by discarding the denominator and then specializing the numerator.

## 5. Central specialization retains an extension, not a top residue cycle

Every Cech term is a localization of `A` and is flat over `A`. Thus termwise substitution computes the **derived** coefficient change to a central Rees face.

For a subset `P` of the three branch indices set the corresponding `t_i` to zero. A target Cech term localized in any index of `P` becomes the zero module; it is disjoint from this fibre. The other terms keep their actual localizations. The selected Koszul complex remains the regular branch Koszul complex.

There are eight such faces. On a face with `|P|=p`, the comparison is the tensor product of `p` one-normal counit/extension maps and `3-p` ordinary residue maps. Its support-extension order is `p`. The checker verifies all face maps, all cube edges and every commuting square before reducing the complexes.

On the fully central face put

\[
 A_0=A/(t_1,t_3,t_5),\qquad S_0=A_0/(x_1,x_3,x_5).
\]

In words: the Rees variables vanish, while the branch equations remain a regular sequence.

The target Cech complex becomes `A0` in degree zero. The full residue specializes to

\[
 \varepsilon_x:K^\bullet_{A_0}(x_1,x_3,x_5)\longrightarrow A_0,
 \qquad
 \varepsilon_x^0=1,\quad
 \varepsilon_x^p=0\ (p>0).
\]

In words: its lower coefficient component survives. Looking only at its highest residue component would incorrectly call this the zero map.

This is not a quasi-isomorphism, nor a same-degree homology isomorphism. It is the primitive Gysin extension. In the ordered parameter frame,

\[
 \operatorname{Ext}^3_{A_0}(S_0,A_0)
 \cong S_0\otimes\det(I/I^2)^\vee,
\]

and `epsilon_x` represents its generator after the standard Koszul-dual identification. In words: the surviving value has a three-degree shift and the dual branch determinant; neither is silently trivialized [M2].

**Complete nonvanishing proof.** In `Hom(K^bullet(x),A0)`, a degree-zero map reads the bottom source component. The boundaries of all possible degree-minus-one homotopies form exactly the ideal `(x1,x3,x5)` in that coefficient copy. Therefore the bottom coefficient one is not a boundary, and no nonzero integer multiple becomes a boundary. The other Hom cohomology vanishes by regularity of the three variables. The checker independently reduces all homogeneous sign/degree cases; its 64 representative frames cover all integer multidegrees because existence of a basis component depends only on whether each degree is negative, zero or positive.

The finite dual and homological residue conventions differ by the usual ordered Koszul self-duality and determinant line. Their shifts are retained in this calculation; the top-coefficient description in the next section is the homological version of the same map.

## 6. The actual endpoint normal factors and the independent excess

At the plus endpoint the target normal factor has states `[v_plus,H]` for the eight subsets of its three labels. In source order the homological form of the selected residue is

\[
 \kappa_x(h_H)=\epsilon(H)
 \left(\prod_{i\in\{1,3,5\}\setminus H}\frac{t_i}{u_i}\right)
 [v_+,H].
\]

In words: only unmarked endpoint normals are inverted. `epsilon(H)` is the permutation sign from the ordered source wedge to the target's lexicographic mark order. It is computed from the actual labels. The map leaves any independently retained occurrence/long-normal coefficient frame unchanged.

The target's normal differential removes a mark with its source-prescribed sign and coefficient one. For each removed mark, multiplying the source differential coefficient `x_i` by the target factor `t_i/u_i` gives exactly one. This proves the full normal chain equation. The checker verifies all eight states and their six transported branch/pair versions. Reflection changes the labelled branch; it is not treated as an automorphism of a fixed plus chart.

Use the actual unimodular excess decomposition from Section 2 and tensor this map with

\[
 \operatorname{id}_{K_A(u_0)}\otimes\operatorname{id}_{\Lambda(\eta_x)}.
\]

In words: the residual pair normal and the independent source excess are both retained. The resulting comparison is checked on all 32 original source wedges, not just on a formal extra generator after forgetting its relation to the source.

On the fully central Rees face, the only surviving endpoint normal state is fully marked. In the ordered source and target frames,

\[
 h_1^+\wedge h_3^+\wedge h_5^+
 \longmapsto [v_+,\{1,3,5\}],
\]
\[
 h_1^+\wedge h_3^+\wedge h_5^+\wedge\eta_x
 \longmapsto [v_+,\{1,3,5\}]\otimes\eta_x.
\]

In words: the ordinary and excess-labelled Gysin channels each have primitive coefficient one. The actual lexicographic target sign is accounted for by `epsilon`, not chosen afterward. The excess source itself specializes to `-h3_pair`, so it is not lost as a source direction.

**Important limitation.** The direct image of the bare degree-one cycle `eta_x` under this central residue chain map is zero: its branch factor is in the bottom source degree, whose pole target has disappeared. The primitive surviving data are the *derived residue/Gysin morphisms* just displayed, with their branch shift. These cannot be reported as a nonzero degree-one homology image. The checker contains an explicit negative control for that mistake.

The tensor product in this section is a normal comparison kernel. It has not been embedded, merely by naming its factors, into the full physical costalk. In particular this construction supplies endpoint normal maps, not the two coupled spatial connector 2-cells.

## 7. The actual reverse support pairing becomes Gysin-valued

The previous branch-purity calculation gives complete finite homogeneous complexes `C_K,C_B,C_Q` with an actual support triangle. In the excess frame their distinguished classes satisfy

\[
 \partial[G_+]=[\beta_+],
 \qquad
 \partial^\#[\beta^\#]=[G^\#],
\]
\[
 \langle\beta^\#,\beta_+\rangle=1,
 \qquad
 \langle G^\#,G_+\rangle=1.
\]

In words: the nine-term short-support obstruction is nonzero; its integral graded dual has the primitive reverse connection. The present checker reconstructs those complexes and these closed classes from the complete target differential, rather than importing their ranks as constants.

The short-support functional reads the residual pair-top column with target state

\[
 [\{x_2,D25\},\{D25\}].
\]

In words: this is the actual unmarked-short/marked-long row. Its incoming generic row is the actual marked `D25` state. No detached norm variable is introduced.

Extend the finite complexes by the central normal coefficient ring and tensor their functionals with the supported morphism `epsilon_x`. Define

\[
 \Theta_B=\varepsilon_x\otimes\beta^\#,
 \qquad
 \Theta_Q=\varepsilon_x\otimes G^\#.
\]

In words: the values now retain the branch Gysin extension rather than collapsing that extension to an integer.

The complete tensor differential gives, in the excess channel,

\[
 \partial^\#[\Theta_B]=[\Theta_Q],
 \qquad
 \langle\Theta_B,\beta_+\rangle=[\varepsilon_x],
 \qquad
 \langle\Theta_Q,G_+\rangle=[\varepsilon_x].
\]

In words: the reverse support-to-generic pairing remains primitive and nonzero in its actual shifted determinant frame. It does not manufacture an ordinary lift of `G_+`.

The checker verifies the full tensor complexes, with 352, 296, 56 and 16 generators for the excess-channel K, B, Q and V objects, respectively. The ordinary channel has 472, 416, 56 and 16 generators. In the inherited cohomological dual convention the ordinary generic evaluation has the opposite sign; the computed excess evaluations are both plus one. This degree sign is not a choice of physical reflection parity.

This is a precise coefficient-level compatibility result. It is still a tensor of a genuine affine supported normal map with an already verified **finite homogeneous** target pairing. It is not a claim that the full polynomial target has been replaced by its graded dual, or that a global supported Verdier identification has been proved.

## 8. What has advanced, and the remaining geometric comparison

The normal operation is no longer unspecified. It is the source-defined map of extended Cech support complexes, composed with the ordered branch Koszul residue. Its central value is an explicit primitive Ext class. The independent repeated-normal excess is retained in both the source basis and the shifted trace channel.

There is also a complete negative theorem: an ordinary polynomial return into the raw Koszul source cannot accomplish this. That is a support-annihilator obstruction for every derived replacement, not just a criticism of the previous adjugate matrix.

The nine-term generic obstruction is not declared zero. The constructed operation retains it as a primitive reverse pairing with values in the branch Gysin line. This is consistent with the earlier conclusion that a geometric supported operation must *use the extension* rather than invent a covariant filler.

The remaining physical construction must identify this normal support comparison with the normal restriction of the actual normalized-log correspondence and construct its two spatial endpoint connector 2-cells while retaining the generic Q representative. Neither a local support inclusion nor its primitive residue value alone determines those cells. No physical parity has been assigned.

## 9. Reproduction and provenance

Run:

```sh
python check_marici_rees_supported_residue_trace.py \
  --output marici_rees_supported_residue_trace_certificate.json
```

The self-contained standard-library checker passes **13,746 exact assertions**. They cover the complete Cech maps; the Koszul dual selector square; all eight partial central Rees faces, cube edges and squares; the primitive central Hom class; the full selected-source excess basis; all 32 source-wedge residue equations; six transported endpoint normal maps; finite monomial controls for the all-polynomial annihilator proof; and both actual Gysin-valued reverse target pairings.

The proofs of support functoriality, all-polynomial annihilators and Ext nonvanishing are given above. Finite monomial tests are controls, not extrapolated proofs. This is executable exact verification, not proof-assistant certification. No repository files were changed.

Pinned source inputs and blob hashes are recorded in the certificate:

- `research/voevodsky/check_d03_plus_excess_beck_chevalley.rs`, blob `df8448271089910a90c8e641af5b8ae95f1472dd`: actual branch/pair ideals and the independent excess.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: actual target coefficient domains and normal differential.
- `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: endpoint labels and transport conventions.
- `src/ledger/20260814-115 Boundary-Triad Tate Realization and the Multi-Rees Cartier Bicomplex.md`, blob `63da17cb5d641705056c5d5b9bc6f53cda72baf5`: the declared product-Rees chart and the distinction between normal symbols and extraordinary spatial maps.

Inherited finite-Hom construction: `marici_branch_purity_dual_transgression.md` and its checker. Its distinction between finite graded duality and full supported Verdier duality remains in force.

Primary mathematical conventions:

[M1] Stacks Project, Section 47.9, *Local cohomology*, tag `0952`: the extended Cech model for derived support and its canonical map to the underlying object.

[M2] Stacks Project, Lemma 48.14.1, *Right adjoint of pushforward for effective Cartier divisors*, tag `0B4B`: the one-normal dual line and shift. Tensoring the three ordered regular equations gives the determinant and degree-three class used here.

[M3] Stacks Project, *Hom complexes*, tag `0A8H`, and *The Koszul complex*, tag `0621`: tensor-Hom signs and ordered exterior comparison.

The particular selected residue matrices, all-return annihilator theorem, complete central-fibre comparison and Gysin-valued literal-row pairing are derived in this note. They are not claims attributed to those general references.
