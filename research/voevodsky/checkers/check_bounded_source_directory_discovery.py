"""Bounded trusted Site declarations do not appoint Farkas row source issuer."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[3]
request=json.loads((root/'research/voevodsky/results/row-attestation-request.json').read_text())
config=json.loads((root/'.narada/config.json').read_text())
roles=json.loads((root/'.narada/.ai/agents/role-plane.json').read_text())
site=(root/'.narada/AGENTS.md').read_text()
files=['.narada/AGENTS.md','.narada/README.md','.narada/config.json','.narada/.ai/agents/role-plane.json','.narada/capabilities/mcp-surfaces.json','.narada/epistemic/README.md']
assert request['requested_owner'] is None and request['owner_event_id'] is None
assert not any(any(x in k.lower() for x in ('row_owner','source_issuer','farkas_issuer')) for k in config)
assert all('Voevodsky' not in r.get('role_id','') for r in roles['roles'])
assert 'code and artifacts outside `site_root` are not Narada knowledge' in site
assert all('fixed-unit-square-farkas-rows' not in (root/f).read_text() for f in files)
report={'passed':True,'inspected_declaration_files':files,'request_source_id':request['manifest']['source_id'],'request_owner':None,'request_event':None,'directory_status':'OWNER_UNDISCOVERED_IN_INSPECTED_DECLARATIONS','non_conclusion':'No assertion that every possible registry or external owner is absent. Research author, path and graph actor are not source grants.','handoff':'No authenticated issuer recipient among inspected declarations; no invented owner message.'}
out=Path(__file__).resolve().parents[1]/'results/bounded-source-directory-discovery.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'directory_status':report['directory_status'],'inspected':len(files)}))
