"""Exact falsification of the stated E_actual > tau conjecture.
Analytical enclosure ownership stays with the signed-pairing calculation.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util
ROOT=Path(__file__).resolve().parents[2];G=ROOT/'grothendieck/results';N=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    report=load(G/'signed-pairing-task-refinement.json')
    for name,digest in report['protected_file_hashes'].items():assert sha(G/name)==digest
    path=G/report['calibration_file'];assert sha(path)==report['calibration_sha256']
    initial=load(N/'retained-middle-decision-attack-contract.json')
    for name in ('calibration-refinement-frozen-inputs.json','time-bin-cubic-observer.json','three-channel-cubic-protocol.json',
                 'three-channel-source-task-calibration-theta-taylor.json'):
        assert sha(G/name)==initial['input_sha256']['grothendieck/results/'+name]
    spec=importlib.util.spec_from_file_location('task',ROOT/'grothendieck/checkers/three_channel_source_task.py')
    t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
    engine=t.SourceTask(path);frozen=load(G/'calibration-refinement-frozen-inputs.json')
    theta=load(G/'theta-mass-refinement.json');tau=Q(theta['threshold'])
    gain=tuple(Q(report['gain_after'][k]) for k in ('lower','upper'))
    assert 0<gain[0]<=gain[1]<tau
    cases={}
    for mode in ('private','reuse'):
        case=frozen['cases'][mode]['middle_threshold'];raw={n:t.interval(case['raw'][n]) for n in t.NAMES}
        budget=Q(case['budget']);assert raw['vacuum']==(Q(1,100),Q(1,100)) and raw['crossed']==(0,0)
        cap=(budget/2**16-8*Q(1,100))/32
        assert cap==Q(499,400) and raw['positive'][0]/cap==tau
        assert engine.calibrations(mode)['positive']==gain
        result=engine.certify(case);assert result['status']=='CERTIFIED_INFEASIBLE'
        necessary=2**16*(32*raw['positive'][0]/gain[1]+8*Q(1,100))
        assert necessary==Q(result['necessary_moment_cost_lower_bound'])>budget
        assert result==report['cases'][mode]['middle_threshold']['after']
        cases[mode]={'status':result['status'],'normalized_necessary_cost_lower':str(necessary/2**16),
                     'normalized_budget':str(budget/2**16)}
    result={'verdict':'FALSIFIED','conjecture':'For the frozen middle-threshold task, E_actual > y_lower/(499/400).',
      'exact_gain_upper':str(gain[1]),'exact_threshold':str(tau),'strict_refutation_margin':str(tau-gain[1]),
      'cases':cases,'calibration_sha256':sha(path),'owning_report_sha256':sha(G/'signed-pairing-task-refinement.json'),
      'unchanged_inputs_verified':True,
      'meaning':'The fixed observations and declared source prior have an empty compatible fiber; this is not a pair of opposing admitted histories.',
      'analytical_scope':'Relies on the owning signed fixed-hat pairing, whole-cell quadrature and complete prime-tail bounds, freshly replayed separately.',
      'cut_reversal_scope':'A bijective transport or reversal of a correctly bound joint relation preserves emptiness. The finite language construction is not yet a reversal map for this assembled observer.',
      'not_claimed':['physical acquisition','incompatibility outside the declared source/prior model','distributed deadline performance']}
    (N/'positive-middle-gain-conjecture-falsification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verdict':'FALSIFIED','gain_upper_approx':float(gain[1]),'threshold_approx':float(tau),
        'positive_refutation_margin_approx':float(tau-gain[1]),
        'normalized_necessary_cost_approx':float(Q(cases['private']['normalized_necessary_cost_lower'])),
        'both_modes':'CERTIFIED_INFEASIBLE'},indent=2))
if __name__=='__main__':main()
