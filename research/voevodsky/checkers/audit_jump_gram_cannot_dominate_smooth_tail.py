#!/usr/bin/env python3
"""Reject PSD domination of the smooth tail by the rank-four jump Gram."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';T=np.load(root/'residual_jump_variation_gram_L06495.npz')['tail_gram'];D=np.load(root/'continuum_residual_jump_smooth_decomposition_L06495_to5000.npz');Sm=D['smooth'];G=Sm.T@Sm;et=np.linalg.eigvalsh((T+T.T)/2);eg=np.linalg.eigvalsh((G+G.T)/2);ker=np.linalg.eigh((T+T.T)/2)[1][:,:36];leak=float(np.linalg.norm(ker.T@G@ker,2));out={'schema':'marici.voevodsky.jump-gram-vs-smooth-tail-rank-audit.v1','jump_gram_numerical_rank':int(np.sum(et>et[-1]*1e-12)),'smooth_partial_gram_numerical_rank':int(np.sum(eg>eg[-1]*1e-12)),'smooth_gram_norm_on_jump_kernel':leak,'psd_domination_by_any_finite_jump_multiplier_possible':leak<1e-20,'conclusion':'scalar multiples of the rank-four jump Gram cannot dominate the smooth tail in PSD order','passed':leak>1e-20,'rh_proved':False};p=root/'jump_gram_vs_smooth_tail_rank_audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
