#!/usr/bin/env python3
"""Exact naturality and forest-coordinate metric checks for augmented observers."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/common-history-augmented-observer-transition.v1.json'
RESULT=ROOT/'research/voevodsky/results/common_history_augmented_observer_transition.json'
d=json.loads(CONTRACT.read_text())
stages=[
 {'v':3,'e':[(0,1),(1,2),(0,2)],'tree':[0,1]},
 {'v':4,'e':[(0,1),(1,2),(0,2),(2,3),(0,3),(1,3)],'tree':[0,1,3]},
 {'v':5,'e':[(0,1),(1,2),(0,2),(2,3),(0,3),(1,3),(3,4),(0,4)],'tree':[0,1,3,6]}]
def incidence(g):
 B=s.zeros(5,len(g['e']))
 for j,(a,b) in enumerate(g['e']): B[a,j]=-1; B[b,j]=1
 return B
def cycle_basis(g,tree=None):
 tree=g['tree'] if tree is None else tree; chords=[j for j in range(len(g['e'])) if j not in tree]; B=incidence(g)[:g['v']-1,:]; cols=[]
 for q in chords:
  x=s.zeros(len(g['e']),1); x[q]=1; sol=list(s.linsolve((B[:,tree],-B[:,q])))[0]
  for j,a in zip(tree,sol): x[j]=a
  cols.append(x)
 return s.Matrix.hstack(*cols),chords
def chord_map(g):
 _,ch=cycle_basis(g); Z=s.zeros(len(ch),len(g['e']))
 for i,j in enumerate(ch): Z[i,j]=1
 return Z
def edge_inclusion(a,b):
 E=s.zeros(len(b['e']),len(a['e']))
 for j in range(len(a['e'])): E[j,j]=1
 return E
def chord_inclusion(a,b):
 za=chord_map(a); zb=chord_map(b); I=s.zeros(zb.rows,za.rows)
 for j in range(za.rows): I[j,j]=1
 return I
checks={}
for i in (0,1):
 a,b=stages[i],stages[i+1]; E=edge_inclusion(a,b); I=chord_inclusion(a,b); Ba,Bb=incidence(a),incidence(b); Za,Zb=chord_map(a),chord_map(b)
 checks[f'history_naturality_{i}']=Bb*E==Ba
 checks[f'cycle_naturality_{i}']=Zb*E==I*Za
 Oa=Ba.col_join(Za); Ob=Bb.col_join(Zb); target=s.diag(s.eye(5),I)
 checks[f'augmented_naturality_{i}']=Ob*E==target*Oa
 checks[f'augmented_faithfulness_{i}']=Oa.rank()==len(a['e'])
 checks[f'old_bound_data_monotone_{i}']=len(b['e'])>=len(a['e']) and b['v']>=a['v']
checks['final_augmented_faithfulness']=incidence(stages[2]).col_join(chord_map(stages[2])).rank()==len(stages[2]['e'])
# Forest-coordinate invariance at middle stage with positive unequal persistent edge weights.
g=stages[1]; F,Fch=cycle_basis(g); Fp,_=cycle_basis(g,[0,3,4]); T=F.gauss_jordan_solve(Fp)[0] # Fp=F T
W=s.diag(1,2,3,4,5,6); Q=F.T*W*F; Qp=Fp.T*W*Fp
checks['forest_Gram_congruence']=Qp==T.T*Q*T
xprime=s.Matrix([2,-1,3]); x=T*xprime
checks['represented_cycle_equal']=F*x==Fp*xprime
checks['forest_coordinate_norm_invariant']=(x.T*Q*x)[0]==(xprime.T*Qp*xprime)[0]
checks['coordinate_identity_metric_not_invariant']=T.T*T!=s.eye(T.cols)
# Old-cycle Gram principal block persists after graph extension with old weights.
F0,_=cycle_basis(stages[0]); F1,_=cycle_basis(stages[1]); W0=s.diag(1,2,3); W1=s.diag(1,2,3,4,5,6)
checks['old_cycle_metric_principal_block']=(F1.T*W1*F1)[:1,:1]==F0.T*W0*F0
checks['calibration_and_completion_not_promoted']=not d['claim_boundary']['edge_weights_source_calibrated'] and not d['claim_boundary']['completed_observer_constructed']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.common-history-augmented-observer-transition-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'tested_cycle_ranks':[1,3,4],'forest_basis_change':[[str(v) for v in row] for row in T.tolist()],'disposition':{'constructed':'cutoffwise natural faithful augmented observers and forest-coordinate invariant ambient-edge cycle form','remaining':'edge weights are uncalibrated and history constants lack uniform cutoff control','next':'uniform_or_weighted_cutoff_completion'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'cycle_ranks':[1,3,4]}))
raise SystemExit(0 if result['passed'] else 1)
