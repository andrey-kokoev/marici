#!/usr/bin/env python3
"""Coefficient-decay scout and admissible source remainder target for corrected matrix family."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['coefficients'];n=[float(np.linalg.norm((x+x.T)/2,2)) for x in C];rat=[n[k]/n[k-1] for k in range(9,17)];q=max(rat[-4:]);geometric=n[-1]*q/(1-q);contract=json.loads((root/'source_to_moving_bundle_error_contract_L0649_L065.json').read_text());targets=contract['required_source_error_components'];out={'schema':'marici.voevodsky.corrected-matrix-chebyshev-tail-L0649-L065.v1','coefficient_spectral_norms':n,'ratios_degree9_16':rat,'last_four_ratio_max':q,'conditional_geometric_tail_after16':geometric,'critical_component_target':targets['critical_diagonal_max'],'conditional_tail_to_critical_target':geometric/targets['critical_diagonal_max'],'passed_conditionally':geometric<targets['critical_diagonal_max'],'passed':False,'required_proof':'directed complex-ellipse Cauchy bound or degree-32 source nodes establishing the coefficient majorant','rh_proved':False};p=root/'corrected_matrix_chebyshev_tail_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']
