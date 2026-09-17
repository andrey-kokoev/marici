#!/usr/bin/env python3
"""Refine source quadrature at eight E10 nodes and compare recursive pivots."""
import json
from pathlib import Path
src=(Path(__file__).parent/'scout_complex_schur_ellipse_L0649_L065_rho10_64.py').read_text().replace('leggauss(500)','leggauss(1000)');ns={'__file__':str(Path(__file__).parent/'scout_complex_schur_ellipse_L0649_L065_rho10_64.py')};exec(src.split('rows=[];Fs=[];Ls=[]')[0],ns);np=ns['np'];block=ns['block'];root=Path(__file__).parents[1]/'results';base=json.loads((root/'complex_schur_ellipse_L0649_L065_rho10_scout128.json').read_text())['samples'];by={round(x['theta'],12):x for x in base}
def pivots(M):
 F=M[:19,:19];T=F[1:,1:][np.ix_(np.arange(17,-1,-1),np.arange(17,-1,-1))].copy();o=[]
 for k in range(18):
  o.append(T[k,k])
  if k<17:T[k+1:,k+1:]-=np.outer(T[k+1:,k],T[k,k+1:])/T[k,k]
 return o
rows=[]
for j in range(0,128,16):
 th=2*np.pi*j/128;z=.5*(10*np.exp(1j*th)+.1*np.exp(-1j*th));q=pivots(block(.6495+.0005*z));x=by[round(float(th),12)];old=[complex(x['strong_ldl_pivot_real'][k],x['strong_ldl_pivot_imag'][k]) for k in range(18)];diff=[abs(a-b) for a,b in zip(q,old)];rows.append({'index':j,'maximum_pivot_change':float(max(diff)),'pivot17_change':float(diff[17])})
out={'schema':'marici.voevodsky.gate3-E10-source-quadrature-prime-exact-refinement.v1','base_orders':[140,500],'refined_orders':[140,1000],'rows':rows,'maximum_change':max(x['maximum_pivot_change'] for x in rows),'maximum_pivot17_change':max(x['pivot17_change'] for x in rows),'target_per_evaluation_error':1e-11,'passed_scout':max(x['maximum_pivot_change'] for x in rows)<1e-11,'passed':False,'rh_proved':False};p=root/'gate3_E10_source_prime_exact_refinement.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
