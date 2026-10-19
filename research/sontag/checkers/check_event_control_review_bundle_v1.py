"""Fresh local suite run and review evidence manifest; no shared net mutation."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
PACKETS=['typed-event-control-interface-v1.md','history-to-state-congruence-v1.md',
         'observation-feedback-realization-v1.md','presentation-naturality-v1.md',
         'wg-retained-history-congruence-v1.md','mathematical-control-realization-candidate-v1.md']
SUITES=[('typed_event_control_interface_v1.py','typed-event-control-interface-v1.json'),
        ('history_to_state_congruence_v1.py','history-to-state-congruence-v1.json'),
        ('observation_feedback_realization_v1.py','observation-feedback-realization-v1.json'),
        ('presentation_naturality_v1.py','presentation-naturality-v1.json'),
        ('wg_retained_history_transport_v1.py','wg-retained-history-transport-v1.json')]
SOURCES=['research/nima/agda/ComposableWitnessSpecialization.agda',
         'research/strominger/checkers/energy_task_reduction.py',
         'research/strominger/checkers/energy_target_controller.py',
         'research/sontag/checkers/contextual_capability_coalgebra.py',
         'research/conjecture_net/contracts/event-sourced-control-work-net.v1.json']
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
before={p:sha(p) for p in SOURCES}
receipts=[]
paths=SOURCES+['research/sontag/'+p for p in PACKETS]
for script,result in SUITES:
    p='research/sontag/checkers/'+script
    run=subprocess.run([sys.executable,str(ROOT/p)],cwd=ROOT,capture_output=True,text=True)
    if run.returncode: raise RuntimeError(run.stderr or run.stdout)
    rp='research/sontag/results/'+result
    data=json.loads((ROOT/rp).read_text(encoding='utf-8'))
    if data.get('passed') is not True or not all(data['checks'].values()):
        raise ValueError('failed evidence: '+rp)
    receipts.append({'checker':p,'result':rp,'exit_code':run.returncode,'checks':len(data['checks'])})
    paths += [p,rp]
if before != {p:sha(p) for p in SOURCES}: raise ValueError('source or shared net changed during review run')
paths.append('research/sontag/checkers/check_event_control_review_bundle_v1.py')
out={'schema':'marici.sontag.event-control-review-manifest.v1','passed':True,
     'candidate_only':True,'shared_net_modified':False,'fresh_agda_check':False,
     'receipts':receipts,'source_sha256':{p:sha(p) for p in paths},
     'open_gates':['owner scope review','physical binding','same-source comparison','extension/coverage']}
p=ROOT/'research/sontag/results/event-control-review-manifest-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'suites':len(receipts),'checks':sum(r['checks'] for r in receipts),'hashed_files':len(paths)},indent=2))
