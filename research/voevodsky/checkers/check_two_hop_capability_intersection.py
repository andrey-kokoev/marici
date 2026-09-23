"""Two-hop grants carry the running intersection, not root action union."""
from pathlib import Path
import json
req=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
origin,use=req['requested_capabilities'];m=req['manifest_sha256']
root={'from':'fictional-root','to':'agent-A','actions':frozenset((origin,use)),'manifest':m,'expiry':20}
one={'from':'agent-A','to':'agent-B','actions':frozenset((origin,)),'manifest':m,'expiry':15}
two={'from':'agent-B','to':'agent-C','actions':frozenset((use,)),'manifest':m,'expiry':12}
def fold(edges,at):
 effective=edges[0]['actions'];expiry=edges[0]['expiry'];previous=edges[0]
 for e in edges[1:]:
  if e['from']!=previous['to'] or e['manifest']!=previous['manifest']:raise ValueError('CHAIN_BINDING_MISMATCH')
  if not e['actions']<=effective:raise ValueError('INTERMEDIATE_CAPABILITY_ESCALATION')
  effective=effective&e['actions'];expiry=min(expiry,e['expiry']);previous=e
 if at>expiry:raise ValueError('CHAIN_EXPIRED')
 return effective
try:fold((root,one,two),10)
except ValueError as err:assert str(err)=='INTERMEDIATE_CAPABILITY_ESCALATION'
else:raise AssertionError('root privilege restored after narrowing')
valid=dict(two,actions=frozenset((origin,)))
assert fold((root,one,valid),10)==frozenset((origin,))
try:fold((root,one,valid),16)
except ValueError as err:assert str(err)=='CHAIN_EXPIRED'
else:raise AssertionError('past intermediate expiry admitted')
try:fold((root,one,dict(valid,**{'from':'other'})),10)
except ValueError as err:assert str(err)=='CHAIN_BINDING_MISMATCH'
else:raise AssertionError('different delegate accepted')
report={'passed':True,'root_actions':'origin+use','first_delegation':'origin only','second_use_attempt':'INTERMEDIATE_CAPABILITY_ESCALATION despite root having use','valid_origin_path':'TEST_ONLY running intersection origin','expiry':'minimum across hops','wrong_delegate':'CHAIN_BINDING_MISMATCH','actual_status':'No real row issuer, root grant, signed edges or publication authorization','scope':'Synthetic two-hop set model; no trusted signatures or analytic role correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/two-hop-capability-intersection.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
