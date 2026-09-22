"""Exact replay of the primitive-evidence DAG and both arrival orders."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util,copy,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2];G=ROOT/'grothendieck/results';N=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def bounds(x):return Q(x['lower']),Q(x['upper'])
def decode(x):return {k:tuple(map(Q,v)) for k,v in x.items()}
def main():
    c=load(N/'incomparable-proof-branch-contract.json');r=load(N/'incomparable-proof-branch-merge.json')
    assert r['contract_sha256']==sha(N/'incomparable-proof-branch-contract.json')
    for name,h in c['inputs_sha256'].items():assert sha(G/name)==h
    assert digest(c['task'])==c['task_sha256']
    boxes={k:decode(v) for k,v in r['primitive_boxes'].items()}
    old=load(G/'projection-resolution-conjecture-attack.json');theta=load(G/'theta-mass-refinement.json');pairing=load(G/'signed-fixed-hat-pairing.json')
    expected={'C':bounds(old['C_after']),'H':bounds(old['h']),'L':bounds(old['L'])}
    for label,window in (('A','A1'),('B','B1')):
        for key in ('X','mu'):expected[key+label]=bounds(old['windows'][window][key])
    assert boxes['P']==expected
    for name in ('A','B'):
        child=dict(expected)
        if name=='A':
            for label,window in (('A','A1'),('B','B1')):
                for key in ('X','mu'):child[key+label]=bounds(theta['windows'][window][key])
        else:child['C']=bounds(pairing['C'])
        assert boxes[name]==child
        assert all(expected[k][0]<=v[0]<=v[1]<=expected[k][1] for k,v in child.items())
    A,B=boxes['A'],boxes['B']
    assert A['XA'][0]>B['XA'][0] and A['XA'][1]<B['XA'][1]
    assert B['C'][0]>A['C'][0] and B['C'][1]<A['C'][1]
    joint={k:(max(A[k][0],B[k][0]),min(A[k][1],B[k][1])) for k in A}
    assert all(lo<=hi for lo,hi in joint.values()) and joint==boxes['AB']
    spec=importlib.util.spec_from_file_location('task',ROOT/'grothendieck/checkers/three_channel_source_task.py')
    t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
    engine=t.SourceTask(G/'three-channel-source-task-calibration-projection272.json')
    for name,box in boxes.items():
        def end(i):return 2*box['XA'][i]*box['XB'][i]*(box['C'][i]+box['H'][i]*(box['muA'][i]-box['L'][1-i]))*(box['C'][i]+box['H'][i]*(box['muB'][i]-box['L'][1-i]))
        parent=engine.calibrations('private')['positive'];gain=max(end(0),parent[0]),min(end(1),parent[1])
        assert list(map(str,gain))==r['gain_bounds'][name]
        local=copy.copy(engine);channels=engine.calibrations('private');channels['positive']=gain
        local.calibrations=lambda mode:dict(channels)
        assert local.certify(c['task'])==r['task_results'][name]
    assert all(r['task_results'][k]['status']=='UNRESOLVED' for k in ('P','A','B'))
    assert r['task_results']['AB']['status']=='CERTIFIED_INFEASIBLE'
    assert Q(r['task_results']['AB']['necessary_moment_cost_lower_bound'])>Q(c['task']['budget'])
    for name,frame in r['frames'].items():
        body=frame['body'];assert frame['digest']==digest(body)
        assert body['task_sha256']==digest(c['task']) and body['parent']==digest(r['primitive_boxes']['P'])
        assert body['bounds']==r['primitive_boxes'][name] and body['status']==r['task_results'][name]['status']
        assert body['necessary_cost']==r['task_results'][name]['necessary_moment_cost_lower_bound']
    for schedule in r['arrival_schedules']:
        assert schedule['events'][0]['status']=='UNRESOLVED'
        assert schedule['events'][1]['status']=='CERTIFIED_INFEASIBLE'
        assert schedule['events'][1]['time']==4<c['delivery_model']['decision_deadline']
        assert schedule['final_digest']==digest(r['primitive_boxes']['AB'])
    assert {tuple(s['order']) for s in r['arrival_schedules']}=={('A','B'),('B','A')}
    assert r['verdict']=='CORROBORATED_ON_THIS_TRIAL' and r['elapsed_seconds']<=30
    out={'passed':True,'report_sha256':sha(N/'incomparable-proof-branch-merge.json'),
         'verdict':r['verdict'],'both_branches_unresolved':True,'joint_result':'CERTIFIED_INFEASIBLE',
         'arrival_orders_agree':True,'scope':'Exact finite composition replay; analytical bounds remain owning proof obligations; host timing is reported, not independently certified.'}
    (N/'incomparable-proof-branch-verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
