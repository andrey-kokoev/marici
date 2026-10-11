"""Actual tetrahedral spinor under the same neutral-record field law.

All-face source projection constructs a rank-two contact, retaining both spins.
An occupation-sector baseline of one unit is inherited from the previous
reference constructor. No mass data enter the interacting Hamiltonian.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from check_electron_tetrahedral_spinor import D, ident, adj, sm, ma, trace, gmm, G0

BASE = Path(__file__).resolve().parents[1]


def decode(z):
    return tuple(D(F(a), F(b)) for a, b in z)


def main():
    store_path = BASE/'results/electron_tetrahedral_spinor_store.json'
    raw = store_path.read_bytes()
    store = json.loads(raw)
    report_path = BASE/'results/electron_tetrahedral_spinor.json'
    electron = json.loads(report_path.read_text())
    assert electron['verification_passed']
    face = [tuple(tuple(decode(z) for z in row) for row in p)
            for p in store['face_projectors']]
    i8 = ident(8)
    l = tuple(tuple(face[i//2][i%2][j%2] if i//2==j//2 else G0
                    for j in range(8)) for i in range(8))
    # Every unordered face pair is a geometric tetrahedral shared edge.
    edges = [(i, j) for i in range(4) for j in range(i+1, 4)]
    degrees = [sum(i in pair for pair in edges) for i in range(4)]
    assert degrees==[3]*4
    b = tuple(tuple(face[i//2][i%2][j] for j in range(2)) for i in range(8))
    assert gmm(adj(b), b)==sm(2, ident(2))
    # Sum the six projected equal-phase edge contacts. Their raw map is
    # (3/sqrt(2))*B and Gram is 9*I_2; normalization gives J=B/sqrt(2).
    n = sm(F(1,2), gmm(b, adj(b)))
    assert gmm(n, n)==n and adj(n)==n
    assert trace(n)[0]==2 and trace(n)[1]==0
    assert gmm(l, n)==gmm(n, l)==n
    # The three supplied spinor stages are L, N, N. Uniform projector-defect
    # generators supply this control kinetic operator, not a rest offset.
    k = ma(ma(i8, sm(-1, l)), sm(2, ma(i8, sm(-1, n))))
    assert gmm(k, n)==tuple(tuple(G0 for _ in range(8)) for _ in range(8))
    assert gmm(k, n)==gmm(n, k)
    local_dark = ma(l, sm(-1, n))
    outer_dark = ma(i8, sm(-1, l))
    assert gmm(k, local_dark)==sm(2, local_dark)
    assert gmm(k, outer_dark)==sm(3, outer_dark)
    assert trace(local_dark)[0]==2 and trace(outer_dark)[0]==4
    # Any positive carrier-defect coefficients leave this ground argument
    # unchanged because the field contact is exactly the coherent doublet.
    pool_path = BASE/'results/finite_record_mediator_constructor.json'
    pool_raw = pool_path.read_bytes()
    pools = json.loads(pool_raw)
    assert pools['verification_passed']
    controls = []
    for item in pools['finite_pool_controls']:
        p_lo, p_hi = map(F, item['proton_ground_interval'])
        b_lo, b_hi = map(F, item['belt_ground_interval'])
        e_lo, e_hi = 1+p_lo, 1+p_hi
        assert 0<e_lo<=e_hi<1
        relative = ((b_lo-p_hi)/e_hi, (b_hi-p_lo)/e_lo)
        controls.append({'neutral_records': item['neutral_records'],
                         'dressed_elementary_rest_interval': list(map(str, (e_lo, e_hi))),
                         'splitting_per_dressed_elementary_interval': list(map(str, relative)),
                         'splitting_per_dressed_elementary_decimal': list(map(float, relative))})
    mediator_path = BASE/'results/neutral_mediator_mass_bridge.json'
    mediator_raw = mediator_path.read_bytes()
    mediator = json.loads(mediator_raw)
    assert mediator['verification_passed']
    split = tuple(map(F, mediator['certified_controls'][-1]['belt_minus_proton_interval']))
    electron_rest = F(3,4)
    ratio = tuple(x/electron_rest for x in split)
    reference_path = BASE.parent/'nima/results/proton-hydrogen-helium-structure.json'
    reference_raw = reference_path.read_bytes()
    inputs = json.loads(reference_raw)['inputs']
    target = F(inputs['neutron_me'])-F(inputs['proton_me'])
    measured_electron_rest = F(inputs['electron_rest_energy_eV'])
    assert ratio[1]<target
    result = {
        'verification_passed': True,
        'source_sha256': {'electron_spinor_store': sha256(raw).hexdigest(),
                          'finite_pool': sha256(pool_raw).hexdigest(),
                          'oscillator': sha256(mediator_raw).hexdigest()},
        'all_face_contacts': edges,
        'all_face_contact_derivation': 'Equal-phase projected sum has Gram 9*I_2; normalized map is J; P_e=J*J_dagger=N_e.',
        'logical_contact_rank': 2,
        'single_spin_selection': False,
        'kinetic_control_spectrum': {'0': 2, '2': 2, '3': 4},
        'kinetic_rule': 'Uniform defects of the supplied L,N,N stages; result unchanged for positive defect coefficients.',
        'field_rule': 'Same neutral pool and g=1/2, Delta=1, P_e=N_e; no elementary-specific vertex.',
        'empty_reference': 'Same ready neutral pool, same scalar generator contribution subtracted in all sectors.',
        'bare_elementary_sector_offset': '1',
        'offset_origin': 'Previous elementary occupation-sector constructor, not selected by the return projector.',
        'finite_pool_controls': controls,
        'oscillator_elementary_rest_energy': str(electron_rest),
        'splitting_per_dressed_elementary_interval': list(map(str, ratio)),
        'splitting_per_dressed_elementary_decimal': list(map(float, ratio)),
        'held_out_mass_comparison': {
            'reference_increment_electron_units': str(target),
            'predicted_increment_eV_interval': [float(x*measured_electron_rest) for x in ratio],
            'reference_increment_eV': float(target*measured_electron_rest),
            'matches_reference': False,
            'reference_sha256': sha256(reference_raw).hexdigest()},
        'spin_and_charge': 'Field acts as a scalar on the full negative-polarization doublet; no species or charge conversion.',
        'next_gate': 'Source the elementary sector charging/rest-offset law. Same-field dressing changes the denominator to 3/4 but does not close the numerical mass comparison.',
    }
    out = BASE/'results/interacting_elementary_reference.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__=='__main__':
    main()
