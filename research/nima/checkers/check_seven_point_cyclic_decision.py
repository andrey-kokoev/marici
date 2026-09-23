"""Complete exact decision for a fixed rational seven-point cyclic fibre."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results'
K=tuple((-1)**i*comb(6,i) for i in range(7));EDGES=[(i,i+1) for i in range(6)]+[(0,6)];PAIRS=list(combinations(range(7),2))
def affine(x,y,p):
 i,j=p;return (x[i]*y[j]-x[j]*y[i], K[i]*y[j]-K[j]*y[i],x[i]*K[j]-x[j]*K[i])
def value(L,z):return L[0]+L[1]*z[0]+L[2]*z[1]
def intersection(L,T):
 c,a,b=L;d,e,f=T;det=a*f-b*e
 if not det:return None
 return ((b*d-c*f)/det,(c*e-a*d)/det)
def decision(x,y):
 lines={p:affine(x,y,p) for p in PAIRS}
 assert all(lines[p][0]>0 for p in EDGES)
 polygon={z for p,q in combinations(EDGES,2) if (z:=intersection(lines[p],lines[q])) is not None
          and all(value(lines[e],z)>=0 for e in EDGES)}
 assert len(polygon)>=3
 certificates=[];counterexamples=[]
 for target in PAIRS:
  if target in EDGES:continue
  minimum=min(value(lines[target],z) for z in polygon)
  if minimum<0:
   witness=min((z for z in polygon if value(lines[target],z)==minimum))
   counterexamples.append({'minor':[i+1 for i in target],'point':list(map(str,witness)),'minimum':str(minimum)})
   continue
  result=None
  for p,q in combinations(EDGES,2):
   P,T=lines[p],lines[q];c,a,b=lines[target];p0,d,e=P;h,g,r=T;det=d*r-e*g
   if not det:continue
   alpha=(a*r-b*g)/det;beta=(d*b-e*a)/det;gamma=c-alpha*P[0]-beta*T[0]
   if min(alpha,beta,gamma)>=0:
    assert all(lines[target][j]==alpha*P[j]+beta*T[j]+(gamma if j==0 else 0) for j in range(3))
    result={'minor':[i+1 for i in target],'edges':[[i+1 for i in p],[i+1 for i in q]],
            'weights':list(map(str,(alpha,beta))),'constant':str(gamma),'minimum':str(minimum)};break
  assert result is not None, 'LP vertex/dual mismatch: bounded feasible fibre must have sparse Farkas witness'
  certificates.append(result)
 assert len(certificates)+len(counterexamples)==14
 return {'verdict':'CYCLIC_SUFFICIENT' if not counterexamples else 'CYCLIC_INSUFFICIENT',
         'cyclic_vertices':len(polygon),'certificates':certificates,'counterexamples':counterexamples}
def main():
 frozen=json.loads((N/'seven-point-cyclic-farkas-packets.json').read_text())['cases'];cases=[]
 for case in frozen:
  x,y=[[Q(v) for v in r] for r in case['source_rows']]
  original=decision(x,y);assert original['verdict']=='CYCLIC_SUFFICIENT' and len(original['certificates'])==14
  # Same target Y, different positive fibre representative; k has six
  # vanishing moments, so the dual verdict and minima are invariant.
  shifted_x=[x[i]+Q(1,1000000)*K[i] for i in range(7)]
  shifted_y=[y[i]-Q(1,1000000)*K[i] for i in range(7)]
  assert all(affine(shifted_x,shifted_y,p)[0]>0 for p in PAIRS)
  assert all(sum(x[i]*(i+1)**r for i in range(7))==sum(shifted_x[i]*(i+1)**r for i in range(7)) for r in range(6))
  assert all(sum(y[i]*(i+1)**r for i in range(7))==sum(shifted_y[i]*(i+1)**r for i in range(7)) for r in range(6))
  shifted=decision(shifted_x,shifted_y)
  assert shifted['verdict']==original['verdict']
  assert [(c['minor'],c['minimum']) for c in original['certificates']]==[(c['minor'],c['minimum']) for c in shifted['certificates']]
  cases.append({'source_gauge':case['negative_initial_columns'],'vertices':original['cyclic_vertices'],
                'whole_fibre_certificates':len(original['certificates']),'gauge_invariant_minima':True})
 outside=decision(list(map(Q,[1,1,0,-1,-1,-1,2])),list(map(Q,[0,1,1,1,0,-2,1])))
 assert outside['verdict']=='CYCLIC_INSUFFICIENT' and outside['counterexamples']
 result={'schema':'marici.nima.seven-point-cyclic-decision.v1','passed':True,'admitted_cases':cases,
  'unadmitted_control':{'verdict':outside['verdict'],'negative_minors':len(outside['counterexamples']),
                        'first_counterexample':outside['counterexamples'][0]},
  'theorem':'For any fixed rational source with strictly positive cyclic minors, the seven-halfspace fibre is compact. Its exact vertices decide all fourteen noncyclic minima; each nonnegative minimum yields an exact Farkas identity supported on at most two cyclic edges, while a negative minimum supplies a rational feasible cyclic vertex violating that minor.',
  'scope':'Complete per-target decision algorithm, not a universal theorem that all admitted targets return CYCLIC_SUFFICIENT.'}
 (N/'seven-point-cyclic-decision.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
