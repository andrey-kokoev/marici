from bounded_replay import audit_file
from program_preflight import preflight
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import json
base=Path(__file__).resolve().parents[1];p=base/'results/replay-example.json';trace=json.loads(p.read_text());decl=trace['declaration'];plan=preflight(decl['bits'],decl['program'])
limits=dict(max_bytes=p.stat().st_size,max_certificates=len(trace['steps']),max_unary=2,max_rewrites=plan.rewrite_bound)
assert audit_file(p,**limits)['source_semantics']=='matched'
checks=0
for key in limits:
 bad=dict(limits);bad[key]-=1
 with patch('bounded_replay.semantic_replay',side_effect=AssertionError('expensive replay invoked')):
  try:audit_file(p,**bad)
  except ValueError:checks+=1
  else:raise AssertionError('limit not enforced')
with TemporaryDirectory() as tmp:
 path=Path(tmp)/'trace.json'
 for data in ('{"steps":[],"steps":[]}','{"steps":[],"value":NaN}'):
  path.write_text(data)
  try:audit_file(path,**limits)
  except ValueError:checks+=1
  else:raise AssertionError('ambiguous JSON accepted')
 with patch('builtins.open',side_effect=AssertionError('opened with invalid policy')):
  try:audit_file(path,**(limits|{'max_bytes':True}))
  except ValueError:checks+=1
  else:raise AssertionError('bad policy accepted')
report={'passed':True,'rejections':checks,'threshold_equality_accepted':True,'scope':'Byte/certificate/unary/estimated-work caps before semantic replay; JSON parser itself is not sandboxed.'}
(base/'results/bounded-replay.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
