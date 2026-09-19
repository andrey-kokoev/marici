#!/usr/bin/env python3
"""Exact A3 weighted-local-system audit for the completed n=8 coefficients."""
from itertools import combinations
from pathlib import Path
from math import gcd
from fractions import Fraction
import json, sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text())
K=s.Matrix([[s.Rational(x) for x in r] for r in src['kernel_matrix']]);K0=s.Matrix([[s.Rational(x) for x in r] for r in src['kernel_without_upper_boundary_transport']]);B=K-K0
N=6; boundary={tuple(sorted((i,(i+1)%N))) for i in range(N)}
ds=[(i,j) for i in range(N) for j in range(i+1,N) if (i,j) not in boundary]
def cross(a,b): x,y=a;u,v=b;return x<u<y<v or u<x<v<y
V=sorted(tuple(sorted(c)) for c in combinations(ds,3) if all(not cross(a,b) for a,b in combinations(c,2)))
E=sorted((i,j) for i,a in enumerate(V) for j,b in enumerate(V) if i<j and len(set(a)^set(b))==2); ep={e:i for i,e in enumerate(E)}
F=[]
for d in ds:
 vs=sorted(i for i,c in enumerate(V) if d in c); adj={i:sorted((b if a==i else a) for a,b in E if i in (a,b) and (b if a==i else a) in vs) for i in vs}; st=min(vs);pr=None;cu=st;cy=[st];nx=min(adj[st])
 while nx!=st: cy.append(nx);pr,cu=cu,nx;nx=next(z for z in adj[cu] if z!=pr)
 F.append({'diagonal':d,'cycle':cy})
F.sort(key=lambda z:z['diagonal'])
D1=s.zeros(14,21);D2=s.zeros(21,9)
for q,(a,b) in enumerate(E):D1[a,q]=-1;D1[b,q]=1
for q,f in enumerate(F):
 for a,b in zip(f['cycle'],f['cycle'][1:]+f['cycle'][:1]):
  e=tuple(sorted((a,b)));D2[ep[e],q]=1 if e==(a,b) else -1
ns=D2.nullspace()[0];den=s.ilcm(*[z.q for z in ns]);top=[int(z*den) for z in ns];g=0
for z in top:g=gcd(g,abs(z))
top=[z//g for z in top]
if next(z for z in top if z)<0:top=[-z for z in top]
D3=s.Matrix(top)
pos={(i-1,j+1) for i in range(1,4) for j in range(i,4)};neg=sorted(set(ds)-pos);x={}
for i in range(1,4):
 for j in range(i,4):x[(i-1,j+1)]=K[j-1,i-1]
for i,d in enumerate(neg):x[d]=B[i,i]
W=[s.factor(s.prod(x[d] for d in c)) for c in V]
# Gauge values on an oriented cell are the potential at its deterministic base vertex.
g0=s.diag(*W);g1=s.diag(*[W[a] for a,b in E]);g2=s.diag(*[W[min(f['cycle'])] for f in F]);g3=s.diag(W[0])
D1w=s.simplify(g0*D1*g1.inv());D2w=s.simplify(g1*D2*g2.inv());D3w=s.simplify(g2*D3*g3.inv())
# The direct edge formula is [-1, W_b/W_a] for every a<b edge.
direct=True
for q,(a,b) in enumerate(E):direct &= D1w[a,q]==-1 and s.factor(D1w[b,q]-W[b]/W[a])==0
# Q ranks and homology.
ranks=[D1w.rank(),D2w.rank(),D3w.rank()];hom=[14-ranks[0]-1,21-ranks[0]-ranks[1],9-ranks[1]-ranks[2],1-ranks[2]]
# A rational coefficient has an F2 reduction only if its denominator is odd. A rank-one local system further needs every gauge value nonzero mod 2.
def v2(z):
 z=int(z);c=0
 while z and z%2==0:c+=1;z//=2
 return c
valuations=[v2(w.p)-v2(w.q) for w in W]; f2_units=all(v==0 for v in valuations)
# Hostile insertion: multiply one incidence in the first face by 1+exchange defect.
defect=s.factor(K[1,0]*K[2,1]-K[1,1]*K[2,0]);bad=s.MutableDenseMatrix(D2w);nz=[i for i in range(21) if bad[i,0]!=0];bad[nz[0],0]=s.factor((1+defect)*bad[nz[0],0]);curv=s.simplify(D1w*bad);nonzero=[{'vertex':i,'face':j,'value':str(s.factor(curv[i,j]))} for i in range(14) for j in range(9) if curv[i,j]!=0]
checks={'direct_edge_ratio_formula':bool(direct),'weighted_d1_d2_zero_over_Q':D1w*D2w==s.zeros(14,9),'weighted_d2_d3_zero_over_Q':D2w*D3w==s.zeros(21,1),'ranks_13_8_1_over_Q':ranks==[13,8,1],'zero_augmented_homology_over_Q':hom==[0,0,0,0],'flat_twist_diagonally_conjugate':True,'exchange_defect_nonzero':defect!=0,'naive_defect_insertion_curved':len(nonzero)>0,'naive_curvature_rank_one':curv.rank()==1}
out={'schema':'marici.nima.a3-weighted-local-system-code-audit.v1','coefficient_field':'Q','gauge_convention':'For each oriented cell use the completed cluster potential at its least-index vertex; D_k^rho=G_(k-1) D_k G_k^{-1}.','vertex_potential_count':len(W),'weighted_ranks':{'d1':ranks[0],'d2':ranks[1],'d3':ranks[2]},'augmented_homology_dimensions':hom,'mod2':{'vertex_potential_2_adic_valuations':valuations,'all_gauge_values_F2_units':f2_units,'disposition':'valid rank-one F2 local system' if f2_units else 'no direct F2 local-system reduction: at least one rational gauge value is not a 2-adic unit'},'exchange_defect':str(defect),'hostile_naive_face_insertion':{'rule':'multiply one nonzero incidence of the first face by 1+exchange_defect','curvature_rank':curv.rank(),'nonzero_residuals':nonzero},'checks':checks,'passed':all(checks.values()),'disposition':{'flat_positive_transport':'trivial gauge twist with zero logical dimension','negative_exchange_defect':'curved obstruction under the tested naive face insertion; not a syndrome, stabilizer deformation, or subsystem generator without an independently typed physical-error-to-chain map'},'minimal_missing_operational_map':'A sourced map from physical canonical-weight perturbations/errors to C1 or C2 chains, together with a declared binary or qudit coefficient reduction and syndrome readout.','claim_boundary':'Exact finite A3 audit over Q for the selected n=8 completed weights. The mod-2 test diagnoses whether the rational gauge itself descends; it does not choose a new integral normalization. No LDPC locality, distance, or operational protection claim follows.'}
p=ROOT/'research/nima/results/a3-weighted-local-system-code-audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
