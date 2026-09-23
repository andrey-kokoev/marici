"""Bind local evidence paths to one canonical research root before reading."""
from pathlib import Path, PurePosixPath
from hashlib import sha256
import json
root=Path(__file__).resolve().parents[1];payload=json.loads((root/'results/unsent-owner-handoff-payload.json').read_text())
expected_root=root.resolve()
def resolve_evidence(path_text,actual_root):
 if actual_root.resolve()!=expected_root:raise ValueError('PROJECT_ROOT_REBIND')
 p=PurePosixPath(path_text)
 if p.is_absolute() or '..' in p.parts or '\\' in path_text or ':' in path_text:raise ValueError('UNSAFE_RELATIVE_PATH')
 resolved=(actual_root/Path(*p.parts)).resolve()
 if not resolved.is_relative_to(expected_root):raise ValueError('EVIDENCE_PATH_ESCAPE')
 return resolved
for item in payload['local_evidence']:
 path=resolve_evidence(item['path'],root)
 assert sha256(path.read_bytes()).hexdigest()==item['sha256']
def reject(path,actual_root,code):
 try:resolve_evidence(path,actual_root)
 except ValueError as err:assert str(err)==code
 else:raise AssertionError('unsafe rebind accepted')
reject('../outside.json',root,'UNSAFE_RELATIVE_PATH')
reject('/tmp/outside.json',root,'UNSAFE_RELATIVE_PATH')
reject('results\\x.json',root,'UNSAFE_RELATIVE_PATH')
reject('results/row-attestation-request.json',root.parent,'PROJECT_ROOT_REBIND')
report={'passed':True,'actual_references':len(payload['local_evidence']),'project_root':str(expected_root),'parent_absolute_backslash':'UNSAFE_RELATIVE_PATH','wrong_project_root':'PROJECT_ROOT_REBIND','symlink_escape':'resolver rejects any resolved target outside root; no symlink created or exercised','authorization':'LOCAL_PREPARED_UNSENDABLE, no owner route','scope':'Local path-resolution policy only; not atomic open/realpath protection against concurrent link swaps or source authority.'}
out=root/'results/unsent-payload-path-binding.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'references':report['actual_references'],'root_bound':True,'status':report['authorization']}))
