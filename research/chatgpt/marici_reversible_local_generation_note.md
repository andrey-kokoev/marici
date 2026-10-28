# Reversible local generation without an independently supplied return witness

**Research note — 2026-10-27**  
**Status:** Source-informed exact finite computations and algebraic constructions. Not a new native Marici rule, and not a Cubical Agda theorem.

## Hypothesis

A primitive may consist of an incremental **witness-generating operation**, rather than the fixed packet `[a,b,c,d,a']`:

- Extend the current retained history by **one admitted segment**.
- Require each segment to be reversible in the specified operating category.
- Require compatibility of a new segment with previous operations, perhaps through a common square or witnessed interchange.
- Construct the return/comparison witness from those local laws, retaining its generating word.

Interpret “square of a term” here as **operator composition** `u²`, not a scalar norm. Other meanings need separate tests. Direction-reversed presentation is not automatically an executable inverse operation.

## Negative result 1: equal squares and invertibility do not force closure

In the eight-element real signed-permutation group `D4`, choose

```
X = [0 1; 1 0]
Z = [1 0; 0 -1]
```

Then `X² = Z² = I`, both operations are invertible, but

`[X,Z] = X Z X⁻¹ Z⁻¹ = −I ≠ I`.

An exact enumeration over all 8 elements gives 40 ordered pairs whose squares agree. Of those, 32 commute strictly and 8 have commutator `−I`. The induced conjugation actions commute because the discrepancy is central; forgetting the central sign loses the distinction.

An explicit flat pair of independent commuting 3×3 diagonal involutions has `[P,Q]=I`, demonstrating that the same local square condition supports both outcomes. Even strict commutation alone does not force an **arbitrary** four-step schedule to return: four positive integer translations are invertible and commute, but translate by `+4`. The return follows only for the **particular commutator itinerary** `P Q P⁻¹ Q⁻¹` when its square is flat.

## Positive result 1: a computed, continuation-invariant residue

For `X,Z` above, set `κ(X,Z)=[X,Z]=−I`. This is not an independently introduced fifth term. It is computed using composition and inverses. Since it is central, every continuation `c` satisfies `c κ c⁻¹=κ`.

The four-step path returns to the same **projective action**, but not the identity of the unprojected representation. `κ` certifies the residual discrepancy; it must not be called an equality `I=−I` in the full carrier. Its actual word history remains distinct from the empty history.

Two extreme continuation rules are insufficient to select a nontrivial structure:

- Requiring strict commutation with **every** continuation in `D4` leaves only its center `{I,−I}` as permissible selected terms.
- Allowing all continuations to be transported by conjugation satisfies `Ad_u(c)u=uc` for **every invertible** `u`; it is coherent but imposes no selection and does not force periodic return.

## Positive result 2: the same local rule builds a four-level nested comparison

Work over `F₂`, with unitriangular matrices of size 5. Supply elementary involutions

`x_i = I + E_(i,i+1)`, for `i=1,...,4`, each satisfying `x_i²=I`.

Use **one unchanged** recursive rule:

`w₁=x₁`, `w_(k+1)=[w_k,x_(k+1)]`.

The results are:

| Step | Constructed transformation | Does it commute with all 1,024 generated continuations? |
| --- | --- | --- |
| 1 | `I + E₁₂` | No |
| 2 | `I + E₁₃` | No |
| 3 | `I + E₁₄` | No |
| 4 | `I + E₁₅` | Yes |

The entire generated group was enumerated (`|UT₅(F₂)|=1024`). Every constructed witness is nonidentity, reversible, and squares to `I`. The terminal witness is central. Commuting it with any further continuation produces identity, so this **fixed model stops**.

The matrix identity follows algebraically: for `i<j<k`,

`[I+E_(i,j), I+E_(j,k)] = I+E_(i,k)` over `F₂`.

Therefore each level is the next relative commutator of the same form. It is a hierarchy of **algebraic comparison depth**, not a construction of cells in distinct geometric dimensions or higher-categorical fillers.

## Negative result 2: the number four is not selected

Keep the same unchanged commutator rule, and replace `UT₅(F₂)` with `UT_n(F₂)`.

The chain is `w_k=I+E_(1,k+1)` for `1≤k≤n−1`, and its last term is central. Exact matrix tests for `n=3,4,5,6,7` yield **2, 3, 4, 5, 6** nontrivial steps respectively. Consequently **four stages come from choosing the ambient size five**, not from invertibility, equal squares, or the commutator recursion alone.

The initial four independent elementary directions were supplied. One generator capable of discovering/selecting all next directions was **not** established.

## Source relationship

These tests align with the existing Marici results:

- [Phase selection from coherence](https://github.com/andrey-kokoev/marici/blob/main/research/nima/phase-selection-from-coherence.md) independently classifies the trivial and Clifford central-phase choices over the actual two-swap source. Its normalized sign-cocycle audit yields 16 cocycles, 4 with positive generator squares, and two commutator-phase outcomes.
- [Clifford retained order recursion](https://github.com/andrey-kokoev/marici/blob/main/research/nima/clifford-retained-order-recursion.md) already constructs the nontrivial central sign with complete word retention; do not report this as new to Marici.
- [Two triangles with shared-edge half-phase](https://github.com/andrey-kokoev/marici/blob/main/research/nima/two-triangles-shared-edge-half-phase.md) already demonstrates noncommuting square roots and an order-five serial update, independently of any new return policy.
- [Typed generator Layer 2](https://github.com/andrey-kokoev/marici/blob/main/research/nima/typed-generator-layer-2.md) separates retained histories from optional interpretation in the original witness relation.

## Proposed source-level discriminator

The productive next theorem is **not** to reprove that commutators, central extensions, or commuting squares exist. Instead:

1. Identify **one actual source-admitted rule** producing the next elementary segment from the current *complete retained witness*, with an explicit admission certificate. Do not supply independent `x₂,x₃,x₄` solely to obtain four steps.
2. Derive the interchange/commutator comparison from that rule. Preserve the full return residue; permit `κ≠I` only when a typed comparison explains its status and its allowed continuation transport.
3. Prove the comparison is coherent under every **source-admitted** continuation in both orientations, by induction over actual histories. Do not substitute the ambient group action for the source-authorized context family.
4. Determine whether the recursion reaches a nontrivial new witness, an identity witness, an obstruction, or an infinite chain. Do not preselect a 4-cycle.
5. Preserve provenance independently from endpoint/operator reduction; an identity evaluation must not erase a nonempty source word.

**Outcome:** The original `a'` need not be supplied independently: a residual return/comparison can be *calculated* from local rules. However, reversible equal-square steps do not force an identity return or a unique four-level hierarchy. They can generate an invariant nontrivial obstruction instead. The unresolved issue is **source-defined selection and admissibility of each next segment and higher comparison**, not a missing algebraic formula.

## Reproducible scripts

- `local_reversible_coherence_audit.py` / `local_reversible_coherence_results.json` — exact signed-matrix, centralizer, transport and normalized cocycle census.
- `local_reversible_tower_audit.py` / `local_reversible_tower_results.json` — generated `UT₅(F₂)` and varying-size higher-commutator tests.

Both scripts run using standard Python, with no external libraries. Neither claims a newly compiled Agda proof.
