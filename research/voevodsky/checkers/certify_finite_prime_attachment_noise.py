"""Rigorous Arb interval calibration of the actual two-window witness.

No sampled quadrature error assumption: every integration cell is evaluated
as an interval, and every omitted infinite sum receives an analytic bound.
Run with: uv run --with python-flint python <this file>
"""
from pathlib import Path
import json
from flint import arb, ctx
ctx.prec=160
PI=arb.pi()
y=arb(3); gamma=arb(2); delta=arb(1)/2
sigma=gamma+arb(1)/2
s0=y+arb(1)/2
CELLS=4096
PRIME_CUTOFF=10000
LOGDERIV_CUTOFF=4096
NOISE=arb('1e-22')

def nonnegative_enclosure(upper):
    assert upper>0
    return arb(0).union(upper.upper())

def prime_tail(N,s):
    n=arb(N)
    return (n**(1-s))*(n.log()/(s-1)+1/(s-1)**2)

def primes_to(N):
    sieve=bytearray(b'\x01')*(N+1)
    sieve[0:2]=b'\x00\x00'
    for p in range(2,int(N**0.5)+1):
        if sieve[p]:
            sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
    return [p for p in range(2,N+1) if sieve[p]]

def phi(x):
    # Completed convention: exp(x/2) sum (4 a_n^2-6 a_n) exp(-a_n).
    c=PI*(2*x).exp()
    terms=arb(0)
    for n in (1,2):
        a=c*n*n
        term=(4*a*a-6*a)*(-a).exp()
        assert term>0
        terms+=term
    # For n>=3 the positive atoms are bounded by 4*c^2*n^4*exp(-c*n^2).
    # Successive majorants have ratio <=(4/3)^4 exp(-7c)<1.
    ratio=(arb(4)/3)**4*(-7*c).exp()
    assert ratio<1
    tail=4*c*c*81*(-9*c).exp()/(1-ratio)
    return (x/2).exp()*(terms+nonnegative_enclosure(tail))

def window(a,b):
    step=(b-a)/CELLS
    X=arb(0); moment=arb(0)
    for j in range(CELLS):
        lo=a+j*step; hi=a+(j+1)*step
        x=lo.union(hi)
        density=phi(x)
        X+=step*(y*x).cosh()*density
        moment+=step*x*(y*x).sinh()*density
    assert X>0 and moment>0
    return X,moment,moment/X

windows=[window(arb(2).log(),arb(4).log()),
         window(arb(4).log(),arb(12).log())]
X1,J1,mu1=windows[0];X2,J2,mu2=windows[1]
gap=mu2-mu1
assert gap>0
# A separately enclosed logarithmic derivative uses finite Mangoldt powers.
P=arb(0)
for p in primes_to(LOGDERIV_CUTOFF):
    n=p
    while n<=LOGDERIV_CUTOFF:
        P+=arb(p).log()*arb(n)**(-s0)
        n*=p
P+=nonnegative_enclosure(prime_tail(LOGDERIV_CUTOFF,s0))
L=1/s0+1/(s0-1)-PI.log()/2+(s0/2).digamma()/2-P
Ctest=((1+y*y).sqrt()+1+2*abs(L))/(2*(y-gamma)).sqrt()
Ctest+=(1/(y+arb(1)/2)**2+1/(y-arb(1)/2)**2).sqrt()
# The source H2_(gamma+delta) / H_(gamma+delta) prior, hence strong-port bound.
prior_factor=(1+y*y+y**4).sqrt()
P1=arb(2).sqrt()*X1*(prior_factor+abs(mu1-L))/(2*(y-gamma-delta)).sqrt()
P2=arb(2).sqrt()*X2*(prior_factor+abs(mu2-L))/(2*(y-gamma-delta)).sqrt()
T=prime_tail(PRIME_CUTOFF,sigma)
Delta=arb(2).sqrt()*gap/(2*y)  # value per w_seam
cutoff_error=3*Ctest*T*(P1/X1+P2/X2)
noise_error=Ctest*NOISE*(1/X1+1/X2)
error=cutoff_error+noise_error
assert error<Delta/2
certified_real_margin=Delta-error
assert certified_real_margin>0
# These coarse decimal claims are themselves verified, not rounded assertions.
assert gap>arb('0.6')
assert certified_real_margin>arb('0.14')
# Implementable rational calibration: no exact unknown X_i or L is used
# in this second, reported measurement functional. Their enclosures below
# propagate the calibration discrepancy into its true full-response value.
Xhat1=arb('0.00056');Xhat2=arb('1e-18');Lhat=arb('0.13668993')
Ctest_hat=((1+y*y).sqrt()+1+2*abs(Lhat))/(2*(y-gamma)).sqrt()
Ctest_hat+=(1/(y+arb(1)/2)**2+1/(y-arb(1)/2)**2).sqrt()
rounded_signal=arb(2).sqrt()/(2*y)*(X2/Xhat2*(mu2+L-2*Lhat)
                                           -X1/Xhat1*(mu1+L-2*Lhat))
rounded_error=Ctest_hat*((NOISE+3*T*P1)/Xhat1+(NOISE+3*T*P2)/Xhat2)
rounded_margin=rounded_signal-rounded_error
assert rounded_margin>arb('0.12')
# Direct finite-prime scalar observation: all powers of each included
# prime sum geometrically on this Euler fibre. The window residual stays
# at its fixed all-prime value; it is not refitted to the cutoff.
P_included=sum((arb(p).log()/(arb(p)**s0-1)
                for p in primes_to(PRIME_CUTOFF)),arb(0))
L_finite=1/s0+1/(s0-1)-PI.log()/2+(s0/2).digamma()/2-P_included
finite_scalar=arb(2).sqrt()/(2*y)*(X2/Xhat2*(mu2+2*L_finite-L-2*Lhat)
                                         -X1/Xhat1*(mu1+2*L_finite-L-2*Lhat))
finite_noisy_margin=finite_scalar-Ctest_hat*NOISE*(1/Xhat1+1/Xhat2)
assert finite_noisy_margin>arb('0.12')

result={'passed':True,'arithmetic':'python-flint Arb real balls, 160 bits',
 'theta_convention':'Phi(x)=exp(x/2) sum_n (4 a_n^2-6 a_n) exp(-a_n), a_n=pi*n^2*exp(2x)',
 'parameters':{'spectral_point':'3i','receiver_gamma':2,'prior_delta':'1/2',
 'forcing_beta':4,'interval_cells_per_window':CELLS,'explicit_theta_atoms':[1,2],
 'prime_cutoff':PRIME_CUTOFF,'included_prime_count':len(primes_to(PRIME_CUTOFF)),
 'logderivative_mangoldt_cutoff':LOGDERIV_CUTOFF,
 'measurement_noise_per_feature':'1e-22',
 'rational_observer_calibration':{'Xhat1':'0.00056','Xhat2':'1e-18','Lhat':'0.13668993'}}, 
 'rigorous_balls':{name:str(value) for name,value in {
 'X1':X1,'X2':X2,'mu1':mu1,'mu2':mu2,'moment_gap':gap,
 'L_at_7_over_2':L,'observer_test_norm':Ctest,'prior_port_bound_1':P1,
 'prior_port_bound_2':P2,'prime_tail_T_N':T,'witness_per_seam_weight':Delta,
 'finite_prime_error_per_seam_weight':cutoff_error,
 'measurement_error_per_seam_weight':noise_error,
 'total_error_per_seam_weight':error,
 'certified_real_observation_per_seam_weight':certified_real_margin,
 'rounded_observer_full_signal':rounded_signal,'rounded_observer_error':rounded_error,
 'rounded_observer_certified_real_margin':rounded_margin,
 'direct_finite_prime_scalar':finite_scalar,
 'direct_finite_prime_noisy_margin':finite_noisy_margin}.items()},
 'certified_claims':{'moment_gap_exceeds_0_6':True,'total_error_below_half_witness':True,
 'real_observation_exceeds_0_14_times_seam_weight':True,
 'rationally_calibrated_observation_exceeds_0_12_times_seam_weight':True,
 'direct_finite_prime_evaluation_confirms_margin':True},
 'scope':'Conditional certificate for noisy finite-prime labelled responses of the actual source witness, including an explicitly rationally calibrated observer with calibration error enclosed. Infinite theta and prime tails are enclosed; the archimedean response itself is held exact. No noisy response vector or reconstruction is manufactured.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/finite-prime-attachment-noise-certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
