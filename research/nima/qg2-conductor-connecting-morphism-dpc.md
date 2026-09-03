# `q_g2` conductor connecting morphism: second conjecture cycle

## Problem

The local DNC face exists without a coefficient. The `q_g2` subleading logarithmic form has sourced endpoint and conductor poles, so its conductor connecting morphism may supply the missing weight.

## Bold conjecture

The oriented finite-residue sum, divided by the labeled collision Euler factor `kappa-1`, is the conductor connecting coefficient:

\[
\delta_{\rm cond}=-\frac{r_{-1}+r_{-\kappa}}{\kappa-1}.
\]

It equals the missing Čech-face coefficient.

## Named rivals

1. the normalized wall square root has opposite Kummer character at the conductor, so the residues subtract and the connecting map vanishes;
2. the collision Euler factor enters with another orientation or without inversion;
3. the finite-residue sum closes the node exactly with trivial wall character.

## Risky consequences

The endpoint and conductor residues must be independently equal, and the resulting coefficient must match

\[
-\frac{1}{32p^4(\kappa-1)^2}
\]

without fitting. The opposite-character test must give a distinct result.

## Strongest falsification attempt and residual

For the exact grade `-1` `q_g2` subleading form, execution `structured_command_execution:e_7396_1788302952437258900_8` gives

\[
r_{-1}=r_{-\kappa}
=\frac{1}{64p^4(\kappa-1)},
\]

and

\[
r_\infty=-\frac{1}{32p^4(\kappa-1)}.
\]

Therefore

\[
-\frac{r_{-1}+r_{-\kappa}}{\kappa-1}
=-\frac{1}{32p^4(\kappa-1)^2},
\]

exactly the required coefficient.

The strongest local-system falsifier assigns opposite character to the conductor residue. It produces zero rather than the target. Thus the conjecture survives algebraically only for trivial relative Kummer character on the normalized `q_g2` wall.

## Disposition and residual conjecture

The previously unexplained coefficient is exactly reconstructed by a conductor connecting formula; this is not a fitted numerical coincidence because both finite residues and the collision factor were independently derived. The remaining conjecture is narrower: the exact-square restriction

\[
K_{\rm exc}|_{q_{g2}}=16p^4(\kappa+\xi)^2
\]

trivializes the relative Kummer character on the normalized wall, and the oriented connecting morphism uses the inverse Euler factor `-(kappa-1)^{-1}`. Ambient sheet transport and Gysin orientation must prove those two structural choices before promoting algebraic closure to a source-typed morphism.

## Evidence

- `research/nima/checkers/check_qg2_conductor_connecting_morphism.py`
- `research/nima/qg2-graded-extension-laurent-dpc.md`
- `research/benincasa/p6-soft-cusp-kummer.md`
