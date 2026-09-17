#!/usr/bin/env python3
"""Five-point direct derivative scout for E10 pivot17."""
import json,sys
from pathlib import Path
# Load definitions without executing the contour loop.
src=(Path(__file__).parent/'scout_complex_schur_ellipse_L0649_L065_rho10_64.py').read_text();ns={'__file__':str(Path(__file__).parent/'scout_complex_schur_ellipse_L0649_L065_rho10_64.py')};exec(src.split('rows=[];Fs=[];Ls=[]')[0],ns);np=ns['np'];block=ns['block'];a=int(sys.argv[1]);b=int(sys.argv[2]);h=float(sys.argv[3]) if len(sys.argv)>3 else 1e-7
def pivot(L):
 M=block(L);F=M[:19,:19];T=F[1:,1:][np.ix_(np.arange(17,-1,-1),np.arange(17,-1,-1))].copy()
 for k in range(17):T[k+1:,k+1:]-=np.outer(T[k+1:,k],T[k,k+1:])/T[k,k]
 return T[17,17]
rows=[]
for j in range(a,b):
 th=2*np.pi*j/128;z=.5*(10*np.exp(1j*th)+.1*np.exp(-1j*th));L=.6495+.0005*z;fm2,fm1,fp1,fp2=[pivot(L+s*h) for s in (-2,-1,1,2)];der=(fm2-8*fm1+8*fp1-fp2)/(12*h);rows.append({'index':j,'derivative_abs':float(abs(der)),'step':h})
out={'schema':'marici.voevodsky.gate3-E10-pivot17-derivative-chunk.v1','range':[a,b],'rows':rows,'maximum':max(x['derivative_abs'] for x in rows),'passed_scout':max(x['derivative_abs'] for x in rows)<.02,'passed':False,'rh_proved':False};p=Path(__file__).parents[1]/'results'/f'gate3_E10_pivot17_derivative_chunk_{a}_{b}_h{h:.0e}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
