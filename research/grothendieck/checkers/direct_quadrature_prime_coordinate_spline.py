"""Scout the alternative repair retaining prime-side spline coordinate."""
import json, math
from pathlib import Path
import mpmath as mp
mp.mp.dps=60
BASE=[mp.mpf(1),-5,mp.mpf(33)/4,-5,1]; BASE_M=[2,1,0,-1,-2]
CROSS=[mp.mpf(1)/2,-mp.mpf(5)/2,mp.mpf(37)/8,-5,mp.mpf(37)/8,-mp.mpf(5)/2,mp.mpf(1)/2]; CROSS_M=[3,2,1,0,-1,-2,-3]
def lag_coeff(k):
 values={m:c for m,c in zip(BASE_M,BASE)}
 ms=list(range(2+k,-3-k,-1))
 return [mp.mpf('0.5')*(values.get(m-k,0)+values.get(m+k,0)) for m in ms],ms
LAG2,LAG2_M=lag_coeff(2);LAG3,LAG3_M=lag_coeff(3);LAG4,LAG4_M=lag_coeff(4)
a=2*mp.log(2)
def k7(u): return sum((-1)**j*math.comb(8,j)*max(u+4-j,mp.mpf('0'))**7/mp.factorial(7) for j in range(9))
def f(x,cs,ms): return sum(c*k7(x+m*a) for c,m in zip(cs,ms))
def pp(limit):
 for p in range(2,limit+1):
  if all(p%d for d in range(2,int(math.sqrt(p))+1)):
   q=p
   while q<=limit: yield p,q;q*=p
def ev(cs,ms):
 f0=f(0,cs,ms)
 def it(x):
  if abs(x)<mp.mpf('1e-30'): x=mp.mpf('1e-30')
  return (f0*mp.exp(-x)-f(x,cs,ms)*mp.exp(-x/4))/(1-mp.exp(-x))
 knots=sorted(set([mp.mpf('0')]+[max(mp.mpf('0'),4-m*a) for m in ms]+[max(mp.mpf('0'),m*a+4) for m in ms]));knots=[x for x in knots if x>0]
 arch=-(mp.euler+mp.log(mp.pi))*f0+mp.quad(it,[0,*knots,mp.inf])
 limit=int(mp.ceil(mp.exp(4-min(ms)*a)))
 prime=sum(-2*mp.log(p)/mp.sqrt(q)*f(mp.log(q),cs,ms) for p,q in pp(limit))
 return arch,prime,arch+prime,limit
rows={}
for name,cs,ms in [('baseline',BASE,BASE_M),('cross',CROSS,CROSS_M),('lag2_cross',LAG2,LAG2_M),('lag3_cross',LAG3,LAG3_M),('lag4_cross',LAG4,LAG4_M)]:
 x=ev(cs,ms);rows[name]={'arch':mp.nstr(x[0],30),'prime':mp.nstr(x[1],30),'total':mp.nstr(x[2],30),'prime_power_limit':x[3]}
lags=[mp.mpf(rows[name]['total']) for name in ['baseline','cross','lag2_cross','lag3_cross','lag4_cross']]
def toeplitz(rank):return mp.matrix([[lags[abs(i-j)] for j in range(rank)] for i in range(rank)])
d,c,c2=lags[:3];eigs=mp.eigsy(toeplitz(3),eigvals_only=True);eigs4=mp.eigsy(toeplitz(4),eigvals_only=True);eigs5=mp.eigsy(toeplitz(5),eigvals_only=True)
r={'schema':'marici.grothendieck.direct-quadrature-prime-coordinate-spline.v1','coordinate':'f(x)=profile(x); prime f(log q)','rows':rows,'two_translate':{'determinant':mp.nstr(d*d-c*c,30),'coherent_eigenvalue':mp.nstr(d+c,30),'disagreement_eigenvalue':mp.nstr(d-c,30)},'three_translate':{'lag2_cross':mp.nstr(c2,30),'eigenvalues':[mp.nstr(x,30) for x in eigs]},'four_translate':{'lag3_cross':mp.nstr(lags[3],30),'eigenvalues':[mp.nstr(x,30) for x in eigs4]},'five_translate':{'lag4_cross':mp.nstr(lags[4],30),'eigenvalues':[mp.nstr(x,30) for x in eigs5]},'claim_boundary':'High-precision scout, not interval certificate.'}
(Path(__file__).parents[1]/'results/direct-quadrature-prime-coordinate-spline.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
