"""Exact leading-jet fixtures for the E=0 collinear stratum.
These fixtures check arithmetic; the general interval proof is in the note.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
paths=[Path(__file__),HERE/'triangle-transverse-density.md',ROOT/'temp/arxiv-2408.16386-source/sections/applications.tex']
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=inventory()
def product(*terms):
    degree=0;coefficient=F(1)
    for d,c in terms:degree+=d;coefficient*=c
    return degree,coefficient
def inverse(term):return -term[0],1/term[1]
def summation(*terms):
    degree=min(d for d,c in terms)
    coefficient=sum(c for d,c in terms if d==degree)
    assert coefficient>0 # all terms positive: no hidden cancellation
    return degree,coefficient
def jet(value,slope):
    assert value>=0 and slope>0
    return (0,value) if value else (1,slope)
records=[]
for a in map(F,(1,2,3)):
 for b in map(F,(1,2,3)):
  for x in (-b-1,-3*b/4,-b/4,a/4,3*a/4,a+1):
    r,s,t=abs(x),abs(x-a),abs(x+b)
    dr,ds,dt=1/(2*r),1/(2*s),1/(2*t)
    q1=jet(r+a+s,dr+ds);q2=jet(r+b+t,dr+dt)
    q3=jet(s+t-a-b,ds+dt)
    q12=jet(a+b+s+t,ds+dt)
    q23=jet(r+s-a,dr+ds);q31=jet(r+t-b,dr+dt)
    bracket=summation(product(inverse((0,r)),summation(inverse(q23),inverse(q31))),
        product(inverse((0,t)),summation(inverse(q31),inverse(q12))),
        product(inverse((0,s)),summation(inverse(q12),inverse(q23))))
    result=product(bracket,inverse(q1),inverse(q2),inverse(q3))
    if 0<x<a:
        assert result==(-2,(a-x)/(a*(a+b)))
        zeros=['q3','q23']
    elif -b<x<0:
        assert result==(-2,(b+x)/(b*(a+b)))
        zeros=['q3','q31']
    else:
        assert result[0]==0
        zeros=[]
    records.append({'a':str(a),'b':str(b),'x':str(x),'vanishing':zeros,
        'w_order':result[0],'leading_coefficient':str(result[1])})
assert before==inventory()
report={'passed':True,'fixture_count':len(records),'source_sha256':before,'source_unchanged':True,
 'coordinate':'w=rho^2; E=0 first; x excludes -b,0,a',
 'interior_density':'w^(epsilon-2) times a nonzero smooth coefficient',
 'absolute_integrability':'Re(epsilon)>1 on compact subintervals of (-b,0) or (0,a)',
 'scope':'exact rational leading-jet fixtures, not a proof of joint E,w asymptotics or analytic regularization',
 'fixtures':records}
(HERE/'triangle-collinear.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='fixtures'},indent=2))
