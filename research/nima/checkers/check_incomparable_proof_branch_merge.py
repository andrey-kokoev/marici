"""Two genuinely incomparable primitive-evidence branches, one frozen task.
Existing owned analytic certificates are inputs; this checks their finite
composition and task-specific local admission, not independent authentication.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util,time,copy,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2];G=ROOT/'grothendieck/results';N=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(x):return tuple(Q(x[k]) for k in ('lower','upper'))
def enc(box):return {k:list(map(str,v)) for k,v in box.items()}
def decode(box):return {k:tuple(map(Q,v)) for k,v in box.items()}
def subset(a,b):return all(b[k][0]<=v[0]<=v[1]<=b[k][1] for k,v in a.items())
def meet(a,b):
    out={k:(max(a[k][0],b[k][0]),min(a[k][1],b[k][1])) for k in a}
    if any(lo>hi for lo,hi in out.values()):raise ValueError('EVIDENCE_CONSISTENCY_FAILURE')
    return out

def main():
    names=['projection-resolution-conjecture-attack.json','theta-mass-refinement.json',
           'signed-pairing-task-refinement.json','signed-fixed-hat-pairing.json',
           'calibration-refinement-frozen-inputs.json','time-bin-cubic-observer.json',
           'three-channel-cubic-protocol.json','three-channel-source-task-calibration-projection272.json']
    task=load(G/'calibration-refinement-frozen-inputs.json')['cases']['private']['middle_threshold']
    contract={'prediction':'A and B individually unresolved; verified joint primitive merge resolves by deadline in either arrival order',
      'task':task,'task_sha256':digest(task),'common_ancestor':'projection272 primitive evidence',
      'A':'replace X_A,X_B,mu_A,mu_B by theta-Taylor intervals; retain ancestor C,H,L',
      'B':'replace C by signed fixed-hat interval; retain ancestor theta,H,L',
      'merge':'coordinatewise intersection of SAME anchored primitive bounds, then recompute gain and source-task proof',
      'scope':'Retrospective composition of existing analytical certificates, not a blinded benchmark or independent error model',
      'compute_budget_seconds':30,'budget_scope':'local exact branch construction, verification and replay; analytical certificate generation is initially available evidence',
      'delivery_model':{'reliable':True,'arrival_times':[2,4],'decision_deadline':5,'orders':[['A','B'],['B','A']],
                        'timing':'stipulated logical times with atomic validation, not physical latency or benchmark-derived execution times'},
      'inputs_sha256':{name:sha(G/name) for name in names}}
    cp=N/'incomparable-proof-branch-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
    started=time.monotonic()
    old=load(G/names[0]);theta=load(G/names[1]);signed=load(G/names[2]);pairing=load(G/names[3])
    # Check the declared evidence bindings, not merely their displayed values.
    for report in (theta,signed):
        for name,h in report['protected_file_hashes'].items():assert sha(G/name)==h
    assert pairing['filter_sha256']==sha(G/'time-bin-cubic-observer.json')
    assert signed['pairing']['C']==pairing['C']
    base={'C':bounds(old['C_after']),'H':bounds(old['h']),'L':bounds(old['L'])}
    for label,window in (('A','A1'),('B','B1')):
        for key in ('X','mu'):base[key+label]=bounds(old['windows'][window][key])
    A=dict(base);B=dict(base)
    for label,window in (('A','A1'),('B','B1')):
        for key in ('X','mu'):A[key+label]=bounds(theta['windows'][window][key])
    B['C']=bounds(pairing['C'])
    assert subset(A,base) and subset(B,base)
    assert not subset(A,B) and not subset(B,A)
    joint=meet(A,B);assert joint==meet(B,A) and meet(joint,A)==joint
    spec=importlib.util.spec_from_file_location('task',ROOT/'grothendieck/checkers/three_channel_source_task.py')
    t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
    engine=t.SourceTask(G/'three-channel-source-task-calibration-projection272.json')
    def gain(box):
        assert min(box['C']+box['H']+box['XA']+box['XB'])>0
        assert box['muA'][0]>box['L'][1] and box['muB'][0]>box['L'][1]
        def end(i):return 2*box['XA'][i]*box['XB'][i]*(box['C'][i]+box['H'][i]*(box['muA'][i]-box['L'][1-i]))*(box['C'][i]+box['H'][i]*(box['muB'][i]-box['L'][1-i]))
        x=end(0),end(1);p=engine.calibrations('private')['positive']
        return max(x[0],p[0]),min(x[1],p[1])
    def replay(box):
        # The task engine's certification algorithm uses these same unchanged
        # source/prior fields; only the proved positive gain interval is replaced.
        local=copy.copy(engine);channels=engine.calibrations('private');channels['positive']=gain(box)
        local.calibrations=lambda mode:dict(channels)
        result=local.certify(task)
        if result['status']=='CERTIFIED_INFEASIBLE':
            assert Q(result['necessary_moment_cost_lower_bound'])>Q(task['budget'])
        return result
    boxes={'P':base,'A':A,'B':B,'AB':joint};results={k:replay(b) for k,b in boxes.items()}
    frames={}
    parent=digest(enc(base))
    for name,box in (('A',A),('B',B)):
        body={'branch':name,'task_sha256':digest(task),'parent':parent,'bounds':enc(box),
              'evidence_sha256':contract['inputs_sha256'][names[1] if name=='A' else names[3]],
              'status':results[name]['status'],'necessary_cost':results[name]['necessary_moment_cost_lower_bound']}
        frames[name]={'body':body,'digest':digest(body)}
    def validate(frame):
        b=frame['body']
        if digest(b)!=frame['digest'] or b['task_sha256']!=digest(task) or b['parent']!=parent:raise ValueError('ABSTAIN')
        name=b['branch']
        if name not in frames or b!=frames[name]['body']:raise ValueError('ABSTAIN')
        box=decode(b['bounds']);r=replay(box)
        if b['status']!=r['status'] or b['necessary_cost']!=r['necessary_moment_cost_lower_bound']:raise ValueError('ABSTAIN')
        return box
    schedules=[]
    for order in contract['delivery_model']['orders']:
        state=base;events=[]
        for time_,name in zip((2,4),order):
            state=meet(state,validate(frames[name]));r=replay(state)
            events.append({'time':time_,'branch':name,'status':r['status'],'state_sha256':digest(enc(state))})
        assert state==joint
        # A duplicate or late ancestor cannot discard an already retained constraint.
        assert meet(state,validate(frames[order[0]]))==state and meet(state,base)==state
        schedules.append({'order':order,'events':events,'final_digest':digest(enc(state)),'final_status':r['status']})
    assert schedules[0]['final_digest']==schedules[1]['final_digest']
    # Lossy merge control: intersecting only projected gain boxes can miss
    # the conclusion recovered by retaining the underlying primitive evidence.
    ga,gb=gain(A),gain(B);gain_only=max(ga[0],gb[0]),min(ga[1],gb[1])
    local=copy.copy(engine);channels=engine.calibrations('private');channels['positive']=gain_only
    local.calibrations=lambda mode:dict(channels);lossy=local.certify(task)
    rejected=[]
    for field,value in [('task_sha256','wrong'),('parent','wrong'),('status','CERTIFIED_FEASIBLE'),('necessary_cost','0')]:
        bad=copy.deepcopy(frames['A']);bad['body'][field]=value;bad['digest']=digest(bad['body'])
        try:validate(bad)
        except ValueError:rejected.append(field)
        else:raise AssertionError('forged frame admitted')
    left=dict(base);right=dict(base);lo,hi=base['C'];third=(hi-lo)/3
    left['C']=(lo,lo+third);right['C']=(hi-third,hi)
    try:meet(left,right)
    except ValueError as e:assert str(e)=='EVIDENCE_CONSISTENCY_FAILURE';rejected.append('empty primitive intersection')
    else:raise AssertionError('empty calibration intersection promoted to task result')
    for name,h in contract['inputs_sha256'].items():assert sha(G/name)==h
    elapsed=time.monotonic()-started
    success=(all(results[k]['status']=='UNRESOLVED' for k in ('A','B')) and
             results['AB']['status'] in ('CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE') and elapsed<=30)
    report={'contract_sha256':sha(cp),'verdict':'CORROBORATED_ON_THIS_TRIAL' if success else 'REFUTED_ON_THIS_TRIAL',
      'primitive_boxes':{k:enc(v) for k,v in boxes.items()},'gain_bounds':{k:list(map(str,gain(v))) for k,v in boxes.items()},
      'task_results':results,'frames':frames,'arrival_schedules':schedules,'elapsed_seconds':elapsed,
      'gain_only_intersection_status':lossy['status'],'negative_controls_rejected':rejected,
      'compatibility_basis':'Both owning analytical certificates bound the SAME fixed quantities for the SAME detector; coordinate intersection needs no statistical independence assumption. Hashes alone do not prove analytical validity.',
      'empty_intersection_control':'Synthetic incompatible boxes test rejection only; not a claim of two sound contradictory analytical certificates.',
      'scope':'Finite task-specific evidence DAG, closed admission and stipulated reliable-message schedule. No signatures, physical latency or universal confluence theorem.'}
    out=N/'incomparable-proof-branch-merge.json';out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'verdict':report['verdict'],'statuses':{k:v['status'] for k,v in results.items()},
      'gain_only_intersection':lossy['status'],'arrival_orders_agree':True,'elapsed_seconds':elapsed,
      'negative_controls':rejected},indent=2))
if __name__=='__main__':main()
