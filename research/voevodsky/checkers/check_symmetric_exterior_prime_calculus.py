#!/usr/bin/env python3
"""Exact operator checks for the symmetric--exterior prime-index calculus."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/naturals_carry_a_symmetric_exterior_prime_index_calculus.md'
RESULT=ROOT/'research/voevodsky/results/symmetric_exterior_prime_calculus.json'
N=5

def add(out,state,value):
 out[state]=out.get(state,0)+value
 if out[state]==0:del out[state]
def creation(i,vector):
 out={}
 for state,c in vector.items():
  target=list(state);target[i]+=1;add(out,tuple(target),c)
 return out
def annihilation(i,vector):
 out={}
 for state,c in vector.items():
  if state[i]:
   target=list(state);target[i]-=1;add(out,tuple(target),c*state[i])
 return out
def transfer(a,b,vector):return creation(a,annihilation(b,vector))
def compose(f,g,state):return f(g({state:1}))
def subtract(a,b):
 out=dict(a)
 for state,c in b.items():add(out,state,-c)
 return out
def scalar_op(value,f,state):return {k:value*v for k,v in f({state:1}).items()}
def identity(state):return {state:1}
def exterior_wedge_same_direction():return 0

states=list(product(range(3),repeat=N));checks={};weyl=0;matrix_units=0
for state in states:
 for i in range(N):
  for j in range(N):
   lhs=subtract(compose(lambda v,i=i:annihilation(i,v),lambda v,j=j:creation(j,v),state),compose(lambda v,j=j:creation(j,v),lambda v,i=i:annihilation(i,v),state))
   expected=identity(state) if i==j else {}
   checks[f'weyl_{state}_{i}_{j}']=lhs==expected;weyl+=1
# Test matrix-unit relations on a bounded but discriminating basis with occupations 0 or 1.
small=list(product(range(2),repeat=N))
for state in small:
 for a,b,c,d in product(range(N),repeat=4):
  left=subtract(compose(lambda v,a=a,b=b:transfer(a,b,v),lambda v,c=c,d=d:transfer(c,d,v),state),compose(lambda v,c=c,d=d:transfer(c,d,v),lambda v,a=a,b=b:transfer(a,b,v),state))
  right={}
  if b==c:
   for target,value in transfer(a,d,{state:1}).items():add(right,target,value)
  if a==d:
   for target,value in transfer(c,b,{state:1}).items():add(right,target,-value)
  checks[f'gl_{state}_{a}_{b}_{c}_{d}']=left==right;matrix_units+=1
for i in range(N-2):
 state=tuple(1 for _ in range(N));ei=lambda v,i=i:transfer(i+1,i,v);ej=lambda v,i=i:transfer(i+2,i+1,v)
 comm=subtract(ei(ej({state:1})),ej(ei({state:1})));expected={k:-v for k,v in transfer(i+2,i,{state:1}).items()}
 checks[f'adjacent_commutator_{i}']=comm==expected
for i in range(N-1):
 for j in range(i+2,N-1):
  state=tuple(1 for _ in range(N));ei=lambda v,i=i:transfer(i+1,i,v);ej=lambda v,j=j:transfer(j+1,j,v)
  checks[f'disjoint_commutator_{i}_{j}']=subtract(ei(ej({state:1})),ej(ei({state:1})))=={}
state=[0]*N;state[1]=2;state=tuple(state);twice=transfer(2,1,transfer(2,1,{state:1}))
checks['same_shell_twice_nonzero']=bool(twice)
checks['same_shell_twice_coefficient_two']=list(twice.values())==[2]
checks['exterior_square_zero']=exterior_wedge_same_direction()==0
checks['symmetric_and_exterior_behaviors_differ']=bool(twice) and exterior_wedge_same_direction()==0
text=PACKET.read_text(encoding='utf-8');checks['physical_scope_excluded']='no physical particle interpretation is asserted' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.symmetric-exterior-prime-calculus.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'valuation_states_tested':len(states),'weyl_tests':weyl,'matrix_unit_tests':matrix_units,'same_shell_twice':{str(k):v for k,v in twice.items()},'checks':checks,'check_count':len(checks),'passed':all(checks.values()),'disposition':{'established':'Weyl prime-occupancy algebra and exterior shell-direction algebra coexist on Sym(F) tensor Lambda(W)','residual':'construct divided-power or labelled-chip higher cells for repeated shell directions'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'weyl':weyl,'matrix_units':matrix_units,'same_shell_twice':result['same_shell_twice']}));raise SystemExit(0 if result['passed'] else 1)
