"""Bounded evidence audit: author/path/graph actor != source-row issuer grant."""
from pathlib import Path
import json,glob
root=Path(__file__).resolve().parents[3]
request=json.loads((root/'research/voevodsky/results/row-attestation-request.json').read_text())
event=json.loads(Path(glob.glob(str(root/'.narada/epistemic/ledger/ev-000000015066-*.json'))[0]).read_text())
site=(root/'.narada/AGENTS.md').read_text()
graph=(root/'.narada/epistemic/README.md').read_text()
assert request['requested_owner'] is None and request['owner_event_id'] is None
assert event['identity_state']['authentication']['status']=='missing'
assert event['identity_state']['authority']['granted'] is False
assert event['certifies_truth'] is False
assert 'does not certify truth' in graph
assert 'code and artifacts outside `site_root` are not Narada knowledge' in site
report={'passed':True,'inspected':['frozen row request','actual event 15066','tracked epistemic README','site-local AGENTS.md'],'row_request_owner_unassigned':True,'graph_actor_source_grant':False,'project_path_implies_source_authority':False,'bounded_result':'NO_ADMITTED_FARKAS_ROW_ISSUER_IN_INSPECTED_EVIDENCE','scope':'Read-only bounded evidence audit, not global proof of absence in all possible surfaces; no unauthorized owner communication or site-law mutation.'}
out=Path(__file__).resolve().parents[1]/'results/farkas-issuer-evidence-scope.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
