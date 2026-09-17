#!/usr/bin/env python3
"""Coefficient-triangle E2 bounds for F, B, and the physical residual Gram."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';even=['L0649','L0649010','L0649038','L0649084','L0649146','L0649222','L0649309','L0649402','L06495','L0649598','L0649691','L0649778','L0649854','L0649916','L0649962','L0649990','L065'];odd=['L'+f'{(.6495+.0005*math.cos((32-j)*math.pi/32)):.10f}'.replace('.','') for j in range(1,32,2)];P=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['packet'];Q=np.linalg.qr(P,mode='complete')[0][:,40:];Fs=[];Bs=[]
for k in range(33):
 tag=even[k//2] if k%2==0 else odd[k//2];A=np.load(root/f'gamma_floor_{tag}_rank1000_midpoint.npz')['matrix'];Fs.append(P.T@A@P);Bs.append(P.T@A@Q)
t=np.cos(np.arange(32,-1,-1)*np.pi/32);CF32=np.polynomial.chebyshev.chebfit(t,np.array(Fs).reshape(33,-1),32).reshape(33,40,40);CB32=np.polynomial.chebyshev.chebfit(t,np.array(Bs).reshape(33,-1),32).reshape(33,40,960);CF=CF32[:17];CB=CB32[:17];np.savez_compressed(root/'gate2_source_FB_degree32_L0649_L065.npz',F=CF32,B=CB32);CR=np.load(root/'degree32_residual_gram_family_L0649_L065.npz')['coefficients'][:17];u=2**-53;gam=4000*u/(1-4000*u)
def bounds(C):return [float(np.nextafter(np.linalg.norm(A,2)+gam*np.linalg.norm(A,'fro'),np.inf)) for A in C]
f=bounds(CF);b=bounds(CB);r=bounds(CR);rho=2.;tk=[(rho**k+rho**-k)/2 for k in range(17)];F=sum(x*y for x,y in zip(f,tk));B=sum(x*y for x,y in zip(b,tk));R=sum(x*y for x,y in zip(r,tk));cinv=1/.5341755858170448;alpha=1.067569476012246;total=F+B*B*cinv+R/alpha;allow=6.465313495638705;out={'schema':'marici.voevodsky.gate2-component-coefficient-bounds-L0649-L065.v1','arithmetic_model':'stored binary64 coefficients, spectral norms inflated by gamma_4000 Frobenius allowance and outward nextafter','F_coefficient_upper':f,'B_coefficient_upper':b,'residual_coefficient_upper':r,'E2_F_triangle_bound':F,'E2_B_triangle_bound':B,'E2_residual_triangle_bound':R,'tail_inverse_bound':cinv,'complete_schur_triangle_bound':total,'admissible_source_norm':allow,'passed_stored_coefficients':bool(total<allow),'passed':False,'remaining':'true post-degree16 analytic source remainder','rh_proved':False};p=root/'gate2_component_coefficient_bounds_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_stored_coefficients']
