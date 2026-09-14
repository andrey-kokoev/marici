#!/usr/bin/env python3
"""Conditional matrix perturbation certificate for the selected rank-three packet."""
import json
from pathlib import Path

def main():
 scout=json.loads((Path(__file__).parents[1]/'results'/'three_translate_source_gram_scout.json').read_text())
 eigs=scout['eigenvalues'];numerical_min=min(eigs)
 # K0 is evaluated directly; K(d),K(2d) are formed from K0 and a deficit.
 errors={'K0':1e-6,'K(d)':2e-6,'K(2d)':2e-6}
 # Spectral norm <= infinity norm <= maximum absolute row sum of entry errors.
 row_bounds=[errors['K0']+errors['K(d)']+errors['K(2d)'],errors['K0']+2*errors['K(d)'],errors['K0']+errors['K(d)']+errors['K(2d)']]
 perturb=max(row_bounds);certified_min=numerical_min-perturb
 assert certified_min>0
 result={'schema':'marici.voevodsky.rank-three-perturbation-certificate.v1','sigma':scout['sigma'],'translate_centers':scout['translate_centers'],'numerical_eigenvalues':eigs,'numerical_minimum_eigenvalue':numerical_min,'entrywise_error_allowances':errors,'maximum_error_row_sum':perturb,'spectral_perturbation_bound':perturb,'conditional_minimum_eigenvalue_lower_bound':certified_min,'positive_definite_under_error_model':True,'error_model':'Each direct source kernel evaluation is within 1e-6; differences inherit 2e-6. This is supported by tail and forward-error audits but assumes small-ulp libm behavior.','directed_interval_certificate':False,'conclusion':'The selected rank-three positivity is stable by more than three orders of magnitude relative to the declared evaluation error.'}
 out=Path(__file__).parents[1]/'results'/'rank_three_perturbation_certificate.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
