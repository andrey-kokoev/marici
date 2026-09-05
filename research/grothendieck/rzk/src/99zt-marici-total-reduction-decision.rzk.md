# Total reduction decision for raw-fraction components

Denominator one is already reduced. At a successor denominator predecessor,
the bounded nonunit-factor search uses the predecessor as its index bound;
absence becomes reducedness via the global common-factor bound.

```rzk
#lang rzk-1
```

```rzk
#define marici-decide-raw-components-reduction
  ( a : MariciInt)
  ( d : MariciNat)
  : MariciRawComponentsReductionDecision a d
  := match d
      ( marici-zero ⇒
          marici-raw-components-reduced a marici-zero
            (marici-unit-denominator-components-are-reduced a)
      | marici-succ n ih ⇒
          match (marici-decide-nonunit-common-factor-bounded
            n a (marici-succ n))
            ( marici-bounded-nonunit-common-factor-found
                f bounded certificate ⇒
                  marici-raw-components-reducible a (marici-succ n)
                    (marici-raw-components-nonunit-common-positive-factor
                      a (marici-succ n) f certificate)
            | marici-bounded-nonunit-common-factor-absent absent ⇒
                marici-raw-components-reduced a (marici-succ n)
                  (\ nonunit → match nonunit
                    ( marici-raw-components-nonunit-common-positive-factor
                        f certificate ⇒
                          absent f
                            (marici-at-most-successors-descend f n
                              (marici-common-positive-factor-at-most-denominator
                                a (marici-succ n) (marici-succ f)
                                certificate))
                            certificate))))
```

## Boundary

Every raw-fraction component pair now computes either an exact nonunit common
factor or constructive reducedness. Together with strict denominator decrease
and the recursive normalization algebra, only a well-founded recursion
construction remains for universal normalization existence.
