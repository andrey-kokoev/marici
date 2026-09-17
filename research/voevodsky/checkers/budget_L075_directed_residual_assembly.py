#!/usr/bin/env python3
"""Conservative directed-assembly budget for the L=.75 critical residual."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];v[1::2]=0;vn=float(np.linalg.norm(v));observed=7.59387617969497e-9;# L=.75-adjusted conservative unit-panel entry budget, then row-sum spectral bound.
entry=3.0e-13;dimension=1000;operator=dimension*entry;node=1e-12;error=vn*(operator+node);upper=observed+error;t=json.loads((root/'L075_residual_norm_tolerance.json').read_text());maximum=t['maximum_residual_norm_for_positivity'];out={'schema':'marici.voevodsky.L075-directed-residual-assembly-budget.v1','critical_vector_norm':vn,'unit_panel_entry_remainder_budget':entry,'dimension':dimension,'operator_remainder_budget':operator,'node_operator_budget':node,'residual_norm_error_budget':error,'observed_residual_norm':observed,'certifiable_residual_upper_target':upper,'maximum_residual_for_positivity':maximum,'reserve_after_budget':maximum-upper,'scope':'budget for prospective Arb unit-panel residual assembly','passed':upper<maximum,'rh_proved':False};p=root/'L075_directed_residual_assembly_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
