# Calibration-dependent source witnesses close the thin-data certificate gap

## Deliverable

The reusable solver and independent verifier now support version-2 certificates with the restricted source policy

`x_i(E)=d_i/E_i`,

where each d_i is an exact rational constant. They admit no arbitrary executable expression or nonlinear calibration program.

The quantifier is explicit:

`for every allowed calibration E, there exists a source x(E)`.

This is NOT the version-1 statement that one fixed vector fits every calibration. Universal target conclusions still require the independently checked dual bound; a favorable source policy alone does not prove a target for every compatible source.

## 1. Certificate checks

The problem format remains `positive-diagonal-real-l1-v1`. Version 2 changes the certificate evidence, not the acquisition model. It declares

`witness_semantics: for-every-calibration-there-exists-source`,

and a witness with kind `inverse-calibration` and a rational numerator vector d.

For data intervals [l_i,u_i], positive calibration intervals [e_i,f_i], weights w_i and budget B, the standalone verifier checks:

1. l_i<=d_i<=u_i. Then E_i x_i(E)=d_i is identically within the raw data interval.
2. sum_i w_i |d_i|/e_i<=B. This bounds the policy's cost for every calibration in the entire enclosure.
3. Where a witness target range is needed, it encloses sum_i t_i d_i/E_i by summing the minimum and maximum of each endpoint expression. This accounts for negative numerators and target coefficients.

These whole-box statements remain sufficient when the actual calibration is correlated: every actual parameter point is inside the certified box. They do not exploit correlations to obtain a sharper result.

Version-1 fixed-vector certificates remain accepted. The solver tries the existing fixed-witness path first and uses version 2 only as a fallback. `solve_fixed` retains the original behavior for regression and scope comparisons.

## 2. Keep existence, universal conclusions and ambiguity distinct

For TARGET_TRUE and TARGET_FALSE, the policy establishes nonempty feasibility for the actual calibration, whichever allowed value it has. The original dual certificate independently proves the target conclusion over ALL compatible sources in the outer model. A policy whose own target value is favorable is not substituted for that proof.

For AMBIGUOUS, two policies are required. The false policy's entire target range must be at most the threshold, and the true policy's entire range must be strictly above it. Consequently at every allowed calibration the SAME calibration admits two conflicting sources. This does not merely compare one favorable source at one calibration with another source at a different calibration.

The verifier rejects a changed witness quantifier, an unsupported formula, a version-2 witness presented as version 1, out-of-data numerators, budget violations and invalid universal dual bounds.

## 3. The original thin-data obstruction is resolved

Take

`data=[1,1]`, `E in [2-delta,2+delta]`, `|x|<=1`, target `x>0`,

with 0<delta<=1/2. No fixed x fits both calibration endpoints. Version 1 therefore remains unresolved.

Version 2 uses d=1 and x(E)=1/E. Its cost is at most 1/(2-delta)<1, and the independent universal bound is x>=1/(2+delta)>0. It certifies TARGET_TRUE at every such nonzero enclosure width, without waiting for the calibration interval to collapse to a point.

For the actual physical calibration E this formula specifies an actual source. It does not claim that the true source changes when a numerical enclosure is refined, or that its numerical coefficients have been exactly acquired.

## 4. A useful completeness fact, and remaining limits

For an independent Cartesian calibration box, this policy family is sufficient to certify uniform feasibility whenever uniform feasibility holds. Choose d_i to be the point of [l_i,u_i] closest to zero. The minimum source cost at any fixed E is sum_i w_i|d_i|/E_i. Its maximum over the box occurs at E_i=e_i. Thus

`for every E there is a feasible source
 iff sum_i w_i|d_i|/e_i<=B`.

The solver uses precisely this lowest-cost numerator policy to establish existence. This does not prove completeness for all interval-calibration task classifications. Universal target bounds may be conservative for correlated calibrations, and the current small policy search for opposing target signs need not find every possible calibration-dependent pair. Some problems are feasible only for part of the calibration box. UNRESOLVED remains a legitimate output.

Nor does this extend the model to general observation matrices, complex coefficients, uncertain target coefficients or arbitrary nonlinear source policies.

## 5. Verification and regressions

New tests:

`python research/nima/checkers/check_parametric_witness_certificates.py`

They resolve 180 generated problems that the fixed-witness solver leaves unresolved: 60 TARGET_TRUE, 60 TARGET_FALSE and 60 AMBIGUOUS. All certificates pass the separate verifier. An additional 1090 explicit calibration-corner evaluations check the source formulas, budget and target signs. All 722 deliberately invalid certificates are rejected, including attempts to replace a universal conclusion by one favorable policy or to check cost only at a favorable endpoint.

Existing suites were rerun:

`python research/nima/checkers/check_diagonal_certificate_engine.py`

`python research/nima/checkers/check_certificate_acquisition_planner.py`

The original 400 generated cases now have 10 unresolved outcomes instead of 19; all 300 exact-calibration vertex-oracle comparisons still pass. The 29 physical fixture outcomes and the acquisition branch guarantees are unchanged. Source/calibration evidence remains an external input to the exact-rational verifier.

The earlier thin-data checker now explicitly tests version-1 failure and version-2 success, rather than leaving an obsolete failure assertion against the upgraded solver.

Artifacts:

- `research/nima/results/parametric-witness-certificates.json`
- `research/nima/results/parametric-witness-summary.json`

## Meaning for the lane

This closes a demonstrated certificate-schema gap without weakening the meaning of an acquired reading or a source budget. The output now distinguishes a common fixed source from a calibration-indexed source policy, and neither is confused with a universal task statement.

No intrinsic source-module boundary, filtered attachment class or source-comparison map is inferred from these numerical certificates.
