#!/usr/bin/env python3
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';A=np.load(root/'gate3_prime_residual_streamed_block_m12.npz')['smooth'];B=np.load(root/'gate3_prime_residual_streamed_block_m12_extra64.npz')['smooth'];e=float(np.linalg.norm(A-B,2));b=float(np.linalg.norm(B,2));out={'schema':'marici.voevodsky.gate3-gauss-overintegration-stability.v1','m':12,'base_nodes':7001,'overintegrated_nodes':7065,'matrix_difference_operator_norm':e,'relative_difference':e/b,'scaled_difference':12*e,'target_reserve':.02-12*b,'reserve_to_difference_factor':(.02-12*b)/(12*e),'passed_stability_scout':12*b+12*e<.02,'passed':False,'note':'independent-node floating stability check, not a directed roundoff proof','rh_proved':False};p=root/'gate3_gauss_overintegration_stability.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_stability_scout']
