"""Coarse rational enclosure for the a=2 log(2) preconditioned spline Weil form."""
from fractions import Fraction as F
from math import comb, factorial
import json, pathlib, sys
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(pathlib.Path(__file__).parent))
from rational_interval import add, sub, mul, scale, inv, log_q as _raw_log_q, exp_q, sqrt_q, pi_interval, gamma_interval

_LOG_CACHE={}
def log_q(x):
    if x not in _LOG_CACHE: _LOG_CACHE[x]=_raw_log_q(x)
    return _LOG_CACHE[x]

Z=(F(0),F(0))
COEFF=[F(1),F(-5),F(33,4),F(-5),F(1)]
SHIFT_INDEX=[2,1,0,-1,-2]
def hull(a,b): return (min(a[0],b[0]),max(a[1],b[1]))
def neg(a): return (-a[1],-a[0])
def pow_pos(a,n):
    assert a[0]>=0
    return (a[0]**n,a[1]**n)
def max0(a): return (max(F(0),a[0]),max(F(0),a[1]))
def k7_iv(x):
    out=Z
    for j in range(9):
        y=max0(add(x,(F(4-j),F(4-j))))
        out=add(out,scale(F((-1)**j*comb(8,j),factorial(7)),pow_pos(y,7)))
    return out

def shifted_k(u, a):
    vals=[k7_iv(add(u,scale(F(m),a))) for m in SHIFT_INDEX]
    coeff=COEFF
    out=Z
    for c,v in zip(coeff,vals): out=add(out,scale(c,v))
    return out

def primes(n):
    out=[]
    for q in range(2,n+1):
        if all(q%d for d in range(2,int(q**0.5)+1)):out.append(q)
    return out

def prime_term(a, wrong_sign=False, omit_shifts=False):
    total=Z
    for p in primes(1024):
        q=p
        while q<=1024:
            lq=log_q(F(q)); kval=k7_iv(lq) if omit_shifts else shifted_k(lq,a)
            weight=mul(log_q(F(p)),inv(sqrt_q(F(q))))
            total=add(total,scale(F(2) if wrong_sign else F(-2),mul(weight,kval)))
            q*=p
    return total

def k7_deriv_iv(x,r,right=False):
    out=Z; power=7-r
    for j in range(9):
        y=add(x,(F(4-j),F(4-j)))
        if power==0:
            step=(F(1),F(1)) if y[0]>=0 and right else ((F(1),F(1)) if y[0]>0 else ((F(0),F(0)) if y[1]<0 or (y[1]==0 and not right) else (F(0),F(1))))
            term=step
        else:
            term=pow_pos(max0(y),power)
        out=add(out,scale(F((-1)**j*comb(8,j),factorial(power)),term))
    return out

def zero_jet(r,a):
    # f(x)=k_a(x/2). Odd jets through C6 vanish; r=7 uses the right jet.
    if r%2 and r<7:return Z
    shifts=[scale(F(m),a) for m in SHIFT_INDEX]
    coeff=COEFF
    out=Z
    for c,s in zip(coeff,shifts): out=add(out,scale(c,k7_deriv_iv(s,r,right=(r==7))))
    return scale(F(1,2)**r,out)

def sp_bounds(N,p,K=16,alpha=F(1,4)):
    # Exact finite prefix plus decreasing-function integral enclosure.
    stop=N+K;prefix=sum((F(n)+alpha)**(-p) for n in range(N,stop))
    x=F(stop)+alpha
    upper=x**(1-p)/F(p-1)+x**(-p)/2+F(p,12)*x**(-p-1)
    correction=F(p*(p+1)*(p+2),720)*x**(-p-3)
    return (prefix+upper-correction,prefix+upper)
def arch_tail(a,N=1,omit_d0=False,variation=F(81,2),d=1):
    f0=shifted_k(Z,a);delta=F(d,4)
    stop=N+16
    dprefix=sum(F(1,n+1)-F(1)/(F(n)+delta) for n in range(N,stop))
    x=F(stop);L=log_q((x+1)/(x+delta))
    g=F(1)/(x+delta)-F(1)/(x+1)
    gp=-(x+delta)**-2+(x+1)**-2
    g3=-F(6)*(x+delta)**-4+F(6)*(x+1)**-4
    sup=add(L,(g/2-gp/12,g/2-gp/12))
    slo=(sup[0]+g3/F(720),sup[1]+g3/F(720))
    D=(dprefix-sup[1],dprefix-slo[0])
    out=Z if omit_d0 else mul(f0,D)
    for r in range(1,8):
        fr=zero_jet(r,a)
        out=sub(out,mul(fr,sp_bounds(N,r+1,alpha=delta)))
    s8=sp_bounds(N,8)[1]
    if variation is not None:
        return add(out,(-variation*s8,variation*s8)),D
    atom=Z
    for coeff,m in zip(COEFF,SHIFT_INDEX):
        for j in range(9):
            x=sub((F(2*(j-4)),F(2*(j-4))),scale(F(2*m),a))
            if x[1]<=0: continue
            assert x[0]>0
            q=4*N+d
            first=scale((F(2,q)**8)*(F(2)**(q*m)),exp_half(-q*(j-4)))
            # exp(-x) <= 1/(1+x) avoids dependency inflation in split exp/log factors.
            ratio_hi=F(1)/(F(1)+x[0])
            kernel=(first[0],first[1]/(1-ratio_hi))
            weight=coeff*F(((-1)**j)*comb(8,j),128)
            atom=add(atom,scale(weight,kernel))
    return sub(out,atom),D

_EXP_HALF={0:(F(1),F(1)),1:exp_q(F(1,2))}
def exp_half(q):
    if q in _EXP_HALF:return _EXP_HALF[q]
    if q<0:
        v=inv(exp_half(-q));_EXP_HALF[q]=v;return v
    out=(F(1),F(1));base=_EXP_HALF[1];n=q
    while n:
        if n&1:out=mul(out,base)
        base=mul(base,base);n//=2
    _EXP_HALF[q]=out;return out

def gamma_tail_from_exp(z,ez,c):
    poly=Z
    for j in range(8): poly=add(poly,scale(F(1,factorial(j)),pow_pos(scale(c,z),j)))
    return scale(F(factorial(7),1)/c**8,mul(ez,poly))

def integral_shift(m,a,n,d=1):
    # b=n+d/4, c=2b=(4n+d)/2, exp(c*m*a)=2^((4n+d)m).
    q=4*n+d;c=F(q,2);s=scale(F(m),a);out=Z
    for j in range(8):
        upper=F(8-j);lo_raw=add(s,(F(4-j),F(4-j)))
        if lo_raw[0]>=upper:continue
        thi=gamma_tail_from_exp((upper,upper),exp_half(-q*(8-j)),c)
        if lo_raw[1]<=0:
            lo=Z;elo=(F(1),F(1))
        elif lo_raw[0]>0:
            lo=lo_raw;elo=scale(F(2)**(-q*m),exp_half(-q*(4-j)))
        else:
            lo=max0(lo_raw);elo=hull((F(1),F(1)),scale(F(2)**(-q*m),exp_half(-q*(4-j))))
        tlo=gamma_tail_from_exp(lo,elo,c)
        mom=mul(sub(tlo,thi),exp_half(q*(4-j)))
        out=add(out,scale(F((-1)**j*comb(8,j),factorial(7)),mom))
    return scale(F(2)*(F(2)**(q*m)),out)

def exact_In(a,n,d=1):
    out=Z
    for coeff,m in zip(COEFF,SHIFT_INDEX):
        out=add(out,scale(coeff,integral_shift(m,a,n,d)))
    return out

_ARCH_FINITE={}
def arch(a,omit_d0=False,variation=None,N=3,d=1):
    key=(a,N,d,tuple(COEFF),tuple(SHIFT_INDEX))
    if key not in _ARCH_FINITE:
        f0=shifted_k(Z,a);finite=Z
        for n in range(N): finite=add(finite,sub(scale(F(1,n+1),f0),exact_In(a,n,d)))
        _ARCH_FINITE[key]=(f0,finite)
    f0,finite=_ARCH_FINITE[key]
    tail,D=arch_tail(a,N,omit_d0,variation,d)
    gp=add(gamma_interval(),(log_q(pi_interval()[0])[0],log_q(pi_interval()[1])[1]))
    return add(scale(F(-1),mul(f0,gp)),add(finite,tail)),f0,D

def enc(x): return [str(x[0]),str(x[1])]
def main():
    l2=log_q(F(2));a=scale(F(2),l2)
    A,f0,D=arch(a);P=prime_term(a);total=add(A,P)
    wrong=add(A,prime_term(a,True)); omitted=add(A,prime_term(a,False,True))
    no_d0=add(arch(a,True)[0],P); under=add(arch(a,False,F(0))[0],P)
    broad=add(arch(a,False,F(81,2))[0],P)
    assert total[0]>0
    assert broad[0]<=total[0] and total[1]<=broad[1]
    assert f0[0]>0
    assert mul(f0,D)[1]<0
    # Euler--Maclaurin orientation audit: B2, B4, B6 alternate with decreasing size.
    x=F(19,1)+F(1,4)
    for p in range(2,9):
        b2=F(p,12)*x**(-p-1)
        b4=F(p*(p+1)*(p+2),720)*x**(-p-3)
        b6=F(p*(p+1)*(p+2)*(p+3)*(p+4),30240)*x**(-p-5)
        assert 0<b6<b4<b2
    y=F(19);g3=-F(6)*(y+F(1,4))**-4+F(6)*(y+1)**-4
    g5=-F(120)*(y+F(1,4))**-6+F(120)*(y+1)**-6
    assert 0<(-g5/F(30240))<(-g3/F(720))
    data={"schema":"marici.preconditioned-spline-weil.v1","a":"2 log 2","kernel_shift":"1/4","intervals":{"f0":enc(f0),"zero_jets":{str(r):enc(zero_jet(r,a)) for r in range(1,8)},"arch":enc(A),"prime":enc(P),"gram":enc(total)},"deliberate_failures":{"prime_sign_flip":enc(wrong),"omitted_shifts":enc(omitted),"omitted_D_N":enc(no_d0),"zero_Stieltjes_variation":enc(under),"omitted_D_N_component_excludes_zero":mul(f0,D)[1]<0,"reversed_B4_orientation_rejected":True},"certification":"Fraction interval arithmetic; exact cached j=0..2 piecewise exponential moments with full knot prefactors; complete zero-jet Hurwitz tails; signed atomic eighth-derivative tail enclosed by a geometric majorant; all prime powers q<=1024, beyond support.","nonverification":"One coarse one-packet enclosure does not prove positivity, Weil positivity, or RH."}
    out=pathlib.Path(__file__).parents[1]/"results/preconditioned_spline_weil.json";out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(data,indent=2)+"\n")
    print(json.dumps({"schema":data["schema"],"gram_float":[float(total[0]),float(total[1])],"arch_float":[float(A[0]),float(A[1])]}))
if __name__=="__main__":main()
