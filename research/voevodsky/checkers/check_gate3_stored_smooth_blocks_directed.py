#!/usr/bin/env python3
"""Directed operation ledger for stored smooth residual blocks.

This certifies the binary64 matrices themselves; source/formula enclosure remains separate.
"""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';S=np.load(root/'continuum_residual_jump_smooth_decomposition_L06495_to5000.npz')['smooth'];u=2**-53;rows=[]
for q in range(4):
 A=S[q*1000:(q+1)*1000];G=A.T@A;G=(G+G.T)/2
 # Dot-product rounding, symmetrization, and symmetric eigensolver backward error.
 gam=1000*u/(1-1000*u);dot=gam*np.linalg.norm(np.abs(A).T@np.abs(A),2);eigerr=(80*u/(1-80*u))*np.linalg.norm(G,'fro');lam=float(np.linalg.eigvalsh(G)[-1]);up=float(np.nextafter(math.sqrt(max(0,lam+dot+eigerr)),math.inf));m=q+1
 rows.append({'m':m,'mode_range':[1000*m,1000*(m+1)-1],'lambda_float':lam,'dot_error_bound':dot,'eigensolver_error_bound':eigerr,'operator_norm_upper':up,'m_times_upper':m*up,'target_0p015_over_m':.015/m,'passes_target':bool(m>=2 and up<.015/m)})
out={'schema':'marici.voevodsky.gate3-stored-smooth-blocks-directed.v1','rows':rows,'later_stored_blocks_pass':all(x['passes_target'] for x in rows[1:]),'scope':'directed binary64 operation ledger for the stored smooth matrices, not enclosure of their generating physical integrals','passed':False,'next_obligation':'port the combined Legendre-antiderivative source formula to Arb and enclose source-to-stored-matrix error','rh_proved':False};p=root/'gate3_stored_smooth_blocks_directed.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['later_stored_blocks_pass']
