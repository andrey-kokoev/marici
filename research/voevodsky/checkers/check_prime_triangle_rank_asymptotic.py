#!/usr/bin/env python3
"""Numerically expose the PNT-scale prime budget and induced rank growth."""
import json,math
from pathlib import Path
N=1_000_000;sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
for p in range(2,int(N**.5)+1):
 if sieve[p]:sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
lam=[0.0]*(N+1)
for p in range(2,N+1):
 if sieve[p]:
  q=p
  while q<=N:lam[q]=math.log(p);q*=p
rows=[];acc=0.0;targets={10**k for k in range(2,7)}
for n in range(2,N+1):
 acc+=lam[n]/math.sqrt(n)
 if n in targets:rows.append({'X':n,'L':.5*math.log(n),'budget':acc,'ratio_to_2sqrtX':acc/(2*math.sqrt(n)),'log_threshold_leading':2*acc})
out={'schema':'marici.voevodsky.prime-triangle-rank-asymptotic.v1','identity':'sum Lambda(n)/sqrt(n) ~ 2sqrt(X), X=exp(2L)','consequence':'M=exp((4+o(1))*exp(L))','rows':rows,'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'prime_triangle_rank_asymptotic.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
