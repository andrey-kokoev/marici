# A cubical complementary-support kernel for the full Marici coefficient target

Date: 2026-09-07  
Project: Marici, Branch B  
Repository input: `andrey-kokoev/marici` at `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. What is constructed

The complete 215-state target has a source-defined **spatial realization of its graded dual**. Its cells are actual cubical intervals in the already used labelled face-poset ball. The generic and endpoint support maps become inclusions or relative quotients of explicitly specified subcomplexes. The permitted coefficient domains become relative coordinate faces. The construction retains the complete differential, not only homology or a chosen trace row.

In this geometry the previously computed reverse generic pairing is the boundary of an actual relative edge, tensored with the two residual source normal/excess cells. The nine-term obstruction evaluates to one against that cell. Its boundary evaluates to one against the generic class. Both known endpoint collar homotopies and the full five-triangle Morse identity remain in the same triangulated space. A cubical cap diagonal and its compatible simplicial diagonal are constructed explicitly.

This is a completion of the **finite graded spatial incidence kernel**. It is not a proof that this kernel equals an unspecified ringed supported-Verdier functor on all normalization-sheet modules. The endpoint collar operators are verified in their existing carrier/unit frame; the endpoint residue channels and the generic excess channel retain their distinct fine degrees. Their presence in one spatial space does not, by itself, construct a source-sheet morphism commuting with all cross-frame Rees and endpoint maps. No physical parity is assigned.

The old factorized residue–blowdown morphism stays generically nullhomotopic. Nothing below turns its zero generic image into a nonzero one. The new operation uses complementary support before taking the generic restriction.

## 2. The actual spatial interval correspondence

Let P be the face poset of the labelled hexagon associahedron, written as noncrossing sets of its nine diagonals, including the empty set. There are 45 such sets. Denote the two endpoint sets by

\[
v_+=\{x_1,x_3,x_5\},\qquad v_-=\{x_0,x_2,x_4\}.
\]

In words: these are the same odd and even endpoint labels as in the source. Here x is a spatial label, not a new identification of an occurrence variable with a Rees coordinate.

For every source state (S,H), with H a subset of S, define the actual closed cube

\[
\square(H,S)=\{z\in[0,1]^9:z_a=1\ (a\in H),\ z_a=0\ (a\notin S)\}.
\]

In words: coordinates in H are fixed at one, coordinates outside S are fixed at zero, and the coordinates in S minus H vary freely. A relative interior, rather than a repeated closed cube, is used as the corresponding cell.

Let W be the union of these cubes. A maximal cube is indexed by a triangulation S of the hexagon. The exact cell counts by dimension are

\[
(45,93,63,14).
\]

In words: the entire spatial cubical complex has 215 cells. Its maximal cubes have dimension three. These numbers are the reversed-degree counts of the actual normal-decorated target, not an added set of filling generators.

Each cube has the standard ordered triangulation

\[
H\subset H\cup\{a_{\pi(1)}\}\subset\cdots\subset S,
\]

summed with the sign of the permutation of its free coordinates. In words: the triangles and tetrahedra are existing flags in P. The union of these triangulations is exactly the earlier 509-simplex flag space, with counts 45 vertices, 170 edges, 210 triangles and 84 tetrahedra.

The cubical face category has an interval object for every H contained in S. If an interval is a face of another interval, its lower endpoint grows while its upper endpoint shrinks. Consequently the two projections define the variance pattern

\[
P^{\mathrm{op}}\longleftarrow\mathcal I(P)\longrightarrow P.
\]

In words: one leg is contravariant in the lower face and the other is covariant in the upper face. This is an actual incidence correspondence, not the ordinary blowdown followed by a transpose of its already zero generic map.

### Exact boundary and sign dictionary

Order the free coordinates of a cube by the source's lexicographic diagonal order. Its boundary is

\[
\partial\square(H,S)=\sum_{a\in S\setminus H}
(-1)^{\operatorname{pos}_{S\setminus H}(a)}
\bigl(\square(H\cup\{a\},S)-\square(H,S\setminus\{a\})\bigr).
\]

In words: every free coordinate has its upper and lower boundary faces, with the ordinary product orientation. The two kinds of faces reverse the source's normal-removal and radial-addition arrows, respectively.

The original target degree is n=3-|S|+|H|. Use a shifted-transpose dual whose geometric degree is 3-n and whose differential is the ordinary matrix transpose. It differs from a conventional Hom-complex sign convention only by an explicit degreewise sign change. On a basis dual, the spatial comparison is

\[
[S,H]^\dagger\longmapsto \epsilon(S,H)\square(H,S),
\]

\[
\epsilon(S,H)=(-1)^{|S|+|H|(3-|S|)+\sum_{h\in H}\operatorname{pos}_S(h)}.
\]

In words: this signed identification carries both classes of source arrows to the actual cubical boundary. The checker verifies the formula on every one of the 215 states, including all mixed normal–radial squares.

The physical group action also retains its orientation line. The geometrical action permutes free cube coordinates with their permutation sign. The source dual action differs from it by precisely the inherited ambient orientation character, not an independently chosen reflection sign. This is checked for all six source transports.

## 3. Complementary supports: the correct generic space and both endpoints

Let L be the set of three long diagonals. Define two closed cubical subcomplexes:

\[
W_Q=\bigcup_{H\subseteq S\in P,\ S\subseteq L}\square(H,S),
\qquad
W_E=\bigcup_{H\subseteq S\in P,\ S\notin\{v_+,v_-\}}\square(H,S).
\]

In words: W-Q is the three-long-direction tripod, and W-E omits the two endpoint upper stars. Their cell counts are 7 and 199. Their inclusion is strict:

\[
W_Q\subset W_E\subset W.
\]

In words: this is the complementary-support counterpart of the source endpoint/short-boundary/full-target filtration.

Write K for the full original target, B for its short-support subcomplex, V for its two endpoint subcomplexes, E=K/V, and Q=K/B. Before the coefficient restrictions in Section 4, the dual spatial objects are:

| Original object | Spatial dual object |
|---|---|
| K | chains on W |
| Q | chains on W-Q |
| B | relative chains on (W,W-Q) |
| E | chains on W-E |
| V | relative chains on (W,W-E) |
| B/V | relative chains on (W-E,W-Q) |

In words: the support arrows genuinely reverse. In particular the reverse connecting map is the boundary of a relative chain, rather than a proposed ordinary lift into E.

This does **not** reinstate the earlier erroneous primal projection onto the chamber–long-facet subposet. That primal projection deleted mixed triangles and was not a chain map. The tripod here is a *dual* subcomplex, with a complementary degree shift and coefficient-dependent relative endpoints. At unit degree it has three edges and four vertices with the three outer vertices relative, and therefore has its two nonzero homology classes in degree one. This matches the actual primal generic carrier in degree two.

## 4. Every coefficient domain has a spatial boundary description

Keep the original ring and localizations

\[
R=\mathbb Z[X_a,u_a\mid a\in\mathscr D],\qquad
R_{S,H}=R[u_a^{-1}:a\in S\setminus H].
\]

In words: occurrence variables remain polynomial. A normal inverse is allowed only on its original unmarked target state.

The unit-frame monomial attached to a state is

\[
w_S=\prod_{a\in S}\frac{X_a}{u_a}.
\]

In words: in a fine degree alpha, that state's unique possible coefficient monomial has exponent alpha plus the exponent of w-S. Whether it is legal is decided in its own stalk. This is not evaluation of the variables at one.

There is an independent geometric description. For each coordinate a:

* a negative occurrence degree equal to minus one deletes the face z-a=0; an occurrence degree below minus one deletes the entire mode;
* a negative normal degree deletes both faces z-a=0 and z-a=1;
* a zero normal degree deletes the face z-a=1;
* a positive normal degree deletes neither face on account of that normal.

Let A-alpha be the union of these forbidden coordinate faces, intersected with W. Each is a closed cubical subcomplex. Thus the degree-alpha dual is genuinely a relative spatial chain complex:

\[
K_\alpha^\dagger\cong C_*(W,A_\alpha;\mathbb Z).
\]

In words: the localization restrictions become relative faces, not illegal inverses and not a discretionary deletion rule.

For the other support objects, intersect the subspaces above with A-alpha. Explicitly,

\[
Q_\alpha^\dagger\cong C_*(W_Q,W_Q\cap A_\alpha),
\quad
E_\alpha^\dagger\cong C_*(W_E,W_E\cap A_\alpha),
\]

\[
B_\alpha^\dagger\cong C_*(W,W_Q\cup A_\alpha),
\quad
V_\alpha^\dagger\cong C_*(W,W_E\cup A_\alpha).
\]

In words: both the spatial support filtration and the coefficient-domain filtration are retained simultaneously.

These formulas hold for arbitrary exponents: the proof is the displayed inequality test on the unique monomial, and depends only on the stated thresholds. The checker compares the independent geometric and algebraic definitions in 575 frames. It additionally checks all 2,304 multiplication arrows in the nine-normal Boolean cube. Under duality, multiplication is the actual quotient map from a less-relative cube complex to a more-relative one.

Accordingly the construction is compatible with the full fine-graded coefficient action. It is not a single unexplained integer functional. Nevertheless, this **graded integral dual** is not automatically the ringed functor RHom over R into a dualizing object. That identification, including its completion convention where relevant, is a separate assertion and is not made here.

## 5. A cap diagonal on the same space

For a cube with free-coordinate set T=S minus H, define

\[
\Delta\square(H,S)=
\sum_{L\subset T}(-1)^{\nu(L)}
\square(H,H\cup L)\otimes\square(H\cup L,S),
\]

where nu counts pairs of ordered free coordinates i<j with i outside L and j inside L. In words: this is the tensor product of the interval diagonal; the sign is the tensor-reordering sign.

The exact identities are

\[
\partial\Delta=\Delta\partial,
\qquad
(\Delta\otimes1)\Delta=(1\otimes\Delta)\Delta.
\]

In words: this is a chain diagonal and is strictly coassociative. It gives a genuine cellular cap operation by evaluating one tensor factor.

Let Tri be the ordered cube-to-flag triangulation. On this particular ordered triangulation, the stronger identity holds:

\[
\Delta_{\rm AW}\operatorname{Tri}
=(\operatorname{Tri}\otimes\operatorname{Tri})\Delta.
\]

In words: the cubical diagonal and the simplicial Alexander–Whitney diagonal agree strictly after subdivision. No additional cap-comparison filler or averaging is needed. The checker initially allows an acyclic-carrier comparison homotopy, then verifies that every column of that homotopy is zero because the two maps already agree.

All of these constructions stay in the closed cube supporting a term. They therefore descend to the relative face quotients in Section 4 and preserve the complementary support subcomplexes. The ordinary cap/Stokes relation is realized here by explicit matrices rather than imported as a numerical pairing.

## 6. The primitive reverse generic pairing is an actual relative edge

Keep the source repeated-normal excess and perform the already verified regular branch purity. The residual source is K(u0,0), retaining the independent zero-differential excess direction. For its homogeneous derived-Hom complex, the new spatial carrier is an explicit relative subcomplex of

\[
W\times I_0\times S^1_\eta.
\]

In words: the residual regular normal is represented by an interval with one relative endpoint, and the excess is represented by its independent zero-boundary one-cell. This is a spatial model of the existing Koszul factor, not the claim that an additional physical circle has been adjoined or discovered.

The source mask and the target coefficient frame determine the permitted product cells. Their closure minus the permitted cells is verified to be a closed subcomplex. Thus these are genuine relative CW pairs, not matrices assigned a spatial name. In the critical excess frame, the full pair has 486 ambient cells, 442 relative cells and 44 active cells. Its short-support quotient has 37 active cells; its generic subcomplex has seven. All 44 complete product differentials, with every source and target contribution, agree with the earlier Hom dual by an explicit signed isomorphism.

The key target edge is

\[
J=\square(\{D25\},\{x_2,D25\}).
\]

In words: this is the existing edge from the marked D25 vertex to the vertex with both x2 and D25 marked. Its upper endpoint is a relative face in the critical frame: the original x2 normal degree forbids that upper state. Its lower endpoint lies in the actual generic subcomplex. Therefore

\[
\partial J=-[\{D25\}].
\]

In words: the nonzero boundary is forced by the actual localization domain, rather than by a fitted sign or coefficient.

Let e0 denote the residual normal interval class and eta the independent excess one-cell. With the verified product orientation, the spatial representatives are

\[
\Xi_B=-e_0\otimes\eta\otimes J,
\qquad
\Xi_Q=e_0\otimes\eta\otimes[\{D25\}],
\qquad
\partial\Xi_B=\Xi_Q.
\]

In words: the short-support class has total geometric dimension three, and its generic boundary has dimension two. The boundary is zero only after taking the short-support relative quotient. This is the required direction of the reverse transgression.

Under the explicit identification with the source-Hom dual, Xi-B is exactly the covector reading the actual row with target `[x2,D25; D25 marked]` and source pair-top input. The primal coefficient of that row is

\[
\frac{X_2X_{D25}u_{D03}u_{D14}}{u_2}.
\]

In words: only u2 is inverted, on its legal unmarked state. Xi-Q corresponds to the negative marked-D25 row, with coefficient X-D25 u-D03 u-D14 and no normal inverse.

Let beta-plus be the actual nine-term short-support obstruction and G-plus its prescribed generic source class. The explicit evaluation is

\[
\langle\Xi_B,\beta_+\rangle=1,
\qquad
\langle\Xi_Q,G_+\rangle=1.
\]

In words: the two earlier one-row functionals now have an actual relative spatial cell and a literal attaching endpoint. The pairings are primitive and agree under all six transported branch/pair charts.

An independent integral cancellation of the entire relative product complexes gives one degree-three short-support class, one degree-two generic class, and no total-complex homology in the critical frame. Hence this connecting map is an integral isomorphism. It is not the dualization of the old nullhomotopic spatial source morphism.

## 7. Both endpoint operators and the full Morse homotopy are retained

The endpoint corners in W are the vertices indexed by v-plus and v-minus. In the unit coefficient frame their dual meridians are the lower boundaries of the actual three-cubes

\[
\square(\varnothing,v_+),\qquad\square(\varnothing,v_-).
\]

In words: each endpoint gives three signed square faces in the endpoint-complement complex; the forbidden upper faces are relative. Both two-cycles are primitive. The endpoint-complement complex has exactly one integral homology class in degree two, and both cycles represent that class up to their prescribed orientation gauges.

More importantly, the actual endpoint *comparison operators* are also transferred, rather than replaced by those homology classes. The positive collar is the one-flip path from v-plus to m={D03,x1,x3}; the negative collar is the three-flip path from v-minus through `{D03,x0,x4}` and `{D03,x0,x3}` to m. Their existing chain equations become exact cochain-homotopy equations on the complementary cubes.

In the lexicographic cube frame the positive operator evaluates the square `[empty,x1 x3]` with coefficient one. The negative operator has coefficients +1 on `[empty,x0 D03]`, +1 on `[empty,x0 x4]`, and -1 on `[empty,D03 x3]`. These are evaluations of the actual oriented paths, not independently fitted endpoint columns. The checker verifies their homotopy equations on every cell of the full unit-frame dual complex.

For occurrence coefficients, these statements use the actual principal occurrence lines and their dual frames. The corresponding raw equations remain

\[
\partial h_+=\mu[m]-w_+[v_+],
\qquad
\partial h_-=\mu[m]-w_-[v_-],
\]

with the same distinct midpoint and endpoint monomials as in the preceding construction. In words: no occurrence variable is set to one or inverted in the coefficient ring.

The full five-triangle Morse chain also stays in the very same 509-simplex triangulation. With q-partial the seven-term completed roof and Gamma the eight-term corridor,

\[
\partial H=q_{\partial}-\Gamma.
\]

In words: the Morse operator is retained on the full flag-cochain complex. Evaluating this equation against every edge covector verifies its higher comparison equation, including the mixed generic/short-support flags.

Consequently the old covariant generic morphism remains null. The new nonzero reverse pairing comes from the complementary incidence correspondence and its relative edge in Section 6, not from deleting H or forgetting the endpoint terms.

### The remaining endpoint limitation

The carrier collar operators in this section are verified in their unit homogeneous sector. After branch purity, both endpoint residue channels occur at the fully marked endpoint vertex, but in their own normal determinant frames. The generic excess channel uses a different frame. The interval correspondence and coefficient quotient maps retain these distinctions; they do not prove that the prescribed normalization-sheet source supplies the missing maps between them.

In particular, a degree-two endpoint residue cell is not automatically the required connector 2-cell in the full normalization-sheet butterfly. The latter is a comparison of specified morphisms and must satisfy the corresponding source-side and Rees equations. That final identification is not asserted.

## 8. Supported Rees residue on the whole spatial kernel

Use the already constructed source support map

\[
\rho:K^\bullet(x_1,x_3,x_5)\longrightarrow
\bigotimes_{i\in\{1,3,5\}}[A\longrightarrow A[(t_ix_i)^{-1}]],
\]

\[
\rho(e_H)=\left(\prod_{i\in H}\frac{t_i}{u_i}\right)e_H,
\qquad u_i=t_ix_i.
\]

In words: this is the complete lower-plus-localized map, not just its highest pole term. The x in this display denotes the declared branch-section coordinate, distinct from the spatial labels and uppercase occurrence variables unless an additional source identification says otherwise.

Tensor rho with the **entire product-cellular differential** of the incidence kernel, retaining its source normal and excess factors. The checker verifies the chain map, both square-zero identities, and the legal localization domains on all 2,816 source columns across the eight central Rees faces. Thus the Stokes identity for Xi-B and Xi-Q remains compatible with the supported coefficient operation.

On the complete central Rees face the localized coefficient summands vanish but the lower component remains the identity. The all-degree normal argument from the preceding supported-residue proof identifies this map with the primitive branch Gysin extension epsilon-x. Accordingly the reverse pairing can retain its supported value:

\[
\langle\Theta_B,\beta_+\rangle
=\langle\Theta_Q,G_+\rangle
=[\varepsilon_x].
\]

In words: the unit spatial incidence coefficient multiplies the nonzero supported extension. The independent excess label is retained. This does not claim that the bare degree-one excess has a nonzero same-degree target homology image.

This tensor construction concerns the specified independent supported coefficient factor and the spatial graded incidence kernel. Identifying their tensor with the raw logarithmic correspondence requires the source-side cross-frame compatibility discussed above. The source chart's occurrence, normal, branch-section and external Rees lines may not be silently equated.

## 9. Consequence and remaining map

There is now a complete finite spatial target for the proposed complementary-support operation. It includes all marked states, the correct reversed support arrows, the coefficient-domain faces, an explicit cap diagonal, the actual relative cell realizing the primitive reverse pairing, and both previously constructed carrier endpoint operators. Another abstract target or another isolated parity detector is unnecessary.

The open physical assertion is narrower but real: construct the normalization-sheet morphism into this kernel, including the maps between its distinct endpoint and excess frames, and identify that morphism with the ringed supported-Verdier/logarithmic pull-push prescribed by the source. The existence of the graded incidence kernel does not prove that assertion, and equality of its scalar evaluations with the desired values cannot substitute for it.

No physical reflection parity is selected by the present result. The previous no-go for the factorized ordinary blowdown remains valid.

## 10. Reproduction and provenance

Run:

```sh
python check_marici_cubical_supported_dual_kernel.py \
  --output marici_cubical_supported_dual_kernel_certificate.json
```

The standalone standard-library checker passes **596,220 exact assertions**. It reconstructs the target from the pinned rules, verifies the 215-cell cubical realization and all 509 flag simplices, constructs and compares the two diagonals, checks 575 coefficient frames and 2,304 normal multiplication maps, retains both endpoint collar operators and all five Morse triangles, realizes both source channels as actual relative CW pairs, verifies the critical reverse pairing and its six transports, and tests the complete supported tensor on all eight Rees faces. The count includes the exact source-Hom and integral-reduction helper checks; it is not a claim of proof-assistant certification.

Source files:

* `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: actual target differential and permitted stalk domains.
* `research/voevodsky/check_d03_plus_excess_beck_chevalley.rs`, blob `df8448271089910a90c8e641af5b8ae95f1472dd`: actual repeated-normal source and excess orientation.
* `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: both physical endpoint labels, road orientation and corridor paths.
* `research/voevodsky/check_d03_normalized_blowdown_counit.py`, blob `0fcbbf37a4f70dc0c2787ad7cb954287b9e97403`: the full Morse and normalized-blowdown chains.
* Ledger 136, `Canonical AW-Cap Roof and the Endpoint-Connector Gap`, blob `9afc5c63217bcf0240bd4837f342981eac680697`: prior carrier cap and its scoped endpoint limitation.
* Ledger 184, `Loaded AW Collar Principal-Line Repair and the Spatial Connector Gate`, blob `68f960715e1c064411f3869daed7edaa2e6ee7cc`: distinction between principal-line evaluation and occurrence inversion.

Prior local constructions: `marici_branch_purity_dual_transgression.md`, `marici_rees_supported_residue_trace.md`, and `marici_common_spatial_correspondence_gate.md`.

Standard conventions: Stacks Project, Hom complexes, tag `0A8H`; local cohomology and extended Cech support complexes, tag `0952`. The new spatial identifications in this note are established by their explicit cubical and coefficient equations rather than attributed to these general references.
