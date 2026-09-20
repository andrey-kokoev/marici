# Coherence-realization depth is a dependent filler tower, not a source cutoff

## Question and adopted meaning

The operator accepted k as the depth of realized coherence. This replaces our earlier unlicensed use of arithmetic edge cutoff as its meaning. Construct the corresponding bounded HoTT representation before introducing another analytical example.

Keep three indices distinct:

- i labels an analytical presentation;
- iota labels independently specified source parameters, such as place set or cutoff;
- k is the maximum coherence-cell degree included in the realization record.

A k-extension does not by definition add a source coordinate, change a cutoff, or apply suspension. No temporal interpretation is assigned to composition or extension.

## Target and scope

Fix a source-declared finite diagram shape and an analytical target with typed objects, maps, and the applicable higher comparisons. Objects must retain their source anchors, domains, endpoint and cycle data, pairings, and determinant structures where these have been constructed. A comparison must preserve the declared structure; equality of underlying scalar outputs is insufficient.

The explicit formulas below give the ordinary HoTT function-type prototype. For the analytical application, the mapping types must represent the appropriate structured comparisons. An ordinary set of linear maps has no nontrivial higher identity structure merely because we call it a mapping type. If analytic homotopies or chain homotopies are intended, their enriched/derived target must be supplied.

The repository's relative Waldhausen-cone enhancement is a candidate target for such data. Its formal stable envelope does not by itself construct a preferred physical analytical realization. This note does not silently identify that envelope with the physical target.

## First four realization records

Use four presentation vertices numbered 0,1,2,3 at one fixed source parameter iota.

R_0 contains the four typed presentation objects X_0,...,X_3 and their retained source data. For a same-datum claim, it also names the common source and the required realization interfaces; equivalence is a witness to be supplied, not a consequence of the number of vertices.

R_1 extends R_0 by the six comparison maps f_ij:X_i->X_j for i<j, with their structure-preservation witnesses. This is the one-dimensional boundary data.

R_2 extends R_1 by four triangular homotopies. For i<j<l, the triangle has type alpha_ijl(x): f_jl(f_ij(x))=f_il(x), for x:X_i. Function extensionality can repackage these as equalities of functions.

The tetrahedral boundary determined by R_2 has two explicitly parallel path composites. For x:X_0, define:

- p(x) := ap(f_23,alpha_012(x)) concatenated with alpha_023(x);
- q(x) := alpha_123(f_01(x)) concatenated with alpha_013(x).

Both are paths from f_23(f_12(f_01(x))) to f_03(x). Their endpoints and types agree before asking for another coherence.

Define Fill_2(r) := product over x:X_0 of the identity type p(x)=q(x), including any additional source-structure compatibility demanded by the fixed diagram. A tetrahedral witness Theta is a term of this type.

Then R_3 := sum over r:R_2 of Fill_2(r). The construction retains the entire lower record together with its filler. It does not replace the boundary by its scalar readout.

## The k-to-k+1 operation

For each declared next cell family, define R_(k+1) := sum over r:R_k of Fill_k(r). The canonical map pi_k:R_(k+1)->R_k is first projection.

There is an equivalence fib(pi_k,r) equivalent-to Fill_k(r). This is the standard fiber-of-dependent-projection theorem, proved by identity elimination. Thus the extension problem is precisely the inhabitance problem for the filler type over the fixed lower datum.

An extension of one r is (r,theta) with theta:Fill_k(r). A uniform forward extension is a dependent function assigning such a theta to every admitted r. It is not provided automatically by the dependent-sum definition.

The equality pi_k(r,theta)=r records preservation of the lower datum. It is not evidence that every boundary has a filler.

For a single prescribed tetrahedron, there are no automatic new geometric cells above degree three. To request R_4, the source must specify further boundary data: for example two independently supplied tetrahedral witnesses Theta and Theta' over the same lower record, whose comparison has type Theta=Theta'. A four-simplex instead requires its actual five tetrahedral faces and their shared-face identifications. Repeatedly naming a higher index does not supply these boundaries.

This note defines bounded records. It does not assert a generic internally constructed infinite semisimplicial type or bypass the separate foundations needed for a full unbounded coherent diagram.

## A genuine higher-coherence hostile

The ordinary function-type prototype already distinguishes triangle existence from tetrahedral compatibility.

Take all four objects to be copies of the circle, and all six maps to be identities. Use the constant homotopy for three triangles. For alpha_023 use the homotopy from identity to itself that rotates the circle once, obtained from circle multiplication and its generating loop.

Every edge and every triangular comparison exists. At the base point, however, the two tetrahedral boundary paths are the generating loop and the constant loop. A tetrahedral filler would identify them. The standard theorem pi_1(circle)=Z rules this out.

Therefore R_2 can be inhabited over these fixed edges while its particular Fill_2 fiber is empty. Replacing alpha_023 by the constant homotopy gives an inhabited filler fiber. The distinction is in the comparison witnesses, not in edge ranks, matrices, or scalar endpoint values.

This is a HoTT/topological consistency test of the proposed type specification, not an assertion that the actual theta source has this circle obstruction. A circle here is the higher circle type with its loop structure, not merely the set of complex numbers of modulus one.

## Residues and corrections have constrained meanings

Failure to have constructed a term of Fill_k(r) is not proof that this type is empty. Keep 'unresolved inhabitance' distinct from 'proved obstruction'. A numerical residue needs an additional source-derived obstruction map out of the boundary data; it is not supplied by HoTT terminology.

For an equality a:r=r', dependent transport gives an equivalence Fill_k(r) equivalent-to Fill_k(r'). Consequently a genuinely empty filler fiber cannot become inhabited through an equivalent relabelling of the same structured boundary. A correction must either establish a previously unresolved filler, or use an explicitly permitted modification of the boundary/source problem. Merely choosing a different presentation cannot remove a proved obstruction.

To combine residuals from two lower tetrahedra, one must further construct their common target and a typed combination operation. To impose two-sided extension constraints, one must supply the restriction maps between those boundary problems. Neither operation is hidden in the definition of R_(k+1).

## Where existing research fits

`research/voevodsky/a-common-graph-presentation-generates-all-opposite-edges-at-fixed-realization-dimension.md` constructs source-anchored chart comparisons. Their common-source factorizations provide compatible internal coherence witnesses; they are not arbitrary triangle choices as in the hostile above.

`research/voevodsky/the-joint-source-graph-makes-the-chamber-twistor-tower-analytically-equivariant.md` supplies naturality for source successors already given. This is evidence for particular cells of the source-indexed diagram, not a general section of every filler projection.

`research/voevodsky/the-relative-equivariant-eight-lattice-tower-admits-a-universal-waldhausen-cone-enhancement.md` supplies a formal stable setting for relative cofibers and octahedral comparisons. Comparing independently defined physical maps with these transported/formal maps remains a separate analytical witness.

`research/voevodsky/realization-dimension-successor-comparison-gate.md` concerns a different index: an independently prescribed arithmetic dimension successor. Its missing arithmetic object is not repaired by renaming the present coherence depth.

## Prior-result audit and scope correction

The subsequent source search found that the dependent-filler pattern is already implemented more concretely in `research/voevodsky/agda/DGPyramidBoundary.agda` and `research/voevodsky/agda/DGPyramidFiller.agda`. The latter source was inspected directly. The boundary discrepancy is Delta=HC-e hM; its closure is derived from the differential equations and graded composition. The admissible filler is the dependent type of K together with delta K=Delta and separate support, endpoint, generic-Q, and Rees/Cartier witnesses. No constructor promotes an unframed filler to a framed one. `research/voevodsky/dg-pyramid-final-requirements-matrix-v1.md` reports checked interfaces and negative controls, while explicitly withholding an independently instantiated physical Q/support adapter. Those verification reports were read, not freshly rerun.

More importantly, `research/voevodsky/combining-h234-and-h134-localizes-the-open-class-to-the-kernel-of-positive-to-signed-forgetfulness.md` records that the semilocal signed tetrahedral discrepancy is already zero, naturally under its admitted source refinement. The associated face-recovery and rapid-decay-quotient packets specify the required observer-generated essential image and asymptotic category. The abstract R_2-to-R_3 extension problem therefore cannot be presented as a newly discovered missing signed cell in that system.

The circle hostile concerns freely specified homotopies in a different target. It does not satisfy a proved adapter into the source-anchored analytical comparison problem, whose triangle witnesses are constrained by common-source realization. It is not evidence that this source needs an independent next coherence degree.

`research/nima/normalized-rank-two-faces-force-all-determinant-path-coherence.md` closes higher scalar path comparisons once every reachable normalized face and common frame satisfies its hypotheses. `research/kitaev/self-closing-towers-have-three-distinct-termination-mechanisms.md` and `research/strominger/the-strict-metaplectic-coherence-tower-terminates-at-the-cocycle-cell.md` likewise explain when governing lower data force higher cells. A filler tower may terminate or have forced fibers; its dependent-sum definition does not establish nontrivial continuation.

The remaining semilocal issue is a source-admissible positive/metric lift of an already coherent signed diagram, with the separately recorded global completion requirements. It is not automatically another homotopy degree. The generic dg physical adapter and the semilocal positive lift are distinct typed obligations; their common use of filler language does not identify them.

## Disposition

Reconstructed at type-specification strength: bounded coherence records and the fiber characterization of their forgetful maps. This is consistent with, but less concrete than, the existing framed Cubical Agda interface. It supplies neither new source coherence nor an argument for an unbounded hierarchy.

The source signed tetrahedron must be treated as closed at its recorded strength. A new cell is justified only by an independently typed comparison not already forced by those theorems. The circle example is retained solely as a generic type-theoretic illustration.

No analytical source realization, physical correction mechanism, seven/eight-simplex, or infinite stabilization has been inferred. No new numerical checker or proof-assistant verification was run in this audit.
