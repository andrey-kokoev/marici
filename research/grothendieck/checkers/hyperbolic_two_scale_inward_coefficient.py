"""Cancellation-free two-scale third variation for the inward coefficient A(k)."""

from __future__ import annotations

import math

from hyperbolic_diagonal_inward_coefficient import add,derivative,div,exp_series,mul,neg,power,second,third


def tanh_series(argument:list[float])->list[float]:
    exponential=exp_series([2.0*x for x in argument]);one=[1.0,0.0,0.0,0.0]
    return div(add(exponential,neg(one)),add(exponential,one))


def coefficients(k:float,holding:float)->tuple[float,float]:
    one=[1.0,0.0,0.0,0.0];p=[1.0,-1.0,0.0,0.0];q=[1.0,-(1.0+k),0.0,0.0]
    tau0=0.5*math.log1p(k)
    d=[tau0]+[((1.0+k)**n-1.0)/(2.0*n*2.0**n) for n in range(1,4)]
    image=[tau0,-d[1],-d[2],-d[3]]
    t=tanh_series([(holding+d[0])/2.0,d[1]/2.0,d[2]/2.0,d[3]/2.0])
    pl=mul(p,[holding,0.0,0.0,0.0])
    r=tanh_series([(pl[n]+image[n])/2.0 for n in range(4)])
    n=add(power(t,4),mul(mul(power(t,2),p),q))
    n=add(n,neg(mul(mul(t,add(p,q)),r)))
    n=add(n,mul(add(one,neg(mul(power(t,2),add([2.0,0,0,0],mul(p,q))))),power(r,2)))
    n=add(n,mul(mul(t,add(p,q)),power(r,3)))
    return n[2],n[3]


def inward_coefficient(k:float)->tuple[float,float]:
    phi=lambda x:coefficients(k,x)[0];psi=lambda x:coefficients(k,x)[1]
    left,right=0.2,3.0
    for _ in range(60):
        middle=(left+right)/2.0
        if derivative(phi,middle,1e-4)>0:left=middle
        else:right=middle
    holding=(left+right)/2.0;h=2e-3
    phi2=second(phi,holding,h);phi3=third(phi,holding,h);psi1=derivative(psi,holding,h);psi2=second(psi,holding,h)
    return holding,-psi2+psi1*phi3/phi2-3.0*phi2


def polynomial_reserve(k:float)->tuple[float,float]:
    holding,_=inward_coefficient(k);phi=lambda x:coefficients(k,x)[0];psi=lambda x:coefficients(k,x)[1];h=2e-3
    p=second(phi,holding,h);b=derivative(psi,holding,h);c=second(psi,holding,h);d=third(phi,holding,h)
    return holding,p*c-b*d+3.0*p*p


def critical_q_l(k:float)->tuple[float,float]:
    """Return the limiting critical holding and Q_L there.

    Since Phi_L=(1-t^2)Q and Q=0 at the critical point,
    Q_L=Phi_LL/(1-t^2).  This form avoids differentiating a generated
    polynomial and is adequate for the directed numerical diagnostic.
    """
    holding,_=inward_coefficient(k)
    phi=lambda x:coefficients(k,x)[0]
    t=math.tanh((holding+0.5*math.log1p(k))/2.0)
    return holding,second(phi,holding,2e-3)/(1.0-t*t)


def monotonicity_margin(k:float)->tuple[float,float,float,float]:
    """Diagnose M=R_k Q_L-R_L Q_k along Q=0.

    On the critical curve this is M=Q_L*dR_*/dk.  A negative value is
    precisely the desired increase of the reserve because Q_L<0.
    """
    step=max(2e-5,2e-4*(1.0+k))
    if k<step:
        r0=polynomial_reserve(k)[1]
        r1=polynomial_reserve(k+step)[1]
        reserve_derivative=(r1-r0)/step
    else:
        rm=polynomial_reserve(k-step)[1]
        rp=polynomial_reserve(k+step)[1]
        reserve_derivative=(rp-rm)/(2.0*step)
    holding,q_l=critical_q_l(k)
    return holding,reserve_derivative,q_l,reserve_derivative*q_l


def main()->None:
    for k in (0.0,0.001,0.01,0.1,0.3,1.0,3.0,10.0,30.0,100.0):
        print(k,inward_coefficient(k),polynomial_reserve(k),monotonicity_margin(k))


if __name__=="__main__":main()
