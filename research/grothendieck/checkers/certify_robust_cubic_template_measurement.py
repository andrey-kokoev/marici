"""Arb calibration and robust common/mismatched-error cubic certificate.

Completed theta windows are integrated in v=pi*exp(2x)-pi*A^2,
with the exponentially tiny global scale factored out analytically.
"""
from pathlib import Path
from math import floor,isqrt
import json
import runpy
from flint import arb,ctx

ROOT=Path(__file__).resolve().parents[3]
base=runpy.run_path(str(Path(__file__).with_name('certify_two_feature_escape_transport.py')))
assert base['result']['passed']
ctx.prec=192
PI=arb.pi(); y=arb(3);gamma=arb(1);s=arb(7)/2
P=100000;V=arb(32);CELLS=8192;step=V/CELLS
Lhat=arb('0.13668993')
a=base['correlation']

def pos_ball(upper):
    assert upper>0
    return arb(0).union(arb(upper.upper()))

def sym_ball(upper):
    u=arb(upper.upper())
    return (-u).union(u)

def primes_to(n):
    sieve=bytearray(b'\x01')*(n+1);sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if sieve[p]]

def window(A,p,label):
    aa=arb(A);t0=PI*A*A;loga=aa.log()
    D=t0*aa**(arb(7)/2)
    assert t0*(p*p-1)>V
    integral=arb(0);centered=arb(0)
    for j in range(CELLS):
        vv=(j*step).union((j+1)*step)
        t=t0+vv;x=(t/PI).log()/2
        atoms=arb(0)
        for n in (1,2):
            q=n*n*t
            atoms+=(4*q*q-6*q)*(-((n*n-1)*t0+n*n*vv)).exp()
        ratio=(arb(4)/3)**4*(-7*t).exp()
        assert ratio<1
        theta_tail=4*t*t*81*(-8*t0-9*vv).exp()/(1-ratio)
        density=(3*x).cosh()*(x/2).exp()*(atoms+pos_ball(theta_tail))/(2*t*D)
        integral+=step*density
        centered+=step*(x*(3*x).tanh()-loga)*density
    # All atoms, all v>=V: normalized density <=2(1+v)^3 exp(-v)/den.
    den=1-16*(-3*t0).exp()
    assert den>0
    tail=2*(-V).exp()*(V**3+6*V**2+15*V+16)/den
    integral+=pos_ball(tail)
    centered+=sym_ball((loga+arb(A*p).log())*tail)
    assert integral>0
    mu=loga+centered/integral
    scale=D*(-t0).exp()
    X=scale*integral
    assert X>0
    # Propose an exact rational scientific-notation normalizer from log scale.
    exponent=floor(float((D.log()-t0+integral.log())/arb(10).log()))
    mantissa=X/(arb(10)**exponent)
    numerator=round(float(mantissa)*1000000)
    Xhat=arb(numerator)/1000000*(arb(10)**exponent)
    r=X/Xhat
    assert abs(r-1)<arb('0.005')
    mu_num=round(float(mu)*1000000)
    mu_hat=arb(mu_num)/1000000
    assert abs(mu_hat-mu)<arb('0.001')
    return {'label':label,'A':A,'p':p,'scaled_integral':integral,'X':X,
            'Xhat':Xhat,'ratio':r,'mu':mu,'mu_hat':mu_hat,
            'normalizer':{'mantissa_numerator':numerator,'mantissa_denominator':1000000,
                          'decimal_exponent':exponent},'moment_numerator':mu_num,
            'tail_bound':tail}

windows=[window(2,2,'A1'),window(4,3,'A2'),window(12,5,'B1'),window(60,7,'B2')]
primes=primes_to(P)
# All-prime L enclosure using finite Mangoldt powers and its analytic tail.
N0=4096;partial=arb(0)
for p in primes:
    if p>N0: break
    n=p
    while n<=N0:
        partial+=arb(p).log()*arb(n)**(-s)
        n*=p
n0=arb(N0)
tail=n0**(1-s)*(n0.log()/(s-1)+1/(s-1)**2)
gamma_part=1/s+1/(s-1)-PI.log()/2+(s/2).digamma()/2
L=gamma_part-partial-pos_ball(tail)
LP=gamma_part-sum((arb(p).log()/(arb(p)**s-1) for p in primes),arb(0))
C_actual=(LP-Lhat)/y

# The shared finite escape-field even contribution, evaluated analytically.
R=arb(8);S=arb(16);logP=arb(P).log();delta=arb(1)/100
assert R<logP and logP<S and logP<R+S
beta_minus=arb(0)
for j,numerator in enumerate(base['numerators']):
    c=arb(numerator)/base['denominator']
    beta_minus+=2*c*((((j+1)*delta)/2).exp()-((j*delta)/2).exp())
C_field=(beta_minus*(-(y+arb(1)/2)*(R+S-logP)).exp()/(y+arb(1)/2)
         +arb(P)**(arb(1)/2-y)*a/(y-arb(1)/2)-2*Lhat*a)
common_budget=arb('0.05')
assert abs(C_actual)<common_budget and abs(C_field)<common_budget

# Independent deviations: even scalar, residual correlation, moment, and
# normalized one-slot response noise. Cross-products are retained.
even_error=arb('0.0001');correlation_error=arb('0.00002')
moment_error=arb('0.001');scalar_noise=arb('0.0001')
assert abs(1/(2*y)-a)<correlation_error
Ctest=((1+y*y).sqrt()+1+2*abs(Lhat))/(2*(y-gamma)).sqrt()
Ctest+=(1/(y+arb(1)/2)**2+1/(y-arb(1)/2)**2).sqrt()

def pair_budget(w1,w2):
    # Common C is budgeted only AFTER forming the calibration-ratio difference.
    d=arb(2).sqrt()*a*(w2['ratio']*(w2['mu']-L)-w1['ratio']*(w1['mu']-L))
    assert d>0
    common=arb(2).sqrt()*abs(w2['ratio']-w1['ratio'])*common_budget
    independent=arb(0)
    for w in (w1,w2):
        independent+=arb(2).sqrt()*abs(w['ratio'])*(
            even_error+abs(w['mu']-L)*correlation_error
            +moment_error*abs(a)+moment_error*correlation_error)+scalar_noise
    return d,common+independent

dA,eA=pair_budget(*windows[:2]);dB,eB=pair_budget(*windows[2:])
# Optional independent projective noise in EACH of four two-feature sectors.
sector_scalar_budget=arb('0.00001')
extra_tensor_error=4*sector_scalar_budget
signal=dA*dB
error=abs(dA)*eB+abs(dB)*eA+eA*eB+extra_tensor_error
margin=signal-error
assert margin>arb('0.05')
# Direct actual finite-prime signal, with rational calibration but no perturbation.
z=[arb(2).sqrt()*w['ratio']*(C_actual+(w['mu']-L)/(2*y)) for w in windows]
actual_signal=(z[1]-z[0])*(z[3]-z[2])
assert actual_signal>arb('0.05')

# Concrete common absolute noise tolerances, rational powers of ten, verified.
min_Xhat=windows[-1]['Xhat']
assert all(min_Xhat<w['Xhat'] for w in windows[:-1])
one_slot_allowance=scalar_noise*min_Xhat/Ctest
worst_product=windows[1]['Xhat']*windows[3]['Xhat']
assert all(worst_product<wa['Xhat']*wb['Xhat']
           for i,wa in enumerate(windows[:2]) for j,wb in enumerate(windows[2:])
           if (i,j)!=(1,1))
two_slot_allowance=sector_scalar_budget*worst_product/(Ctest*Ctest)
exp_one=floor(float(one_slot_allowance.log()/arb(10).log()))
exp_two=floor(float(two_slot_allowance.log()/arb(10).log()))
assert arb(10)**exp_one<one_slot_allowance
assert arb(10)**exp_two<two_slot_allowance

result={'schema':'marici.grothendieck.robust-cubic-template-measurement.v1','passed':True,
        'arithmetic':'Arb 192 bits, scaled completed-theta interval integration',
        'parameters':{'spectral_y':3,'receiver_gamma':1,'prime_cutoff':P,
                      'cells_per_window':CELLS,'scaled_v_cutoff':32,
                      'observer_Lhat':'0.13668993','common_even_scalar_budget':'0.05',
                      'independent_even_scalar_error':'0.0001',
                      'independent_residual_correlation_error':'0.00002',
                      'moment_representation_error':'0.001',
                      'normalized_one_slot_noise':'0.0001',
                      'normalized_noise_per_two_feature_sector':'0.00001'},
        'windows':[{key:(str(value) if isinstance(value,arb) else value)
                    for key,value in w.items()} for w in windows],
        'rigorous_balls':{name:str(value) for name,value in {
            'all_prime_L':L,'finite_prime_L':LP,'observer_test_norm_bound':Ctest,
            'actual_common_even_scalar':C_actual,'finite_field_common_even_scalar':C_field,
            'A_gap_reference':dA,'B_gap_reference':dB,'A_gap_error':eA,'B_gap_error':eB,
            'calibrated_reference_signal_per_w_squared':signal,
            'total_error_per_w_squared':error,'remaining_margin_per_w_squared':margin,
            'direct_actual_finite_prime_signal_per_w_squared':actual_signal,
            'minimum_one_slot_absolute_noise_allowance':one_slot_allowance,
            'minimum_two_feature_absolute_noise_allowance':two_slot_allowance}.items()},
        'certified_claims':{'remaining_real_margin_exceeds_0_05_w_seam_squared':True,
                            'all_relative_amplitude_errors_below_0_005':True,
                            'all_rational_moment_errors_below_0_001':True,
                            'common_absolute_one_slot_noise_suffices':f'10^({exp_one})',
                            'common_absolute_two_feature_noise_suffices':f'10^({exp_two})'},
        'scope':'Original four-sector cubic gap witness only. Fixed rational calibration, scaled theta tails, finite primes, shared/mismatched templates and explicit independent noise budgets. No crossed-source or translated-family uniformity and no noisy derived class are asserted.'}
out=ROOT/'research/grothendieck/results/robust-cubic-template-measurement.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
