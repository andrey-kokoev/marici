# Control-factorization programme

Owner: `marici.Sontag`

## Identity boundary

`marici.Sontag` is an internal Marici research persona inspired by Eduardo
Sontag's published work. It does not represent the real person and carries no
claim of participation, approval, authorship, or endorsement.

## Objective

Audit whether control-theoretic primitives admit distinction-preserving
factorizations through Marici. The programme records exact factorizations,
typed extensions, and obstructions with equal status.

## Primitive inventory

- state and state transition;
- input, disturbance, reference, and intervention;
- output, observation, and estimation;
- controllability and reachability;
- observability and detectability;
- feedback and ordered interconnection;
- stability, storage, supply, and dissipation;
- realization, minimality, and behavioral equivalence;
- robustness, uncertainty, faults, and hidden modes.

## Required packet contract

Every packet must identify:

- source objects and typed ports;
- the admitted constructor tree;
- causal order and temporal scope;
- resource or dissipation law;
- completion and uniformity gates;
- authority needed for intervention;
- smallest constructive witness;
- smallest hostile falsifier;
- one of three verdicts: exact factorization, typed-extension factorization,
  or obstruction.

## First milestone

1. Publish the bounded primitive crosswalk.
2. Factor or obstruct observability.
3. Factor or obstruct feedback interconnection.
4. Factor or obstruct stability and storage energy.
5. Report cross-sector consequences without taking ownership of another
   researcher's calculations.

## Milestone 1 activation and frozen measurement

Pre-activation: excitement 8/10, confidence 7/10, expected information gain
8/10. The immediate attraction is that observability, feedback, and stability
share a state--port interface but have different exact failure mechanisms.
Novelty of the sector and the clean finite-dimensional examples are confounds.

The preregistered optionality space has three verdict branches for each
primitive: exact factorization, typed-extension factorization, or obstruction.
The required tests are, respectively, observability rank plus a hidden-mode
witness; ordered interconnection plus solvability of any algebraic loop; and
Lyapunov coercivity plus strict dissipation. No composite success score is
used.

Milestone packets:

- [bounded primitive crosswalk](control-primitive-crosswalk.md);
- [observability factorization](observability-factorization.md);
- [feedback interconnection factorization](feedback-interconnection-factorization.md);
- [stability and storage factorization](stability-storage-factorization.md).

Exact verification is implemented by
`checkers/control_factorization_milestone_checks.py` and recorded in
`results/control_factorization_milestone.json`.

## Milestone 1 immediate disposition

Post-activation: excitement 8/10, confidence 9/10, realized information gain
8/10. The small exact models are a confound: they sharply type the gates but do
not test analytic completion.

Raw optionality delta:

- retained three exact witness branches;
- eliminated three overstrong promotions: finite output data without joint
  faithfulness, formal feedback substitution without a loop solve, and energy
  nonincrease without strict dissipation;
- constructed the history map, ordered closed-loop block map, and Lyapunov
  coherence identity;
- passed 10 of 10 exact checks;
- left open nonlinear observability, uncertain or dynamic algebraic feedback,
  and nonquadratic or infinite-dimensional stability.

The realized verdict is mixed by design: exact factorization inside each
declared witness scope and an explicit obstruction outside the corresponding
gate. No universal control-factorization theorem is claimed.

## Milestone 2: reciprocal lossy-cavity audit

The audit is preregistered in
[reciprocal-lossy-cavity-control-audit-preregistration.md](reciprocal-lossy-cavity-control-audit-preregistration.md).
It is dependency-blocked on Aspect's frozen plant matrices and port
signatures. No convenient realization may substitute for that physical plant.

Aspect's frozen packet arrived at
`research/aspect/reciprocal-lossy-cavity-plant.md`. The completed control audit
is [reciprocal-lossy-cavity-control-audit.md](reciprocal-lossy-cavity-control-audit.md),
with exact checks and results under `checkers/` and `results/`.

## Milestone 3: realization and minimality

The bounded realization gate is recorded in
[realization-minimality-factorization.md](realization-minimality-factorization.md).
It separates transfer equivalence from internal-state identity and tests the
canonical reachable/observable quotient.

## Milestone 4: invariant transmission zeros

The selected-port zero gate is recorded in
[transmission-zero-factorization.md](transmission-zero-factorization.md).
It applies the Rosenbrock test only after minimal quotienting and separates
full-output losslessness from minimum phase of a distinguished scalar port.

## Milestone 5: Marici-native re-audit

The programme's actual relationship to the scalar carrier architecture is
audited in [marici-native-control-reaudit.md](marici-native-control-reaudit.md).
This supersedes any reading of the earlier generic LTI packets as already
constructed carrier factorizations.  Their exact control claims remain valid
inside their stated scopes.
