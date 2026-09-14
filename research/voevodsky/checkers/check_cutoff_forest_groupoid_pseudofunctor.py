#!/usr/bin/env python3
"""Exact cutoff/forest interchange and reciprocal naturality checks."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/cutoff-forest-groupoid-pseudofunctor.v1.json'
RESULT=ROOT/'research/voevodsky/results/cutoff_forest_groupoid_pseudofunctor.json'
d=json.loads(CONTRACT.read_text())
stages=(4,6,8)
def boundary(N):
 B=s.zeros(2,N)
 for j in range(N):
  a,b=((0,1) if j%2==0 else (1,0)); B[a,j]=-1; B[b,j]=1
 return B
def basis(N,tree):
 B=boundary(N); chords=[j for j in range(N) if j!=tree]; cols=[]
 for q in chords:
  x=s.zeros(N,1); x[q]=1; x[tree]=-B[0,q]/B[0,tree]; cols.append(x)
 return s.Matrix.hstack(*cols)
def pad(M,N):
 J=s.zeros(N,M); J[:M,:M]=s.eye(M); return J
def coord(Ndst,tdst,Nsrc,tsrc): return basis(Ndst,tdst).gauss_jordan_solve(pad(Nsrc,Ndst)*basis(Nsrc,tsrc))[0]
def change(N,dst,src): return basis(N,dst).gauss_jordan_solve(basis(N,src))[0]
def refl_edge(N):
 R=s.zeros(N)
 for j in range(0,N,2): R[j,j+1]=R[j+1,j]=1
 return R
def refl_coord(N,t): return basis(N,1-t).gauss_jordan_solve(refl_edge(N)*basis(N,t))[0]
checks={}
checks['cycle_dimensions']=all(basis(N,t).shape==(N,N-1) and boundary(N)*basis(N,t)==s.zeros(2,N-1) for N in stages for t in (0,1))
checks['horizontal_integrality']=all(all(x.q==1 for x in coord(E,t2,D,t1)) for D,E in ((4,6),(6,8),(4,8)) for t1 in (0,1) for t2 in (0,1))
checks['interchange']=all(change(E,u2,t2)*coord(E,t2,D,t1)==coord(E,u2,D,u1)*change(D,u1,t1) for D,E in ((4,6),(6,8),(4,8)) for t1,u1,t2,u2 in ((0,1,0,1),(1,0,1,0),(0,1,1,0),(1,0,0,1)))
checks['cutoff_composition']=all(coord(8,t8,6,t6)*coord(6,t6,4,t4)==coord(8,t8,4,t4) for t4 in (0,1) for t6 in (0,1) for t8 in (0,1))
checks['identity']=all(coord(N,t,N,t)==s.eye(N-1) for N in stages for t in (0,1))
checks['edge_reflection_commutes_with_cutoff']=all(refl_edge(E)*pad(D,E)==pad(D,E)*refl_edge(D) for D,E in ((4,6),(6,8),(4,8)))
checks['reciprocal_naturality']=all(refl_coord(E,tE)*coord(E,tE,D,tD)==coord(E,1-tE,D,1-tD)*refl_coord(D,tD) for D,E in ((4,6),(6,8),(4,8)) for tD in (0,1) for tE in (0,1))
checks['reciprocal_involution']=all(refl_coord(N,1-t)*refl_coord(N,t)==s.eye(N-1) for N in stages for t in (0,1))
# Stable diagonal edge forms pull back exactly along zero extension.
def metric(N): return s.diag(*[1+j//2 for j in range(N)])
checks['ambient_forms_cutoff_compatible']=all(pad(D,E).T*metric(E)*pad(D,E)==metric(D) for D,E in ((4,6),(6,8),(4,8)))
checks['cycle_metrics_pull_back']=all((basis(E,tE)*coord(E,tE,D,tD)).T*metric(E)*(basis(E,tE)*coord(E,tE,D,tD))==basis(D,tD).T*metric(D)*basis(D,tD) for D,E in ((4,6),(6,8),(4,8)) for tD in (0,1) for tE in (0,1))
checks['no_completion_or_calibration_promotion']=not d['claim_boundary']['completed_projective_colimit_constructed'] and not d['claim_boundary']['metric_calibrated']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.cutoff-forest-groupoid-pseudofunctor-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'stages':list(stages),'forest_presentations_per_stage':2,'disposition':{'constructed':'finite nested-cutoff pseudofunctor with forest interchange, reciprocal naturality, and metric pullback','remaining':'instantiate source arithmetic cutoff and prove completed continuity'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'stages':len(stages)}))
raise SystemExit(0 if result['passed'] else 1)
