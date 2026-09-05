# Marici natural-number semiring laws

This increment derives the remaining multiplication laws needed for the
commutative-semiring fragment.

```rzk
#lang rzk-1
```

Swapping two additive prefixes is derived from associativity and commutativity.

```rzk
#define marici-add-swap-prefix
  ( a b c : MariciNat)
  : marici-add a (marici-add b c)
    =_{MariciNat} marici-add b (marici-add a c)
  := concat MariciNat
      (marici-add a (marici-add b c))
      (marici-add (marici-add a b) c)
      (marici-add b (marici-add a c))
      (rev MariciNat
        (marici-add (marici-add a b) c)
        (marici-add a (marici-add b c))
        (marici-add-assoc a b c))
      (concat MariciNat
        (marici-add (marici-add a b) c)
        (marici-add (marici-add b a) c)
        (marici-add b (marici-add a c))
        (ap MariciNat MariciNat
          (marici-add a b) (marici-add b a)
          (\ q → marici-add q c)
          (marici-add-comm a b))
        (marici-add-assoc b a c))
```

Multiplication by a successor in the right argument is then proved by induction
on the left argument.

```rzk
#define marici-mul-succ-right
  ( n m : MariciNat)
  : marici-mul n (marici-succ m)
    =_{MariciNat} marici-add n (marici-mul n m)
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒
          ap MariciNat MariciNat
            (marici-add m (marici-mul k (marici-succ m)))
            (marici-add k (marici-add m (marici-mul k m)))
            marici-succ
            (concat MariciNat
              (marici-add m (marici-mul k (marici-succ m)))
              (marici-add m (marici-add k (marici-mul k m)))
              (marici-add k (marici-add m (marici-mul k m)))
              (ap MariciNat MariciNat
                (marici-mul k (marici-succ m))
                (marici-add k (marici-mul k m))
                (\ q → marici-add m q) ih)
              (marici-add-swap-prefix m k (marici-mul k m))))
```

```rzk
#define marici-mul-comm
  ( n m : MariciNat)
  : marici-mul n m =_{MariciNat} marici-mul m n
  := match n
      ( marici-zero ⇒ rev MariciNat
          (marici-mul m marici-zero) marici-zero
          (marici-mul-zero-right m)
      | marici-succ k ih ⇒
          concat MariciNat
            (marici-add m (marici-mul k m))
            (marici-add m (marici-mul m k))
            (marici-mul m (marici-succ k))
            (ap MariciNat MariciNat
              (marici-mul k m) (marici-mul m k)
              (\ q → marici-add m q) ih)
            (rev MariciNat
              (marici-mul m (marici-succ k))
              (marici-add m (marici-mul m k))
              (marici-mul-succ-right m k)))

#define marici-mul-assoc
  ( n m k : MariciNat)
  : marici-mul (marici-mul n m) k
    =_{MariciNat} marici-mul n (marici-mul m k)
  := match n
      ( marici-zero ⇒ refl
      | marici-succ j ih ⇒
          concat MariciNat
            (marici-mul (marici-add m (marici-mul j m)) k)
            (marici-add (marici-mul m k)
              (marici-mul (marici-mul j m) k))
            (marici-add (marici-mul m k)
              (marici-mul j (marici-mul m k)))
            (marici-mul-add-left-distrib m (marici-mul j m) k)
            (ap MariciNat MariciNat
              (marici-mul (marici-mul j m) k)
              (marici-mul j (marici-mul m k))
              (\ q → marici-add (marici-mul m k) q) ih))
```

Right distributivity is transported from left distributivity through
multiplicative commutativity.

```rzk
#define marici-mul-add-right-distrib
  ( n m k : MariciNat)
  : marici-mul n (marici-add m k)
    =_{MariciNat} marici-add (marici-mul n m) (marici-mul n k)
  := concat MariciNat
      (marici-mul n (marici-add m k))
      (marici-mul (marici-add m k) n)
      (marici-add (marici-mul n m) (marici-mul n k))
      (marici-mul-comm n (marici-add m k))
      (concat MariciNat
        (marici-mul (marici-add m k) n)
        (marici-add (marici-mul m n) (marici-mul k n))
        (marici-add (marici-mul n m) (marici-mul n k))
        (marici-mul-add-left-distrib m k n)
        (concat MariciNat
          (marici-add (marici-mul m n) (marici-mul k n))
          (marici-add (marici-mul n m) (marici-mul k n))
          (marici-add (marici-mul n m) (marici-mul n k))
          (ap MariciNat MariciNat
            (marici-mul m n) (marici-mul n m)
            (\ q → marici-add q (marici-mul k n))
            (marici-mul-comm m n))
          (ap MariciNat MariciNat
            (marici-mul k n) (marici-mul n k)
            (\ q → marici-add (marici-mul n m) q)
            (marici-mul-comm k n))))
```

## Boundary

Together with the prior modules this establishes the equational
commutative-semiring laws. Packaging as a reusable structure and proving
sethood remain separate obligations.
