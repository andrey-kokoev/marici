# Local DNC relative chain: fifth conjecture cycle

## Problem

The ordered Čech face is not the bulk iterated residue. Prior DNC work suggests that ordered first-jet conormal data may instead construct an independent relative chain `Gamma`.

## Bold conjecture

The local DNC first jet constructs both the ordered `q_g1/q_g2` face generator and its required boundary coefficient

\[
-\frac{1}{32p^4(\kappa-1)^2}.
\]

## Named rivals

1. first-jet incidence constructs only an unweighted oriented face;
2. the unresolved exceptional/collision equations are too rank-deficient to construct a face at all;
3. the chain and coefficient have different sources, with the coefficient supplied by lower-point factorization or a physical relative-chain map.

## Risky consequences

The ordered conormal determinant must remain nonzero at the relevant collision and must independently produce the rational coefficient, including its `p` and `kappa` dependence.

## Strongest falsification attempt and residual

For the exceptional strict transforms

\[
u=\xi+1,
\qquad v=a-p,
\]

the ordered conormal determinant is one. Hence these coordinates construct an oriented, unweighted local face away from the collision.

For the unresolved exceptional and collision equations

\[
f=x(\xi+1),
\qquad g=x(\kappa-1),
\]

execution `structured_command_execution:e_7396_1788302745218153600_7` finds conormal rank one on the generic exceptional fiber and rank zero at `xi=-1, kappa=1`. Thus the collision equations do not construct a regular two-face. Neither the unit strict-transform determinant nor the rank-deficient collision map determines the required rational coefficient. The bold conjecture is falsified.

## Disposition and residual conjecture

The surviving scope splits cleanly:

- DNC incidence supplies an oriented local face generator `Gamma` from the independent strict-transform normals;
- it does not supply the coefficient;
- the collision locus requires additional transverse source data;
- a lower-point factorization map or explicit physical relative chain must determine the coefficient.

The residual conjecture is therefore that the missing coefficient is physical normalization data attached to the local DNC generator, not geometric incidence data. The acceptance test is a lower-point source packet that predicts the coefficient before comparison with the residue residual.

## Evidence

- `research/nima/checkers/check_qg12_local_dnc_chain.py`
- `research/benincasa/results/qg2_excess_gysin_normal_bundle_dpc.json`
- `research/voevodsky/cosmology-formal-neighborhood-dependence-of-witness.md`
