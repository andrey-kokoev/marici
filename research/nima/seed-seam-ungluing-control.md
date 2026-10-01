# Ungluing control: generic coefficient algebra versus seam-selected reference

## Controlled intervention

Keep the original ordered occurrence contexts

    left:  (AB,BC,CA), right: (BA,AD,DB).

Preserve all six occurrence IDs, both cyclic orders, coefficient inputs, and fixed occurrence-addressed readers. Change only endpoint identities: replace each vertex by its context-tagged copy (left,A), (right,A), and so on. Four shared-graph vertices become six vertices in two disjoint directed triangles.

The checker uses the actual packet endpoint fields, not the spelling of the occurrence IDs, after this intervention. In particular, retained labels AB and BA no longer denote reciprocal arrows between the SAME vertex identities.

This is a counterfactual control on the declared representation, not a physically executed graph surgery.

## Result: the response algebra does not depend on cross-context gluing

Both fixtures yield exactly the same:

- local cyclic matrices and all nine mode-pair projectors;
- componentwise product-category endpoint-composition mask;
- relative-rotation projection D;
- six-plus-three coefficient split under the same tracked role exchange W;
- length-graded coefficient product and its symmetric/residual update;
- nonzero residual-residual correction and its off-diagonal support;
- numerical response under unchanged occurrence-addressed readers.

The reason is structural. Product-category matching compares each component's target with that SAME component's next source. It never compares a vertex identity in the left triangle with one in the right. Splitting their shared vertices therefore does not change that matching relation.

The test also composes actual packet endpoints and histories for both fixtures. Labelled primitive words remain identical, but the stored endpoint assignments differ. This does not identify the complete source packets or discard the intervention's provenance.

The residual correction remains an exact and useful change-of-coordinates law. Its survival after ungluing means it does not establish a seam-generated interaction, force or binding effect. This conclusion concerns THIS algebra; it is not a no-go theorem for every possible source-derived response.

## What the seam actually contributes here

The source-derived reciprocal cross-context pair count changes from one to zero. Before the intervention, the unique pair is {AB,BA}. Afterwards the reference-extraction query has no answer.

The code rejects that query as unavailable. It does not insert a zero reference response or designate a replacement pair. An externally held reader may still address the labels AB and BA, but after ungluing it is no longer reading a source-extracted reciprocal seam.

The directed graph's vertex-automorphism count grows from 2 to 18. The role-aligned triangle exchange used in P=(I+W)/2 remains one symmetry of the unglued graph, but is no longer its unique nonidentity automorphism. Holding that comparison fixed is a matched-control convention, not evidence that the unglued graph independently selects it.

Thus the seam genuinely supplies a distinguished address and restricts symmetry. It does not enter the current coefficient multiplication as an interaction-generating dependency.

## Synthesis boundary

The recovered programme now separates three layers:

1. **Local occurrence algebra:** spectral modes, graded products and exact six-plus-three updates exist for the two declared cycle contexts even when disconnected.
2. **Shared source structure:** gluing identifies a reciprocal reference and reduces symmetry.
3. **Operational binding:** a source-justified rule making that shared reference affect preparation, composition, admission or response is still not supplied by this coefficient algebra.

Do not tune a coefficient after observing this result or rename the existing AA correction as coupling. The algebra is a reusable conditional representation and retention mechanism. Its source-specific explanatory content currently lies in reference selection, not demonstrated seam-dependent dynamics.

## Verification

    python research/nima/checkers/check_seed_seam_ungluing.py

Fresh exact checks pass for both endpoint fixtures, all 243 basis-pair/length-residue products, 49 complex path-length combinations, spectral equality, the nonzero AA hostile, retained ordered words, changed endpoints, reciprocal-reference rejection and exhaustive automorphism counts.

Report: `results/seed-seam-ungluing.json`.
