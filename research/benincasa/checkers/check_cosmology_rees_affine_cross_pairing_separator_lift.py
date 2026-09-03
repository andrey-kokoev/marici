#!/usr/bin/env python3
import contextlib,io,json,math,runpy
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve();h0=P.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(h0))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,T,B=g['H'],h['Q'],h['K'],h['target'],h['B'];O={(0,0):F(1)};R=mul(H,Q);c=F(17,839808)
def pw(a,n):
 r=O
 for _ in range(n):r=mul(r,a)
 return r
def M(f,z,k):
 p=2-k;C=F(-1,2)-k;Kp=K if p==1 else mul(K,K);Km=O if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),C));return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-4))
def solve(E,p,n):
 bs={}
 for S in E:
  a={j:v.numerator*pow(v.denominator,-1,p)%p for j,v in S.items() if v};a={j:v for j,v in a.items() if v}
  while a:
   q=min(a)
   if q==n:raise RuntimeError('inconsistent')
   if q not in bs:
    iv=pow(a[q],-1,p);bs[q]={j:v*iv%p for j,v in a.items()};break
   v=a[q]
   for j,x in bs[q].items():
    y=(a.get(j,0)-v*x)%p
    if y:a[j]=y
    elif j in a:del a[j]
 x=[0]*n
 for q in sorted(bs,reverse=True):x[q]=(-bs[q].get(n,0)-sum(v*x[j] for j,v in bs[q].items() if q<j<n))%p
 return x,tuple(bs)
def rr(x,m):
 B=math.isqrt(m//2);a,b=m,x%m;u,v=0,1
 while b>B:a,b,u,v=b,a-(a//b)*b,v,u-(a//b)*v
 return F(b,v) if b<=B and 0<abs(v)<=B and math.gcd(b,v)==1 and (b-x*v)%m==0 else None
def prime(q):
 if q<2:return False
 d=2
 while d*d<=q:
  if q%d==0:return False
  d+=1 if d==2 else 2
 return True
C=[]
for k,cap in ((1,33),(0,29)):
 for z in (0,1):
  for d in range(cap+1):
   for i in range(d+1):C.append(M({(i,d-i):F(1)},z,k))
u=mul(T,pw(R,4));v=mul(T,pw(R,5));q=add(u,sc(v,-c));mons=sorted(set(q)|{m for x in C for m in x},key=lambda x:(sum(x),x[0]));ix={m:i for i,m in enumerate(mons)};n=len(mons);E=[{ix[m]:a for m,a in x.items()} for x in C];E.append({**{ix[m]:a for m,a in q.items()},n:F(-1)});sp=P.parents[1]/'results'/'cosmology_rees_affine_cross_pairing_separator_crt.json'
if sp.exists():s=json.loads(sp.read_text());res=list(map(int,s['res']));mod=int(s['mod']);used=s['primes'];p=s['next']
else:res=[0]*n;mod=1;used=[];p=1000003
for _ in range(3):
 while not prime(p) or p in used:p+=1
 x,piv=solve(E,p,n);iv=pow(mod,-1,p)
 for i in range(n):res[i]+=mod*((x[i]-res[i])*iv%p)
 mod*=p;used.append(p);p+=1
sp.write_text(json.dumps({'res':list(map(str,res)),'mod':str(mod),'primes':used,'next':p+1})+'\n');lam=[rr(x,mod) for x in res]
if any(x is None for x in lam):print(json.dumps({'status':'checkpointed','primes':len(used),'unreconstructed':sum(x is None for x in lam)}));raise SystemExit
bad=sum(sum(a.get(m,F(0))*lam[i] for i,m in enumerate(mons))!=0 for a in C);pq=sum(q.get(m,F(0))*lam[i] for i,m in enumerate(mons))
if bad or pq!=1:print(json.dumps({'status':'checkpointed_after_failed_reconstruction','primes':len(used),'bad':bad,'pairing':str(pq)}));raise SystemExit
cert=[{'monomial':list(m),'coefficient':str(lam[i])} for i,m in enumerate(mons) if lam[i]];out={'schema':'marici.benincasa.cosmology-rees-affine-cross-pairing-separator.v1','columns':len(C),'equations':n,'support_size':len(cert),'relation_pairing':str(pq),'previous_target_pairing':str(sum(u.get(m,F(0))*lam[i] for i,m in enumerate(mons))),'current_target_pairing':str(sum(v.get(m,F(0))*lam[i] for i,m in enumerate(mons))),'certificate':cert};(P.parents[1]/'results'/'cosmology_rees_affine_cross_pairing_separator.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='certificate'},indent=2))
