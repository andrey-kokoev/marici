# Bounded cofactor search with rejection evidence

A rejection log records each tested cofactor and its refutation. The traced
search either returns an exact factorization or a log containing every failed
test performed by its fuel recursion.

```rzk
#lang rzk-1
```

```rzk
#data MariciPositiveCofactorRejectionLog
  ( factor-predecessor value-predecessor : MariciNat)
  := marici-positive-cofactor-rejection-log-empty
  | marici-positive-cofactor-rejection-log-cons
      ( candidate-predecessor : MariciNat)
      ( refutation :
        (marici-mul
          (marici-succ candidate-predecessor)
          (marici-succ factor-predecessor)
        =_{MariciNat} marici-succ value-predecessor) → MariciEmpty)
      ( earlier : MariciPositiveCofactorRejectionLog
          factor-predecessor value-predecessor)

#data MariciTracedPositiveCofactorSearch
  ( factor-predecessor value-predecessor : MariciNat)
  := marici-traced-positive-cofactor-search-hit
      ( cofactor-predecessor : MariciNat)
      ( equation : marici-mul
          (marici-succ cofactor-predecessor)
          (marici-succ factor-predecessor)
        =_{MariciNat} marici-succ value-predecessor)
  | marici-traced-positive-cofactor-search-miss
      ( rejection-log : MariciPositiveCofactorRejectionLog
          factor-predecessor value-predecessor)
```

```rzk
#define marici-search-positive-cofactor-traced
  ( fuel factor value : MariciNat)
  : MariciTracedPositiveCofactorSearch factor value
  := match fuel
      ( marici-zero ⇒
          marici-traced-positive-cofactor-search-miss factor value
            (marici-positive-cofactor-rejection-log-empty factor value)
      | marici-succ remaining recurse ⇒
          match (marici-nat-decide-equality
            (marici-mul (marici-succ remaining) (marici-succ factor))
            (marici-succ value))
            ( marici-nat-equal equation ⇒
                marici-traced-positive-cofactor-search-hit
                  factor value remaining equation
            | marici-nat-unequal refutation ⇒ match recurse
                ( marici-traced-positive-cofactor-search-hit q equation ⇒
                    marici-traced-positive-cofactor-search-hit
                      factor value q equation
                | marici-traced-positive-cofactor-search-miss log ⇒
                    marici-traced-positive-cofactor-search-miss factor value
                      (marici-positive-cofactor-rejection-log-cons
                        factor value remaining refutation log))))
```

## Boundary

Search misses now retain every failed equality test rather than an untyped
failure marker. A coverage theorem relating the log to all positive cofactors
within the fuel bound, followed by a proof that the chosen bound is complete,
remains before misses imply nondivisibility.
