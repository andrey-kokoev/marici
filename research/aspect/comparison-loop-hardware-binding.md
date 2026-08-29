# Comparison-loop hardware binding

The two mesh programs contain 108 tunable rotations in total. A telescoping product bound makes the route-operator error no larger than the sum of absolute rotation-angle errors. The two-route fringe error is bounded by the sum of the two route errors.

The frozen systematic rotation budget is 0.01, giving a per-rotation bound of 0.01/108, approximately 9.26e-5 radians when enforced uniformly. Terminal phase and differential loss each receive 0.003. Statistical quadrature error receives 0.02. Total fringe uncertainty is at most 0.036.

The compiled reference fringes span about 0.22578. Even a two-sided 0.072 uncertainty band cannot erase that probe dependence. Thus the source-dependent route mismatch remains resolvable under the frozen hardware budget.

The emitted binding template has one record per tunable rotation. Hardware identity, control channels, measured angles, losses, timestamps, and calibration authority are deliberately null until a physical controller binds them. A synthetic target packet is provided only to test ingestion.

