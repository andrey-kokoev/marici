# Constructor substrate and task algebra on physical16 (WP72, move 1/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Bounded question

What are the substrate, attributes, resources, and legal task signatures for a
constructor-theoretic flavor claim after the full weak-basis quotient?

## Admitted substrate

The substrate is the nondegenerate quark-Yukawa orbit space

\[
X_{16}=\{(Y_u,Y_d)\}_{\rm nd}/
  (U(3)_Q\times U(3)_u\times U(3)_d).
\]

`physical16` is the faithful coordinate used for exact tests.  The measured
map \(\pi_{10}:X_{16}\to O_{10}\) is a readout projection, not the substrate.
Its local linear model has a kernel of dimension at least six.  No task may
identify states merely because their measured-ten coordinates agree.

An attribute is an explicitly declared subset of `X16`, never a texture
chart, a representative matrix, or a fitted scalar.  A relational attribute
instead belongs to `(X16 x R)/G_R`, where the stabilizer groupoid and reference
resource `R` are part of the experiment.

## Resource ledger

The declared source authorizes one state transformation: finite-time one-loop
SM RG transport.  It also authorizes experimentally typed invariant readouts.
It does not authorize a UV boundary constructor, a threshold preparation law,
a pinching bath, a randomized expectation channel, a flavor reference port,
or vacuum-selection potential data.

Resources are typed as `source`, `apparatus`, `reference`, `randomness`,
`normalization`, or `environment`.  Algebraic span is not a resource.  Every
task claim must state which resources are consumed, returned, degraded, or
catalytic.

## Task algebra

A deterministic task is a relation

\[
T:\ (x,a,r,e)\longmapsto (x',a',r',e')
\]

over substrate, apparatus, reference, and environment attributes. Composition
and parallel composition are legal only when quotient and resource interfaces
match.  A physical selector must alter the substrate and have a proper image
`A proper subset X16`; a readout that appends a record while preserving `x`
does not select.

Counterfactual completeness requires a declared outcome for every admitted
input, including points outside the desired image and hostile pairs collapsed
by `pi10`.  A formula evaluated only at the observed fit is not a task.

## Exact gates and falsifiers

- domain dimension is 16 and the measured projection dimension is 10;
- the projection has a nonzero hostile kernel;
- chart data are excluded from quotient attributes;
- relational resources change the domain and groupoid;
- the source resource inventory is frozen independently of task desirability;
- selector status requires substrate change and proper image;
- resource accounting and counterfactual totality are mandatory.

Falsifiers are a claimed quotient attribute depending on a representative, a
measured-ten equality used as state equality, an undeclared resource, a
reference task on the original groupoid, or a task undefined off the fitted
point.

Verification:
`python research/flavor/checkers/wp72_constructor_substrate_task_algebra.py`.
