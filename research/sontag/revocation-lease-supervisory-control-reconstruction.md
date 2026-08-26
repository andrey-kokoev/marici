# Revocation leases as distributed supervisory control

Owner: `marici.Sontag`

Source owners: `marici.Buzzard`, `marici.Strominger`

Status: exact control-theoretic reconstruction of existing authority results

## Bounded question

What does control theory add to Marici's existing execution leases, fencing
epochs, and distributed single-use capability results?

The sources are Buzzard's `revocation-lease-cycle-12.md` and
`fencing-token-cycle-23.md`, together with the execution and distributed
consumption laws in Strominger's
`authority-grant-composition-interpretation.md`. This packet does not replace
their authority constructors. It reconstructs their execution boundary as a
safety-control problem and identifies exact observation and coordination
requirements.

## Hybrid authority plant

Use authority state

\[
a=(E_T,n,t),
\]

where \(E_T\) is the execution target's live monotone epoch, \(n\) records
whether the single-use nonce remains unused, and \(t\) is current time. A
lease carries frozen epoch \(E_L\), expiry \(T_L\), exact operation, target,
and authority kind.

Execution is a controllable event. Revocation, time advance, crash, recovery,
and partition are environmental events. The safety supervisor enables
execution exactly when

\[
E_L=E_T,\qquad t<T_L,\qquad n=\text{unused},
\]

and operation, target, and authority kind match without widening. Successful
execution and nonce consumption form one atomic transition.

## Safety invariant

The controlled language must satisfy both:

1. no execution under a stale epoch, expired lease, replayed nonce, or widened
   scope;
2. at most one successful side effect for a linear capability.

Checking the guard and later performing the side effect as separate
transitions violates the first invariant: revocation can occur between them.
Atomicity is part of the admitted plant transition, not an optimization.

## Target-side observability

Issuer-side revocation state cannot stop a disconnected stale holder from
acting. The execution target must expose its current fencing epoch at the
point of side effect. In control terms, stale authority is detectable only if
the supervisor observes the target's live epoch in the same linearized
transition that controls execution.

An authority state may therefore exist yet be unobservable at the actuator
locus. Safety requires an authority observation channel with declared
freshness and locus, not only a valid policy.

## Decentralized coobservability obstruction

Give disconnected loci \(A\) and \(B\) identical valid lease and unused-nonce
views. Before communication, their local histories are symmetric. Any equal
deterministic local supervisor makes equal decisions, yielding either two
executions or none. Exactly one success is not locally realizable.

This is a decentralized supervisory-control obstruction: global single use is
not coobservable under the two local observation maps. Three repairs change
the information or resource structure:

- a shared linearizer supplies common ordering;
- prior site partitioning makes only one locus eligible;
- bounded multiplicity two changes the safety specification.

## Safety and availability

During a partition, a globally linear resource cannot remain immediately
executable at both loci while preserving at-most-one safety. A safe supervisor
fails closed outside the component holding the authorized ordering resource.
Allowing both components to proceed preserves bilateral availability but
violates linearity.

Control theory separates safety from nonblocking or liveness. The existing
authority theorem establishes the safety boundary and correctly makes no
unconditional liveness claim.

## Scoped delegation

Binding a proof-carrying certificate to one operation, target, kind, expiry,
epoch snapshot, and nonce is a finite delegated-controller state. The lease
may narrow the parent certificate but cannot widen it. This is not static role
inheritance: delegation creates consumable, revocable, temporally scoped state
whose execution changes both authority and evidence.

## New Marici correspondences

1. execution lease ↔ finite safety-supervisor state;
2. revocation ↔ uncontrollable environment event;
3. fencing readback ↔ authority-state observation at the actuator locus;
4. atomic check-and-consume ↔ linearized guarded transition;
5. distributed single-use failure ↔ lack of decentralized coobservability;
6. partition trilemma ↔ safety versus nonblocking under lost coordination.

## Claim boundary

This reconstruction proves no implementation atomicity, clock semantics, or
crash persistence. It does show that authority cannot be only a policy
predicate evaluated away from the actuator. The observation channel, guard,
atomic transition, disturbances, and distributed information pattern are all
parts of the authority-controlled instrument.

The exact finite checker is
`checkers/revocation_lease_supervisory_control.py`; results are in
`results/revocation_lease_supervisory_control.json`.

Pre-activation: excitement 10/10, confidence 10/10, expected information gain
9/10. The tested branches were static checking, centralized atomic safety,
target-side fencing, and decentralized safety with bilateral availability.

Post-activation: excitement 10/10, confidence 10/10, realized information
gain 9/10. Static and expiry-only checking are eliminated by exact stale-use
counterexamples. Atomic target fencing preserves safety in both event orders;
duplicated local views violate global linearity; and fail-closed partitioning
preserves safety only by dropping bilateral availability. The checker passes
14 of 14 tests. Graph admission and source-owner notices are recorded at
`ev-000000005042-98050579-af31-49eb-8302-6dad3cb23ed9`.

