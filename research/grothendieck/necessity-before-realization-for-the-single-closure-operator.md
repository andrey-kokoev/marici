# Necessity before realization for the single closure operator

## Correction after following the construction beyond the facade

The frame-gap diagnosis below was incomplete. `ClosureFiniteGluingNormalization.agda` already derives global frames from pieces, boundary types, and attachment maps by recursive pushout normalization. `ClosureDependentRefinementTrees.agda` similarly derives frames for its admitted dependent nodes. Thus the facade's frame parameters are not evidence that all frames remain unconstructed. The outstanding analytical question is whether the arithmetic and Green packages instantiate the same constructor data, including the polarized attachment compatibility. See `closure-operator-generated-comparison-and-the-arithmetic-attachment-obligation.md` for the corrected investigation and newly checked local-to-global necessity lemmas.

## Starting point

The operator under investigation is recursive closure by attachment, decomposition, and cut-and-rejoin, organized in Nima's nested Waldhausen S-construction sketch. Arithmetic, analytical presentations, and their comparisons are to be constructed internally from this operation, not supplied as unrelated repair interfaces.

This note separates consequences of the presently defined operation from the stronger generation theorem we seek. It reports source inspection and mathematical arguments, not a new Agda verification.

## 1. What the implementation actually constructs

`research/voevodsky/agda/ClosureCofiberComposition.agda` takes types A,B,C and maps f:A->B, g:B->C. It constructs the induced cofiber map, acts on attachment paths, and derives

cofib(cofib(f)->cofib(gf)) equivalent to cofib(g).

Its cut and rejoin maps and both round trips are outputs, not assumptions. Thus changing a cut does not change the complete object. The attachment data are part of that object.

`research/voevodsky/agda/NestedFourPresentation.agda` takes a target category and a complete nested functor. It constructs its expansion and inverse nesting, preserving mixed naturality. It does not construct the original category or the functor's arrows from nothing.

A particularly relevant facade is `research/voevodsky/agda/ClosureReferenceNormalForm.agda`. Its module header takes:

- cut-indexed input/output carriers X,Y;
- reference carriers A,B;
- inputFrame(k):X(k) equivalent to A;
- outputFrame(k):Y(k) equivalent to B;
- operation:A->B.

It derives presentation views and proves reference-based cycles trivial. The realization frames themselves are input parameters. This is the exact place where a universal generation claim would need to strengthen the current implementation.

## 2. First necessity: complete-object transport, not scalar agreement

If e:X equivalent to Y is a generated cut-change, every probe object P has an induced equivalence Map(P,X) equivalent to Map(P,Y), by composition with e. The inverse is composition with e inverse; their homotopies follow from the cut/rejoin homotopies.

Consequently a genuine cut-change preserves the entire represented behavior, including all attachment information. A scalar output is only one composite out of that behavior. Equality of scalar values does not imply equivalence of their sources or establish that an independently specified map is a cut-change.

This explains the previous route reconstruction results without elevating them into the central theorem: they diagnose that particular output quotients are not equivalent presentations of the complete source. Their repair is not automatically the missing arithmetic realization.

## 3. Second necessity: distinguish reindexing from arbitrary holonomy

The common-reference implementation proves that its generated routes reduce to a reference normal form, and their closed cycles act identically on every value. The companion holonomy regression also constructs a nontrivial Bool-by-Bool swap loop fixing a selected value.

Therefore the internal obligation is not merely that the Xi value returns. It is to show that the proposed arithmetic/Green comparison is one of the generated compatible routes, with the same attachment data and the specified higher comparison. Otherwise the existing reference-route theorem does not apply to it.

This is a construction obligation inside the operator program, not a request to assume an external comparison.

## 4. What is not forced by the present universal law

The cofiber theorem is polymorphic in its types and maps. The stable S-construction sketch is likewise applicable to different stable categories. The zero category has trivial closures; Perf(Q) has nontrivial ones. Both satisfy the closure laws. Thus those laws alone, without a specified seed or universal generation prescription, do not select a unique nontrivial arithmetic realization.

There is a sharper metric test. Suppose one tries to derive a positive definite form on every nonzero finite-dimensional rational vector space naturally under every linear isomorphism, using only that unstructured category. Naturality for 2 id would require

q(2x,2x)=q(x,x).

Bilinearity gives 4q(x,x)=q(x,x), forcing q(x,x)=0. This contradicts positive definiteness. Hence a positive metric cannot be an isomorphism-invariant output of that bare category alone.

This does not rule out an internally generated metric. It specifies what its construction must achieve: the full generated object must include additional internal structure that distinguishes norm-changing transformations from its admissible symmetries. One must derive this structure from the operator and its stated seed, rather than quietly insert a chosen metric. The argument does not assume that 2 id preserves such a future structured object.

## 5. The hard theorem, now stated at the operator level

Specify a seeded closure system G and its admitted constructors. Then prove, rather than parameterize, that the desired arithmetic and Green presentations are generated views of G. In particular:

1. construct their carriers and operations by evaluation of the same closure expressions;
2. construct their frames and comparison paths from attachment/cut operations;
3. identify the internally generated duality or quadratic structure and prove that the comparison preserves it;
4. identify the Xi section and the local prime-energy expression within those views;
5. derive the vanishing of the existing energy residual from that generated compatibility.

The terminal implication cannot be presumed while defining the quadratic structure. Nor can it be replaced by a metric pulled back along the desired comparison unless that metric is independently identified with the already specified Green form.

The order is necessity, then construction: first characterize the complete generated object and its invariant structure strongly enough to force compatibility; then give the realization on generators and attachments.

## 6. First precise outstanding question

What is the seed and universal property of G that produces the input/output frames currently passed to `ClosureReferenceNormalForm.Model`?

Possible answers are not to be selected for convenience. They must be found in the intended operator's definition or proved from it. If G is the free closure on a given arithmetic source, the source remains part of the stated input. If G is intended to generate the arithmetic source itself, its distinguished initial data and generation rule must explain why that source appears rather than an arbitrary model.

This is the first missing necessity statement in the inspected implementation. It is upstream of detector calibration, finite route tomography, and the proposed source-to-Green metric adapter. We should work here rather than substitute another downstream task.

## Sources inspected

- `research/nima/nested-closure-system-full-categorical-construction-sketch.md`
- `research/voevodsky/agda/NestedFourPresentation.agda`
- `research/voevodsky/agda/ClosureCofiberComposition.agda`
- `research/voevodsky/agda/ClosureReferenceNormalForm.agda`
- `research/voevodsky/closure-reference-normal-form-and-residual-actions.md`
