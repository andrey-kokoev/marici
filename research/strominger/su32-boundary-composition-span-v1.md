# Boundary composition is an operation, not a self-containing payload

## Implemented object

The new construction is a finite, source-generated operadic envelope for a three-vertex cross-cone tree. Its vertices are:

- C: an upstream `compareAt` operation;
- J: a downstream `channelOperand`, restricted by the previously tested producer-context reference refinement;
- D: a downstream `compareAt` operation.

The complete geometric family has **448 motifs**. Both internal edges use actual shared faces. D is selected by a structural condition: its varying reference is the producer reference. Consequently, its other boundary channel does not silently contain a second copy of that producer reference.

The family is constructed before evaluating local decorations. The five external ports are the two C inputs, J's other reference value, D's other channel input, and D's output.

## The span and its interpretation

The left map restricts a compatible complete decoration to three local operation rows, preserving the two full internal matching points. Gluing those rows reconstructs the complete decoration exactly.

The right map denotes the **composite operation** on the five-port boundary. Its retained description includes the source generators and the sewn internal interfaces. It is not installed as the static content of an external fibre.

This follows the composition-span formulation on p. 2 of Doherty–Hackney, arXiv:2506.15622v2. The present boundary operation lives in a **formal source-generated envelope**. Identifying that envelope's boundary operation with an element of the intended native boundary-corolla fibre remains an obligation. We have not supplied that identification by renaming the output of our adapter.

Existing candidate constructors still produce their original full records. The evaluation tests use those records without changing their representation. This work introduces no new nested-payload adapter, and it does not undo the static finite-JSON obstruction: it stops equating an operation definition or execution witness with static content.

## Two-edge coherence

Let u join C to J and v join J to D. Contracting u then v and contracting v then u produces the same composite operation description. Evaluation of the two corresponding source programs also agrees, including all retained data.

For the two internal edges, the retained-edge poset has four vertices, five strict comparable pairs and two nondegenerate triangles. Its two triangles form the square described by the cubical construction in §7, p. 19 of the paper.

The variance is explicit: adding retained edges refines a presentation; contracting edges goes in the opposite direction. The receipt labels both conventions rather than treating contraction as inclusion.

This reproduces the finite cube shape and tests its source-program comparison. It does not implement the paper's full homotopy-coherent nerve functor or establish all higher fillers of a cyclic infinity operad.

## Cyclic ports and gaps

The implementation retains all eight choices of local cyclic orientation at the three trivalent vertices. These are declared formal planar structures, not a source-selected physical planar embedding. In particular, the registry argument of `channelOperand` does not itself choose a cyclic order.

A ribbon-tree boundary traversal computes five cyclically ordered external legs. Each gap is the pair of consecutive external legs delimiting it. Contraction preserves both the external cyclic order and its gap data. Cyclic rotation transports the gap indexing, and reversing all local orientations reverses the external cyclic order. Root selection determines one outgoing incidence in each component of every partial contraction.

This supplies the combinatorial input for the paper's tree-to-cyclic-gaps discussion on p. 3. It does **not** identify these gaps with our physical contents, establish the cyclic 2-Segal condition, or infer a five-step dynamical period from five boundary ports.

## Verification

Fresh checks pass:

- 14,336 source-program contraction squares;
- 14,336 restriction/gluing round trips;
- 14,336 rejected internal-point mismatches;
- 8 structural contraction squares, one for each formal planar structure;
- 32 boundary/gap-preservation checks across partial contractions;
- 320 component-root lifting checks.

The structural template counts are separate from the source-instance counts. A single local planar reversal changes the boundary cyclic order, so no unnoticed planar quotient is used.

```sh
node research/strominger/checkers/check_su32_boundary_composition_span.mjs
python research/aspect/scc/scc.py check strominger-su32-boundary-composition-span-v1
```

Implementation: `su32-operadic-boundary-span.mjs`.
Contract: `contracts/su32-boundary-composition-span-v1.json`.
Receipt: `results/su32-boundary-composition-span-v1/verification.json`.

The receipt retains all motifs, all eight planar templates, the retained-edge cube, source hashes and one complete compatible decoration alongside its separate composite-operation description. No existing source operator was modified and no proof assistant was run.

## Remaining identification

We now have the finite operation-level span and its first two-edge coherence, rather than another attempted static payload equation. The next required map is from this source-generated operation space to the **native boundary-corolla operation fibre**, respecting generators, contraction and cyclic structure. Separately, the gap structure needs a source-supported content interpretation before it can substantiate the proposed channel–content duality.
