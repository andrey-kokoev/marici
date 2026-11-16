# Reflected Simplex Trees, Return Residues, and Green Coherence

**Consolidated research note — 9 November 2026**  
**Programme:** Marici; simplicial composition and reflection; exploratory relation to Ramsey numbers.  
**Status:** Existing formal source results plus exact finite constructions and model counterexamples. The stage computations were rerun for this consolidation. No new native generator, formal proof, or Ramsey theorem is claimed.

## 1. Problem and current result

The starting conjecture was that a simplex tree **R** forces an opposing tree **B** by point reflection, while a third, balancing structure **G** connects their endpoints and makes the total space coherently triangulated. The investigation has clarified that this cannot yet be stated as one theorem: the objects called R, B, and G have appeared in three different carriers.

1. **Native Marici source:** directed labeled occurrences and retained execution histories. Here a candidate green object begins as a **comparison boundary** between parallel histories, not as a spatial simplex.
2. **Geometric/Δ-complex completions:** reflected filled triangles and mixed 2-cells, under additional closure or embedding assumptions. Here G denotes actual faces.
3. **Independent-operation configuration spaces:** routes, subsets, and their order complexes. Here G denotes simplices representing intermediate execution states, not a comparison of distinct retained histories.

The strongest source-relative result is this: **the actual six-arrow seed determines a nontrivial return loop and corresponding reflected green discrepancies; it does not supply a filling of those discrepancies.** If the red and blue triangles are *additionally filled*, both green comparisons reduce to the single question of canceling the return loop. In a specified reflection-equivariant group-effect model, this obstruction is the inverse square of the return operation. It may vanish, be central and nontrivial, or be noncentral.

Consequently, the research target is no longer “find the triangulation.” It is **derive an admissible comparison, residue, or obstruction from the retained source operations, with correct behavior under reflection and continuation**, then investigate whether a spatial triangulation follows.

## 2. The frozen six-arrow source

The actual endpoint table has four vertices and six directed, independently labeled occurrences:

```
AB : A → B       BC : B → C       CA : C → A
AD : A → D       DB : D → B       BA : B → A
```

The two triangles are directed cycles `AB·BC·CA` and `AD·DB·BA`. At the native source level these are **cycles, not filled 2-simplices**. The occurrence `BA` is not stipulated to be the inverse of `AB`; reversing a geometric path is different from supplying an independently labeled source occurrence. Histories are retained even when they have the same endpoint or identical output under an interpretation.

The two basic parallel-history pairs are

```
p = AB          q = AD·DB        : A → B
r = BA          s = BC·CA        : B → A.
```

The repository proves `p ≠ q` and `r ≠ s` as free retained histories. In the free geometric realization it also proves that the candidate faces identifying these pairs do not exist. `TypedGeneratorLayers` retains and composes finite histories; composition or equality in the original witness relation requires separately admitted structure. `NativeTableRules` comparison constructors require the relevant equivalence and marked-value comparison among their inputs; they do not infer either from common endpoint labels.

The free geometric realization is homotopy equivalent to a bouquet of three circles. Its graph has `V=4`, `E=6`, `π₁=F₃`, `H₁=Z³`, and no 2-cells. It also has **no pair of different length-two directed paths with the same ordered endpoints**: the ten length-two paths occupy distinct ordered endpoint pairs. Therefore a primitive commuting two-step diamond is not present in this unchanged source.

These are already established source-level boundaries, not new results of the present finite enumeration.

## 3. Reflection exists; the based return is not involutive

The directed graph has exactly one nonidentity automorphism:

```
ρ: A ↔ B,   C ↔ D;
   AB ↔ BA, BC ↔ AD, CA ↔ DB.
```

It is an involution on occurrences and can be realized by point reflection in a chosen planar embedding. Such an embedding is a **model choice**, not a metric produced by the source.

In the formal groupoid completion, inverse paths are available for geometric bookkeeping, without replacing `BA` by `AB⁻¹`. The two green **boundary loops** are

```
δ_A = AB · (AD·DB)⁻¹,
δ_B = BA · (BC·CA)⁻¹.
```

Let the following loops be based at A:

```
x = AB·BC·CA,
y = AD·DB·AB⁻¹,
z = AB·BA.
```

Then `π₁=F(x,y,z)`. In this basis `δ_A=y⁻¹` and `AB·δ_B·AB⁻¹=z·x⁻¹`, so neither vanishes in the free realization.

Because ρ exchanges the basepoints A and B, transport its action back to A using the specific edge `AB`:

```
Φ(w) = AB · ρ(w) · AB⁻¹.
Φ(x)=z·y,       Φ(y)=x·z⁻¹,       Φ(z)=z,
Φ²(w)=z·w·z⁻¹.
```

Thus ρ is strictly involutive as an unbased graph symmetry, but the chosen **based** action squares to an inner automorphism carried by the retained return `z`. No canonical nullhomotopy of `z` is supplied. A different basepoint transporter changes the representative of this discrepancy; it does not turn a nontrivial loop into a source-provided filler.

This is a generated, reflection-compatible **obstruction boundary**, not a green 2-cell.

## 4. What follows if R and B are declared filled

Make the extra assumption that the red and blue cycles bound 2-cells:

```
R : AB·BC·CA  ≃ 1,
B : AD·DB·BA  ≃ 1.
```

Then `AD·DB ≃ BA⁻¹` and `BC·CA ≃ AB⁻¹`. Pasting and cancellation give an equivalence of **existence obligations**:

```
AB ≃ AD·DB     ⇔     AB·BA ≃ 1,
BA ≃ BC·CA     ⇔     AB·BA ≃ 1.
```

This is not equality of the original occurrence histories or strict identification of spaces of possible comparison witnesses. Both candidate green faces are governed by the return loop `z=AB·BA`.

Preserve all six distinct 1-cell occurrences. The oriented candidate faces are

```
∂R  = AB + BC + CA,
∂B  = AD + DB + BA,
∂G₁ = AD + DB − AB,
∂G₂ = BC + CA − BA.
```

Their boundary cancellation is exact:

```
∂R − ∂B + ∂G₁ − ∂G₂ = 0.
```

With the conditions **(i)** use only these six 1-cells, **(ii)** use distinct simple triangular cycles, **(iii)** every edge meets exactly two triangular 2-cells, and **(iv)** all vertex links are connected circles, the two green faces are the unique additional triangles. The result is a closed orientable Δ-complex with `V=4`, `E=6`, `F=4`, Euler characteristic `2`, hence `S²`. The cellular reflection is free and its quotient is `RP²`.

| Attached 2-cells | π₁ | H₁(Z) | H₂(Z) |
|---|---|---|---|
| None | `F₃` | `Z³` | 0 |
| R, B | `Z` | `Z` | 0 |
| R, B, G₁ | 1 | 0 | 0 |
| R, B, G₁, G₂ | 1 | 0 | `Z` |

The first green face kills the surviving loop; the second, reflected green face creates a 2-dimensional fundamental cycle. A 3-cell filling that sphere is still another operation.

**Carrier warning:** This is a Δ-complex, **not** a four-vertex abstract simplicial complex: `AB` and `BA` remain distinct edges with the same unordered endpoints. If instead they are identified as two orientations of one geometric edge, R and B form a disk and a tetrahedral-sphere completion requires the additional edge `CD` and two further triangles. That is a different model. Neither carrier identification is a consequence of the source incidence alone.

## 5. The return-square theorem in a specified effect model

To decide whether the green defects **vanish**, an effect interpretation must be chosen. One exact class has a common group-torsor fiber at every vertex, with reflection transporting the fibers trivially in these coordinates and assigning identical group labels to reflected occurrence pairs:

```
AB = BA = a,    BC = AD = b,    CA = DB = c.
```

Write products in path-execution order. If the red and blue triangular holonomies are flat, then

```
abc = bca = 1  ⇒  bc = a⁻¹.
```

With the orientation `G₁: AD·DB·AB⁻¹` (and its reflected mate), the green holonomy and return are

```
κ_G = bc·a⁻¹ = a⁻²,        return = a².
```

**Conditional theorem.** In this group-effect model, flat green closure occurs if and only if `a²=1`. Reflection, reversible group actions, associativity, and red/blue flatness **do not imply** `a²=1`.

For a finite group H, there are `|H|²` red/blue-flat assignments and `|H|·#{a∈H : a²=1}` also-green-flat assignments. The finite check obtained:

| H | R/B-flat | G-flat | G-obstructed |
|---|---:|---:|---:|
| `C₂` | 4 | 4 | 0 |
| `C₄` | 16 | 8 | 8 |
| `S₃` | 36 | 24 | 12 |
| `Q₈` | 64 | 16 | 48 |

For `Q₈`, choose `a=i`, `b=j`, `c=−k`. Both R and B close, while the return is `−1` and `κ_G=−1`. This is a nonzero **central** residue, stable under conjugation. More generally `a²∈Z(H)` if the projected return element `aZ(H)` is an involution; centrality is **not** automatic. For example, an order-three element of `S₃` can give a noncentral square.

In other equally reversible, reflection-equivariant effect models, the defect can be zero or nonzero even before declaring R/B flatness. Therefore there is no interpretation-independent strict green filling in the unrestricted class. The generated loop/holonomy is a well-defined diagnostic **relative to its declared carrier**; it is not a new native Marici witness.

## 6. Alternative translation: independent branches and route spaces

For a separate model, assume `n` independent operations, every partial subset of operations is admitted, and the result of composing them depends only on that subset. The order complex of the full Boolean lattice gives a canonical staircase triangulation of the `n`-cube: 2 triangles for `n=2`, 6 tetrahedra for `n=3`, 24 four-simplices for `n=4`. Complementation reverses chains and realizes point reflection.

Remove the initial and terminal subsets. The resulting order complex `K_n` has vertices the nonempty proper subsets of `[n]` and simplices their strict-inclusion chains. It is the known Coxeter complex of type `A_(n−1)`, a triangulated sphere `S^(n−2)` with `2^n−2` vertices and `n!` maximal simplices. Complementation is antipodal reflection:

| n | Vertices | Maximal simplices | Topology |
|---|---:|---:|---|
| 3 | 6 | 6 | `S¹` |
| 4 | 14 | 24 | `S²` |
| 5 | 30 | 120 | `S³` |
| 6 | 62 | 720 | `S⁴` |

Designating an operation `a` gives an explicit decomposition by routes with `a` first (R), last (B), or interior (G). For `n=4` these contribute 6, 6, and 12 maximal triangles, respectively. R and B are disks and G is an annular collar; together they triangulate `S²`. Adjacent swaps of independent operations generate all routes from the initial family.

**Limit:** This is a theorem about **route-state incidence**, not a rule that produces a comparison 2-cell between retained Marici words. Initial pairwise diamonds alone do not guarantee a joint three-operation state. Dependencies produce balls or obstruct complement closure. Consistent central comparison signs can remain nonunique even when the route complex closes. The original six-arrow seed has no primitive adjacent-swap diamond, so this generator cannot simply be declared native.

## 7. Geometric balancing tests and rejected shortcuts

Other finite constructions constrain possible spatial readings, but their selection conditions were supplied externally.

- **Six antipodal vertices:** for R and B the two opposite triangles on `±e₁,±e₂,±e₃`, reflection plus abstract closed-sphere incidence admits ten labeled completions. Requiring a straight embedded realization at those specified points eliminates the nine with edges passing through the center and selects the octahedral boundary. The embedding assumption is extra.
- **Branching four-triangle R:** with a reflected copy B and a prescribed six-panel connecting strip, eight reflection-invariant diagonal choices give spheres. Exactly one gives vertex degree five everywhere, producing the icosahedral graph. Uniform degree five was imposed, not derived from a coherence generator. The corresponding four-triangle chain has no uniform-degree completion in that strip model.
- **Graph-tree requirement:** a reflection-invariant green graph-tree on the boundary of a centrally symmetric convex polytope is impossible: an invariant finite tree has a fixed vertex or edge, forcing a fixed point at the reflection center, which is outside the boundary. G may be a higher-dimensional coherence complex with cycles.

The icosahedron's appearance does **not** construct the Poincaré homology sphere. `Σ(2,3,5)=S³/I*` uses a binary icosahedral group action not derived by the R/B/G rules. The antipodal quotient of `K₅≈S³` is `RP³`, not that homology sphere.

## 8. Ramsey R(3,7): evidence and missing translation

The established result is `R(3,7)=23`. The previous Ramsey-side work examined a 21-vertex graph on `Z/21` with edges at offsets `±3,±4,±5`, and sampled three 22-vertex extremal graphs. The 21-vertex graph has 63 edges and 399 five-cycles. Filling **all** five-cycles kills `π₁` but yields 399 incident 2-cells, not a manifold; its integral/finite homology does not resemble the Poincaré sphere. The three tested 22-vertex samples likewise gave trivial fundamental groups after filling all pentagons. This is a sample, not a check of the full 191-graph catalog.

The earlier two-field `SL(2,Z)` construction has two 60-step cycles sharing four vertices; its selected rotation system gives a sphere with face lengths `6,6,54,54,60,60`, not pentagons. Neither construction supplies a canonical source-admitted green filler.

Crucially, **no translation has been proved** between reflected R/B/G simplex incidences and the complementary *pair-edge colors* in Ramsey's theorem. The appearance of 3, 5, 7, 12, 20, 24, or 120 in the models is not evidence of such a translation. Therefore nothing here proves, predicts, or explains the threshold 23.

## 9. Revised conjecture and immediate discriminator

The usable conjecture is conditional and typed:

> Given a retained incidence source `S`, a source-admitted involution `ρ`, and two parallel admitted histories `p,q`, there is a locally generated **coherence response** that retains both histories and returns either a comparison cell, a transportable nonzero residue, or an obstruction. It is equivariant under reflection and natural under every source-admitted continuation. Spatial closure, if any, is derived from these responses rather than assumed.

The open question is **what native admission rule determines that response**. A generator that always declares `p=q` is contradicted by the existing free-source obstruction. A generator that always returns a formally named defect, without a source-authorized effect or higher-witness interpretation, merely renames the boundary and does not solve the problem.

The highest-value next theorem is an **admissibility/transport theorem for the retained return** `z=AB·BA`:

1. Define the actual continuation contexts in the source and the types of allowed response witnesses.
2. Determine whether the return has a source-defined involutive effect, a central square, or a noncentral obstruction; derive this without selecting a convenient representation after observing the outcome.
3. Show that reflection transports the first green response to its mate and that mixed pasting is coherent, with histories intact.
4. Extend to the smallest branching source *only after* the first comparison is produced, and then test confluence under different orders.
5. If a spatial realization follows, compute links, homology and higher-cell attachment; only after an explicit incidence-to-coloring functor exists should `R(3,7)` be tested again.

The test must accept a negative outcome: perhaps no such native generator exists under the frozen six-arrow grammar. In that event, the exact missing constructor or admissibility premise is itself the result.

## 10. Evidence, provenance, and formal status

The consolidated finite checks were rerun with the original stage scripts on 2026-11-09:

```
python ramsey_g_attack/first_critical_pair.py
python marici_coherence_stage2/source_pair_audit.py
python marici_coherence_stage3/check_stage3_defect.py
python marici_coherence_stage4/reproduce.py
python marici_coherence_stage5/stage5_reflection_return_obstruction.py
```

These are exact finite graph, group, boundary, and incidence checks, not new Cubical Agda compilations. Each stage has its original research note and, where applicable, JSON receipt in its sibling directory. Formal source findings below were checked in the pre-existing Marici work; this consolidation did not modify the repository.

**Primary source records**

- [ActualSeedEndpointTable.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/ActualSeedEndpointTable.agda)
- [SeedSeamPathComparisonBoundary.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedSeamPathComparisonBoundary.agda)
- [SeedFaceObstruction.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedFaceObstruction.agda)
- [SeedFirstReturnActions.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedFirstReturnActions.agda)
- [TypedGeneratorLayers.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/TypedGeneratorLayers.agda)
- [Source graph free realization](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/source-graph-free-realization-v1.md)
- [Seed-native promotion binding gate](https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-native-promotion-binding-gate.md)
- [Phase selection from coherence](https://github.com/andrey-kokoev/marici/blob/main/research/nima/phase-selection-from-coherence.md)
- [Source incidence selects the coherence nerve](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/source-incidence-selects-the-coherence-nerve.md)
- [Codimension-one pairing note](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/marici_codim_one_pair_research_note.md)

**Overall disposition:** A nontrivial source-derived *boundary/residue* is available; a universally generated green *filler* is not. Conditional green closure can produce a sphere, and independent-route incidence can produce canonical spheres, but neither is yet a native solution or a Ramsey mechanism.
