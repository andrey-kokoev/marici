# Positive cofactors are bounded by the target

A non-strict natural bound is witnessed by an additive gap. Any positive
factorization bounds the cofactor predecessor by the target predecessor, giving
the finite search bound needed for divisibility.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatAtMost
  ( smaller larger : MariciNat)
  := marici-nat-at-most-witness
      ( gap : MariciNat)
      ( equation : marici-add gap smaller =_{MariciNat} larger)

#define marici-positive-cofactor-at-most-target
  ( q f n : MariciNat)
  ( e : marici-mul (marici-succ q) (marici-succ f)
    =_{MariciNat} marici-succ n)
  : MariciNatAtMost q n
  := marici-nat-at-most-witness q n
      (marici-mul f (marici-succ q))
      (concat MariciNat
        (marici-add (marici-mul f (marici-succ q)) q)
        (marici-add q (marici-mul f (marici-succ q)))
        n
        (marici-add-comm (marici-mul f (marici-succ q)) q)
        (marici-succ-injective
          (marici-add q (marici-mul f (marici-succ q))) n
          (concat MariciNat
            (marici-mul (marici-succ f) (marici-succ q))
            (marici-mul (marici-succ q) (marici-succ f))
            (marici-succ n)
            (rev MariciNat
              (marici-mul (marici-succ q) (marici-succ f))
              (marici-mul (marici-succ f) (marici-succ q))
              (marici-mul-comm (marici-succ q) (marici-succ f)))
            e)))
```

## Boundary

Every positive cofactor predecessor lies at most at the target predecessor, so
searching candidates zero through the target predecessor is extensionally
complete. A theorem that the traced fuel search tests exactly this interval and
turns its rejection log into a universal refutation remains open.
