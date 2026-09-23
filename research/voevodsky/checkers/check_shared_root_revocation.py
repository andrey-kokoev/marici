"""Common root revocation invalidates both previously checked route snapshots."""
from pathlib import Path
import json
req=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text());o,u=req['requested_capabilities']
root={'id':'fictional-root-event-7','epoch':7,'revoked':False,'manifest':req['manifest_sha256']}
route_a={'root_id':root['id'],'epoch':7,'actions':frozenset((o,))}
route_b={'root_id':root['id'],'epoch':7,'actions':frozenset((u,))}
def use(routes,snapshot,live):
 if snapshot['epoch']!=live['epoch'] or snapshot!=live:raise ValueError('ROOT_SNAPSHOT_STALE')
 if live['revoked']:raise ValueError('ROOT_REVOKED')
 if any(r['root_id']!=live['id'] or r['epoch']!=live['epoch'] for r in routes):raise ValueError('ROUTE_ROOT_BINDING_STALE')
 return frozenset().union(*(r['actions'] for r in routes))
assert use((route_a,route_b),dict(root),root)==frozenset((o,u))
revoked=dict(root,epoch=8,revoked=True)
for routes in ((route_a,),(route_b,),(route_a,route_b)):
 try:use(routes,root,revoked)
 except ValueError as err:assert str(err)=='ROOT_SNAPSHOT_STALE'
 else:raise AssertionError('stale shared root accepted')
try:use((route_a,route_b),revoked,revoked)
except ValueError as err:assert str(err)=='ROOT_REVOKED'
else:raise AssertionError('revoked root admitted')
rotated=dict(root,id='fictional-root-event-8',epoch=8)
try:use((route_a,route_b),rotated,rotated)
except ValueError as err:assert str(err)=='ROUTE_ROOT_BINDING_STALE'
else:raise AssertionError('routes migrated to new root')
report={'passed':True,'checked_at_epoch7':'origin and use in synthetic model','revoked_at_epoch8':'both old routes ROOT_SNAPSHOT_STALE; fresh snapshot ROOT_REVOKED','new_root_same_manifest':'ROUTE_ROOT_BINDING_STALE','actual_authority':'NO_REAL_ISSUER_OR_ROOT_GRANT','scope':'Synthetic atomic root/snapshot predicate, not signature verifier or publication permission; analytic roles deferred.'}
out=Path(__file__).resolve().parents[1]/'results/shared-root-revocation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
