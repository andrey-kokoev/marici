# Decoding an encoded natural path

First, structural induction proves that decoding the reflexive code yields the
reflexive path. Identity elimination then proves that decoding the encoding of
an arbitrary natural path returns that path.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-identity-decode-refl
  ( n : MariciNat)
  : marici-nat-identity-decode n n
      (marici-nat-identity-code-refl n)
    =_{(n =_{MariciNat} n)} refl
  := match n
      ( marici-zero ⇒ refl
      | marici-succ i ih ⇒
          ap (i =_{MariciNat} i)
            ((marici-succ i) =_{MariciNat} (marici-succ i))
            (marici-nat-identity-decode i i
              (marici-nat-identity-code-refl i))
            refl
            (\ q → ap MariciNat MariciNat i i marici-succ q)
            ih)

```

## Boundary

Decoding the reflexive code is checked. Extending this computation to arbitrary
paths by identity elimination, the code-side composite, and uniqueness of each
inhabited code remain before natural identity-path uniqueness follows.
