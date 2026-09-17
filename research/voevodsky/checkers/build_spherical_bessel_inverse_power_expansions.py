#!/usr/bin/env python3
"""Build exact j_n(x)=S_n(1/x)sin(x)+C_n(1/x)cos(x), n<=79."""
import json,hashlib
from pathlib import Path
N=80
# Dense integer coefficient lists indexed by inverse power.
S=[[0,1]];C=[[0,0]]
S.append([0,0,1]);C.append([0,-1,0])
def add_scaled_shift(a,b,scale):
 m=max(len(a)+1,len(b));out=[0]*m
 for k,v in enumerate(a):out[k+1]+=scale*v
 for k,v in enumerate(b):out[k]-=v
 while len(out)>1 and out[-1]==0:out.pop()
 return out
for n in range(1,N-1):
 S.append(add_scaled_shift(S[n],S[n-1],2*n+1));C.append(add_scaled_shift(C[n],C[n-1],2*n+1))
# Recurrence and parity structure checks.
assert all(all(v==0 for k,v in enumerate(S[n]) if (k-n-1)%2) for n in range(N))
assert all(all(v==0 for k,v in enumerate(C[n]) if (k-n)%2) for n in range(N))
for n in range(1,N-1):
 assert S[n+1]==add_scaled_shift(S[n],S[n-1],2*n+1)
 assert C[n+1]==add_scaled_shift(C[n],C[n-1],2*n+1)
payload={'schema':'marici.voevodsky.spherical-bessel-inverse-power-expansions.v1','identity':'j_n(x)=sum_k S[n][k] x^-k sin(x)+sum_k C[n][k] x^-k cos(x)','maximum_order':N-1,'S':S,'C':C}
raw=json.dumps(payload,separators=(',',':')).encode();payload['coefficient_digest_sha256']=hashlib.sha256(raw).hexdigest();payload['checks']={'three_term_recurrence':True,'parity_support':True,'integer_coefficients':True};payload['passed']=True;payload['rh_proved']=False
p=Path(__file__).parents[1]/'results'/'spherical_bessel_inverse_power_expansions.json';p.write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps({'maximum_order':79,'digest':payload['coefficient_digest_sha256'],'max_coefficient_digits':max(len(str(abs(v))) for row in S+C for v in row),'passed':True},indent=2))
