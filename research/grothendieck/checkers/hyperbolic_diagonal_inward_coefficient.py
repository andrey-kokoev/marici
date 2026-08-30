"""Cancellation-free third variation for the diagonal inward coefficient A(0)."""

from __future__ import annotations

import math


ORDER=3


def add(a:list[float],b:list[float])->list[float]:return [x+y for x,y in zip(a,b)]
def neg(a:list[float])->list[float]:return [-x for x in a]
def mul(a:list[float],b:list[float])->list[float]:return [sum(a[j]*b[n-j] for j in range(n+1)) for n in range(ORDER+1)]
def power(a:list[float],n:int)->list[float]:
    r=[1.0]+[0.0]*ORDER
    for _ in range(n):r=mul(r,a)
    return r
def reciprocal(a:list[float])->list[float]:
    r=[0.0]*(ORDER+1);r[0]=1/a[0]
    for n in range(1,ORDER+1):r[n]=-sum(a[j]*r[n-j] for j in range(1,n+1))/a[0]
    return r
def div(a:list[float],b:list[float])->list[float]:return mul(a,reciprocal(b))
def exp_series(a:list[float])->list[float]:
    r=[0.0]*(ORDER+1);r[0]=math.exp(a[0])
    for n in range(1,ORDER+1):r[n]=sum(j*a[j]*r[n-j] for j in range(1,n+1))/n
    return r


def coefficients(holding:float)->tuple[float,float]:
    one=[1.0,0.0,0.0,0.0];p=[1.0,-1.0,0.0,0.0]
    t=[math.tanh(holding/2)]+[0.0]*ORDER
    exponent=mul(p,[holding,0.0,0.0,0.0]);e=exp_series(exponent)
    r=div(add(e,neg(one)),add(e,one))
    n=add(power(t,4),mul(mul(power(t,2),p),p))
    n=add(n,neg(mul(mul(mul(t,add(p,p)),r),one)))
    n=add(n,mul(add(one,neg(mul(power(t,2),add([2.0,0,0,0],mul(p,p))))),power(r,2)))
    n=add(n,mul(mul(mul(t,add(p,p)),power(r,3)),one))
    return n[2],n[3]


def derivative(f,x,h):return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)
def second(f,x,h):return (-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h*h)
def third(f,x,h):return (f(x+2*h)-2*f(x+h)+2*f(x-h)-f(x-2*h))/(2*h**3)


def main()->None:
    phi=lambda x:coefficients(x)[0];psi=lambda x:coefficients(x)[1]
    left,right=1.5,2.5
    for _ in range(60):
        middle=(left+right)/2
        if derivative(phi,middle,1e-4)>0:left=middle
        else:right=middle
    x=(left+right)/2;h=2e-3
    phi2=second(phi,x,h);phi3=third(phi,x,h);psi1=derivative(psi,x,h);psi2=second(psi,x,h)
    inward=-psi2+psi1*phi3/phi2-3*phi2
    print(f"L_star={x}\nphi_second={phi2}\npsi_first={psi1}\npsi_second={psi2}\nfirst_inward_coefficient={inward}")


if __name__=="__main__":main()
