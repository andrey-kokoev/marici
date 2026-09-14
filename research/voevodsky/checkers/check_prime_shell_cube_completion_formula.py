#!/usr/bin/env python3
"""Finite exhaustive hostile for prime-shell cube completion formula."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/canonical_prime_shell_cube_has_the_minimal_completion_grade.md'
RESULT=ROOT/'research/voevodsky/results/prime_shell_cube_completion_formula.json'
PRIMES=(2,3,5,7,11,13,17,19,23,29,31,37)

def cube(indices):
 base=1
 for i in indices:base*=PRIMES[i-1]
 vertices={}
 for mask in range(1<<len(indices)):
  v=base
  for bit,i in enumerate(indices):
   if mask>>bit&1:v=v*PRIMES[i]//PRIMES[i-1]
  vertices[mask]=v
 edges=[]
 for mask,source in vertices.items():
  for bit,i in enumerate(indices):
   if not(mask>>bit&1):edges.append((mask,i,source,vertices[mask|1<<bit],source*PRIMES[i]))
 return vertices,edges

def formula(indices):return PRIMES[indices[-1]-1]*prod(PRIMES[i] for i in indices)
def prod(xs):
 out=1
 for x in xs:out*=x
 return out

checks={};dimensions={};tested=0
for n in range(2,7):
 records=[]
 for indices in combinations(range(1,11),n):
  vertices,edges=cube(indices);grades=[e[4] for e in edges];actual=max(grades);expected=formula(indices);latest=[e for e in edges if e[4]==actual]
  key='-'.join(map(str,indices));checks[f'injective_{key}']=len(set(vertices.values()))==1<<n;checks[f'formula_{key}']=actual==expected;checks[f'unique_latest_{key}']=len(latest)==1 and latest[0][1]==indices[-1];tested+=1
  records.append((actual,indices))
 records.sort();canonical=tuple(range(1,n+1));checks[f'canonical_unique_min_n{n}']=records[0][1]==canonical and (len(records)==1 or records[1][0]>records[0][0])
 dimensions[str(n)]={'canonical_indices':canonical,'completion_grade':records[0][0],'second_grade':records[1][0] if len(records)>1 else None,'subsets_tested':len(records)}
checks['known_grades']= [dimensions[str(n)]['completion_grade'] for n in range(2,6)]==[45,525,8085,165165]
text=PACKET.read_text(encoding='utf-8');checks['noncubical_global_residual_retained']='noncubical subgraph' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.prime-shell-cube-completion-formula.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'shell_subsets_tested':tested,'dimensions':dimensions,'check_count':len(checks),'checks':checks,'passed':all(checks.values()),'disposition':{'established':'completion formula and unique canonical minimum in exhaustive range','residual':'exclude earlier noncubical full-support shell residues'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'subsets':tested,'dimensions':dimensions}));raise SystemExit(0 if result['passed'] else 1)
