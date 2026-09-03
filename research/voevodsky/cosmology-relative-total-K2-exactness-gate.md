# Relative total K2 exactness correction

## Correction

The former nonexactness proof projected `(Xi_log,-sigma123)` to `H^2(U)` and treated `Xi_log` as if the projection were a chain map. That is not valid for a comparison cone: the cone differential can include the map carrying the boundary/flag representative to the logarithmic representative.

The verified statements are narrower:

- `{u,v}` is nonzero in motivic/de Rham degree two;
- its full tame boundary is the divisor-unit tuple `(v^-1,u,-v/u)`;
- secondary oriented flags recover the primitive triangle cycle;
- `{u,v}` is not itself a degree-one precycle.

Whether `(Xi_log,-sigma123)` is exact depends on the actual total complex, its shifts, and an explicit chain-level comparison from the flag resolution to the logarithmic complex. If that comparison is a quasi-isomorphism, its mapping cone is acyclic and a comparison homotopy can exist even though `Xi_log` is nonzero in `H^2(U)`. If `sigma123` is only an associated-graded representative, extension data may obstruct such a lift.

## Disposition

The claimed nonexactness of the pair is withdrawn. The result JSON and former checker are superseded. The next gate defines the comparison cone before any exactness claim.
