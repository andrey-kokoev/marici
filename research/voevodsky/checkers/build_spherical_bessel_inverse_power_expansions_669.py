#!/usr/bin/env python3
"""Build exact inverse-power sine/cosine expansions through j_669."""
import json,hashlib
from pathlib import Path
N=670;S=[[0,1],[0,0,1]];C=[[0,0],[0,-1,0]]
def step(a,b,q):
 out=[0]*max(len(a)+1,len(b))
 for k,v in enumerate(a):out[k+1]+=q*v
 for k,v in enumerate(b):out[k]-=v
 while len(out)>1 and out[-1]==0:out.pop()
 return out
for n in range(1,N-1):S.append(step(S[n],S[n-1],2*n+1));C.append(step(C[n],C[n-1],2*n+1))
assert all(all(v==0 for k,v in enumerate(S[n]) if (k-n-1)%2) for n in range(N));assert all(all(v==0 for k,v in enumerate(C[n]) if (k-n)%2) for n in range(N))
payload={'schema':'marici.voevodsky.spherical-bessel-inverse-power-expansions.v1','identity':'j_n(x)=S_n(1/x)sin(x)+C_n(1/x)cos(x)','maximum_order':N-1,'S':S,'C':C};raw=json.dumps(payload,separators=(',',':')).encode();payload['coefficient_digest_sha256']=hashlib.sha256(raw).hexdigest();payload['passed']=True;payload['rh_proved']=False
p=Path(__file__).parents[1]/'results'/'spherical_bessel_inverse_power_expansions_669.json';p.write_text(json.dumps(payload,separators=(',',':'))+'\n');print(json.dumps({'maximum_order':669,'digest':payload['coefficient_digest_sha256'],'max_coefficient_digits':max(len(str(abs(v))) for row in S+C for v in row),'file_bytes':p.stat().st_size,'passed':True},indent=2))
