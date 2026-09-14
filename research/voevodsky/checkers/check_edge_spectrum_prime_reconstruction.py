#!/usr/bin/env python3
"""Reconstruct primes from ordered minimal edge-attachment grades."""
from hashlib import sha256
from math import gcd,isqrt
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/ordered_edge_attachment_spectrum_reconstructs_primes.md';RESULT=ROOT/'research/voevodsky/results/edge_spectrum_prime_reconstruction.json'
def primes_first(n):
 limit=10000
 while True:
  a=bytearray(b'\1')*(limit+1);a[:2]=b'\0\0'
  for p in range(2,isqrt(limit)+1):
   if a[p]:a[p*p:limit+1:p]=b'\0'*(((limit-p*p)//p)+1)
  ps=[i for i in range(2,limit+1) if a[i]]
  if len(ps)>=n:return ps[:n]
  limit*=2
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def reconstruct(spectrum):
 out=[2];failure=None
 for i,value in enumerate(spectrum,1):
  if value%out[-1]:failure={'position':i,'condition':'divisibility','value':value,'divisor':out[-1]};break
  q=value//out[-1]
  if not prime(q):failure={'position':i,'condition':'primality','candidate':q};break
  if q<=out[-1]:failure={'position':i,'condition':'strict_order','candidate':q};break
  out.append(q)
 if failure is None:
  for i in range(len(spectrum)-1):
   if gcd(spectrum[i],spectrum[i+1])!=out[i+1]:failure={'position':i+1,'condition':'neighbor_gcd'};break
 return out,failure
expected=primes_first(1001);spectrum=[a*b for a,b in zip(expected,expected[1:])];recovered,failure=reconstruct(spectrum)
gcd_recovered=[2]+[gcd(spectrum[i],spectrum[i+1]) for i in range(999)]+[spectrum[-1]//gcd(spectrum[-2],spectrum[-1])]
perturbations=[]
for j in range(200):
 altered=spectrum[:];altered[j]+=1;partial,error=reconstruct(altered);perturbations.append({'position':j+1,'detected':error is not None,'first_failure':error})
checks={'recursive_reconstruction':failure is None and recovered==expected,'gcd_reconstruction':gcd_recovered==expected,'all_recovered_prime':all(prime(p) for p in recovered),'all_200_perturbations_detected':all(x['detected'] for x in perturbations),'label_boundary_retained':'does not reconstruct primes from an unordered multiset' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.edge-spectrum-prime-reconstruction.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'spectrum_length':len(spectrum),'first_ten_spectrum_values':spectrum[:10],'last_reconstructed_prime':recovered[-1],'recovered_count':len(recovered),'perturbation_summary':{'tested':len(perturbations),'detected':sum(x['detected'] for x in perturbations),'failure_conditions':{k:sum(x['first_failure'] and x['first_failure']['condition']==k for x in perturbations) for k in ('divisibility','primality','strict_order','neighbor_gcd')}},'checks':checks,'passed':all(checks.values()),'disposition':{'theorem':'ordered minimal edge grades plus p1=2 reconstruct the ordered primes','interior_reconstruction':'adjacent gcds require no supplied interior labels','scope':'ordered spectrum, not unfiltered homotopy type'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'recovered_count':len(recovered),'last_prime':recovered[-1],'perturbations':result['perturbation_summary'],'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
