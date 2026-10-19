# Conditional two-cycle deuterium trial

**Current scope:** research algebra only. Cycle/transport controls have been
removed from the viewer; its two buttons assemble the native single packet.
The assumed inter-realization identification is not phase-admission evidence.
See [the phase audit](phase-discipline-audit-v1.md).

The viewer now offers **Next cycle** at R0's terminal electron and **Previous
cycle** at R1's entrance. These are separate from same-cycle traversal. One
geometry is viewed in two realization charts; no translated duplicate atom or
ordinary E→P spatial edge is inserted. The readout explicitly says “assumed glue.”

The declared hypothesis is preservation of the canonical five-slot reference
carrier between cycles. If T is the within-cycle frame transport, the boundary
map in local coordinates is **B = T⁻¹**; its reverse is T. This is an explicit
model assumption, not a recovered physical law. The model requires the option
`boundaryIdentification: 'canonical-identity-hypothesis'` before enabling a
second cycle. The single-cycle API remains the default without that option.

Crossing a boundary computes the map on the actual carried coefficients. It
does not restore a stored input vector or manufacture two spatial return steps.
Construction history, bindings, geometry and identity remain intact. Boundary
crossings and ordinary traversals have separate journals. The six states
R0:P/N/E and R1:P/N/E can be visited and the full carrier returned to its start,
including nonzero complement coefficients.

## Branching check and limitation

The two full-frame exchanges commute algebraically. Reordering them gives the
same five-slot vector, but the reordered reverse path would try N→P while still
at E. It fails the typed window-order check. It is **not** admitted as a second
particle branch merely because its linear algebra agrees.

Nor does reversibility determine B: inserting a sign change on the fifth
canonical coefficient gives a different, equally invertible boundary map.
The checker uses a nonzero fifth coefficient to expose this difference rather
than hiding it in an active-window projection. Consequently the identity-gluing
round trip validates an implementation of the assumption; it is not evidence
selecting that physical boundary map over alternatives.

`check_deuterium_cycles.mjs` tests both directions, all three modes, explicit
opt-in, wrong-port rejection, unchanged geometry/history, full five-slot return,
frame-order agreement, typed-branch rejection and the alternative gluing.
Browser tests exercise the cycle buttons and unchanged mesh identities.
Evidence: `results/deuterium-cycles/verification.json`.

Physical inter-realization tunneling and a physical branching network remain
unestablished. No such claim is inferred from the successful conditional test.
