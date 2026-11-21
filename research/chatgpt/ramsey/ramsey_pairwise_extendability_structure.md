# Thousands of contradictions compress to a pairwise extendability structure

Define a selected set to be EXTENDABLE if it is contained in at least one valid disjoint coalition of the candidate switches. Extendability is not validity: a partial set can be invalid but capable of completion. Its faces form a simplicial complex.

ramsey_completion_compatibility_complex.py constructs this complex from the exact compiled rule models, then tests for minimal incompatible sets beyond size2. For ALL ten regular candidate systems there are NONE. Once individually unextendable switches are removed, a set has a valid completion iff every pair in it has a common valid completion. Equivalently, the complex is the clique complex of its co-extendability graph (a flag complex).

This is a nontrivial finite compression, not the assertion that pairwise valid operations suffice. An irreducible quintuple has every pair extendable (using the quintuple) although no pair is itself valid.

## Certificates of the exclusions

Across663 candidate switches,597 never occur in any valid coalition.595 of these are refuted by unit propagation from the compiled low-order repair rules. Two exceptions at source182 (candidate indices4,59) need one Boolean case split: whether candidate24 is selected. Both branches unit-refute. Thus no larger branching search is necessary for these two cases.

Among the remaining66 participating switches,234 vertex-disjoint pairs cannot be extended together. ALL234 are refuted by unit propagation. Other incompatible pairs overlap supports and are excluded geometrically. There are no new minimal triple-or-larger extendability obstructions. See ramsey_minimal_completion_refutations.py/JSON for the individual counts and split certificates.

## The main Hall example has only three component shapes

For source191,50 of80 switches are individually unextendable. The remaining30 form a co-extendability graph with40 edges and seven components:
- five isolated triangles (five maximal three-operation completions);
- one five-triangle ring: a five-cycle with a separate extra vertex completing each cycle edge to a triangle (five further maximal three-operation completions);
- one complete graph on five vertices (the irreducible five-operation completion).
Every clique extends to one of these maximal completions. The five-triangle ring is the phase-frustrated branch whose three-way cooperation was previously found; the complete five-vertex component is the synchronized full-orbit transfer. This organizes earlier isolated examples into one finite compatibility structure.

These shapes do not erase differences between valid and extendable subsets. In particular the five-vertex clique represents a completion whose proper nonempty subsets are ALL invalid; the clique records that each partial choice belongs to the same possible full completion.

Limit: co-extendability was initially extracted from the exact finite model set, so this is an explanatory compression with verified exclusion certificates, not yet a geometry-only method for discovering the graph. The next step is to characterize its vertices and edges directly from incidence/phase data, without reconstructing all31 valid models. No claim of a universal flag-complex theorem outside these ten candidate systems is established.
