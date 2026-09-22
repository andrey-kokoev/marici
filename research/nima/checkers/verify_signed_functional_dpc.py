"""Exact independent replay of the frozen DPC task and its recorded verdict.
Clock measurements are observations, not portable mathematical certificates.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib
ROOT=Path(__file__).resolve().parents[2];N=ROOT/'nima/results';G=ROOT/'grothendieck/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    cp=N/'signed-functional-dpc-contract.json';c=load(cp);r=load(N/'signed-functional-dpc-result.json')
    assert r['contract_sha256']==sha(cp)
    for group in ('inputs_sha256','code_sha256'):
        for name,digest in c[group].items():assert sha(ROOT/name)==digest
    spec=importlib.util.spec_from_file_location('task',ROOT/'grothendieck/checkers/three_channel_source_task.py')
    t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
    parent=t.SourceTask(G/'three-channel-source-task-calibration-theta-taylor.json')
    lo,hi=parent.calibrations('private')['positive'];threshold=(lo+hi)/2
    assert threshold==Q(c['threshold']) and list(map(str,(lo,hi)))==c['initial_positive_gain']
    task=c['task'];cap=(Q(task['budget'])/2**16-8*Q(1,125))/32
    assert cap==Q(156,125)==Q(c['positive_capacity']) and Q(task['budget'])==40*2**16
    assert t.interval(task['raw']['positive'])==(cap*threshold,2*cap*threshold)
    assert t.interval(task['raw']['vacuum'])==(Q(1,125),Q(1,125))
    assert t.interval(task['raw']['crossed'])==(0,0)
    assert parent.certify(task)['status']=='UNRESOLVED'
    frozen=load(G/'calibration-refinement-frozen-inputs.json')
    assert all(task!=old for cases in frozen['cases'].values() for old in cases.values())
    assert c['worker_wall_budget_seconds']==180 and c['arithmetic_threads']==1
    for method,trial in r['trials'].items():
        if trial['outcome']=='completed':
            p=N/f'signed-functional-dpc-{method}-result.json';result=load(p)
            assert sha(p)==trial['result_sha256'] and result['contract_sha256']==sha(cp)
            calpath=ROOT/result['calibration_file'];assert sha(calpath)==result['calibration_sha256']
            ep=N/f'signed-functional-dpc-{method}-pairing.json';assert sha(ep)==result['pairing_sha256']
            evidence=load(ep);assert evidence['contract_sha256']==sha(cp) and evidence['method']==method
            engine=t.SourceTask(calpath);assert engine.certify(task)==result['task_result']
            assert trial['task_status']==result['task_result']['status']
            assert tuple(map(Q,result['gain_bounds']))==engine.calibrations('private')['positive']
        expected=(trial['outcome']=='completed' and trial.get('task_status') in ('CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE') and trial['elapsed_seconds']<=180)
        assert trial['success']==expected
    expected='CORROBORATED_ON_THIS_TRIAL' if r['trials']['signed']['success'] and not r['trials']['projection']['success'] else 'REFUTED_ON_THIS_TRIAL'
    assert r['verdict']==expected
    # This observed outcome fails the positive prediction independently of the
    # projection worker's timing: even its returned signed enclosure straddles.
    signed=load(N/'signed-functional-dpc-signed-result.json');gain=tuple(map(Q,signed['gain_bounds']))
    assert gain[0]<threshold<gain[1]
    sr=signed['task_result'];budget=Q(task['budget'])
    necessary=Q(sr['necessary_moment_cost_lower_bound']);robust=Q(sr['automatic_witness_search']['moment_cost'])
    assert necessary<budget<robust and sr['status']=='UNRESOLVED'
    result={'passed':True,'verdict':expected,'contract_sha256':sha(cp),
      'result_sha256':sha(N/'signed-functional-dpc-result.json'),'selection_rule_verified':True,
      'new_task_distinct_from_all_previous_frozen_cases':True,'initial_evidence_unresolved':True,
      'signed_gain_strictly_straddles_threshold':True,
      'normalized_necessary_cost':str(necessary/2**16),'normalized_robust_cost':str(robust/2**16),
      'normalized_budget':'40',
      'scope':'Exact evidence/task replay. The bounded prediction fails; no claim of physical ambiguity, universal algorithmic inferiority or causal delivery impossibility.',
      'timing_scope':'Reported host timings are not independently certified by this replay.'}
    (N/'signed-functional-dpc-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'verdict':expected,'signed_status':sr['status'],
        'normalized_cost_bracket':[float(necessary/2**16),float(robust/2**16)],'budget':40},indent=2))
if __name__=='__main__':main()
