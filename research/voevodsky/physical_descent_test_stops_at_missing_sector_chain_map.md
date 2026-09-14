# Physical descent test stops at the missing sector chain map

## Question

Does an existing optics or flavor artifact supply the source-derived chain map required to test the contraction-descent conjecture physically?

## Claim boundary

This is an interface and authority audit. It does not alter sector-owned artifacts or replace the missing constructor with an abstract map.

## Audited optics candidate

The Aspect interferometer contract defines the relative vector

\[
v=(1,1)^T
\]

in the basis \((\Xi_{\log},-\sigma_{123})\), the residue differential, and scalar versus complementary readouts. Its finite-field checker establishes:

- residue closure;
- rank-one dark-port readout;
- rank-two complementary readout;
- algebraic sufficiency of a hypothetical incoming column \((1,1)^T\).

The same contract explicitly marks the required exceptional constructor as not currently constructed. Its result records:

- `simulation_only: true`;
- `exceptional_constructor_source_derived: false`;
- `total_lift_constructed: false`;
- `global_contour_constructed: false`;
- `physical_period_constructed: false`.

A companion scope packet further states that the full specialization mapping-cone differential and its homology have not been constructed.

## First missing typed object

The missing object is a source-derived chain map from either a resolved/Rees exceptional generator or a Cayley--Menger face cone into the logarithmic Čech--de Rham total complex, with image

\[
(\Xi_{\log},-\sigma_{123}).
\]

Its acceptance test is:

1. name source and target chain groups and ordered bases;
2. provide every differential matrix;
3. provide the map on source generators;
4. verify the chain square;
5. assemble the full mapping-cone differential and verify its square is zero;
6. compute cone homology and the descent residual class;
7. provide the source-authorized contour/readout map required for physical interpretation.

## Flavor candidate status

No flavor packet located by the exact chain-map/target-differential search supplies this complete interface. The directed request to `marici.Figueiredo` remains unanswered at this boundary.

## Disposition

Physical testing is blocked at the first missing typed object. The simulation proves classifier adequacy, not a physical contraction obstruction. Constructing an abstract incoming column would violate the source-identity gate and is not an admissible substitute. Reopen only when the exact sector chain map and mapping-cone package materialize.
