# Mixed associativity at total-magnitude cancellation

When the third negative predecessor equals the predecessor of the sum of the
two positive terms, the left parenthesization cancels immediately. On the
right, natural commutativity presents the negative term as an explicit gap over
the middle positive term; its residual cancels the first term.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-assoc-total-positive-magnitude-cancellation
  ( a b : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-pos b)
      (marici-int-neg (marici-succ (marici-add a b)))
  := concat MariciInt
      (marici-int-add
        (marici-int-add (marici-int-pos a) (marici-int-pos b))
        (marici-int-neg (marici-succ (marici-add a b))))
      marici-int-zero
      (marici-int-add (marici-int-pos a)
        (marici-int-add (marici-int-pos b)
          (marici-int-neg (marici-succ (marici-add a b)))))
      (marici-int-add-pos-neg-self (marici-succ (marici-add a b)))
      (rev MariciInt
        (marici-int-add (marici-int-pos a)
          (marici-int-add (marici-int-pos b)
            (marici-int-neg (marici-succ (marici-add a b)))))
        marici-int-zero
        (concat MariciInt
          (marici-int-add (marici-int-pos a)
            (marici-int-add (marici-int-pos b)
              (marici-int-neg (marici-succ (marici-add a b)))))
          (marici-int-add (marici-int-pos a)
            (marici-int-add (marici-int-pos b)
              (marici-int-neg (marici-add (marici-succ b) a))))
          marici-int-zero
          (ap MariciNat MariciInt
            (marici-succ (marici-add a b))
            (marici-add (marici-succ b) a)
            (\ predecessor →
              marici-int-add (marici-int-pos a)
                (marici-int-add (marici-int-pos b)
                  (marici-int-neg predecessor)))
            (marici-successor-add-swap a b))
          (concat MariciInt
            (marici-int-add (marici-int-pos a)
              (marici-int-add (marici-int-pos b)
                (marici-int-neg (marici-add (marici-succ b) a))))
            (marici-int-add (marici-int-pos a) (marici-int-neg a))
            marici-int-zero
            (ap MariciInt MariciInt
              (marici-int-add (marici-int-pos b)
                (marici-int-neg (marici-add (marici-succ b) a)))
              (marici-int-neg a)
              (\ value → marici-int-add (marici-int-pos a) value)
              (marici-int-add-pos-neg-negative-gap b a))
            (marici-int-add-pos-neg-self a))))

#define marici-int-add-assoc-total-negative-magnitude-cancellation
  ( a b : MariciNat)
  : MariciIntAddAssociates
      (marici-int-neg a) (marici-int-neg b)
      (marici-int-pos (marici-succ (marici-add a b)))
  := marici-int-add-assoc-sign-reversal
      (marici-int-pos a) (marici-int-pos b)
      (marici-int-neg (marici-succ (marici-add a b)))
      (marici-int-add-assoc-total-positive-magnitude-cancellation a b)
```

## Boundary

The equality boundary between positive-total dominance and negative-total
dominance is checked, together with its sign reversal. The two strict
intermediate regions on either side still require arbitrary residual
reassociation.
