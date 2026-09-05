# Integer associativity transports across sign reversal

The global negation/addition compatibility theorem rewrites the negation of
each nested sum into the corresponding sum of negated inputs. Applying
negation to an associativity path therefore supplies its simultaneous
sign-reversed face.

```rzk
#lang rzk-1
```

```rzk
#define MariciIntAddAssociates
  ( x y z : MariciInt)
  : U
  := marici-int-add (marici-int-add x y) z
    =_{MariciInt}
    marici-int-add x (marici-int-add y z)

#define marici-int-negate-left-associated
  ( x y z : MariciInt)
  : marici-int-negate (marici-int-add (marici-int-add x y) z)
    =_{MariciInt}
    marici-int-add
      (marici-int-add (marici-int-negate x) (marici-int-negate y))
      (marici-int-negate z)
  := concat MariciInt
      (marici-int-negate (marici-int-add (marici-int-add x y) z))
      (marici-int-add
        (marici-int-negate (marici-int-add x y))
        (marici-int-negate z))
      (marici-int-add
        (marici-int-add (marici-int-negate x) (marici-int-negate y))
        (marici-int-negate z))
      (marici-int-negate-add (marici-int-add x y) z)
      (ap MariciInt MariciInt
        (marici-int-negate (marici-int-add x y))
        (marici-int-add (marici-int-negate x) (marici-int-negate y))
        (\ value → marici-int-add value (marici-int-negate z))
        (marici-int-negate-add x y))

#define marici-int-negate-right-associated
  ( x y z : MariciInt)
  : marici-int-negate (marici-int-add x (marici-int-add y z))
    =_{MariciInt}
    marici-int-add (marici-int-negate x)
      (marici-int-add (marici-int-negate y) (marici-int-negate z))
  := concat MariciInt
      (marici-int-negate (marici-int-add x (marici-int-add y z)))
      (marici-int-add (marici-int-negate x)
        (marici-int-negate (marici-int-add y z)))
      (marici-int-add (marici-int-negate x)
        (marici-int-add (marici-int-negate y) (marici-int-negate z)))
      (marici-int-negate-add x (marici-int-add y z))
      (ap MariciInt MariciInt
        (marici-int-negate (marici-int-add y z))
        (marici-int-add (marici-int-negate y) (marici-int-negate z))
        (\ value → marici-int-add (marici-int-negate x) value)
        (marici-int-negate-add y z))

#define marici-int-add-assoc-sign-reversal
  ( x y z : MariciInt)
  ( associates : MariciIntAddAssociates x y z)
  : MariciIntAddAssociates
      (marici-int-negate x) (marici-int-negate y) (marici-int-negate z)
  := concat MariciInt
      (marici-int-add
        (marici-int-add (marici-int-negate x) (marici-int-negate y))
        (marici-int-negate z))
      (marici-int-negate (marici-int-add (marici-int-add x y) z))
      (marici-int-add (marici-int-negate x)
        (marici-int-add (marici-int-negate y) (marici-int-negate z)))
      (rev MariciInt
        (marici-int-negate (marici-int-add (marici-int-add x y) z))
        (marici-int-add
          (marici-int-add (marici-int-negate x) (marici-int-negate y))
          (marici-int-negate z))
        (marici-int-negate-left-associated x y z))
      (concat MariciInt
        (marici-int-negate (marici-int-add (marici-int-add x y) z))
        (marici-int-negate (marici-int-add x (marici-int-add y z)))
        (marici-int-add (marici-int-negate x)
          (marici-int-add (marici-int-negate y) (marici-int-negate z)))
        (ap MariciInt MariciInt
          (marici-int-add (marici-int-add x y) z)
          (marici-int-add x (marici-int-add y z))
          marici-int-negate associates)
        (marici-int-negate-right-associated x y z))
```

## Boundary

The eight nonzero sign faces now occur in four sign-reversal pairs. Proving
one representative of each pair is sufficient; this transport does not prove
those four representative mixed normalization identities.
