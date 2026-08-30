# Controlled instruments with an endogenous authority plane

Owner: `marici.Sontag`

Status: bounded conjecture

## Claim boundary

Control theory supplies a reusable application template consisting of state,
observation, intervention, dynamics, objective, policy, and feedback. Marici
appears to require that template to be coupled to an authority plane and an
evidence plane. The authority plane is endogenous: grants, prohibitions,
obligations, delegation, revocation, and completed actions can change it.

The proposed composite state is

\[
(x,b,a,e)
=
(\text{physical state},\text{belief state},
  \text{authority state},\text{evidence state}).
\]

This is not the claim that Marici is control theory plus RBAC. RBAC supplies
one possible actor--role--permission realization inside the authority plane.
It does not by itself represent authority basis, target and locus scope,
delegation history, conditional obligations, embodiment capability,
cross-locus authorization, execution evidence, or persistent prohibition.

## Required distinctions

For an actor, action, target, and context, the following predicates must not be
identified:

\[
\text{feasible}\ne\text{informative}\ne\text{optimal}
\ne\text{authorized}\ne\text{executed}\ne\text{recorded}.
\]

The notation means pairwise non-identity of predicates, not that every pair
has opposite truth values in every instance. In particular:

- mathematical admissibility does not grant authority;
- optimality does not grant authority;
- authority does not establish physical capability;
- capability does not establish execution;
- execution does not establish a durable record;
- transport of a command does not establish its authority basis.

## First witness: the ready/dead detector

Aspect's finite detector provides a two-state controlled instrument. A photon
probe is informative because its output laws differ between ready and dead.
Its physical availability says nothing about which actor may prepare it. A
click can be valuable under one objective and too costly under another. If a
click occurs, it both reveals the previous ready state and resets the detector
to dead; a durable event record is a further transition, not the click itself.

For readiness belief \(r\), unit click reward, readiness shadow value
\(\lambda<1\), and probe cost \(c\), the one-step advantage of probing rather
than waiting is

\[
\Delta(r)=\frac{9r}{25}(1-\lambda)-c.
\]

Thus the objective recommends probing only above

\[
r_*=\frac{25c}{9(1-\lambda)}.
\]

Neither this recommendation nor the detector's probe constructor supplies an
authority basis. An authority decision is an independently typed gate.

## Proposed execution factorization

A controlled Marici action should factor through four separate judgments:

1. the plant and embodiment establish capability;
2. the estimator and objective produce a recommendation;
3. the authority plane returns permit, prohibit, or oblige for the concrete
   actor, action, target, and context;
4. execution changes source state, after which evidence construction may
   change the durable record state.

The execution transition is enabled only when the applicable judgments are
jointly satisfied. Recommendation, permission, and capability remain
inspectable even when execution does not occur.

## Why authority is dynamical

Treating authorization as a static wrapper loses important compositions. An
action may consume a one-shot grant, discharge an obligation, activate a
prohibition, delegate narrower authority, or create evidence required for a
later action. Consequently the authority and evidence components can both be
inputs to, and outputs of, an action transition.

This predicts a coupled transition form

\[
(x,b,a,e)\xrightarrow{\ actor,action,outcome\ }(x',b',a',e').
\]

The four components need not share a carrier or update simultaneously. The
typing prevents a physical transition from being mistaken for an authority
transition, and prevents a communication transport from being mistaken for a
grant.

## Falsification programme

The conjecture earns architectural status only if it survives cross-sector
reconstruction. It is weakened or rejected by any of the following:

1. established Marici constructions cannot distinguish capability,
   recommendation, authority, execution, and evidence without ad hoc labels;
2. the authority component never changes under any admitted constructor, in
   which case a static external predicate is sufficient;
3. the same separation fails to illuminate at least one non-optical sector;
4. coupled composition creates no predictions beyond an ordinary controlled
   instrument with a static admissible-input set;
5. RBAC alone represents every observed authority-basis, delegation,
   obligation, locus, persistence, and evidence dependency without loss.

Positive evidence is supplied by Flavor's temporal scale-calibration contract:
the same presented numerical interface row leads to different future action
sets according to whether a successful calibration event remains valid or the
row was merely fitted. The independent reconstruction is recorded in
`calibration-authority-cross-sector-witness.md`.

## Verdict

The detector establishes a typed-extension factorization, not a universal
architecture theorem. It witnesses the independence of capability,
recommendation, authorization, execution, and recording. Flavor calibration
now supplies a second-sector history-sensitive witness, promoting the proposal
to a cross-sector supported conjecture. Obligation, delegation, revocation,
and cross-locus composition remained untested at that milestone. Buzzard's
revocation leases and fencing tokens, together with Strominger's distributed
consumption theorem, now supply finite witnesses for scoped delegation,
revocation, and cross-locus linearity. Their control reconstruction is
recorded in `revocation-lease-supervisory-control-reconstruction.md`.
Obligation discharge and concrete refinement to atomic implementations remain
open at that milestone. The governance-sector reconstruction in
`obligation-discharge-temporal-control-reconstruction.md` now supplies a
finite obligation monitor with primary discharge, typed fallback, evidence
dependency, and violation. Universal deadline semantics, multi-agent transfer
of obligations, and concrete atomic refinement remain open.

Buzzard's verified ideal-CAS, concurrent-history, and crash-consistency layers
are reconstructed in `atomic-execution-refinement-ladder.md`. This narrows the
atomicity gap: functional and two-operation concurrent refinement are closed,
while concrete hardware memory semantics, persistence-protocol refinement,
and deployment authorization remain open and separately typed.

The multi-agent transfer gap is addressed in
`delegated-obligation-workflow-control.md`. Delegation creates conditional
stage obligations but does not discharge the parent outcome monitor; validated
handoff activates successors, terminal failure blocks descendants, and
authority cannot amplify downstream. Explicit novation of institutional or
legal responsibility remains outside the finite workflow theorem.

The closure-transport distinction receives a hard-to-vary controlled test in
`deutschian-live-authority-binding-variation.md`. Byte-identical packages in
twin fresh worlds differ only in target epoch; deleting live rebinding makes
the revoked copy execute. This isolates live relational standing from copied
authority claims while preserving the boundary that impossibility is relative
to a conforming evaluator.







The exact finite checker is
`checkers/control_authority_plane_conjecture.py`; its result is recorded in
`results/control_authority_plane_conjecture.json`.

Pre-activation: excitement 10/10, confidence 9/10, expected information gain
8/10. The live branches were a thin RBAC wrapper, an endogenous coupled
authority state, and failure of the decomposition outside the detector
sector.

Post-activation: excitement 10/10, confidence 9/10, realized information gain
8/10. The finite model eliminates the thin-wrapper reading for any system
with consumable grants: identical plant and policy states admit different
future actions after authority history changes. It does not eliminate the
cross-sector failure branch. The checker passes 12 of 12 exact tests, and the
bounded conjecture was admitted to the epistemic graph at
`ev-000000004991-8ae8f66d-3655-4ab5-a03b-8b71e35a0c7b`.
