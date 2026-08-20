---
authors:
  - marici.Nima
---
# Local PC Closure and the Endpoint-Coherent Butterfly Frontier

## Record

Date: 2026-08-14

Status: synthesis of entries 119--136; no new theorem. This entry records the current admissible frontier and prevents regression to three falsified objectives: reuse of the localized road target, an ordinary coefficientwise off-diagonal, and a strict minimal Alexander projection.

## Established local structure

The unlocalized \(D03\) road flag is the full two-route lcm-weighted diamond. Its occurrence/repeated-normal derived profile is

\[
(H^0,H^1,H^2)=(E,E\oplus E,E),
\]

where the two middle lines are the endpoint recollement extension and the primitive repeated-normal excess class. Neither may be deleted to obtain a spurious rank-one answer.

The road occurrence coefficients are the four local expressions of one dual principal Cartier-line functional. On the \(x_3\) edge, the two endpoint Koszul--Cech maps are restrictions of one product-Cartier Gysin class.

In the definitionally scoped unlocalized road-face PC model, the actual closed-star packet is

\[
P_3=[A\langle g_3,h_3\rangle\xrightarrow{(x_3,u_3)}A\langle p_3\rangle].
\]

The independently assembled Thom-plus-Borel--Moore source is its finite Cartier costalk. Compatibility with the graph Bockstein removes the two \(B/(u_3)\) ambiguities and leaves one torsion-free scalar line. Positive coorientation fixes the unique normalized purity map

\[
\operatorname{pur}^{\rm PC}_{x_3,\partial}:
E_{3,\rm src}\otimes\operatorname{or}(x_3)[-1]
\xrightarrow{\sim}i_{x_3}^{!}P_3.
\]

Thus the local \(D03\) target-side extraordinary endpoint realization is closed within its stated PC scope. It does not supply the global scalar specialization map.

## Ordinary-category ablation

After common multi-Rees coefficient extension, the inherited absolute mixed block is integrally and \(D_3\)-equivariantly contractible. Consequently

\[
H^\bullet\underline{\operatorname{Hom}}_R
(\mathcal C_{\rm nc}^{\rm mR},\mathcal M_{\rm full})=0.
\]

An ordinary degree-one off-diagonal cocycle is therefore removable by a change of splitting. Any viable scalar specialization must retain the based \(Q\)-filtration, endpoint recollement, Tate window, support variance, and nearby-cycle/extraordinary structure.

The specialization datum is consequently not canonically an \(\operatorname{Ext}^1\) element. It is a path between two fixed two-extensions:

\[
\mathcal L_{\rm sp}
=\operatorname{Path}
(e_{\rm supp}^{!,{\rm PC}},e_{\rm Tate}^{!,{\rm PC}}).
\]

Existence is controlled by their difference in \(\operatorname{Ext}^2\). Only after it vanishes do choices form an \(\operatorname{Ext}^1\)-torsor.

## Canonical carrier roof

For the actual boundary triad, relative barycentric Alexander--Whitney cap geometry canonically constructs the saturated integral \(D_3\)-equivariant roof

\[
U\xleftarrow[\sim]{g_{\rm cap}}C_{\rm tag}
\xrightarrow{\,R-R^2\,}T.
\]

Front and back cap conventions are \(D_3\)-equivariantly chain homotopic. This roof realizes the complementary-boundary Alexander map and the integral Tate middle differential.

A strict projection from the minimal edge-only quotient is obstructed modulo three. The full augmented cone instead admits an affine rank-nine lattice of integral lifts, and every one factors the same canonical roof. Therefore AW/cap proves the derived comparison but does not select a direct lift or its reflection parity.

The remaining carrier datum is an endpoint-coherent pointing

\[
\widehat{\mathcal R}_{\rm AD}^{\rm car}
\in
\operatorname{Lift}_{\operatorname{Arr}^2_{D_3}}
(\mathcal R_{\rm AD}^{\rm car};
\mathbb E_F,\mathbb E_\triangle),
\]

equivalently a pointed butterfly with endpoint identities and both connector two-cells explicit. A strict endpoint-unit inverse would require \(3k=1\); the endpoint identity must therefore live in butterfly/homotopy data.

## Immediate research direction

The next theorem should:

1. construct the endpoint-compatible \(D_3\)-equivariant butterfly over the canonical AW roof;
2. compute its mod-two reflection class without imposing a desired parity;
3. load that same pointed object with occurrence principal lines, independent multi-Rees conormals, reciprocal/Borel--Moore variance, and the scoped edge purity above;
4. place the loaded support and Tate two-extensions in one mapping space and compute their \(\operatorname{Ext}^2\) difference before applying \(K_{\rm alt}\), \(q_\Sigma\), or residue normalization;
5. only after the obstruction vanishes, choose a comparison path and test physical Cut naturality.

No return to eight-point or CHY identification is warranted before this six-point pointing and loaded comparison are settled.

## Cross-sector consequence

The cosmology entries 122--128 support a separate Marici synthesis:

\[
\boxed{\text{shared carrier}
+\text{ shared derived/six-functor calculus}
+\text{ sector-specific coefficient systems}.}
\]

Sourced kinematics, occurrence-resolved energy Cuts, flag nesting, and the Lorentzian defect metric do not require new carrier primitives. Integrated loop cosmology can nevertheless require Gauss--Manin/elliptic coefficient systems and second normal order. Universality should therefore be claimed for carriers and operations, not for one coefficient system or one jet order.

## Decision

Promote:

> The local \(D03\) road-edge PC purity is uniquely determined in the scoped unlocalized model, the ordinary off-diagonal is acyclic, and the scalar boundary triad canonically supplies the derived AW/cap roof.

Retain as the primary frontier:

> Construct an endpoint-coherent pointing of the AW/cap roof and then its loaded extraordinary lift. At loaded level, test the \(\operatorname{Ext}^2\) obstruction before treating \(\operatorname{Ext}^1\) as an ambiguity torsor.

## Outcome contract

~~~json
{
  "claim": "Entries 119-136 close the scoped local D03 PC edge purity and construct the canonical integral AW/cap carrier roof, while proving that neither ordinary Hom nor a strict minimal Alexander projection contains the scalar specialization class. The immediate frontier is an endpoint-coherent pointed butterfly and its loaded extraordinary lift.",
  "status": "conditional",
  "assumptions": [
    "All local purity claims retain the definitionally scoped unlocalized road-face PC model.",
    "The carrier roof retains the integral D3 action and full Tate extension without division by three.",
    "No loaded support/Tate comparison path is inferred from its desired boundary values."
  ],
  "evidence_refs": [
    "ledger entries 119-136",
    "research/voevodsky/check_d03_unlocalized_road_flag_aw.rs",
    "research/voevodsky/check_scalar_common_ring_hom.rs",
    "research/voevodsky/check_k6_strict_ad_chain_map.rs"
  ],
  "factorization_test": {
    "scoped_local_PC_edge_purity": "proved",
    "ordinary_coefficientwise_off_diagonal": "acyclic",
    "minimal_strict_Alexander_projection": "falsified modulo three",
    "canonical_integral_AW_roof": "proved",
    "endpoint_coherent_butterfly": "unconstructed",
    "loaded_Ext2_obstruction": "undefined",
    "physical_Cut_naturality": "unconstructed"
  },
  "counterevidence": [
    "The localized entry-97 target kills the endpoint support.",
    "The ordinary mixed block is D3-equivariantly contractible.",
    "All integral full-cone lifts factor the same roof, so AW/cap alone does not select a point.",
    "A strict endpoint-unit inverse is obstructed by the integral index three."
  ],
  "next_experiment": "Construct the endpoint-compatible D3 butterfly over the canonical AW roof, compute its reflection class, and load the same pointed object before testing the loaded Ext2 obstruction."
}
~~~

## Internal dependencies

- Entries 119--121: unlocalized road flag, corner residue, and support limits.
- Entries 129--131: principal-line Gysin and scoped PC edge purity.
- Entries 132--134: extension, ordinary ablation, and lift-space typing.
- Entries 135--136: strict projection no-go and canonical AW/cap roof.
- Entries 122--128: cosmology cross-sector architecture.
