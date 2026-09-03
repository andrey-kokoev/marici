from __future__ import annotations
import json

def main():
    threshold=1/130
    lam25=.03156750089329365; lam26=.005327308700984034
    projection_gap=min(lam25-threshold,threshold-lam26)
    observed_margin=.0044690002992322925
    target_margin=.001
    error_budget=observed_margin-target_margin
    range_residual=4.96817810148134e-8
    range_correction=40*range_residual**2
    spatial_delta=abs(.0044690002992322925-.004464963317598018)
    assert projection_gap>0 and range_correction<1e-12 and spatial_delta<1e-5
    result={"schema":"marici.voevodsky.cutoff-250-certificate-budget-check.v1",
      "status":"quantitative_interval_certificate_target_defined",
      "projection_threshold":threshold,"projection_gap":projection_gap,
      "observed_tight_tolerance_margin":observed_margin,"target_certified_margin":target_margin,
      "total_operator_error_budget":error_budget,"range_residual":range_residual,
      "range_residual_correction_upper":range_correction,
      "empirical_fixed_cutoff_spatial_delta":spatial_delta,
      "quadrature_error_certified":False,"projection_error_certified":False,
      "continuum_positivity_verified":False,"rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
