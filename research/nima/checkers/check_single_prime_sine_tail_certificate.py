"""Exact rational certificate for the one-prime gamma/prime odd sine tail.

Analytical inputs: Binet's integral, digamma real-part series, unitary Fourier
normalization and the recorded combined-symbol convention. No floating-point
or computed prolate eigenvalue is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


def main():
    L=Q(7,20)
    R=10000
    N=40000
    delta=Q(1,20)
    # Inherited Binet exterior bound at z=1/4+5000i, valid beyond it too.
    gamma_exterior=(Q(17,2)-Q(23,20)-Q(1,30000)-Q(1,200000000))/Q(88,7)
    prime_upper=Q(7,10)*Q(71,100)
    gamma_numerator_upper=1+Q(11,7)+Q(21,10)+Q(23,20)
    # pi>3 and beta_(N+1)>2R make the direct sine-tail band bound rational.
    theta_upper=Q(64)*L*R/(Q(9)*27*N)
    c=delta-(delta+1)*theta_upper
    t=L/2
    sinh_upper=t/(1-t*t)
    endpoint_norm_tail=8*L*sinh_upper*sinh_upper/(9*N)
    endpoint_leverage_tail=endpoint_norm_tail/c
    checks={
        'one_prime_enters_by_exp_lower_sum':sum(Q(7,10)**k/__import__('math').factorial(k) for k in range(4))>2,
        'binet_exterior_beats_prime_plus_delta':gamma_exterior>prime_upper+delta,
        'digamma_global_lower_exceeds_minus_half':gamma_numerator_upper<6,
        'prime_upper_below_half':prime_upper<Q(1,2),
        'all_global_symbol_values_exceed_minus_one':gamma_numerator_upper/Q(12)+prime_upper<1,
        'sine_tail_frequencies_exceed_twice_band':Q(3)*(N+1)/L>2*R,
        'band_leakage_below_one_over_42':theta_upper<Q(1,42),
        'certified_tail_margin':c==Q(209,8100) and c>Q(1,40),
        'endpoint_sinh_majorant_domain':0<t<1,
        'endpoint_tail_leverage_below_one_over_100000':endpoint_leverage_tail<Q(1,100000),
    }
    assert all(checks.values()),checks
    result={
        'schema':'marici.nima.single-prime-sine-tail-certificate.v1',
        'strength':'fixed_support_analytic_tail_theorem_with_exact_rational_constants',
        'L':str(L),'frequency_band_R':R,'odd_sine_cutoff_N':N,
        'checks':checks,
        'gamma_exterior_lower':str(gamma_exterior),
        'prime_upper':str(prime_upper),
        'band_leakage_upper':str(theta_upper),
        'bulk_tail_lower_bound':str(c),
        'unnormalized_endpoint_squared_tail_upper':str(endpoint_norm_tail),
        'unnormalized_endpoint_tail_leverage_upper':str(endpoint_leverage_tail),
        'bulk':'recorded gamma-minus-finite-prime multiplier compressed to odd L2(-L,L)',
        'endpoint':'sqrt(2)*sinh(x/2), no extra physical coefficient assumed',
        'finite_low_block_computed':False,
        'low_high_coupling_certified':False,
        'whole_schur_positivity_proved':False,
        'support_uniformity_proved':False,
    }
    out=Path(__file__).resolve().parents[1]/'results/single-prime-sine-tail-certificate.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
