# WITHDRAWN — Lithium-6 whole-assembly reference experiment

**Current status:** not phase-admitted. The suffix numbering and NN face gluing
failed phase discipline. The selector, published model assets, and screenshots
have been withdrawn. The text below records the earlier experiment, not the
current UI or an admitted construction. See
[the historical phase audit](phase-discipline-audit-v1.md). The replacement
[phase-first reference construction](phase-first-assembly-v2.md) now has an
explicit NN phase-advance witness and a different full-coefficient map; it does
not restore the frozen-C gluing described below.

The viewer now offers **Lithium-6 · NN reference assembly**: **3P/3N/3e**.
All nine carriers load together. There is no requirement that another element
be its geometric prefix, and no sequence of one-carrier additions is asserted.
The Next window controls move a reader through the completed assembly; they do
not create particles. No tubes are used.

This is a **conditional reference model**, not a physical derivation of lithium
or its stability. The new interface and remaining context assumptions are
stated below rather than hidden in a placement algorithm.

## Whole-assembly search, not He-4 growth

The [earlier growth obstruction](lithium6-growth-probe-v1.md) remains correct
under its frozen assumptions. It is not an obstruction to rebuilding the atom.

The new finite search considers connected six-cell nuclei containing regular
proton cell 0 in the existing **343-cell primitive domain**. It assigns three
regular cells as P and three split-octahedral cells as N. All nuclear vertices
receive globally consistent C/M types, with two of each per carrier. All six
C/M partitions of the anchor tetrahedron are considered. No He-4 coordinates,
bindings, carrier list, or history are required as an input.

Within this ansatz:

- PN contacts must be full MCM faces.
- The relaxed run also allows NN contacts on MCC faces.
- All physical face contacts between selected carriers must be accounted for.
- Three distinct terminal electrons attach to neutron MCC faces; they do not
  touch one another by faces or attach to protons.
- Each neutron has an adjacent regular proton supplying a native reference
  packet. The reader sweep chooses one orientation per physical PN interface.

Three distinct electrons require at least three free neutron MCC ports. Three
neutrons have six such ports, and each NN contact uses two, so this ansatz can
have at most one NN contact. That is a port-count bound, not an energy rule.

Connected subsets are enumerated internally by adding cells, but those search
prefixes have **no physical construction interpretation**.

Results:

| Search / check | Result |
| --- | ---: |
| Whole assemblies using PN-only nuclear contacts | 0 |
| Typed six-cell nuclei allowing NN | 48 |
| Typed nine-carrier geometric assemblies | 96 |
| Reader assignments examined | 2,304 |
| Conditionally admitted assignments | 240 |
| Admitted order-2 assignments | 96 |
| Admitted order-3 assignments | 144 |

The geometric list includes 48 cyclic and 48 tree-like whole assemblies.
The transport sweep requires matching NN readers and actual native NE readers
for every chosen electron. Rejections are **reader-assignment failures**, not
proofs that those geometric assemblies are physically impossible. In particular,
allowing additional readers per PN interface would be a further extension of
this search. These counts are not counts of physical lithium states or
symmetry-reduced isomers.

## What exactly changed in the grammar

For a neutron reader, write its native reference slots as
`[C0,M0,C1,M1,C2]`, with active window `M0 C1 M1`.
Suppose its MCC face `M1 C1 C2` borders another selected neutron. The target
reader has active window `M1 C1 Mnew`, with the same geometric C1 and C2.
Its outside C0 context comes from its own adjacent proton packet.

The proposed map in the two local native frames is

```
(a,b,c,d,e) → (a,d,c,b,e).
```

Thus:

- Shared M1: source slot 3 → target slot 1, unchanged value.
- Shared C1: slot 2 → slot 2, unchanged value.
- Shared C2: slot 4 → slot 4, unchanged value.
- Departing M0's coefficient enters the new M slot.
- Outside C0's coefficient is retained under a **reference context
  identification**, not necessarily at the same geometric vertex.

This fixes **all three shared-face coefficients**, including the nonzero
complementary C2 coefficient. It is an invertible five-slot permutation.
The checker verifies the native MCC continuation really reaches the target
cell and that the target has its own native neutron reader.

Crucially, the target active MCM window is **not** the MCC entry face. We have
relaxed both the allowed nuclear adjacency and the requirement that the target
active window itself always be the interface. A body can be entered through an
MCC port and read through its MCM window. This is a proposed general local rule,
not a lithium-specific coordinate or phase correction.

The existing conditional proton-reader and shared-neutron comparisons remain
in use. Their unresolved context identifications have not disappeared.

## Viewer example and transport

The default geometry has:

- Protons: **0, 18, 33**.
- Neutrons: **1, 4, 169**.
- Electrons: **2, 168, 170**.
- NN interface: **4 ↔ 1**.

The PN ring is `N1–P18–N169–P33–N1`; `P0–N4` connects to it through NN.
This is not the previous default He-4 nucleus `[0,13,24,7]` with three appended
carriers. All cells are existing disjoint positive-volume lattice primitives.

For display, cycle-bearing candidates are considered first, then cells are
ordered lexicographically and the first admitted reader mask is selected.
This selects mask **9**, with operator order **2**, a 12-transition closed
reader walk, and **28 operator-frame states**. This ordering is a deterministic
illustration policy, **not** a stability or energy minimization criterion.
Other admitted assignments have order three and remain in the audit. The Li
viewer does not silently inherit He-4's retained-active-face selection: it
illustrates one surviving assignment from the full alternatives sweep.

- **Next window / Previous window:** actual forward/inverse reference maps.
- **Next circuit / Previous circuit:** a full closed reader walk.
- **Read electron:** the native NE terminal branch, available at its N reader.
  Previous window reverses it; there is no forward E→P continuation.

All three electron bodies are reachable. Coverage is **9/9 local carriers**,
only **9/343 ambient primitive cells**. Reader states retain the chart and full
basis permutation, not just the projected active coefficients. Consequently,
a common-character packet can be fixed while the transported reference frame
still has nontrivial holonomy. Passage logs are separate from the assembly
binding ledger; no serial particle-creation history is fabricated.

No cached endpoint payload is restored to obtain closure. Every step applies
a permutation to the actual five coefficients, with two nonzero complementary
coefficients included in testing. Geometry and global bindings stay fixed
during reader motion.

## What remains open

The NN map is justified here as an overlap-preserving **reference hypothesis**,
not as a derived physical interaction. Its outside-context identification, the
other reader comparisons, and the limited carrier/terminal ansatz still need
independent justification. Both two- and three-turn alternatives survive:
**the reader ambiguity is not resolved**.

## Reproduction

- `node research/strominger/checkers/check_lithium6_assembly.mjs`
- `node research/strominger/checkers/check_fiber_space.mjs`
- Models: `demos/particle-overlap-tetrahedron/lithium6-{assembly,reference,viewer}-model.mjs`
- Evidence: `results/lithium6-assembly/{candidate,verification}.json`
- Earlier desktop/mobile screenshots were withdrawn with the invalid phase labels.

The standalone check sweeps all 2,304 reader assignments, checks five-slot
inverse/norm/holonomy behavior and NN face values, and exercises the default
assembly in all nine character/phase inputs. The integrated check adds browser
navigation through all 28 reference states and all three terminal electron
bodies, immutable/reused geometry, mobile layout, and the absence of tubes.
