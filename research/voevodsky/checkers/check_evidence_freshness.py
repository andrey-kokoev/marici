from evidence_freshness import verify
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil,json
root=Path(__file__).resolve().parents[1]
assert verify(root)['fresh']
with TemporaryDirectory() as tmp:
 copy=Path(tmp)
 shutil.copytree(root/'checkers',copy/'checkers',ignore=shutil.ignore_patterns('__pycache__'))
 (copy/'results').mkdir()
 for name in ('recurrent-program-closure.json','combined-signature.json','replay-example.json'):shutil.copy2(root/'results'/name,copy/'results'/name)
 assert verify(copy)['fresh']
 for rel in ('checkers/program_runtime.py','results/combined-signature.json','results/replay-example.json'):
  p=copy/rel;original=p.read_bytes();p.write_bytes(original+b'\n')
  try:verify(copy)
  except ValueError:pass
  else:raise AssertionError('stale evidence accepted: '+rel)
  p.write_bytes(original)
print(json.dumps({'passed':True,'drifts_rejected':3,'scope':'Source and key generated dependency hashes; not signatures or environment reproducibility.'}))
