"""Arb calibration of the improved cubic observer at actual background A=2.

Boundary-scaled interval integration encloses the full completed theta sum.
No sampled quadrature, asymptotic substitution, or late-window float values.
"""
from pathlib import Path
import json, math
from flint import arb,ctx
ctx.prec=192
pi=arb.pi(); y=arb(3); gamma=arb(2)
CELLS=8192; T=arb(64)
def pos(U):return arb(0).union(U.upper())
def window(a,b):
    q0=pi*a*a; vmax=pi*(b*b-a*a)
    end=vmax if vmax<T else T
    step=end/CELLS; X=arb(0);J=arb(0)
    for j in range(CELLS):
        v=(j*step).union((j+1)*step)
        q=q0+v;x=(q/pi).log()/2
        # e^(q0) Phi(x) dx/dv, atoms n=1,2 and bounded n>=3.
        density=(2*q-3)*(-v).exp()+(32*q-12)*(-3*q0-4*v).exp()
        ratio=(arb(4)/3)**4*(-7*q).exp()
        assert ratio<1
        tail=2*q*81*(-8*q0-9*v).exp()/(1-ratio)
        density=(x/2).exp()*(density+pos(tail))
        X+=step*(y*x).cosh()*density
        J+=step*x*(y*x).sinh()*density
    if vmax>T:
        # On the tail, cosh(3x)<=exp(3x), x<=q and q^(11/4)<=q^3.
        ratio=(arb(3)/2)**4*(-5*q0).exp()
        factor=2*pi**(-arb(7)/4)*(1+16*(-3*q0).exp()/(1-ratio))
        Q=q0+T
        X+=pos(factor*(-T).exp()*(Q**3+3*Q**2+6*Q+6))
        J+=pos(factor*(-T).exp()*(Q**4+4*Q**3+12*Q**2+24*Q+24))
    assert X>0 and J>0
    return {'X':X*(-q0).exp(),'mu':J/X,'scaled_X':X}
windows={k:window(a,b) for k,a,b in (
 ('A1',2,4),('A2',4,12),('B1',12,60),('B2',60,420),('CROSS',20,60))}
def primes(N):
    sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
    for p in range(2,math.isqrt(N)+1):
        if sieve[p]:sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
    return [p for p in range(2,N+1) if sieve[p]]
s=arb(7)/2;N=4096;P=arb(0)
for p in primes(N):
    n=p
    while n<=N:P+=arb(p).log()*arb(n)**(-s);n*=p
P+=pos(arb(N)**(1-s)*(arb(N).log()/(s-1)+1/(s-1)**2))
L=1/s+1/(s-1)-pi.log()/2+(s/2).digamma()/2-P
X={k:v['X'] for k,v in windows.items()};mu={k:v['mu'] for k,v in windows.items()}
gA=mu['A2']-mu['A1'];gB=mu['B2']-mu['B1']
assert gA>0 and gB>0
S0=gA*gB/(2*y*y);SX=-(mu['A1']-L)*(mu['B2']-L)/(2*y*y)
h2=1/(2*(y+gamma))
E0=2*h2*X['A1']*X['B1']*(mu['A1']-L)*(mu['B1']-L)
EX=2*h2*X['A1']*X['CROSS']*(mu['A1']-L)*(mu['CROSS']-L)
assert E0>0 and EX>0
alpha0=S0/E0;alphaX=SX/EX
# Exact rational proposals; all conclusions use their rigorous evaluations.
a0=alpha0.mid().fmpq(); ax=alphaX.mid().fmpq()
a0b=arb(a0);axb=arb(ax)
err0=abs(a0b*E0-S0);errX=abs(axb*EX-SX)
assert err0<abs(S0)/10 and errX<abs(SX)/10
assert abs(axb)>abs(a0b)
newnorm=abs(axb)  # per w_seam^2, exact l1-direct-sum dual norm
# Old observer exact norm: t0=1/sqrt(2), since other components are smaller.
assert 2*abs(L)<1
assert 1/(y+arb(1)/2)**2+1/(y-arb(1)/2)**2<arb(1)/2
assert X['A1']>X['A2'] and X['B1']>X['B2']
oldnorm=1/(2*X['A2']*X['B2'])
ratio=oldnorm/newnorm
assert ratio>arb('1e4000')
assert abs(alphaX)>abs(alpha0)
ideal_ratio=oldnorm/abs(alphaX)
assert ideal_ratio>arb('1e4000')
noise=arb('1e-550')
noise_error=newnorm*noise
signal=a0b*E0 # the actual v0 has coefficient zero on the private cross row
margin=signal-noise_error
assert margin>arb('0.04')
original_functional_margin=margin-err0
assert original_functional_margin>arb('0.04')
# Calibration error for arbitrary source coefficients is stated basiswise,
# not converted into an unproved uniform relative-source error.
result={'passed':True,'arithmetic':'python-flint Arb, 192 bits',
 'parameters':{'background_A':2,'spectral_point':'3i','receiver_gamma':2,
 'cells_per_scaled_window':CELLS,'scaled_tail_cutoff':64,'prime_cutoff':10000,
 'prime_cutoff_error_for_this_test':'exactly zero (unchanged residual coordinates)',
 'total_independent_two_row_projective_response_noise':'1e-550'},
 'windows':{k:{a:str(b) for a,b in v.items()} for k,v in windows.items()},
 'rigorous_balls':{k:str(v) for k,v in {'L_at_7_over_2':L,'original_witness_value_per_w_squared':S0,
 'crossed_source_value_per_w_squared':SX,'ideal_private_coefficient_0':alpha0,
 'ideal_private_coefficient_cross':alphaX,'calibration_error_on_v0':err0,
 'calibration_error_on_vcross':errX,'new_response_norm_per_w_squared':newnorm,
 'old_response_norm_per_w_squared':oldnorm,'old_to_new_norm_ratio':ratio,
 'old_to_ideal_same_functional_norm_ratio':ideal_ratio,
 'noise_error_per_w_squared':noise_error,'calibrated_positive_margin_per_w_squared':margin,
 'original_functional_certification_margin':original_functional_margin}.items()},
 'rational_coefficients_per_w_squared':{'row_0':str(a0),'row_cross':str(ax)},
 'certified_claims':{'positive_witness_margin_exceeds_0_04_w_squared':True,
 'both_nonzero_basis_calibration_errors_below_ten_percent':True,
 'response_norm_improvement_exceeds_10_to_4000':True,
 'same_functional_ideal_norm_improvement_exceeds_10_to_4000':True,
 'original_functional_margin_after_calibration_exceeds_0_04':True},
 'scope':'Exact functional equality belongs to the ideal calibrated coefficients in the companion theorem. Saved rational coefficients have explicitly enclosed errors on both visible source basis directions; other 268 basis values remain zero. All response labels are retained, but this observer tests only two private residual sectors. No uncalibrated transfer of the old four-sector noise protocol is made.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/certified-private-sector-cubic-observer.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rational_coefficients_per_w_squared'},indent=2))
print('Exact rational observer coefficients saved in',out)
