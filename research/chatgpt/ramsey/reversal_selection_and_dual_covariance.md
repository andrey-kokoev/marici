# Stage 12: reversal selection cannot be recovered from the six-arrow source

**Date:** 2026-11-09  
**Status:** Elementary structural theorem plus exact finite-model audit. No new Cubical Agda compilation or native Marici constructor.  
**Predecessor:** Stages 9–11 of the R/B/G coherence investigation.

## Question

Can the previously established Marici primitives, augmented only by ordinary reversible transport, strict point-reflection covariance, and contragredient state/effect transport, select the operational inverse of `AB` so that `BA` is its inverse and the green comparisons follow?

**Answer in the specified free-source and reversible-local-system semantics: no.** There are two independent obstacles: the free directed source cannot support an identity-on-objects dagger reversal, and even its free groupoid completion admits reflection-equivariant orthogonal local systems with nontrivial green monodromy.

## 1. Exact primitive data

The six source occurrences and endpoints are those of [`ActualSeedEndpointTable.agda`](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/ActualSeedEndpointTable.agda):

| Occurrence | Endpoints | Primitive opposite |
|---|---|---|
| AB | A→B | BA |
| BA | B→A | AB |
| BC | B→C | none |
| CA | C→A | none |
| AD | A→D | none |
| DB | D→B | none |

The covariant graph reflection is `ρ(A)=B`, `ρ(B)=A`, `ρ(C)=D`, `ρ(D)=C`, with `AB↔BA`, `BC↔AD`, and `CA↔DB`. Its square is the identity on labeled vertices and occurrences. This is *not* a reversal of arrow directions.

## 2. No internal dagger on the free path category

**Proposition.** The free category on this directed graph has no identity-on-objects contravariant involutive functor `†`.

**Proof.** In a free category, the indecomposable nonidentity morphisms are precisely the one-edge paths. Any contravariant equivalence of categories sends such indecomposable morphisms to indecomposable morphisms: a factorization of `f†` into two nonidentity factors would, after applying its inverse functor, factor `f`. In particular, `BC:B→C` would require an indecomposable path `C→B`. No such edge exists. Contradiction.

This does not prohibit an external adjoint operation on effects or formal groupoid completion. It prohibits claiming that the original free category already has this reversal.

## 3. Free groupoid completion is not a mate identification

Adjoin formal inverses to all six arrows. This is a canonical groupoidification. The resulting inverse `(AB)⁻¹:B→A` is a new formal word, still distinct from the already present primitive occurrence `BA:B→A`. Groupoidification makes each arrow invertible but imposes **no** relation `BA=(AB)⁻¹`.

The original free graph has fundamental group `F₃` (six edges, four vertices, connected). Admitting the red and blue face boundaries reduces the fundamental group to `ℤ`, with retained generator `z=AB·BA`. Thus a reversible groupoid interpretation can still detect `z`.

The existing [`SeedGeometricResponseState`](https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-geometric-response-state.md) already establishes a finer reversible geometric path-state model and explicitly separates `BA` from geometric reversal of `AB`. That native result is independent of the finite control below.

## 4. Strongest finite adversarial control

Let `n≥1`, let `U∈Sₙ` be any permutation acting as an orthogonal matrix on `ℝⁿ`, and choose identical response fibers at all four vertices. Give the primitive edges the effects

```
AB = BA = U
AD = BC = I
DB = CA = U^-1
```

All source operations are equivalences. Both red and blue face words act as identity. With the identity map between reflected response fibers, the edge assignments satisfy strict covariance under the **covariant** source reflection `ρ`.

The green comparison is

```
AB = AD·DB  iff  U = U^-1  iff U² = I.
```

The reflected green comparison has the same criterion. The return word `AB·BA` acts by `U²`.

Choose `U=(0 1 2)` on three states. Then `U³=I` but `U²≠I`. This is the smallest finite permutation model in this uniform-fiber class violating G. The restriction to finite permutation carriers matters: smaller linear countermodels exist.

### Smaller linear countermodels

The same construction works with any unitary `U`. In complex dimension one take `U=ω`, where `ω³=1` and `ω≠1`. The red and blue composites are identity but the retained return acts as `ω²`, which is not identity as a linear map. This scalar may disappear under projectivization, so it is not by itself a measurement claim.

A non-scalar exact real example acts in two dimensions:

```
U = [[0,-1],[1,-1]],   M = [[2,-1],[-1,2]].
```

Here `U³=I`, `U²≠I`, and `Uᵀ M U=M` with `M` positive definite. After changing to an orthonormal basis for `M`, it is an ordinary 120° real-plane rotation. Thus the obstruction remains even with real isometric, non-scalar effects.

### Dual evaluation covariance does not select G

The same model satisfies evaluation covariance. For a state `x∈ℝⁿ` and a covector `f∈(ℝⁿ)*`, transform the state by `U` and the covector by `(U⁻¹)*`:

`⟨(U⁻¹)*f, Ux⟩=⟨f,x⟩`.

This equation holds for every invertible `U`, including the order-three counterexample. Invertible, orthogonal, unitary, and evaluation-covariant effects do not determine which separate primitive occurrence should be the operational inverse of another.

This is consistent with the existing [`ContinuationPhaseTransport`](https://github.com/andrey-kokoev/marici/blob/main/research/nima/continuation-charge-character.md) theorem: evaluation covariance uniquely determines the dual transport **given an input transport**. It does not declare the independent primitive `BA` to be that dual transport.

## 5. Exhaustive finite audit

For each `n≤7`, every permutation `U∈Sₙ` was enumerated. Face closure, strict reflection covariance, invertibility, and the exact green criterion were checked.

| States n | Tested models | Green closes | Green obstructed |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 2 | 2 | 0 |
| 3 | 6 | 4 | 2 |
| 4 | 24 | 10 | 14 |
| 5 | 120 | 26 | 94 |
| 6 | 720 | 76 | 644 |
| 7 | 5,040 | 232 | 4,808 |

The successful counts agree with the closed formula for involutions:

`I_n = Σ_{k=0}^{⌊n/2⌋} n!/[2^k k!(n−2k)!]`.

The counterexample is not a numerical accident; all permutation monodromies are allowed under the tested contracts, and only involutions satisfy the green relation.

## 6. The minimal missing binding

The source's primitive *presentation reversal* keeps the occurrence label `AB`. A separately supplied edge action `F(AB)` may have an inverse, but that action's inverse is not automatically `F(BA)`.

One additional **mate binding**,

`F(BA) ≃ F(AB)⁻¹` with pointed and continuation-coherent witnesses,

would make the return trivial at the effect level. Given the R/B face fillings, it would derive both G comparisons. But in the present model that binding is equivalent to the desired return cancellation. It is **not** an independent explanation merely because it is expressed in typed language.

A productive independent justification must come from some primitive operational specification—such as a physically implemented inverse execution, with tracked error and context behavior—not from the desired green topology.

## 7. Research disposition

1. The source free path category has no internal dagger, and groupoidification does not pair `AB` with `BA`.
2. Stronger externally supplied effect properties—unitarity, strict covariant reflection-equivariance, and dual evaluation covariance—still admit the three-state obstruction.
3. The existing canonical geometric path-state interpretation independently retains the discrepancy.
4. Therefore the next mathematically meaningful task is **source authority for the mate relation**, not a new abstract filler theorem. If the source does not supply it, preserve the obstruction and stop treating strict G as necessary.
5. No evidence is obtained for Ramsey thresholds or for a native topology beyond the conditional constructions in previous stages.

## Reproduction

`python check_reversal_selection.py`

The checker uses only the standard library, writes `reversal_selection_results.json`, verifies the exact complex-phase and real-plane countermodels, and enumerates all 5,913 uniform-fiber permutation models through seven states. The structural no-dagger proof is mathematical (not formalized in Agda). The Marici repository was not modified.
