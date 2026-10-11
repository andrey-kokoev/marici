# Exchange and composition certify supplied pair factors but do not select one

## Question

Do the current native composition/exchange rules restrict the helium pair factor beyond the supplied WG adapter's certificates? Active obligation: inspect the actual native signature, then test nonuniqueness under the declared spatial symmetry and readout-composition laws. This is not a new optimization of helium binding.

## Native source audit

`agda/NativeTableRules.agda` defines twelve rule kinds. A comparison's parameters include an equivalence and a proof that it takes one retained value to the other. Composition consumes two such comparisons and constructs their composite, retaining both parents. Higher comparison likewise requires its higher path as input. These schemas do not contain a pair-distance kernel, a Coulomb operator, or a physical energy-selection law.

The pair adapter's exchange proof is additional supplied data, not a new primitive exchange rule in that signature. Its application bridge is into the separately application-extended runtime and requires function/argument derivations. No result here shows that arbitrary factors can be generated from an unchanged old-native seed family.

## Formal and numerical countermodels

`agda/PairFactorSelectionAudit.agda` proves that for any exchange-invariant distance d and any function h, the factor h(d(x)) inherits exchange invariance. The resulting equality certificates compose twice for every h. A finite Boolean countermodel supplies two distinct factors with the same coincidence value and the same exchange property; their inequality is proved, not inferred from separate syntax.

For the concrete helium realization, fix the existing exponent and b=99/500. Use scaled distance u=zeta*r12 and compare

\[
F_c(u)=1+bu+cu^2,
\qquad c\in\{0,b^2/2,b^2\}.
\]

All three factors:

- are exchange invariant and positive for nonnegative separation;
- have coincidence value one and the same first derivative b in the scaled coordinate;
- remain normalizable with the fixed exponential envelope;
- obey multiplication-composition and exchange compatibility while construction records can remain ordered.

Their normalization integrals and Coulomb kinetic/potential readouts are calculated exactly. All three energies differ. No parameter was reoptimized to favor one example, and no helium target was used. The factor 1+b*r1 fails the exchange test, establishing that the test does impose a real constraint. Equality of first derivatives here is not a claim that the selected derivative satisfies the exact physical Coulomb cusp condition.

## Disposition

The tested coherence requirements rule out an asymmetric spatial factor for the declared singlet presentation but do not select the radial correlation function. This is a bounded nonuniqueness result, not a no-go theorem for additional native physics. An admissibility/selection law acting on the pair factor remains absent; repeating representation checks cannot supply it. A concrete new source law would need to separate these rivals without being chosen from the measured helium value.

Verification: exact executable test `python research/nima/checkers/check_pair_factor_selection.py` passed via `structured_command_execution:e_32876_1791225579610277600_31`; output `results/pair-factor-selection.json`. Fresh safe Cubical Agda verification of `agda/PairFactorSelectionAudit.agda` passed via `structured_command_execution:e_32876_1791225714324363700_32`, after correcting a missing product-type import. Receipt: `results/agda-PairFactorSelectionAudit.json`. No commit or publication is claimed.
