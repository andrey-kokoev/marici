#!/usr/bin/env python3
"""Source-side Fejer scout with rank growing to preserve physical span."""
import cmath,json,math
from pathlib import Path
B2=(1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510)
def digamma(z):
 s=0j
 while abs(z)<12:s-=1/z;z+=1
 out=s+cmath.log(z)-1/(2*z);power=z*z
 for k,b in enumerate(B2,1):out-=b/(2*k*power);power*=z*z
 return out
def simpson(f,U,N=12000):
 h=U/N;s=f(0)+f(U)
 for i in range(1,N):s+=(4 if i%2 else 2)*f(i*h)
 return h*s/3
def prime_terms(N=1200000):
 vm=[0.0]*(N+1);sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
 for p in range(2,N+1):
  if not sieve[p]:continue
  if p*p<=N:sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
  q=p
  while q<=N:vm[q]=math.log(p);q*=p
 return [(math.log(n),vm[n]/math.sqrt(n)) for n in range(2,N+1) if vm[n]]
def kernel(sigma,d,terms):
 t=2*sigma;pref=math.exp(-d*d/(4*t));E=math.exp(sigma/2)*math.cosh(d/2);c=-math.log(math.pi)/(4*math.sqrt(math.pi*t))*pref;U=max(12,math.sqrt(35/t))
 G=simpson(lambda u:math.exp(-t*u*u)*digamma(.25+.5j*u).real*math.cos(d*u),U)/(2*math.pi)
 C=1/(2*math.sqrt(math.pi*t));P=-C*sum(w*(math.exp(-(L-d)**2/(4*t))+math.exp(-(L+d)**2/(4*t)))/2 for L,w in terms)
 return E+c+G+P
def fejer(k,N,x):return k[0]+2*sum((1-m/N)*k[m]*math.cos(m*x) for m in range(1,N))
def main():
 sigma=.005;terms=prime_terms();schedules=[(.25,13),(.125,25),(.0625,49)];rows=[];mesh=1048576
 for h,N in schedules:
  k=[kernel(sigma,m*h,terms) for m in range(N)];best=(float('inf'),0)
  for j in range(mesh):
   x=2*math.pi*j/mesh;v=fejer(k,N,x)
   if v<best[0]:best=(v,x)
  deriv=2*sum((1-m/N)*m*abs(k[m]) for m in range(1,N));interp=deriv*math.pi/mesh
  coefficient_error=1e-6+4e-6*sum(1-m/N for m in range(1,N))
  rows.append({'h':h,'N':N,'physical_span':h*(N-1),'mesh_minimum':best[0],'angle':best[1],'interpolation_error':interp,'coefficient_error':coefficient_error,'conditional_global_lower':best[0]-interp-coefficient_error})
 result={'schema':'marici.voevodsky.fixed-span-fejer-refinement.v1','sigma':sigma,'rows':rows,'rank_scales_inverse_to_spacing':True,'all_mesh_global_lowers_positive':all(r['conditional_global_lower']>0 for r in rows),'coefficient_errors_included':True,'certified':False,'conclusion':'This is the correctly scaled finite refinement experiment; unlike fixed rank, it preserves a nonzero real-line observation span.'}
 out=Path(__file__).parents[1]/'results'/'fixed_span_fejer_refinement.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
