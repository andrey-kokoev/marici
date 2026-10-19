# Calibration-aware optical binding: interval risk theorem

## Fixed scope

Conditional coherent/Gamma statistical successor, two equal-frequency signals, fresh vacuum ports and retained outcome history. Calibration parameters and prior context are supplied independently with interval bounds. The theorem does not prove that a real apparatus meets those bounds, justify the prior, or bound photon-count noise.

## Propagating calibration through information and state

Let unknown efficiency, tap fraction and current surviving preparation factor lie in positive boxes. For each mode, pre-tap count exposure c=eta*tau*f satisfies `c∈[eta_lo*tau_lo*f_lo, eta_hi*tau_hi*f_hi]`. Given recorded counts, posterior shape K is known and posterior rate is initial rate plus summed exposures. Surviving factor updates to `(1−tau)f`; gain updates to q²f or q⁴f. Interval products therefore propagate both physical attenuation and information rate. They may overapproximate correlated parameters, but do not understate their range.

For every fixed calibration choice in the supplied box, conjugate Gamma formulas still apply, PROVIDED gain/tap calibration is a fixed shared parameter independent of initial preparation under the stated prior model. Conditional on that calibration and the recorded history, means and variances obey

`m_i ∈ [f_lo*K/r_hi, f_hi*K/r_lo]`,

`v_i <= f_hi²*K/r_lo²`.

If calibration is itself uncertain with a posterior distribution supported on the box, the uniform conditional bound below integrates to the same risk bound. This does not presume that a nominal rate equals the mixed posterior or erase calibration/preparation correlations outside the stipulated model.

## Bias plus uncertainty certificate

For a commanded gain whose ACTUAL amplitude lies in [q_lo,q_hi], final expected occupation lies in

`mu_lo=q_lo²*m1_lo+q_lo⁴*m2_lo`,

`mu_hi=q_hi²*m1_hi+q_hi⁴*m2_hi`.

Final conditional variance is bounded by `V=q_hi⁴*v1_hi+q_hi⁸*v2_hi`. For requested target h and absolute tolerance epsilon, define `B=max(|mu_lo−h|,|mu_hi−h|)`. If B<epsilon, then for EVERY supplied calibration context,

`P(|Hfinal−h|>=epsilon | transcript,calibration) <= min(1,V/(epsilon−B)²)`.

This follows from the triangle inequality and Chebyshev about the TRUE conditional mean. It explicitly accounts for systematic bias. If B>=epsilon or the bound exceeds requested delta, abstain; do not silently substitute a nominal exact target certificate. There may be sharper successful policies, but failure of this sufficient test is not proof of their impossibility.

## Prospective declared fixtures

Concentrated posterior shapes 100000 for each mode, rates within 0.1% of 100000 and factors exactly 1. Command nominal q=1/2, giving nominal h=5/16. Require epsilon=h/4 and delta=1/20. Actual gain interval [0.499,0.501] certifies the conditional risk bound; the predeclared wider interval [0.4,0.6] abstains. These are THEORETICAL input bounds and preparation fixtures, not measured device tolerances or a free upgrade of the low-count specimen's prior.

Independent evidence first needed: calibrated gain and detector-efficiency coverage over the operating regime, preparation/prior evidence, fresh-vacuum and frequency control. Physical pulse time, routing, detector resetting, environmental disposal and controller cost remain separately unquantified. A mathematical interval certificate does not install those operations.

## Execution and disposition

`python research/sontag/checkers/optical_calibration_bounds_v1.py`

Seven exact rational checks pass: tight regime certifies, wide regime abstains, bias is nonzero, corner moments are enclosed, exposure bounds include efficiency/tap factors, survival interval is ordered and zero posterior-rate bounds are rejected. Monotonic interval formulas establish all-box coverage analytically; corners are corroborating tests, not the proof.

Result: `results/optical-calibration-bounds-v1.json`.

Constructed at conditional interval-theorem strength: error propagation into the decision certificate and an explicit first missing empirical evidence package. This satisfies the owner-local calibration-aware node's declared construction task, not empirical calibration itself. The final assembly must label the result conditional and retain the physical evidence gaps.
