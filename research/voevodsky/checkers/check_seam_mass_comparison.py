"""Held-out mass comparison of the fixed single-clock seam model.

Rounded empirical reference inputs are reused from a retained Nima receipt.
No mass is used to choose the model coefficients. All rejection inequalities
use rational enclosures of sqrt(5); decimal values are presentation only.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]


def main():
    reference_path = BASE.parent/'nima/results/proton-hydrogen-helium-structure.json'
    reference_raw = reference_path.read_bytes()
    reference = json.loads(reference_raw)
    mp = F(reference['inputs']['proton_me'])
    mn = F(reference['inputs']['neutron_me'])
    me_ev = F(reference['inputs']['electron_rest_energy_eV'])
    observed = mn-mp
    assert observed==F('2.530989')
    model_path = BASE/'results/single_clock_seam_record.json'
    model_raw = model_path.read_bytes()
    model = json.loads(model_raw)
    assert model['verification_passed'] and model['source_seams']==21
    assert model['fixed_parameters']=={'epsilon':'1','J':'1','g':'1/2','kappa':'1','flip_constant':'1/2'}
    assert model['extra_energy_per_seam']=={'0':'-1/2','4':'1/2'}

    denominator = 10**30
    k = isqrt(5*denominator*denominator)
    root_lo,root_hi = F(k,denominator),F(k+1,denominator)
    assert root_lo*root_lo<5<root_hi*root_hi
    def enclosure(a,b):
        return (a+b*root_lo,a+b*root_hi) if b>=0 else (a+b*root_hi,a+b*root_lo)
    def display(interval):
        return float(sum(interval)/2)

    geometry_path = BASE/'results/native_operation_energy_lift_store.json'
    geometry_raw = geometry_path.read_bytes()
    seam_rows = json.loads(geometry_raw)['carriers']['belt']['seam_projectors']
    edges = [tuple(row['triangles']) for row in seam_rows if max(row['triangles'])<6]
    assert model['source_sha256']==sha256(geometry_raw).hexdigest()
    assert len(edges)==7
    assert {tuple(row['triangles']) for row in seam_rows} == {
        (a+6*s,b+6*s) for a,b in edges for s in range(3)}
    # Diagnostic alternative implementations: retain a connected subgraph
    # in each paired sector and use the same subgraph under C3 rotation.
    # Removing seams changes the physical record network, not coordinates.
    connected = Counter()
    for mask in range(1<<len(edges)):
        selected = [edge for j,edge in enumerate(edges) if mask&(1<<j)]
        reached = {0}
        while True:
            old = set(reached)
            for a,b in selected:
                if a in reached or b in reached:
                    reached.update((a,b))
            if old==reached:
                break
        if len(reached)==6:
            connected[3*len(selected)] += 1
    assert connected==Counter({15:9,18:6,21:1})
    rows = []
    for identification in ('isolated_involution_gap_is_electron','inactive_dressed_record_gap_is_electron'):
        for count in sorted(connected):
            # delta=(sqrt(5)-1)/2. If sqrt(5)*E*=m_e c^2,
            # count*delta/sqrt(5) = count/2-count*sqrt(5)/10.
            a,b = (-F(count,2),F(count,2)) if identification.startswith('isolated') else (F(count,2),-F(count,10))
            low,high = enclosure(a,b)
            assert low>observed
            rows.append({'identification':identification,'registers':count,
                         'predicted_increment_me':display((low,high)),
                         'predicted_increment_MeV':display((low*me_ev/10**6,high*me_ev/10**6)),
                         'predicted_neutron_me_anchored_to_observed_proton':display((mp+low,mp+high)),
                         'excess_over_reference_me':display((low-observed,high-observed)),
                         'exact_prediction':{'rational':str(a),'sqrt5':str(b)},
                         'rational_enclosure_me':[str(low),str(high)],
                         'disposition':'overpredicts_the_rounded_reference_without_any_parameter_adjustment'})
    # Descriptive calibration only: E*/m_e needed to force this model's
    # 21-seam increment to agree. It is not fed back into the constructor.
    delta_low,delta_high = enclosure(F(-21,2),F(21,2))
    required_scale = (observed/delta_high,observed/delta_low)
    assert required_scale[1]<F(1,3)  # below either declared direct gap assignment
    report = {
        'verification_passed':True,
        'reference_status':reference['input_status'],
        'reference_refresh':'The initial audit attempted the NIST allascii endpoint and received HTTP 403; this offline checker reuses the retained rounded reference, not a fresh constants retrieval.',
        'comparison_assumptions':'Only the added seam energy splits equal bare carrier baselines; identify one of the two constructed reference gaps with m_e*c^2. Other contributions are not fitted to cancel the discrepancy.',
        'observed_proton_me':str(mp),'observed_neutron_me':str(mn),
        'observed_increment_me':str(observed),'observed_increment_MeV':float(observed*me_ev/10**6),
        'actual_source_registers':21,
        'connected_C3_subgraph_counts':dict(sorted(connected.items())),
        'predictions':rows,
        'both_direct_electron_identifications_rejected':True,
        'removing_only_redundant_seams_cannot_fix_comparison':True,
        'required_scale_Estar_over_electron_descriptive_only':display(required_scale),
        'required_scale_is_not_a_prediction':True,
        'atomic_mass_unit_conversion':'Cannot rescue a failed dimensionless mass ratio; no atomic binding correction is added to a free-neutron comparison.',
        'scope':'Rejects these direct reference identifications for the seam-only increment; does not refute belt formation or all possible physical interface Hamiltonians.',
        'source_sha256':{'rounded_reference':sha256(reference_raw).hexdigest(),'fixed_model':sha256(model_raw).hexdigest(),'seam_geometry':sha256(geometry_raw).hexdigest()}
    }
    (BASE/'results/seam_mass_comparison.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
