# The native conductor dual maps to the short-face occurrence diagram

Date: 2026-09-07  
Project: Marici, native-source comparison lane  
Pinned source repository: `andrey-kokoev/marici`  
Commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## 1. Result and exact scope

There is a canonical polynomial ring quotient from the coordinate ring of the actual short-face complex to the native normalization-conductor node. Its complete derived dual is now realized by an inclusion of explicit module-valued spatial face complexes. Both native branch maps, their joint normalization homotopy, and their principal occurrence frames are retained.

The comparison does not send the native conductor class to a nonzero closed class. The three actual mixed short edges attach that class: each has the native endpoint difference as its boundary, up to the existing same-branch comparisons. The resulting connecting map is the constant-value row `(1,1,1)`. Its two-dimensional kernel is computed, not inserted.

The source free resolution has ranks `(1,9,18,15,6,1)`. The short-face coordinate ring has a free resolution of ranks `(1,6,9,6,2)`. We construct the resolution-level quotient map, its derived dual, two polynomial quasi-isomorphisms to the spatial face complexes, and the homotopy making the whole comparison square commute. Thus this is more than an agreement of cohomology groups or endpoint values.

**Scope:** the constructed target is the squarefree occurrence dualizing diagram of the existing short-face geometry. It is not asserted to be the original 215-state support-PC stalk diagram, nor its complete independent-normal/Rees-supported Verdier dual. The new face modules are specified coordinate-support quotients. Their relation to the original localization stalks still requires a comparison, not a change of names. Physical endpoint collar 2-cells and physical reflection parity are not identified by this result.

## 2. Native source and the actual short faces

Let S be the polynomial spectator ring in the three long occurrence variables. The executable uses the six short variables and proves identities that extend over S by flat base change. Put

\[
A=S[X_0,X_1,X_2,X_3,X_4,X_5],\qquad
E=\{0,2,4\},\quad O=\{1,3,5\}.
\]

In words: occurrence variables remain polynomial and independent. No occurrence variable is identified with a normal or Rees parameter.

The native source [S1] is

\[
\mathfrak B=A/(J_EJ_O),\qquad
J_E=(X_0,X_2,X_4),\quad J_O=(X_1,X_3,X_5).
\]

In words: every mixed even-odd product vanishes. The plus normalization sheet is `A/J_E`, the minus sheet is `A/J_O`, and their conductor is `C=A/(J_E+J_O)`.

This is the coordinate ring of the simplicial complex Sigma consisting of the filled even triangle and the filled odd triangle. The two triangles are disjoint as geometric simplicial complexes; they share only the empty face in the augmented face notation.

Independently enumerate the six short diagonals `(i,i+2)` in the labelled hexagon using the source's crossing test [S2]. Two short diagonals cross precisely when their indices are adjacent modulo six. Therefore their noncrossing complex Delta is

\[
\Delta=\{F\subseteq\{0,\ldots,5\}:\{i,i+1\}\nsubseteq F\quad(0\le i<6)\}.
\]

In words: retain the short-label subsets that do not contain adjacent cyclic labels. The indices in this formula are cyclic.

The only faces of Delta not already in Sigma are

\[
\{0,3\},\qquad\{2,5\},\qquad\{1,4\}.
\]

In words: exactly three actual mixed short edges join the native triangles. There are no mixed triangles. The counts by cardinality, including the empty face, are

\[
(1,6,6,2),\qquad(1,6,9,2).
\]

In words: the native complex has fifteen face summands; the full short complex has eighteen. All these faces occur in the already fixed forty-five-face hexagon complex.

## 3. A canonical ring map and its exact kernel

Define

\[
T=A/(X_0X_1,X_1X_2,X_2X_3,X_3X_4,X_4X_5,X_5X_0).
\]

In words: this ring imposes exactly the six crossing-pair relations of the actual short-face complex. The native node additionally imposes the three mixed opposite-pair relations. Consequently restriction to the two native triangles gives a canonical quotient

\[
q:T\longrightarrow\mathfrak B.
\]

In words: this map is supplied by the inclusion of labelled face complexes, not prescribed by a target residue value.

For an oriented even-to-odd bridge `(e,o)`, put

\[
A_{eo}=A/(X_j:j\notin\{e,o\}),\qquad
P_{eo}=X_eX_o A_{eo}.
\]

In words: the bridge kernel contains a genuine principal occurrence factor, while the remaining four short coordinates annihilate it. The long spectators remain untouched.

There is a short exact sequence of A-modules

\[
0\longrightarrow P_{03}\oplus P_{25}\oplus P_{41}
\longrightarrow T\xrightarrow{q}\mathfrak B\longrightarrow0.
\]

In words: the entire difference between the native source and the short-face coordinate ring is three explicitly supported opposite-pair modules.

Proof for all polynomial exponents: a monomial in T is nonzero exactly when its support is a face of Delta. It maps to zero in the node exactly when the support meets both parities. The only such faces of Delta are the three opposite pairs. Such a monomial therefore belongs to exactly one of the displayed modules and is divisible by its pair product. Multiplication by any of the four complementary coordinates creates a forbidden adjacent pair, while powers of the two pair coordinates survive. The summands are disjoint because no face contains two different mixed pairs. This proves exactness, the direct-sum decomposition, and the precise annihilators without any localization.

The short-face ring T is a newly explicit coordinate-support model extracted from the existing geometry. It is not obtained by silently replacing the polynomial modules in the original support-PC complex by their face-coordinate quotients.

## 4. The polynomial module-valued spatial dual

For every face F define

\[
A_F=A/(X_i:i\notin F).
\]

In words: the module at a face is its actual coordinate-support quotient. For a face complex Gamma, define

\[
\mathcal I_\Gamma^{-p}=\bigoplus_{F\in\Gamma,\ |F|=p}A_F.
\]

In words: a face with p labels contributes in cohomological degree minus p. The empty-face summand is C in degree zero.

If `F=(i_0,...,i_{p-1})` is increasingly ordered, the differential on its summand is

\[
d(a[F])=\sum_{j=0}^{p-1}(-1)^j
\bigl(a\bmod X_{i_j}\bigr)[F\setminus\{i_j\}].
\]

In words: remove a vertex, evaluate its coordinate at zero, and keep the incidence sign. The maps are A-linear between the stated quotient modules. Every double deletion cancels in opposite orders, so the differential squares to zero.

Let the relative ambient canonical line retain its fine degree:

\[
\omega_A=A\,(dX_0\wedge dX_1\wedge\cdots\wedge dX_5),\qquad
\mathcal D(M)=R\operatorname{Hom}_A(M,\omega_A)[6].
\]

In words: this common dualizing normalization records all six occurrence directions. The earlier native degree-three and degree-five groups occur in degrees minus three and minus one after this common shift. The six-direction determinant is not deleted.

We construct polynomial quasi-isomorphisms

\[
j_{\mathfrak B}:\mathcal D(\mathfrak B)\xrightarrow{\simeq}\mathcal I_\Sigma,
\qquad
j_T:\mathcal D(T)\xrightarrow{\simeq}\mathcal I_\Delta.
\]

In words: these identify complete derived duals, including their nonzero attachments, with the module-valued spatial face complexes.

This type of squarefree dualizing description is consistent with the squarefree-module/sheaf duality literature [M1]. Here the integral comparison is proved directly by constructing the maps and testing their mapping cones in every possible homogeneous pattern. We do not import a field-only theorem as an unproved assertion over the integers.

### Explicit free models and the all-degree proof

The node has the native product-ideal resolution. Its positive-degree generators are pairs `(U,V)` of nonempty even and odd subsets, in degree `|U|+|V|-1`, with coefficient weight equal to their union. The first nine differentials are the nine even-odd products; all higher differentials are the two ordered Koszul differentials with their tensor sign. This is a resolution because it is the tensor product of the two truncated regular Koszul resolutions of the ideals, followed by their product inclusion into A. It has fifty generators.

The short-face ring has its six-generator Taylor resolution, with sixty-four generators. The differential deletes an ideal generator and multiplies by the corresponding quotient of least common multiples. In each monomial degree the augmented complex is the simplex on the ideal generators dividing that monomial, proving exactness. Twenty signed-unit cancellations give the minimal twenty-four-generator resolution, with ranks `(1,6,9,6,2)`.

The quotient map is lifted to these free resolutions by explicitly contracting the acyclic monomial-degree subcomplexes of the native resolution. This gives a sixty-four-column polynomial map lifting the identity on degree-zero ambient coefficients. Its dual has fifty source columns.

Every free dual generator, after the common six-direction twist, has internal shift with entries zero or one. A degree-zero map to `A_F` has one possible coefficient monomial, and that monomial is legal exactly when its positive support lies in F. The complete native-to-face system has twenty-four integer unknowns. Its cochain equations plus the primitive native conductor normalization have rank eighteen; an integral solution is exhibited.

The target-to-face map and the naturality homotopy are solved together, in a system with 167 integer unknowns and rank 100. Exact elimination produces integral coefficients; no occurrence variable is a pivot or denominator. These systems construct representatives; their nonunique auxiliary solutions are not physical parity choices.

For each nonnegative fine degree alpha, all matrices depend only on which alpha-coordinates are zero and which are positive. Below zero both sides are empty. Thus sixty-four patterns exhaust all possible homogeneous comparison cones, including arbitrary exponent sizes. All 128 cones contract by signed-unit operations. This proves both quasi-isomorphisms over A, not just in a selected occurrence slice.

## 5. The whole source-to-spatial square, including its homotopy

The geometric inclusion is a strict A-linear cochain map

\[
\iota:\mathcal I_\Sigma\longrightarrow\mathcal I_\Delta.
\]

In words: keep every native face summand and all its restriction maps. Both endpoint triangles and all their lower faces remain unchanged.

For the resolution-level quotient lift phi, the constructed degree-minus-one homotopy K satisfies

\[
j_T\phi^\vee-\iota j_{\mathfrak B}=dK+Kd.
\]

In words: the source ring quotient and the geometric inclusion represent the same complete derived map. This is a comparison of full polynomial complexes, with the off-diagonal homotopy retained [M2].

The certificate contains phi, both j maps, and K as explicit polynomial matrices. In the constructed representatives, they have 67, 6, 16, and 4 nonzero target entries respectively. Their construction does not split the native source into independent cohomology lines.

The exact native node-to-sheet maps are also retained. On a positive-degree source generator they are

\[
f_+(p_{U,\{v\}})=X_v e_U,
\qquad
f_-(p_{\{u\},V})=X_u e_V.
\]

In words: the other components vanish, and the common degree-zero unit maps to one on both sheets. Their joint comparison to the conductor resolution is the existing ordered-wedge homotopy, including the sign from the normalization difference.

After duality and the constructed spatial comparison, the two branch classes are

\[
X_1X_3X_5[1,3,5],\qquad -X_0X_2X_4[0,2,4].
\]

In words: the two source branches map to the actual endpoint triangles with their full principal occurrence factors. The relative minus sign is derived from the same native normalization sequence. These are primitive generators of their respective principal ideals; there is no division by either product.

This intertwines the native endpoint attachment data within the occurrence face model. It does **not** identify these cohomological maps with the physical collar 2-cells in their separate normal/Rees frames.

## 6. The conductor class is attached by three literal mixed edges

In the common dualizing frame, the native conductor generator can be represented by

\[
c=[1]-[0]\in\mathcal I_\Sigma^{-1}.
\]

In words: it is the difference of the two native connected components. It is a cycle, is not a native boundary, and is annihilated in cohomology by all six short coordinates.

Orient each new mixed edge from its even endpoint to its odd endpoint. Its actual differential is

\[
d[e,o]=[o]-[e].
\]

In words: each mixed edge attaches the same primitive native conductor class, after the existing comparisons within each filled triangle. No boundary row has been inserted by hand.

The quotient complex is

\[
\mathcal I_\Delta/\mathcal I_\Sigma
\cong(A_{03}\oplus A_{25}\oplus A_{41})[2].
\]

In words: the three coordinate-plane modules lie in degree minus two, and their quotient differential is zero. Their attaching maps remain in the full complex.

The connecting map is

\[
\delta:A_{03}\oplus A_{25}\oplus A_{41}\longrightarrow C,
\qquad
\delta(a_{03},a_{25},a_{41})
=a_{03}(0,0)+a_{25}(0,0)+a_{41}(0,0).
\]

In words: each bridge contributes its constant value on the conductor. The input modules retain all polynomials on their respective two-coordinate planes. This is not just an integer rank statement.

An explicit short-face homotopy is

\[
d\bigl([0,3]-[1,3]\bigr)=[1]-[0].
\]

In words: the conductor class becomes a boundary using one actual mixed edge and one existing same-branch edge. This path is a displayed representative, not a privileged physical route. Different choices differ by genuine cycles in the short-face complex.

Thus

\[
H^{-1}(\mathcal I_\Delta)=0,\qquad
H^{-2}(\mathcal I_\Delta)=\ker\delta,
\]

\[
H^{-3}(\mathcal I_\Delta)
=X_1X_3X_5B_+\oplus X_0X_2X_4B_-.
\]

In words: the endpoint branch channels remain, the isolated conductor cohomology class no longer survives, and the new degree-minus-two information is the full kernel of the three bridge augmentations. These are the only nonzero cohomology modules.

For Sigma alone, the degree-minus-three group is the same and the degree-minus-one group is C. The complete inclusion, rather than those groups by themselves, transports the native nonsplit attachment.

In constant degree, the exact sequence reduces to

\[
0\longrightarrow\mathbb Z^2\longrightarrow\mathbb Z^3
\xrightarrow{(1,1,1)}\mathbb Z\longrightarrow0.
\]

In words: two independent differences of bridge choices remain. The augmentation is primitive. A strictly rotation-invariant integral lift of one would require three equal coefficients with sum one; it does not exist. This is only the strict-splitting test in this occurrence model, not a physical coherence obstruction or a newly chosen parity.

## 7. Exact location inside the existing spatial kernel

For Gamma equal to Sigma or Delta, take the subspace of the earlier cubical kernel with cells `square(H,F)` for `H subset F` and `F in Gamma`. The native cubical subspace has 53 cells, and the short-face cubical subspace has 65 cells. Both are literal subcomplexes of the 215-cell cubical space, reconstructed using the source's nine diagonals.

Their radial links at the common origin are homeomorphic to the geometric realizations of Sigma and Delta. Explicitly the max-coordinate-one section is carried to the sum-coordinate-one section by radial normalization. The latter is the usual realization of the corresponding simplicial face complex. No new physical simplex is adjoined.

The module-valued complexes above are the coordinate-support dualizing diagrams on these links. They are not the ordinary cellular chain groups of the contractible cubical cones. The augmentation and the face-coordinate quotient maps are essential. Contracting either cone as an unadorned space would lose the native conductor information.

Similarly, the three mixed short edges are not automatically the three long generic-Q facet states. Their labels, dimensions and coefficient modules have now been specified; a physical comparison to the long-facet quotient must preserve that data rather than infer an identification from the number three.

## 8. Polynomial naturality and symmetry

All six occurrence multiplications are represented on each face module by ordinary multiplication followed, when necessary, by the specified coordinate quotient. In a homogeneous support basis, a transition is the projection onto faces containing the newly positive coordinate. The checker verifies all 192 zero-to-positive transition arrows in the six-coordinate Boolean cube on both spatial complexes. Since every map is A-linear, the corresponding squares commute for all exponents and all compositions.

The native and short complexes carry the actual labelled D3 action: a two-step rotation and reflection exchanging the even and odd triangles. The face differential has the ordered simplex orientation, and all six actions commute with it. The spatial inclusion is strictly equivariant.

The untwisted spatial conductor class is reflection-odd, and each even-to-odd mixed edge is reflected with the corresponding sign. The six-coordinate determinant is also odd under this reflection. Reverting to the original untensored ambient dual therefore gives the previously derived reflection-even native conductor frame. This verifies the source character; it does not assign a physical comparison parity.

The quasi-isomorphism representatives and the displayed path need not individually be invariant. Their choice is not substituted for a source-prescribed equivariant physical connector. The canonical derived map is the dual of the equivariant ring quotient; the explicit face model displays that map without discarding its native endpoint attachments.

## 9. Verification and next unresolved identification

Run:

```sh
python check_marici_native_short_face_comparison.py --output marici_native_short_face_comparison_certificate.json
```

The checker performs 13,623 exact assertions. They include the native and target resolutions, the full polynomial quotient map, both derived-duality maps, the complete naturality homotopy, all 128 homogeneous quasi-isomorphism cones, the 192 occurrence transitions, both source endpoint maps and their joint homotopy, exact kernel annihilators, actual cubical containment, and all six labelled symmetries. All polynomial and homogeneous matrix reductions used for exactness are integral; no proof assistant is invoked.

The remaining identification is now between **specified** constructions. The native source has a complete, polynomial-natural occurrence-spatial map, whose three mixed-face attachments are explicit. The full support-PC comparison must connect these modules and their attaching maps to the independently graded generic-Q object and the two physical collar 2-cells, while retaining normal localization domains, external Rees determinants, and excess Tor. None of those layers is identified simply by the squarefree occurrence construction.

## Sources

[S1] `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, blob `840258522d45e450e4f1e8bb927d9aae58c75566`, at the pinned commit: native polynomial node and the two normalization augmentations.

[S2] `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`, blob `e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8`: actual labelled diagonals, noncrossing faces, and the 215-state target. The new coordinate-support quotient modules are not attributed to this source as already constructed PC stalks.

[S3] `research/voevodsky/check_two_endpoint_tate_carrier.rs`, blob `0147e2e42dafac0da7289c571cb0331b51338be1`: native endpoint labels, physical half-corridors, and the distinction between carrier data and full ringed endpoint comparison.

[M1] Kohji Yanagawa, *Stanley-Reisner rings, sheaves, and Poincare-Verdier duality*, arXiv `math/0301030`: the squarefree-module/sheaf duality framework. The integral examples here have independently constructed polynomial maps and all-degree cone proofs.

[M2] Stacks Project, *Hom complexes*, tag `0A8H`: cochain-map and comparison-homotopy conventions. Stacks Project, *Local cohomology*, tag `0952`: derived support and the full Cech complex.

Preceding project artifacts: `marici_native_conductor_dual_endpoint_attachment.md` and `marici_cubical_supported_dual_kernel.md`. Their distinctions between graded duals, polynomial-linear duals, and full supported-Verdier functors remain in force.
