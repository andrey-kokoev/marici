# Path operations connect the comparison incidence graph, not yet the charges

## Fresh source and obligation

Forward realization, before an energy readout. The shared-state comparison
hypothesis supplies composable four-state paths with retained positive traversal
resource, and source/target maps of directed arrows. The prior symmetry and
Gauss-completion checkers are freshly rerun. The present test asks what those
operations do to the finite labelled comparison domain, without inventing29
bridge links between symmetry orbits.

## Typed operations

For a slot (outer,inner), an active arrow (i,j) can be followed by (j,k), k!=j.
The active last-arrow label changes; the full path must append the new edge,
not discard its previous history. Apply this independently to the outer arrow
and the two inner arrows when the inner slot is an arrow pair.

For an inner arrow pair (a,b), the source-pair and target-pair are state-pair
readouts. Retain such a link in the153-slot domain only if both readout states
are nonreference states. Otherwise it lies outside the proposed nine-state
block and is not silently added. In a physical readout, retain the parent
arrow/path in a record: the endpoint alone cannot reconstruct it.

These are operations of the declared path/endpoint calculus. They do not supply
Hamiltonian coupling coefficients or license replacing a readout by an inverse.

## Connectivity result

Starting from the generous rooted-relabelling envelope:

| Operations admitted | Undirected components |
|---|---:|
| Rooted relabellings only |30|
| Also outer path continuation |10|
| Also left inner continuation |4|
| Also right inner continuation |2|
| Also endpoint readout incidence |1|

The path/readout links alone, without relabelling links, already form a connected
UNDIRECTED graph on1836 vertices and15174 edges. No arbitrary component bridges
are needed at this incidence level.

Direction matters. In the same graph with operation directions retained there
are TEN strongly connected components: one1728-vertex arrow block and nine
12-vertex state blocks. Endpoint readout goes from arrows to states; no reverse
operation is supplied. Hence the result is weak incidence connectivity, not a
reversible physical coupling or a strongly connected dynamical sector.

## Retained-history obstruction

The path (0,1) and its extension (0,1,0,1) have the same last arrow but different
histories and resource. The continuation cycle

    (0,1) -> (1,0) -> (0,1)

costs two traversals. A scalar potential on active-arrow labels cannot increment
by one at each step: summing its differences round this cycle gives0, not2.
This does NOT say traversal work is impossible. It says history, a clock, an
external work reservoir or another retained port is needed to account for it.
Work per traversal must not silently become a rest-energy potential on the
finite slot graph.

## Conservation is not channel locking

Let B be the oriented vertex-edge incidence matrix of the undirected graph.
The earlier proposed locking law was

    B^T n = 0

for charges assigned to VERTICES. Connectivity makes n constant. Ordinary
Kirchhoff current conservation instead says

    B j = 0

for currents assigned to EDGES. These are different objects and different laws.
The latter has cycle rank15174-1836+1=13339. An exact three-edge circulation
through outer arrows (0,1),(1,2),(2,0), at one fixed state-comparison slot, obeys
current conservation while occupying only three edges. It does not require all
1836 channels to carry a unit charge.

Thus connectivity and current conservation do not derive the compact-rotor
locking constraint. Declaring every incidence to impose n_s=n_t would reinsert
the missing physical law, even though the links now have typed source names.
The energy-normalization obstructions from the earlier audits also remain.

## Verification and remaining physical constructor

    python research/nima/checkers/check_mass_path_port_connectivity.py
    python research/aspect/scc/scc.py check nima-mass-path-port-connectivity

The finite graph construction, directed reachability, cycle witness and path
resource contradiction use exact arithmetic. Report:
`results/mass-path-port-connectivity.json`.

Progress: there is an explicit, non-arbitrary incidence route between the two
comparison types. Remaining: lift it to a history-retaining physical interaction
with a DERIVED charge-locking constraint, rather than a lossy endpoint projection
or mere current conservation. Its charging form and particle identification
must still be sourced. No mass ratio or decimal correction has been fitted.
