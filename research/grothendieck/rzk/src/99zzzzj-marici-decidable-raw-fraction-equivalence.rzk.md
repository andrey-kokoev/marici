# Raw-fraction equivalence is decidable by normalization

The executable component-equality decision on normalized representatives can
now be reinterpreted exactly. Its positive branch reflects to raw equivalence;
its negative branch refutes raw equivalence because equivalence would force
normalized equality.

```rzk
#lang rzk-1
```

```rzk
#data MariciRawFractionEquivalenceDecision
  ( p q : MariciRawFraction)
  := marici-raw-fractions-equivalent
      ( witness : marici-raw-fraction-equivalent p q)
  | marici-raw-fractions-not-equivalent
      ( refutation : marici-raw-fraction-equivalent p q → MariciEmpty)

#define marici-raw-fraction-decide-equivalence
  ( p q : MariciRawFraction)
  : MariciRawFractionEquivalenceDecision p q
  := match (marici-normalized-representatives-decide-equality p q)
      ( marici-raw-fractions-equal normalized-equal ⇒
          marici-raw-fractions-equivalent p q
            (marici-raw-fraction-equivalent-if-normalized-equal
              p q normalized-equal)
      | marici-raw-fractions-unequal normalized-refutation ⇒
          marici-raw-fractions-not-equivalent p q
            (\ equivalent → normalized-refutation
              (marici-normalized-raw-representatives-respect-equivalence
                p q equivalent)))
```

## Boundary

Raw positive-denominator fraction equivalence now has a total decision
procedure whose branches carry either an equivalence witness or a refutation.
The computation normalizes both presentations and compares canonical integer
and natural components. This completes the bounded canonical rational
normalization objective and supplies the exact presentation-independent
comparison test required downstream. Full additive rational laws remain a
separate branch blocked by mixed-sign integer addition associativity.
