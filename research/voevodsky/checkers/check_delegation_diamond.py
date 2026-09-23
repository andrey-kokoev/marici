"""Separate hypothetical delegation paths; never splice parent edges."""
from pathlib import Path
import json
req=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text());origin,use=req['requested_capabilities'];m=req['manifest_sha256']
root={'from':'fictional-root','to':'fictional-root','actions':frozenset((origin,use)),'manifest':m,'epoch':7}
a1={'from':'fictional-root','to':'A','actions':frozenset((origin,)),'manifest':m,'epoch':7};a2={'from':'A','to':'C','actions':frozenset((origin,)),'manifest':m,'epoch':7}
b1={'from':'fictional-root','to':'B','actions':frozenset((use,)),'manifest':m,'epoch':7};b2={'from':'B','to':'C','actions':frozenset((use,)),'manifest':m,'epoch':7}
def path(edges,live_epoch):
 effective=root['actions'];previous=root
 for e in edges:
  if e['from']!=previous['to'] or e['manifest']!=root['manifest']:raise ValueError('BROKEN_PATH')
  if e['epoch']!=live_epoch:raise ValueError('STALE_PATH')
  if not e['actions']<=effective:raise ValueError('CAPABILITY_ESCALATION')
  effective=effective&e['actions'];previous=e
 if previous['to']!='C':raise ValueError('WRONG_RECIPIENT')
 return effective
assert path((a1,a2),7)==frozenset((origin,))
assert path((b1,b2),7)==frozenset((use,))
assert path((a1,a2),7)|path((b1,b2),7)==frozenset((origin,use))
try:path((a1,b2),7)
except ValueError as err:assert str(err)=='BROKEN_PATH'
else:raise AssertionError('cross-path splice admitted')
try:path((b1,dict(b2,epoch=6)),7)
except ValueError as err:assert str(err)=='STALE_PATH'
else:raise AssertionError('stale route admitted')
assert path((a1,a2),7)==frozenset((origin,)) # other path failure does not erase A
report={'passed':True,'path_A':'origin only','path_B':'use only','union':'TEST_ONLY if BOTH paths independently validated','cross_path_splice':'BROKEN_PATH','stale_B':'STALE_PATH; only origin remains from A','real_world_status':'NO_AUTHENTICATED_ROOT_OR_SIGNED_EDGES','scope':'Synthetic scope/epoch structural model, not an authorization to compose unsigned evidence or actual Farkas proof publication.'}
out=Path(__file__).resolve().parents[1]/'results/delegation-diamond.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
