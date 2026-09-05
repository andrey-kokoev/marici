# Bounded positive-cofactor decision

A bounded decision either supplies a factorization with a cofactor in the
bounded interval or refutes every factorization whose cofactor lies in that
interval.

```rzk
#lang rzk-1
```

```rzk
#data MariciBoundedPositiveCofactorDecision
  ( bound factor value : MariciNat)
  := marici-bounded-positive-cofactor-found
      ( cofactor : MariciNat)
      ( bounded : MariciNatAtMost cofactor bound)
      ( equation : marici-mul
        (marici-succ cofactor) (marici-succ factor)
        =_{MariciNat} marici-succ value)
  | marici-bounded-positive-cofactor-absent
      ( refutation : (cofactor : MariciNat)
        → MariciNatAtMost cofactor bound
        → (marici-mul (marici-succ cofactor) (marici-succ factor)
          =_{MariciNat} marici-succ value)
        → MariciEmpty)
```

```rzk
#define marici-at-most-zero-equal-zero
  ( q : MariciNat)
  ( bounded : MariciNatAtMost q marici-zero)
  : q =_{MariciNat} marici-zero
  := match bounded
      ( marici-nat-at-most-witness gap equation ⇒
          (match gap into
            (\ g → (marici-add g q =_{MariciNat} marici-zero)
              → q =_{MariciNat} marici-zero)
          ( marici-zero ⇒ \ e → e
          | marici-succ h ih ⇒ \ e →
              marici-empty-elim (q =_{MariciNat} marici-zero)
                (marici-succ-not-zero (marici-add h q) e))) equation)

#define marici-reindex-positive-cofactor-equation
  ( q q-prime factor value : MariciNat)
  ( p : q =_{MariciNat} q-prime)
  ( e : marici-mul (marici-succ q) (marici-succ factor)
    =_{MariciNat} marici-succ value)
  : marici-mul (marici-succ q-prime) (marici-succ factor)
    =_{MariciNat} marici-succ value
  := transport MariciNat
      (\ x → marici-mul (marici-succ x) (marici-succ factor)
        =_{MariciNat} marici-succ value)
      q q-prime p e
```

```rzk
#define marici-decide-positive-cofactor-bounded
  ( bound factor value : MariciNat)
  : MariciBoundedPositiveCofactorDecision bound factor value
  := match bound
      ( marici-zero ⇒ match (marici-nat-decide-equality
          (marici-mul marici-one (marici-succ factor))
          (marici-succ value))
          ( marici-nat-equal equation ⇒
              marici-bounded-positive-cofactor-found
                marici-zero factor value marici-zero
                (marici-nat-at-most-witness
                  marici-zero marici-zero marici-zero refl)
                equation
          | marici-nat-unequal not-equal ⇒
              marici-bounded-positive-cofactor-absent
                marici-zero factor value
                (\ q bounded e →
                  not-equal
                    (marici-reindex-positive-cofactor-equation
                      q marici-zero factor value
                      (marici-at-most-zero-equal-zero q bounded) e)))
      | marici-succ n previous ⇒
          match (marici-nat-decide-equality
            (marici-mul (marici-succ (marici-succ n))
              (marici-succ factor))
            (marici-succ value))
            ( marici-nat-equal endpoint ⇒
                marici-bounded-positive-cofactor-found
                  (marici-succ n) factor value (marici-succ n)
                  (marici-nat-at-most-witness
                    (marici-succ n) (marici-succ n) marici-zero refl)
                  endpoint
            | marici-nat-unequal not-endpoint ⇒ match previous
                ( marici-bounded-positive-cofactor-found q bounded equation ⇒
                    marici-bounded-positive-cofactor-found
                      (marici-succ n) factor value q
                      (marici-at-most-lift-successor q n bounded) equation
                | marici-bounded-positive-cofactor-absent prior ⇒
                    marici-bounded-positive-cofactor-absent
                      (marici-succ n) factor value
                      (\ q bounded e →
                        match (marici-at-most-successor-split q n bounded)
                          ( marici-at-most-strictly-below-successor below ⇒
                              prior q below e
                          | marici-at-most-equal-successor at-endpoint ⇒
                              not-endpoint
                                (marici-reindex-positive-cofactor-equation
                                  q (marici-succ n) factor value
                                  at-endpoint e))))))
```

## Boundary

The bounded search now returns universal refutation evidence rather than an
execution log. Applying it with target predecessor as bound is complete by the
cofactor-bound theorem; the unbounded divisibility decision is the next step.
