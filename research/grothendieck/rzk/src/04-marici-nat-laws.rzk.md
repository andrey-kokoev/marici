# Marici natural-number laws

This increment derives further arithmetic laws from the recursive definitions
in `03-marici-nat.rzk.md`.

```rzk
#lang rzk-1
```

```rzk
#define marici-add-assoc
  ( n m k : MariciNat)
  : marici-add (marici-add n m) k
    =_{MariciNat} marici-add n (marici-add m k)
  := match n
      ( marici-zero ⇒ refl
      | marici-succ j ih ⇒
          ap MariciNat MariciNat
            (marici-add (marici-add j m) k)
            (marici-add j (marici-add m k))
            marici-succ ih)

#define marici-mul-zero-left
  ( n : MariciNat)
  : marici-mul marici-zero n =_{MariciNat} marici-zero
  := refl

#define marici-mul-zero-right
  ( n : MariciNat)
  : marici-mul n marici-zero =_{MariciNat} marici-zero
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒ ih)

#define marici-mul-one-left
  ( n : MariciNat)
  : marici-mul marici-one n =_{MariciNat} n
  := marici-add-zero-right n

#define marici-mul-one-right
  ( n : MariciNat)
  : marici-mul n marici-one =_{MariciNat} n
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒
          ap MariciNat MariciNat
            (marici-mul k marici-one)
            k marici-succ ih)
```

Left distributivity follows directly from recursion on the first multiplier.
The successor step uses the reverse of additive associativity to reassociate
the target.

```rzk
#define marici-mul-add-left-distrib
  ( n m k : MariciNat)
  : marici-mul (marici-add n m) k
    =_{MariciNat} marici-add (marici-mul n k) (marici-mul m k)
  := match n
      ( marici-zero ⇒ refl
      | marici-succ j ih ⇒
          concat MariciNat
            (marici-add k (marici-mul (marici-add j m) k))
            (marici-add k
              (marici-add (marici-mul j k) (marici-mul m k)))
            (marici-add
              (marici-add k (marici-mul j k))
              (marici-mul m k))
            (ap MariciNat MariciNat
              (marici-mul (marici-add j m) k)
              (marici-add (marici-mul j k) (marici-mul m k))
              (\ q → marici-add k q) ih)
            (rev MariciNat
              (marici-add
                (marici-add k (marici-mul j k))
                (marici-mul m k))
              (marici-add k
                (marici-add (marici-mul j k) (marici-mul m k)))
              (marici-add-assoc k (marici-mul j k) (marici-mul m k))))
```

## Boundary

These theorems establish additive associativity, both multiplicative zero laws,
both multiplicative unit laws, and left distributivity. Multiplicative
associativity, commutativity, right distributivity, order, cancellation, and
sethood remain open.
