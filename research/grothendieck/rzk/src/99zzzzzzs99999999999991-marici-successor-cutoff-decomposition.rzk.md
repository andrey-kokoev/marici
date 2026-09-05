# Bounds beyond a successor cutoff expose a local predecessor

An additive gap from `succ cutoff` to a target determines the local predecessor
`gap + cutoff`. Successor-right addition identifies the target with its
successor, while the same gap witnesses that the requested cutoff is below the
local predecessor.

```rzk
#lang rzk-1
```

```rzk
#data MariciSuccessorCutoffDecomposition
  ( cutoff target : MariciNat)
  := marici-successor-cutoff-decomposition
      ( local-cutoff : MariciNat)
      ( target-path : marici-succ local-cutoff =_{MariciNat} target)
      ( cutoff-bound : MariciNatAtMost cutoff local-cutoff)

#define marici-successor-cutoff-decompose
  ( cutoff target : MariciNat)
  ( witness : MariciNatAtMost (marici-succ cutoff) target)
  : MariciSuccessorCutoffDecomposition cutoff target
  := match witness
      ( marici-nat-at-most-witness gap equation ⇒
          marici-successor-cutoff-decomposition cutoff target
            (marici-add gap cutoff)
            (concat MariciNat
              (marici-succ (marici-add gap cutoff))
              (marici-add gap (marici-succ cutoff))
              target
              (rev MariciNat
                (marici-add gap (marici-succ cutoff))
                (marici-succ (marici-add gap cutoff))
                (marici-add-succ-right gap cutoff))
              equation)
            (marici-nat-at-most-witness
              cutoff (marici-add gap cutoff) gap refl))
```

## Boundary

Every index admitted beyond the successor modulus now supplies the exact local
cutoff required by the ordered partial-sum theorem and an order witness comparing
its reciprocal tolerance with the requested tolerance. The remaining Cauchy
step composes this decomposition with the gap between the two arbitrary indices.
