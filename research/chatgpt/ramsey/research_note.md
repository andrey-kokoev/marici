# Native birth-boundary test

Date: 2026-10-30
Source: andrey-kokoev/marici at cb0c25477b0b710fc1feb9dd5cc1e82e8ecdef6c.
Execution: isolated local snapshot, Node.js v22.16.0 and Python/SymPy 1.14.0. No repository files were modified. All ten imported Git blob hashes were checked.

## Result

The native same-body N reread exposes the two missing spatial faces of the proposed tetrahedral birth boundary. For admissible markings, selecting their existing native transfers gives a certified 2P/1N/2E patch with every face of the N body witnessed.

The complete occurrence-labelled four-contact surface is not a closed tetrahedral boundary. It has six vertices, nine edges, four triangles, and a six-edge boundary. Forgetting two occurrence distinctions maps it onto a closed tetrahedral surface. The original proposal therefore succeeds as an incidence description of the N body, but not as a native same-boundary higher filler.

The retained output is a grade-changing comparison record and a relative four-triangle surface. No additional N particle, freely added tetrahedral filler, or neutron-count rule is inferred.

## 1. Exact source incidence

Consider a native PN followed by NE. In the common reference marks set

    a = C1, b = M1, p = M0, q = C2.

The PN face is F_in=[a,b,p]; the NE face is F_out=[a,b,q]. These are contact faces, not the complete P and E bodies. Their union uses exactly the four vertices of the intervening native N primitive:

    W = [a,b,p,q] = [C1,M1,M0,C2].

The apex link [p,q] and the other faces S_a=[a,p,q], S_b=[b,p,q] are already present in that cell's incidence. With the displayed orientations,

    boundary(W) = F_out - F_in + S_b - S_a.

Boundary(F_out-F_in) is nonzero; both side terms are necessary for this chain to close. Its Gram determinant is 4 in the native sum-one barycentric metric, so this N tetrahedron is nondegenerate. Its squared Euclidean volume is 1/9 in those coordinate units.

The complete root P chart already generates this N reference geometry and its C2 mark. At initial construction there are two geometric cells but only the P reader and no transfer operations. Reference support and occupied support must therefore not be conflated.

## 2. The source operation that exposes both sides

`GenerativeAssemblyRules.outgoing` supplies a same-body N reader advance when `completeN` accepts its new incoming face. Its four body aliases are

    M0' = M1, C1' = C2, M1' = M0, C2' = C1.

The outside C0 reference is recomputed from the actual adjacent regular primitive. It is retained, not dropped. The five-slot coefficient permutation is

    sigma_N = [0,3,4,1,2].

The new absolute origin is o+1. From that reader:

    inverse-PN crosses [M1,C2,M0] = S_b;
    NE crosses [M0,C2,C1] = S_a.

No new operation was registered to obtain either face. Both were found by calling the unmodified native generator.

For the tested charts, rereading is admitted exactly when the N primitive's long internal diagonal is C1--C2. This occurs for eight of the 24 root markings, at every tested P-reread origin 0 through 7. The other 16 markings have no such direct same-body N advance; this is not a claim that every longer construction from them is impossible.

The successful native construction word is

    prior P rereads; PN; NE; N reader advance; inverse-PN; NE.

Every prefix is compatible. The completed patch has two P bodies, one N body, two E bodies, and two distinct N readers. Independent root and reverse-exit traversals pass, as does the native occupied-contact check. All four N faces have actual selected native transfer witnesses.

## 3. Full occurrence labels change the boundary

Let o denote absolute realization origin, not a shell number or physical time. The four actual contact triangles, omitting their unchanged geometric coordinates from this display, are

    F_in:  M_o,     C_(o+1), M_(o+1)
    F_out: M_(o+1), C_(o+1), C_(o+2)
    S_b:   M_(o+1), C_(o+2), M_(o+2)
    S_a:   M_(o+2), C_(o+2), C_(o+3).

The retained common occurrences are M_(o+1) and C_(o+2). The same physical p location supports distinct occurrences M_o and M_(o+2); the same physical a location supports distinct occurrences C_(o+1) and C_(o+3).

Using the orientations from section 1, the remaining boundary is the directed six-edge cycle

    C_(o+1) -> M_o -> M_(o+1) -> M_(o+2)
              -> C_(o+3) -> C_(o+2) -> C_(o+1).

Its f-vector is (6,9,4), and its Betti numbers over the rationals are (1,0,0). The geometric projection identifies the two renewed vertex pairs and has f-vector (4,6,4), Betti numbers (1,0,1), and zero boundary. Thus a two-cycle appears only after those occurrence distinctions are forgotten.

This is a necessary-label test: the failure occurs before any attempted equality of complete charts and coefficient records. The unchanged retained edge is identified using the actual phase-advance witness, not by identifying its parent readers.

There is a sharper local typing obstruction. The old-labelled side faces

    [C_(o+1), M_o, C_(o+2)]
    [M_(o+1), M_o, C_(o+2)]

cannot be ordered as any of the native P, N or E active-window templates at any nonnegative origin. The checker solves the common-offset condition for all vertex orders; it does not assume a numerical cutoff on possible origins. Their renewed versions do match the native templates. A same-occurrence side-face completion would therefore need an additional admissible comparison, not just another drawing of the same face.

The four-triangle strip can be read as a relative comparison between the old cross-channel edge C_(o+1)--M_o and the renewed edge C_(o+3)--M_(o+2), with two-step C and M continuation paths on its other sides. Treating this retained surface as a birth witness is an interpretation of an explicitly constructed object, not a proof that it is a native identity-type 3-cell.

## 4. Actual spatial involution and retained expansion

The native N reread acts on its four geometric vertices by

    (C1 C2)(M0 M1).

For admitted rereads this is a proper Euclidean half-turn. An exact affine map was derived from its four ordered vertex images. It preserves the native metric and transports all five N/P reference marks and all six E reference marks, including the outside contexts, to their corresponding other-side charts.

Its fixed locus in the N tetrahedron is the line segment joining

    (C1+C2)/2 and (M0+M1)/2.

The earlier fixed-triangle proposal used a different map: the apex-only exchange (M0 C2). That is not the native N reread. No fixed neutral sheet follows from this native operation.

For the complete reader, two rereads satisfy

    R_N^2(chart, o, permutation) = (chart, o+2, permutation).

The chart and coefficient permutation return, but the absolute origin does not. Replacing the endpoint by the old reader is rejected. Likewise the coefficient NE permutation squares to identity, but native E readers are terminal; this does not create a native inverse NE operation.

## 5. Path-level completion is a separate, explicit theorem

The inspected repository contains `RootedSpokePathCompletion`, `MarkedTetrahedronCoherence`, and `RetainedTetrahedralPackage`. These work with actual typed paths and triangular comparison witnesses, not arbitrary geometric incidence or raw directed reader operations.

For two genuinely path-typed faces with common edge,

    u:a->b, v:a->p, w:a->q, s:b->p, t:b->q,
    alpha:(u;s)=v, beta:(u;t)=w,

set h=inverse(v);w. Cancellation supplies gamma:(v;h)=w. The repository's `unique123` derives delta:(s;h)=t together with tetrahedral coherence, retaining alpha and beta. A new triangle/filler pair is derived; a previously supplied arbitrary fourth face is not declared coherent.

This theorem does not solve the native occurrence obstruction in section 3. It requires one common marked boundary and actual path typing. The side-face occurrence data constructed by the native reread do not have that same boundary.

The accompanying finite strict 2-groupoid regression keeps S3 edge actions, integer grades, and independent central integer face labels. In that strict test, gamma=0 and delta=alpha-beta. Erasing delta fails whenever alpha differs from beta. These executable checks test the algebraic interpretation; they are not a fresh Agda compilation. No Agda compiler was available in this instance, and no new formal-proof verification is claimed.

## 6. Executed checks

- All ten imported Git blob hashes matched the pinned manifest.
- 192 PN/NE routes: 24 root markings, eight reachable P-reader origins each. Every route matched the proposed N-cell incidence and retained its full records.
- 576 deliberately altered source-type, origin, or coefficient-transfer controls were rejected.
- 64 direct N-reread completions: every resulting 2P/1N/2E patch passed prefix, root, exit and four-face contact checks.
- 128 routes lacked this particular same-body N reread.
- 64 attempts to replace a two-reread endpoint with the old-origin reader were rejected.
- 64 exact spatial half-turn checks transported all complete geometric marks.
- 64 occurrence-boundary checks: zero closed occurrence surfaces, 64 closed geometric projections, six remaining boundary edges in every lifted contact surface.
- 5,832 exact typed edge/grade tests and 5,400 proof-relevant face-label tests passed; 4,320 face-label erasures were rejected.
- Exact integer chain identities and rational homology calculations distinguish the two-face disk, tetrahedral sphere, filled tetrahedron, and actual native occurrence strip.

## 7. Reproduction

From this directory, with Node.js and Python with SymPy available:

    node check_native_boundary.mjs
    node check_native_side_completion.mjs
    python check_boundary_algebra.py
    python check_reread_geometry.py
    python check_occurrence_boundary.py

The scripts import the included unmodified source snapshot. Outputs are the five `*_results.json` files. Native construction packets retain exact charts, coefficient permutations, absolute origins, prefix histories, occupied contacts and phase frames.

## Disposition

The proposed extra incidence is native: the apex edge and both side faces belong to the N reference tetrahedron, and admissible same-body rereading exposes both sides through existing native transfers. A fully witnessed occupied patch was constructed.

The stronger proposed identification with one closed same-occurrence tetrahedral birth witness fails this test. The retained comparison has an open six-edge boundary and a grade shift. Its geometric closure cannot be promoted to native higher closure. No neutron-excess formula, shell-contraction operator, energy, stability criterion or physical-time interpretation is established here.
