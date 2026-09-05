# Cauchy equivalence law package

The separately proved reflexive, symmetric, and transitive operations are
assembled into one typed law object. A completion quotient can consume this
package without importing the quantitative proofs individually.

```rzk
#lang rzk-1
```

```rzk
#data MariciRationalCauchyEquivalenceLaws
  := marici-rational-cauchy-equivalence-laws
      ( reflexive : (x : MariciRationalCauchySequence)
        → MariciRationalCauchySequencesEquivalent x x)
      ( symmetric : (x y : MariciRationalCauchySequence)
        → MariciRationalCauchySequencesEquivalent x y
        → MariciRationalCauchySequencesEquivalent y x)
      ( transitive : (x y z : MariciRationalCauchySequence)
        → MariciRationalCauchySequencesEquivalent x y
        → MariciRationalCauchySequencesEquivalent y z
        → MariciRationalCauchySequencesEquivalent x z)

#define marici-rational-cauchy-equivalence-law-package
  : MariciRationalCauchyEquivalenceLaws
  := marici-rational-cauchy-equivalence-laws
      marici-rational-cauchy-sequences-equivalent-reflexive
      marici-rational-cauchy-sequences-equivalent-symmetric
      marici-rational-cauchy-sequences-equivalent-transitive
```

## Boundary

The Cauchy completion relation is now supplied with an explicit equivalence-law
package. No quotient, identity type, real carrier, or quotient eliminator is
inferred from this package; constructing those objects requires an admitted Rzk
set-quotient or an independently proved canonical-representative construction.
