# Fourth-order theta quadrature removes the mass-box bottleneck

## Result

The completed-theta windows now use degree-three Taylor integration with a rigorous fourth-derivative remainder. This replaces the old whole-cell range sums without changing the detector, source observations, prior, 272-dimensional projection, or integration cutoff.

With 1024 cells instead of 262144, the mass-enclosure widths improve by approximately:

- A1: 131236 times;
- B1: 62291 times.

The positive-gain interval narrows by about 5.0684 times, to approximately

    [6.280225597046373, 6.280678506004204] * 1e-193.

Both frozen middle cases remain UNRESOLVED. Their normalized costs are approximately

    necessary lower cost: 39.99866351238511,
    robust witness cost:  40.00154231347434,
    budget:               40.

The previous mass-only Cartesian obstruction is removed. Exact rational endpoint tests now identify the retained C_bin interval as the remaining obstruction to this decision method. No physical ambiguity or actual acquisition is asserted.

## 1. Certified integration, not sampled agreement

On a cell of width d and midpoint c, Taylor's theorem gives

    integral f = d*f(c) + d^3*f''(c)/24 + R,
    |R| <= d^5*sup_cell|f^(4)|/1920.

Odd Taylor terms integrate to zero. Arb series coefficients are derivatives divided by factorials. Hence the implementation uses

    d*series_mid[0] + d^3*series_mid[2]/12,
    remainder radius <= d^5*sup_cell|series_cell[4]|/80.

The fourth coefficient is evaluated with the ENTIRE cell as the series constant term. This encloses the fourth derivative at every real point in the cell; a midpoint derivative alone would not justify the remainder.

Both the mass density and the centered-moment density are treated this way. They are analytic compositions of exponential, logarithmic and rational functions on t>=pi*A^2>0. Hyperbolic functions are expressed through exponentials for the series API. Denominators stay positive. Interval arithmetic encloses all parameter and arithmetic errors as well as the derivative bounds.

The reported `quadrature_remainder_bounds` are enclosures of computed upper-bound expressions, not measurements of the actual integration error.

## 2. The theta completion and integration tail remain bounded

Use the same normalized variable and scale as the owning calculation:

    t0=pi*A^2, t=t0+v, x=(log(t/pi))/2,
    D=t0*A^(7/2), X=D*exp(-t0)*integral(density).

The n=1,2 theta atoms are integrated by the Taylor rule. For n>=3, the first majorizing atom is

    4*t^2*81*exp(-8*t0-9*v).

Successive majorants have ratio at most

    (4/3)^4*exp(-7*t) < 1.

Each cell therefore retains a positive geometric-series bound for every omitted atom. Its contribution to the centered moment is multiplied by an interval enclosure of x*tanh(3x)-log(A); it is not silently dropped.

The cutoff remains V=32. The existing all-atom density bound

    density(v) <= 2*(1+v)^3*exp(-v)/(1-16*exp(-3*t0))

gives the retained tail bound

    2*exp(-V)*(V^3+6*V^2+15*V+16)/(1-16*exp(-3*t0)).

On the actual finite window, the centered weight has absolute value at most log(A)+log(A*p), supplying its tail bound. Extending the mass majorant to infinity only enlarges the bound. The true upper integration limit exceeds V for both windows.

After enclosing the mass I and centered moment J, the code computes

    mu=log(A)+J/I,

with a verified positive denominator. No tiny X amplitude is divided out during the normalized integration.

## 3. What now prevents resolution

The gain remains

    E(C)=2 X_A X_B (C+H(mu_A-L))(C+H(mu_B-L)).

All old projection quantities H, C and L are retained. Let E_max(C_low) use the most favorable remaining interval endpoints, and E_min(C_high) the least favorable ones. Exact rational arithmetic verifies

    E_max(C_low) < threshold < E_min(C_high).

Thus the two ends of the current C interval force opposite decisions even after accounting for all the new mass and moment uncertainty. This is no longer the earlier situation where the mass boxes straddled the threshold at every fixed C.

The critical C value is enclosed using

    alpha=H*(mu_A-L), beta=H*(mu_B-L),
    C_critical=-(alpha+beta)/2
               +sqrt(((alpha-beta)/2)^2 + threshold/(2*X_A*X_B)).

Its approximate enclosure is

    [1.972185405022678, 1.9721854136734076].

The checker independently verifies the direction of this bracket by substituting its endpoints into the exact rational extreme-gain formulas.

The next useful pairing certificate would place C wholly below the lower critical endpoint, or wholly above the upper critical endpoint. The former is sufficient for prior incompatibility; the latter supports the nonvacuous feasible branch. Merely promising a narrower C interval does not guarantee resolution near equality. The projection center is not an established value of the true C.

## 4. Tests and retained evidence

The suite includes:

- positive and negative polynomial integrands of degrees zero through four;
- exactness of the remainder formula on cubics and its necessary size on quartics;
- an independent analytic exponential integral;
- a fresh 2048-cell replay of both windows;
- strict nesting inside the old window and gain enclosures;
- exact threshold binding to each frozen middle task;
- unchanged detector, data, prior and projection bindings;
- preservation of earlier feasible/infeasible and task-positive certificates;
- ten extended portable chains, all verified in isolated execution.

Mesh overlap is a regression check, not the proof of integration accuracy. The proof is the whole-cell fourth-derivative enclosure plus the omitted-atom and integration-tail bounds. The portable task verifier checks exact source-task obligations; it does not independently prove those analytical enclosures.

## Reproduction

Fresh quadrature, calibration and task replay:

    uv run --with python-flint python research/grothendieck/checkers/certify_theta_mass_refinement.py

Quadrature regressions, exact bottleneck diagnosis and portable export:

    uv run --with python-flint python research/grothendieck/checkers/check_theta_mass_refinement.py

Standalone task-chain verification:

    python research/grothendieck/certificates/verify_source_task_transition.py research/grothendieck/results/portable-source-task-transitions/private-middle_threshold-theta-taylor.json

Implementation:

- `research/grothendieck/checkers/refine_theta_mass_quadrature.py`
- `research/grothendieck/checkers/certify_theta_mass_refinement.py`
- `research/grothendieck/checkers/check_theta_mass_refinement.py`

Artifacts:

- `research/grothendieck/results/theta-mass-refinement.json`
- `research/grothendieck/results/theta-mass-refinement-tests.json`
- `research/grothendieck/results/three-channel-source-task-calibration-theta-taylor.json`
- `research/grothendieck/results/portable-source-task-transitions/*-theta-taylor.json`

The failed projection-only conjecture remains recorded in its original artifact. This follow-up changes the integration proof, not that experiment's outcome or its frozen inputs.
