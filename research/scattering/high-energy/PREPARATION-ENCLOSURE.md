# H6 — exact-moment Gaussian preparation enclosure

For each stored energy grid, use exact binary nodes K_i and exact trapezoid weights w_i. Set x_i=(K_i-33/10)/(7/200). The normalized Gaussian family is written in natural parameters

    p_i(alpha,beta)=w_i exp(alpha x_i+beta x_i²)/Z.

The target equations are E[x]=0 and E[x²]=1. They express exact mean 3.30 and exact RMS 0.035, not their rounded binary versions. The Jacobian is the covariance matrix of x and x². With at least three distinct nodes and positive weights it is positive definite, so the log-partition function is strictly convex and has at most one moment-matching parameter pair. The enclosed beta is negative, hence this exponential family corresponds to the intended Gaussian rather than an increasing quadratic profile.

The checker finds an approximate center numerically, then uses Arb to evaluate the exact center residual and Jacobian over a radius-1e-10 parameter box. With a fixed binary inverse approximation C, it verifies

    -C F(center)+(I-C J(box)) (box-center) is strictly inside box-center,
    ||I-C J(box)||_infinity < 1.

These Krawczyk/contractive inclusion conditions prove an exact root exists in the box. They do not assume the numerical center is the root. Interval moment weights and coherent coefficients sqrt(w_i p_i/(2pi)) are then evaluated over the proven box, retaining all uncertainty.

The receipt bounds L1 weight error and L2 coherent-coefficient error against the readout's stored values. These must next be propagated into occupation/current/probability and peak stability. A certificate on this exact-binary grid is not an enclosure of any ideal rational energy grid or exact model's spectral energies; that reference difference remains explicit.

H6 remains open. Three of the six certification cycles are spent; three remain. This step does not certify stationary kernels or renew H7's exhausted budget.

Replay:

    uv run --with numpy --with scipy --with python-flint python research/scattering/high-energy/check_preparation_enclosure.py --check
