from semantic_replay import semantic_replay
from offline_replay import replay
from pathlib import Path
from copy import deepcopy
from unittest.mock import patch
import json,subprocess,sys
base=Path(__file__).resolve().parents[1];trace=json.loads((base/'results/replay-example.json').read_text())
result=semantic_replay(trace);assert result['source_semantics']=='matched' and result['authenticated'] is False
partial=deepcopy(trace);partial['complete']=False
assert replay(partial)['terminal'] is None
try:semantic_replay(partial)
except ValueError as e:assert 'complete trace' in str(e)
else:raise AssertionError('partial accepted')
# Unit-test the explicit comparator path; shared source/manifest fault is separate.
with patch('semantic_replay.interpret',return_value={'word':(),'observations':()}):
 try:semantic_replay(trace)
 except ValueError as e:assert 'differs' in str(e)
 else:raise AssertionError('mismatch accepted')
run=subprocess.run([sys.executable,'-E',str(Path(__file__).with_name('semantic_replay.py')),str(base/'results/replay-example.json')],capture_output=True,text=True,check=True)
assert json.loads(run.stdout)['source_semantics']=='matched'
print(json.dumps({'passed':True,'complete_example_steps':result['steps'],'partial_rejected':True,'semantic_mismatch_rejected':True,'cli_checked':True}))
