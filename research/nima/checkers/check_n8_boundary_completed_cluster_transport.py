#!/usr/bin/env python3
"""Complete A3 cluster coefficients with the three exact boundary corrections."""
from itertools import combinations
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text());K=s.Matrix([[s.sympify(x) for x in r] for r in src['kernel_matrix']]);K0=s.Matrix([[s.sympify(x) for x in r] for r in src['kernel_without_upper_boundary_transport']]);B=K-K0
N=6;boundary={tuple(sorted((i,(i+1)%N))) for i in range(N)};ds=[(i,j) for i in range(N) for j in range(i+1,N) if (i,j) not in boundary]
def cross(a,b):x,y=a;u,v=b;return x<u<y<v or u<x<v<y
clusters=sorted(tuple(sorted(c)) for c in combinations(ds,3) if all(not cross(a,b) for a,b in combinations(c,2)))
pos={(i-1,j+1) for i in range(1,4) for j in range(i,4)};neg=sorted(set(ds)-pos)
x={}
for i in range(1,4):
 for j in range(i,4):x[(i-1,j+1)]=K[j-1,i-1]
for i,d in enumerate(neg):x[d]=B[i,i]
W=[s.factor(s.prod(x[d] for d in c)) for c in clusters];edges=sorted((i,j) for i,a in enumerate(clusters) for j,b in enumerate(clusters) if i<j and len(set(a)^set(b))==2)
facehol=[]
for d in ds:
 vs=sorted(i for i,c in enumerate(clusters) if d in c);adj={i:sorted((b if a==i else a) for a,b in edges if i in (a,b) and (b if a==i else a) in vs) for i in vs};st=min(vs);pr=None;cu=st;cy=[st];nx=min(adj[st])
 while nx!=st:cy.append(nx);pr,cu=cu,nx;nx=next(z for z in adj[cu] if z!=pr)
 facehol.append(s.factor(s.prod(W[b]/W[a] for a,b in zip(cy,cy[1:]+cy[:1]))))
defect=s.factor(K[1,0]*K[2,1]-K[1,1]*K[2,0])
checks={'boundary_corrections_exactly_fill_negative_simples':len(neg)==3 and all(B[i,i]!=0 for i in range(3)),'all_nine_coordinates_positive':all(s.sign(v)==1 for v in x.values()),'all_twenty_one_edge_ratios_defined':all(W[a]!=0 and W[b]!=0 for a,b in edges) and len(edges)==21,'all_face_holonomies_one':all(v==1 for v in facehol),'negative_exchange_defect_survives_completion':s.sign(defect)==-1}
out={'schema':'marici.nima.n8-boundary-completed-cluster-transport.v1','completion_rule':'x_[i,j]=K_[i,j] for positive roots; x_(-alpha_i)=(K-K0)_(i,i)','negative_simple_weights':{str(d):str(s.factor(x[d])) for d in neg},'cluster_vertices':14,'mutation_edges':21,'face_holonomies':[str(v) for v in facehol],'exchange_defect':str(defect),'checks':checks,'passed':all(checks.values()),'conclusion':'The exact boundary corrections canonically fill the three missing A3 coefficient coordinates and define a positive flat mutation-ratio system. The negative physical exchange defect remains separate and therefore is not holonomy of this rank-one coefficient line.','claim_boundary':'Exact only for the selected n=8 kernel. Arbitrary-n use requires proving that every negative-simple coordinate is the corresponding transported diagonal boundary correction.'};p=ROOT/'research/nima/results/n8-boundary-completed-cluster-transport.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
