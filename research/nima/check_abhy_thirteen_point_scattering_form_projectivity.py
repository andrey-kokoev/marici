#!/usr/bin/env python3
"""Exact projectivity of the thirteen-point planar scattering 10-form."""
import json
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
N=13;D=N-3

def edge(a,b):return tuple(sorted((a,b)))
zero=(0,)*D
X={edge(i,i+1):zero for i in range(1,N)};X[(1,N)]=zero
for j in range(3,N):X[(1,j)]=tuple(int(k==j-3) for k in range(D))
for i in range(1,N-2):
 for j in range(i+2,N):X[(i+1,j+1)]=tuple(X[(i,j+1)][k]+X[(i+1,j)][k]-X[(i,j)][k] for k in range(D))
def det(A):
 A=[list(r) for r in A];sign=1;prev=1
 for k in range(len(A)-1):
  if A[k][k]==0:
   r=next(r for r in range(k+1,len(A)) if A[r][k]);A[k],A[r]=A[r],A[k];sign=-sign
  pivot=A[k][k]
  for i in range(k+1,len(A)):
   for j in range(k+1,len(A)):A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
  prev=pivot
 return sign*A[-1][-1]
@lru_cache(None)
def tris(v):
 if len(v)==3:return (frozenset(),)
 out=set();a,q=v[0],v[-1]
 for k in range(1,len(v)-1):
  b=v[k];L=(frozenset(),) if k+1<3 else tris(v[:k+1]);R=(frozenset(),) if len(v)-k<3 else tris(v[k:]);add=set()
  if k>1:add.add(edge(a,b))
  if k<len(v)-2:add.add(edge(b,q))
  for l in L:
   for r in R:out.add(frozenset(set(l)|set(r)|add))
 return tuple(out)
def wedge(labels):
 if len(set(labels))<len(labels):return None,0
 inv=sum(labels[i]>labels[j] for i in range(len(labels)) for j in range(i+1,len(labels)))
 return tuple(sorted(labels)),(-1)**inv
terms=[]
for t in tris(tuple(range(1,N+1))):
 ds=sorted(t);names=tuple(f'X{a}{b}' for a,b in ds);J=det([X[d] for d in ds]);terms.append((J,names))
def build(rescaled):
 out=defaultdict(int)
 for orient,names in terms:
  choices=[names]
  if rescaled:choices += [names[:i]+('L',)+names[i+1:] for i in range(N-3)]
  for labels in choices:
   key,sign=wedge(labels)
   if sign:out[key]+=orient*sign
 return {k:v for k,v in out.items() if v}
original=build(False);scaled=build(True);variation={k:scaled.get(k,0)-original.get(k,0) for k in set(original)|set(scaled)};variation={k:v for k,v in variation.items() if v}
checks={'fiftyeightthousandsevenhundredeightysix_cubic_graph_terms':len(terms)==58786,'sixtyfive_channels':len([d for d,v in X.items() if v!=zero])==65,'unit_graph_orientations':all(abs(o)==1 for o,_ in terms),'nonzero_scattering_form':len(original)==58786,'local_rescaling_variation_zero':not variation}
report={'schema':'marici.nima.abhy-thirteen-point-scattering-form-projectivity.v1','benchmark':{'paper':'Arkani-Hamed, Bai, He, Yan, Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet','arxiv':'1711.09102','result':'projectivity of the thirteen-point planar scattering form'},'term_count':len(terms),'oriented_terms':[{'sign':o,'channels':list(q)} for o,q in terms],'transformation':'dlog X_a -> dlog X_a + dlog Lambda','variation_coefficients':{str(k):v for k,v in variation.items()},'checks':checks,'passed':all(checks.values()),'scope':'Exact exterior-algebra projectivity check for the thirteen-point planar scattering 10-form.'}
out=ROOT/'research/nima/results/abhy-thirteen-point-scattering-form-projectivity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'variation_terms':len(variation)},indent=2));raise SystemExit(0 if report['passed'] else 1)
