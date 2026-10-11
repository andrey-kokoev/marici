"""Replay the known bond/error-register control on the bridged source.

This is not a new Hamiltonian proposal. It tests whether the retained geometric,
phase and seam data alone force the existing satisfied-interface occupation
interpretation. An immutable content-addressed bundle makes the test resumable.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json

from check_constraint_energy_accounting import identity, plus, times, compose, adjoint, trace
from check_belt_three_by_twelve import decode

BASE = Path(__file__).resolve().parents[1]


def matrix(entries):
    return {(i,j):decode(v) for i,j,v in entries}


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(',',':'))+'\n').encode()


def freeze_inputs():
    paths = {
        'native': BASE/'results/native_operation_energy_lift_store.json',
        'bridge': BASE/'results/geometric_phase_energy_bridge.json',
        'occupation': BASE/'results/seam_occupation_energy.json',
    }
    raw = {key:path.read_bytes() for key,path in paths.items()}
    records = {key:json.loads(data) for key,data in raw.items()}
    assert records['bridge']['status']=='partial_bridge_checked'
    assert records['occupation']['verification_passed']
    assert records['occupation']['source_sha256']==sha256(raw['native']).hexdigest()
    for key in ('native','occupation'):
        locator = str(paths[key].relative_to(BASE.parent))
        assert records['bridge']['sources'][locator]==sha256(raw[key]).hexdigest()
    bundle = {'schema':'marici.phase-occupation-source.v1', 'records':records,
              'source_sha256':{key:sha256(data).hexdigest() for key,data in raw.items()},
              'source_locators':{key:str(path.relative_to(BASE.parent.parent)) for key,path in paths.items()},
              'interpretation':'The same retained source and carrier are used in both register-role controls.'}
    data = canonical(bundle)
    digest = sha256(data).hexdigest()
    path = BASE/'results/phase-occupation-sources'/f'{digest}.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        assert path.read_bytes()==data
    else:
        path.write_bytes(data)
    return path,bundle,digest


def check(bundle):
    native = bundle['records']['native']['carriers']['belt']
    bridge = bundle['records']['bridge']['proton_and_belt']['belt']
    assert bridge['all_native_seam_projectors_reconstructed_exactly']
    assert bridge['native_phase_and_alignment_H_reconstructed_exactly']
    metric = tuple(map(Q,native['metric_denominators']))
    n = len(metric)
    I = identity(n)
    N = matrix(native['return_entries'])
    H = matrix(native['native_energy_entries'])
    seam_records = native['seam_projectors']
    seams = [matrix(row['entries']) for row in seam_records]
    assert len(seams)==21 and trace(N,n)==1 and compose(N,N)==N
    assert compose(H,N)=={}
    for P in seams:
        assert compose(P,P)==P and adjoint(P,metric)==P
        assert compose(P,N)=={}
        assert compose(plus(I,times(-1,P)),N)==N
    assert any(compose(a,b)!=compose(b,a) for a,b in zip(seams,seams[1:]))
    epsilon,J,kappa = Q(1,4),Q(1,2),Q(1)
    assert 0<epsilon<J and kappa>epsilon
    # Both models retain the identical 21 labelled register slots and c=1.
    # h = kappa*p + epsilon*n + J*(n-S)^2, g=0.
    # Only the physical interpretation of S differs.
    controls = {}
    for name in ('satisfied_interface','defect_syndrome'):
        spectrum = {}
        for p in (0,1):
            S = 1-p if name=='satisfied_interface' else p
            for occupation in (0,1):
                spectrum[p,occupation] = kappa*p+epsilon*occupation+J*(occupation-S)**2
        if name=='satisfied_interface':
            ground,occupied,defect_bound = epsilon,1,kappa-epsilon
        else:
            ground,occupied,defect_bound = Q(0),0,kappa+epsilon
        assert spectrum[0,occupied]==ground
        assert all(value-ground-defect_bound*p>=0 for (p,_),value in spectrum.items())
        assert spectrum[0,1-occupied]>ground and defect_bound>0
        # Summing these local positive bounds is valid for noncommuting P_e:
        # H_total - 21*ground >= H_native + defect_bound*sum_e P_e >= 0.
        # N tensor the indicated register product attains it term by term.
        controls[name] = {
            'register_slots':len(seams), 'source_return':'same rank-one N',
            'control':'c-P_e' if name=='satisfied_interface' else 'P_e',
            'local_p_n_energies':{f'p={p},n={occupation}':str(value) for (p,occupation),value in spectrum.items()},
            'occupation_on_return':occupied,
            'vacuum_subtracted_register_energy':str(len(seams)*ground),
            'positive_residual_defect_coefficient':str(defect_bound),
            'zero_native_constraint_energy':True,
            'same_retained_record_labels_and_phase_data':True,
            'carrier_return_preserved':True,
        }
    assert controls['satisfied_interface']['vacuum_subtracted_register_energy']=='21/4'
    assert controls['defect_syndrome']['vacuum_subtracted_register_energy']=='0'
    assert bundle['records']['occupation']['defect_control_rule_increment_on_N'].startswith('0;')
    return {'source_seam_records':len(seams), 'all_existing_control_identities_replayed':True,
            'controls':controls,
            'retained_source_forces_occupation':False,
            'reason':'The admitted geometry, phases, metrics and return constraints hold in both completions. A physical register role/coupling is extra information; retaining a record label does not impose n=1.',
            'electron_gate':bundle['records']['bridge']['electron_gate'],
            'novelty':'This binds and replays the earlier bond-versus-syndrome control on the new geometric phase bridge; the control itself was already known.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot',type=Path,help='Replay the frozen bundle without consulting mutable source stores')
    args = parser.parse_args()
    if args.snapshot:
        raw = args.snapshot.read_bytes()
        digest = sha256(raw).hexdigest()
        assert args.snapshot.stem==digest,'Content-addressed snapshot digest mismatch'
        bundle,path = json.loads(raw),args.snapshot.resolve()
    else:
        path,bundle,digest = freeze_inputs()
    result = check(bundle)
    report = {'status':'nonnecessity_control_verified', 'result':result,
              'immutable_source_snapshot':path.relative_to(BASE.parent.parent).as_posix(),
              'snapshot_sha256':digest,
              'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
              'implementation_sha256':{name:sha256((BASE/'checkers'/name).read_bytes()).hexdigest()
                  for name in ('check_constraint_energy_accounting.py','check_belt_three_by_twelve.py','check_coupled_six_piece_belt.py')},
              'scope':'Exact local positive bounds on the existing zero-mixing fixture, not a new mass model or a proof that every possible source extension leaves occupation free.'}
    (BASE/'results/phase_occupation_necessity.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
