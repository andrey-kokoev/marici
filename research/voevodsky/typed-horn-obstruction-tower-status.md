# Typed horn-obstruction tower status

## Question

At which dimensions are Markov, cross-sector, and mixed horn obstructions currently defined or filled?

## Claim boundary

This status object tracks typeability and realized fillers. It is distinct from the finite tetrahedral residual checker, which demonstrates that complete face data can carry a nonzero obstruction.

## Markov tower

On the metric-transition Markov domain:

- dimension 0 vertices are realized;
- dimension 1 incidence maps are realized;
- dimension 2 comparison cells are filled;
- dimension 3 associativity and compatibility fillers are realized;
- dimension 4 coherence is filled for the six declared cell classes and five declared law classes.

No unbounded higher-coherence claim follows.

## Cross-sector tower

The sector nerve has one admitted vertex and no admitted edge. Its first obstruction dimension is therefore 1: the boundary of the first edge is incomplete because no candidate supplies a common typed object, two source-derived incidence maps, and a comparison cell.

Dimensions 2 through 4 are undefined, not failed and not zero. Their horn boundaries do not yet exist.

## Mixed tower

Mixed horns compare certificate strengthening with sector gluing. Since no sector edge exists, no mixed horn boundary can be formed. The mixed tower is undefined at its first nondegenerate stage.

## Complementary finite witness

The pre-existing checker `check_horn_filling_obstruction_tower.py` verifies the distinct higher-dimensional phenomenon: all four triangular faces of a tetrahedron may be present while a mod-two residual obstructs the 3-filler. It also verifies that vanishing obstruction does not imply filler uniqueness and that one passing loop does not establish tetrahedral coherence.

## Disposition

The Markov internal tower is filled through the declared presentation laws. The cross-sector programme is stopped at edge construction, before any genuine cross-sector triangle or tetrahedral obstruction class can be evaluated.

## Verification

- `research/voevodsky/horn-filling-obstruction-tower-v1.json`
- `research/voevodsky/checkers/check_typed_horn_obstruction_tower_status.py`
- `research/voevodsky/results/typed_horn_obstruction_tower_status.json`
- `research/voevodsky/checkers/check_horn_filling_obstruction_tower.py`
