"""Independent replay of fixed-support failures and adaptive successes."""
import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results';k=(1,-6,15,-20,15,-6,1)
cyclic=[(i,i+1) for i in range(6)]+[(0,6)]
def line(x,y,p):
 i,j=p;return x[i]*y[j]-x[j]*y[i],k[i]*y[j]-k[j]*y[i],x[i]*k[j]-x[j]*k[i]
def coeff(L,P,T):
 c,a,b=L;p,d,e=P;q,f,g=T;det=d*g-e*f
 if det==0:return None
 A=(a*g-b*f)/det;B=(d*b-e*a)/det;G=c-A*p-B*q
 assert all(L[z]==A*P[z]+B*T[z]+(G if z==0 else 0) for z in range(3))
 return A,B,G
def main():
 rows=json.loads((N/'seven-point-farkas-support-chambers.json').read_text())['rows'];assert len(rows)==2
 result=[]
 for row in rows:
  src=row['counterexample'];assert src
  neg=src['negative_initial_columns'];w=list(map(Q,src['weights']));t=list(map(Q,src['slopes']))
  x=[(-w[i] if i<neg else w[i]) for i in range(7)];y=[x[i]*t[i] for i in range(7)]
  assert all(line(x,y,p)[0]>0 for p in combinations(range(7),2))
  target=tuple(z-1 for z in row['target_minor']);P,T=[tuple(z-1 for z in p) for p in row['fixed_support']]
  bad=coeff(line(x,y,target),line(x,y,P),line(x,y,T));assert bad is None or min(bad)<0
  good=next((p,q,c) for p,q in combinations(cyclic,2) if (c:=coeff(line(x,y,target),line(x,y,p),line(x,y,q))) is not None and min(c)>=0)
  result.append({'target':row['target_minor'],'fixed_coefficients':None if bad is None else list(map(str,bad)),
   'adaptive_support':[[z+1 for z in p] for p in good[:2]],'adaptive_coefficients':list(map(str,good[2]))})
 output={'passed':True,'cases':result,'scope':'Two exact admitted targets refute two previously stable fixed supports while accepting alternative sparse certificates.'}
 (N/'seven-point-farkas-support-chambers-verification.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
if __name__=='__main__':main()
