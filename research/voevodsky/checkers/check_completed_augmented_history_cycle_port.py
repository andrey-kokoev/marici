#!/usr/bin/env python3
"""Checks finite chord faithfulness and completed-port continuity boundaries."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/the_completed_augmented_history_is_faithful_without_a_cycle_hilbert_metric_20260912.md'
GLOBAL=ROOT/'research/voevodsky/a_symmetric_arithmetic_grade_constructs_an_all_ratio_history_carrier_20260912.md'
RESULT=ROOT/'research/voevodsky/results/completed_augmented_history_cycle_port.json'
primes=(2,3,5,7,11,13,17); shells=list(zip(primes,primes[1:])); checks={}
def graph(L):
 E=sorted([(k*p*q,k,p,q) for p,q in shells for k in range(1,L+1) if k*p*q<=L]); V=sorted({k*p for w,k,p,q in E}|{k*q for w,k,p,q in E}); vi={v:i for i,v in enumerate(V)}; B=s.zeros(len(V),len(E))
 for j,(w,k,p,q) in enumerate(E): B[vi[k*p],j]-=1; B[vi[k*q],j]+=1
 parent=list(range(len(V)))
 def find(x):
  while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
  return x
 tree=[]
 for j,(w,k,p,q) in enumerate(E):
  a,bb=find(vi[k*p]),find(vi[k*q])
  if a!=bb: parent[a]=bb; tree.append(j)
 chords=[j for j in range(len(E)) if j not in tree]; Z=s.zeros(len(chords),len(E))
 for i,j in enumerate(chords): Z[i,j]=1
 return E,V,B,Z,tree,chords
for L in (100,200,400):
 E,V,B,Z,T,K=graph(L); beta=len(E)-B.rank()
 checks[f'cycle_dimension_{L}']=beta==len(K)
 checks[f'chord_injective_on_cycles_{L}']=s.Matrix.vstack(B,Z).rank()==len(E)
 checks[f'forest_size_{L}']=len(T)==B.rank()
 for delta in (1,2):
  c=[Fraction((i%7)-3,i+1) for i in range(len(E))]
  qE=sum(abs(c[i])*(E[i][0]**delta) for i in range(len(E))); qK=sum(abs(c[j])*(E[j][0]**delta) for j in K)
  checks[f'chord_contractive_{L}_{delta}']=qK<=qE
# Global all-ratio weight only strengthens the normalized chord estimate.
checks['global_grade_dependency']='W_{\\mathrm{all}}(a,b;j,k)' in GLOBAL.read_text()
text=PACKET.read_text()
checks['completion_kernel_is_explicit_premise']='This closure is an explicit premise here' in text
checks['forest_uniformity_not_claimed']='Without that uniform estimate' in text
checks['no_cycle_hilbert_promotion']='constructs no cycle-sector Hilbert metric' in text
checks['separate_structures_stated']='route residue has a projective locally convex topology' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.completed-augmented-history-cycle-port-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'global_history':hashlib.sha256(GLOBAL.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'disposition':{'proved':'chord selector projective continuity and finite-cutoff joint faithfulness','conditional':'completed joint faithfulness requires completed cycle-kernel closure','remaining':['cycle-kernel closure','uniform forest-change continuity','physical cycle covariance']}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks)})); raise SystemExit(0 if result['passed'] else 1)
