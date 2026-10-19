# Shared-leg controllability: energy task control, not full active control

## Disposition

29 exact checks pass. Controllability is not inferred from the existing38-coordinate energy observer.

The inspected prior family-disagreement law supplies a conditional COMMON GAIN, not independently writable comparison outputs. It can regulate the declared scalar energy downward while preserving family means, but cannot independently steer the whole active state.

No installed or physically admitted input matrix is supplied. The result is a mathematical control/preparation audit with explicit scope.

## Inputs grounded in prior research

Inspected:

- `research/nima/family-disagreement-preparation-law.md`: computed feedback from actual30 legs, incoming-target families, supplied common gain and retained old records;
- `research/nima/matrix-leg-preparation-exchange-closure.md`: independently changing comparison cells can leave the shared-leg preparation image;
- `research/nima/bilinear-branch-preparation-synthesis.md`: a span of products is not the same as one prepared product;
- `research/nima/control-theoretic-explanation-audit-protocol.md`: freeze admitted interventions before claiming controllability;
- `research/nima/commutant-separation-does-not-imply-sector-controllability.md`: visible sector separation does not provide independently executable sector controls;
- `research/nima/history-controlled-preparation.md`: reservoir and controller are supplied even in a conditional conservative preparation.

These prior notes are clues and boundaries, not physical actuator certificates. The new checker reruns the retained energy observer chain but does not independently replay all those unrelated prior suites.

## Coordinate counts: compare like with like

The native field has137 matrix-valued comparison slots, each with four response entries:548 scalar coefficient coordinates.

Its active observer has38 coordinates PER response channel, so the full matrix-valued active task has152 scalar coordinates. The stationary sector has396 scalar coordinates, or99 per channel.

The prepared source consists of30 shared2x2 legs:120 scalar leg coefficients. The independent reference is fixed and is not treated as a new input port.

Thus49 scalar active preparation directions must be compared with152, not with38.

## Primitive input map is differentiated, not assumed

For actual path values C_ij=Y_j X_i,

    delta C_ij=Y_j delta X_i+delta Y_j X_i.

The checker derives the548-by120 preparation Jacobian J from the actual30 matrix legs and labels each column by its source role, leg index and matrix entry. No B=I is installed on the137 responses.

At the supplied fixture:

- rank(J)=112;
- eight intermediate-factorization redundancy directions have zero response;
- rank((C_active tensor I4)J)=49.

The eight kernel directions come from deltaX=S X, deltaY=-Y S, separately in the arrow and state branches. This is an algebraic redundancy in the product response, not permission to identify physically distinct preparation budgets.

These Jacobian columns describe possible mathematical preparation variations, NOT120 independently admitted actuators. Small variations remain near the actual invertible legs. The labels by themselves do not provide hardware, forcing strengths or controller timing.

## A preparation ceiling, independent of one operating point

The active response ignores the stationary state branch. It depends on only22 arrow matrices, giving88 parameters, with four intermediate-factorization redundancy directions on the invertible shared-leg class.

Therefore its generic factored active-image dimension is at most84, below the152-dimensional ambient active task. At the supplied fixture its tangent rank is49.

Consequently arbitrary FINAL shared-leg preparations cannot fill every ambient active coefficient state while retaining this factorization. Histories that always finish as the same shared-leg products do not remove that ceiling.

This is not a claim that84 is attained, that49 is a Kalman reachable rank, or that every state in the152-dimensional ambient model is a physically admissible target. It distinguishes full ambient controllability from controllability within a specified prepared task manifold.

## The actual prior gain candidate is bilinear control

Let ell stack the120 primitive leg entries. D11 is the previously constructed interface-preserving arrow generator. L applies it to each arrow-leg bank, leaving the state legs stationary.

Let P replace each arrow leg by its original incoming-target-family mean. State legs have singleton families. Set Qleg=I-Pleg.

The existing discrete preparation law is

    ell_next=(Pleg+q Qleg)ell, q=1-eta.

For the audited contraction class, eta is in[0,1]. A NEW explicitly declared continuous-rate version is

    dot ell=L ell-u(t)Qleg ell, u(t)>=0.

This is BILINEAR/state-dependent input control, not an additive LTI force. The native output is also nonlinear: F_ij=Y_j X_i. A frozen constant-B Kalman calculation would not establish controllability of this actual system.

Exactly, L and Qleg commute. Hence

    ell(t)=exp(t L)(Pleg+q Qleg)ell_initial,
    q=exp(-integral u dt).

Free time plus integrated gain provide at most TWO continuous orbit parameters. At fixed time only the gain parameter remains. The checker finds rank2 at the supplied fixture both in the leg orbit and its active-response tangent.

Discrete gain schedules likewise collapse to one product of q factors. Interleaving gain and the exact drift step does not create new control directions.

The law is homogeneous: it cannot excite a zero leg state. Family-constant legs receive no drive. State legs are untouched. It can scale some stationary arrow disagreements, but cannot independently prepare the entire stationary sector.

## Positive result: scalar energy is conditionally regulatable

For the supplied preparation, the declared native Hamiltonian after relaxation is exactly

    H(q)=26 q^2(43 q^2+221)/675.

Family means and J4 remain unchanged. The controller changes retained active leaf data, not the reference or observation convention.

Since the quadratic and quartic coefficients are positive, the discrete gain law reaches any ENERGY VALUE in[0,H_initial] on this one-parameter preparation family. It does not reach an arbitrary state having that energy.

For H(q)=a q^2+b q^4 and target h in that range, a witness is

    q^2=2h/(a+sqrt(a^2+4bh)),
    eta=1-q.

The checker produces an exact half-energy witness for h=1144/225; equivalently,

    eta=1-sqrt((sqrt71545-221)/86).

It rejects a target above the initial energy rather than quietly turning a contraction gain into a source of excitation.

For the continuous-rate model, finite integrated gain reaches only positive q, so zero energy is a limit. The prior discrete eta=1 projection reaches zero visible energy while archiving the old data. These are different execution assumptions.

Retaining the kick recovers the old legs exactly. This is software/history retention, NOT a proof that discarded visible energy is physically disposed of for free or that the combined controller/archive is conservative. Pump, reservoir, back-action, reset and uncertainty remain unsupplied.

## What this says about the intuition

There is a concrete reachability–observability pairing for the scalar energy task: the new observer reads H, and the prior conditional gain law supplies exact downward energy targets.

There is NOT full controllability of the active field. The current scalar controller leaves a huge sector-selectivity gap, and even arbitrary shared-leg preparation cannot realize every ambient active state.

To claim more, provide source-admitted additional interventions: which leg/memory/reservoir ports are writable, their action and domain, normalization, schedule, resource budget and physical realization. Independently writable retained memory can change the preparation domain, but it is a NEW source operation, not something inferred from137 or from observability.

## Task-relevance follow-up

`energy-task-reduction.md` makes the narrower goal explicit: full independent mode control is not required for the original Hamiltonian-transport question.38 checks give a sufficient two-statistic energy summary under the existing gain law: one-leg and two-leg disagreement energies update by q^2 and q^4. Equal current total energy and family means can hide different next energies. No new actuator is introduced, and the full retained state is not replaced or discarded.

## Verification

    uv run research/strominger/checkers/check_shared_leg_controllability.py

29 exact checks pass. The43-check observer,65-check source-algebra/native T9 chain and their numerical dependencies rerun. Existing formal proof receipts/source hashes are validated where the pinned suite requires them; no new compiler closure or physical-source admission is claimed.

Artifacts:

- `research/strominger/checkers/shared_leg_control_ports.py`
- `research/strominger/checkers/check_shared_leg_controllability.py`
- `research/strominger/results/shared-leg-controllability.json`

The result includes all120 candidate primitive coefficient-port labels, exact Jacobian/orbit ranks and the half-energy gain witness.

Graph report/request: `ev-000000015913-cae2209f-81c4-4926-b9fc-3cd8738e9d9d` (proposal `ep_43af1691-f2a6-4414-8d63-e794003d4311`). A directed request asks the source owner for concrete admitted intervention evidence; no input authority is assumed. Admission records scoped provenance, not truth certification. No Git commit or push was authorized or performed.
