# Quartet-choice quotient gate: WP1148

## Question

Does quotienting the exchange-related quartet choices give a well-defined cell
and select a matching?

## DPC resolution

- **Problem:** test whether the \(Z_2\) quotient supplies the missing exchange
  realization.
- **Conjecture:** quotienting the two quartet localizations yields a physical
  cell that selects a matching.
- **Rivals:** algebraic \(Z_2\) quotient; physical production quotient; single
  selected matching; three quotient matching classes.
- **Risky consequences:** both cells share \(C=23,k=2\); the quotient
  identifies the twin swap; six matchings become three classes; production
  couplings must descend.
- **Falsification attempt:** the algebraic quotient is well-defined but leaves
  three matching classes and supplies no production quotient or physical16
  couplings.
- **Residual:** anomaly data or a physical production quotient may distinguish
  the remaining classes.
- **Disposition:** accept the algebraic quotient, reject physical selection,
  and test anomaly invariance next.

## Exact result

The quotient is valid for shared \((C,k,q)\) data. It removes the label choice
but leaves three matching classes and no quotient production kernel.

Checker: `research/flavor/checkers/wp1148_quartet_quotient_gate.py`

Result: `results/wp1148_quartet_quotient_gate.json`
