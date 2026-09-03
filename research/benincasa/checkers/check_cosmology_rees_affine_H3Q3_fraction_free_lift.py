#!/usr/bin/env python3
"""Dependency-free modular/CRT/rational lift for H^3Q^3."""
import contextlib,io,json,math,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_affine_localized_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=h['H'],h['Q'],h['K'],h['target'],h['B']
def Lnum(f,z,kp,D):
 p=2-kp;c=F(-1,2)-kp;one={(0,0):F(1)};Kp=K if p==1 else mul(K,K);Km=one if p==1 else K
 return add(mul(Kp,add(mul(D,B(f,z)),sc(mul(mul(Q,f),der(D,z)),-1))),sc(mul(mul(mul(Km,Q),mul(der(K,z),f)),D),c))
def solve_mod(eqs,p,n):
 basis={}
 for src in eqs:
  row={j:(v.numerator*pow(v.denominator,-1,p))%p for j,v in src.items() if v};row={j:v for j,v in row.items() if v}
  while row:
   q=min(row)
   if q==n:raise RuntimeError('inconsistent certificate equations')
   if q not in basis:
    iv=pow(row[q],-1,p);basis[q]={j:v*iv%p for j,v in row.items()};break
   v=row[q]
   for j,x in basis[q].items():
    y=(row.get(j,0)-v*x)%p
    if y:row[j]=y
    elif j in row:del row[j]
 sol=[0]*n
 for q in sorted(basis,reverse=True):
  row=basis[q];sol[q]=(-row.get(n,0)-sum(v*sol[j] for j,v in row.items() if q<j<n))%p
 return sol,tuple(basis)
def ratrec(x,m):
 B=math.isqrt(m//2);r0,r1=m,x%m;t0,t1=0,1
 while r1>B:r0,r1,t0,t1=r1,r0-(r0//r1)*r1,t1,t0-(r0//r1)*t1
 if r1<=B and abs(t1)<=B and t1 and math.gcd(r1,t1)==1 and (r1-x*t1)%m==0:return F(r1,t1)
 return None
def isprime(q):
 if q<2:return False
 d=2
 while d*d<=q:
  if q%d==0:return False
  d+=1 if d==2 else 2
 return True
D=mul(mul(mul(H,H),H),mul(mul(Q,Q),Q));cols=[]
for kp,maxd in ((1,26),(0,22)):
 for z in (0,1):
  for d in range(maxd+1):
   for i in range(d+1):cols.append(Lnum({(i,d-i):F(1)},z,kp,D))
tgt=mul(target,mul(D,D));mons=sorted(set(tgt)|{m for c in cols for m in c},key=lambda x:(sum(x),x[0]));idx={m:i for i,m in enumerate(mons)};n=len(mons);eq=[{idx[m]:v for m,v in c.items()} for c in cols];eq.append({**{idx[m]:v for m,v in tgt.items()},n:F(-1)})
state_path=HERE.parents[1]/'results'/'cosmology_rees_affine_H3Q3_crt_checkpoint.json'
if state_path.exists():state=json.loads(state_path.read_text());res=[int(x) for x in state['residues']];M=int(state['modulus']);used=state['primes'];q=state['next_start']
else:res=[0]*n;M=1;used=[];q=1000003
primes=[]
while len(primes)<3:
 if isprime(q) and q not in used:primes.append(q)
 q+=1
piv=None
for p in primes:
 s,ps=solve_mod(eq,p,n)
 if piv is None:piv=ps
 elif ps!=piv:raise RuntimeError('pivot drift')
 inv=pow(M,-1,p)
 for i in range(n):res[i]+=M*((s[i]-res[i])*inv%p)
 M*=p
used+=primes;state_path.write_text(json.dumps({'modulus':str(M),'residues':[str(x) for x in res],'primes':used,'next_start':q})+'\n');lam=[ratrec(x,M) for x in res]
if any(x is None for x in lam):print(json.dumps({'status':'checkpointed','prime_count':len(used),'crt_digits':len(str(M)),'unreconstructed':sum(x is None for x in lam)}));raise SystemExit(0)
assert all(sum(c.get(m,F(0))*lam[i] for i,m in enumerate(mons))==0 for c in cols);pair=sum(tgt.get(m,F(0))*lam[i] for i,m in enumerate(mons));assert pair==1
cert=[{'monomial':[m[0],m[1]],'coefficient':str(lam[i])} for i,m in enumerate(mons) if lam[i]];out={'schema':'marici.benincasa.cosmology-rees-affine-H3Q3-exact-certificate.v1','denominator':'H^3Q^3','numerator_caps':[26,22],'unknowns':len(cols),'equations':n,'primes':used,'crt_modulus':str(M),'support_size':len(cert),'target_pairing':str(pair),'certificate':cert};(HERE.parents[1]/'results'/'cosmology_rees_affine_H3Q3_exact_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='certificate'},indent=2))
