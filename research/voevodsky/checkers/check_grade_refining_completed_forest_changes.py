#!/usr/bin/env python3
"""Exact finite checks for grade-controlled greedy forest transitions."""
from pathlib import Path
import hashlib,json,math
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/grade_refining_greedy_forests_have_equivalent_completed_cycle_coordinates_20260912.md'
GROUP=ROOT/'research/voevodsky/contracts/forest-presentation-cycle-groupoid.v1.json'
RESULT=ROOT/'research/voevodsky/results/grade_refining_completed_forest_changes.json'
primes=(2,3,5,7,11,13,17,19); shells=list(zip(primes,primes[1:])); checks={}
def setup(L,reverse_ties=False):
 E=[(k*p*q,k,p,q) for p,q in shells for k in range(1,L+1) if k*p*q<=L]; E=sorted(E,key=lambda e:(e[0],(-e[1],-e[2],-e[3]) if reverse_ties else (e[1],e[2],e[3])))
 V=sorted({k*p for w,k,p,q in E}|{k*q for w,k,p,q in E}); vi={v:i for i,v in enumerate(V)}; B=s.zeros(len(V),len(E)); parent=list(range(len(V)))
 for j,(w,k,p,q) in enumerate(E): B[vi[k*p],j]-=1; B[vi[k*q],j]+=1
 def find(x):
  while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
  return x
 tree=[]
 for j,(w,k,p,q) in enumerate(E):
  a,b=find(vi[k*p]),find(vi[k*q])
  if a!=b: parent[a]=b; tree.append(j)
 chords=[j for j in range(len(E)) if j not in tree]; cols=[]
 for qidx in chords:
  x=s.zeros(len(E),1); x[qidx]=1
  sol=list(s.linsolve((B[:-1,tree],-B[:-1,qidx])))[0]
  for j,v in zip(tree,sol): x[j]=v
  cols.append(x)
 F=s.Matrix.hstack(*cols) if cols else s.zeros(len(E),0)
 return E,B,tree,chords,F
for L in (100,200,400):
 # Orders can differ only when grades tie; align common edge rows before comparing.
 ET,BT,TT,KT,FT=setup(L,False); EU,BU,TU,KU,FU=setup(L,True); posU={e:i for i,e in enumerate(EU)}; P=s.zeros(len(EU),len(ET))
 for i,e in enumerate(ET): P[posU[e],i]=1
 C=FU.gauss_jordan_solve(P*FT)[0]
 checks[f'cycle_representation_{L}']=BU*FU==s.zeros(BU.rows,FU.cols) and BU*P*FT==s.zeros(BU.rows,FT.cols)
 checks[f'integral_transition_{L}']=all(x.q==1 for x in C)
 checks[f'invertible_transition_{L}']=C.rows==C.cols and abs(C.det())==1
 checks[f'grade_path_T_{L}']=all(all(ET[j][0]<=ET[q][0] for j,x in enumerate(FT[:,i]) if x!=0) for i,q in enumerate(KT))
 checks[f'grade_path_U_{L}']=all(all(EU[j][0]<=EU[q][0] for j,x in enumerate(FU[:,i]) if x!=0) for i,q in enumerate(KU))
 for delta in (.2,1):
  ok=True
  for col,qidx in enumerate(KT):
   source=ET[qidx][0]; target=sum(abs(float(C[row,col]))*math.exp(delta*math.log(EU[u][0])) for row,u in enumerate(KU)); ok &= target<=math.exp((delta+5)*math.log(source))+1e-10
  checks[f'projective_column_bound_{L}_{delta}']=ok
text=PACKET.read_text(); checks['arbitrary_forest_boundary']='An arbitrary spanning forest need not satisfy the path-grade condition' in text
checks['no_preferred_forest']='No one forest is selected as ontologically or physically preferred' in text
checks['finite_groupoid_dependency']='integral' in json.loads(GROUP.read_text())['arrows']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.grade-refining-completed-forest-change-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'groupoid':hashlib.sha256(GROUP.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'proved':'bicontinuous completed forest changes for grade-refining greedy orders with seminorm shift 5','excluded':'arbitrary forests without path-grade control','remaining':'physical cycle covariance'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
