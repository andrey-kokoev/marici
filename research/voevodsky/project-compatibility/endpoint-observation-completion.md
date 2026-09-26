# A source-generated endpoint observation and its topology boundary

## Problem and scope

The previous exact hostile control gave residues2 and1 depending on whether integration preceded formal residue. Identify the missing observation from the integrand itself, rather than declaring interchange or adding a fitted correction.

This note concerns that explicit interval model, not the cosmological triangle. Rational identities are machine checked. The measure convergence arguments below are written proofs, not Agda formalizations or source-owner physical identifications.

## Derive the extra observation

For E>0 and0≤y≤1,

    f_E(y)=1/E + 1/(E+y)^2,
    E f_E(y)dy = dy + k_E(y)dy,
    k_E(y)=E/(E+y)^2.

Exact primitive and mass formulas are

    integral_0^delta k_E dy = delta/(E+delta),
    integral_0^1 k_E dy = 1/(1+E),
    integral_delta^1 k_E dy = E/(E+delta)-E/(E+1).

For0<E≤1, half the layer mass lies on[0,E]. Those sets have Lebesgue measure tending to zero, so the family is not uniformly integrable. This explicitly identifies the failure in the naive interchange argument.

The blow-up y=Et gives k_E(y)dy=dt/(1+t)^2 on[0,1/E]. Its limiting mass is1. This derives the boundary coefficient from the source kernel; it is not fitted to the observed discrepancy.

## Exact observation limit on continuous tests

Let phi be continuous on[0,1], M=||phi||_infinity and omega_phi(delta) its modulus of continuity. Splitting at delta gives

    |integral phi k_E dy - phi(0)|
      ≤ omega_phi(delta) + 2M E/(E+delta) + M E/(1+E).

Proof: subtract phi(0) inside the integral. On[0,delta] the difference is bounded by omega_phi(delta), and total layer mass is at most1. On[delta,1] it is bounded by2M; use the exact tail mass and discard its negative term. The remaining mass deficit contributes at most M E/(1+E).

First make delta small, then E small. Hence k_E dy converges weak-star, as finite measures tested on C([0,1]), to delta_0. Therefore

    lim_{E down to0} E integral phi(y) f_E(y)dy
      = integral phi(y)dy + phi(0).

The missing test is endpoint evaluation. With phi=1 the repaired reading is2, exactly recovering the previous residue mismatch.

For arbitrary continuous phi this is a scaled boundary limit, NOT a claim that its complex-parameter period is meromorphic or has an ordinary Laurent residue. For the constant test the earlier rational period does have that residue.

## Quantitative test class and a stronger-topology obstruction

For ||phi||_infinity≤M and Lipschitz constant≤L, the estimate is uniform with omega_phi(delta)≤L delta. Taking delta=sqrt(E), for E≤1, gives error at most

    (L+2M)sqrt(E) + M E.

The checker evaluates the sharper rational bound at E=1/n^2, delta=1/n, M=L=1. These samples validate arithmetic, not the universal analytic argument by enumeration.

There is NO total-variation norm convergence: k_E dy and delta_0 are mutually singular positive measures, so

    ||k_E dy - delta_0||_TV = 1/(1+E)+1 →2.

Here total variation denotes the full signed-measure variation norm. The same obstruction holds for the difference between dy+k_Edy and dy+delta_0, since the common Lebesgue term cancels.

Thus a uniform bound on a regularity-restricted test class can coexist with complete failure of convergence uniform over all bounded continuous tests. The completion/test topology matters; it cannot be replaced by a scalar identity or pointwise finite success.

## Structural synthesis and physical admission gate

The model supplies a concrete construction–observation compatibility repair:

- retaining only the interior pointwise limit gives the wrong observable;
- retaining the source-derived endpoint measure restores all fixed continuous-test limits;
- the repaired pairing is stable in weak-star or bounded-Lipschitz testing, but not total variation.

This is a diagnostic candidate mechanism, not permission to impose weak-star measure topology on the physical triangle. The actual twist may be signed, complex, multivalued or distributional, and its chain/domain may vary.

For the triangle, a source-authorized trivialization must first identify the actual pulled-back normalized forms on an appropriate common domain, while retaining kappa0, K^gamma, the regulator and endpoint data. Then test whether the boundary contribution vanishes under a proved uniform-integrability/dominating hypothesis or survives as an explicitly derived boundary/nearby-cycle object. Uniform integrability is a sufficient route in the applicable finite-measure setting with convergence in measure, not a necessary characterization of every complex twisted-period problem.

No physical E0 specialization or completion norm is supplied here. Existing Benincasa/Nima handoff remains active. Local next step is to audit the triangle's full source normalization and degeneration before borrowing this repair.

## Verification

`python research/voevodsky/project-compatibility/check_period_residue_boundary.py` passes exact polynomial identities for the primitive, masses, blow-up kernel, half-mass concentration and original positive/negative controls, plus exact rational bound samples. `period-residue-boundary.json` binds the checker and inspected source snapshots; all inventoried bytes stayed unchanged during the run.
