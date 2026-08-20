# Loaded Fold-Kernel Generic Top and the Endpoint Connector Extension Gate

Date: 2026-08-15  
Status: proved only in the explicitly labelled finite fold-kernel and
double-Rees coefficient model. Normalization/spatial entry-143 provenance,
the endpoint butterfly, and physical parity remain unconstructed. No graph
admission is claimed.

## The saturated fold kernel

Let \(G\) be the entry-95 conductor normal-link fold and put
\(K=\ker G\). In the invariant labelled basis,

\[
K_2=\mathbb Z\langle k_2\rangle,\qquad
K_1=\bigoplus_{D\in\{14,03,25\}}\mathbb Z\langle k_{1,D}\rangle,
\qquad
d k_2=\sum_D k_{1,D}.
\]

Entry 95 proves that this kernel is saturated, admits degreewise integral
right inverses in the ambient fold sequence, and has no integer torsion. Its
homology is the integral \(A_2\) contact lattice. These facts concern the
carrier fold and do not choose a spatial normalization-sheet realization.

## The finite loaded generic-top map

For every long road \(D\), let \(p_D\) be its labelled target state and
let

\[
y_D=X_D\otimes u_D^\vee
\]

be the line-valued long-normal loading. Let \(T\) be the single generic top
with the shifted target convention

\[
dT=-\sum_D y_Dp_D.
\]

Then the labelled homomorphism

\[
\Phi:K\longrightarrow Q[1],\qquad
\Phi(k_2)=-T,\qquad
\Phi(k_{1,D})=y_Dp_D
\]

is a chain map. Indeed,

\[
d\Phi(k_2)=-dT=\sum_D y_Dp_D
=\Phi\left(\sum_Dk_{1,D}\right)
=\Phi(dk_2).
\]

The coefficient \(-1\) on \(T\) and the three primitive line
loadings have greatest common divisor one, so the map is primitive and adds
no integer torsion. Rotation cyclically permutes the three roads and fixes
the generic top. Reflection reverses the oriented fold top and the normal
cap; the established road-orientation twist restores covariance. Thus the
finite labelled map is \(D_3\)-compatible with the declared reflection
character.

This theorem uses \(y_D\) as the tensor \(X_D\otimes u_D^\vee\), not
as a global inversion of \(u_D\).

## Four-flip kernel holonomy and spectators

In the explicitly labelled D03 double-Rees kernel square, all four
orientation-normalized relative-normal caps are strict chain maps. Their
common labelled spectator packets have identity counits, all four finite
Beck--Chevalley squares commute, and their cyclic holonomy is \(+\mathrm{id}\).
The primitive product-Rees top has boundary

\[
(1,1,-1,-1),
\]

which supplies the four-edge coefficient coherence. Endpoint-exclusive
normal and double-overlap grades are integrated out. The common spectator
packet retains exactly one \(\operatorname{Tor}_0\) and one
\(\operatorname{Tor}_1\) grade; no higher Tor or integer torsion appears.

These identity counits and line loadings are proved only as labels and maps
in the finite kernel model. They are not the branch counits or stalkwise
corestrictions of a constructed normalization/spatial correspondence into
entry 143.

## Provenance boundary

The paired-incidence certificate proves the three projective labels,
branch-incidence equations, generic \(\mathbb P^2\), deep
\(\mathbb P^3\), and primitive torsion-free incidence kernel. It does
not construct the Rees normalization, global cdh descent, or a ringed Gysin.
The four-flip certificate proves finite kernel holonomy, cap signs, spectator
Tor, and top coherence, but explicitly does not realize these kernels by
entry-143 spatial six-functor maps.

Accordingly \(\Phi\) is a canonical finite loaded map, not yet the
generic-top arrow of the physical endpoint/\(Q\) object. In particular, its
symbol \(T\) must not be identified with a based physical \(q_\Sigma\)
class merely by matching names or coefficients.

## The endpoint connector extension gate

Let \(\pi\) denote the source projection, \(a\) the desired
normalization-sheet/road map, \(i_{\mathrm{road}}\) the target road
inclusion, and \(\delta_E\) the target connecting morphism. Extending the
finite map to a morphism of endpoint triangles requires an actual homotopy
\(h\) satisfying

\[
\boxed{
d_{\operatorname{Hom}}h
=i_{\mathrm{road}},a,\pi-\delta_E\Phi.
}
\]

Neither side is currently identified inside one normalization-provenanced
mixed-variance category. The following data remain unconstructed:

- the spatial realization of \(K\) and \(\Phi\) on every literal
  entry-143 \([S,H]\) stalk ring and corestriction;
- the collar-to-Alexander--Whitney comparison matrices;
- both endpoint columns, including their branch/conductor attachment and
  shared-counit comparison cells;
- the three-road overlap, top, and reflection coherences;
- the normalization-provenanced generic \(Q\) source arrow.

The finite identity counits do not solve this equation: using them as the
physical endpoint columns would assume the missing spatial identification.

## Parity boundary

Until the displayed Hom equation and both endpoint columns are constructed,
the endpoint-fixed mapping fiber is uninstantiated. Therefore the physical
\(p_{\partial,Q}\), its mod-two obstruction, and its conductor Bockstein
are undefined. Neither the primitive map \(\Phi\) nor the local
\([2,1]\) cap of entry 176 selects their values.

## Falsifiers and anti-circularity

The finite theorem is falsified if the fold kernel is not saturated; if
\(dk_2\) is not the three-road norm; if the target top has a different
boundary after the declared shift; if any loading is nonprimitive; if a
four-flip shared-vertex square or top coherence fails; if reflection is not
restored by the fixed road twist; or if spectator Tor has ranks other than
\((1,1)\).

The physical extension is not established by manually identifying finite
identity counits with endpoint maps, replacing \(y_D\) by an illegal
inverse, prescribing \(h\), or declaring \(T\) based. Conversely, failure
of a future spatial extension would not invalidate the scoped finite kernel
map.

## Exact certificates

- `research/voevodsky/check_conductor_normal_link_fold.rs`, SHA-256
  `61ebadf9eb8e106c69833c912ec6667dd929547f86550d17ae440906a11f8718`;
- `research/voevodsky/check_paired_incidence_fibre_product.rs`, SHA-256
  `3061d92a43e7ac0750fbc9827e9203d21f8a555e45d4bbf9b8a7222e7e440a2e`;
- `research/voevodsky/check_d03_four_flip_kernel_holonomy.rs`, SHA-256
  `3d713865162372e0d9d3b321bc24593371ef0757e4452f42e068d904cf346a4c`.

Relevant ledger inputs are entries 95, 100, 113, 143, 164, 170, 176, and
179.

## Next experiment

Construct the two endpoint columns and collar-to-Alexander--Whitney matrices
on the literal entry-143 stalk diagram. Use them to type both terms in
\(d_{\operatorname{Hom}}h=i_{\mathrm{road}}a\pi-\delta_E\Phi\),
then solve or falsify that equation without changing \(\Phi\). Only after
the one-road triangle closes should the construction be rotated and tested
for three-road overlap/top/reflection coherence and physical parity.

## Outcome contract

~~~json
{
  "claim": "In the explicitly labelled finite fold-kernel/double-Rees model, K=ker(G) has dk2=sum_D k1_D and admits the primitive loaded chain map Phi:K->Q[1] with Phi(k2)=-T and Phi(k1_D)=y_D*p_D, y_D=X_D tensor u_D^vee. The finite four-flip caps have identity shared counits, +id holonomy, primitive top coherence, and surviving spectator Tor0/Tor1 with no torsion.",
  "status": "proved",
  "scope": "explicitly labelled finite saturated fold kernel, line-valued loadings, and double-Rees cap holonomy only; no normalization/spatial entry-143 provenance, endpoint butterfly, graph admission, or physical parity",
  "assumptions": [
    "The entry-95 fold kernel and its invariant three-road basis are fixed.",
    "The shifted target convention is dT=-sum_D y_D*p_D.",
    "Each y_D is the line-valued tensor X_D tensor u_D^vee, not a base-ring inverse.",
    "The finite four-flip labels and established road-orientation twist are retained."
  ],
  "factorization": {
    "kernel": "K=ker(entry95 fold)",
    "kernel_differential": "dk2=sum_D k1_D",
    "Phi_top": "Phi(k2)=-T",
    "Phi_roads": "Phi(k1_D)=y_D*p_D",
    "line_loading": "y_D=X_D tensor u_D^vee",
    "chain_equation": "d Phi(k2)=Phi(d k2)=sum_D y_D*p_D",
    "D3_rotation": "cyclic on roads, fixes T",
    "reflection": "covariant after the fixed road-orientation twist",
    "primitive": true,
    "integer_torsion": "none",
    "four_flip_BC_commutators": [0, 0, 0, 0],
    "finite_shared_counits": "identity",
    "cyclic_holonomy": "+id",
    "product_top_boundary": [1, 1, -1, -1],
    "spectator_Tor0_Tor1": [1, 1],
    "higher_Tor": 0,
    "spatial_entry143_realization": "unconstructed",
    "morphism_of_triangles_equation": "d_Hom h=i_road*a*pi-delta_E*Phi",
    "collar_to_AW_matrices": "unconstructed",
    "endpoint_columns": "unconstructed",
    "physical_p_partial_Q": "undefined",
    "physical_Bockstein": "undefined"
  },
  "evidence_refs": [
    "research/voevodsky/check_conductor_normal_link_fold.rs",
    "research/voevodsky/check_paired_incidence_fibre_product.rs",
    "research/voevodsky/check_d03_four_flip_kernel_holonomy.rs",
    "src/ledger/20260814-95 Conductor Normal-Link Fold and the Occurrence-Loaded Trace Boundary.md",
    "src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md",
    "src/ledger/20260814-113 Marked-Exit Tate Detector and the Mixed Boundary-Crossing Block.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-164 Paired-Incidence Descent and the Reduced cdh Vertex Connector.md",
    "src/ledger/20260815-170 Product-Rees F03 Square and the Forced Long-Normal Completion.md",
    "src/ledger/20260815-176 Central Exceptional Relative Cap and the Conditional Parity Test.md",
    "src/ledger/20260815-179 Crossing-Road Facewise Descent No-Go and the Derived Overlap Source Gate.md"
  ],
  "checker_sha256": {
    "conductor_normal_link_fold": "61ebadf9eb8e106c69833c912ec6667dd929547f86550d17ae440906a11f8718",
    "paired_incidence_fibre_product": "3061d92a43e7ac0750fbc9827e9203d21f8a555e45d4bbf9b8a7222e7e440a2e",
    "four_flip_kernel_holonomy": "3d713865162372e0d9d3b321bc24593371ef0757e4452f42e068d904cf346a4c"
  },
  "unconstructed": [
    "normalization/spatial realization on literal entry-143 stalks",
    "collar-to-Alexander-Whitney matrices",
    "both endpoint columns and connector cells",
    "solution of the morphism-of-triangles Hom equation",
    "three-road overlap/top/reflection coherence",
    "based physical mapping fiber and p/Bockstein"
  ],
  "counterevidence": [
    "Finite identity counits do not supply physical endpoint columns.",
    "Paired incidence does not construct Rees normalization, global cdh descent, or a ringed Gysin.",
    "The four-flip checker does not realize its kernels through entry-143 spatial six functors.",
    "The generic top remains unbased until the normalization-provenanced Q/source arrow is built."
  ],
  "next_experiment": "Construct both endpoint columns and collar-to-AW matrices on the literal entry-143 diagram, type and solve d_Hom h=i_road*a*pi-delta_E*Phi without changing Phi, then rotate and test three-road overlap/top/reflection coherence before evaluating physical parity."
}
~~~
