# Equivariant obstruction transfer in reflected simplex coherence

**Research note · 2026-11-09**  
**Status:** Exact finite boundary and mod-2 homology computations, plus elementary topological proofs. The source involution and face attachments are defined explicitly. The resulting topological mechanism is conditional; it does not derive the green face attachments from Marici's unfilled source.

## Research question

What prevents a locally defined coherence-completion rule from simply killing every cycle, and what does point reflection contribute to the topology of completed simplex complexes?

The source distinction remains essential: in `ActualSeedEndpointTable.agda` the six directed occurrences `AB, BC, CA, AD, DB, BA` are distinct; the endpoint data do not identify `AB` and `BA`, and do not supply 2-cell fillings. `SeedFaceObstruction.agda` supplies an explicit free-realization counterexample to an inferred green face.

## 1. Boundary generator versus filler

Let `F` be the free fundamental groupoid of the six-arrow graph; its underlying graph has V=4 and E=6, hence free fundamental group of rank 3. The candidate red and blue oriented 2-boundaries are

    r = AB BC CA,
    b = AD DB BA.

Admitting these 2-cells gives a CW complex `K_RB`. Using the spanning tree `AB, BC, AD`, the three residual loop generators may be chosen as `x=CA`, `y=DB`, `z=BA` in the usual tree-contracted presentation, and the relations become `x=1` and `yz=1`. Thus

    π1(K_RB) = <x,y,z | x, yz> ≅ <z> ≅ Z.

The two proposed green faces are bounded by

    g1 = AB DB^-1 AD^-1,
    g2 = BA CA^-1 BC^-1.

After the tree contraction and the red/blue relations, both represent the same generator `z` (up to orientation or basepoint-conjugation). Neither is a consequence of `r,b`. This is an exact obstruction: Whitehead's free crossed module theorem shows the boundaries of generated 2-dimensional fillers from already admitted relations are precisely their normal closure. In particular the initial green 2-cell cannot be generated as a filler from the red and blue cells alone.

A new source law, an interpretation admitting such an effect comparison, or a genuinely new cell is necessary. The boundary loop itself **is** constructible from the existing arrows; its filling is not.

## 2. Effect of adding one or two green faces

Oriented cellular 2-boundaries (using edge basis AB, BC, CA, AD, DB, BA):

    ∂R  = AB + BC + CA
    ∂B  = AD + DB + BA
    ∂G1 = AB - DB - AD
    ∂G2 = BA - CA - BC

Exact boundary ranks:

| Admitted faces | rk ∂₂ | rk H₁ | rk H₂ | Euler characteristic |
|---|---:|---:|---:|---:|
| R,B | 2 | 1 | 0 | 0 |
| R,B,G1 | 3 | 0 | 0 | 1 |
| R,B,G1,G2 | 3 | 0 | 1 | 2 |

The first `G1` kills the loop `z`; this specific 3-face complex is a disk. Admitting the reflected face `G2` yields a closed 2-dimensional Δ-complex with circular vertex links and topology `S²`. A Δ-complex is used rather than a strict simplicial complex because the independent edge occurrences `AB` and `BA` may connect the same vertices.

The unique integral 2-cycle up to sign is

    Z = R - B - G1 + G2.

The source involution `ρ` exchanges vertices `A↔B`, `C↔D`; edge occurrences `AB↔BA`, `BC↔AD`, `CA↔DB`; and faces `R↔B`, `G1↔G2`. It is a free cellular involution on the closed complex, and sends `Z` to `-Z`. The quotient of this completed sphere is topologically `RP²`.

**Important:** `ρ` is source-combinatorial. A particular *Euclidean point-reflection embedding* is additional geometric data and has not been constructed here.

## 3. The finite free-reflection obstruction

**Proposition (Euler parity).** If a finite CW complex `Y` has a free cellular involution `ρ`, after an equivariant subdivision if necessary, its cells occur in pairs. Therefore

    χ(Y) = 2 χ(Y/ρ),

so `χ(Y)` is even. If `Y` is nonempty and connected, it cannot be rationally acyclic (in particular cannot be contractible), since a rationally acyclic connected complex has Euler characteristic 1.

This is standard topology, not a novel theorem. Its application has a definite consequence: **no finite fixed-point-free reflection-equivariant extension of the R/B/G sphere can erase all positive-dimensional rational homology.** At least one homology class must survive in some positive dimension. This is stronger than excluding a 3-ball filling, and it does not assume that the extension stays two-dimensional.

The statement assumes the reflection remains free on the *entire extended space*. Allowing fixed cells or fixed points removes the parity conclusion. Infinite-dimensional free contractible `EC₂` spaces also exist; finiteness matters.

## 4. A canonical continuation: move the obstruction upward

For any triangulated sphere `(S^n,ρ)` with free involution, form its simplicial suspension

    ΣS^n = S^n * {u+,u-} ≅ S^{n+1},

and extend reflection by

    ρ'(x,t) = (ρ(x), -t),   ρ'(u+) = u-.

The action remains free. It exchanges the two cones. The reduced homology suspension isomorphism gives

    H̃_{k+1}(ΣX; Z) ≅ H̃_k(X; Z).

In particular, the surviving sphere class moves from degree `n` to degree `n+1`. The action on top homology gains a minus sign due to swapping the cones; starting with degree `-1` on the source `S²`, it has degree `+1` on `S³`, then `-1` on `S⁴`.

The quotient of these specific antipodal-type actions is the corresponding real projective space. **This does not produce the Poincaré homology sphere**. The construction is an available completion rule, not a native consequence of the six-arrow operations.

A strict simplicial realization was checked by first barycentrically subdividing the six-arrow Δ-complex's face poset (so edge occurrences are not merged), then suspending twice:

| Complex | Vertices | Edges | Triangles | Tetrahedra | 4-simplices | Euler characteristic |
|---|---:|---:|---:|---:|---:|---:|
| sd(K) ≅ S² | 14 | 36 | 24 | 0 | 0 | 2 |
| Σsd(K) ≅ S³ | 16 | 64 | 96 | 48 | 0 | 0 |
| Σ²sd(K) ≅ S⁴ | 18 | 96 | 224 | 240 | 96 | 2 |

Every cell has a distinct reflected counterpart. Binary boundary-rank calculations give mod-2 Betti vectors `(1,0,1)`, `(1,0,0,1)`, `(1,0,0,0,1)` respectively; the topological identifications follow from the suspension construction, not merely from those Betti numbers.

## 5. Why this is a deeper distinction than a generic horn-filling program

Higher-dimensional rewriting/Squier completion constructs *coherence among admitted relations*. It does not authorize the initial relation `g1` if its boundary is nontrivial in the presentation already supplied. This is consistent with Whitehead's free crossed module description.

This yields a three-way separation:

- **Derived boundary/discrepancy:** existing arrows and their compositions determine `g1` as a closed loop.
- **New 2-cell admission:** requires a genuine source condition, absent in the free six-arrow realization. Adding `g1` changes π₁.
- **Higher coherence generated by symmetry:** once `g1` is admitted with a reflected counterpart `g2`, a 2-sphere class arises; its finite free-reflection-equivariant continuations cannot erase all positive rational homology.

Thus imposing 'fill all cycles' contradicts the topology of this reflection-preserving model. An obstruction-selective rule must indicate *when to introduce a new relation*, not merely how to fill already-null boundaries.

## 6. Limits, next theorem target

Nothing here derives a free point-reflection action on general simplex trees, a unique green cell, a bound on dimension, or any Ramsey threshold. Free reflection and finite-cell continuation are explicit hypotheses, and suspension is a **possible** extension, not the uniquely required one.

The next genuinely open source-level question is whether the original local incidence/extension rules supply an **admission predicate** `Admit(γ,history)` that can be justified without specifying its value on the initial green loop, and that remains stable under continuation and reflection. The theorem should discriminate these cases: preserve nontrivial loop; attach a new green relation; or retain a higher comparison with a nonzero residue. Only then can the outcome for branching trees or Ramsey colorings be predictive.

## Sources

- Actual Marici six-arrow source: https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/ActualSeedEndpointTable.agda
- Free-face obstruction: https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedFaceObstruction.agda
- Exact original source graph realization: https://github.com/andrey-kokoev/marici/blob/main/research/strominger/source-graph-free-realization-v1.md
- Prior native witness-construction audit: https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-seam-native-witness-construction-audit.md
- Whitehead free crossed module discussion: https://link.springer.com/article/10.1007/s00283-021-10110-9
- Squier coherence and critical branchings (2025): https://www.cambridge.org/core/books/abs/polygraphs-from-rewriting-to-higher-categories/homological-syzygies-and-confluence/5FAE190EE4E75B74DD01EC4BBE26FCB9

## Reproduction

    python reflective_crossed_module_check.py
    python reflective_suspension_check.py

Both scripts use exact integer arithmetic. `sympy` is required by the former; the latter uses only the Python standard library. No Agda compilation or repository mutation was performed.
