# Natural divisibility with arbitrary cofactors

The Euclid proof needs divisibility for arbitrary natural values, including
zero. This differs from the normalization search witness, whose value and
cofactor are structurally positive. The general relation retains its cofactor
and exact product equation.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatDivides
  ( divisor value : MariciNat)
  := marici-nat-divides-witness
      ( cofactor : MariciNat)
      ( equation : marici-mul cofactor divisor =_{MariciNat} value)

#define marici-nat-one-divides
  ( value : MariciNat)
  : MariciNatDivides (marici-succ marici-zero) value
  := marici-nat-divides-witness
      (marici-succ marici-zero) value value
      (marici-mul-one-right value)

#define marici-nat-divides-reflexive
  ( value : MariciNat)
  : MariciNatDivides value value
  := marici-nat-divides-witness value value
      (marici-succ marici-zero)
      (marici-mul-one-left value)

#define marici-nat-divides-zero
  ( divisor : MariciNat)
  : MariciNatDivides divisor marici-zero
  := marici-nat-divides-witness divisor marici-zero marici-zero
      (marici-mul-zero-left divisor)

#define marici-nat-divides-transitive
  ( divisor middle value : MariciNat)
  ( divides-middle : MariciNatDivides divisor middle)
  ( divides-value : MariciNatDivides middle value)
  : MariciNatDivides divisor value
  := match divides-middle
      ( marici-nat-divides-witness q equation-first ⇒ match divides-value
        ( marici-nat-divides-witness r equation-second ⇒
          marici-nat-divides-witness divisor value
            (marici-mul r q)
            (concat MariciNat
              (marici-mul (marici-mul r q) divisor)
              (marici-mul r (marici-mul q divisor))
              value
              (marici-mul-assoc r q divisor)
              (concat MariciNat
                (marici-mul r (marici-mul q divisor))
                (marici-mul r middle)
                value
                (ap MariciNat MariciNat
                  (marici-mul q divisor) middle
                  (\ x → marici-mul r x) equation-first)
                equation-second))))

#define marici-positive-right-divides-gives-nat-divides
  ( factor value : MariciNat)
  ( divides : MariciPositiveNatRightDivides factor value)
  : MariciNatDivides (marici-succ factor) (marici-succ value)
  := match divides
      ( marici-positive-nat-right-divides-witness q equation ⇒
          marici-nat-divides-witness
            (marici-succ factor) (marici-succ value)
            (marici-succ q) equation)
```

## Boundary

General natural divisibility now supports zero, reflexivity, unit divisors, and
transitivity, and receives every existing positive-divisibility witness. The
remaining Euclid construction can now be stated and proved without forcing
zero into a positive-cofactor encoding.
