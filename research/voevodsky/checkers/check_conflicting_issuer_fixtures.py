"""No graph-order tie break for conflicting claimed Farkas row publishers."""
from pathlib import Path
import json
req=json.loads((Path(__file__).resolve().parents[1]/'results/row-attestation-request.json').read_text())
label=req['manifest']['source_id'];h=req['manifest_sha256']
a={'source_id':label,'issuer':'fictional-A','generation':1,'manifest':h,'event':'fictional-A-event','action':'attest-primitive-row-origin','graph_sequence':1}
b={'source_id':label,'issuer':'fictional-B','generation':2,'manifest':'different-ordered-row-manifest','event':'fictional-B-event','action':'attest-primitive-row-origin','graph_sequence':2}
def resolve(claims,registry):
 if registry is None:return 'UNAUTHENTICATED_CLAIMS'
 live=[c for c in claims if (c['issuer'],c['generation'],c['manifest'],c['event']) in registry['validated_live_claims']]
 if len(live)>1:return 'CONFLICTING_LIVE_GRANTS'
 if not live:return 'NO_VALID_LIVE_GRANT'
 c=live[0]
 if (c['issuer'],c['generation'],c['manifest'],c['event'])!=registry.get('designated'):return 'NO_DESIGNATED_LIVE_GRANT'
 return 'TEST_ONLY_REGISTRY_DESIGNATION_NOT_AUTHORIZED'
assert resolve((a,b),None)==resolve((b,a),None)=='UNAUTHENTICATED_CLAIMS'
key=lambda c:(c['issuer'],c['generation'],c['manifest'],c['event'])
conflict={'validated_live_claims':{key(a),key(b)},'designated':None}
assert resolve((a,b),conflict)==resolve((b,a),conflict)=='CONFLICTING_LIVE_GRANTS'
exclusive={'validated_live_claims':{key(a)},'designated':key(a)}
assert resolve((a,b),exclusive)=='TEST_ONLY_REGISTRY_DESIGNATION_NOT_AUTHORIZED'
assert resolve((a,b),dict(exclusive,designated=key(b)))=='NO_DESIGNATED_LIVE_GRANT'
report={'passed':True,'actual_state':'UNAUTHENTICATED_CLAIMS','hypothetical_two_live_incompatible':'CONFLICTING_LIVE_GRANTS','graph_order_reversal_invariant':True,'hypothetical_exclusive_live_registry':'TEST_ONLY_REGISTRY_DESIGNATION_NOT_AUTHORIZED','scope':'Fictional claims/registry only; no real trust root, signature, revocation stream, issuer designation or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/conflicting-issuer-fixtures.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
