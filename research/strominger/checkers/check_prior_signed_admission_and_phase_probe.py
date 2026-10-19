"""Read-only audit of current signed-record admission and a phase discriminator.

Do not mutate the owning research ledger or treat conditional admission as
physical calibration. The phase probe is a specification, not an apparatus.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]


def main():
    paths={k:ROOT/p for k,p in {
        'net':'research/voevodsky/results/retained_reaggregation_conjecture_net.json',
        'physical':'research/voevodsky/contracts/retained-reaggregation-physical-admission-gate.v1.json',
        'source_k':'research/voevodsky/contracts/retained-reaggregation-source-k.v1.json',
        'contract':'research/voevodsky/contracts/retained-reaggregation-conjecture-net.v1.json',
        'calibration':'research/strominger/results/neutron-rest-gap-calibration.json',
        'phase_note':'research/nima/one-qubit-clifford-composition-exposes-the-horizontal-phase-kernel.md'}.items()}
    data={k:json.loads(p.read_text()) for k,p in paths.items() if k!='phase_note'}
    net=data['net'];checks={};mismatches=[];count=0
    for name in ('net','source_k','calibration'):
        for field in ('source_hashes','evidence_hashes'):
            for p,h in data[name].get(field,{}).items():
                current=ROOT/p;count+=1
                if not current.exists() or hashlib.sha256(current.read_bytes()).hexdigest()!=h:mismatches.append({'owner':name,'field':field,'path':p})
    # Preserve drift rather than refreshing the owning ledger or silently
    # treating its recorded theorem outcome as a freshly rerun proof.
    assert all(m['field']=='evidence_hashes' and m['path']=='research/nima/completion-refinement-conjecture-net.md' for m in mismatches),mismatches
    checks['current_contract_hashes_valid_and_supporting_drift_reported']=True
    assert net['target_outcome']=='++' and net['state']=='resolved-conditional-only'
    assert net['physical_admission'] is False and net['physical_gate']['evidence_package_count']==0
    assert data['source_k']['physical_admission'] is False
    assert data['physical']['current_state']=='not_admitted_no_physical_evidence_package_registered'
    assert data['contract']['frozen_comparison']['candidate_parameters']=={
        'record_gap':'1','vertex_g':'1/2','relative_native_orbital_unit':'1','readout_time':'1 model-time unit'}
    checks['conditional_completion_not_physical_energy_calibration']=True
    trials=data['calibration']['parameter_completions']
    # Both matched register Hamiltonians have the same eigenprojectors and
    # transition frequency, but differ by a scalar 33/40.
    scalar_shift=F(trials[1]['epsilon'])-F(trials[0]['epsilon'])
    assert scalar_shift==F(trials[1]['J'])-F(trials[0]['J'])==F(33,40)
    gaps=[F(t['rest_gap']['0']) for t in trials];assert gaps==[F(147,20),F(189,8)]
    assert gaps[1]-gaps[0]==F(651,40)
    # Exact ideal reference test at supplied t=40*pi model-time units.
    # A relative phase exp(-i E*t) is then +1 versus -1. A |+> control,
    # followed by X readout, distinguishes them perfectly in this ideal model.
    integers=[e*40 for e in gaps];assert all(k.denominator==1 for k in integers)
    phases=[(-1)**int(k) for k in integers];assert phases==[1,-1]
    control_states=[(F(1),F(p)) for p in phases] # numerator/sqrt(2)
    x_readings=[2*a*b/(a*a+b*b) for a,b in control_states];assert x_readings==[1,-1]
    checks['scalar_matched_Hamiltonian_difference_located']=True
    checks['ideal_relative_phase_probe_distinguishes_both_gap_candidates']=True
    result={'status':'passed','checks':checks,'hash_bindings_checked':count,
            'supporting_evidence_drift':mismatches,
            'freshness_scope':'Current contract hashes verified; one contextual supporting note has changed. Recorded conditional ++ is not promoted to a fresh theorem replay by this audit.',
            'current_signed_record_branch':{'conditional_outcome':net['target_outcome'],
                'physical_evidence_package_count':net['physical_gate']['evidence_package_count'],
                'physical_admission':False,'missing_physical_evidence_classes':net['physical_gate']['missing_evidence_classes'],
                'source_k_selection':data['source_k']['selection_basis'],
                'frozen_parameters':data['contract']['frozen_comparison']['candidate_parameters']},
            'phase_probe':{'matched_register_scalar_shift':str(scalar_shift),
                'two_rest_gaps':list(map(str,gaps)),'rest_gap_difference':str(gaps[1]-gaps[0]),
                'supplied_probe_time':'40*pi model-time units','exact_phase_signs':phases,
                'ideal_control_X_expectations':x_readings,
                'scope':'A controlled, vacuum-referenced phase protocol would distinguish the two models. Its control implementation, calibrated timing, reference energy and work account are not supplied by operator conjugation data.',
                'charge_warning':'This is not permission to coherently mix bare neutron and vacuum. Any particle-number-changing reference needs a charge-compensating reservoir; a number-preserving controlled implementation also requires an explicit physical control Hamiltonian.'},
            'conclusion':'Prior native signed-record construction is complete conditionally, but the current owning packet has no physical normalization evidence. A reference-sensitive phase probe identifies a concrete missing discriminator; it does not supply its observation.'}
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in list(paths.values())+[Path(__file__).resolve()]}
    out=ROOT/'research/strominger/results/prior-signed-admission-and-phase-probe.json'
    # Fractions in ideal X outputs are integers by the exact check above.
    result['phase_probe']['ideal_control_X_expectations']=list(map(str,x_readings))
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'hash_bindings_checked':count,'supporting_evidence_drift':mismatches,
        'conditional_signed_record_outcome':'recorded ++; no theorem replay','physical_evidence_packages':0,
        'ideal_reference_probe_readouts':['+1','-1'],'physical_calibration_delivered':False},indent=2))

if __name__=='__main__':main()
