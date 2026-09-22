"""Arb certificate for uniform finite-cutoff escape on source-prior balls.

All prime powers and the analytic archimedean response are retained.
No PNT remainder, floating quadrature, or zero-trace condition is used.
"""
from pathlib import Path
from math import isqrt
import json
from flint import arb,ctx

ctx.prec=192
CUTOFF=100000
r=arb(1)/4

def primes_to(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if sieve[p]]

primes=primes_to(CUTOFF)
P=arb(CUTOFF);sqrtP=P.sqrt()
w=arb(0)
# W(x)=0 on (0,2): exact integrals there.
abs_integral=4*arb(2).sqrt()
square_integral=arb(8)
power_norm=arb(0)
for index,p in enumerate(primes):
    ap=arb(p);lp=ap.log();sp=ap.sqrt()
    w+=lp/sp
    power_norm+=2*lp/(ap-sp) # both directions, all k>=2, exact geometric sum
    stop=primes[index+1] if index+1<len(primes) else CUTOFF
    # This is VERIFIED only for this finite prime list, not assumed globally.
    assert w<2*sp
    if stop>p:
        b=arb(stop);sb=b.sqrt();logratio=(b/ap).log()
        abs_integral+=4*(sb-sp)-w*logratio
        square_integral+=w*w*logratio-8*w*(sb-sp)+4*(b-ap)

mass=w/sqrtP
assert mass<2
mass_error=2-mass
D1=abs_integral/sqrtP
D2=(square_integral/P).sqrt()
K=mass_error+D1
H1_bound=(mass_error**2+D1**2).sqrt()
TV=mass+2

# |a_infty(xi)| <= c0 + log(sqrt(1+xi^2)).
c0=4+(4*arb.pi()).log()
arch_Hr=c0+1/(arb(1).exp()*r)
# Explicit unrestricted zero-extension H1(R+) -> H^r(R), r<1/2.
extension=(2**(r+1)*(1+1/(arb.pi()*(1-2*r)))).sqrt()

full_Hr_error=2*TV**(1-r)*H1_bound**r+(power_norm+arch_Hr)/sqrtP
# Trace-aware prime error, then the same exact higher-power and arch bounds.
halfline_error=2*(H1_bound+D2)+(power_norm+arch_Hr*extension)/sqrtP

result={'schema':'marici.grothendieck.certified-uniform-escape.v1',
        'arithmetic':'python-flint Arb real balls, 192 bits',
        'parameters':{'prime_cutoff':CUTOFF,'included_prime_count':len(primes),
                      'included_powers':'all powers of every prime <= cutoff',
                      'fractional_exponent':'1/4','halfline_prior':'unrestricted H1(R+) norm <= M'},
        'rigorous_balls':{name:str(value) for name,value in {
            'first_prime_mass':mass,'mass_discrepancy':mass_error,
            'tail_discrepancy_L1':D1,'tail_discrepancy_L2':D2,'K_P':K,
            'one_profile_H1_error_bound':H1_bound,'signed_measure_total_variation':TV,
            'higher_power_operator_bound':power_norm,
            'archimedean_Hquarter_operator_bound':arch_Hr,
            'unrestricted_zero_extension_bound':extension,
            'normalized_full_Hquarter_error_per_prior_unit':full_Hr_error,
            'normalized_halfline_H1_error_per_prior_unit':halfline_error}.items()},
        'scope':'Rigorous global ordinary-L2 approximation error for normalized finite-place fields and exact moving profiles. Includes higher powers and a uniform bound for the unchanged analytic gamma multiplier. Does not discretize a response, certify a measured attachment, or redefine the operator.'}
assert D1>0 and D2>0 and H1_bound>0
# Concrete rational certificates are checked against entire Arb balls.
assert full_Hr_error<arb('4')
assert halfline_error<arb('0.72')
result['certified_claims']={'Hquarter_error_below_4_times_prior':True,
                            'unrestricted_halfline_H1_error_below_0_72_times_prior':True,
                            'all_finite_step_signs_certified':True}
result['passed']=True
root=Path(__file__).resolve().parents[3]
p=root/'research/grothendieck/results/certified-uniform-escape.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
