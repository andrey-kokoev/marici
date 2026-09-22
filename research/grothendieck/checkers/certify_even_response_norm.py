"""Enclose the exact common even-response norm by Laplace Plancherel.

Finite-frequency integrals enclose WHOLE real frequency cells with Acb.
The infinite frequency tail has an explicit digamma/PNT-free Euler-line bound.
"""
from pathlib import Path
import json
from flint import arb,acb,acb_series,ctx

ctx.prec=80;ctx.cap=2
Y=arb(3);GAMMA=arb(1);BETA=GAMMA+arb(1)/2;S=Y+arb(1)/2
T=2048
BANDS=[(0,16,2048),(16,128,512),(128,T,32)]
I=acb(0,1);PI=arb.pi()

def logderivative(q):
    zz=acb_series([q,1],2).zeta()
    return 1/q+1/(q-1)-PI.log()/2+(q/2).digamma()/2+zz[1]/zz[0]

Ls=logderivative(acb(S))
assert Ls.imag.contains(0)

def profiles(q):
    lq=logderivative(q)
    plus=-(Ls+lq)/(S+q-1)+1/(S*(q-1))+1/((S-1)*q)
    minus=(lq-Ls)/(q-S)+1/((S-1)*(q-1))+1/(S*q)
    return plus,minus

positive=arb(0);negative=arb(0)
visitor=globals().get('CELL_VISITOR')
for lo,hi,rate in BANDS:
    width=arb(1)/rate
    for j in range(lo*rate,hi*rate):
        t=(j*width).union((j+1)*width)
        pp,mp=profiles(acb(BETA,t))
        assert pp.is_finite() and mp.is_finite()
        if visitor is not None: visitor(j,rate,pp,mp)
        positive+=width*abs(pp)**2
        negative+=width*abs(mp)**2
integral=acb(positive,negative)

# |psi(z)-log z|<=1/|z| for Re z>0, by one integration by parts.
# For t>=T, |L(beta+it)| <= 0.5 log t + constant below.
zbeta=acb_series([acb(BETA),1],2).zeta()
Pbeta=(-zbeta[1]/zbeta[0]).real
assert Pbeta>0
cL=Pbeta+3/arb(T)-((2*PI).log())/2+PI/4+(1+(BETA/T)**2).log()/4
A=cL+abs(Ls)+1/S+1/(S-1)
assert A.imag.is_zero() if isinstance(A,acb) else True
if isinstance(A,acb): A=A.real
Q=A+arb(T).log()/2
tail=(Q*Q+Q+arb(1)/2)/(PI*T)
assert tail>0
nonnegative_tail=arb(0).union(arb(tail.upper()))
plus_sq=integral.real/PI+nonnegative_tail
minus_sq=integral.imag/PI+nonnegative_tail
assert plus_sq>0 and minus_sq>0
endpoint=(1/S**2+1/(S-1)**2).sqrt()
weak_even=1/(2*(Y+GAMMA)).sqrt()
C=plus_sq.sqrt()+minus_sq.sqrt()+endpoint+weak_even
assert C>1 and C<3
result={'schema':'marici.grothendieck.even-response-norm.v1','passed':True,
        'arithmetic':'Acb whole-real-cell enclosures and Arb explicit infinite tail, 80 bits',
        'parameters':{'y':3,'gamma':1,'Euler_line_beta':'3/2','frequency_cutoff':T,
                      'frequency_bands_start_end_cells_per_unit':BANDS},
        'rigorous_balls':{k:str(v) for k,v in {
            'L_at_7_over_2':Ls,'Euler_prime_majorant_at_beta':Pbeta,
            'finite_integral_plus_and_minus':integral,
            'tail_bound_per_squared_halfline_norm':tail,
            'positive_response_squared_norm':plus_sq,'negative_response_squared_norm':minus_sq,
            'endpoint_norm':endpoint,'weak_even_norm':weak_even,'C_even':C}.items()},
        'scope':'Exact all-prime common even-response norm in the fixed five-label sum norm. No ordinary L2 norm is assigned to the undamped limiting response. This is a norm-weight input, not a solved observer LP.'}
root=Path(__file__).resolve().parents[3]
out=root/'research/grothendieck/results/even-response-norm.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
