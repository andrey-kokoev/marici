# Lower-point face coefficient: first conjecture cycle

## Problem

Local DNC geometry supplies an oriented face generator but not its coefficient. The required coefficient is

\[
-\frac{1}{32p^4(\kappa-1)^2}.
\]

## Bold conjecture

Existing lower-point factorization or action-level normalization packets independently predict this coefficient and therefore weight the local DNC face.

## Named rivals

1. a two-point field-strength or three-point vertex normalization supplies the factor;
2. background/free-state counterterm insertions supply it;
3. no lower-point map is currently defined, and the coefficient belongs instead to conductor reduction or a physical relative chain.

## Risky consequences

The source packet must contain a defined insertion map with the same `p` and `kappa` dependence, obtained before comparison with the closure residual. A coefficient absent from the source or reconstructed from the target does not count.

## Strongest falsification attempt and residual

A bounded search of Benincasa source packets finds no occurrence of the required functional dependence. The action-level bridge states:

- the two-point divergence has momentum degree zero and generates no one-loop field-strength counterterm;
- the triangle generates no vertex counterterm;
- the surviving lower-point maps only impose zero one-point background and massless/conformal free-state normalization;
- their insertions into the labelled three-point wavefunction remain to be derived;
- the compatible parent action does not itself define a renormalization prescription.

The `q_G12` wall packet independently records normalization/conductor reduction and the Čech sum as the remaining test. Thus no existing lower-point map predicts the coefficient. The bold conjecture is falsified under the current source envelope.

## Disposition and residual conjecture

The coefficient is not presently lower-point normalization data. The surviving executable rival is intrinsic conductor reduction: the grade `-1` residual may be the boundary value of the `q_g2` endpoint-to-conductor logarithmic class after applying the conductor connecting morphism. This would derive the coefficient from the already sourced pole pair rather than from an absent counterterm map.

The next test is to compute the conductor connecting morphism on the two residues and compare its node component with the required coefficient, retaining twisted square-root character.

## Evidence

- `research/benincasa/action-level-renormalization-source-bridge.md`
- `research/benincasa/physical-g12-shared-wall-residues.json`
- `research/nima/qg12-local-dnc-chain-dpc.md`
