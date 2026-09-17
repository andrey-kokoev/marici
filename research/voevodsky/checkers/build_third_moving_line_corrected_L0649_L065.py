#!/usr/bin/env python3
"""Moving third eigenline for corrected degree-16 slab polynomial."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from numpy.polynomial.chebyshev import chebfit,chebmul
root=Path(__file__).parents[1]/'results';C=np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['coefficients'];t=np.cos(np.arange(32,-1,-1)*np.pi/32);Vv=[];ee=[];prev=None
for x in t:
 H=np.polynomial.chebyshev.chebval(x,C);e,V=np.linalg.eigh((H+H.T)/2);v=V[:,2]
 if prev is not None and v@prev<0:v=-v
 Vv.append(v);ee.append(e[2]);prev=v
P=chebfit(t,np.array(Vv),32);lc=chebfit(t,np.array(ee),32);R=np.zeros((65,40))
for i in range(40):
 for j in range(40):q=chebmul(C[:,i,j],P[:,j]);R[:len(q),i]+=q
 q=chebmul(lc,P[:,i]);R[:len(q),i]-=q
normpoly=np.zeros(65)
for i in range(40):q=chebmul(P[:,i],P[:,i]);normpoly[:len(q)]+=q
normpoly[0]-=1;res=sum(np.linalg.norm(x) for x in R);nd=sum(abs(normpoly));grid=np.linspace(-1,1,4001);mn=min(np.polynomial.chebyshev.chebval(grid,lc));out={'schema':'marici.voevodsky.third-moving-line-corrected-L0649-L065.v1','degree':32,'normalization_defect_bound':float(nd),'eigen_residual_bound':float(res),'minimum_branch':float(mn),'post_degree16_frame_l1':float(sum(np.linalg.norm(x) for x in P[17:])),'passed_scout':bool(nd<1e-10 and res<1e-10 and mn>0),'passed':False,'rh_proved':False};np.savez_compressed(root/'third_moving_line_corrected_L0649_L065.npz',frame=P,eigenvalue=lc,residual=R,normalization_defect=normpoly);p=root/'third_moving_line_corrected_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
