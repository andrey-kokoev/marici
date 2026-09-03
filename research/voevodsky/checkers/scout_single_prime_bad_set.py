from __future__ import annotations
import cmath, json, math
B=[1/6,-1/30,1/42,-1/30,5/66,-691/2730]
def psi(z):
 s=0j
 while abs(z)<12: s-=1/z; z+=1
 v=cmath.log(z)-1/(2*z)
 for k,b in enumerate(B,1): v-=b/(2*k*z**(2*k))
 return v+s
def mg(u): return (psi(complex(.25,u/2)).real-math.log(math.pi))/(4*math.pi)
def root_level(level):
 lo,hi=0.,30.
 for _ in range(150):
  m=(lo+hi)/2
  if mg(math.exp(m))<level: lo=m
  else: hi=m
 return math.exp(hi)
def isolate(delta,L):
 c=math.log(2)/math.sqrt(2); a=math.log(2); U=root_level(c+delta)
 step=math.pi/(16*a); roots=[]
 def f(u): return mg(u)-c*math.cos(a*u)-delta
 x=0.; fx=f(x); bad=fx<0; start=0. if bad else None
 while x<U:
  y=min(U,x+step); fy=f(y)
  if (fx<0)!=(fy<0):
   lo,hi=x,y
   for _ in range(55):
    mid=(lo+hi)/2
    if (f(lo)<0)==(f(mid)<0): lo=mid
    else: hi=mid
   r=(lo+hi)/2; roots.append(r)
  x,fx=y,fy
 intervals=[]; points=[0.]+roots+[U]
 for p,q in zip(points,points[1:]):
  if f((p+q)/2)<0: intervals.append((p,q))
 Wpos=sum(q-p for p,q in intervals); Npos=len(intervals)
 W=2*Wpos; N=2*Npos-1 if intervals and intervals[0][0]==0 else 2*Npos
 Cminus=(0.5772156649015329+math.pi/2+3*math.log(2)+math.log(math.pi))/(4*math.pi)+c
 eta=delta/(delta+Cminus); trace=L*W/math.pi
 if L*W>=N: D=N*N/math.pi**2*(3+2*math.log(L*W/N))
 else: D=(4*L*W*N-L*L*W*W)/math.pi**2
 return {"delta":delta,"cutoff":U,"components":N,"measure":W,"trace":trace,
         "transition_bound":D,"dimension_bound":trace+D/eta}
def main():
 L=.35; rows=[isolate(d,L) for d in [.02,.05,.1,.2]]; best=min(rows,key=lambda r:r['dimension_bound'])
 print(json.dumps({"schema":"marici.voevodsky.single-prime-bad-set-scout.v1","status":"nonrigorous_single_prime_root_isolation_scout","L":"7/20","included_prime_powers":[2],"rows":rows,"best":best,"directed_interval_certified":False,"rh_implication":False,"passed":True},indent=2,sort_keys=True))
if __name__=='__main__': main()
