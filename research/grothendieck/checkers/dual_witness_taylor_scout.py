"""High-precision source-only Taylor scout for the weakest frozen dual cell."""
import json,math
from pathlib import Path
import mpmath as mp
mp.mp.dps=60
TC=mp.mpf('.299');XC=mp.mpf('4.5025');HT=mp.mpf('.001');HX=mp.mpf('.0025');P=512
ALPHA=mp.mpf('6817744927666.86');BETA=mp.mpf('-997228471888.1238')
def primes(n):
 s=[True]*(n+1);s[0]=s[1]=False
 for p in range(2,math.isqrt(n)+1):
  if s[p]:
   for k in range(p*p,n+1,p):s[k]=False
 return [p for p in range(2,n+1) if s[p]]
terms=[]
for p in primes(P):
 n=p;lp=mp.log(p)
 while n<=P:terms.append((n,lp,mp.log(n)));n*=p
def ub(t,j):
 L=mp.log(P);return L**(j+1)/mp.sqrt(P)*mp.exp(-L*L/(4*t))+mp.quad(lambda y:y**(j+1)*mp.exp(y/2-y*y/(4*t)),[L,mp.inf])
def D(t,x):
 rt=mp.sqrt(t);c=1/(2*mp.sqrt(mp.pi*t));e=mp.exp(t/4-t*x*x)*mp.cos(t*x);e1=mp.exp(t/4-t*x*x)*(-2*t*x*mp.cos(t*x)-t*mp.sin(t*x));q0=mp.quad(lambda y:mp.exp(-y*y)*mp.re(mp.digamma(mp.mpf('.25')+.5j*(x+y/rt))),[-mp.inf,0,mp.inf]);q1=mp.quad(lambda y:y*mp.exp(-y*y)*mp.re(mp.digamma(mp.mpf('.25')+.5j*(x+y/rt))),[-mp.inf,0,mp.inf]);g0=-mp.log(mp.pi)/(4*mp.sqrt(mp.pi*t))+q0/(4*mp.pi*rt);g1=q1/(2*mp.pi);rp=mp.fsum(lp/mp.sqrt(n)*mp.exp(-ln*ln/(4*t))*mp.cos(x*ln) for n,lp,ln in terms);ip=mp.fsum(lp*ln/mp.sqrt(n)*mp.exp(-ln*ln/(4*t))*mp.sin(x*ln) for n,lp,ln in terms);rr=(e+g0)/c-rp;ii=-(e1+g1)/c-ip;u0=ub(t,0);u2=ub(t,2);return ALPHA*rr+BETA*ii-mp.sqrt(ALPHA**2*u0**2+BETA**2*u0*u2)
f00=D(TC,XC);ftp=D(TC+HT,XC);ftm=D(TC-HT,XC);fxp=D(TC,XC+HX);fxm=D(TC,XC-HX);fpp=D(TC+HT,XC+HX);fpm=D(TC+HT,XC-HX);fmp=D(TC-HT,XC+HX);fmm=D(TC-HT,XC-HX)
dt=(ftp-ftm)/(2*HT);dx=(fxp-fxm)/(2*HX);dtt=(ftp-2*f00+ftm)/HT**2;dxx=(fxp-2*f00+fxm)/HX**2;dtx=(fpp-fpm-fmp+fmm)/(4*HT*HX);quadratic_lower=f00-abs(dt)*HT-abs(dx)*HX-(abs(dtt)*HT**2+2*abs(dtx)*HT*HX+abs(dxx)*HX**2)/2
out={'schema':'marici.dual-witness-taylor-scout.v1','certified':False,'source_only':True,'center':[str(TC),str(XC)],'radii':[str(HT),str(HX)],'alpha':str(ALPHA),'beta':str(BETA),'center_margin':mp.nstr(f00,20),'derivatives':{'t':mp.nstr(dt,15),'xi':mp.nstr(dx,15),'tt':mp.nstr(dtt,15),'tx':mp.nstr(dtx,15),'xx':mp.nstr(dxx,15)},'quadratic_absolute_remainder_lower_scout':mp.nstr(quadratic_lower,20),'corner_margins':[mp.nstr(v,20) for v in (fmm,fmp,fpm,fpp)],'limitations':['finite differences do not certify derivative bounds','mpmath quadrature is not interval enclosed','tail majorant integral is numerical']};(Path(__file__).parents[1]/'results'/'dual-witness-taylor-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
