# Native Bool pilot: action, observation and finite stability

Contract: `contracts/pilot-capability-audit.v1.json`.
Checker/result: `check_pilot_capabilities.py`, `results/pilot-capability-audit.json`.

## What the audit asks

The finite fragment and spectral/realification transport establish a scoped realization. They do not determine how many controls or observers the source supplies. This audit uses the **same** native flips and local spectral flows, without adding a repair after examining the output.

The native domain is four source labels with retained records. For a stronger test, explicitly enlarge to Hermitian operators on the declared C4 linearization and use mathematical trace pairing. That enlargement and pairing are premises, not source-selected preparations or a derived Born rule. Failure on the larger domain does not undo separation of the original four labels.

## Gate 1: carrier splitting

P_L and P_R commute and square to I. Their four joint idempotents are

`Pi_(a,b)=(I+a P_L)(I+b P_R)/4`, with a,b in {+1,-1}.

They are mutually orthogonal self-adjoint rank-one projectors summing to I. Thus the declared finite linear carrier splits into four joint sectors. The checker verifies the exact identities and traces.

## Gate 2: action is not arbitrary control

The native discrete operations reach all four labels from one label. Their complex linear action algebra has basis `I,P_L,P_R,P_L P_R` and dimension four, whereas End(C4) has dimension sixteen.

The chosen continuous controls span `i Q_L,i Q_R`; their commutator vanishes. Hence the controlled Lie algebra is only two-dimensional. Adding an explicitly available global-phase control would give three dimensions, not u(4). Full arbitrary unitary control is not supplied.

Even the four joint sectors cannot receive arbitrary independent relative phases from the two existing controls: the joint-sector phase is the sum of its factor phases. A mixed-sector coefficient would be a new authorized control, not a consequence of commutation or a reinterpretation of the existing two Hamiltonians.

These are obstructions to specified stronger capability claims, not proof that every physical theory requires arbitrary u(4) control or that the original local construction fails.

## Gate 3: propagated observation has a seven-dimensional kernel

Predeclare all sixteen tensor Pauli directions from I,X,Y,Z. Native coordinate projectors span four Hermitian directions and separate the original four delta labels.

For the local spectral flow,

`U(t)=exp(-i*pi*t/2)[cos(pi*t/2) I+i sin(pi*t/2) X]`.

Its conjugated coordinate axis obeys

`U(t)* Z U(t)=cos(pi*t) Z-sin(pi*t) Y`.

Therefore **every** propagated coordinate projector lies in

`span{I,Y,Z} tensor span{I,Y,Z}`.

That provides the all-time dimension-nine upper bound; it is not inferred from sampling. At a,b in {0,1/2}, the four exact setting pairs reach all nine directions, proving the matching lower bound. Every Pauli direction with X in either factor is invisible: seven directions.

A concrete hostile is

`rho_plus/minus=(I4 +/- (1/2) X tensor I)/4`.

The two matrices differ, have trace one, and have positive eigenvalues 3/8 and 1/8, each twice. The checker supplies their positive-weight orthogonal-projector decomposition. They give identical records for every propagated coordinate effect by the all-time span bound. These are mathematical states, not independently authorized physical preparations.

On the trace-one tangent domain, the dimensions are fifteen total, eight visible and seven invisible. Retaining source/schedule records remains separate; a scalar observation kernel is not an endpoint or whole-Tick classification theorem.

## Gate 4: finite bounds only on the visible subspace

Use Pauli coordinates `d_P=trace(P rho)`, so `rho=(1/4)sum d_P P`. For the sixteen complete coordinate effects at the four spanning setting pairs, the observation Gram on the nine visible coordinates is diagonal:

- identity coordinate: 1;
- four one-factor Y/Z coordinates: 1/2;
- four two-factor Y/Z coordinates: 1/4.

Thus on the visible subspace,

`(1/4)||delta d||^2 <= ||delta records||^2 <= ||delta d||^2`.

On the full Hermitian domain the lower bound is zero, because of the explicit kernel. No cutoff-uniform bound for a growing or infinite carrier is claimed. On the original four-label domain the coordinate record map already separates labels; that narrower success is retained.

## Structural synthesis forks exposed by this audit

1. **Keep the native finite domain.** Use it as a checked local/process primitive without claiming a complete quantum state/control/observer model.
2. **Enlarge the source-authorized observer family.** Independent X-sensitive instruments would remove the identified observation gap mathematically, but their source, preparation and calibration must be justified. A kernel-targeted projector invented after this audit is not source authorization.
3. **Enlarge the source dynamics.** An independently justified mixed/entangling or additional control changes the source contract and the original locality assumptions; it is a new branch, not closure by renaming the existing flows.
4. **Change the common carrier.** A richer retained relational source might generate those capabilities. It needs its own typed embedding and preservation tests against the successful finite witness.

The immediate synthesis task is choosing the required state/control/observer domain and an independently justified source enrichment if that stronger domain is desired. A physical source/instrument bridge cannot be inferred from this audit. The Compton calibration pilot stays disconnected.

## Verification boundary

The audit result's `status: pass` means the ranks, projectors, kernel witness and finite bounds were checked exactly. It does **not** mean all capability gates pass. No proof-attempt outcome, physical authorization, new kernel theorem, infinite stability or programme root closure is generated.
