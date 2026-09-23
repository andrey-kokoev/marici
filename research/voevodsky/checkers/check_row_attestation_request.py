"""Exact owner-input packet; mathematical evidence is not owner authentication."""
from hashlib import sha256
from pathlib import Path
import json
rows=[{'normal':['-1','0'],'upper':'0'},{'normal':['1','0'],'upper':'1'},
      {'normal':['0','-1'],'upper':'0'},{'normal':['0','1'],'upper':'1'}]
canonical=lambda obj:json.dumps(obj,sort_keys=True,separators=(',',':'))
manifest={'source_id':'fixed-unit-square-farkas-rows:v1','dimension':2,'ordered_primitive_rows':rows}
digest=sha256(canonical(manifest).encode()).hexdigest()
packet={'schema':'research.row-attestation-request.v1','manifest':manifest,'manifest_sha256':digest,
 'requester':'marici.Voevodsky','requested_owner':None,'owner_event_id':None,
 'requested_capabilities':['attest-primitive-row-origin','authorize-future-source-rooted-proof-use'],
 'required_owner_evidence':['authorized-issuer-identity','independently-bound-source-manifest','source-event-id','atomic-live-generation','revocation-route'],
 'mathematical_evidence':['research/voevodsky/results/integrated-tagged-thin-verifier.json','research/voevodsky/results/hypothetical-row-issuer.json'],
 'status':'owner_unassigned_no_live_grant'}
def validate(p):
 if sha256(canonical(p['manifest']).encode()).hexdigest()!=p['manifest_sha256']:return 'MANIFEST_DIGEST_MISMATCH'
 if p['requested_owner'] is None or p['owner_event_id'] is None:return 'OWNER_BOUNDARY_UNSATISFIED'
 # Caller-supplied owner labels and events never authenticate their own source.
 return 'OWNER_ATTESTATION_REQUIRES_INDEPENDENT_ISSUER_VERIFICATION'
assert validate(packet)=='OWNER_BOUNDARY_UNSATISFIED'
assert validate({**packet,'manifest_sha256':'0'*64})=='MANIFEST_DIGEST_MISMATCH'
assert validate({**packet,'requested_owner':'self','owner_event_id':'self'})=='OWNER_ATTESTATION_REQUIRES_INDEPENDENT_ISSUER_VERIFICATION'
base=Path(__file__).resolve().parents[1]
(base/'results/row-attestation-request.json').write_text(json.dumps(packet,indent=2)+'\n')
report={'passed':True,'manifest_sha256':digest,'owner_unassigned':True,'live_grant':False,'self_asserted_owner_event_refused':True,'digest_tamper_refused':True,'scope':'Evidence-bearing INPUT REQUEST only; owner and event are intentionally unset. No real attestation, publication, or analytic role mapping.'}
(base/'results/row-attestation-request-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
