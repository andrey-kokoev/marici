"""Completed-zeta Clark kernel against endpoint/gamma/prime coordinates."""
from pathlib import Path
import json
import sympy as sp
import mpmath as mp
s,t=sp.symbols('s t')
q=1/s+1/(s-1)
qt=1/t+1/(t-1)
endpoint=1/(s*(t-1))+1/((s-1)*t)
assert sp.cancel((q+qt)/(s+t-1)-endpoint)==0
mp.mp.dps=60
xi=lambda a:a*(a-1)*mp.power(mp.pi,-a/2)*mp.gamma(a/2)*mp.zeta(a)/2
L=lambda a:1/a+1/(a-1)-mp.log(mp.pi)/2+mp.digamma(a/2)/2+mp.diff(mp.zeta,a)/mp.zeta(a)
N=2000
Lambda=[mp.mpf(0)]*(N+1)
for p in list(sp.primerange(2,N+1)):
    power=p
    while power<=N:
        Lambda[power]=mp.log(p)
        power*=p
prime=lambda a:sum(Lambda[n]*mp.power(n,-a) for n in range(2,N+1) if Lambda[n])
tail=lambda sigma:mp.power(N,1-sigma)*(mp.log(N)/(sigma-1)+1/(sigma-1)**2)
X=lambda z:xi(mp.mpf('.5')-1j*z)
records=[]
for sv,sw in [(mp.mpc(3,'.4'),mp.mpc(4,'-.2')),(mp.mpc(2,0),mp.mpc(3,0))]:
    z=1j*(sv-mp.mpf('.5'));w=1j*(sw-mp.mpf('.5'))
    xz,xw=X(z),X(w)
    dz,dw=mp.diff(X,z),mp.diff(X,w)
    E=lambda x,d:x+1j*d
    Es=lambda x,d:x-1j*d
    kernel=(mp.conj(E(xw,dw))*E(xz,dz)-mp.conj(Es(xw,dw))*Es(xz,dz))/(-1j*(z-mp.conj(w)))
    denom=sv+mp.conj(sw)-1
    pref=2*mp.conj(xw)*xz
    exact=pref*(L(sv)+mp.conj(L(sw)))/denom
    assert abs(kernel-exact)<mp.mpf('1e-50')
    end=1/(sv*(mp.conj(sw)-1))+1/((sv-1)*mp.conj(sw))
    arch=(-mp.log(mp.pi)+(mp.digamma(sv/2)+mp.conj(mp.digamma(sw/2)))/2)/denom
    primes=-(prime(sv)+mp.conj(prime(sw)))/denom
    truncated=pref*(end+arch+primes)
    bound=abs(pref/denom)*(tail(mp.re(sv))+tail(mp.re(sw)))
    assert abs(kernel-truncated)<bound
    records.append({'s':str(sv),'s_w':str(sw),'truncation_error':mp.nstr(abs(kernel-truncated),15),'analytic_tail_bound':mp.nstr(bound,15)})
result={'schema':'marici.grothendieck.clark-arithmetic-green-crosswalk.v1','passed':True,
        'checks':{'endpoint_swap_identity_exact':True,'full_xi_log_derivative_crosswalk':True,
                  'euler_sum_with_analytic_tail_bound':True},'cutoff':N,'fixtures':records,
        'scope':'Signed kernel identity on the Euler chart, with meromorphic continuation. No positive-kernel conclusion.'}
p=Path(__file__).resolve().parents[1]/'results/clark-arithmetic-green-crosswalk.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
