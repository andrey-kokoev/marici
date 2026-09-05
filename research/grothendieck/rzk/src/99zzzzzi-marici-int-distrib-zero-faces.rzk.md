# Zero faces of integer distributivity

The global distributivity interface is separated from its constructor proofs.
A zero multiplier and a zero summand pair compute directly, removing those
faces before assembling the nonzero same-sign and mixed-gap branches.

```rzk
#lang rzk-1
```

```rzk
#define MariciIntLeftDistributes
  ( x y z : MariciInt)
  : U
  := marici-int-mul x (marici-int-add y z)
    =_{MariciInt}
    marici-int-add (marici-int-mul x y) (marici-int-mul x z)

#define marici-int-left-distrib-zero-factor
  ( y z : MariciInt)
  : MariciIntLeftDistributes marici-int-zero y z
  := refl

#define marici-int-left-distrib-zero-summands
  ( x : MariciInt)
  : MariciIntLeftDistributes x marici-int-zero marici-int-zero
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒ refl
      | marici-int-neg a ⇒ refl)
```

## Boundary

The zero multiplier and double-zero summand faces of global integer left
distributivity are checked. Arbitrary nonzero summands still require assembly
of the existing same-sign and explicit mixed-gap distributive families; no
claim of global distributivity is made.
