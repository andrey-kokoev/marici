"""Owning scalar fiber over a public segment; exact affine compatibility."""
from fractions import Fraction as Q
from itertools import product,combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
# An affine function is slope*p+intercept.
histories={'A':([(Q(0),Q(0))],[(Q(0),Q(1,2))]),
 'B':([(Q(1,4),Q(-1,4))],[(Q(0),Q(3,4))]),
 'C':([(Q(1,2),Q(-1,2))],[(Q(0),Q(1))]),
 'D':([(Q(1,2),Q(0))],[(Q(0),Q(1))])}
def val(f,p):return f[0]*p+f[1]
def fiber(names,p):
 lower=[Q(0)];upper=[Q(1)]
 for name in names:
  ls,us=histories[name];lower.extend(val(f,p) for f in ls);upper.extend(val(f,p) for f in us)
 return max(lower),min(upper)
def source(p,h):return (p-h/128,1+129*h/128,1-h)
def observe(x):return sum(x),sum(v*Q(1,128**j) for j,v in enumerate(x))
def main():
 certificates=[]
 for name,(low,high) in histories.items():
  for p in (Q(1),Q(2)):assert fiber([name],p)[0]<=fiber([name],p)[1]
 lows=[(Q(0),Q(0))]+[f for n in 'ABC' for f in histories[n][0]]
 highs=[(Q(0),Q(1))]+[f for n in 'ABC' for f in histories[n][1]]
 for l,u in product(lows,highs):
  gaps=[val(u,p)-val(l,p) for p in (Q(1),Q(2))];assert min(gaps)>=0
  certificates.append({'lower':list(map(str,l)),'upper':list(map(str,u)),'vertex_slacks':list(map(str,gaps))})
 samples=[]
 for p in (Q(1),Q(5,4),Q(3,2),Q(7,4),Q(2)):
  lo,hi=fiber('ABC',p);assert lo==(p-1)/2 and hi==Q(1,2)
  h=(lo+hi)/2;assert h==p/4;x=source(p,h)
  assert all(0<=v<=100+2*j for j,v in enumerate(x))
  assert observe(x)==(p+2,p+Q(1,128)+Q(1,16384))
  for name in 'ABC':a,b=fiber([name],p);assert a<=h<=b
  samples.append({'p':str(p),'common_interval':[str(lo),str(hi)],'h':str(h),'source':list(map(str,x))})
 assert fiber('ABC',Q(2))==(Q(1,2),Q(1,2))
 assert fiber('AD',Q(1))==(Q(1,2),Q(1,2)) and fiber('AD',Q(2))[0]>fiber('AD',Q(2))[1]
 graph=[]
 for a,b in combinations(histories,2):
  witnesses=[p for p in (Q(1),Q(2)) if fiber([a,b],p)[0]>fiber([a,b],p)[1]]
  if witnesses:graph.append({'pair':[a,b],'public_parameter':str(witnesses[0])})
 assert any(e['pair']==['A','D'] for e in graph)
 assert all(not set(e['pair'])<=set('ABC') for e in graph)
 # Fine relations pairwise differ: endpoint fiber bounds suffice here.
 for a,b in combinations(histories,2):assert any(fiber([a],p)!=fiber([b],p) for p in (Q(1),Q(2)))
 report={'passed':True,'public_domain':'1<=p<=2','compatibility_certificates':certificates,
 'common_section':'h=p/4 for A,B,C','source_controls':samples,'incompatibility_graph':graph,
 'minimal_initial_state_counts':{'public_answers':1,'common_lifting':2,'fine_reexposure':4},
 'scope':'Vertex certificates establish all-domain compatibility for finite affine scalar bounds. No independent packet verifier or general coloring solver.'}
 (OUT/'common-lifting-domain.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ('passed','common_section','incompatibility_graph','minimal_initial_state_counts')},indent=2))
if __name__=='__main__':main()
