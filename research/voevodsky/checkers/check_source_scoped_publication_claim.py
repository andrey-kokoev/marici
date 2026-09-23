"""Graph admission, row mathematics and issuer attestation are different types."""
import json,glob
from pathlib import Path
root=Path(__file__).resolve().parents[3]
event=json.loads(Path(glob.glob(str(root/'.narada/epistemic/ledger/ev-000000015066-*.json'))[0]).read_text())
request=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
def gate(graph_record,math_verified,claim,external_owner_verifier=None):
 if graph_record.get('event_kind')!='proposal_admitted':return 'NOT_GRAPH_ADMISSION'
 if not math_verified:return 'MATH_NOT_VERIFIED'
 if claim.get('source')!=request['manifest']['source_id'] or claim.get('row_digest')!=request['manifest_sha256']:return 'SOURCE_MANIFEST_MISMATCH'
 if not claim.get('issuer') or not claim.get('source_event'):return 'MISSING_OWNER_EVENT_BINDING'
 if external_owner_verifier is None:return 'OWNER_ATTESTATION_UNVERIFIED'
 if not external_owner_verifier(claim):return 'OWNER_ATTESTATION_REJECTED'
 return 'CONDITIONAL_EXTERNAL_OWNER_ATTESTATION_ONLY'
claim={'source':request['manifest']['source_id'],'row_digest':request['manifest_sha256'],'issuer':'marici.Voevodsky','source_event':'self-claimed-event'}
assert gate(event,True,claim)=='OWNER_ATTESTATION_UNVERIFIED'
assert gate(event,True,claim,lambda _:False)=='OWNER_ATTESTATION_REJECTED'
assert gate(event,True,claim,lambda _:True)=='CONDITIONAL_EXTERNAL_OWNER_ATTESTATION_ONLY'
assert gate(event,False,claim)=='MATH_NOT_VERIFIED'
assert gate(event,True,{**claim,'row_digest':'fake'})=='SOURCE_MANIFEST_MISMATCH'
assert gate(event,True,{**claim,'source_event':None})=='MISSING_OWNER_EVENT_BINDING'
assert event['certifies_truth'] is False and event['identity_state']['authority']['granted'] is False
report={'passed':True,'graph_record_type':'coordination admission','math_record_type':'local checked Farkas source','owner_attestation_type':'absent external verifier','self_claimed_same_actor_name_insufficient':True,'positive_stub':'conditional only under injected external verifier premise','refused':['MATH_NOT_VERIFIED','SOURCE_MANIFEST_MISMATCH','MISSING_OWNER_EVENT_BINDING','OWNER_ATTESTATION_REJECTED'],'scope':'Read-only graph event plus locally constructed source packet. True callback is a hypothetical trusted premise, not actual owner authentication or publication checkpoint.'}
out=Path(__file__).resolve().parents[1]/'results/source-scoped-publication-claim.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
