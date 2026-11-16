# Boundary Conservation, Six-State Ambiguity, and Apex Symmetry in Marici

Scope: exact combinatorics and finite-group theory, with an explicit source-admission boundary. The additional fifth vertex, complete spoke incidence, mod-two chains, and the five-vertex symmetry action are **not derived** from the frozen six-occurrence native seed. The `NativeSpokeIndexIndependence.agda` candidate is *not freshly typechecked*: Agda is unavailable in this runtime.

## 1. Canonical parity closure is too weak

Let `V` be any `n`-element vertex set, `z` a fresh vertex, and let `c` be an F2 1-chain on the complete graph on `V`. Write `d c` for its odd-degree 0-chain and `z*(d c)` for the star 1-chain having an edge `zv` for each odd-degree vertex `v`. Define

`kappa_z(c) = c + z*(d c)`.

This is the **unique** 1-cycle on `V ∪ {z}` whose restriction to edges inside `V` is `c`. Indeed, on each old vertex `v`, vanishing degree parity determines its spoke coefficient to be `(d c)(v)`; parity at `z` then vanishes because `d c` has even total cardinality. Hence the restriction map is a natural linear isomorphism

`Z_1(K_(n+1); F2) ≅ C_1(K_n; F2)`.

For `n=4`, `dim=6` and all 64 labeled two-colorings of K4 extend uniquely to *complementary Eulerian* subgraphs on K5. Only twelve give complementary C5/C5 (six unordered). A monochromatic triangle may survive unchanged. This is an independence theorem: boundary conservation alone does not select the Ramsey-admissible family.

## 2. Complete classification of unordered local alternatives

On K5, the 64 Eulerian labeled edge subsets comprise:

| red Eulerian edge subset | count |
|---|---:|
| empty | 1 |
| triangle | 10 |
| 4-cycle | 15 |
| 5-cycle | 12 |
| complement of 4-cycle | 15 |
| complement of triangle | 10 |
| complete K5 | 1 |

Quotienting by swapping the two complementary bundles yields 32 unordered pairs. The S5-orbits are exactly `1,6,10,15`, organized by unordered edge-count pairs `(0,10),(5,5),(3,7),(4,6)`. Therefore any S5-invariant **six-element** subset is necessarily the six complementary C5 pairs. The same orbit census holds under A5, so A5-invariance already suffices.

## 3. Sharp ambiguity under the old four-vertex A4 action

Mark the new apex `z`. Restrict to global A4 permutations of the four old vertices, fixing `z` (the triangle permutations available as global vertex actions, **not** automorphisms of the original six directed occurrences). The 32 unordered Eulerian pairs split into A4-orbits of sizes

`1,3,4,6,6,12`.

There are exactly two A4-invariant six-element subsets:

- The six complementary C5 pairs (the Ramsey target).
- The six pairs `{triangle(z,u,v), K5 \ triangle(z,u,v)}` as `{u,v}` runs over old-vertex pairs (the hostile alternative).

Both are transitive A4-sets isomorphic to `A4/<s>` for `s=(AB)(CD)`; the stabilizer of a suitable point is `<s>`. Thus the previous source six-state coset, parity, complementarity, six-state count, and old-vertex A4 covariance do **not** select the pentagon family.

Adjoin one apex-moving 3-cycle `t=(A B z)`. Exact group enumeration gives `<A4,t>=A5` (60 elements). The hostile six apex triangles are not invariant under `t`; the C5-pair family is. One apex-moving triangle operation is sufficient at the abstract group-action level, but **its native history-level realization is not established**.

## 4. The existing pentachoron gives a positive *target* control, not source authority

`research/voevodsky/common-geometric-assembly-six-hypothesis-audit.md` verifies that the regular five-vertex electron pentachoron has 60 orientation-preserving symmetries (A5), while those preserving the marked ABCD attachment facet form A4 (12). It also exhibits distinct equidistant fifth-vertex extensions of the same regular base tetrahedron: squared fifth-to-base edge lengths `s=4` and `s=8` both preserve the base A4 action, but only `s=8`, with every edge length squared equal to 8, yields full apex-moving A5 isometries. This is a concrete geometric independence control.

The fifth point/regular-pentachoron metric is supplied target data in that research. None of this establishes a WG operation constructing the point, the necessary metric, or the A5 action from the original six-arrow source.

## 5. Native E/Pi-rules do not impose closure on freely chosen indices

In `research/nima/agda/WholePackageResolution.agda` the native `E-rule` takes `(I,F,i)` and derives `E-package I F i` from actual derivations of `F(j)` for every `j:I`. For `I = Bool^4` and the constant family `F(i)=pointQ A`, every branch is derivable from the existing seed `root A`. Therefore for *each* of the 16 masks `eps`, the native derivation

`apply (E-rule Bool^4 F eps) (lambda _ -> root A)`

exists and stores its chosen mask. For the sample old Hamiltonian path `C-A-B-D`, the closure mask is only `(0,0,1,1)` (red spokes at C and D). An all-zero mask is natively **index-admitted** but violates closure. The candidate `NativeSpokeIndexIndependence.agda` expresses the corresponding contradiction to a blanket `Resolve -> Closed` assertion. It is not a proof that the *bad mask denotes an actual admitted apex attachment*: the apex/spoke semantics are absent from this constant family. Rather, it proves the native E/Pi constructors impose no such law on their arbitrary supplied indices without an explicitly structured extension predicate.

## 6. Overlap holonomy separates parity from Hamiltonicity

For the six five-vertex facets `W_i` of K6, take local fibers `X_i=Z_1(K5;F2)`, of size 64 (labeled). Each restriction to a common four-vertex overlap is bijective by the star-cone theorem, so canonical overlap transports exist. Every ordered triangular loop acts as a transposition of two vertices of the starting K5. A transposition fixes sixteen of the 64 Eulerian cycles; the group generated by all such loops is S5, whose common invariant cycles are exactly `empty` and `complete K5`. Consequently there are **two** compatible global labeled sections, both monochromatic. On the unordered 32-state quotient these counts become eight fixed per triangle and one global section.

Restricting instead to the twelve labeled C5s (six unordered complementary pairs) leaves no fixed state for any triangular loop and no global section. Therefore *parity closure alone does not produce the Ramsey obstruction*, even though it defines the same overlap-transport mechanism. The obstruction depends on selecting a proper local orbit of admissible states.

## 7. Next native theorem

Construct or refute a provenance-preserving adapter from the original A4-marked six-occurrence seed to the existing regular-pentachoron A5 action. Required concrete fields are: (i) a source-admitted fifth-vertex attachment and four spokes, (ii) transport of all original occurrence histories under an apex-moving three-cycle, (iii) native proof that the continued local alternative family has exactly six unordered Eulerian states, and (iv) compatibility of restrictions and selected comparison witnesses. Successful realization would identify the C5/C5 family by the orbit theorem without specifying triangle-free coloring. Failure must name the first absent typed witness.

## Verification

Reproduce with `python /mnt/data/marici_boundary_conservation_independence.py`. Exact finite tests include all 64 K4 partitions and all 16 possible spoke masks per partition, 120 ordered triangular overlap loops on 64 states, S5/A5/A4 orbit enumerations, source stabilizers, and the two source-compatible six-state countermodels. Result: `marici_boundary_conservation_independence_results.json`.

Relevant upstream sources:

- `research/nima/agda/ActualSeedEndpointTable.agda`
- `research/strominger/agda/NativeExtensionFamilyAudit.agda`
- `research/strominger/agda/SourceIndexedExtensionFamilies.agda`
- `research/nima/agda/WholePackageResolution.agda`
- `research/nima/agda/WholePackageSigmaPi.agda`
- `research/voevodsky/common-geometric-assembly-six-hypothesis-audit.md`
