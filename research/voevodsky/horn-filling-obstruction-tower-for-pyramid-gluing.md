# Horn-filling obstruction tower for pyramid gluing

## Question

What local-to-global test remains after certificate domains, overlap comparisons, and loop-probe coverage are all recorded?

## Claim boundary

This packet gives a simplicial obstruction organization for finite overlap nerves. It does not assert that every target sector is an infinity-category or that the displayed mod-two fixture is the physical coefficient system of any Marici sector.

## Skeletal representation data

Let \(N\) be the nerve of the cover by certificate opens. A representation assembled through simplicial degree \(n\) assigns compatible target data to the \(n\)-skeleton:

- degree 0: local sector objects;
- degree 1: comparison arrows on pairwise overlaps;
- degree 2: associator/fusion cells filling triangular boundaries;
- degree 3: pentagon-type compatibility filling tetrahedral boundaries;
- higher degrees: coherence among prior fillers.

At each degree, extension requires filling every admitted horn. Existing boundary data do not imply a filler. This makes global coherence an obstruction tower rather than one terminal Boolean certificate.

## Relation to loop probes

An ordered loop probe evaluates a closed boundary composite. It can detect a residual on a selected boundary, but it does not itself construct the interior filler. Even complete cycle-basis coverage of the 1-skeleton leaves degree-2 and degree-3 horn fillers to be checked.

Kitaev's four-copy Bargmann trace belongs at this boundary-evaluation layer. Its exact scalar value can test one ordered associator loop relative to a prediction. A valid face filler additionally requires a typed comparison cell realizing that boundary. A valid global tetrahedral filler requires compatibility among all face cells.

## Tetrahedral countermodel

Consider a tetrahedral nerve with four triangular faces and mod-two residual labels. Assign residual one to exactly one face and zero to the other three. Every face has a well-defined local residual, and any selected zero face passes its loop test. Nevertheless the total tetrahedral boundary residual is one, so no compatible 3-simplex filler exists in this coefficient model.

This separates:

1. existence of every local face datum;
2. measured values on every face boundary;
3. vanishing of the tetrahedral obstruction;
4. construction and uniqueness class of a filler.

Vanishing is necessary but still may not prove a unique filler; the target can have a nontrivial fiber of fillers.

## Certificate refinement

The partial-representation schema should index coherence certificates by simplicial degree and horn:

- `nerve_simplex_id`;
- `simplicial_degree`;
- `boundary_cells`;
- `boundary_probe`;
- `predicted_residual`;
- `observed_residual`;
- `filler_status`;
- `filler_coordinate_faithfulness`;
- `higher_compatibility_dependencies`;
- `fault_independence_class`.

A global gluing claim requires complete simplex coverage through the claimed truncation degree, fillers for every required horn, and all next-degree compatibility relations. A finite truncation must be labelled as such; it cannot be silently promoted to unbounded coherence.

## Interaction with certificate DAGs

Certificate dependencies now have two independent structures:

- prerequisite reachability in the certificate DAG;
- face relations in the simplicial nerve.

They should not be collapsed into one order. The DAG says when a test or filler is admissible. The nerve says which boundaries that filler must match. Their product indexing explains why one can have all authority and source certificates for a local cell yet fail global coherence, or have a mathematically exact global residual with no physical constructor.

## Disposition

The deepest current overlay is a horn-filling problem indexed simultaneously by certificate state and nerve simplex. Kitaev's loop probe supplies boundary evaluation; the Markov equipment supplies explicit fillers in its analytic subnerve; cross-sector global gluing remains blocked at uncovered or unfilled higher simplices.

## Verification

- `research/voevodsky/checkers/check_horn_filling_obstruction_tower.py`
- `research/voevodsky/results/horn_filling_obstruction_tower.json`
