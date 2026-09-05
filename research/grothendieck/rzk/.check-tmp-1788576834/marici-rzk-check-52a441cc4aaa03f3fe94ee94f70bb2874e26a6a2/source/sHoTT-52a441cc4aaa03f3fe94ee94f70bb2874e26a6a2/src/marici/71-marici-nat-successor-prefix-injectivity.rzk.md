# Successor and additive-prefix injectivity

The predecessor map cancels a supplied equality between successors. Iterating
that cancellation proves injectivity of adding a fixed natural prefix, without
assuming decidable equality or constructor disjointness.

```rzk
#lang rzk-1
```

```rzk
#define marici-succ-injective
  ( a b : MariciNat)
  ( e : marici-succ a =_{MariciNat} marici-succ b)
  : a =_{MariciNat} b
  := ap MariciNat MariciNat
      (marici-succ a) (marici-succ b) marici-pred e

#define marici-add-prefix-injective
  ( k a b : MariciNat)
  ( e : marici-add k a =_{MariciNat} marici-add k b)
  : a =_{MariciNat} b
  := (match k into
        (\ k-prime →
          (marici-add k-prime a =_{MariciNat} marici-add k-prime b)
          → a =_{MariciNat} b)
      ( marici-zero ⇒ \ q → q
      | marici-succ j ih ⇒ \ q →
          ih (marici-succ-injective
            (marici-add j a) (marici-add j b) q))) e
```

## Boundary

These are cancellation theorems for supplied successor and common-prefix
identities. They do not prove zero--successor disjointness, decidable equality,
or identity-path uniqueness. Constructor disjointness remains the missing edge
for unrestricted positive-factor cancellation across zero/nonzero inputs.
