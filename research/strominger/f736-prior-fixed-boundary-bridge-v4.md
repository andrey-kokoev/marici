# Prior bridge for translating the paired F736 completion without changing shared faces

## Search target

After locating the dependent bottom/filler constructor, search for the comparison needed to preserve its shared boundaries across presentations. This search inspected prior source and theorem statements; it did not compile Agda or certify analytical estimates.

## 1. A fixed-boundary bridge already exists

Read `research/nima/tetrahedron-presentation-bridge.md` and the exported theorem declarations in `research/nima/agda/TetrahedronPresentationBridge.agda`.

The source defines

    FixedBoundaryTarget.Goal
      = (s : CubicalSurface) -> CubicalTetrahedron(s) equivalent old_filler(s),

where all four faces in old_filler(s) are translated using the SAME triangle-comparison map, determined only by that triangle's fixed edges and witness.

`FixedBoundaryTarget.equivalence` inhabits this goal. It is not merely a record slot or a horn-relative assumption. The source also supplies proved `route-naturality` and `face-naturality`.

This matters for the F736 patch: translating the common H736 face must not depend on whether it is being viewed from T324 or T325. The theorem's context-independent triangle map provides that property in the declared path-coherence setting, provided the retained edge/face identifications into that setting are the same.

It does not identify two arbitrary independently selected presentation maps.

## 2. The bridge transports the entire paired completion

The horn-relative part of the same module supplies:

    completion-equivalence : CubicalCompletion equivalent OldCompletion,
    complete-then-translate,
    translate-then-complete.

The first is built as a dependent sum equivalence: translate the missing face and transport its filler into the corresponding boundary-indexed type. The two following paths identify the canonical completion on either side after translation.

The source's explicit missing-face example uses its 023 horn; the fixed-boundary theorem covers the complete surface. Applying it to the current missing123 problem requires the actual local reindexing, not silently treating differently indexed bottom faces as equal.

For F736 the retained target remains

    (H745,Theta324) over (H731,H732,H736),
    (H760,Theta325) over (H734,H735,H736).

Use one face translation for H736, then translate both completed surfaces with that fixed shared boundary. If a bottom is supplied independently, retain its dependent pair comparison rather than replacing it by a new chosen center.

## 3. The bridge has a computation API

The exported theorems

    equivalence-route-computation,
    equivalence-sweep-computation

identify the existing filler map with an explicit normalized route expression and with its direct sweep expression. They do not replace the selected equivalence by a convenient alternative.

The proof includes unit/associator correction paths, path-over transport and explicit square pasting. This is useful for a witness-level calculation: compare the actual route formulas instead of assuming that two equivalences between the same filler types coincide.

`TriangleProjection` proves edge-package projection compatibility and endpoint preservation. Thus translating a face retains its marked edges, rather than merely its scalar boundary value.

## 4. A further higher comparison remains open in the inspected source

Read `research/nima/four-simplex-pentagon-bridge.md` completely.

The independent marked pentagon has its own paired missing-tetrahedron completion. The note explicitly distinguishes that completion from an induced four-cell equation-family completion. Its target comparison is equivalent to equality of their canonical centers, and neither that center coherence nor the final general comparison is inhabited in the inspected source.

The note does supply computation laws and a sweep cube, but says the remaining step is higher boundary normalization. Separate contractibility of the two completion spaces is NOT used to assert that their centers coincide.

For the F736 task this is a warning, not a new required arbitrary-dimensional gate: fixed-boundary tetrahedral translation is available, while compatibility with an independently defined four-dimensional pentagon presentation must not be claimed automatically if the task later requires it.

## 5. Check against the signed analytical lift audit

Search of the two inspected owner Agda trees for semilocal/rapid-decay target declarations found the signed-lift audit and regression references, not a concrete analytical target implementation.

`research/voevodsky/dg-pyramid-signed-lift-audit.md` expressly states that no concrete semilocal signed target and DG-to-signed comparison was found in its inspected adapter/higher-Hom modules. Its formal module also says it postulates no semilocal analytical equivalence. The regression is explicitly nonphysical.

This is consistent with the present distinction:

- paired path-horn construction: available;
- lossless packaging and dependent pair agreement: available;
- fixed-boundary Cubical/route presentation bridge: available;
- exact analytical response-to-cutoff realization comparison for F736: not supplied by those generic modules.

The search does not prove that no analytical implementation exists elsewhere.

## 6. Refined constructive use

Use the fixed-boundary theorem AFTER declaring a common analytical comparison target and actual interpretation of the retained F736 edges/faces into it. It then removes a formal presentation mismatch while preserving the common H736 and both bottom/filler pairs.

The analytical comparison must still carry the full observer anchor, regulator/domain data, finite remainder, endpoint channels and both ordered placements. A context-independent formal face map is not itself a map from physical response operators to cutoff/spectral realizations.

Therefore the next extraction can be split accurately:

1. analytical interpretation with source/domains and retained witness data;
2. existing fixed-boundary presentation translation;
3. existing paired completion and comparison to any prescribed bottoms;
4. structured physical/positive lift, where required.

No new generic paired completion or generic tetrahedral presentation theorem needs to be invented. The newly located bridge is reusable prior work, with the analytical interpretation remaining explicit rather than hidden inside formal contractibility.
