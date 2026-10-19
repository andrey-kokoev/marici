# Phase-first He-3, He-4 and Li-6 reference assemblies

This replaces the withdrawn mixed-index reader constructions in the viewer.
It corrects phase bookkeeping and full-field reference transport; it does not
derive physical binding, stability, or a unique atomic interaction law.

## Advance the entire local frame

Keep the native templates, translated by an integer origin r:

```
P_r: C_r M_r C_(r+1) [M_(r+1)]
N_r: M_r C_(r+1) M_(r+1) [C_(r+2)]
E_r: M_(r+1) C_(r+1) C_(r+2) [M_(r+2)]
```

A neutron next-realization comparison is

```
M0 C1 M1 [C2]  ->  M1 C2 M2 [C3].
```

M1 and C2 are retained occurrences. The explicit successor chains are
`M0 -> M1 -> M2` and `C1 -> C2 -> C3`. C3 can occupy the old C1 position,
but is not the old C1 occurrence. The new M2 can be at the old M0 position
when re-reading one neutron, or at the next tetrahedron's entering vertex
when crossing an NN face. Both cases must satisfy the same local phase rule.
The NN case additionally crosses the actual native MCC continuation face.

For a proton re-reading, both C and M pairs advance, retaining the actual
C1/M1 occurrences and explicitly witnessing `C0 -> C1 -> C2` and
`M0 -> M1 -> M2`. Reversing just the C pair while freezing M is rejected.

The earlier offset contradiction was a valid rejection of **frozen-C,
same-occurrence gluing**, not a proof that every phase-advancing NN connection
is impossible. The corrected third shared face vertex has a later C occurrence,
with its intervening C phase explicitly retained.

## Context enters the active field

In the native five-coordinate order `C0, M0, C1, M1, C2`, the reference maps are

```
N advance: [0,3,4,1,2]
P advance: [2,3,0,1,4]
```

In particular,

```
[alpha, a, b, c, beta] -> [alpha, c, beta, a, b].
```

The neutron's old C2 coefficient beta enters the new active C slot. The old
active C1 coefficient b becomes the new C3 context. All coefficients on the
shared geometric face are retained, although one of those positions now has
a later phase occurrence. For a same-body reader advance, all four geometric
vertex coefficients are retained.

The active face is generally a superposition of common, positive and negative
C3 characters. The implementation retains and reconstructs all three Fourier
components, as well as the two complementary coordinates. It neither resets
the face to a pure character nor renormalizes away its complement. Complex
omega exponents are character phases, not realization indices: changing an
input character phase does not advance the origin or rename an occurrence.

The fifth, outside reference context advances by one C phase, with its
coefficient retained. **This outside-context comparison is an explicit
reference law, not derived particle dynamics.** Equal indices or coefficients
alone never identify unrelated occurrences.

## Check the combination, not just each tetrahedron

`phase-assembly-model.mjs` starts at the original, fixed C0/M0/C1[M1] seed.
It obtains candidate geometry, then searches native reader assignments subject
to the phase constraints; it does not assign phase suffixes by sorting vertices.
He-3 and He-4 reuse their candidate geometries. Li is searched as a whole
3P/3N/3e assembly, not by requiring a retained He-4 growth prefix.

PN/NE use the existing native full-carrier maps within one origin. Reader/NN
advances have explicit source and target frames, retained occurrences, C/M
successor chains, outside-context provenance, and five-slot permutations.
An assignment without these witnesses is rejected before display admission.

Entry-to-electron-exit certificates retain the chart, absolute origin, full
five-slot permutation, and complete command history. Coverage is checked at
that state level before projecting onto physical carriers: 5/5, 6/6 and 9/9
for the selected He-3, He-4 and Li-6 reference assemblies.

Different histories remain distinct even when their numerical coefficients
and geometric positions coincide. Branches may have equal phase indices at
different positions; they are not silently identified as one occurrence.

Two forward neutron re-readings restore the coefficient vector, but advance
the origin by two. They are **not** an identity realization command. The
unbounded origin and history are not quotiented by a finite permutation order.
An inverse coefficient map alone does not invert the realization history.

## Viewer

The selector now uses the corrected phase-reference models for He-3, He-4 and
Li-6. Only **Previous item / Next item** remain. These buttons change a retained
assembly-display prefix; they do not execute or undo physical phase transport.

Every visible item's four witnessed phase occurrences are labelled. Shared
vertices list all distinct C/M names, without carrier or origin annotations.
The per-item occurrence records retain their full provenance in the model data,
including when names coincide visually. The label toggle applies to the whole
visible assembly, not just the latest item. Underlying geometric IDs remain
neutral `vertex-*` keys. Display prefixes are ordered without decreasing the
selected witness origin; they are not a claimed particle-creation law.

The two shape selectors allow side-by-side comparison with one common
Previous/Next item index. Shorter assemblies stay complete while longer ones
continue. Selections start fully assembled; Previous/Next wrap at both ends.
Each retains its own phase certificate; comparison translations do
not assert an inter-atom phase identification. Both drawings share the label
toggle and face-transparency slider. This is a desktop-oriented comparison,
without mobile-specific stacking.

The old `helium3-tunnel-model.mjs`, `helium4-window-model.mjs`, and
`lithium6-reference-model.mjs` coefficient constructions remain diagnostic
negative controls. Their old receipts do not describe the current viewer.

## Verification

```
node research/strominger/checkers/check_phase_assembly.mjs
node research/strominger/checkers/check_fiber_space.mjs
```

Receipts:

- `results/phase-assembly/verification.json`
- `results/fiber-space/verification.json`

Tests cover both families' consecutive phases, native root marking, actual
shared geometric coefficients, nonzero contexts, all three face modes, all
five carrier coordinates, complete history-bearing entry/exit witnesses,
rejected locally-valid-but-combination-skipping phase edits, frozen-C maps,
missing carriers, and reversible desktop/mobile assembly display.
