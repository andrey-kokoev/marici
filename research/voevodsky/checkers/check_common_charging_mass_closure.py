"""Close absolute and relative masses under the recovered common charging law.

Occupied source channels cost one shared elementary gap. The existing
charged-core dressing law supplies N=1836, not a fitted particle offset.
Exact elimination shows the shared displacement law cannot match both ratios.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]


def receipt(path):
    raw = path.read_bytes()
    return json.loads(raw), sha256(raw).hexdigest()


def main():
    bridge, bridge_hash = receipt(BASE/'results/geometry_comparison_energy_bridge.json')
    assert bridge['verification_passed']
    counts = bridge['counts']
    n = sum(counts['proton'].values())
    assert n==sum(counts['belt'].values())==1836
    # Reuse the prior charged-core record law. At c=0 the empty record
    # minimizes n_s+2*(n_s-c)^2; at c=1 the occupied record minimizes it.
    minima = {}
    for core in (0, 1):
        energies = {record: F(record)+2*F(record-core)**2 for record in (0, 1)}
        winner = min(energies, key=energies.get)
        assert winner==core
        minima[str(core)] = {'record_occupation': winner,
                             'energy_per_record': str(energies[winner])}
    assert F(minima['0']['energy_per_record'])==0
    assert F(minima['1']['energy_per_record'])==1
    interacting, interacting_hash = receipt(BASE/'results/interacting_elementary_reference.json')
    assert interacting['verification_passed']
    mediator, mediator_hash = receipt(BASE/'results/neutral_mediator_mass_bridge.json')
    assert mediator['verification_passed']
    d = -F(mediator['proton_exact_ground_relative_to_mu'])
    assert d==F(1,4)
    electron_rest = 1-d
    proton_rest = n-d
    b_lo, b_hi = map(F, mediator['certified_controls'][-1]['belt_ground_interval'])
    neutron_interval = (n+b_lo, n+b_hi)
    p_ratio = proton_rest/electron_rest
    splitting = ((b_lo+d)/electron_rest, (b_hi+d)/electron_rest)
    assert electron_rest==F(interacting['oscillator_elementary_rest_energy'])
    assert splitting==tuple(map(F, interacting['splitting_per_dressed_elementary_interval']))
    ref_path = BASE.parent/'nima/results/proton-hydrogen-helium-structure.json'
    refs, ref_hash = receipt(ref_path)
    rp, rn = F(refs['inputs']['proton_me']), F(refs['inputs']['neutron_me'])
    target = rn-rp
    electron_eV = F(refs['inputs']['electron_rest_energy_eV'])
    assert p_ratio>rp
    # Eliminate the displacement scale d from rp=(N-d)/(1-d).
    required_d = (rp-n)/(rp-1)
    assert 0<required_d<1
    assert (n-required_d)/(1-required_d)==rp
    max_split = required_d/(1-required_d)
    assert max_split==(rp-n)/(n-1)
    assert 0<max_split<target
    # Any profile lies in -d <= e_b <= 0, so its splitting <=d.
    # Regression the scale-free identity at independent rational parameters.
    for trial_d in (F(0), F(1,10000), F(1,4), F(3,4), F(99,100)):
        rtrial = (n-trial_d)/(1-trial_d)
        assert trial_d/(1-trial_d)==(rtrial-n)/(n-1)
        for fraction in (F(0), F(1,3), F(1)):
            eb = -trial_d*fraction
            assert 0<=(eb+trial_d)/(1-trial_d)<=(rtrial-n)/(n-1)
    # Independently, positive mu_e=1 gives the profile-independent bound
    # splitting/electron <= d/(1-d)=1/3 at the frozen half-gap vertex.
    assert splitting[1]<=d/(1-d)==F(1,3)<target
    report = {
        'verification_passed': True,
        'source_sha256': {'geometry_bridge': bridge_hash,
                          'interacting_elementary': interacting_hash,
                          'mediator': mediator_hash,
                          'held_out_reference': ref_hash},
        'charging_law_reused': 'One shared unit per occupied channel; n+2*(n-c)^2 locks the channel to its core.',
        'single_channel_ground_checks': minima,
        'source_channels': n,
        'bare_sector_baselines': {'elementary': '1', 'proton': str(n), 'belt': str(n)},
        'frozen_field_absolute_readout': {
            'elementary_rest_clock_units': str(electron_rest),
            'proton_rest_clock_units': str(proton_rest),
            'belt_rest_clock_interval': list(map(str, neutron_interval)),
            'proton_per_interacting_elementary': str(p_ratio),
            'proton_per_interacting_elementary_decimal': float(p_ratio),
            'reference_proton_per_electron': str(rp),
            'splitting_per_interacting_elementary': list(map(str, splitting)),
            'matches_absolute_and_relative_references': False},
        'all_couplings_no_go': {
            'assumptions': ['Common occupied-channel gap for all N intrinsic channels',
                            'Elementary occupation baseline one',
                            'Identical normalized projector-displacement field law',
                            'Proton and elementary contacts are their coherent modes',
                            'Stable elementary sector 0<=d<1; belt ground shift in [-d,0]'],
            'identity': 'splitting/electron <= (proton/electron-N)/(N-1)',
            'displacement_required_to_match_proton_ratio': str(required_d),
            'maximum_splitting_electron_units_if_proton_matches': str(max_split),
            'maximum_splitting_eV_if_proton_matches': float(max_split*electron_eV),
            'reference_splitting_electron_units': str(target),
            'reference_splitting_eV': float(target*electron_eV),
            'simultaneous_match_possible': False},
        'geometry_only_repair_at_frozen_vertex': {
            'maximum_splitting_per_elementary': '1/3',
            'reference_splitting_per_electron': str(target),
            'possible': False},
        'parameters_fitted_back_into_model': False,
        'next_gate': 'Change a source-supported charging or elementary-sector interaction, not the overall clock, field cutoff or contact geometry within this common-law family.',
    }
    out = BASE/'results/common_charging_mass_closure.json'
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__=='__main__':
    main()
