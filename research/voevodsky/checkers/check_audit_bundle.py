from audit_bundle import build,verify_bundle
from pathlib import Path
from tempfile import TemporaryDirectory
import json
with TemporaryDirectory(prefix='portable-audit-') as tmp:
 bundle=Path(tmp)/'bundle';manifest=build(bundle)
 result=verify_bundle(bundle,execute=True)
 assert result['replay']['source_semantics']=='matched' and result['replay']['steps']==70
 for relative in ('checkers/pure_replacement.py','results/combined-signature.json','results/replay-example.json'):
  p=bundle/relative;original=p.read_bytes();p.write_bytes(original+b'\n')
  try:verify_bundle(bundle)
  except ValueError:pass
  else:raise AssertionError('altered dependency accepted')
  p.unlink()
  try:verify_bundle(bundle)
  except ValueError:pass
  else:raise AssertionError('missing dependency accepted')
  p.write_bytes(original)
report={'passed':True,'bundled_files':len(manifest['files']),'isolated_replay_steps':70,'altered_or_missing_rejections':6,'scope':'Portable temporary-directory replay with -I; hash consistency, not authenticated code.'}
p=Path(__file__).resolve().parents[1]/'results/audit-bundle.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
