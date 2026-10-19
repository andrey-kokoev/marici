"""Exact nonuniqueness of the rest gap even after occupied-frequency matching.

Use two positive-mixing completions with the same occupied-register gap and
projector, same mixing g, same kappa and unchanged source/native operators.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from check_neutron_canonical_occupied_closure import ROOT
from check_seam_occupation_energy import local_certificate
from check_pentachoron_spin_interfaces import A,I,add,scale,mm


def matched_projector(epsilon,J,g,gap,low):
    H=((A(J),A(-g)),(A(-g),A(epsilon)))
    P=scale(A(1)/gap,add(scale(low+gap,I),scale(-1,H)))
    assert mm(P,P)==P
    return P


def main():
    paths={k:ROOT/p for k,p in {
        'gap':'research/strominger/results/neutron-charge-completed-rest-gap.json',
        'source_energy':'research/strominger/results/canonical-source-energy.json',
        'clock':'research/nima/recovered-source-to-qp-clock-chain.md',
        'local_checker':'research/voevodsky/checkers/check_seam_occupation_energy.py'}.items()}
    packet=json.loads(paths['gap'].read_text());assert packet['status']=='passed';checks={}
    for p,h in packet['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    energy=json.loads(paths['source_energy'].read_text());assert energy['status']=='passed'
    for p,h in energy['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    checks['current_gap_and_source_pulse_receipts_valid']=True
    # Each source phase generator is a projector, hence has nonzero relative
    # angular frequency one. Match the occupied neutral-register gap to one.
    g=F(2,5);kappa=F(2);occupied_gap=A(1);d=F(3,5)
    assert d*d+4*g*g==1
    trials=[(F(9,20),A(F(17,10))),(F(51,40),A(F(13,4)))]
    reports=[];projectors=[]
    for epsilon,vacuum_gap in trials:
        J=epsilon+d
        assert J>epsilon>0 and kappa>epsilon and g>0
        assert occupied_gap*occupied_gap==A((J-epsilon)**2+4*g*g)
        assert vacuum_gap*vacuum_gap==A((J+epsilon)**2+4*g*g)
        cert=local_certificate(epsilon,J,g,vacuum_gap,occupied_gap)
        P=matched_projector(epsilon,J,g,occupied_gap,cert['matched_ground']);projectors.append(P)
        reports.append({'epsilon':str(epsilon),'J':str(J),'g':str(g),'kappa':str(kappa),
                        'occupied_register_gap':occupied_gap.record(),'vacuum_register_gap':vacuum_gap.record(),
                        'occupied_register_ground':cert['matched_ground'].record(),
                        'vacuum_register_ground':cert['inactive_ground'].record(),
                        'matched_occupation':cert['matched_occupation'].record(),
                        'inactive_occupation':cert['inactive_occupation'].record(),
                        'rest_gap':(21*cert['relative_seam_energy']).record()})
    assert projectors[0]==projectors[1]
    assert reports[0]['matched_occupation']==reports[1]['matched_occupation']=={'0':'4/5'}
    assert reports[0]['rest_gap']=={'0':'147/20'} and reports[1]['rest_gap']=={'0':'189/8'}
    checks['occupied_transition_frequency_and_full_ground_projector_identical']=True
    checks['same_positive_mixing_and_same_seam_penalty']=True
    checks['different_exact_vacuum_subtracted_rest_gaps']=True
    # Spectral separation identity: r_v^2-r_b^2=4 epsilon J. Thus identifying
    # BOTH local gaps with the same unit source pulse frequency is impossible
    # for the positive-gap parameter domain. This only excludes that literal
    # calibration, not every possible source-derived register construction.
    for row in reports:
        e=F(row['epsilon']);J=F(row['J']);rv=F(row['vacuum_register_gap']['0'])
        assert rv*rv-1==4*e*J>0
    checks['both_conditioned_gaps_cannot_equal_unit_pulse_frequency']=True
    # Stronger family than an overall energy-unit rescaling: only epsilon and
    # J shift together, while J-epsilon, g, kappa, all source matrices and the
    # occupied dynamics modulo scalar phase remain fixed.
    assert F(reports[0]['J'])-F(reports[0]['epsilon'])==F(reports[1]['J'])-F(reports[1]['epsilon'])==d
    checks['nonuniqueness_is_not_merely_a_common_change_of_energy_units']=True
    result={'status':'passed','checks':checks,'same_occupied_ground_projector':[[v.record() for v in r] for r in projectors[0]],
            'parameter_completions':reports,
            'general_family':{'parameters':'J=epsilon+3/5, g=2/5, kappa=2, 0<epsilon<2',
                              'occupied_gap':'1',
                              'vacuum_gap':'sqrt((2 epsilon+3/5)^2+16/25)',
                              'rest_gap':'(21/2)*(sqrt((2 epsilon+3/5)^2+16/25)-1)',
                              'monotonicity':'Strictly increases with epsilon on the admissible interval.'},
            'source_data_unchanged':'Actual neutron modes, source pulse matrices and metric, retained bank, conserved particle label, native seam controls, occupied register relative frequency and matched-register ground projector.',
            'not_claimed_unchanged':'The supplied rest Hamiltonian, its scalar occupied phase and inactive-register/vacuum response change. Those are precisely inputs not fixed by the source pulse binding.',
            'calibration_obstruction':'r_vacuum^2-r_occupied^2=4 epsilon J>0; both cannot be identified with the same unit source pulse frequency.',
            'conclusion':'The current source packet does not determine a unique neutron rest energy, even after one natural relative-frequency calibration. A supplied-law conditional gap is calculable; a source-selected physical mass is not.',
            'required_new_input':['Source operation identifying the inactive versus matched neutral-register spectra, including scalar/reference terms.',
                                  'Physical energy/time normalization and occupied-sector bare baseline.']}
    bound=list(paths.values())+[Path(__file__).resolve(),ROOT/'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}
    out=ROOT/'research/strominger/results/neutron-rest-gap-calibration.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'same_occupied_gap':'1','same_matched_occupation':'4/5',
                      'same_g':'2/5','same_kappa':'2','distinct_rest_gaps':['147/20','189/8'],
                      'unique_source_selected_rest_energy':False},indent=2))

if __name__=='__main__':main()
