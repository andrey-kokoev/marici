# Ne-20: a ribbon surface with a Morse handle decomposition

## Question and claim boundary

Construct a smooth orientable surface with boundary whose spine is the application's authored Ne-20 graph. The source is the actual incidence table, not a planar union of drawn strokes. This is a **forward realization** obligation in SCC terminology: graph plus an explicit rotation convention to a surface. No route-coherence or physical-readout claim is made.

The application uses the current diagram, including browser edits. The bundled incidence has 12 vertices and 26 edges; edge 5 is retired. The five non-junction crossings (12/27, 7/23, 6/24, 17/25, 22/26) do not create vertices. Colored edits and arrow reversals do not change this incidence or its local geometric rotation.

## Construction

1. For every vertex take an oriented disk. For every edge take an oriented rectangular band. Each edge has two distinct half-edges, identified by its edge ID and `from`/`to` endpoint.
2. Order the attachment intervals clockwise around each disk using the first nonzero outgoing segment of each edge's authored polyline, in the diagram's y-down coordinate system. Signs and cross products use exact integer arithmetic after clearing positive rational denominators. Screen coordinates and arrow directions do not enter this order.
3. Glue the two short sides of each band to the corresponding disk intervals, reversing induced boundary orientations. This specifies an orientable, untwisted ribbon surface. Distinct rays are required: coincident outgoing tangents or completely collapsed edges are rejected, not resolved by an arbitrary edge-ID tie-break.
4. Round corners. Retract the disks onto stars meeting at their centers and the bands onto their core intervals. These retractions agree at attachments, so the surface deformation-retracts onto the original graph.

Let alpha exchange the two half-edges of each edge, and let sigma take the next clockwise half-edge at a vertex. The cycles of sigma composed with alpha are the boundary circles. An isolated vertex contributes one disk boundary despite having no half-edges. Connected components are computed from incidence, not coordinates.

For a connected component with V vertices, E edges and b boundary cycles,

\[
\chi=V-E=2-2g-b,\qquad \beta_1=E-V+1=2g+b-1.
\]

Changing the rotation system can change the surface type without changing graph incidence. This construction does **not** compute the minimum embedding genus of the abstract graph.

## Morse function

Sort vertex and edge IDs in code-point lexicographic order. Give vertex i (starting at zero) the minimum level

\[
a_i=\frac{i+1}{V+1},
\]

and edge j the saddle level

\[
c_j=1+\frac{j+1}{E+1}.
\]

Thus every minimum lies between 0 and 1, every saddle between 1 and 2, and critical values are distinct. Use local Morse charts

\[
f=a_i+x^2+y^2,\qquad f=c_j-x^2+y^2.
\]

Build the sublevel surfaces by the disks followed by the specified bands in this level order. Unused attachment intervals remain on the current boundary. Regular product collars join the handle charts with f equal to the collar coordinate. Extend the final collars to boundary level 3; the outward derivative is positive there. This realizes the specified handle decomposition by a smooth Morse function, without interior maxima. These are construction levels, not physical time, height in the existing SVG, or nuclear energy.

The implementation supplies the exact attaching permutations and critical-level data; it does not generate a numerical smooth atlas, gradient metric, triangulation, or rendered 3D mesh. The local-chart/handle argument is the mathematical realization, not a claim that an arbitrary interpolation of plotted values is Morse.

## Uncontracted Ne-20 surface

For the authored clockwise rotation:

- one connected component;
- genus 5 and six boundary circles;
- boundary half-edge cycle lengths 12, 8, 8, 8, 8, 8;
- Euler characteristic -14 and first Betti number 15;
- twelve minima, twenty-six saddles, and no interior maxima.

The counts agree independently:

\[
12-26=-14=2-2(5)-6,\qquad 15=2(5)+6-1.
\]

An independent exact checker also constructs a **different** rotation system on the same incidence graph with genus 0 and sixteen boundary circles. It reverses the upper-left and upper-right rotations and routes the four outer chords through explicitly listed corner rotations. Thus this graph is abstractly planar; genus 5 belongs to the authored clockwise attachment convention, not to incidence alone. A proposed shortcut reversing four tip rotations and the lower block at the top junction was rejected: it still gives six boundaries and genus 5. Both the failed shortcut and the valid planar witness are retained in `research/strominger/checkers/check_ne20_morse_surface.py`.

These critical-point counts preserve one disk per vertex and one band per edge; they are not asserted to be minimal. Capping the six boundary circles would instead produce a closed genus-five surface and require six additional 2-handles/maxima. The capped surface would no longer deformation-retract onto this graph, so capping is not performed.

## Ten-minimum decomposition (default Ne-20 view)

The Morse view now contracts edges 8 and 9 **in the handle presentation only**. The source graph, colored arrows, click phases and saved versions are not changed. The three disks at upper-left, upper-tip and upper-right, together with those two joining bands, form a disk. Replace that patch by one disk, keeping every remaining attachment interval in its inherited cyclic order.

For an edge with endpoint half-edges a and b, write the two endpoint rotations as `(a, A)` and `(b, B)`. Remove a and b, merge the endpoint disks and use cyclic order `(A, B)`. Do not re-sort ports using the original coordinates after merging. Each contraction must join distinct current disks; missing/repeated edges and cycles in the requested contraction set are rejected.

The resulting presentation has ten disks and twenty-four bands: **10 minima, 24 saddles, no interior maxima**. Its genus remains 5, it still has six boundary circles, and its Euler characteristic and first Betti number remain -14 and 15. Boundary words are the original words with the four cancelled half-edges removed; their lengths are 10, 8, 6, 8, 8, 8.

Edge 12 becomes a loop at the merged disk. Edges 10, 11 and 27 remain three distinct parallel bands between it and top-junction. Dropping these connections or reordering their attachments would be a different operation. Each remaining minimum records its original `sourceVertices`; the merged disk uses upper-right as its representative ID, not as a new physical vertex location.

Assign fresh distinct critical levels using the same formulas with V=10 and E=24. This realizes the cancelled handle decomposition; it is not a numerical animation of a previously generated smooth function. Ten is a chosen critical-point count, not an intrinsic invariant of the surface. In particular, the original convention of one minimum per original graph vertex no longer applies.

The independent checker verifies contraction through a different description: restrict the original boundary permutation by skipping the four removed ports, then recover the required new rotations by composing with alpha. It also checks source-vertex provenance, the surviving loop and parallel bands, and the revised critical levels. Lost reduced ports and lost provenance must fail validation.

## Colored arrows and risky tests

The conjecture tested here is that the declared ribbon construction preserves incidence, yields valid orientable surface invariants, and is independent of color/arrow edits. Rivals are accidental merging at crossings, a planar-union interpretation, or using colored-arrow direction as the disk rotation.

The checker tests boundary half-edge coverage and pairing, exact rational-coordinate invariance, global reflection, recoloring and arrow reversal, plus tree, circle, isolated-vertex and disconnected controls. Deliberate collapsed-edge and coincident-tangent inputs must fail. A directed triangular cycle must be reported as an obstruction to any strictly descending scalar assignment along its arrows.

The bundled arrow assignment has no directed cycle; the live UI checks the current edited assignment separately. Absence of a cycle is only a necessary consistency check for interpreting arrows as descent. In **this** handle construction both endpoint vertices are minima and an edge carries an intervening saddle, so the whole original edge is not a single downhill trajectory even if its arrow graph is acyclic. The app's colored routing is not a gradient flow, Reeb graph, or Morse–Smale complex by declaration.

## Disposition and verification

Implemented as a read-only **Morse** dialog, with component invariants, critical levels, attachment orders and boundary cycles derived from the active document. Ne-20 defaults to the ten-minimum presentation; other diagrams retain the uncontracted construction. The domain API still supports both. No diagram, named version, route, camera state or browser storage is changed by the construction.

The TypeScript checker writes `research/strominger/results/ne20-morse-surface.json`, including the source document, construction and source/constructor hashes. From the repository root, `python research/strominger/checkers/check_ne20_morse_surface.py` independently reconstructs rotations and boundary permutations with rational arithmetic, checks the receipt's source freshness, rejects tampered genus/rotation/boundary data, and verifies the alternative planar rotation. SCC registers this bounded forward-realization check in `research/strominger/scc-models/ne20-morse-surface.json`; compiler success is not a physical-readout certificate.

Sources: `src/schemas/morse-surface.ts`, `src/domain/morse-surface.ts`, `src/vue/MorseSurface.vue`. Run `pnpm check:morse-surface` for the construction tests, and the existing native-browser suite for dialog integration.
