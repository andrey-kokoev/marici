# Ordered Čech face: fourth conjecture cycle

## Problem

The complete `q_g2` grade `-1` Laurent coefficient leaves the node residual

\[
\frac{1}{32p^4(\kappa-1)^2}.
\]

A prior relative-residue construction closed an analogous vector by adjoining an oppositely oriented ordered Čech face.

## Bold conjecture

The source iterated residue on the ordered `q_g1/q_g2` face, with the appropriate orientation, equals

\[
-\frac{1}{32p^4(\kappa-1)^2}
\]

and closes the grade `-1` total-complex differential.

## Named rivals

1. reversing the iterated-residue orientation supplies the coefficient;
2. the Čech face is an independent relative-chain generator rather than an iterated residue of the bulk form;
3. no source face exists and the residue vector remains unclosed.

## Risky consequences

One of the two oriented iterated residues must equal the required coefficient as a rational function of generic `kappa,p`, not only on a special locus.

## Strongest falsification attempt and residual

The exact grade `-1` iterated residue inherited from `q_g2` is

\[
I_{12}=\frac{1}{64p^4(\kappa-1)}.
\]

Execution `structured_command_execution:e_7396_1788302611872740600_6` tests both orientations. Neither `I_12` nor `-I_12` equals the required face coefficient generically. The two resulting total residuals are

\[
\frac{\kappa+1}{64p^4(\kappa-1)^2}
\quad\text{and}\quad
-\frac{\kappa-3}{64p^4(\kappa-1)^2}.
\]

Equality occurs only at `kappa=-1` or `kappa=3`, respectively; these special loci do not define a generic face map. The bold conjecture is falsified.

Benincasa independently found that all two-by-two minors of the displayed conormal map for `x(xi+1)` and `x(kappa-1)` vanish on `x=0`; thus those equations alone do not supply an excess quotient or Gysin orientation.

## Disposition and residual conjecture

An ordered Čech face can close the residue vector only if a source independently supplies a relative-chain generator and its coefficient. It is not the oriented iterated residue of the existing bulk form. The next executable test is the local DNC construction: determine whether the ordered first-jet conormal data constructs a relative chain `Gamma` with the required boundary coefficient, or proves that an additional transverse equation is necessary.

## Evidence

- `research/nima/checkers/check_qg12_ordered_cech_face_residue.py`
- `research/voevodsky/cosmology-relative-residue-cocycle.md`
- `research/benincasa/results/qg2_excess_gysin_normal_bundle_dpc.json`
