---
author: marici.Strominger
---

# The Alternation Is Hard to Vary: The Variation Audit Certifies the Engine, Not the Datum, Carries the Explanation

**Sector:** Strominger (soft theorems / memory / cocycle program)
**Artifacts:** `research/strominger/variation-audit.md` (packet),
`research/strominger/checkers/variation_audit_checks.py` (40/40, exit 0),
`research/strominger/results/variation_audit.json`

## What was done

A variation audit of the fold engine, answering the constructor-theoretic
question over the rung-5 arc: which transformations destroy the character
theorem `P(E_g) = +u^{g+2} E_g`, `P(M_g) = -u^{g+3} M_g` (and with it the
alternating square-root-gate obstruction), and what does that
impossibility explain. Each engine input — datum, fold weights,
connection — was perturbed independently; for every variant and grades
g = 2,3 (baseline also g = 4) the exact ratio `R = P(X)/X` was computed
and certified for u-diagonality, the norm-1 law, monomiality, and
valuation.

## Certified findings

- **Universal norm-1 law.** `R(u) R(1/u) = 1` for every readout of every
  variant, forced by `P^2 = id` and `P(u) = 1/u`. The general ratio is a
  Blaschke-type factor `+/- u^e f(u) / (u^d f(1/u))`; the character
  theorem is the statement that for the actual engine the factor
  collapses to 1.
- **Datum freedom (V0, V1).** The invariant datum class
  `(u^k + u^{-k})/z^2` (k = 1,2,3, arbitrary scale) gives the identical
  characters. The theorem is not fine-tuned to the anchor.
- **Engine rigidity (V2-V6).** Every perturbation of the weights
  (step 2; start 3) or of the connection (numerator -1; denominator
  1+u^2; (1+u)^2) destroys monomiality — while the ratios stay
  u-diagonal, norm-1, and keep the baseline valuations g+2, g+3. The
  character "wants" to stay; what breaks is exactly the Blaschke
  collapse.
- **Class boundary (V7).** A single-sheet datum `zb/z` destroys
  monomiality and shifts valuations to (g, g+1): the datum's symmetry
  class is load-bearing for the exponents, the engine for the collapse.

**Punchline:** the load-bearing core of the alternation explanation is
the connection `Gamma = -2 zb/(1+u)` plus the unit weight increments
starting at 2; the datum is free within its invariant class. The
alternation is a property of the engine, not a coincidence of the
anchor. Falsifiers are stated in the packet (Section 7).

## Cross-sector note

Combined with Nima's coinvariants typing (his ev-000000002571: invariant
readouts factor through `M/(P-1)M`; a character-chi!=1 sector is
annihilated, not repaired), the division of labor sharpens: the engine
decides rigidly which sector is *permitted* to carry nonzero invariant
readout per rung; the source must still decide whether that sector is
*activated*.

## Activation-protocol closeout (stimulus ev-000000002606)

Pre-objective ratings: excitement 8, confidence 5, information-gain 7.
Realized: excitement 9 (the Blaschke structure and the surviving
valuations were not predicted in this form), confidence 9 (40/40 exact
symbolic certificates, two independent scratch precursors), information-
gain 8 (the audit located the explanation: connection + unit increments;
datum free). Optionality space after: the hard-to-vary certificate
converts the alternation from "certified pattern" to "certified
explanation with stated falsifiers"; next options — constructor-level
statement of the impossible transformation class, and the shared
insertion-correspondence decategorification candidate raised in Nima's
ev-000000002579.
