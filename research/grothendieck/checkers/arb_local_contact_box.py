"""Arb enclosure for the numerically weakest P=512 residual-island cell.

Finite y quadrature is rigorous by interval rectangles. The reported status is
conditional on the separately stated digamma Gaussian-tail and all-integer
moment-majorant constants.
"""
import json, math
from pathlib import Path
from flint import arb, acb, ctx
ctx.dps=60
T=arb('0.298','0.001'); X=arb('5.35','0.0025'); P=512; Y=arb(8); H=arb('0.02')
U0=arb('1.3e-13'); U2=arb('5e-12')
# Candidate bound for omitted |y|>8 gamma integrals, pending analytic lemma.
GTAIL=arb('1e-27')

def primes(n):
 s=[True]*(n+1);s[0]=s[1]=False
 for p in range(2,math.isqrt(n)+1):
  if s[p]:
   for q in range(p*p,n+1,p):s[q]=False
 return [p for p in range(2,n+1) if s[p]]
terms=[]
for p in primes(P):
 n=p;lp=arb(p).log()
 while n<=P:
  terms.append((n,lp,arb(n).log()))
  n*=p
rootpi=arb.pi().sqrt(); rootT=T.sqrt(); c=1/(2*rootpi*rootT)
e= (T/4-T*X*X).exp()*(T*X).cos()
e1=(T/4-T*X*X).exp()*(-2*T*X*(T*X).cos()-T*(T*X).sin())
rp=arb(0);ip=arb(0)
for n,lp,ln in terms:
 w=lp/arb(n).sqrt()*(-(ln*ln)/(4*T)).exp();rp+=w*(X*ln).cos();ip+=w*ln*(X*ln).sin()
# Interval-rectangle quadrature on [-8,8].
s0=arb(0);s1=arb(0);k=-400
while k<400:
 y=arb(str((k+.5)*.02),'.01');u=X+y/rootT;z=acb(arb('.25'),u/2);q=z.digamma().real;ga=(-y*y).exp();s0+=ga*q*H;s1+=ga*y*q*H;k+=1
g0=-arb.pi().log()/(4*rootpi*rootT)+s0/(4*arb.pi()*rootT)+arb(0,GTAIL)
g1=s1/(2*arb.pi())+arb(0,GTAIL)
rr=(e+g0)/c-rp;ii=-(e1+g1)/c-ip

def loabs(v):
 lo=float(v.lower());hi=float(v.upper())
 return 0.0 if lo<=0<=hi else min(abs(lo),abs(hi))
margin_lower=loabs(rr)**2/float(U0.upper())**2+loabs(ii)**2/(float(U0.upper())*float(U2.upper()))-1
out={'schema':'marici.arb-local-contact-box.v1','status':'conditional_certificate' if margin_lower>0 else 'not_excluded','box':{'t_mid':.298,'t_radius':.001,'xi_mid':5.35,'xi_radius':.0025},'prefix':P,'exact_terms':len(terms),'required_tail_R_interval':str(rr),'required_tail_I1_interval':str(ii),'tail_M0_upper':str(U0),'tail_M2_upper':str(U2),'margin_lower':margin_lower,'conditions':['prove |y|>8 digamma Gaussian value/slope contribution <=1e-27','prove all-integer tail M0<=1.3e-13 and M2<=5e-12 throughout t<=.299'],'method':'Arb interval rectangles on |y|<=8 plus exact Arb finite prefix'}
(Path(__file__).parents[1]/'results'/'arb-local-contact-box.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
