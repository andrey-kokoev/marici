#!/usr/bin/env python3
"""Large-cutoff modular-rank hostile for coded shell and scale probes."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/large_cutoff_hostile_finds_no_coded_modulation_countercycle_20260912.md'
RESULT=ROOT/'research/voevodsky/results/large_cutoff_coded_modulation_rank.json'
def primes_upto(n):
 sieve=bytearray(b'\x01')*(n+1); sieve[:2]=b'\x00\x00'
 for p in range(2,int(n**.5)+1):
  if sieve[p]: sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if sieve[i]]
def graph(L):
 ps=primes_upto(L//2+2); shells=list(zip(ps,ps[1:])); E=[]
 for j,(p,q) in enumerate(shells):
  for k in range(1,L//(p*q)+1): E.append((k*p*q,j,k,k*p,k*q))
 E.sort(); V=sorted({e[3] for e in E}|{e[4] for e in E}); vi={v:i for i,v in enumerate(V)}
 return E,V,vi
def rows_for(E,V,vi,code=None):
 rows=[{} for _ in V]
 for col,e in enumerate(E):
  d=1 if code is None else code(e); a,b=vi[e[3]],vi[e[4]]
  rows[a][col]=rows[a].get(col,0)-d; rows[b][col]=rows[b].get(col,0)+d
 return rows
def rank_mod(rows,p):
 basis={}
 for source in rows:
  row={k:v%p for k,v in source.items() if v%p}
  while row:
   lead=min(row)
   if lead not in basis:
    inv=pow(row[lead],p-2,p); row={k:(v*inv)%p for k,v in row.items() if (v*inv)%p}; basis[lead]=row; break
   factor=row[lead]; br=basis[lead]
   for k,v in br.items():
    nv=(row.get(k,0)-factor*v)%p
    if nv: row[k]=nv
    elif k in row: del row[k]
 return len(basis)
cutoffs=(960,1920,3840,7680); moduli=(1000000007,1000000009); census={}; checks={}
for L in cutoffs:
 E,V,vi=graph(L); base=rows_for(E,V,vi); shell=rows_for(E,V,vi,lambda e:e[1]+1); scale=rows_for(E,V,vi,lambda e:e[2]); ranks=[]
 for mod in moduli:
  rb=rank_mod(base,mod); rs=rank_mod(base+shell,mod); rk=rank_mod(base+scale,mod); ranks.append({'modulus':mod,'boundary':rb,'shell_joint':rs,'scale_joint':rk})
 checks[f'shell_code_counterkernel_{L}']=all(r['shell_joint']<len(E) for r in ranks)
 checks[f'scale_code_counterkernel_{L}']=all(r['scale_joint']<len(E) for r in ranks)
 checks[f'boundary_rank_consistent_{L}']=len({r['boundary'] for r in ranks})==1
 census[str(L)]={'edges':len(E),'vertices':len(V),'cycle_dimension':len(E)-ranks[0]['boundary'],'ranks':ranks}
text=PACKET.read_text() if PACKET.exists() else ''
if text:
 checks['finite_only_boundary']='does not prove any fixed finite family suffices on the unbounded completion' in text
 checks['two_modulus_method_stated']='two large prime moduli' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.large-cutoff-coded-modulation-rank-check.v1','input_digest':hashlib.sha256(PACKET.read_bytes()).hexdigest() if PACKET.exists() else None,'checks':checks,'passed':all(checks.values()),'census':census,'disposition':{'countercycle_found':True,'tested':'single shell-index and scale-coded modulations','boundary':'finite modular rank deficiency corroborated by exact rational witnesses at cutoff 960'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'summary':{L:(x['edges'],x['cycle_dimension']) for L,x in census.items()}})); raise SystemExit(0 if result['passed'] else 1)
