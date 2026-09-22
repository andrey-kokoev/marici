"""Create compact replayable transport frames for two frozen signed-task decisions."""
from pathlib import Path
import importlib.util,json,hashlib,copy
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck';OUT=ROOT/'research/voevodsky/results'
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
t=module('task',G/'checkers/three_channel_source_task.py');v=module('verify',G/'certificates/verify_source_task_transition.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
cal=G/'results/three-channel-source-task-calibration-signed-pairing.json';frozen_path=G/'results/calibration-refinement-frozen-inputs.json'
chains=G/'results/portable-source-task-transitions';frozen=json.loads(frozen_path.read_text());engine=t.SourceTask(cal)
for n in ('lower_threshold','upper_threshold'):v.verify(v.load(chains/f'private-{n}-signed-pairing.json'))
def frame(name):
 task=copy.deepcopy(frozen['cases']['private'][name]);result=engine.certify(task)
 assert result['status'] in ('CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE')
 proof={'kind':'marici.signed-source-task-transport.v1','calibration_sha256':sha(cal),
   'frozen_inputs_sha256':sha(frozen_path),'task_id':name,'mode':task['mode'],'budget':task['budget'],'auto_witness':task['auto_witness'],
   'raw':task['raw'],'claimed_status':result['status'],
   'necessary_cost':result['necessary_moment_cost_lower_bound'],
   'portable_chain_sha256':sha(chains/f'private-{name}-signed-pairing.json')}
 return proof
frames={n:frame(n) for n in ('lower_threshold','upper_threshold')}
# The compact frame carries raw obligations and hashes, not B's uncheckable word.
def verify(x):
 assert set(x)=={'kind','calibration_sha256','frozen_inputs_sha256','task_id','mode','budget','auto_witness','raw','claimed_status','necessary_cost','portable_chain_sha256'}
 assert x['kind']=='marici.signed-source-task-transport.v1' and x['calibration_sha256']==sha(cal)
 assert x['frozen_inputs_sha256']==sha(frozen_path) and x['mode']=='private'
 assert x['task_id'] in ('lower_threshold','upper_threshold')
 assert x['raw']==frozen['cases']['private'][x['task_id']]['raw']
 assert set(x['raw'])==set(t.NAMES)
 r=engine.certify({k:x[k] for k in ('mode','budget','auto_witness','raw')})
 assert r['status']==x['claimed_status'] and r['necessary_moment_cost_lower_bound']==x['necessary_cost']
 return r
for x in frames.values():verify(x)
assert {x['claimed_status'] for x in frames.values()}=={'CERTIFIED_FEASIBLE','CERTIFIED_INFEASIBLE'}
# The common two rows do not distinguish these valid opposite task worlds.
common={k:frames['lower_threshold']['raw'][k] for k in ('vacuum','crossed')}
assert common=={k:frames['upper_threshold']['raw'][k] for k in common}
rejected=[]
for label,mutate in (
 ('changed calibration binding',lambda x:x.__setitem__('calibration_sha256','0'*64)),
 ('changed decision claim',lambda x:x.__setitem__('claimed_status','CERTIFIED_FEASIBLE')),
 ('changed necessary cost',lambda x:x.__setitem__('necessary_cost','0')),
 ('changed positive row',lambda x:x['raw']['positive'].__setitem__('center','0')),
 ('missing positive row',lambda x:x['raw'].pop('positive'))):
 bad=copy.deepcopy(frames['upper_threshold']);mutate(bad)
 try:verify(bad)
 except (AssertionError,KeyError,ValueError):rejected.append(label)
 else:raise AssertionError('accepted corruption: '+label)
report={'passed':True,'schema':'marici.signed-source-task-transport.v1','calibration':str(cal.relative_to(ROOT)),
 'calibration_sha256':sha(cal),'frozen_inputs_sha256':sha(frozen_path),'frames':frames,
 'common_coarse_rows':common,'contrasting_outcomes':{n:x['claimed_status'] for n,x in frames.items()},
 'checks':{'local_replay_from_frame':True,'portable_chains_verified':True,'common_rows_leave_opposite_outcomes':True,
            'rejected_corruptions':rejected},
 'scope':'A bounded task-specific transport format. It establishes sufficiency of this frame for independent replay and necessity of the positive row within the two declared contrasting worlds; it does not prove information-theoretic minimality over all possible encodings or source tasks.'}
(OUT/'signed-task-transport.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'frame_bytes':{n:len(canonical(x)) for n,x in frames.items()},'rejected':rejected},indent=2))
