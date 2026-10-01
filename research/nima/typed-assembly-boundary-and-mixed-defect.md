# Typed assembly boundary and the mixed comparison defect

## Use the actual assembly inputs

The existing137-slot assembly has maps

    x_i:A->U, y_j:U->B       (11 of each),
    s_a:A->V, t_b:V->B       (4 of each),
    d:A->B                  (retained direct reference).

Its121 arrow composites and16 state composites are paths sharing these legs.
The boundary adapter therefore starts with four endpoint objects and31
primitive/reference legs, rather than treating every composite as a new
independent primitive arrow.

For each counted slot retain a reference-comparison2-cell with additive path
boundary

    partial sigma_ij = x_i+y_j-d,
    partial sigma_ab = s_a+t_b-d.

These boundaries are closed because each path and d have the same endpoints.
This is the additive chain shadow of the typed path construction; finite matrix
composition is evaluated separately as y_j*x_i or t_b*s_a.

## Exact chain dimensions

The31-leg incidence boundary has rank3. The137 reference-comparison boundaries
have rank28, filling every cycle of the connected leg graph. Their kernel has
dimension109:

    137 - 28 = (11-1)^2 + (4-1)^2 = 100+9.

A complete kernel basis consists of rooted rectangles

    sigma_ij - sigma_i0 - sigma_0j + sigma_00

in each block. Every basis vector has its own unit interior-slot coordinate,
so independence is explicit.

The137 composites can also be retained as named1-cells p_s, with composition
witnesses tau_s satisfying partial tau_s=path_s-p_s. Together with the137
reference cells partial sigma_s=p_s-d, the expanded complex has168 1-cells,
274 2-cells and boundary rank165. Its2-kernel is again109-dimensional.
An exact chain retraction sends p_s to its retained path, tau_s to zero and
sigma_s to the path-reference cell; the inverse sends a path-reference cell
to tau_s+sigma_s. Thus retaining composite names preserves the result.

Forgetting shared legs instead leaves138 parallel primitive arrows (137
composites plus d) and137 independent comparison boundaries. That simplification
has no2-kernel. The109 relations come from retained composition provenance.

## What those closed relations actually read

The matrix response of a reference cell is

    R_ij=y_j*x_i-d.

Its rectangle response is exactly

    R_ij-R_i0-R_0j+R_00 = (y_j-y_0)*(x_i-x_0).

The state block obeys the same formula with t and s. Reference changes cancel
from every rectangle. Perturbing only one leg family also gives zero. Simultaneous
perturbations generally give a nonzero second-order response.

The checker takes x_1=I+(2/3)H and y_1=I+(3/5)K, with H=E12 and K=E21, obtaining
(2/5)KH, which is nonzero. The multiplication order is retained; matrices are
not assumed commutative. Averaging all137 cell responses recovers the existing
assembly residual exactly.

At the unit baseline, the transpose of the additive boundary matrix is the
scalar first-order response map delta R_ij=delta x_i+delta y_j-delta d.
The109 rectangles annihilate this first-order map. Their exact finite responses
are the bilinear terms above. This explains both the earlier rank28 response
calculation and the next retained defect data using the actual input legs.

## Implication for the filler adapter

A closed path boundary can carry a nonzero finite matrix response. Declaring
all109 rectangles to be zero-valued higher coherence cells would discard that
mixed response. A response-compatible higher filler must expose a boundary or
action whose readout matches (delta right)*(delta left), with its support on the
four participating slots.

This typed assembly complex is distinct from the earlier primitive-family
biclique complex with1152 rectangle cells and1459 degree3 filler directions.
Those counts cannot be transferred by identifying every occurrence of the word
'comparison'. A chain/response adapter between the constructions must preserve
path sharing, endpoints and these mixed defects.

The next concrete successor datum is now derived:100 arrow-block and9 state-
block rectangle defects, carrying factored matrix responses. They are109 labelled
relations, not109 freely independent matrix parameters. Their next-level record
and filler rule must preserve the factorization and actual response.

## Verification

    python research/nima/checkers/check_typed_assembly_boundary_adapter.py

Exact leg/path boundaries, ranks28 and165, expanded/reduced chain retraction,
all109 kernel generators, reference-cone control, bilinear response identity,
single-leg and reference-change controls, and recovery of the existing normalized
137-slot assembly. All arithmetic is rational. The file imports and reruns the
original typed assembly checker.
