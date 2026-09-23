"""Shortcut is a derived view, never a destructive rewrite of audit edges."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
audit={'events':{'fake-x1':{'bound':1},'fake-x2':{'bound':2},'fake-x3':{'bound':3}},'edges':(('fake-x1','fake-x2','weakening'),('fake-x2','fake-x3','weakening'))}
def H(x):return sha256(repr(x).encode()).hexdigest()
old=deepcopy(audit);digest=H(old)
def shortcut(graph):
 if graph['edges']!=(('fake-x1','fake-x2','weakening'),('fake-x2','fake-x3','weakening')):raise ValueError('PATH_NOT_VALIDATED')
 if tuple(graph['events'][x]['bound'] for x in ('fake-x1','fake-x2','fake-x3'))!=(1,2,3):raise ValueError('BOUNDS_INVALID')
 return {'kind':'derived-arithmetic-view','source_path_digest':H(graph),'source_path_ids':('fake-x1','fake-x2','fake-x3'),'direct_math':{'from_bound':1,'to_bound':3,'surplus_increment':2},'observed_direct_edge':False}
view=shortcut(audit)
assert audit==old and H(audit)==digest and view['source_path_digest']==digest
assert ('fake-x1','fake-x3','weakening') not in audit['edges'] and not view['observed_direct_edge']
tampered=deepcopy(audit);tampered['events']['fake-x2']['bound']=4
try:shortcut(tampered)
except ValueError as err:assert str(err)=='BOUNDS_INVALID'
else:raise AssertionError('bad intermediate accepted')
assert view['source_path_digest']!=H(tampered)
report={'passed':True,'original_chain':'preserved with both edges and intermediate occurrence','direct_shortcut':'derived arithmetic view referencing entire original path digest, not observed direct event','tampered_intermediate':'refused; stale view digest','scope':'Synthetic audit graph only, not an actual observed derivation, row-source issuer or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/nondestructive-weakening-shortcut.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
