"""Immutable local proof-use REQUEST is not an authorization or owner message."""
from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parents[1]
source=json.loads((root/'results/row-attestation-request.json').read_text())
def H(value):return sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
packet={'multipliers':['0','1','0','0'],'surplus':'0','target_normal':['1','0'],'target_bound':'1'}
request={'schema':'research.local-proof-use-request.v1','source_id':source['manifest']['source_id'],'source_manifest_sha256':source['manifest_sha256'],'source_generation':None,'owner':None,'action':'authorize-future-source-rooted-proof-use','packet_sha256':H(packet),'status':'LOCAL_UNAUTHORIZED_REQUEST'}
def check(req,proof,claimed_action,live_generation):
 if req['action']!=claimed_action:raise ValueError('ACTION_SUBSTITUTION')
 if H(proof)!=req['packet_sha256']:raise ValueError('PACKET_SUBSTITUTION')
 if req['source_generation'] is None or live_generation is None:raise ValueError('SOURCE_GENERATION_UNASSIGNED')
 if req['source_generation']!=live_generation:raise ValueError('GENERATION_MISMATCH')
 return 'REQUEST_FIELDS_MATCH_NOT_AUTHORIZED'
assert H(packet)==request['packet_sha256']
def refuse(req,proof,action,gen,code):
 try:check(req,proof,action,gen)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('unauthorized or substituted request accepted')
refuse(request,dict(packet,multipliers=['0','0','0','1']),request['action'],None,'PACKET_SUBSTITUTION')
refuse(request,packet,'attest-primitive-row-origin',None,'ACTION_SUBSTITUTION')
refuse(request,packet,request['action'],None,'SOURCE_GENERATION_UNASSIGNED')
hypothetical=dict(request,source_generation=7)
refuse(hypothetical,packet,request['action'],8,'GENERATION_MISMATCH')
assert check(hypothetical,packet,request['action'],7)=='REQUEST_FIELDS_MATCH_NOT_AUTHORIZED'
report={'passed':True,'request':request,'packet':packet,'packet_substitution':'PACKET_SUBSTITUTION','action_substitution':'ACTION_SUBSTITUTION','actual_generation':'SOURCE_GENERATION_UNASSIGNED','hypothetical_matching_generation':'REQUEST_FIELDS_MATCH_NOT_AUTHORIZED','scope':'Local immutable-intent test only. No issuer, authorized recipient, signed owner event, actual source generation or proof-use publication grant.'}
(root/'results/proof-use-request-envelope.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'request_digest':H(request),'status':request['status'],'actual_generation':report['actual_generation']}))
