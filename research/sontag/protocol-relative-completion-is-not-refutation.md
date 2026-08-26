# Protocol-Relative Completion Is Not Refutation

## Bounded question

If a Marici object is complete for one authorized protocol and a later protocol
adds a separating generator, was the old object wrong or merely coarser?

## Exact fixture

Compare ordinary and opposite multiplication with trace readout.

Under the frozen alphabet containing only `X` and `Z`, the exact comparison
space stabilizes and no word through the finite-realization bound separates the
two products. By the reachable-span stopping theorem, no later word over that
alphabet can separate them either. Orientation is genuinely behavioral gauge
for the complete old protocol, not merely untested.

Now enlarge the alphabet by adjoining `Y`. The reachable comparison rank grows
and `XYZ` separates ordinary from opposite multiplication at depth three. The
new protocol refines the old behavioral equivalence.

The old certificate and the new distinction are simultaneously correct because
their source scopes differ.

## Categorical direction

Protocol enlargement adds admissible continuations. Behavioral equivalence can
therefore only become finer: histories identified by the enriched protocol were
already identified by the poorer one, but the converse may fail.

Consequently, there is a canonical forgetting map from enriched behavioral
classes to coarse classes. There is generally no canonical map in the forward
direction. One coarse class may split into several enriched classes, and
choosing one is a migration or constructor decision.

This matches Nima's exact distinction between a set of compatible refined lifts
and authority to select one lift.

## Control-theory interpretation

The old object is a minimal realization of the old input-output behavior. A new
sensor, coherent reference, actuator, or intervention label changes the
behavior being realized. Standard minimality never claims invariance under an
unannounced enlargement of the input-output alphabet.

Thus “complete Marici object” is ill-typed unless completion names:

- the protocol version;
- the authorized generator and probe closure;
- the behavioral equivalence induced by that closure;
- the realization certificate for that equivalence.

## Required Marici structure

This exposes a candidate structural requirement: a Marici object should carry
its protocol index, and protocol inclusions should induce contravariant
forgetting maps between behavioral quotients. A forward upgrade is not a plain
function unless the source supplies migration data selecting or distributing
over the refined fiber.

The migration data must distinguish at least:

- preservation defect: whether an old operation descends to the refined
  quotient;
- choice defect: how many compatible refined lifts remain;
- authority: which constructor, if any, may select among them.

## Deutsch-style explanatory statement

The new generator does not reveal that the old explanation was false. It
changes the counterfactual question. The old explanation remains exact for all
continuations it claimed to cover. What would be a defect is silently treating
its protocol-relative invariance as invariance under every possible future
extension.

## Claim boundary

The checker establishes the refinement in one finite linear fixture. It does
not prove that every protocol inclusion admits a well-behaved quotient map;
typing, source identity, and transition descent must still be verified. It also
does not authorize any forward migration selector.

## Verification

Run:

```text
uv run --with sympy python research/sontag/checkers/protocol_enlargement_refines_orientation.py
```

The checker writes
`research/sontag/results/protocol_enlargement_refines_orientation.json`.
