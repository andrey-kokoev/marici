# Theory-neutral port infrastructure

`abstract_port_net.py` is a new separate core, not an alias of the scalar implementation. It imports only Python dataclasses. There are no scalar expressions, metric signatures, particle labels, normalization conventions or physics imports.

## Core responsibilities

* Per-net explicit signatures: one named principal port and declared auxiliary ports.
* Linear involutive wiring: each completed graph port has exactly one peer.
* Fresh monotone node allocation.
* Structural principal-pair discovery, without deciding which pairs have permitted rewrite rules.
* Atomic local replacement preserving every external boundary endpoint.
* Opaque payload HANDLE ownership: each consumed handle transfers exactly once to replacement agents. Payload objects stay in a client-owned store and are never copied, inspected or evaluated by the core.

Replacement stages new structural dictionaries and commits only after validation. Rejected replacements leave nodes, wiring and allocator unchanged. This is single-threaded transactional mutation, not thread safety. The initial replacement contract refuses additional wires internal to the consumed pair beyond the principal edge.

## Deliberately outside the core

Agent meanings, permitted rules, addition/multiplication, payload creation or disposal, observation policies, publication/completion protocols, typing of physical quantities, and theory conventions belong to clients. An OUT--VALUE principal pair is structural incidence, not automatically an enabled rewrite. A client must supply a rule table. Payload-computing rules will need an explicit ownership/effect interface rather than bypassing handle conservation.

## Evidence and migration status

A theory-free client example defines its own publication and completion rules. A payload object designed to reject copying and arithmetic remains untouched. Six refusal controls cover handle loss/duplication/invention, omitted boundary slots, late invalid wiring and incomplete replacement ports; every refusal preserves the old state.

Checker: `research/nima/checkers/check_abstract_port_net.py`.
Result: `research/nima/results/abstract-port-net.json`.

The existing scalar and biadjoint implementations have NOT yet been migrated. They remain legacy attributed prototypes. Next extract a reusable protocol/rule-dispatch layer over this core, then move theory adapters onto that layer without importing physics into the core. No claim of general normalization or observational equivalence follows from structural validation alone.
