# Mixed associativity when the positive middle term dominates

Write the positive middle predecessor as `(c+1)+r`, so its magnitude exceeds
the following negative magnitude `c+1`. The inner mixed sum normalizes to
positive `r`; natural reassociation presents the outer positive sum with the
same explicit gap, and both parenthesizations normalize to predecessor
`1+(a+r)`.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-middle-outer-gap-path
  ( a c r : MariciNat)
  : marici-succ
      (marici-add a (marici-add (marici-succ c) r))
    =_{MariciNat}
    marici-add (marici-succ c) (marici-succ (marici-add a r))
  := concat MariciNat
      (marici-succ
        (marici-add a (marici-add (marici-succ c) r)))
      (marici-succ
        (marici-add (marici-succ c) (marici-add a r)))
      (marici-add (marici-succ c) (marici-succ (marici-add a r)))
      (ap MariciNat MariciNat
        (marici-add a (marici-add (marici-succ c) r))
        (marici-add (marici-succ c) (marici-add a r))
        marici-succ
        (marici-add-swap-prefix a (marici-succ c) r))
      (rev MariciNat
        (marici-add (marici-succ c) (marici-succ (marici-add a r)))
        (marici-succ
          (marici-add (marici-succ c) (marici-add a r)))
        (marici-add-succ-right (marici-succ c) (marici-add a r)))

#define marici-int-add-assoc-positive-middle-dominates-negative
  ( a c r : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos a)
      (marici-int-pos (marici-add (marici-succ c) r))
      (marici-int-neg c)
  := concat MariciInt
      (marici-int-add
        (marici-int-add (marici-int-pos a)
          (marici-int-pos (marici-add (marici-succ c) r)))
        (marici-int-neg c))
      (marici-int-pos (marici-succ (marici-add a r)))
      (marici-int-add (marici-int-pos a)
        (marici-int-add
          (marici-int-pos (marici-add (marici-succ c) r))
          (marici-int-neg c)))
      (concat MariciInt
        (marici-int-add
          (marici-int-pos
            (marici-succ
              (marici-add a (marici-add (marici-succ c) r))))
          (marici-int-neg c))
        (marici-int-add
          (marici-int-pos
            (marici-add (marici-succ c)
              (marici-succ (marici-add a r))))
          (marici-int-neg c))
        (marici-int-pos (marici-succ (marici-add a r)))
        (ap MariciNat MariciInt
          (marici-succ
            (marici-add a (marici-add (marici-succ c) r)))
          (marici-add (marici-succ c)
            (marici-succ (marici-add a r)))
          (\ predecessor →
            marici-int-add (marici-int-pos predecessor) (marici-int-neg c))
          (marici-positive-middle-outer-gap-path a c r))
        (marici-int-add-pos-neg-gap c (marici-succ (marici-add a r))))
      (rev MariciInt
        (marici-int-add (marici-int-pos a)
          (marici-int-add
            (marici-int-pos (marici-add (marici-succ c) r))
            (marici-int-neg c)))
        (marici-int-pos (marici-succ (marici-add a r)))
        (concat MariciInt
          (marici-int-add (marici-int-pos a)
            (marici-int-add
              (marici-int-pos (marici-add (marici-succ c) r))
              (marici-int-neg c)))
          (marici-int-add (marici-int-pos a) (marici-int-pos r))
          (marici-int-pos (marici-succ (marici-add a r)))
          (ap MariciInt MariciInt
            (marici-int-add
              (marici-int-pos (marici-add (marici-succ c) r))
              (marici-int-neg c))
            (marici-int-pos r)
            (\ value → marici-int-add (marici-int-pos a) value)
            (marici-int-add-pos-neg-gap c r))
          refl))
```

## Boundary

One strict three-magnitude region of the two-positive/one-negative
associativity face is checked, together with its sign reversal via the existing
transport theorem. Equal middle/negative magnitudes were checked previously;
the region where the negative magnitude dominates the middle remains.
