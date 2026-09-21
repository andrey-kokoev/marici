"""Algebraic Laplace identities; numerical zero fixtures are regressions only."""
from pathlib import Path
import json
import sympy as sy
import mpmath as mp

q,s,rho,m,c0,Ps=sy.symbols('q s rho m c0 Ps')
Pq,dq,ds,lp=sy.symbols('Pq dq ds lp')
# dq=digamma(q/2), ds=digamma(s/2); use psi(1+x)=psi(x)+1/x.
prime=(Pq-Ps)/(s-q)-1/((s-1)*(q-1))
gamma=((dq+2/q)-(ds+2/s))/(2*(q-s))
Lq=1/q+1/(q-1)-lp/2+dq/2-Pq
Ls=1/s+1/(s-1)-lp/2+ds/2-Ps
assert sy.factor(prime+gamma-(Lq-Ls)/(q-s))==0
# The pole of zeta at 1 is removed by the source endpoint subtraction.
at_one=prime.subs(Pq,1/(q-1)+c0)
assert sy.simplify(sy.limit((q-1)*at_one,q,1))==0
assert sy.simplify(sy.limit(at_one,q,1)-(1/(s-1)**2+(c0-Ps)/(s-1)))==0
# Every completed-zeta zero leaves this residue.
assert sy.simplify(sy.limit((q-rho)*(m/(q-rho)-Ls)/(q-s),q,rho)+m/(s-rho))==0
# A rational Euler packet vanishing identically has zero coefficients.
s1,s2,s3,c1,c2,c3=sy.symbols('s1 s2 s3 c1 c2 c3')
packet=sum(c/(ss-rho) for c,ss in ((c1,s1),(c2,s2),(c3,s3)))
for c,ss in ((c1,s1),(c2,s2),(c3,s3)):
    assert sy.simplify(sy.limit((ss-rho)*packet,rho,ss)-c)==0

mp.mp.dps=60
def P(z):return -mp.diff(mp.zeta,z)/mp.zeta(z)
def xi_log(z):
    return 1/z+1/(z-1)-mp.log(mp.pi)/2+mp.digamma(z/2)/2-P(z)
def transform(ss,qq):
    return ((P(qq)-P(ss))/(ss-qq)-1/((ss-1)*(qq-1))
            +(mp.digamma(1+qq/2)-mp.digamma(1+ss/2))/(2*(qq-ss)))
for ss,qq in ((mp.mpf(2),mp.mpf('1.3')),(mp.mpc('2.2','.4'),mp.mpc('1.5','.3'))):
    assert abs(transform(ss,qq)-(xi_log(qq)-xi_log(ss))/(qq-ss))<mp.mpf('1e-50')
zero=mp.zetazero(1)
ss=mp.mpf(2)
expected=-1/(ss-zero)
fixtures=[]
for eps in (mp.mpf('1e-3'),mp.mpf('1e-5'),mp.mpf('1e-7')):
    error=abs(eps*transform(ss,zero+eps)-expected)
    fixtures.append({'epsilon':str(eps),'scaled_residue_error':mp.nstr(error,12)})
assert mp.mpf(fixtures[-1]['scaled_residue_error'])<mp.mpf('1e-7')
result={'passed':True,'checks':{'source_endpoint_removes_q_one_pole':True,
 'prime_plus_gamma_is_completed_xi_divided_difference':True,
 'zero_residue_is_minus_m_over_s_minus_rho':True,
 'distinct_euler_packet_partial_fractions_are_independent':True},
 'critical_zero_regressions':fixtures,
 'scope':'Exact symbolic identities and numerical sign regression. Non-L2 follows in the note from the Laplace L2 bound and the classical existence of infinitely many distinct critical-line zeros, not from numerical zero verification.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/euler-residual-laplace-obstruction.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
