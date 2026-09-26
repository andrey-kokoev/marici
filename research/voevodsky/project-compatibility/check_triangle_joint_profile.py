"""Exact rational fixtures for the energy/collinear leading profile.
General derivation and analytic scope: triangle-joint-profile.md.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
paths=[Path(__file__),HERE/'triangle-transverse-density.md',HERE/'triangle-collinear-obstruction.md',
 ROOT/'temp/arxiv-2408.16386-source/sections/applications.tex']
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def sqrt_exact(q):
    n,d=isqrt(q.numerator),isqrt(q.denominator)
    assert n*n==q.numerator and d*d==q.denominator
    return F(n,d)
before=inventory()
records=[]
for a in map(F,(1,2,3)):
 for b in map(F,(1,2,3)):
  for ratio in map(F,('1/4','1/2','3/4')):
    x=a*ratio;s=a-x;t=x+b;h=8*a*b*(a+b)
    A=b*s/(a*t);B=(a+b)/(2*s*t);alpha=a/(2*x*s)
    assert h/(4*a*a*t*t)==4*A*B
    lam_star=A/B
    assert lam_star==2*b*s*s/(a*(a+b))
    radical=sqrt_exact(h*lam_star)
    assert radical==4*b*s
    # Taylor jets from the actual squared lengths at w=E*lambda_star.
    dr=lam_star/(2*x);ds=lam_star/(2*s)
    dt=(lam_star-2*(a+b)*x/a-radical/a)/(2*t)
    assert 1+ds+dt==0 # q3/E vanishes at z=1
    assert 1+dr+ds==1+alpha*lam_star>0 # q23/E remains positive
    # Large-lambda overlap must recover the E0-first collinear coefficient.
    assert 1/(4*x*s*t*alpha*B)==s/(a*(a+b))
    records.append({'a':str(a),'b':str(b),'x':str(x),'lambda_star':str(lam_star),
      'D23_at_pinch':str(1+alpha*lam_star)})
jet_count=0
for a in map(F,(1,4,9)):
 b=a
 for ratio in map(F,('1/4','1/2','3/4')):
  x=a*ratio;s=a-x;t=x+b;h=8*a*b*(a+b)
  A=b*s/(a*t);B=(a+b)/(2*s*t)
  for root_lam in map(F,('1/3','1','2','3')):
   lam=root_lam**2;radical=sqrt_exact(h*lam)
   for z in map(F,('-1','0','1/2','1')):
    dr=lam/(2*x);ds=lam/(2*s)
    dt=(lam-2*(a+b)*x/a-radical*z/a)/(2*t)
    D3=A+B*lam-radical*z/(2*a*t)
    assert D3==1+ds+dt and D3>=0
    assert 1+dr+ds==1+a*lam/(2*x*s)
    assert (A+B*lam)**2-4*A*B*lam==(A-B*lam)**2
    jet_count+=1
# Density powers: F^epsilon, dw, and A_E contribute epsilon+1-2.
assert (F(0)+1-2,F(1))==(F(-1),F(1))
assert before==inventory()
report={'passed':True,'pinch_fixtures':records,'additional_jet_fixture_count':jet_count,
 'source_sha256':before,'source_unchanged':True,
 'chart':'0<x<a compactly; w=E*lambda; candidate real reduced family',
 'D23':'1+a*lambda/(2*x*(a-x))',
 'D3':'A+B*lambda-2*sqrt(A*B*lambda)*z',
 'A':'b*(a-x)/(a*(x+b))','B':'(a+b)/(2*(a-x)*(x+b))',
 'profile':'W=1/(4*x*(a-x)*(x+b)*D23*D3)',
 'pinch':'lambda=A/B, z=1',
 'formal_density_power':'E^(epsilon-1)',
 'profile_absolute_integrability_strip':'0<Re(epsilon)<1',
 'verification_boundary':'Exact rational jet/pinch/overlap fixtures only; general profile and integrability proof are written mathematics. No uniform finite-E integral asymptotic or physical cycle is certified.'}
(HERE/'triangle-joint-profile.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='pinch_fixtures'},indent=2))
