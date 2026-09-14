#!/usr/bin/env python3
"""Floating source-side scout for K_sigma(0)-K_sigma(d); not a certificate."""
import cmath,json,math
from pathlib import Path
B2=(1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510)
def digamma(z):
 s=0j
 while abs(z)<12:s-=1/z;z+=1
 out=s+cmath.log(z)-1/(2*z)
 zp=z*z
 power=zp
 for k,b in enumerate(B2,1):out-=b/(2*k*power);power*=zp
 return out
def simpson(f,a,b,n):
 if n%2:n+=1
 h=(b-a)/n;s=f(a)+f(b)
 for i in range(1,n):s+=(4 if i%2 else 2)*f(a+i*h)
 return s*h/3
def mangoldt(N):
 out=[0.0]*(N+1);sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
 for p in range(2,N+1):
  if not sieve[p]:continue
  if p*p<=N:sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
  q=p
  while q<=N:out[q]=math.log(p);q*=p
 return out
def deficit(sigma,d,vm):
 t=2*sigma;pref=math.exp(-d*d/(4*t))
 endpoint=-math.exp(sigma/2)*(math.cosh(d/2)-1)
 c=-math.log(math.pi)/(4*math.sqrt(math.pi*t));gamma_const=c*(1-pref)
 U=max(12.0,math.sqrt(35/t));nquad=12000
 gamma_int=simpson(lambda u: math.exp(-t*u*u)*digamma(.25+.5j*u).real*(1-math.cos(d*u)),0,U,nquad)/(2*math.pi)
 C=1/(2*math.sqrt(math.pi*t));prime=0.0
 for n in range(2,len(vm)):
  if not vm[n]:continue
  L=math.log(n);p0=math.exp(-L*L/(4*t));pair=(math.exp(-(L-d)**2/(4*t))+math.exp(-(L+d)**2/(4*t)))/2
  prime+=vm[n]/math.sqrt(n)*(pair-p0)
 return endpoint+gamma_const+gamma_int+C*prime,{'endpoint':endpoint,'gamma_constant':gamma_const,'gamma_integral':gamma_int,'prime':C*prime}
def main():
 # log cutoff 14 makes omitted log-Gaussian terms negligible for scanned widths <=0.1.
 N=1200000;vm=mangoldt(N);rows=[]
 for sigma in (0.005,0.01,0.02,0.05,0.1):
  for d in (0.0625,0.1,0.125,0.1875,0.25,0.3125,0.375,0.4375,0.5,0.5625,0.625,0.6875,0.75,0.875,1.0,1.125,1.25,1.375,1.5,1.75,2.0,2.25,2.5,2.75,3.0):
   value,parts=deficit(sigma,d,vm);rows.append({'sigma':sigma,'d':d,'K0_minus_Kd':value,'parts':parts})
 minimum=min(rows,key=lambda r:r['K0_minus_Kd'])
 reliable=[r for r in rows if r['sigma']<=0.05];minimum_reliable=min(reliable,key=lambda r:r['K0_minus_Kd'])
 result={'schema':'marici.voevodsky.two-translate-weil-deficit-scout.v1','method':'direct endpoint+digamma-integral+von-Mangoldt source formula','prime_cutoff':N,'rows':rows,'minimum':minimum,'minimum_before_roundoff_regime':minimum_reliable,'negative_sample_found':minimum['K0_minus_Kd'] < -1e-10,'roundoff_threshold':1e-10,'certified':False,'next_gate':'Repeat the tightest positive cases with interval arithmetic and rigorous gamma-integral and prime-tail bounds.'}
 out=Path(__file__).parents[1]/'results'/'two_translate_weil_deficit_scout.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'minimum':minimum,'negative_sample_found':result['negative_sample_found']},indent=2))
if __name__=='__main__':main()
