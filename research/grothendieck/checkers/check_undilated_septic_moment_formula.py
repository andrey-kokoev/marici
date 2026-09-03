"""Numerical identity check for the direct c=1 finite gamma moment formula."""
import json, math
from pathlib import Path
import mpmath as mp
mp.mp.dps=70
a=2*mp.log(2)
BASE=[mp.mpf(1),-5,mp.mpf(33)/4,-5,1]; BASE_M=[2,1,0,-1,-2]
CROSS=[mp.mpf(1)/2,-mp.mpf(5)/2,mp.mpf(37)/8,-5,mp.mpf(37)/8,-mp.mpf(5)/2,mp.mpf(1)/2]; CROSS_M=[3,2,1,0,-1,-2,-3]
def lag_coeff(k):
 values={m:c for m,c in zip(BASE_M,BASE)};ms=list(range(2+k,-3-k,-1))
 return [mp.mpf('0.5')*(values.get(m-k,0)+values.get(m+k,0)) for m in ms],ms
LAG2,LAG2_M=lag_coeff(2);LAG3,LAG3_M=lag_coeff(3)
def k7(u): return sum((-1)**j*math.comb(8,j)*max(u+4-j,mp.mpf('0'))**7/mp.factorial(7) for j in range(9))
def profile(x,cs,ms): return sum(c*k7(x+m*a) for c,m in zip(cs,ms))
def J(b,s):
 y=max(s,mp.mpf('0'))
 return mp.exp(b*(s-y))*b**-8*sum((b*y)**r/mp.factorial(r) for r in range(8))
def closed(b,cs,ms): return sum(c*(-1)**j*math.comb(8,j)*J(b,m*a+4-j) for c,m in zip(cs,ms) for j in range(9))
def direct(b,cs,ms):
 knots=sorted(set(max(mp.mpf('0'),j-4-m*a) for m in ms for j in range(9)))
 return mp.quad(lambda x: profile(x,cs,ms)*mp.exp(-b*x),[0,*[x for x in knots if x>0],mp.inf])
rows=[]
for name,cs,ms in [('baseline',BASE,BASE_M),('cross',CROSS,CROSS_M),('lag2_cross',LAG2,LAG2_M),('lag3_cross',LAG3,LAG3_M)]:
 for n in range(4):
  b=mp.mpf(n)+mp.mpf(1)/4; x=closed(b,cs,ms); y=direct(b,cs,ms)
  rows.append({'profile':name,'n':n,'closed':mp.nstr(x,35),'quadrature':mp.nstr(y,35),'absolute_residual':mp.nstr(abs(x-y),8)})
result={'schema':'marici.grothendieck.undilated-septic-moment-formula-check.v1','rows':rows,'claim_boundary':'High-precision identity check, not directed interval certification.'}
(Path(__file__).parents[1]/'results/undilated-septic-moment-formula-check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
