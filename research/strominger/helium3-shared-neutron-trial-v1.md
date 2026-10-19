# Helium-3: shared-neutron reference algebra (phase admission withheld)

**Historical model, not the current viewer:** its mixed-index second-reader
windows fail necessary phase checks; permutation and inverse tests were not
phase-admission evidence. The corrected viewer uses
[phase-first assemblies v2](phase-first-assembly-v2.md), including context-to-active
transfer and explicit successive realization occurrences. The older transport
controls remain removed.

Helium-3 is the next stable isotope by mass after deuterium: two protons, one
neutron and two electrons. This trial is distinct from the legacy helium-4
occupancy preset. Its geometry is window-driven, not radially selected.

## Four-port completion hypothesis

Start with the accepted P → N → E packet. Its marked neutron has two MCM
faces and two MCC faces. The trial completes the unused MCM input and MCC output
ports, constructing a second proton and electron while retaining **one** neutron.

The second proton is the unique lattice neighbor across the remaining MCM face.
Both possible M orders are tested: one returns to the already occupied electron
carrier; the other uses the remaining output port. No distance or coordinate
ordering chooses the branch.

The two global-mark paths are:

```
R0: C0 M0 C1 [M1] → M0 C1 M1 [C2] → M1 C1 C2 [M2]
R1: C3 M1 C2 [M0] → M1 C2 M0 [C1] → M0 C2 C1 [M3]
```

The two N windows have the same four physical vertices. C3 and M3 are fresh
geometric identities; existing global marks never move or get renamed. The
second packet's local labels are explicitly aliased to these global marks.
The five physical carriers occupy base cells **0, 13, 16, 24, 14**.

Each construction click adds exactly one new physical carrier. Reading the
existing neutron in the second realization is recorded separately, not counted
as another construction. There are five carriers but six realization-window
states. Both electrons remain terminal within their own packets.

## Reference-state comparison

The shared-N comparison fixes the common global M0/M1 identities and exchanges
C1/C2. Matching the outside context slot of the two neutron charts is an
**additional reference identification**, not a derived physical law. All five
complex coefficients are carried; geometric M2/M3 acquire no invented native
coefficient.

In each packet's local reference order `C0,M0,C1,M1,C2`, the neutron comparison
S exchanges slots M0/M1. Let P be the P→N exchange and E the N→E exchange. Then:

- shared-N comparison: S;
- first electron to second proton boundary map: `P⁻¹ S E⁻¹`;
- canonical seed comparison: `P⁻¹ S P`, exchanging C0/M0.

For the default character this gives:

```
R0: positive ω⁰ → positive ω¹ → negative ω⁰
R1: negative ω¹ → negative ω⁰ → positive ω¹
```

These signs name reference characters, not particle charges or derived spins.
The old canonical-identity gluing does not fit this shared-N comparison in the
non-common sectors. Direct N-chart passage and the detour through the cycle
boundary agree on all five coefficients. A fifth-slot phase perturbation can
leave the active neutron triple unchanged while failing the full comparison.

## Viewer and scope

Choose **Helium-3 · shared-neutron trial** in
`/experiments/particle-overlap-tetrahedron/vacuum.html`, then add four elements.
At the shared neutron, previous/next-cycle controls change its reader chart.
At the appropriate packet endpoints they apply the boundary map. Geometry and
construction history are unchanged during passage.

The viewer shows the carrier geometry and active reader without a tube
visualization. Particle volumes remain unchanged.

The spatial carrier graph is a four-leaf star. It does **not** admit a single
five-cell Hamiltonian spatial path. The neutron is constructed once but read
in both realization frames. Coverage is 5/5 trial carriers, only 5/343 ambient
base primitives. Four-port completion and context gluing remain hypotheses;
matching the known isotope census does not derive physical stability.

Sources: `demos/particle-overlap-tetrahedron/helium3-tunnel-model.mjs` and
`checkers/check_helium3_tunnel.mjs`. Evidence:
`results/helium3-tunnel/verification.json`
and the integrated geometry/browser checks in `checkers/check_fiber_space.mjs`.
