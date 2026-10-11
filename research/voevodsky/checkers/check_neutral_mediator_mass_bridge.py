"""Complete scalar-mediator interaction on source-derived all-face contacts.

New uniform law: Delta=E_star, g=E_star/2, oscillator Fock semantics.
Exact rational Schur-tail bounds certify the infinite oscillator, not just a
cutoff diagonalization. No empirical mass enters parameter selection.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]
DELTA, G = F(1), F(1, 2)


def matrix(rows, cutoff, energy, tail=False, pool=None):
    d = len(rows)
    n = d*(cutoff+1)
    h = [[F(0) for _ in range(n)] for _ in range(n)]
    for level in range(cutoff+1):
        for i, (pole, _) in enumerate(rows):
            h[level*d+i][level*d+i] = pole+DELTA*level-energy
            if level<cutoff:
                for j, (_, weight) in enumerate(rows):
                    contraction = F(1) if pool is None else 1-F(level, pool)
                    h[level*d+i][(level+1)*d+j] = G*(level+1)*contraction*weight
                    h[(level+1)*d+i][level*d+j] = G*weight
    if tail:
        # On levels >=cutoff+1: H >= Delta*N/2-2*g^2/Delta.
        lower = DELTA*(cutoff+1)/2-2*G*G/DELTA
        assert lower>energy
        contraction = F(1) if pool is None else 1-F(cutoff, pool)
        correction = G*G*(cutoff+1)*contraction/(lower-energy)
        for i in range(d):
            for j, (_, weight) in enumerate(rows):
                h[cutoff*d+i][cutoff*d+j] -= correction*weight
    # Unnormalized Fock basis |n>'=sqrt(n!)*|n>, spectral-coordinate
    # metric diag(contact weights). This avoids all irrational coefficients.
    norms = [F(1)]
    for level in range(1, cutoff+1):
        contraction = F(1) if pool is None else 1-F(level-1, pool)
        norms.append(norms[-1]*level*contraction)
    metric = [norms[level]*w for level in range(cutoff+1) for _, w in rows]
    s = [[metric[i]*h[i][j] for j in range(n)] for i in range(n)]
    assert all(s[i][j]==s[j][i] for i in range(n) for j in range(n))
    return s


def positive_definite(s):
    n = len(s)
    lower = [[F(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        pivot = s[i][i]-sum(lower[i][k]**2*pivots[k] for k in range(i))
        if pivot<=0:
            return False
        pivots.append(pivot)
        for j in range(i+1, n):
            lower[j][i] = (s[j][i]-sum(lower[j][k]*lower[i][k]*pivots[k]
                                     for k in range(i)))/pivot
    return True


def bounds(rows, cutoff, pool=None):
    # Tail-corrected PD implies positivity of the full infinite operator.
    lo, hi = F(-1), F(0)
    assert positive_definite(matrix(rows, cutoff, lo, tail=True, pool=pool))
    assert not positive_definite(matrix(rows, cutoff, hi, tail=True, pool=pool))
    for _ in range(42):
        mid = (lo+hi)/2
        if positive_definite(matrix(rows, cutoff, mid, tail=True, pool=pool)):
            lo = mid
        else:
            hi = mid
    certified_lower = max(-G*G/DELTA, lo)
    # Non-PD finite principal section gives a variational upper bound.
    lo, hi = -G*G/DELTA, F(0)
    assert positive_definite(matrix(rows, cutoff, lo, pool=pool))
    assert not positive_definite(matrix(rows, cutoff, hi, pool=pool))
    for _ in range(42):
        mid = (lo+hi)/2
        if positive_definite(matrix(rows, cutoff, mid, pool=pool)):
            lo = mid
        else:
            hi = mid
    assert certified_lower<hi<0
    return certified_lower, hi


def main():
    path = BASE/'results/all_face_contact.json'
    raw = path.read_bytes()
    source = json.loads(raw)
    assert source['verification_passed']
    spectra = {}
    for name, carrier in source['carriers'].items():
        spectra[name] = list(zip(map(F, carrier['normalized_profile_poles']),
                                map(F, carrier['normalized_profile_weights'])))
        assert len(carrier['cross_face_edges'])==6
        assert sum(w for _, w in spectra[name])==1
    assert spectra['proton']==[(F(0), F(1))]
    assert spectra['belt']==[(F(0), F(2386,4485)), (F(4485,3292), F(2099,4485))]
    p_ground = -G*G/DELTA
    controls = []
    for cutoff in (4, 8):
        lo, hi = bounds(spectra['belt'], cutoff)
        assert p_ground<lo<hi<0
        controls.append({'cutoff': cutoff,
                         'belt_ground_interval': [str(lo), str(hi)],
                         'belt_ground_interval_decimal': [float(lo), float(hi)],
                         'belt_minus_proton_interval': [str(lo-p_ground), str(hi-p_ground)],
                         'belt_minus_proton_interval_decimal': [float(lo-p_ground), float(hi-p_ground)],
                         'infinite_tail_included': True})
    # A product trial in the coherent belt state already gives attraction.
    r = spectra['belt'][0][1]
    trial = -G*G*r*r/DELTA
    assert controls[-1]['belt_ground_interval_decimal'][1]<float(trial)<0
    report = {
        'verification_passed': True,
        'source_sha256': sha256(raw).hexdigest(),
        'law': 'H_s=mu I+E_star*(K_s+Delta*N+g*P_s*(a+a_dagger)); P_s=|W_s><W_s|.',
        'shared_parameters': {'Delta': str(DELTA), 'g': str(G)},
        'completed_square': 'K+Delta*(a+g*P/Delta)^dagger*(a+g*P/Delta)-(g^2/Delta)*P',
        'global_lower_bound_relative_to_mu': str(p_ground),
        'proton_exact_ground_relative_to_mu': str(p_ground),
        'belt_coherent_product_trial': str(trial),
        'certified_controls': controls,
        'spin_action': 'I_2 on every carrier and mediator operation; mediator is a scalar.',
        'species_number_charge_baryon_preserved': True,
        'stable_empty_reference_condition': 'mu>g^2/Delta in elementary-gap units',
        'elementary_gap_identification': 'Oscillator spacing equals E_star; g=E_star/2 is a declared uniform field vertex, not obtained by dropping projector diagonal terms.',
        'elementary_rest_mass_selected': False,
        'new_inputs': ['Neutral scalar Fock mediator', 'Projector-density displacement vertex', 'Common spacing and half-gap coupling rule'],
        'measured_mass_inputs': [],
        'scope': 'Complete shared-law construction and certified infinite-oscillator ordering; physical mediator and elementary rest-energy identification remain inputs to construct.',
    }
    out = BASE/'results/neutral_mediator_mass_bridge.json'
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__=='__main__':
    main()
