#!/usr/bin/env python3
"""Exact prime-height floor sums for pyramid cells and path counts."""
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/pyramid_cell_counts_are_prime_height_floor_sums.md'
C525=ROOT/'research/voevodsky/results/pyramid_surface_paths_and_fillers_525.json'
C8085=ROOT/'research/voevodsky/results/pyramid_surface_paths_and_fillers_8085.json'
FIVE=ROOT/'research/voevodsky/results/five_cube_probe_depth.json'
RESULT=ROOT/'research/voevodsky/results/pyramid_cell_floor_sums.json'

def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
def selected_floor_sum(values,r,limit,total_scale):
 if r==0:return limit
 total=0
 def visit(start,left,product):
  nonlocal total
  if left==0:total+=limit//product;return
  if len(values)-start<left:return
  for pos in range(start,len(values)-left+1):
   value=values[pos]
   if product*value>limit:break
   # The remaining least possible factors must fit.
   candidate=product*value;minimum=candidate
   for q in values[pos+1:pos+left]:minimum*=q
   if left>1 and minimum>limit:break
   visit(pos+1,left-1,candidate)
 visit(0,r,1);return total
def cell_count(L,n):
 ps=primes(L//2+3);total=0
 for m in range(n-1,len(ps)-1):
  base=ps[m]*ps[m+1]
  if base>L:break
  limit=L//base;values=[ps[i+1] for i in range(m)]
  total+=selected_floor_sum(values,n-1,limit,limit)
 return total
def census(L):
 counts={};n=1
 while True:
  value=cell_count(L,n)
  if value==0:break
  counts[str(n)]=value;n+=1
 return counts
def paths(counts):return sum(factorial(int(n))*v for n,v in counts.items())

checks={};computed={}
references={}
for path in (C525,C8085):
 data=json.loads(path.read_text(encoding='utf-8'))
 references.update(data['censuses'])
for L in (522,524,525,8084,8085):
 counts=census(L);computed[str(L)]={'cell_counts':counts,'typed_maximal_paths':paths(counts)}
 if str(L) in references:
  ref=references[str(L)]
  checks[f'cell_counts_{L}']=all(counts.get(k,0)==v for k,v in ref['cell_counts'].items() if k!='0') and all(ref['cell_counts'].get(k,0)==v for k,v in counts.items())
  checks[f'path_count_{L}']=paths(counts)==ref['typed_maximal_paths']
for L in (525,8085):
 before=computed[str(L-1)]['cell_counts'];at=computed[str(L)]['cell_counts'];delta={str(n):at.get(str(n),0)-before.get(str(n),0) for n in range(1,max(map(int,at))+1)}
 computed[str(L)]['positive_degree_attachment']=delta
checks['attachment_525']=computed['525']['positive_degree_attachment']=={'1':2,'2':2,'3':1}
checks['attachment_8085']=computed['8085']['positive_degree_attachment']=={'1':3,'2':4,'3':3,'4':1}
for L in (165164,165165):
 counts=census(L);computed[str(L)]={'cell_counts':counts,'typed_maximal_paths':paths(counts)}
before=computed['165164']['cell_counts'];at=computed['165165']['cell_counts'];delta={str(n):at.get(str(n),0)-before.get(str(n),0) for n in range(1,max(map(int,at))+1)};computed['165165']['positive_degree_attachment']=delta
checks['five_cube_top_cell_unique']=delta.get('5')==1
five=json.loads(FIVE.read_text(encoding='utf-8'));checks['five_cube_vertex_attachment_one']=five['cutoffs'][1]['vertices']-five['cutoffs'][0]['vertices']==1
text=PACKET.read_text(encoding='utf-8');checks['repeated_shell_scope_retained']='Repeated same-shell divided-power cells are outside this count' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.pyramid-cell-floor-sums.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'computed':computed,'five_cube_full_attachment':{'0':1,**delta},'checks':checks,'passed':all(checks.values()),'disposition':{'established':'prime-height floor sums reproduce all direct positive cell counts and path counts through 8085','prediction':'five-cube attachment at 165165 computed without full cell enumeration'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'five_attachment':result['five_cube_full_attachment'],'five_path_increment':sum(factorial(int(k))*v for k,v in delta.items())}));raise SystemExit(0 if result['passed'] else 1)
