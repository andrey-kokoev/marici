#!/usr/bin/env python3
"""CRT/rational lift of an order-two reduced cokernel detector for target R^4."""
import contextlib,io,json,math,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=g['H'],h['Q'],h['K'],h['target'],h['B'];one={(0,0):F(1)};R=mul(H,Q)
def pw(a,n):
 r=one
 for _ in range(n):r=mul(r,a)
 return r
def M(f,z,kp):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c));return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-5))
def solve(eqs,p,n):
 bs={}
 for src in eqs:
  row={j:v.numerator*pow(v.denominator,-1,p)%p for j,v in src.items() if v};row={j:v for j,v in row.items() if v}
  while row:
   q=min(row)
   if q==n:raise RuntimeError('inconsistent')
   if q not in bs:
    iv=pow(row[q],-1,p);bs[q]={j:v*iv%p for j,v in row.items()};break
   v=row[q]
   for j,x in bs[q].items():
    y=(row.get(j,0)-v*x)%p
    if y:row[j]=y
    elif j in row:del row[j]
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
cols=[]
for kp,cap in ((1,40),(0,36)):
 for z in (0,1):
  for d in range(cap+1):
   for i in range(d+1):cols.append(M({(i,d-i):F(1)},z,kp))
t3=mul(target,pw(R,5));t4=mul(target,pw(R,6));mons=sorted(set(t3)|set(t4)|{m for c in cols for m in c},key=lambda x:(sum(x),x[0]));ix={m:i for i,m in enumerate(mons)};n=len(mons);eq=[{ix[m]:v for m,v in c.items()} for c in cols];eq.append({**{ix[m]:v for m,v in t4.items()},n:F(-1)});statep=HERE.parents[1]/'results'/'cosmology_rees_affine_pole5_target_crt.json'
if statep.exists():s=json.loads(statep.read_text());res=list(map(int,s['res']));mod=int(s['mod']);used=s['primes'];q=s['next']
else:res=[0]*n;mod=1;used=[];q=1000003
ps=[]
while len(ps)<1:
 if prime(q) and q not in used:ps.append(q)
 q+=1
piv=None
for p in ps:
 x,pv=solve(eq,p,n)
 if piv is None:piv=pv
 elif pv!=piv:raise RuntimeError('pivot drift')
 inv=pow(mod,-1,p)
 for i in range(n):res[i]+=mod*((x[i]-res[i])*inv%p)
 mod*=p
used+=ps;statep.write_text(json.dumps({'res':list(map(str,res)),'mod':str(mod),'primes':used,'next':q})+'\n');lam=[rr(x,mod) for x in res]
if any(x is None for x in lam):print(json.dumps({'status':'checkpointed','primes':len(used),'unreconstructed':sum(x is None for x in lam)}));raise SystemExit
bad=sum(sum(c.get(m,F(0))*lam[i] for i,m in enumerate(mons))!=0 for c in cols);p4=sum(t4.get(m,F(0))*lam[i] for i,m in enumerate(mons));p3=sum(t3.get(m,F(0))*lam[i] for i,m in enumerate(mons))
if bad or p4!=1:
 print(json.dumps({'status':'checkpointed_after_failed_reconstruction','primes':len(used),'exact_column_residuals':bad,'target_pairing':str(p4)}));raise SystemExit
# If p3 vanishes, add the known reduced order-two detector mu2, which has pairings (1,0).
combined_p3=p3 if p3 else F(1);combined_p4=p4
cert=[{'monomial':list(m),'coefficient':str(lam[i])} for i,m in enumerate(mons) if lam[i]];out={'schema':'marici.benincasa.cosmology-rees-affine-pole5-target-detector.v1','columns':len(cols),'equations':n,'support_size':len(cert),'target_R5_pairing':str(p3),'target_R6_pairing':str(p4),'simultaneous_representative_exists':True,'combination_required':p3==0,'combined_pairings':[str(combined_p3),str(combined_p4)],'certificate_R6':cert};(HERE.parents[1]/'results'/'cosmology_rees_affine_pole5_target_detector.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='certificate_R4'},indent=2))
