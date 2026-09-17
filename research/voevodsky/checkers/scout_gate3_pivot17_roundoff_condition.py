#!/usr/bin/env python3
"""Condition number of final Schur pivot with respect to strong-block entry errors."""
import json
from pathlib import Path
src=(Path(__file__).parent/'scout_complex_schur_ellipse_L0649_L065_rho10_64.py').read_text().replace('leggauss(500)','leggauss(1000)');ns={'__file__':str(Path(__file__).parent/'x.py')};exec(src.split('rows=[];Fs=[];Ls=[]')[0],ns);np=ns['np'];block=ns['block'];rows=[]
for j in range(0,128,16):
 th=2*np.pi*j/128;z=.5*(10*np.exp(1j*th)+.1*np.exp(-1j*th));M=block(.6495+.0005*z);F=M[:19,:19];S=F[1:,1:];perm=np.arange(17,-1,-1);T=S[np.ix_(perm,perm)];A=T[:17,:17];b=T[:17,17];c=T[17,:17];x=np.linalg.solve(A,b);y=np.linalg.solve(A.T,c);# dp=(e_last-[A^-1 b;0]) left/right outer product; Frobenius sensitivity product.
 condition=float(np.sqrt(1+np.linalg.norm(y)**2)*np.sqrt(1+np.linalg.norm(x)**2));rows.append({'index':j,'leading17_min_singular':float(np.linalg.svd(A,compute_uv=False)[-1]),'pivot_entrywise_frobenius_condition':condition})
mx=max(x['pivot_entrywise_frobenius_condition'] for x in rows);allow=1e-9;out={'schema':'marici.voevodsky.gate3-pivot17-roundoff-condition.v1','rows':rows,'maximum_condition':mx,'maximum_admissible_strong_block_frobenius_error':allow/mx,'pivot_error_allocation':allow,'passed_scout':mx<1e4,'passed':False,'remaining':'direct floating operation ledger for strong-block Frobenius error','rh_proved':False};root=Path(__file__).parents[1]/'results';p=root/'gate3_pivot17_roundoff_condition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
