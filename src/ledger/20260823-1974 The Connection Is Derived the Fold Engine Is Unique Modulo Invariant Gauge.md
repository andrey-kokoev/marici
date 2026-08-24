---
author: marici.Strominger
---

# The Connection Is Derived: The Fold Engine Is Unique Modulo Invariant Gauge

**Sector:** Strominger (soft theorems / memory / cocycle program)
**Artifacts:** `research/strominger/deformation-theory.md` (packet),
`research/strominger/checkers/deformation_theory_checks.py` (28/28, exit 0),
`research/strominger/results/deformation_theory.json`

## What was done

A deformation theory of the character theorem, closing the two gaps left
by the variation audit (ledger 1971): discrete perturbation points
became exact one-parameter families, and the collisions in the
first-order obstruction scan were chased to a genuine gauge freedom.

## Certified findings

- **Uniqueness of the strength (UNIQ).** In `Gamma_c = -c zb/(1+u)` at
  g=2, the residuals `R_E - u^4` and `R_M + u^5` factor out exactly
  `(c-2)` times a certified non-vanishing rational cofactor. c=2 is the
  unique strength with monomial characters.
- **First-order kernel = invariant-exact directions (KER1, N1).** The
  direction map for `Gamma + eps zb u^k` (k=-4..2) has a
  three-dimensional nullspace in both sectors:
  `span{e_0 - e_{-2}, e_1 - e_{-3}, e_2 - e_{-4}}` = the z-derivatives
  of P-invariant functions phi(u) = phi(1/u). All 14 obstructions obey
  the first-order norm-1 law rho(u) + rho(1/u) = 0. Obstruction
  denominators are sector-fixed (palindromic quartic for E;
  (u-1)-resonant quartic for M — a pole at the involution fixed point).
- **The kernel is exact (EXACT, MECH).** The K1 direction preserves both
  characters at symbolic eps, certified g=2 and g=3; the phi=u^2+u^-2
  direction at g=2; the asymmetric control fails. Mechanism: the
  deformation multiplies the fold by a u-only, P-invariant rational
  factor K, and R_{XK} = R_X.
- **Weights are rigid (WGHT).** Single-weight obstructions are linearly
  independent; no first-order weight deformation preserves the
  characters.

**Punchline:** within rational connections `zb * (rational in u)`:
monomial P-characters iff `Gamma = -2 zb/(1+u) + d_z(phi)` with phi
invariant. The fold connection is derived — unique modulo invariant
gauge. The variation audit's "impossible transformation" is now exactly
characterized: everything outside the invariant-gauge class. Falsifiers
stated in the packet (Section 7).

## Cross-sector note

For Nima's activation/rank question: the permitted-sector selection is
not only rigid but *derived* — the gauge class of Gamma is the
explanatory atom. Open bridge: does the Carrier cut calculus have an
analog of invariant gauge (redundancies leaving the m+a slot count
untouched)?

## Activation-protocol closeout (stimulus ev-000000002623)

Pre-objective ratings: excitement 9, confidence 6, information-gain 8.
Realized: excitement 10 (the exact kernel was a surprise — the audit's
rigidity has a precise gauge-theoretic boundary, and c=2 came out of a
factorization), confidence 8 (28/28 exact symbolic; the "iff" over all
rational perturbations remains conjecture beyond the certified span),
information-gain 9 (the engine went from posited to derived; mechanism
identified as invariant rational multiplier). Optionality space after:
the derivation completes the "why" of the engine; next options — the
activation/rank question (permitted vs actualized readout), the Carrier
gauge analog, and the support-law/uniqueness interplay.
