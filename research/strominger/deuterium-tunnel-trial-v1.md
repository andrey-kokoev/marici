# Deuterium: a small window-fiber and tunnel trial

**UI update:** the viewer now has only **Previous item / Next item** for assembly
display. The transport operations below remain model tests, not viewer controls.
Only the native single-packet phase templates are currently admitted by the
necessary checks; see [the phase audit](phase-discipline-audit-v1.md).

The local trial has one P, one N, one e. The default viewer now extends it as
**Deuterium · 2-cycle trial**, with an explicitly assumed boundary map; see
[the conditional cycle test](deuterium-two-cycle-trial-v1.md).
Deuterium is the smallest neutral composition exercising all three retained
windows. Hydrogen would require a separate P→E rule that is not supplied here.
This is a constructive composition model, not a derivation of nuclear binding.

## Growing the tunnel

The trial wraps `window-construction-model.mjs`, retaining its actual lattice
cells 0, 13, 16. It does not use the legacy deuterium placement selector.
N and E are distinct primitive carriers inside one ambient octahedral group;
that whole octahedron is not simultaneously assigned to N. Here “item” means
a committed particle carrier, not its ambient assembly parent.

- Initially only P is committed. Entry and the current exit coincide at its center.
- **Next element** adds N through the previous exit window M0,C1,M1.
- **Next element** adds E through M1,C1,C2, reversing the retained C1/M1 edge.
- Each addition preserves the previous prefix and makes the new item the current
  exit. Every prefix is a simple, uninterrupted chain with no repeated cell.
- E is terminal. There is no construction step after its MCC window.

The frontier is explicit in `snapshot().tunnel.frontier`. Before completion it
is an extendable exit, not an additional electron or a prescribed distant target.
The original `snapshot().exit` still describes the final realization-boundary
port and remains pending until E is committed.

For the default marking, the three bodies tile a closed oblique triangular
prism: the triangle M1,C2,M2 is a translate of C0,M0,C1, and the summed carrier
volumes equal the prism volume. There is no internal hole between P and E;
the neutron occupies the intervening tetrahedral part.

The three bodies have positive, disjoint lattice volumes. E is a nonregular
subdivision tetrahedron with dotted edges and translucent faces. The viewer
shows the carrier geometry and active reader without a tube visualization.
Particle volumes remain unchanged.

## Fiber and inverse transport

`deuterium-tunnel-model.mjs` retains a five-slot complex reference carrier on
C0,M0,C1,M1,C2, alongside global marks and history. The active ordered window
reads three slots; its two-slot complement is preserved, not projected away.
The reference C2 coefficient is retained even before C2 acquires its geometric
binding. M2 remains geometric context, not an invented sixth native coefficient.

The full frame exchanges swap C0/M1 for P→N and M0/C2 for N→E. Their active
window views induce the following maps:

```
P→N: (a,b,c) → (b,c,a)
N→E: (a,b,c) → (c,b,a)
```

Their algebraic inverses are implemented directly. Reverse transport does not
restore a saved coefficient snapshot. These permutations preserve the standard
coefficient norm—not an asserted physical spatial metric—and recover arbitrary
complex input vectors after forward/inverse transport, including nonzero
complement components. The carried five-slot vector and active mode are checked
against the retained fiber state at each item.

For the initial positive character, the local reference modes are:

```
P: positive, phase 0
N: positive, phase 1
E: negative, phase 0
```

**Toward entry** and **Toward exit** traverse the completed tunnel one interface
at a time. They move the reader, not the geometry. The same identity, all six
vertex bindings, construction events and the repeated-C1 occurrence history
remain intact in both directions. Navigation has a separate append-only log.
Returning to entry does not erase the completed atom or its construction history.

The no-revisit rule applies to construction. Passing back through an already
built item is precisely the reverse-read operation under test, not another
construction visit. Neither boundary permits movement beyond the modeled path.

## Coverage and evidence

The trial's declared domain has three particle carriers. Completion requires
3/3 state-compatible coverage and the specified 1P/1N/1e composition. During
construction the readout says 1/3 or 2/3 built; it does not call a one-cell prefix
a completed atom. Ambient coverage remains separately available in the viewer
API: this trial still covers only 3/343 primitives of the original whole space.

`check_deuterium_tunnel.mjs` tests 24 supplied seed markings × three modes:

- one-item commits, continuous frontier interfaces and no construction revisits;
- actual shared-face guide segments and existing-lattice membership;
- forward/inverse coefficient maps, including arbitrary five-slot complex
  payloads and nonzero complements in all 24×3 construction/traversal tests;
- all three phase offsets for each reference mode;
- repeated round trips without changing geometry, identity, bindings or history;
- blocked extension past E, blocked passage past either endpoint, and immutable
  returned coefficient snapshots.

The full browser closure additionally verifies geometry, visual passage in both
directions, phase readouts, electron styling, mesh reuse and mobile controls.
Evidence: `results/deuterium-tunnel/verification.json` and
`results/fiber-space/sequential-assembly.png`.

## What remains conjectural

This is a discrete local fiber with **declared reference-frame adapters**. It is
not a full native particle-state lift or a physical tunneling law. An inverse
on one path is a consistency check, not a test of branch holonomy.

No physical next-realization boundary map has been supplied or derived. The
[two-cycle extension](deuterium-two-cycle-trial-v1.md) tests an explicitly assumed
identity identification in canonical coordinates. Physical passage between
realization cycles remains conjectural. Branching on top of this tunnel is also
not implemented here. The full Pb-208 layout remains unbound.
