"""Frozen single-trial DPC comparison: direct signed vs projection pairing.

New synthetic task is generated ONLY from the initial calibration midpoint.
No tuned thresholds, retries, reused pairing outputs, or success-by-abstention.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,sys,subprocess,time,platform,copy,os
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2];G=ROOT/'grothendieck/results';N=ROOT/'nima/results'
MANIFEST=N/'signed-functional-dpc-contract.json'

def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def bounds(d):return Q(d['lower']),Q(d['upper'])
def output(method,suffix):return N/f'signed-functional-dpc-{method}-{suffix}.json'

def worker(method):
    started=time.monotonic()
    from flint import arb,ctx
    ctx.threads=1
    contract=load(MANIFEST)
    for name,digest in contract['inputs_sha256'].items():assert sha(ROOT/name)==digest
    for name,digest in contract['code_sha256'].items():assert sha(ROOT/name)==digest
    t=module('task',ROOT/'grothendieck/checkers/three_channel_source_task.py')
    parent=t.SourceTask(G/'three-channel-source-task-calibration-theta-taylor.json')
    initial=parent.certify(contract['task']);assert initial['status']=='UNRESOLVED'
    def ball(q):return arb(q.numerator)/q.denominator
    def enc(x):return {'lower':str(x.lower().fmpq()),'upper':str(x.upper().fmpq()),'display':x.str(24)}
    params=contract['methods'][method]
    if method=='signed':
        impl=module('signed',ROOT/'grothendieck/checkers/certify_signed_fixed_hat_pairing.py')
        C,evidence=impl.compute(N=params['prime_cutoff'],bits=params['bits'],mesh_divisions=params['mesh_divisions'])
    else:
        impl=module('projection',ROOT/'grothendieck/checkers/refine_fixed_bin_response.py')
        ctx.prec=params['bits'];norm=load(G/'bulk-response-norm-refinement.json')
        C,h,diagnostics=impl.refine([ball(Q(side['new_squared_norm']['upper'])) for side in norm['sides']],
                                   subdivisions=params['subdivisions'],bits=params['bits'])
        evidence={'C':enc(C),'h':enc(h),'diagnostics':diagnostics}
    evidence['contract_sha256']=sha(MANIFEST);evidence['method']=method
    ep=output(method,'pairing');save(ep,evidence)
    # Both methods use exactly the SAME initial theta, H and L boxes.
    theta=load(G/'theta-mass-refinement.json');old=load(G/'projection-resolution-conjecture-attack.json')
    beforeC=bounds(old['C_after']);cc=bounds(evidence['C'])
    cc=max(cc[0],beforeC[0]),min(cc[1],beforeC[1]);assert cc[0]<=cc[1]
    H=bounds(old['h']);L=bounds(old['L']);xa=bounds(theta['windows']['A1']['X']);xb=bounds(theta['windows']['B1']['X'])
    ma=bounds(theta['windows']['A1']['mu']);mb=bounds(theta['windows']['B1']['mu'])
    assert min(cc+H+xa+xb)>0 and ma[0]>L[1] and mb[0]>L[1]
    def extreme(k):return 2*xa[k]*xb[k]*(cc[k]+H[k]*(ma[k]-L[1-k]))*(cc[k]+H[k]*(mb[k]-L[1-k]))
    oldgain=parent.calibrations('private')['positive']
    gain=max(oldgain[0],extreme(0)),min(oldgain[1],extreme(1));assert 0<gain[0]<=gain[1]
    # Calibration artifacts live beside their existing parents for the owning loader.
    calibration=copy.deepcopy(parent.cal)
    calibration['parent_calibration_file']='three-channel-source-task-calibration-theta-taylor.json'
    calibration['parent_calibration_sha256']=sha(G/calibration['parent_calibration_file'])
    for mode in ('private','reuse'):
        calibration['diagonal_refinements'][mode]['positive']={name:[str(q.numerator),str(q.denominator)] for name,q in zip(('lower','upper'),gain)}
    calibration['refinement_evidence']={
        'method':f'DPC-{method}-fixed-filter-pairing','contract_sha256':sha(MANIFEST),
        'parameters':params,'pairing_evidence_sha256':sha(ep),
        'unchanged_theta_evidence_sha256':sha(G/'theta-mass-refinement.json'),
        'C_bin_lower':[str(cc[0].numerator),str(cc[0].denominator)],
        'C_bin_upper':[str(cc[1].numerator),str(cc[1].denominator)]}
    calpath=G/f'three-channel-source-task-calibration-dpc-{method}.json';save(calpath,calibration)
    engine=t.SourceTask(calpath);result=engine.certify(contract['task'])
    # Exact verification of any positive/negative task certificate is inside the timed worker.
    threshold=Q(contract['threshold']);budget=Q(contract['task']['budget'])
    if result['status']=='CERTIFIED_INFEASIBLE':
        assert gain[1]<threshold and Q(result['necessary_moment_cost_lower_bound'])>budget
    elif result['status']=='CERTIFIED_FEASIBLE':
        assert gain[0]>=threshold and result['automatic_witness_search']['accepted']
        witness={k:Q(v) for k,v in result['automatic_witness_search']['coefficients_at_A2'].items()}
        assert sum(t.WEIGHTS[k]*abs(v) for k,v in witness.items())*2**16<=budget
        for k,v in witness.items():assert t.contains(t.interval(contract['task']['raw'][k]),t.scale(engine.calibrations('private')[k],v))
    else:assert gain[0]<threshold<gain[1]
    save(output(method,'result'),{'contract_sha256':sha(MANIFEST),'method':method,
        'gain_bounds':list(map(str,gain)),'threshold':str(threshold),'task_result':result,
        'calibration_file':str(calpath.relative_to(ROOT)).replace('\\','/'),'calibration_sha256':sha(calpath),
        'pairing_sha256':sha(ep),'worker_elapsed_seconds':time.monotonic()-started,
        'analytical_scope':'The owning pairing proof supplies analytic enclosure validity; task inequalities are rechecked exactly here.'})

def main():
    t=module('task',ROOT/'grothendieck/checkers/three_channel_source_task.py')
    parent=t.SourceTask(G/'three-channel-source-task-calibration-theta-taylor.json')
    lower,upper=parent.calibrations('private')['positive'];threshold=(lower+upper)/2
    vacuum=Q(1,125);budget=40*2**16;cap=(Q(budget,2**16)-8*vacuum)/32;assert cap==Q(156,125)
    y=cap*threshold
    task={'mode':'private','budget':str(budget),'auto_witness':True,
          'raw':{'positive':{'center':str(3*y/2),'radius':str(y/2)},
                 'crossed':{'center':'0','radius':'0'},'vacuum':{'center':str(vacuum),'radius':'0'}}}
    initial=parent.certify(task);assert initial['status']=='UNRESOLVED'
    inputs=['three-channel-source-task-calibration-theta-taylor.json','theta-mass-refinement.json',
            'projection-resolution-conjecture-attack.json','bulk-response-norm-refinement.json',
            'time-bin-cubic-observer.json','three-channel-cubic-protocol.json']
    code=['grothendieck/checkers/certify_signed_fixed_hat_pairing.py','grothendieck/checkers/refine_fixed_bin_response.py',
          'grothendieck/checkers/refine_theta_mass_quadrature.py','grothendieck/checkers/three_channel_source_task.py',
          'nima/checkers/test_signed_functional_dpc.py']
    contract={'schema':'signed-functional-vs-projection-DPC-v1',
      'prediction':'signed returns a verified definite answer within budget; projection does not',
      'selection_rule':'initial positive gain midpoint; vacuum=1/125; budget=40*2^16; positive interval=[cap*midpoint,2*cap*midpoint]',
      'selection_scope':'New related synthetic task, not blinded or statistically independent of previous work. No new pairing output enters task construction.',
      'task':task,'threshold':str(threshold),'positive_capacity':str(cap),
      'initial_status':initial['status'],'initial_positive_gain':list(map(str,(lower,upper))),
      'methods':{'signed':{'prime_cutoff':1000000,'bits':192,'mesh_divisions':32},
                 'projection':{'subdivisions':24,'dimension':408,'bits':9216}},
      'worker_wall_budget_seconds':180,'arithmetic_threads':1,'worker_order':['signed','projection'],
      'runtime':{'python':sys.version,'platform':platform.platform(),'processor':platform.processor(),'cpu_count':os.cpu_count()},
      'execution':'Sequential fresh subprocesses, one attempt each, no cached pairings or retries. Timeout includes imports, input checks, numerical calculation and exact task replay.',
      'shared_parameters':'Identical frozen detector, source prior, raw data, theta mass/moment boxes, H and L; only the proof of C differs.',
      'success':'CERTIFIED_FEASIBLE or CERTIFIED_INFEASIBLE with verified exact task obligations; UNRESOLVED is failure',
      'failure_interpretation':'Reject this bounded prediction, not mathematical decidability or all possible implementations.',
      'inputs_sha256':{'grothendieck/results/'+name:sha(G/name) for name in inputs},
      'code_sha256':{name:sha(ROOT/name) for name in code}}
    save(MANIFEST,contract)
    print('Contract frozen:',sha(MANIFEST),flush=True)
    trials={}
    for method in contract['worker_order']:
        for suffix in ('pairing','result'):
            path=output(method,suffix)
            if path.exists():path.unlink()
        started=time.monotonic()
        try:
            run=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--worker',method],
                               capture_output=True,text=True,timeout=contract['worker_wall_budget_seconds'])
            trial={'outcome':'completed' if run.returncode==0 else 'worker_failed','returncode':run.returncode,
                   'elapsed_seconds':time.monotonic()-started,'stdout':run.stdout[-2000:],'stderr':run.stderr[-2000:]}
            if run.returncode==0:
                result=load(output(method,'result'));assert result['contract_sha256']==sha(MANIFEST)
                trial['task_status']=result['task_result']['status'];trial['result_sha256']=sha(output(method,'result'))
        except subprocess.TimeoutExpired:
            trial={'outcome':'timeout','elapsed_seconds':time.monotonic()-started,'task_status':'NO_CERTIFICATE'}
        trial['success']=trial['outcome']=='completed' and trial.get('task_status') in ('CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE') and trial['elapsed_seconds']<=180
        trials[method]=trial;print(json.dumps({method:trial}),flush=True)
    for name,digest in contract['inputs_sha256'].items():assert sha(ROOT/name)==digest
    for name,digest in contract['code_sha256'].items():assert sha(ROOT/name)==digest
    verdict='CORROBORATED_ON_THIS_TRIAL' if trials['signed']['success'] and not trials['projection']['success'] else 'REFUTED_ON_THIS_TRIAL'
    report={'contract_sha256':sha(MANIFEST),'trials':trials,'verdict':verdict,
            'interpretation':'A task-specific bounded performance result, not universal superiority or an information-theoretic obstruction.'}
    save(N/'signed-functional-dpc-result.json',report)
    print(verdict)

if __name__=='__main__':
    if '--worker' in sys.argv:worker(sys.argv[-1])
    else:main()
