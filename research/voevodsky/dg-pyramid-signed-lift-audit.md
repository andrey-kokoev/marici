# Resuming the Cubical model: forced signed completion versus structured lift

## Result

The model now checks a reduction, not an existence assumption: when signed horn completion is contractible, the entire structured completion problem is equivalent to the fiber over its forced signed completion. No inhabitant of that remaining fiber is assumed or constructed by the reduction.

Implemented in `agda/DGPyramidSignedLiftAudit.agda`; tested in `agda/DGPyramidSignedLiftRegression.agda`. Existing boundary, frame, and adapter modules were not changed.

## Audit of the current model

The current tree is substantially beyond the original ten-iteration requirements matrix. `DGPyramidPartialMariciAdapter.agda` already bundles many later certificate interfaces and explicitly retains `PhysicalCompletionGates`. Those gates include the mixed-variance mate, both physical endpoint connectors and their carrier identifications, physical e and H_C comparisons, Cartier/Rees comparison, and the native kernel realization. Even completion of those gates does not construct the separate `AdmissibleFiller`.

Thus the earlier description that the model merely lacks a generic Q/support interface is stale as a description of its API. It must not be used to disregard the later interfaces. Their fields still require concrete source witnesses; compiling the records does not instantiate the physical comparison.

`DGPyramidHigherCoherenceHom.agda` also already separates negative coherence degrees from positive Ext degrees. Its no-lift theorem uses an explicitly supplied nonzero obstruction class. It does not prove that the signed semilocal tetrahedron has that obstruction. Its augmentation record requires a new transgression and proves that a compatible retraction to the obstructed complex is impossible. None of these statements identifies an Ext enlargement with a k-step of pure coherence realization.

`DGPyramidThreeLayerHigherHom.agda` explicitly leaves the physical vertical maps and composite nullhomotopy unconstructed. Its level names do not supply maps.

## Exact checked reduction

The `SignedHorn` module takes an equivalence R:A equivalent-to B and a boundary b:B. Its completion type is fib(R,b), including both the recovered face and its boundary equation. Equivalence gives a contractible completion type, with center c. For any structured lift family L, the module proves that the sum over s:fib(R,b) of L(s) is equivalent to L(c).

The hypothesis is a whiskering equivalence, not bare faithfulness. The source face-recovery note argues for such an equivalence on the specified observer-generated essential image. This module does not postulate or formalize the analytical representation theorem itself.

The `FramedComparison` module reuses the existing DG types without weakening their predicates. Given an actual comparison map from `BoundaryFiller P Frame` to a signed completion type S, define `RemainingAt s` to contain:

- an actual DG boundary filler u, including its boundary equation;
- an identification of its signed comparison with s;
- all four existing frame witnesses on the candidate underlying u.

It proves that the total space of `RemainingAt` is equivalent to `AdmissibleFiller P Frame`, with explicit inverse and round-trip paths. If S is contractible, it then proves that `AdmissibleFiller P Frame` is equivalent to `RemainingAt` at the forced signed point.

This removes independent choice of a signed completion from the list of possible extra obstructions. It does not produce a DG filler, a positive metric, or an endpoint/completion witness. The four existing predicates do not automatically include all analytic positivity and domain requirements; any claimed physical instantiation must account for these explicitly.

The separate `DiscrepancyComparison` module checks precisely what signed vanishing transfers: an identification between the observed DG discrepancy and the signed discrepancy, followed by signed vanishing, proves vanishing of the observed discrepancy. It does not prove the DG discrepancy is zero or exact, or that a framed lift exists.

## Regression strength

The regressions reuse the existing explicitly nonphysical terminal fixture. Both have the same contractible signed completion and the same DG differential. With the original frame, the remaining fiber is inhabited. With an empty support predicate, an unframed filler still exists but the remaining fiber is provably empty. This tests the reduction and retention of frame conditions, not the actual analytical source. It does not repeat the circle example as a purported physical counterexample.

## Verification

A fresh dependency-closure check ran with Agda 2.8.0.1 and Cubical 0.9:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/DGPyramidSignedLiftRegression.agda`

Exit 0. Both added modules use `--safe --cubical --guardedness`; no holes or postulates were added. The first incremental run caught an incorrect library accessor for contractible equivalence fibers; replacing it by `equiv-proof (snd whiskering) boundary` fixed the error. The subsequent fresh closure check passed.

## Actual stopping point

No concrete implementation of the semilocal signed target and the DG-to-signed comparison was found in the inspected adapter/higher-Hom modules. We therefore did NOT install the prose signed-coherence theorem as a purported physical Agda inhabitant. The exact physical frame, its analytical domains/completion conditions, and the comparison map remain to be instantiated from source mathematics.

This is a checked narrowing of obligations, not the requested full analytical instantiation. The next useful work is constructing that comparison and accounting for the current `PhysicalCompletionGates`, rather than adding another generic tower or assuming a physical filler as a record field. The known coherent signed diagram must remain distinguished from the generic DG boundary until those comparisons are supplied.
