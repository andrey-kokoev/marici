#!/usr/bin/env python3
"""Test whether termwise triangle summation of higher derivative jumps can close the tail."""
import json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];v[1::2]=0;L=.75;n=np.arange(150);scale=np.sqrt((2*n+1)/(2*L));der=[]
for m in range(7):
 vals=np.zeros(150)
 for k in range(m,150):vals[k]=math.prod(range(k-m+1,k+m+1))/(2**m*math.factorial(m)) if m else 1
 der.append(float(np.dot(v*scale,vals)))
ratios=[abs(der[m+1]/der[m])/1000 if der[m] else None for m in range(6)];out={'schema':'marici.voevodsky.L075-derivative-jump-hierarchy-viability.v1','endpoint_derivatives_orders_0_6':der,'successive_derivative_over_N_ratios_at_N1000':ratios,'third_jump_directed_bound':1.9542690570196358e-10,'remaining_triangle_reserve':2.521150533421369e-10,'termwise_triangle_route_viable':False,'reason':'higher endpoint derivatives initially grow faster than each added 1/N integration factor; separate triangle bounds discard essential cancellation among derivative orders','required_route':'sum the complete finite boundary-jet expansion coefficientwise before taking the l2 norm','passed':True,'rh_proved':False};p=root/'L075_derivative_jump_hierarchy_viability.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
