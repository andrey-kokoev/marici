#!/usr/bin/env python3
"""Parameterized dependency-free replay of a stored reduced order-two detector."""
import argparse,contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--certificate',required=True);ap.add_argument('--level1-cap',type=int,required=True);ap.add_argument('--level0-cap',type=int,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=g['H'],h['Q'],h['K'],h['target'],h['B'];one={(0,0):F(1)};R=mul(H,Q)
def pw(x,n):
 r=one
 for _ in range(n):r=mul(r,x)
 return r
def pf(s):
 x,y=s.split('/') if '/' in s else (s,'1');return F(int(x),int(y))
def M(f,z,kp):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c));return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-2))
cert_path=Path(a.certificate);cert_path=cert_path if cert_path.is_absolute() else HERE.parents[3]/cert_path
obj=json.loads(cert_path.read_text());lam={tuple(x['monomial']):pf(x['coefficient']) for x in obj['certificate_R4']};bad=0;count=0
for kp,cap in ((1,a.level1_cap),(0,a.level0_cap)):
 for z in (0,1):
  for d in range(cap+1):
   for i in range(d+1):
    q=M({(i,d-i):F(1)},z,kp);bad+=sum(lam.get(m,F(0))*v for m,v in q.items())!=0;count+=1
t3=mul(target,pw(R,3));t4=mul(target,pw(R,4));p3=sum(lam.get(m,F(0))*v for m,v in t3.items());p4=sum(lam.get(m,F(0))*v for m,v in t4.items());out={'schema':'marici.benincasa.transportable-representative-replay.v1','certificate':str(a.certificate),'caps':[a.level1_cap,a.level0_cap],'columns':count,'nonannihilated_columns':bad,'target_R3_pairing':str(p3),'target_R4_pairing':str(p4),'verified':bad==0 and p3!=0 and p4!=0};outp=Path(a.output);outp=outp if outp.is_absolute() else HERE.parents[3]/outp;outp.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
