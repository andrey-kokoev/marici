# Natural multiplication preserves truncated subtraction

Common additive prefixes can be removed from truncated subtraction. Combined
with multiplication by successors, this proves that natural multiplication
preserves truncated subtraction in its right argument.

```rzk
#lang rzk-1
```

```rzk
#define marici-sub-common-prefix
  ( k a b : MariciNat)
  : marici-sub (marici-add k a) (marici-add k b)
    =_{MariciNat} marici-sub a b
  := match k
      ( marici-zero ⇒ refl
      | marici-succ j ih ⇒ ih)
```

```rzk
#define marici-mul-sub-right-distrib
  ( n a m : MariciNat)
  : marici-sub (marici-mul n a) (marici-mul n m)
    =_{MariciNat} marici-mul n (marici-sub a m)
  := (match a into
        (\ a-prime → (b-prime : MariciNat) →
          marici-sub (marici-mul n a-prime) (marici-mul n b-prime)
          =_{MariciNat} marici-mul n (marici-sub a-prime b-prime))
      ( marici-zero ⇒ \ b → concat MariciNat
          (marici-sub
            (marici-mul n marici-zero) (marici-mul n b))
          marici-zero
          (marici-mul n marici-zero)
          (concat MariciNat
            (marici-sub
              (marici-mul n marici-zero) (marici-mul n b))
            (marici-sub marici-zero (marici-mul n b))
            marici-zero
            (ap MariciNat MariciNat
              (marici-mul n marici-zero) marici-zero
              (\ z → marici-sub z (marici-mul n b))
              (marici-mul-zero-right n))
            (marici-sub-zero-left (marici-mul n b)))
          (rev MariciNat
            (marici-mul n marici-zero) marici-zero
            (marici-mul-zero-right n))
      | marici-succ i ih ⇒ \ b → match b
          ( marici-zero ⇒ concat MariciNat
              (marici-sub
                (marici-mul n (marici-succ i))
                (marici-mul n marici-zero))
              (marici-sub
                (marici-mul n (marici-succ i)) marici-zero)
              (marici-mul n (marici-succ i))
              (ap MariciNat MariciNat
                (marici-mul n marici-zero) marici-zero
                (\ z → marici-sub
                  (marici-mul n (marici-succ i)) z)
                (marici-mul-zero-right n))
              (marici-sub-zero-right
                (marici-mul n (marici-succ i)))
          | marici-succ j jh ⇒ concat MariciNat
              (marici-sub
                (marici-mul n (marici-succ i))
                (marici-mul n (marici-succ j)))
              (marici-sub
                (marici-add n (marici-mul n i))
                (marici-add n (marici-mul n j)))
              (marici-mul n (marici-sub i j))
              (concat MariciNat
                (marici-sub
                  (marici-mul n (marici-succ i))
                  (marici-mul n (marici-succ j)))
                (marici-sub
                  (marici-add n (marici-mul n i))
                  (marici-mul n (marici-succ j)))
                (marici-sub
                  (marici-add n (marici-mul n i))
                  (marici-add n (marici-mul n j)))
                (ap MariciNat MariciNat
                  (marici-mul n (marici-succ i))
                  (marici-add n (marici-mul n i))
                  (\ z → marici-sub z
                    (marici-mul n (marici-succ j)))
                  (marici-mul-succ-right n i))
                (ap MariciNat MariciNat
                  (marici-mul n (marici-succ j))
                  (marici-add n (marici-mul n j))
                  (\ z → marici-sub
                    (marici-add n (marici-mul n i)) z)
                  (marici-mul-succ-right n j)))
              (concat MariciNat
                (marici-sub
                  (marici-add n (marici-mul n i))
                  (marici-add n (marici-mul n j)))
                (marici-sub (marici-mul n i) (marici-mul n j))
                (marici-mul n (marici-sub i j))
                (marici-sub-common-prefix n
                  (marici-mul n i) (marici-mul n j))
                (ih j))))) m
```

## Boundary

The theorem preserves truncated subtraction under multiplication by a supplied
natural factor. It does not establish order reflection or cancellativity of
that factor.
