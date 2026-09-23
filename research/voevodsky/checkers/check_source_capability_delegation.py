"""Synthetic delegated actions must be a subset of admitted parent actions."""
from pathlib import Path
import json
req=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
origin,use=req['requested_capabilities'];manifest=req['manifest_sha256']
parent={'issuer':'fictional-root','delegate':'fictional-agent','manifest':manifest,'actions':frozenset((origin,)),'expires':10}
def check(parent,edge,at):
 if edge is None:raise ValueError('DELEGATION_EDGE_MISSING')
 if edge['issuer']!=parent['issuer'] or edge['delegate']!=parent['delegate'] or edge['manifest']!=parent['manifest']:raise ValueError('DELEGATION_BINDING_MISMATCH')
 if not edge['actions']<=parent['actions']:raise ValueError('DELEGATION_ESCALATION')
 if at>min(parent['expires'],edge['expires']):raise ValueError('DELEGATION_EXPIRED')
 return 'TEST_ONLY_SCOPE_MATCH_NOT_AUTHORIZED'
ed=dict(parent,actions=frozenset((use,)),expires=9)
def refuse(edge,at,code):
 try:check(parent,edge,at)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('invalid delegation accepted')
refuse(None,8,'DELEGATION_EDGE_MISSING')
refuse(ed,8,'DELEGATION_ESCALATION')
valid=dict(ed,actions=frozenset((origin,)))
assert check(parent,valid,8)=='TEST_ONLY_SCOPE_MATCH_NOT_AUTHORIZED'
refuse(valid,11,'DELEGATION_EXPIRED')
refuse(dict(valid,manifest='foreign'),8,'DELEGATION_BINDING_MISMATCH')
report={'passed':True,'origin_only_parent_to_use':'DELEGATION_ESCALATION','missing_edge':'DELEGATION_EDGE_MISSING','expired_or_wrong_manifest':'refused','fictional_origin_to_origin':'TEST_ONLY_SCOPE_MATCH_NOT_AUTHORIZED','real_request':'unassigned issuer/event; no admitted parent, signature verifier or live delegation','scope':'Subset/expiry/binding structural test only; never accepts a live capability or authenticates issuer.'}
out=Path(__file__).resolve().parents[1]/'results/source-capability-delegation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
