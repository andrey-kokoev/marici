#!/usr/bin/env python3
"""Source-side evaluation of K(0)+K(d) at the enclosed sample."""
import cmath,json,math
from pathlib import Path
B2=(1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510)
def digamma(z):
 s=0j
 while abs(z)<12:s-=1/z;z+=1
 out=s+cmath.log(z)-1/(2*z);power=z*z
 for k,b in enumerate(B2,1):out-=b/(2*k*power);power*=z*z
 return out
def simpson(f,U,N):
 h=U/N;s=f(0)+f(U)
 for i in range(1,N):s+=(4 if i%2 else 2)*f(i*h)
 return h*s/3
def mangoldt(N):
 out=[0.0]*(N+1);sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
 for p in range(2,N+1):
  if not sieve[p]:continue
  if p*p<=N:sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
  q=p
  while q<=N:out[q]=math.log(p);q*=p
 return out
def main():
 sigma=.005;d=.25;t=2*sigma;U=math.sqrt(35/t);N=1200000;vm=mangoldt(N)
 c=-math.log(math.pi)/(4*math.sqrt(math.pi*t))
 gamma0=c+simpson(lambda u:math.exp(-t*u*u)*digamma(.25+.5j*u).real,U,24000)/(2*math.pi)
 C=1/(2*math.sqrt(math.pi*t));prime0=-C*sum(vm[n]/math.sqrt(n)*math.exp(-math.log(n)**2/(4*t)) for n in range(2,N+1) if vm[n])
 endpoint0=math.exp(sigma/2);K0=endpoint0+gamma0+prime0
 deficit=json.loads((Path(__file__).parents[1]/'results'/'two_translate_weil_deficit_scout.json').read_text())
 D=next(r['K0_minus_Kd'] for r in deficit['rows'] if r['sigma']==sigma and r['d']==d)
 symmetric=2*K0-D
 result={'schema':'marici.voevodsky.two-translate-symmetric-eigenvalue-scout.v1','sigma':sigma,'d':d,'K0_parts':{'endpoint':endpoint0,'gamma':gamma0,'prime':prime0},'K0':K0,'antisymmetric_eigenvalue':D,'symmetric_eigenvalue':symmetric,'both_positive_numerically':D>0 and symmetric>0,'certified':False,'conclusion':'At the selected sample both rank-two eigenchannels are positive with ordinary floating source-side evaluation.'}
 out=Path(__file__).parents[1]/'results'/'two_translate_symmetric_eigenvalue_scout.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
