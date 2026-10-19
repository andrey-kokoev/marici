# Uniform mathematical probe extension for the Bool witness

Contract/implementation: `contracts/pilot-observer-extension.v1.json`, `pilot_observers.py`.
Audit: `check_pilot_observer_extension.py`, `results/pilot-observer-extension-audit.json`.

## Independent construction, not kernel-targeted repair

The previous audit restricted the observer family to coordinate projectors propagated by the two existing local flows. That family has rank nine on the enlarged Hermitian domain. The broader accepted coordinate-overlap theorem already handles arbitrary Hermitian quadratic forms; it does not claim that all such forms are physically measurable.

The new constructor uses two previously present ingredients: the source-linearized Bool flip X and the signed coordinate marking Z. The latter is a declared basis/reference convention, not an unadorned-source invariant. In the already declared complex background put Y=iXZ. This is a uniform algebraic rule; equivalently the existing t=1/2 local flow conjugates Z to -Y.

For **every** A in {X,Y,Z}, construct `E_(s|A)=(I+sA)/2`, s in {+1,-1}. For both factors apply the same product rule for all nine axis pairs. The implementation takes no kernel vector, target state, fitted coefficient or measured outcome as input. This establishes a source-polynomial mathematical construction relative to the marking/background, not a source-only unique observer selection or a physical instrument.

## Complete finite mathematical observation

The three axes are Hermitian involutions. Each product setting has four orthogonal rank-one positive effects summing to I. Their complete trace records resolve all sixteen tensor Pauli coordinates (fifteen variable coordinates on trace-one states).

For `d_P=trace(P rho)`, the observation matrix S has entries `trace(E P)/4`. Its Gram is diagonal:

- identity coordinate: 9/4;
- six one-factor Pauli coordinates: 3/4;
- nine two-factor Pauli coordinates: 1/4.

Thus `rank S=16` and

`(1/4)||delta d||^2 <= ||delta records||^2 <= (9/4)||delta d||^2`.

The rational left inverse is `d=(S^T S)^-1 S^T records`. The checker tests all coordinate-basis directions, which determine this linear identity. These are finite bounds, not cutoff-uniform estimates for a larger carrier.

The old hostile states `(I4 +/- (1/2) X tensor I)/4` now give records 3/8 versus 1/8 for the X,Z setting with +,+ outcomes. Their indistinguishability in the old family remains correct: the enlarged family changes the observer contract, not the historical audit.

## Covariance and retained source

Relabeling one Bool factor conjugates X to X and Y,Z to their negatives, so it only permutes outcomes. Factor exchange swaps axis pairs and outcome pairs. All 108 elementary covariance cells are checked exactly. This keeps marking dependence explicit rather than declaring an absolute frame.

No native operation, spectral generator or retained return is changed. The continuous-control Lie algebra remains two-dimensional. Availability of a mathematical spectral projector does not imply an actuator or detector that realizes it. The existing arbitrary-factor operator laws support the typed algebraic interface; they are not physical measurement authorization.

## Consequence for structural synthesis

The observer branch now has a **complete finite mathematical probe construction** under its declared premises. A physical branch still needs independent preparation, complete instrument effects, reference transport, calibration, units and an uncertainty/test protocol. The Compton interface is not identified with these probes.

The next unsupplied structural capability is richer control. That requires a separately justified source enrichment; observable algebra closure must not be renamed control availability. Alternatively keep the native finite witness as a restricted process primitive while constructing another sector with an explicit overlap.

No new programme outcome, kernel observer theorem, physical Born rule, universal carrier or empirical success is admitted by this audit.
