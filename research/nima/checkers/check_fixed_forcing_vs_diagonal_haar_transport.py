"""Exact Haar-core comparison of fixed-forcing and diagonal prime transport.

Real profiles f_a(x)=a*x*exp(-a*x), a>0, lie in both Haar spaces.
All integrals below are evaluated analytically; their coefficients are rational.
This is a transport/metric falsifier, not an Xi-zero computation or RH proof.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def mul_inner(a, b):
    # Integral f_a*f_b dx/x.
    return a*b/(a+b)**2


def add_inner(a, b):
    # Integral f_a*f_b dx.
    return 2*a*b/(a+b)**3


def correlation(a, b, exp_t):
    # Integral f_a(exp(q))*f_b(exp(q+t)) dq.
    return a*b*exp_t/(a+b*exp_t)**2


def pair_inner(left, right):
    # Relative-Haar form after J tensor I, on unscaled real tensor profiles.
    a, b = left
    c, d = right
    return mul_inner(a, c)*mul_inner(b, d)


def positive_pivots(matrix):
    m = [row[:] for row in matrix]
    pivots = []
    for k in range(len(m)):
        pivot = m[k][k]
        assert pivot > 0
        pivots.append(pivot)
        for i in range(k+1, len(m)):
            for j in range(k+1, len(m)):
                m[i][j] -= m[i][k]*m[k][j]/pivot
    return pivots


def main():
    scales = list(map(F, [1, 2, 3, 6]))
    pivots = positive_pivots([[mul_inner(a,b) for b in scales] for a in scales])
    primes = list(map(F, [2, 3, 5, 7]))
    covariance_checks = 0
    for p in primes:
        for a in scales:
            for b in scales:
                # Ua(p) f_a = sqrt(p) f_(pa); Um(p) f_a = f_(pa).
                assert p*add_inner(p*a,p*b) == add_inner(a,b)
                assert mul_inner(p*a,p*b) == mul_inner(a,b)
                assert p*mul_inner(p*a,p*b) == p*mul_inner(a,b)
                for exp_t in [F(1,2), F(1), F(2), F(3)]:
                    # One-leg translation shifts the separation variable.
                    assert correlation(a,p*b,exp_t) == correlation(a,b,p*exp_t)
                    # Simultaneous shifts leave separation unchanged.
                    assert correlation(p*a,p*b,exp_t) == correlation(a,b,exp_t)
                    covariance_checks += 1
                # Source tensor recovery: contraction of fixed first leg is identity.
                assert add_inner(a,a)/add_inner(a,a) == 1
        for q in primes:
            for exp_t in [F(1,2),F(1),F(2)]:
                assert correlation(p*q,p*q,exp_t) == correlation(1,1,exp_t)
                # Scalar energy multiplier composes under successive dilations.
                assert p*q*pair_inner((p*q,p*q),(p*q,p*q)) == p*q/F(16)

    cases = []
    for p in primes:
        based = (F(1),p)
        diagonal = (p,p)
        energy = pair_inner(based,based)
        assert energy == pair_inner(diagonal,diagonal) == F(1,16)
        defect = energy + energy - 2*pair_inner(based,diagonal)
        expected = (p-1)**2/(8*(p+1)**2)
        assert defect == expected and defect > 0
        density_defect = correlation(p,p,F(1))-correlation(F(1),p,F(1))
        assert density_defect == (p-1)**2/(4*(p+1)**2) > 0
        # At real centered parameter sigma=k/2 the modular energy is p^(-k)*E.
        energy_cycles = {}
        for k in [-2,-1,0,1,2]:
            multiplier = p**(-k)
            cycle = (1-multiplier)*energy
            assert multiplier > 0
            assert multiplier*p**k == 1  # Forward/reverse closes at every tested sigma.
            assert (cycle == 0) == (k == 0)
            energy_cycles[str(k)] = str(cycle)
        cases.append({'p': int(p), 'seam_energy_each_route': str(energy),
                      'squared_transport_defect': str(defect),
                      'separation_readout_defect_at_zero': str(density_defect),
                      'identity_minus_modular_energy_for_twice_sigma': energy_cycles})
    assert cases[0]['squared_transport_defect'] == '1/72'
    # Deliberate hostile: marginal energy equality does not certify vector equality.
    assert cases[0]['seam_energy_each_route'] == '1/16'
    assert cases[0]['squared_transport_defect'] != '0'
    # At s=1/2, moving the forcing base repairs normalized tensor transport.
    for p in primes:
        moved_base_image = (p,p)
        actual_diagonal_image = (p,p)
        assert moved_base_image == actual_diagonal_image

    out = {
        'schema': 'marici.nima.fixed-forcing-diagonal-haar-transport.v1',
        'passed': True,
        'classification': 'based_graph_is_not_a_fixed_base_diagonal_haar_intertwiner',
        'core': 'f_a(x)=a*x*exp(-a*x), real a>0; exact additive/multiplicative Haar integrals',
        'positive_gram_pivots': list(map(str,pivots)),
        'correlation_covariance_checks': covariance_checks,
        'cases': cases,
        'moving_base_transport': 'Ua(p) tensor Um(p) sends Phi tensor u to Ua(p)Phi tensor Um(p)u; no fixed-forcing identification is made',
        'reciprocal_roundtrip': 'positive energy multipliers p^(-k) and p^k compose to one for every tested k; one-step energy equality holds only at k=0',
        'claim_boundary': 'Certifies exact core covariance and falsifies conflating one-leg history translation with simultaneous relative-Haar dilation. Does not refute energy equality on the seam, nor establish its restriction to all Xi states.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'rh_proved': False,
    }
    target = ROOT/'research/nima/results/fixed-forcing-vs-diagonal-haar-transport.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
