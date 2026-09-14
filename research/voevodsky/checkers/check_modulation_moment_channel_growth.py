#!/usr/bin/env python3
"""Find minimal shell/scale moment-channel depth at finite cutoffs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/modulation_moment_channels_recover_large_cutoff_route_residue_20260912.md'
RESULT=ROOT/'research/voevodsky/results/modulation_moment_channel_growth.json'
def primes_upto(n):
 sieve=bytearray(b'\x01')*(n+1); sieve[:2]=b'\x00\x00'
 for p in range(2,int(n**.5)+1):
  if sieve[p]: sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if sieve[i]]
def graph(L):
 ps=primes_upto(L//2+2); E=[]
 for j,(p,q) in enumerate(zip(ps,ps[1:])):
  for k in range(1,L//(p*q)+1): E.append((k*p*q,j+1,k,k*p,k*q))
 E.sort(); V=sorted({e[3] for e in E}|{e[4] for e in E}); vi={v:i for i,v in enumerate(V)}; return E,V,vi
def rows(E,V,vi,code,mod):
 out=[{} for _ in V]
 for col,e in enumerate(E):
  d=code(e)%mod; a,b=vi[e[3]],vi[e[4]]; out[a][col]=(-d)%mod; out[b][col]=d
 return out
def rank_mod(rows_,p):
 basis={}
 for src in rows_:
  row={k:v%p for k,v in src.items() if v%p}
  while row:
   lead=min(row)
   if lead not in basis:
    inv=pow(row[lead],p-2,p); basis[lead]={k:(v*inv)%p for k,v in row.items() if (v*inv)%p}; break
   factor=row[lead]
   for k,v in basis[lead].items():
    nv=(row.get(k,0)-factor*v)%p
    if nv: row[k]=nv
    elif k in row: del row[k]
 return len(basis)
def depth(E,V,vi,index,mod,maxdepth=12):
 stacked=[]; ranks=[]
 for r in range(maxdepth+1):
  stacked += rows(E,V,vi,lambda e,rr=r:e[index]**rr,mod); rank=rank_mod(stacked,mod); ranks.append(rank)
  if rank==len(E): return r,ranks
 return None,ranks
cutoffs=(960,1920,3840,7680,15360,30720); moduli=(1000000007,1000000009); census={}; checks={}
for L in cutoffs:
 E,V,vi=graph(L); records=[]
 for mod in moduli:
  ds,rs=depth(E,V,vi,1,mod); dk,rk=depth(E,V,vi,2,mod); records.append({'modulus':mod,'shell_max_power':ds,'scale_max_power':dk,'shell_ranks':rs,'scale_ranks':rk})
 checks[f'shell_moments_recover_{L}']=all(r['shell_max_power'] is not None for r in records)
 checks[f'scale_moments_recover_{L}']=all(r['scale_max_power'] is not None for r in records)
 checks[f'moduli_agree_{L}']=len({(r['shell_max_power'],r['scale_max_power']) for r in records})==1
 census[str(L)]={'edges':len(E),'vertices':len(V),'records':records}
text=PACKET.read_text() if PACKET.exists() else ''
if text:
 checks['finite_axis_stated']='finite-cutoff theorem' in text
 checks['no_uniform_depth_promotion']='does not establish a cutoff-independent channel depth' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.modulation-moment-channel-growth-check.v1','input_digest':hashlib.sha256(PACKET.read_bytes()).hexdigest() if PACKET.exists() else None,'checks':checks,'passed':all(checks.values()),'census':census,'disposition':{'tested':'Vandermonde shell-index and scale moment channels','boundary':'finite modular full rank only'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'depths':{L:(x['records'][0]['shell_max_power'],x['records'][0]['scale_max_power']) for L,x in census.items()}})); raise SystemExit(0 if result['passed'] else 1)
