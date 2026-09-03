"""Independent high-precision quadrature scout for baseline and cross spline forms."""
import json, math
from pathlib import Path
import mpmath as mp

mp.mp.dps=60
BASE=[mp.mpf(1),-5,mp.mpf(33)/4,-5,1]; BASE_M=[2,1,0,-1,-2]
CROSS=[mp.mpf(1)/2,-mp.mpf(5)/2,mp.mpf(37)/8,-5,mp.mpf(37)/8,-mp.mpf(5)/2,mp.mpf(1)/2]; CROSS_M=[3,2,1,0,-1,-2,-3]
a=2*mp.log(2)

def k7(u):
    return sum((-1)**j*math.comb(8,j)*max(u+4-j,mp.mpf('0'))**7/mp.factorial(7) for j in range(9))
def profile(x,coeff,ms):
    u=x/2
    return sum(c*k7(u+m*a) for c,m in zip(coeff,ms))
def prime_powers(limit=800000):
    for p in range(2,limit+1):
        if all(p%d for d in range(2,int(math.sqrt(p))+1)):
            q=p
            while q<=limit:
                yield p,q
                q*=p

def evaluate(coeff,ms):
    f0=profile(mp.mpf('0'),coeff,ms)
    # Stable removable value at zero follows from evenness: numerator vanishes linearly.
    def integrand(x):
        if abs(x)<mp.mpf('1e-30'):
            x=mp.mpf('1e-30')
        return (f0*mp.exp(-x)-profile(x,coeff,ms)*mp.exp(-x/4))/(1-mp.exp(-x))
    # All profiles vanish beyond a finite endpoint; retain the f0 tail analytically through quadrature.
    knots=sorted(set([mp.mpf('0')]+[max(mp.mpf('0'),2*(4-m*a)) for m in ms]+[max(mp.mpf('0'),2*(m*a+4)) for m in ms]))
    knots=[x for x in knots if x>0]
    arch=-(mp.euler+mp.log(mp.pi))*f0+mp.quad(integrand,[0,*knots,mp.inf])
    prime=mp.mpf('0')
    for p,q in prime_powers():
        value=profile(mp.log(q),coeff,ms)
        if value: prime-=2*mp.log(p)/mp.sqrt(q)*value
    return arch,prime,arch+prime

rows={}
for name,coeff,ms in [('baseline',BASE,BASE_M),('cross',CROSS,CROSS_M)]:
    arch,prime,total=evaluate(coeff,ms)
    rows[name]={'arch':mp.nstr(arch,30),'prime':mp.nstr(prime,30),'total':mp.nstr(total,30)}
result={'schema':'marici.grothendieck.direct-quadrature-two-translate-spline.v1','prime_power_limit':800000,'coordinate_convention':'single physical test f(x)=profile(x/2); prime evaluation f(log q)','rows':rows,'claim_boundary':'High-precision mpmath quadrature scout, not directed interval certification.'}
out=Path(__file__).parents[1]/'results/direct-quadrature-two-translate-spline.json';out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
