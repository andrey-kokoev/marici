#!/usr/bin/env python3
"""Partial Legendre derivative-energy Gram for the smooth prime residual."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';G=np.zeros((40,40));rows=[]
for m in range(5,37):
 if m<=7:p=root/f'continuum_residual_jump_smooth_L06495_{m}000_{m}999.npz';key='smooth'
 else:
  p=root/f'gate3_prime_residual_streamed_block_m{m}_extra0.npz'
  if not p.exists():p=root/f'gate3_prime_residual_streamed_block_m{m}.npz'
  key='smooth'
 A=np.load(p)[key];n=np.arange(1000*m,1000*(m+1));G+=A.T@((n*(n+1))[:,None]*A)
 lam=float(np.linalg.eigvalsh((G+G.T)/2)[-1]);rows.append({'through_m':m,'sqrt_energy_gram_norm':lam**.5})
final=rows[-1]['sqrt_energy_gram_norm'];out={'schema':'marici.voevodsky.gate3-smooth-legendre-energy-5000-36999.v1','rows':rows,'partial_sqrt_energy_norm':final,'threshold_for_0p025_over_m':25.,'partial_below_threshold':final<25,'passed':False,'interpretation':'If the complete derivative-energy Gram has sqrt norm <=25, then orthogonality gives every thousand-mode block <=0.025/m. This artifact contains only modes 5000..36999.','rh_proved':False};p=root/'gate3_smooth_legendre_energy_5000_36999.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
