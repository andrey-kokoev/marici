# Mixed associativity for an arbitrary positive pair and cancellation

The sum of two positive canonical integers has predecessor
`succ(a+b)`. Commutativity identifies this with the explicit gap presentation
`(b+1)+a`; gap normalization then cancels the following negative `b` term and
leaves positive `a`. The other parenthesization cancels `b` first.

```rzk
#lang rzk-1
```

```rzk
#define marici-successor-add-swap
  ( a b : MariciNat)
  : marici-succ (marici-add a b)
    =_{MariciNat}
    marici-add (marici-succ b) a
  := ap MariciNat MariciNat
      (marici-add a b) (marici-add b a)
      marici-succ
      (marici-add-comm a b)

#define marici-int-add-assoc-positive-positive-negative-self
  ( a b : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-pos b) (marici-int-neg b)
  := concat MariciInt
      (marici-int-add
        (marici-int-add (marici-int-pos a) (marici-int-pos b))
        (marici-int-neg b))
      (marici-int-add
        (marici-int-pos (marici-add (marici-succ b) a))
        (marici-int-neg b))
      (marici-int-add (marici-int-pos a)
        (marici-int-add (marici-int-pos b) (marici-int-neg b)))
      (ap MariciNat MariciInt
        (marici-succ (marici-add a b))
        (marici-add (marici-succ b) a)
        (\ predecessor →
          marici-int-add (marici-int-pos predecessor) (marici-int-neg b))
        (marici-successor-add-swap a b))
      (concat MariciInt
        (marici-int-add
          (marici-int-pos (marici-add (marici-succ b) a))
          (marici-int-neg b))
        (marici-int-pos a)
        (marici-int-add (marici-int-pos a)
          (marici-int-add (marici-int-pos b) (marici-int-neg b)))
        (marici-int-add-pos-neg-gap b a)
        (ap MariciInt MariciInt
          marici-int-zero
          (marici-int-add (marici-int-pos b) (marici-int-neg b))
          (\ value → marici-int-add (marici-int-pos a) value)
          (rev MariciInt
            (marici-int-add (marici-int-pos b) (marici-int-neg b))
            marici-int-zero
            (marici-int-add-pos-neg-self b))))

#define marici-int-add-assoc-negative-negative-positive-self
  ( a b : MariciNat)
  : MariciIntAddAssociates
      (marici-int-neg a) (marici-int-neg b) (marici-int-pos b)
  := marici-int-add-assoc-sign-reversal
      (marici-int-pos a) (marici-int-pos b) (marici-int-neg b)
      (marici-int-add-assoc-positive-positive-negative-self a b)
```

## Boundary

Associativity is checked for arbitrary positive first and second terms when the
third is the additive inverse of the second, and for the sign-reversed family.
This removes the unit restriction from the prior cancellation theorem. A fully
independent third magnitude still requires a three-way gap decomposition.
