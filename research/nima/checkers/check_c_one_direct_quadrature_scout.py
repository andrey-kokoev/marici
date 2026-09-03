"""Independent high-precision c=1 direct-quadrature scout with the post-support f(0) tail."""
import json, mpmath as mp
mp.mp.dps=60
A=2*mp.log(2)
BASE=[mp.mpf(1),-5,mp.mpf(33)/4,-5,1]; BM=[2,1,0,-1,-2]
CROSS=[mp.mpf(1)/2,-mp.mpf(5)/2,mp.mpf(37)/8,-5,mp.mpf(37)/8,-mp.mpf(5)/2,mp.mpf(1)/2]; CM=[3,2,1,0,-1,-2,-3]
def k7(x): return sum((-1)**j*mp.binomial(8,j)*max(mp.mpf(0),x+4-j)**7/mp.factorial(7) for j in range(9))
def profile(x,C,M): return sum(c*k7(x+m*A) for c,m in zip(C,M))
def primes(n):
 out=[]
 for p in range(2,n+1):
  if all(p%d for d in range(2,int(p**.5)+1)):out.append(p)
 return out
def prime(C,M,sign=-1):
 s=mp.mpf(0)
 for p in primes(1024):
  q=p
  while q<=1024:
   s += sign*2*mp.log(p)/mp.sqrt(q)*profile(mp.log(q),C,M);q*=p
 return s
def arch(C,M):
 f0=profile(0,C,M)
 def integrand(x): return (f0*mp.e**(-x)-profile(x,C,M)*mp.e**(-x/4))/(1-mp.e**(-x))
 top=max(-min(M)*A+4,1)
 knots=sorted({mp.mpf('1e-12')}|{max(mp.mpf('1e-12'),-m*A-4+j) for m in M for j in range(9) if 0<-m*A-4+j<top})
 finite=mp.quad(integrand,knots+[top])
 surviving_f0_tail=-f0*mp.log(1-mp.e**(-top))
 return -(mp.euler+mp.log(mp.pi))*f0+finite+surviving_f0_tail
def value(C,M,sign=-1): return arch(C,M)+prime(C,M,sign)
d=value(BASE,BM);c=value(CROSS,CM);wrong=value(CROSS,CM,1);det=d*d-c*c
assert d>0 and det>0 and d+c>0 and d-c>0
print(json.dumps({'schema':'marici.nima.c-one-direct-quadrature-scout.v2','status':'passed','baseline':mp.nstr(d,18),'cross':mp.nstr(c,18),'determinant':mp.nstr(det,18),'coherent':mp.nstr(d+c,18),'disagreement':mp.nstr(d-c,18),'prime_sign_failure_cross':mp.nstr(wrong,18),'positive_definite':True,'tail_repair':'included exact surviving f(0) tail beyond profile support','quadrature':'direct digamma-integral representation; no signed-atomic tail'},sort_keys=True))
