#!/usr/bin/env python3
"""Compare Q=140 and Q=180 frequency quadrature with prime-exact Q=1000."""
import json
from pathlib import Path
base=(Path(__file__).parent/'scout_complex_schur_ellipse_L0649_L065_rho10_64.py').read_text().replace('leggauss(500)','leggauss(1000)');prefix=base.split('rows=[];Fs=[];Ls=[]')[0];n0={'__file__':str(Path(__file__).parent/'x.py')};exec(prefix,n0);n1={'__file__':str(Path(__file__).parent/'x.py')};exec(prefix.replace('leggauss(140)','leggauss(180)'),n1);np=n0['np']
def piv(M):
 F=M[:19,:19];T=F[1:,1:][np.ix_(np.arange(17,-1,-1),np.arange(17,-1,-1))].copy();o=[]
 for k in range(18):
  o.append(T[k,k])
  if k<17:T[k+1:,k+1:]-=np.outer(T[k+1:,k],T[k,k+1:])/T[k,k]
 return o
rows=[]
for j in range(0,128,16):
 th=2*np.pi*j/128;z=.5*(10*np.exp(1j*th)+.1*np.exp(-1j*th));L=.6495+.0005*z;a=piv(n0['block'](L));b=piv(n1['block'](L));d=[abs(x-y) for x,y in zip(a,b)];rows.append({'index':j,'maximum_pivot_change':float(max(d)),'pivot17_change':float(d[17])})
out={'schema':'marici.voevodsky.gate3-E10-frequency-quadrature-refinement.v1','frequency_orders':[140,180],'prime_order':1000,'rows':rows,'maximum_change':max(x['maximum_pivot_change'] for x in rows),'maximum_pivot17_change':max(x['pivot17_change'] for x in rows),'passed_scout':max(x['pivot17_change'] for x in rows)<1e-11,'passed':False,'rh_proved':False};root=Path(__file__).parents[1]/'results';p=root/'gate3_E10_frequency_quadrature_refinement.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
