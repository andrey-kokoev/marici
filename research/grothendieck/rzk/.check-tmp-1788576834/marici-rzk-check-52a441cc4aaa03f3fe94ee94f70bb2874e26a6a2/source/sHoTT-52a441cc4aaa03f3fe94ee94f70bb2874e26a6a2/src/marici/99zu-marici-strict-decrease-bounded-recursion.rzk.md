# Converting strict decrease to a predecessor bound

For recursion at denominator predecessor `succ n`, strict decrease to a
cofactor predecessor removes the positive gap's outer successor and yields the
non-strict bound needed by the induction hypothesis at `n`.

```rzk
#lang rzk-1
```

```rzk
#define marici-strictly-less-successor-gives-at-most
  ( r n : MariciNat)
  ( decrease : MariciNatStrictlyLess r (marici-succ n))
  : MariciNatAtMost r n
  := match decrease
      ( marici-nat-strictly-less-witness gap equation ⇒
          marici-nat-at-most-witness r n gap
            (marici-succ-injective
              (marici-add gap r) n equation))

#define marici-at-most-reflexive
  ( n : MariciNat)
  : MariciNatAtMost n n
  := marici-nat-at-most-witness n n marici-zero refl
```

The induction hypothesis required by bounded normalization is now an explicit
function type: it normalizes every component pair whose denominator predecessor
is bounded by the current recursion index.

```rzk
#define MariciBoundedNormalizationFamily
  ( bound : MariciNat)
  : U
  := (a : MariciInt) → (d : MariciNat) → MariciNatAtMost d bound
    → MariciRawFractionNormalization (marici-raw-fraction a d)
```

## Boundary

Strict factor-removal decrease now has exactly the bound shape required for
structural recursion on an external denominator bound. Constructing that
bounded normalization family by induction, then applying it at the reflexive
bound, remains the final universal-existence step.
