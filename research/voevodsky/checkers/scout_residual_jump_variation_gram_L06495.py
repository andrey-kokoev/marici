#!/usr/bin/env python3
"""Jump component of the weighted variation Gram for the L=.6495 regularized residual."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');U=d['packet'];D=d['tail_maps'][4];Z=U-D;L=.6495;N=1000;n=np.arange(N);sc=np.sqrt((2*n+1)/(2*L));fplus=np.array([legval(1,Z[:,j]*sc) for j in range(40)]);fminus=np.array([legval(-1,Z[:,j]*sc) for j in range(40)]);atoms=[]
for p in (2,3):
 a=math.log(p);c=math.log(p)/math.sqrt(p);# h(t)=g(Lt), jump locations t=(+-L -/+ a)/L
 for t,row in (((L-a)/L,.5*c*fplus),((-L+a)/L,-.5*c*fminus)):
  w=(1-t*t)**(-.25);atoms.append((w,row))
A=sum(w*np.linalg.norm(r) for w,r in atoms);B=np.zeros((40,40))
for w,r in atoms:
 nr=np.linalg.norm(r)
 if nr:B+=w*np.outer(r,r)/nr
G=A*B;factor=4*L/(math.pi*(4000-1));tail=factor*G;alpha=1.067569476012246;S=d['schur'][4];lower=S-tail/alpha;lower=(lower+lower.T)/2;out={'schema':'marici.voevodsky.residual-jump-variation-gram-L06495.v1','jump_atoms':len(atoms),'weighted_total_variation':float(A),'variation_gram_norm':float(np.linalg.norm(G,2)),'mode4000_jump_tail_gram_norm':float(np.linalg.norm(tail,2)),'range_compatible_min_after_jump_tail':float(np.linalg.eigvalsh(lower)[0]),'uncorrected_min':float(np.linalg.eigvalsh(S)[0]),'status':'floating jump component only; smooth derivative variation not included','passed_jump_component':float(np.linalg.eigvalsh(lower)[0])>0,'passed':False,'rh_proved':False};p=root/'residual_jump_variation_gram_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'residual_jump_variation_gram_L06495.npz',variation_gram=G,tail_gram=tail);print(json.dumps(out,indent=2));assert out['passed_jump_component']
