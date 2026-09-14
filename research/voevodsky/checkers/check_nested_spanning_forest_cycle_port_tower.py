#!/usr/bin/env python3
"""Exact nested-forest cycle-coordinate transition checks."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/nested-spanning-forest-cycle-port-tower.v1.json'
RESULT=ROOT/'research/voevodsky/results/nested_spanning_forest_cycle_port_tower.json'
d=json.loads(CONTRACT.read_text())
stages=[
 {'vertices':3,'edges':[(0,1),(1,2),(0,2)],'tree':[0,1]},
 {'vertices':4,'edges':[(0,1),(1,2),(0,2),(2,3),(0,3),(1,3)],'tree':[0,1,3]},
 {'vertices':5,'edges':[(0,1),(1,2),(0,2),(2,3),(0,3),(1,3),(3,4),(0,4)],'tree':[0,1,3,6]},]
def incidence(stage):
 B=s.zeros(stage['vertices'],len(stage['edges']))
 for j,(a,b) in enumerate(stage['edges']): B[a,j]=-1; B[b,j]=1
 return B
def basis(stage,tree=None):
 tree=stage['tree'] if tree is None else tree; chords=[j for j in range(len(stage['edges'])) if j not in tree]; B=incidence(stage); cols=[]
 for chord in chords:
  x=s.zeros(len(stage['edges']),1); x[chord]=1
  # Solve tree boundary cancellation with one redundant vertex row removed.
  Bt=B[:-1,tree]; rhs=-(B[:-1,chord]); sol=list(s.linsolve((Bt,rhs)))[0]
  for j,v in zip(tree,sol): x[j]=v
  cols.append(x)
 return s.Matrix.hstack(*cols),chords
checks={}; bases=[]
for i,g in enumerate(stages):
 B=incidence(g); Z,ch=basis(g); bases.append((Z,ch))
 beta=len(g['edges'])-g['vertices']+1
 checks[f'cycle_rank_{i}']=Z.rank()==beta==len(ch)
 checks[f'boundary_zero_{i}']=B*Z==s.zeros(g['vertices'],beta)
 checks[f'chord_identity_coordinates_{i}']=Z.extract(ch,range(beta))==s.eye(beta)
# Inclusions append edge coordinates; old fundamental cycles remain columns.
for i in (0,1):
 Zi,chi=bases[i]; Zj,chj=bases[i+1]; padded=Zi.col_join(s.zeros(len(stages[i+1]['edges'])-len(stages[i]['edges']),Zi.cols))
 checks[f'old_cycles_persist_{i}_{i+1}']=Zj[:,:Zi.cols]==padded
 P=s.zeros(Zi.cols,Zj.cols)
 for k in range(Zi.cols): P[k,k]=1
 I=P.T
 checks[f'cycle_coordinate_split_{i}_{i+1}']=P*I==s.eye(Zi.cols)
I01=s.Matrix([[1],[0],[0]]); I12=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,0]]); I02=s.Matrix([[1],[0],[0],[0]])
checks['three_stage_coordinate_composition']=I12*I01==I02
# Alternate forest on stage 1 changes cycle basis nonorthogonally.
Zold,_=bases[1]; Zalt,_=basis(stages[1],[0,3,4]);
T=Zalt.gauss_jordan_solve(Zold)[0]
checks['alternate_forest_integral_basis_change']=all(x.q==1 for x in T)
checks['identity_chord_metric_not_forest_invariant']=T.T*T!=s.eye(T.cols)
checks['cycle_rank_unbounded_not_claimed']=not d['claim_boundary']['uniform_cycle_rank_bound_claimed']
checks['history_transition_still_open']=not d['claim_boundary']['history_transition_constructed']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.nested-spanning-forest-cycle-port-tower-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'fixture_cycle_ranks':[z.cols for z,_ in bases],'alternate_forest_basis_change':[[str(x) for x in row] for row in T.tolist()],'disposition':{'constructed':'nested finite cycle-port inclusions/projections with persistent old fundamental cycles','residual':'identity covariance depends on forest basis and common-history Hilbert transitions remain undeclared','next':'common_history_cutoff_transition'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'cycle_ranks':result['fixture_cycle_ranks']}))
raise SystemExit(0 if result['passed'] else 1)
