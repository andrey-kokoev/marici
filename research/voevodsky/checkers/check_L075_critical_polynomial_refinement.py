#!/usr/bin/env python3
"""Q300/Q400 refinement check for the degree-149 critical residual certificate."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:,-1];w=v.copy();w[150:]=0;alpha=.022276778741280565
def calc(name):
 A=np.load(root/name)['total'];J=float(w@A@w);r=A@w;r[:150]=0;rn=float(np.linalg.norm(r));return {'candidate':J,'residual_norm':rn,'lower':J-rn*rn/alpha}
a=calc('gamma_floor_L075_prime4_decomposition.npz');b=calc('gamma_floor_L075_prime4_Q400_decomposition.npz');c=calc('gamma_floor_L075_prime4_Q500_decomposition.npz');out={'schema':'marici.voevodsky.L075-critical-polynomial-refinement.v1','Q300':a,'Q400':b,'Q500':c,'Q300_Q400_differences':{k:abs(a[k]-b[k]) for k in a},'all_positive':a['lower']>0 and b['lower']>0 and c['lower']>0,'status':'floating refinement evidence; directed reduced assembly remains required','passed':False,'rh_proved':False};p=root/'L075_critical_polynomial_refinement.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
