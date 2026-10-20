# The actual six-arrow free realization is a bouquet of three circles

## Result and scope

`agda/SourceGraphFreeRealization.agda` proves an explicit equivalence

    SeedTetrahedronBridge.Realization ≃ Bouquet Chord
    Chord = bc | db | ba.

This reuses the actual predecessor, not a fresh substitute graph. A second theorem gives its exact mapping property: for every type X, maps from Realization to X are equivalent to a point of X for every vertex and an endpoint-correct path for every primitive occurrence.

**Thus the topology is determined relative to the declared task: freely interpret each retained arrow as a path, with no extra relations.** The task is not proved uniquely selected by native WG. This is a useful stronger boundary than arbitrary span selection: an independently stated mapping property fixes this realization, rather than selecting a circle as the desired output.

The three-circle bouquet is not a single circle (standard fundamental-group/H1 distinction). This packet formalizes the bouquet equivalence, not a separate fundamental-group classification or circle-inequivalence theorem. An independent exact cellular calculation gives H1 rank 3. Neither is an all-WG impossibility claim.

## Predecessor and relation audit

- `research/nima/agda/ActualSeedEndpointTable.agda` declares four vertices and six distinct occurrences AB, BC, CA, AD, DB, BA. Its triangle equations only identify adjacent **endpoints**. They do not fill path cycles. Presentation reversal retains AB's occurrence label rather than replacing it with BA.
- `research/strominger/agda/NativeExtensionFamilyAudit.agda` declares the same six indexed edges and retains their endpoint list in graphQ. The new module maps every predecessor occurrence to its endpoint-correct native edge and proves an equivalence with the total native Edge family.
- `research/nima/agda/SeedTetrahedronBridge.agda` already supplies precisely the desired node/edge HIT, with **no face constructors**. Its `WithFaces` module takes additional inputs; its all-composite spine control replaces independent edges. Neither provides missing seed relations.
- `research/nima/agda/SeedFaceObstruction.agda` already proves that AD followed by DB cannot equal AB, and AB followed by BC cannot equal reverse CA, in this free realization. These results are reused in the fresh closure.
- `research/nima/agda/SeedGeometricResponseInterpretation.agda` already constructs dependent response families from supplied edge equivalences. Rebuilding that interface would not be new progress; it does not select the edge actions.
- `rooted-spoke-shared-assembly.md` already explains why a different three-spoke primitive source can generate a filled tetrahedral package. Its composite diagonals must not be substituted for the six independent occurrences here.

This audits the frozen six-arrow source, not every richer filled source package in the repository. A genuine supplied filling in another source must be compared through its actual input contract, not refuted by this free-realization theorem.

## Constructed comparison

Choose the spanning tree AB, AD, reverse CA. This choice is proof coordinates, not physical data. Collapse those tree paths and all four nodes to the bouquet base; send BC, DB and BA to its three loops. Expand those loops to:

| Chord | Based path at A |
|---|---|
| BC | AB; BC; CA |
| DB | AD; DB; reverse AB |
| BA | AB; BA |

The implementation uses the exact double-composition variants of these paths, including unit legs. Cubical composition fillers give the tree-contraction homotopy on every original edge. Congruence of double composition gives the other inverse homotopy on each bouquet loop. Both homotopies are checked as HIT eliminations, including their boundaries.

`Universal.universal` establishes the mapping equivalence with full path data, not just an equality of counts or connected components.

## Observation and relation boundaries

`no-discrete-retraction` proves there is no Vertex-valued map that sends every realized node back to its original discrete label. The AB path alone would force A=B. The vertex constructors and original source data remain available, but the old reader cannot descend as a retraction. This is not a ban on dependent observations or construction-level provenance.

The finite cellular controls deliberately CHANGE the presentation:

| Presentation | Rational H1 rank |
|---|---:|
| Six independent edges, no faces | 3 |
| Delete BA | 2 |
| Adjoin the forward and ABC face relations | 1 |
| Also adjoin BA = reverse AB | 0 |

The integral chord-coordinate matrix of the three displayed source cycles is the identity. These rank controls expose exactly what erasure or additional relations do; they are **not** formal HIT-equivalence proofs for the modified presentations, and the added relations are not supplied seed facts.

## Verification and durable records

Run:

    python research/strominger/checkers/check_source_graph_free_realization.py

Fresh safe Cubical/guarded Agda closure passed with ignored interfaces and implicit libraries disabled. Three negative controls reject erasing a chord, supplying the ABC face by reflexivity, and defining a discrete endpoint retraction. The controls are compiler regressions; the positive equivalence and obstruction theorems carry the mathematical claims.

The checker records a conservative 2,290-file include-root/primitive manifest and verifies stable inputs. Cubical indexed-match warnings are recorded. The existing `TypedGeneratorLayers.agda` unused import of the unexported `isPropIsContr` is explicitly allowlisted and recorded; this is not a warning-free repository claim. No other-owner source was edited.

- Contract: `contracts/source-graph-free-realization.v1.json`
- Proof: `agda/SourceGraphFreeRealization.agda`
- Receipt: `results/source-graph-free-realization/verification.json`
- Dependency lock: `results/source-graph-free-realization/dependency-manifest.json`
- Connected research net: `wg-source-determination-conjecture-net-v1.md`

## Consequence for effort allocation

The proposed free-realization test is complete; there is no reason to rebuild it or immediately extend a join tower. Under this task, the source gives three circles, not a chosen one. A proposed single-circle reading must identify its additional relation, quotient, boundary collapse or different task and justify that input independently. If a richer filled source is intended, compare its actual retained relations with this frozen free baseline. Native admission and covariance alone do not supply that justification, and no physical interpretation is validated here.
