"""Independent query proofs and source lifts; no projection producer import."""
from pathlib import Path
from fractions import Fraction as Q
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 packets=json.loads((OUT/'lazy-envelope-state.json').read_text())['packets'];assert len(packets)==6
 proofs=lifts=0
 for (n,refined),p in zip([(n,r) for n in (2,4,8) for r in (False,True)],packets):
  assert (p['n'],p['refined'])==(n,refined)
  rows=[]
  for j,b in enumerate((1,1,4,4)):
   for s in (-1,1):rows.append((tuple(Q(s if k==j else 0) for k in range(4)),Q(b)))
  for i in range(n):
   a=Q(2*i+1-n,n);rows.extend([((2*a,Q(0),Q(-1),Q(0)),a*a),((Q(0),2*a,Q(1),Q(-1)),a*a)])
  if refined:rows.append(((Q(0),Q(0),Q(0),Q(1)),Q(1)))
  assert p['base_rows']==[[list(map(str,a)),str(b)] for a,b in rows]
  assert len(p['cases'])==5
  for c in p['cases']:
   point=tuple(map(Q,c['point']));keep=(0,1,3) if c['stage']==1 else (1,3)
   assert len(point)==len(keep)
   # Independent analytic membership of these y=0 / x=0 controls.
   z=point[-1];expected=z>=-Q(2,n*n) and (not refined or z<=1)
   assert ('lift' in c)==expected
   if 'cut' in c:
    cut=c['cut'];a=tuple(map(Q,cut['a']));b=Q(cut['b']);w=cut['weights']
    assert len({i for i,v in w})==len(w) and all(type(i) is int and 0<=i<len(rows) and Q(v)>=0 for i,v in w)
    full=[sum(Q(v)*rows[i][0][k] for i,v in w) for k in range(4)]
    assert tuple(full[k] for k in keep)==a and all(full[k]==0 for k in range(4) if k not in keep)
    assert sum(Q(v)*rows[i][1] for i,v in w)==b and dot(a,point)>b;proofs+=1
   else:
    x=tuple(map(Q,c['lift']));assert len(x)==4 and tuple(x[k] for k in keep)==point
    assert all(dot(a,x)<=b for a,b in rows)
    # Independent inverse of owning (U,V,t0,t1) at the admitted local box.
    center=[Q(50),Q(51),Q(52),Q(53)];r=[Q(1,128**j) for j in range(4)];delta=Q(1,128**4)
    U=sum(center)+delta*x[0];V=dot(center,r)+delta*x[1]
    t0=center[0]+delta*x[2];t1=center[1]+delta*x[3]
    u=U-t0-t1;v=V-t0-r[1]*t1
    t2=(v-r[3]*u)/(r[2]-r[3]);t3=u-t2;t=(t0,t1,t2,t3)
    assert all(0<=v<=100+2*j for j,v in enumerate(t)) and sum(t)==U and dot(t,r)==V;lifts+=1
 result={'passed':True,'cases':30,'separating_proofs':proofs,'owning_source_lifts':lifts,
 'scope':'One/two-stage envelope membership, separation, appended public refinement. No optimization backend or controlled arbitrary-depth complexity claim.'}
 (OUT/'lazy-envelope-state-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
