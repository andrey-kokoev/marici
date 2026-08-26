# Marici as a contextual capability coalgebra

## Reconstruction question

Are source, authority, resource, and continuation fields primitive pieces of a
Marici packet, or can they be reconstructed from a more invariant process
object?

## Strong rival to the packet ontology

Treat a context as a source task, actor authority, resource state, protocol
epoch, and residual continuation resource. Above each context sits the minimal
state that predicts the controls, records, and successors available there.
Lawful context changes induce maps between these fibers.

The candidate Marici object is then the whole context-indexed capability law,
not one fiber plus copied metadata. Packet fields are coordinates used to
present that law.

## Exact latent-axis witness

Use two authority states, observer and controller, and two repair-resource
states, empty and available. Immediate set actions are enabled only for the
controller with available resource.

Three contexts therefore have identical current capability: observer-empty,
observer-available, and controller-empty all expose only no-op. No inspection
of that immediate capability can reconstruct whether authority or resource is
missing.

Two lawful context commands reveal the distinction:

- grant changes observer to controller;
- replenish changes empty resource to available resource.

Granting observer-available exposes set actions; replenishing
controller-empty does the same. The one-step continuation signatures separate
all four contexts exactly.

The immediate capability quotient is not a congruence for these context
commands. The correct typed transition maps the one-step contextual quotient
to the immediate quotient. This repeats the earlier finite-horizon result at a
deeper level: not only state but also object schema is relative to the future
variation language.

## Explanatory consequence

Authority and resource are genuine distinctions here because the admitted
process contains independent operations that address them and later change
constructive capability. They need not be stored as universal fields. They can
be reconstructed from the contextual behavior law.

Conversely, if no admitted continuation can distinguish two proposed fields,
future-capability minimization identifies them. Keeping both would be
presentation maximalism, not explanation.

This yields a stronger answer to why a Marici object has its structure:

> Its structure is the minimal factorization required to make lawful changes
> of source, authority, resource, and continuation context act compositionally
> on constructive capability.

The packet structure is forced only where those axes are independently
variable. It is derived rather than universally primitive.

## Revised object candidate

A Marici object is a context-indexed, source-relative capability coalgebra,
minimized under equality of all admitted future construction traces. A closed
packet is one transportable section or presentation of that object.

The controlled-invariant constructor principle supplies the semantic content:
which task remains constructively available. The contextual coalgebra supplies
the compositional form: how that capability varies as source, authority,
resources, and continuation budgets change.

## Claim boundary

The finite witness reconstructs authority and resource axes from named context
updates. It does not yet reconstruct the source task itself. If the task
success relation is omitted from all effects and continuations, no behavior
can recover why one state counts as correct. Either the source task remains
base structure, or a deeper constructor calculus must generate it.

This is the next unresolved explanatory boundary.

## Verification

```text
python research/sontag/checkers/contextual_capability_coalgebra.py
```
