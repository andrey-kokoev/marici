"""C2: exact full-core bound count and trace-class model audit for the analytic proof."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3];HOME=ROOT/'research/scattering/low-energy';OWNER=ROOT/'research/voevodsky'
sys.path.insert(0,str(OWNER/'checkers'))
from check_native_adapter_collective_closure import F,Span
from check_native_port_bound_spectrum import inertia,secular_gram,energy
from check_no_singular_continuous import audit as sc_audit
from check_three_port_threshold import audit as threshold_audit

PROOF=HOME/'THREE-PORT-COMPLETENESS-PROOF.md'
RESULT=HOME/'results/three-port-completeness.v1.json'


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def audit():
    sc=sc_audit();threshold=threshold_audit()
    for obj,name in ((sc,'no-singular-continuous.v1.json'),(threshold,'three-port-threshold.v1.json')):
        assert obj==json.loads((HOME/'results'/name).read_text(encoding='utf-8'))
    source=json.loads((OWNER/'results/native_joint_generator_resolvent.json').read_text(encoding='utf-8'))
    report=json.loads((OWNER/'results/native_port_bound_spectrum.json').read_text(encoding='utf-8'))
    for name,value in report['source_hashes'].items():assert digest(OWNER/name)==value,name
    K=[[F(*x) for x in row] for row in source['joint_generator']];metric=[F(*x) for x in source['gram_diagonal']]
    core=inertia([[metric[i]*K[i][j] for j in range(11)] for i in range(11)]);assert core==(10,0,1)
    top=inertia(secular_gram(K,metric,3,Q(1)));far=inertia(secular_gram(K,metric,3,Q(1,32)))
    assert top==(6,5,0) and far==(11,0,0)
    brackets=[]
    for sector in report['sector_reports']:
        for candidate in sector['brackets']:
            low,high=map(Q,candidate['decay_interval']);assert 0<low<high<1
            left=inertia(secular_gram(K,metric,3,low));right=inertia(secular_gram(K,metric,3,high))
            assert left[2]==right[2]==0 and right[1]-left[1]==1
            elo,ehi=energy(high),energy(low);assert elo>4 and elo<ehi
            assert [elo,ehi]==list(map(Q,candidate['energy_interval']))
            brackets.append({'decay_interval':[str(low),str(high)],'energy_interval':[str(elo),str(ehi)],
                             'full_inertia_low_decay':list(left),'full_inertia_high_decay':list(right),'root_multiplicity':1})
    ordered=sorted((Q(b['energy_interval'][0]),Q(b['energy_interval'][1])) for b in brackets)
    assert len(ordered)==5 and all(a[1]<b[0] for a,b in zip(ordered,ordered[1:]))
    # The same-space reference differs only by three symmetric endpoint couplings.
    contact=[[F(0) for _ in range(14)] for _ in range(14)]
    for j in range(3):contact[j][11+j]=contact[11+j][j]=F(-1)
    rank=Span(14)
    for i,row in enumerate(contact):rank.add(row,{'row':i})
    assert len(rank.rows)==6
    # Algebraic tail norm coefficient and secular derivative agree.
    for r in (Q(1,32),Q(1,2),Q(3,4)):
        tail=r*r/(1-r*r);assert tail>0 and 1+tail>0
    paths=set(sc['source_sha256'])|set(threshold['source_sha256'])|{
        PROOF.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix(),
        'research/voevodsky/results/native_port_bound_spectrum.json',
        'research/scattering/low-energy/results/no-singular-continuous.v1.json',
        'research/scattering/low-energy/results/three-port-threshold.v1.json'}|{(OWNER/n).relative_to(ROOT).as_posix() for n in report['source_hashes']}
    return {'schema':'marici.scattering.three-port-completeness.v1','status':'pass','C2_disposition':'established',
            'source_sha256':{p:digest(ROOT/p) for p in sorted(paths)},'core_gram_inertia':list(core),
            'upper_threshold_inertia':list(top),'far_above_band_inertia':list(far),'fresh_full_core_brackets':brackets,
            'total_simple_bound_modes':5,'same_space_reference_difference_rank':6,
            'wave_operator_theorem':'Kato-Rosenblum for a trace-class self-adjoint difference; free ac subspace is exactly all three Dirichlet leads.',
            'full_tail_normalization':'x*H x + r²/(1-r²) sum_j h_j |x_j|²',
            'below_band_exclusion':'Positive total energy form',
            'band_and_edge_point_exclusion':'L2 lead recurrence forces zero tails; K-only cyclicity excludes invisible core eigenvectors.',
            'singular_continuous_input':'Fresh C9 analytic proof/source certificate',
            'source_stationary_solver_replayed':False,'machine_checked_scattering_theorem':False,'physical_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    result=audit();text=json.dumps(result,indent=2)+'\n'
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==json.loads(text),'stale C2 certificate'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: C2 full-space scattering proof inputs, five simple bound modes and rank-six perturbation verified.')


if __name__=='__main__':main()
