"""Fresh conditional assembly checks; no experimental license or shared mutation."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
SUITES=[('passive_optical_gain_binding_v1.py','passive-optical-gain-binding-v1.json'),
 ('optical_statistical_feedback_v1.py','optical-statistical-feedback-v1.json'),
 ('optical_same_source_history_v1.py','optical-same-source-history-v1.json'),
 ('optical_adaptive_feedback_accuracy_v1.py','optical-adaptive-feedback-accuracy-v1.json'),
 ('optical_confidence_policy_v1.py','optical-confidence-policy-v1.json'),
 ('optical_calibration_bounds_v1.py','optical-calibration-bounds-v1.json')]
shared=ROOT/'research/conjecture_net/contracts/event-sourced-control-work-net.v1.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before=sha(shared); receipts=[]
for script,result in SUITES:
    run=subprocess.run([sys.executable,str(ROOT/'research/sontag/checkers'/script)],cwd=ROOT,capture_output=True,text=True,timeout=120)
    if run.returncode:raise RuntimeError(run.stderr or run.stdout)
    data=json.loads((ROOT/'research/sontag/results'/result).read_text(encoding='utf-8'))
    if data['passed'] is not True or not all(data['checks'].values()):raise ValueError('failed suite')
    receipts.append({'checker':script,'result':result,'checks':len(data['checks'])})
run=subprocess.run([sys.executable,str(ROOT/'research/sontag/checkers/check_optical_statistical_work_net_v1.py')],cwd=ROOT,capture_output=True,text=True)
if run.returncode:raise RuntimeError(run.stderr or run.stdout)
cpath=ROOT/'research/sontag/contracts/optical-statistical-control-work-net.v1.json'
c=json.loads(cpath.read_text(encoding='utf-8'))
if c['frontier'] or c['objective']['outcome'] is not None:raise ValueError('unclosed conditional branch or overclaimed root')
if sha(shared)!=before:raise ValueError('shared predecessor changed')
paths={str(cpath.relative_to(ROOT)), 'research/sontag/checkers/check_optical_binding_assembly_v1.py'}
paths.update(p for a in c['artifacts'] for p in a['paths'])
paths.update('research/sontag/checkers/'+s for s,_ in SUITES)
out={'schema':'marici.sontag.optical-binding-assembly.v1','passed':True,'conditional_only':True,
 'empirical_license':False,'shared_predecessor_changed':False,'receipts':receipts,
 'check_count':sum(r['checks'] for r in receipts),'deferred':'empirical-optical-realization',
 'source_sha256':{p:sha(ROOT/p) for p in sorted(paths)}}
p=ROOT/'research/sontag/results/optical-binding-assembly-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'suites':len(receipts),'checks':out['check_count'],'empirical_license':False},indent=2))
