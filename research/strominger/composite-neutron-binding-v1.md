# Whole-octahedron neutron: native skeleton binding probe

**Prior-research follow-up:** [recovered clues](prior-assembly-clues-v1.md)
identify an already implemented reference-only-P convention and supplied
subdivision choice that should be tested before enlarging particle volumes.
The local binding below does not supersede those earlier constructions.

## Result: a partial binding exists, but no whole-body admission law yet

A whole octahedron can contain a native four-vertex neutron reader whose
**incoming PN and outgoing NE faces are both external octahedron faces**.
This gives a useful marked-window-preserving alternative to the legacy Pb
outward chains. It does not yet make the whole volume one native neutron.

The [protocol](composite-neutron-binding-protocol-v1.md) was recorded before
execution. Production admission and the viewer were not changed.

## Exhaustive local marking test

Test one upright and one inverted regular proton seed, with all 24 ordered
C0/M0/C1/M1 bindings on each. Replay the unchanged native window constructor
and identify the whole octahedron containing the constructed neutron cell.

For **each orientation**:

| Outcome | Markings |
|---|---:|
| Native NE face lies on whole-octahedron boundary; E is an external regular tetrahedron | **8** |
| Native NE face is internal; E is another constituent cell of that octahedron | **16** |

The external cases preserve the actual C1/M1 edge between PN and NE windows.
The native N tetrahedron is one of the four existing octahedral components;
the extra three components are a proposed volume decoration, not extra counted
particles in an admitted model. P, whole-octahedron volume and E have distinct
constituent cells and use six honeycomb primitive cells altogether.

All existing native five-slot PN/NE maps and their inverses are retained:
`[3,1,2,0,4]` then `[0,4,2,3,1]`. Same-occurrence phase audits pass on both
native interfaces. All three branch modes and three phase exponents replay
with the native NE reversal and unchanged final phase exponent. The partial
binding introduces no new spectral coefficient.

## Two important obstacles for transfer

### 1. The existing root marking selects the internal case

For the upright root, none of the four ordered bindings preserving its fixed
C/M role assignment produces an external E face. The analogous role-pattern
control on the inverted seed has the same result. The exact canonical root
binding is included in those four controls.

Thus one cannot simply enlarge the first neutron in the default P->N->E packet
and keep its electron as a separate body: that electron would lie *inside* the
new neutron volume. The external examples use different seed markings. The
probe does not authorize changing the production root or prove that a larger
multi-reader nuclear assembly could never connect that root to a different
external reader.

### 2. The marked exit is lateral, not farther out than the whole N centroid

Every external case fails the legacy Pb ordering `P < whole-N < E` along the
incoming face's outward axis. For a representative upright seed, the relevant
coordinate is:

- P center: `+0.25`
- whole-octahedron center: `-0.50`
- E center: `-0.25`

Outward is decreasing on this axis. The E endpoint is exterior across the
correct adjacent boundary face, but its center is not farther out than N's.
The inverted example has the reversed coordinate direction and same behavior.

This identifies a **heuristic worth dropping in a future diagnostic search**:
strictly monotone centroid chains are not required for nonoverlap or native
window transfer. Enumerate boundary ports that preserve the marked edge, then
solve global resources; do not choose faces by radial ordering alone. This is
not a permission to change native phase or physical contact rules.

## What still prevents a whole-body binding claim

The whole octahedron has six geometric vertices. The native N reader binds four;
the other two are not any of the existing packet's named C0/M0/C1/M1/C2/M2
vertices. They remain explicit, unmarked geometric context.

The retained source does not specify whether these extra vertices are passive
support, additional field data, another realization, or a different particle
representation. We have not introduced extra independent coefficients. If one
hypothetically appends auxiliary data, different norm-preserving actions agree
on all five native coordinates but disagree on the auxiliary sector. This
shows the existing action does not uniquely determine that extension; it does
not prove new coefficients are physically required.

A complete representation still needs:

1. A reason this decorated six-vertex volume counts as **one** neutron.
2. Compatible comparisons between native readers on different constituent
   tetrahedra, including their contexts and absolute occurrence histories.
3. A field/boundary interpretation for all other exposed faces and incidental
   contacts—not just the selected PN/NE pair.
4. A boundary/continuation criterion that does not smuggle in a chosen neutral
   electron quota as nuclear admissibility.

No isotope search was performed under an invented whole-body law. It would be
misleading to feed octahedral bodies to the unchanged primitive-cell compiler
or count their four constituents as one neutron only when convenient.

## Consequence for N-14

There is a concrete **local candidate architecture** now: whole-octahedron
support, a retained four-vertex native reader, and a lateral regular E endpoint.
It improves on Pb's 0/82 marked-edge score at the local level. It does **not**
yet establish a 7P/7N/7e packing or solve neutral N-14.

The next meaningful object is the whole-body reader/context comparison law,
not an isotope-specific geometry exception. If treating the extra volume as
passive support is proposed, that must be an explicit new representation
hypothesis with all-contact tests, rather than a claimed derivation from the
existing four-vertex source.

## Verification

```sh
node research/strominger/checkers/check_composite_neutron_binding.mjs
```

Evidence: `results/composite-neutron-binding/verification.json`, including source
and protocol hashes, all root-type countercontrols, representative actual
coordinates for both orientations, native packet histories/maps and centroid
ordering tests. Local geometry is translation invariant; other translated
seeds were not redundantly enumerated. No multi-neutron global packing claim.
