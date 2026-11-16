# Stage 2 — Source-level reflection, comparison, and residual closure

Date: 2026-11-09. Status: exact graph/chain calculations rerun; source-relative Agda theorems cited from existing Marici repository. No new Agda compilation or native WG witness constructed.

## Frozen source

Four vertices `A B C D`; directed occurrences `AB BC CA AD DB BA`. An occurrence and its oppositely oriented geometric edge are not automatically inverse operations; source transpose preserves the occurrence label.

Existing [SeedSeamPathComparisonBoundary.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedSeamPathComparisonBoundary.agda) proves both parallel histories remain distinct:

- x0=`AB`, x1=`AD;DB` : A→B
- y0=`BA`, y1=`BC;CA` : B→A.

Existing [SeedFaceObstruction.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedFaceObstruction.agda) and [SeedNativePromotionBindingGate.agda](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedNativePromotionBindingGate.agda) prove the candidate first faces are absent in the **free seed realization**. The latter excludes the attempted source-preserving filled-tetrahedron bridge, not every possible interpretation or enriched seed.

## New exact finite audit (relative to these pre-existing results)

The directed graph has precisely two automorphisms: identity and `rho` interchanging A↔B, C↔D, and
`AB↔BA`, `BC↔AD`, `CA↔DB`. It has a planar point-reflection realization, e.g. A=(1,0), B=(-1,0), C=(0,1), D=(0,-1). This geometric realization is a convenient coordinate model, **not a derived metric/geometry**. Its nontrivial automorphism exchanges the forward and return parallel-history pairs.

The reflection alone does NOT generate a filler. A reflection-equivariant edge-label functor to the one-object groupoid `Z/2` sends AB and BA to 1, and every other edge to 0. Then `AB` and `AD;DB` evaluate differently, as do `BA` and `BC;CA`; the map even respects an OPTIONAL relation identifying BA with inverse AB (because 1=-1 modulo 2). This is a concrete countermodel to deriving any forced equality from endpoints+reflection+reversibility alone.

## Based reflection produces a canonical residual loop

Work in the formal groupoid completion of the graph; this adds formal inverses for *path bookkeeping* and does not identify `BA` with inverse `AB`. Choose the source occurrence `s=AB` to transport the reflection of loops at B back to basepoint A. The three free generators are

- `p = AB;BC;CA`
- `q = AD;DB;AB^-1`
- `t = AB;BA`.

The based automorphism `Phi(w) = s rho(w) s^-1` satisfies, exactly:

```text
Phi(p) = t q
Phi(q) = p t^-1
Phi(t) = t
Phi^2(w) = t w t^-1
```

This follows because `rho` exchanges A and B and `s rho(s)=AB;BA=t`. The graph involution is strict, but its chosen *based* lift squares to inner conjugation by the nonempty return loop `t`. This is the precise residual that the proposed green coherence would have to account for if it seeks a strict equivariant basepoint. It is not automatically a geometric 2-cell or selected nullhomotopy. Changing `s` changes the representative of the residue.

The Z/2 grading above is stable under *every* pre- and postcomposition because the difference of path grades cancels the common prefix and suffix. Thus reversal, reflection and continuation invariance do not force zero discrepancy.

After adding the two hypothetical comparison cells, `q=1, p=t`, leaving `t` alone. Then `Phi` acts as identity on the residual abelian group `Z`; the loop `t` still survives. Requiring a **homotopy-fixed basepoint** (a specified nullhomotopy of `s rho(s)`) is stronger than requiring an involutive action on this π1.

## If we supply two green 2-cells hypothetically

Attach a cell along each comparison loop, represented by `AB = AD;DB` and `BA = BC;CA` in the groupoid completion. Keep `AB` and `BA` distinct occurrences. These 2-cells are *additional premises*, not generated source cells.

The resulting cellular complex has V=4, E=6, F=2, chi=0; H1(Z)=Z, H2=0, and π1=Z. Direct presentation: the free underlying graph has based generators `p=AB;BC;CA`, `q=AD;DB;AB^-1`, `t=AB;BA`. The two relations impose `q=1`, `p=t`, leaving free generator `t`.

A further, independent relation `BA = (AB)^-1` kills `t`. At the 2D geometric level it identifies the two opposite directed AB occurrences as one unoriented edge; the two triangular cells then form a disk (V=4, E=5, F=2, chi=1, H1=0). This is still not a closed manifold.

**Simplicial typing:** Since AB and BA are two distinct source occurrences with the same unordered endpoint pair, the source is not itself an abstract simplicial complex on four vertices: such a complex permits only one edge for {A,B}. Treat it as a directed graph / free category / simplicial set (or triangulate a refinement) until an admissible occurrence-sensitive construction is specified. The two 2-cells above are CW/Δ-type attachments, not automatically abstract simplices with separate AB and BA edges.

These are calculations in the optional cellular/groupoid interpretation. They do not identify source history records or prove a physical/native G operation.

## Conditional reduction: one comparison generates the reflected comparison

Let `X(v)` be an effect/payload carrier at each source vertex; let each occurrence `e` act by `F_e:X(source e)→X(target e)`. Suppose *additional* data give an involutive equivariance family `J_v:X(v)→X(rho v)` and commuting action squares `J_target(e) ∘ F_e = F_rho(e) ∘ J_source(e)`.

Then **one supplied pointwise witness**

`alpha(a): F_AB(a) = F_DB(F_AD(a))` for `a:X(A)`

canonically transports to the reflected return witness

`beta(b): F_BA(b) = F_CA(F_BC(b))` for `b:X(B)`.

Proof: apply `alpha` at `J_B(b)` and map the resulting equality through `J_B`, using action equivariance and `J_A J_B=id`. The existing [SeedFirstReturnActions](https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-first-return-actions.md) then derives the mixed comparison square from `alpha` and `beta`, retaining their histories. Thus under *rho-equivariant effect semantics*, the initial independent witness count drops from two to one; the one remaining witness is still not generated by the source.

Negative control: set every `X(v)=Z/2` and every `J_v=id`; let `AB` and `BA` toggle the bit, all other occurrences act as identity. The actions are rho-equivariant and reversible, but `F_AB(a) ≠ F_DB(F_AD(a))` for every a. So even source reflection + equivariant payload dynamics does **not** force the initial `alpha`. The all-identity action model admits it. Both models preserve the actual source incidence.

## Minimal obligation now isolated

We require an **admissibility predicate and comparison constructor on retained source histories**, with outputs that may be a new higher cell, a nontrivial residue, or an obstruction. Candidate interface:

- `admit(s; p,q)` : source-authorized witness that parallel histories p,q can be jointly compared;
- `compare(s; p,q,admit)` : retains original paths plus a typed comparison;
- `extend(c; h)` : transports a comparison through each source-admitted continuation h;
- `rho-compat` : relates comparison on p,q to that on rho(p),rho(q);
- `critical-pair` : comparison of three extensions is independent of pairwise composition order up to a retained higher witness.

Crucially, this must NOT assert `p=q` in the original free history type. Under the free realization that is already disproved. The first discriminating target is a **source-derived rule for when comparison is admitted**, not merely new syntax storing a path pair or assigning a generic zero residue.

## Prior related work

- [source-graph-free-realization-v1.md](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/source-graph-free-realization-v1.md): free seed is a bouquet of three circles; previous H1-rank controls.
- [seed-first-return-actions.md](https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-first-return-actions.md): typed retained append actions and conditional mixed square from supplied α,β.
- [marici_codim_one_pair_research_note.md](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/marici_codim_one_pair_research_note.md): pair match, nonunique fillers, K(Z/2,2) countermodel.
- [seed-native-promotion-binding-gate.md](https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-native-promotion-binding-gate.md): formal nonexistence of first proposed face under frozen free interpretation.

Reproduction: `python source_pair_audit.py` (standard library only). No repository files modified.
