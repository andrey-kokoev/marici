"""Finite neutral-record constructor and direct elementary-rest reference test.

Source-addressed controlled involutions are assembled from the all-face
projector and signed record maps. The pool normalization is a declared uniform
collective rule, shared by both carriers and by the empty reference.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from check_neutral_mediator_mass_bridge import bounds, DELTA, G

BASE = Path(__file__).resolve().parents[1]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def tensor(a, b):
    return [[x*y for x in row for y in br] for row in a for br in b]


def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def proton_interval(pool):
    # M independent two-level records: E=M*(1-sqrt(1+1/M))/2.
    q = 1+F(1, pool)
    lo, hi = F(1), F(2)
    for _ in range(90):
        mid = (lo+hi)/2
        if mid*mid<q:
            lo = mid
        else:
            hi = mid
    assert lo*lo<q<=hi*hi
    return pool*(1-hi)/2, pool*(1-lo)/2


def main():
    path = BASE/'results/all_face_contact.json'
    raw = path.read_bytes()
    source = json.loads(raw)
    assert source['verification_passed']
    gate_checks = {}
    spectra = {}
    x = [[F(0), F(1)], [F(1), F(0)]]
    bit_i = identity(2)
    for name, carrier in source['carriers'].items():
        rows = list(zip(map(F, carrier['normalized_profile_poles']),
                        map(F, carrier['normalized_profile_weights'])))
        spectra[name] = rows
        weights = [w for _, w in rows]
        d = len(rows)
        p = [weights[:] for _ in range(d)]
        i = identity(d)
        complement = add(i, p, -1)
        assert mm(p, p)==p
        px = tensor(p, x)
        spectator = tensor(complement, bit_i)
        rplus = add(spectator, px)
        rminus = add(px, spectator, -1)
        ii = identity(2*d)
        assert mm(rplus, rplus)==mm(rminus, rminus)==ii
        qplus = [[v/2 for v in row] for row in add(ii, rplus, -1)]
        qminus = [[v/2 for v in row] for row in add(ii, rminus, -1)]
        assert add(qplus, qminus)==add(ii, px, -1)
        metric = [w for w in weights for _ in range(2)]
        for r in (rplus, rminus):
            assert all(metric[a]*r[a][b]==metric[b]*r[b][a]
                       for a in range(2*d) for b in range(2*d))
        gate_checks[name] = {
            'two_signed_controlled_involutions': True,
            'weighted_self_adjoint': True,
            'sum_of_generators': 'I-P tensor X',
            'ready_record_history_reversible': True,
        }
    # Scalar Pauli Z record yields the elementary occupation generator.
    z = [[F(1), F(0)], [F(0), F(-1)]]
    occupation = [[v/2 for v in row] for row in add(bit_i, z, -1)]
    assert occupation==[[0, 0], [0, 1]]
    # The same occupation reader for a charged reference with logical spin.
    e_h = [[F(0), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    e_q = [[-v for v in row] for row in e_h]
    assert mm(e_h, e_q)==mm(e_q, e_h)
    assert [e_h[i][i] for i in range(3)]==[0, 1, 1]
    controls = []
    for pool in (16, 64, 256):
        p_lo, p_hi = proton_interval(pool)
        b_lo, b_hi = bounds(spectra['belt'], 8, pool=pool)
        assert p_hi<b_lo<b_hi<0
        assert -F(1,4)<p_lo
        # Other permutation irreps have effective pool M'=M-2k and
        # occupation offset k>=1. Their lower bound is k-g^2*M'/M.
        # It is positive; they cannot undercut the symmetric ground.
        other_irrep_lower = min(F(k)-G*G*F(pool-2*k, pool)
                               for k in range(1, pool//2+1))
        assert other_irrep_lower>0
        controls.append({
            'neutral_records': pool,
            'retained_occupation_cutoff': 8,
            'proton_ground_interval': list(map(str, (p_lo, p_hi))),
            'belt_ground_interval': list(map(str, (b_lo, b_hi))),
            'splitting_interval_decimal': [float(b_lo-p_hi), float(b_hi-p_lo)],
            'omitted_finite_pool_tail_included': True,
            'non_symmetric_irrep_lower_bound': str(other_irrep_lower),
        })
    # Reference values enter only AFTER constructing and checking the law.
    reference_path = BASE.parent/'nima/results/proton-hydrogen-helium-structure.json'
    reference_raw = reference_path.read_bytes()
    reference = json.loads(reference_raw)['inputs']
    reference_difference = F(reference['neutron_me'])-F(reference['proton_me'])
    oscillator = json.loads((BASE/'results/neutral_mediator_mass_bridge.json').read_text())
    assert oscillator['verification_passed']
    lo, hi = map(F, oscillator['certified_controls'][-1]['belt_minus_proton_interval'])
    assert hi<reference_difference
    electron_energy = F(reference['electron_rest_energy_eV'])
    report = {
        'verification_passed': True,
        'source_sha256': sha256(raw).hexdigest(),
        'signed_controlled_gate_checks': gate_checks,
        'finite_pool_law': 'sum n_j + (g/sqrt(M))*sum(Qplus_j+Qminus_j)',
        'empty_pool_energy': 'g*sqrt(M), same for every carrier and empty sector',
        'vacuum_subtracted_law': 'K+sum n_j-(g/sqrt(M))*P*sum X_j',
        'full_controlled_diagonal_terms_retained': True,
        'dicke_ladder_squared': '(n+1)*(1-n/M)',
        'oscillator_limit_on_fixed_occupation': 'sqrt((n+1)*(1-n/M)) -> sqrt(n+1)',
        'finite_pool_controls': controls,
        'spin_charge_species_action': 'Neutral scalar record pool; vertex commutes with all declared carrier spin and species labels.',
        'elementary_reference': 'H_e=0 direct_sum E_star*I_2, Q_e=0 direct_sum -I_2: one empty vacuum and occupied doublet E_star.',
        'elementary_gap_equals_reference_sector_rest_energy': True,
        'physical_electron_identification': 'Not derived by the occupation construction.',
        'held_out_direct_identification': {
            'rule': 'Identify E_star with electron rest energy, without changing the shared mediator law.',
            'predicted_neutron_proton_increment_electron_units': [str(lo), str(hi)],
            'reference_increment_electron_units': str(reference_difference),
            'predicted_increment_eV_interval': [float(lo*electron_energy), float(hi*electron_energy)],
            'reference_increment_eV': float(reference_difference*electron_energy),
            'matches_reference': False,
            'reference_sha256': sha256(reference_raw).hexdigest(),
        },
        'construction_inputs': ['Source all-face projector', 'Neutral record tensor copies', 'Controlled signed extensions of record flip', 'Collective 1/sqrt(M) normalization', 'Elementary charged occupation sector'],
        'next_gate': 'Construct the physical elementary sector and determine its relation to the collective clock; direct electron-unit identification fails the held-out splitting.',
    }
    out = BASE/'results/finite_record_mediator_constructor.json'
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__=='__main__':
    main()
