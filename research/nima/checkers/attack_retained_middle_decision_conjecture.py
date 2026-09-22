"""Attack the proposed retained-observer middle-task decision conjecture.

Distinguishes a proved observation-factorization obstruction, interval-model
branches, and the still-unproved realizability of calibration endpoints.
A single optional proof-only pairing refinement has a frozen 180-second budget.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import importlib.util,json,hashlib,sys,subprocess,time,copy
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2];G=ROOT/'grothendieck/results';N=ROOT/'nima/results'
CONTRACT=N/'retained-middle-decision-attack-contract.json'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def projection():
    from flint import arb,ctx
    contract=load(CONTRACT)
    for name,digest in contract['input_sha256'].items():assert sha(ROOT/name)==digest
    r=module('pairing',ROOT/'grothendieck/checkers/refine_fixed_bin_response.py')
    assert sha(ROOT/'grothendieck/checkers/refine_fixed_bin_response.py')==contract['pairing_code_sha256']
    ctx.prec=contract['projection_bits']
    def ball(q):return arb(q.numerator)/q.denominator
    norm=load(G/'bulk-response-norm-refinement.json')
    C,h,diagnostics=r.refine([ball(Q(side['new_squared_norm']['upper'])) for side in norm['sides']],
                             subdivisions=contract['projection_subdivisions'],bits=contract['projection_bits'])
    def enc(x):return {'lower':str(x.lower().fmpq()),'upper':str(x.upper().fmpq()),'display':x.str(24)}
    save(N/'retained-middle-pairing-candidate.json',{'C':enc(C),'h':enc(h),'diagnostics':diagnostics,
         'contract_sha256':sha(CONTRACT),'pairing_code_sha256':contract['pairing_code_sha256']})

def main():
    paths=[G/name for name in ('calibration-refinement-frozen-inputs.json','three-channel-source-task-calibration-theta-taylor.json',
        'theta-mass-refinement.json','projection-resolution-conjecture-attack.json','three-channel-cubic-protocol.json',
        'time-bin-cubic-observer.json','bulk-response-norm-refinement.json')]
    paths += [N/name for name in ('actual-private-core-with-original-cubic.json','actual-retained-cubic-observer-union.json')]
    contract={'schema':'retained-middle-decision-attack-v1','task':'private middle_threshold; reuse middle_threshold is a control',
      'actions':['CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE'],'unresolved_is_success':False,
      'initial_evidence':'Frozen raw intervals, order-16 source prior, deployed filter, and existing theta-Taylor calibration; no additional acquisition',
      'actor':'One local certificate worker with all listed files at start; not a distributed physical execution claim',
      'history':'No additional dynamic history supplied by the frozen middle task; no synthetic history substituted',
      'admission_bridge':'Not presumed: test whether task observations factor through the ideal assembled observer',
      'permitted_refinement':'One proof-only fixed-filter Hilbert pairing projection; theta mass/moment boxes, detector and observations unchanged',
      'projection_subdivisions':24,'projection_dimension':408,'projection_bits':9216,
      'projection_worker_deadline_seconds':180,'deadline_scope':'Measured local worker deadline, not a universal algorithmic or delivery lower bound',
      'pairing_code_sha256':sha(ROOT/'grothendieck/checkers/refine_fixed_bin_response.py'),
      'input_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in paths}}
    save(CONTRACT,contract)
    t=module('task',ROOT/'grothendieck/checkers/three_channel_source_task.py')
    engine=t.SourceTask(G/'three-channel-source-task-calibration-theta-taylor.json')
    frozen=load(G/'calibration-refinement-frozen-inputs.json');task=frozen['cases']['private']['middle_threshold']
    before=engine.certify(task);assert before['status']=='UNRESOLVED'
    raw={n:t.interval(task['raw'][n]) for n in t.NAMES};B=Q(task['budget'])
    assert raw['crossed']==(0,0) and raw['vacuum']==(Q(1,100),Q(1,100)) and raw['positive'][0]>0
    cap=(B/2**16-8*Q(1,100))/32;assert cap==Q(499,400)
    threshold=raw['positive'][0]/cap
    old=load(G/'projection-resolution-conjecture-attack.json');theta=load(G/'theta-mass-refinement.json')
    assert threshold==Q(old['threshold'])==Q(theta['threshold'])
    def bounds(x):return Q(x['lower']),Q(x['upper'])
    C=bounds(old['C_after']);H=bounds(old['h']);L=bounds(old['L'])
    xa=bounds(theta['windows']['A1']['X']);xb=bounds(theta['windows']['B1']['X'])
    ma=bounds(theta['windows']['A1']['mu']);mb=bounds(theta['windows']['B1']['mu'])
    assert min(C+H+xa+xb)>0 and ma[0]>L[1] and mb[0]>L[1]
    def extreme(c,high):
        i=int(high);return 2*xa[i]*xb[i]*(c+H[i]*(ma[i]-L[1-i]))*(c+H[i]*(mb[i]-L[1-i]))
    assert extreme(C[0],True)<threshold<extreme(C[1],False)
    assert 2**16*(32*(raw['positive'][0]/extreme(C[0],True))+8*Q(1,100))>B
    assert 2**16*(32*(raw['positive'][0]/extreme(C[1],False))+8*Q(1,100))<B
    # Actual rational source separator: three forgotten two-event commutators.
    source={}
    for flips in product((0,1),repeat=3):
        word=tuple(e for pair,flip in zip(((0,1),(2,3),(4,5)),flips) for e in (pair[::-1] if flip else pair))
        source[word,(0,)*6]=(-1)**sum(flips)
    assert len(source)==8 and sum(source.values())==0
    base=load(N/'actual-private-core-with-original-cubic.json');union=load(N/'actual-retained-cubic-observer-union.json')
    allrows=base['rows']+[row for frame in union['frames'] for row in frame['rows']]
    assert len(allrows)==3591
    for row in allrows:
        if row['corner_masks']==[0,63]:
            assert all((tuple(term['word']),tuple(term['marks'])) not in source for term in row['terms'])
    protocol=load(G/'three-channel-cubic-protocol.json');vac=protocol['channels']['vacuum']
    assert vac['source_signature']==[[[0,1],[2,3],[4,5]],[0,0,0]]
    assert vac['forward_gain_lower']==vac['forward_gain_upper']==['1','1']
    assert source[tuple(range(6)),(0,)*6]==1
    assert 8*2**16<=B
    # These sources obstruct factorization, NOT the frozen middle decision:
    # both have zero positive reading and hence fail that frozen observation.
    assert not(raw['positive'][0]<=0<=raw['positive'][1])
    candidate=N/'retained-middle-pairing-candidate.json'
    if candidate.exists():candidate.unlink() # prevents reuse of an old timed-out candidate
    started=time.monotonic()
    try:
        run=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--projection'],capture_output=True,text=True,
                           timeout=contract['projection_worker_deadline_seconds'])
        attempt={'elapsed_seconds':time.monotonic()-started,'returncode':run.returncode,
                 'status':'completed' if run.returncode==0 else 'worker_failed'}
        if run.returncode:attempt['stderr']=run.stderr[-4000:]
    except subprocess.TimeoutExpired:
        attempt={'elapsed_seconds':time.monotonic()-started,'status':'worker_timeout',
                 'interpretation':'No impossibility conclusion about another method or about information sufficiency'}
    after={'private':before,'reuse':engine.certify(frozen['cases']['reuse']['middle_threshold'])}
    if attempt['status']=='completed':
        proposal=load(candidate);assert proposal['contract_sha256']==sha(CONTRACT)
        cc=bounds(proposal['C']);hh=bounds(proposal['h'])
        assert max(H[0],hh[0])<=min(H[1],hh[1])
        refined=(max(C[0],cc[0]),min(C[1],cc[1]));assert refined[0]<=refined[1]
        newgain=(extreme(refined[0],False),extreme(refined[1],True))
        parentgain=engine.calibrations('private')['positive']
        newgain=max(newgain[0],parentgain[0]),min(newgain[1],parentgain[1]);assert 0<newgain[0]<=newgain[1]
        calibration=copy.deepcopy(engine.cal)
        calibration['parent_calibration_file']='three-channel-source-task-calibration-theta-taylor.json'
        calibration['parent_calibration_sha256']=sha(G/calibration['parent_calibration_file'])
        for mode in ('private','reuse'):
            calibration['diagonal_refinements'][mode]['positive']={name:[str(q.numerator),str(q.denominator)] for name,q in zip(('lower','upper'),newgain)}
        calibration['refinement_evidence'].update(method='408-dimensional-proof-only-fixed-filter-pairing',
            projection_dimension=408,projection_bits=9216,
            C_bin_lower=[str(refined[0].numerator),str(refined[0].denominator)],
            C_bin_upper=[str(refined[1].numerator),str(refined[1].denominator)],
            attack_contract_sha256=sha(CONTRACT),pairing_candidate_sha256=sha(candidate))
        calpath=G/'three-channel-source-task-calibration-pairing408.json';save(calpath,calibration)
        refined_engine=t.SourceTask(calpath)
        after={mode:refined_engine.certify(frozen['cases'][mode]['middle_threshold']) for mode in ('private','reuse')}
        attempt.update(C_display=proposal['C']['display'],gain_bounds=list(map(str,newgain)),
            branch='below' if newgain[1]<threshold else 'above_or_equal' if newgain[0]>=threshold else 'straddles',
            calibration_file=str(calpath.relative_to(ROOT)).replace('\\','/'),calibration_sha256=sha(calpath))
    for name,digest in contract['input_sha256'].items():assert sha(ROOT/name)==digest
    report={'passed':True,'contract_sha256':sha(CONTRACT),
      'observation_factorization':{'verdict':'REFUTED: the frozen task vacuum channel does not factor through the assembled ideal observer',
        'source_corner':[0,63],'hidden_source':[{'word':w,'marks':m,'coefficient':str(c)} for (w,m),c in source.items()],
        'assembled_value':'zero in all 3591 readouts','task_vacuum_value':'one',
        'moment_cost':str(8*2**16),'both_zero_and_hidden_source_fit_prior':True,
        'not_a_middle_task_counterexample':'Their positive readings are zero, outside the frozen middle interval. Its separately retained vacuum measurement must not be discarded.'},
      'exact_feasibility_reduction':{'cap':str(cap),'threshold':str(threshold),
        'theorem':'With fixed actual gains, the frozen joint source/prior fiber is nonempty iff E_positive >= threshold.',
        'necessity':'a_A2 >= raw_positive_lower/E; crossed coefficient is zero and vacuum coefficient is 1/100; all other moment costs are nonnegative.',
        'sufficiency':'Choose a_A2=raw_positive_lower/E, crossed=0, vacuum=1/100 and all other coefficients/backgrounds zero.',
        'nonemptiness_warning':'Deleting the low-gain branch conditional on existence is not a proof that the actual fiber is nonempty.'},
      'endpoint_attack':{'opposite_box_branches_verified':True,'realizable_opposing_actual_histories':False,
        'interpretation':'C_bin is fixed by the deployed filter, not a freely assignable source coordinate. Low-gain endpoints have EMPTY prior-compatible fibers; they are not opposing admitted sources.'},
      'bounded_pairing_attempt':attempt,'middle_results':after,
      'joint_history_claim':'NOT ESTABLISHED: no admitted cross-protocol dynamic history bridge or timing theorem follows from this test',
      'restatement':'For the frozen three-channel task INCLUDING its separately acquired vacuum reading, can an explicitly budgeted proof-only refinement certify the actual gain on one side of the exact feasibility threshold? Retention coherence is an interface condition, not the reason for sufficiency.'}
    save(N/'retained-middle-decision-conjecture-attack.json',report)
    print(json.dumps({'passed':True,'factorization':'refuted by explicit forgotten source',
      'pairing_attempt':{k:v for k,v in attempt.items() if k not in ('gain_bounds','stderr')},
      'middle_statuses':{mode:value['status'] for mode,value in after.items()},
      'actual_joint_history_counterexample':False},indent=2))

if __name__=='__main__':
    if '--projection' in sys.argv:projection()
    else:main()
