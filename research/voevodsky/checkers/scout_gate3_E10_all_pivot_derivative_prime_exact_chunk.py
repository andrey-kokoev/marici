#!/usr/bin/env python3
"""Five-point direct derivatives for all recursive strong pivots on E10."""
import json,sys
from pathlib import Path
src=(Path(__file__).parent/'scout_complex_schur_ellipse_L0649_L065_rho10_64.py').read_text().replace('leggauss(500)','leggauss(1000)');ns={'__file__':str(Path(__file__).parent/'scout_complex_schur_ellipse_L0649_L065_rho10_64.py')};exec(src.split('rows=[];Fs=[];Ls=[]')[0],ns);np=ns['np'];block=ns['block'];a=int(sys.argv[1]);b=int(sys.argv[2]);h=5e-8
def pivots(L):
 M=block(L);F=M[:19,:19];T=F[1:,1:][np.ix_(np.arange(17,-1,-1),np.arange(17,-1,-1))].copy();out=[]
 for k in range(18):
  out.append(T[k,k])
  if k<17:T[k+1:,k+1:]-=np.outer(T[k+1:,k],T[k,k+1:])/T[k,k]
 return np.array(out)
rows=[]
for j in range(a,b):
 th=2*np.pi*j/128;z=.5*(10*np.exp(1j*th)+.1*np.exp(-1j*th));L=.6495+.0005*z;fm2,fm1,fp1,fp2=[pivots(L+s*h) for s in (-2,-1,1,2)];der=np.abs((fm2-8*fm1+8*fp1-fp2)/(12*h));rows.append({'index':j,'derivative_abs':[float(x) for x in der]})
out={'schema':'marici.voevodsky.gate3-E10-all-pivot-derivative-prime-exact-chunk.v1','range':[a,b],'rows':rows,'passed_scout':True,'passed':False,'rh_proved':False};p=Path(__file__).parents[1]/'results'/f'gate3_E10_all_pivot_derivative_prime_exact_chunk_{a}_{b}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'range':[a,b],'max':max(max(x['derivative_abs']) for x in rows)}))
