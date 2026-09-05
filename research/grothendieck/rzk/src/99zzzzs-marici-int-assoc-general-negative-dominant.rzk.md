# General negative-dominant mixed associativity

For arbitrary positive first and middle terms, parameterize the following
negative predecessor as `(b+1)+((a+1)+r)`. Natural reassociation and
commutativity identify this with the explicit outer gap. The inner gap leaves a
negative term still dominating the first term, so both parenthesizations reduce
to `-r`.

```rzk
#lang rzk-1
```

```rzk
#define marici-two-positive-gap-reassociate
  ( a b r : MariciNat)
  : marici-add (marici-succ b)
      (marici-add (marici-succ a) r)
    =_{MariciNat}
    marici-add (marici-succ (marici-succ (marici-add a b))) r
  := concat MariciNat
      (marici-add (marici-succ b) (marici-add (marici-succ a) r))
      (marici-add
        (marici-add (marici-succ b) (marici-succ a)) r)
      (marici-add (marici-succ (marici-succ (marici-add a b))) r)
      (rev MariciNat
        (marici-add
          (marici-add (marici-succ b) (marici-succ a)) r)
        (marici-add (marici-succ b) (marici-add (marici-succ a) r))
        (marici-add-assoc (marici-succ b) (marici-succ a) r))
      (ap MariciNat MariciNat
        (marici-add (marici-succ b) (marici-succ a))
        (marici-succ (marici-succ (marici-add a b)))
        (\ value → marici-add value r)
        (concat MariciNat
          (marici-add (marici-succ b) (marici-succ a))
          (marici-add (marici-succ a) (marici-succ b))
          (marici-succ (marici-succ (marici-add a b)))
          (marici-add-comm (marici-succ b) (marici-succ a))
          (marici-add-succ-right (marici-succ a) b)))

#define marici-int-add-assoc-general-negative-dominant
  ( a b r : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-pos b)
      (marici-int-neg
        (marici-add (marici-succ b) (marici-add (marici-succ a) r)))
  := concat MariciInt
      (marici-int-add
        (marici-int-add (marici-int-pos a) (marici-int-pos b))
        (marici-int-neg
          (marici-add (marici-succ b) (marici-add (marici-succ a) r))))
      (marici-int-neg r)
      (marici-int-add (marici-int-pos a)
        (marici-int-add (marici-int-pos b)
          (marici-int-neg
            (marici-add (marici-succ b) (marici-add (marici-succ a) r)))))
      (concat MariciInt
        (marici-int-add (marici-int-pos (marici-succ (marici-add a b)))
          (marici-int-neg
            (marici-add (marici-succ b) (marici-add (marici-succ a) r))))
        (marici-int-add (marici-int-pos (marici-succ (marici-add a b)))
          (marici-int-neg
            (marici-add
              (marici-succ (marici-succ (marici-add a b))) r)))
        (marici-int-neg r)
        (ap MariciNat MariciInt
          (marici-add (marici-succ b) (marici-add (marici-succ a) r))
          (marici-add (marici-succ (marici-succ (marici-add a b))) r)
          (\ predecessor →
            marici-int-add
              (marici-int-pos (marici-succ (marici-add a b)))
              (marici-int-neg predecessor))
          (marici-two-positive-gap-reassociate a b r))
        (marici-int-add-pos-neg-negative-gap
          (marici-succ (marici-add a b)) r))
      (rev MariciInt
        (marici-int-add (marici-int-pos a)
          (marici-int-add (marici-int-pos b)
            (marici-int-neg
              (marici-add (marici-succ b) (marici-add (marici-succ a) r)))))
        (marici-int-neg r)
        (concat MariciInt
          (marici-int-add (marici-int-pos a)
            (marici-int-add (marici-int-pos b)
              (marici-int-neg
                (marici-add (marici-succ b)
                  (marici-add (marici-succ a) r)))))
          (marici-int-add (marici-int-pos a)
            (marici-int-neg (marici-add (marici-succ a) r)))
          (marici-int-neg r)
          (ap MariciInt MariciInt
            (marici-int-add (marici-int-pos b)
              (marici-int-neg
                (marici-add (marici-succ b)
                  (marici-add (marici-succ a) r))))
            (marici-int-neg (marici-add (marici-succ a) r))
            (\ value → marici-int-add (marici-int-pos a) value)
            (marici-int-add-pos-neg-negative-gap b
              (marici-add (marici-succ a) r)))
          (marici-int-add-pos-neg-negative-gap a r)))
```

## Boundary

The entire region where the negative third magnitude dominates the sum of the
two positive magnitudes is checked. Together with sign reversal this covers the
opposite region. Intermediate regions, where the third term dominates the
middle term but not the positive pair, still require residual-positive outer
normalization.
