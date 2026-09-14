#!/usr/bin/env python3
"""Verify first global probe-depth thresholds through cubical dimension five."""
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/prime_shell_cube_completion_is_the_first_global_probe_depth_transition_through_dimension_five.md'
RESULT=ROOT/'research/voevodsky/results/global_probe_depth_thresholds_through_five.json'
MODS=(1000000007,1000000009);SETTINGS=((5,6),(3,4),(7,10),(2,3))

def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
def graph(L):
 ps=primes(L//2+2);e=[]
 for j,(p,q) in enumerate(zip(ps,ps[1:]),1):
  for k in range(1,L//(p*q)+1):e.append((k*p*q,j,k*p,k*q))
 e.sort();v=sorted({x[2] for x in e}|{x[3] for x in e});return e,v,{x:i for i,x in enumerate(v)}
def rows(e,v,vi,p,setting=None):
 out=[{} for _ in v];t=None if setting is None else setting[0]*pow(setting[1],p-2,p)%p
 for c,x in enumerate(e):
  w=1 if t is None else pow(t,x[1],p);out[vi[x[2]]][c]=-w%p;out[vi[x[3]]][c]=w
 return out
def rank(a,p):
 b={}
 for source in a:
  r={k:v%p for k,v in source.items() if v%p}
  while r:
   lead=min(r)
   if lead not in b:
    inv=pow(r[lead],p-2,p);b[lead]={k:v*inv%p for k,v in r.items() if v*inv%p};break
   q=r[lead]
   for k,v in b[lead].items():
    x=(r.get(k,0)-q*v)%p
    if x:r[k]=x
    else:r.pop(k,None)
 return len(b)
def deficiency(L,mods,p):
 e,v,vi=graph(L);a=rows(e,v,vi,p)
 for setting in SETTINGS[:mods]:a+=rows(e,v,vi,p,setting)
 return len(e)-rank(a,p),e

checks={};table={}
for n,L in ((2,45),(3,525)):
 records=[]
 for p in MODS:
  below,eb=deficiency(L-1,n-2,p);at,ea=deficiency(L,n-2,p);detected,_=deficiency(L,n-1,p)
  records.append({'modulus':p,'below':below,'at':at,'detected':detected})
  checks[f'n{n}_threshold_mod_{p}']=(below,at,detected)==(0,1,0)
  checks[f'n{n}_edge_inclusion_mod_{p}']=set(eb).issubset(set(ea))
 table[str(n)]=records
four=json.loads((ROOT/'research/voevodsky/results/grade_8085_four_cube_probe_depth.json').read_text(encoding='utf-8'))
five=json.loads((ROOT/'research/voevodsky/results/five_cube_probe_depth.json').read_text(encoding='utf-8'))
for n,data in ((4,four),(5,five)):
 if n==4:
  below=data['census']['8084']['ranks'];at=data['census']['8085']['ranks'];idx_low=1;idx_high=2
 else:
  below=data['cutoffs'][0]['moduli'];at=data['cutoffs'][1]['moduli'];idx_low=2;idx_high=3
 records=[]
 for a,b in zip(below,at):
  rec={'modulus':a['modulus'],'below':a['joint'][idx_low]['deficiency'],'at':b['joint'][idx_low]['deficiency'],'detected':b['joint'][idx_high]['deficiency']};records.append(rec);checks[f'n{n}_threshold_mod_{a["modulus"]}']=(rec['below'],rec['at'],rec['detected'])==(0,1,0)
 table[str(n)]=records
checks['four_cube_deletion_localized']=four['deletion_two_setting_deficiencies']['shell_4_735_1155']==[0,0]
checks['five_cube_deletion_localized']=five['deletion_three_setting_deficiencies']['shell_5_12705_15015']==[0,0]
text=PACKET.read_text(encoding='utf-8');checks['finite_scope_retained']='does not establish the analogous assertion in every dimension' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.global-probe-depth-thresholds-through-five.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'thresholds':table,'checks':checks,'passed':all(checks.values()),'disposition':{'established':'first global zero-one-zero probe-depth thresholds at canonical cube grades through n=5','residual':'general theorem or six-cube computation at grade 3318315'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'thresholds':table}));raise SystemExit(0 if result['passed'] else 1)
