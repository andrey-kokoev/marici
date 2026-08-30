# 2597 — The Cyclic Quadratic Connection Is Not a Constant-Residue Soft–Triangle Line

## Correction from Entry 2602

The tested scalar is the coefficient of pointwise derivative closure, not a
typed quotient connection. Its failure of the constant-residue model remains
correct as a finite algebraic result, but it cannot classify intrinsic
connection support. Entry 2602 supersedes that interpretation.

## Hard-to-vary claim

Let \(s_i=P_i^2\), and let \(\Lambda_P\) be the momentum-triangle
discriminant. The scalar connection induced on Entry 2593's horizontal
quadratic quotient line does not have the form

\[
\omega_i
=
c_{\rm soft}\,\partial_{s_i}\log(s_1s_2s_3)
+
c_\Lambda\,\partial_{s_i}\log\Lambda_P
\]

with kinematics-independent residues \(c_{\rm soft}\) and \(c_\Lambda\).

## Finite falsifier

The predeclared two-parameter model was tested at five generic
squared-momentum points away from both candidate divisors. Each point gives
three directional equations. The calculation was independently replicated
over primes 32003 and 65521.

After fitting two equations, 13 of the remaining 13 equations have nonzero
residual at each prime.

The implementation audit confirms that the derivative varies the overridden
\(P_i^2\) values in the complete Cayley--Menger polynomial and in every
labelled normal linear. Entry 2593's rank-four horizontality regression still
passes.

## Interpretation

This is a failure of the smallest constant-residue support model, not evidence
for a new divisor. In particular, the line remains a valid source-derived
coefficient port, but horizontality does not collapse its transport to the two
obvious logarithmic factors.

Adjoining another factor after inspecting the failed samples is prohibited.
The next admissible calculation is an exact or degree-certified reconstruction
of the scalar connection followed by gauge-invariant pole classification.

## Scope

No total-energy map, marked-relative lift, physical activation, or intrinsic
new support is established here.

## Artifacts

- `research/benincasa/cm-cyclic-connection-two-divisor-falsifier.md`
- `research/benincasa/checkers/check_cm_cyclic_connection_poles.py`
- `research/benincasa/results/cm-cyclic-connection-poles.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

Ledger sequence claim: `seqclaim-a38c94d6501f3b755ba1b21c`.

Epistemic event: `ev-000000003783-9a35f055-6f25-4ea4-b378-a8660b1f9292`.
