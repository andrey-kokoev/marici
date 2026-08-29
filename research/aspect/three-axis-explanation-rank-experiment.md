# Three-axis explanation-rank experiment

The coherent refinement-loop apparatus permits an explanatory tomography rather than a single witness measurement.

## Independent controls

- `p`: visibility of the entangled Bell state;
- `gamma`: visibility of the local constructor-loop fringe;
- `phi`: phase of the local constructor loop.

The ideal observables are:

- inclusive Bell witness `S = 2 sqrt(2) p`;
- control quadrature `X = gamma cos(phi)`;
- control quadrature `Y = gamma sin(phi)`.

Their Jacobian with respect to `(p, gamma, phi)` has determinant `2 sqrt(2) gamma`. Thus the instrument resolves three independent explanatory coordinates whenever `gamma` is nonzero. At `gamma = 0`, the phase direction disappears and the observable rank falls from three to two.

This supplies an operational explanation of decoherence: it is a singular quotient of the comparison geometry. The underlying phase parameter may still occur in an implementation, but no admitted observable distinguishes it once the comparison visibility vanishes.

## Factorial experiment

Scan all preregistered combinations of Bell visibility, loop visibility, and loop phase. For each cell, acquire an immutable packet, pass the same-ledger pushforward auditor, and estimate `(S, X, Y)` without postselection. Fit the full three-parameter response and compare it with rank-one and rank-two latent alternatives.

The decisive signatures are:

- changing `gamma` at fixed `p` changes the fringe but not CHSH;
- changing `p` at fixed `gamma` changes CHSH but not the fringe;
- changing `phi` rotates `(X,Y)` at fixed `S` and fixed fringe magnitude;
- at `gamma = 0`, phase estimates become unidentified rather than arbitrarily zero.

A one-hidden-cause explanation predicts a response surface of rank at most one. The factorial interventions falsify it if the observed Jacobian is full rank. A coupling between controls is reported as apparatus cross-talk, not interpreted as a new physical law until independently reproduced.

The current execution is an exact mathematical fixture. Physical factorial packets remain unrun.
