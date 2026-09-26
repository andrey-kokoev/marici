"""Package local review artifacts; hash consistency is not code authenticity."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys
FILES=('pure_replacement.py','certified_replacement.py','rule_templates.py','remaining_rule_templates.py','program_inputs.py','initial_net_recognizer.py','offline_replay.py','source_interpreter.py','semantic_replay.py')
EXPECTED={*(f'checkers/{name}' for name in FILES),'results/combined-signature.json','results/replay-example.json'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build(destination):
 from evidence_freshness import verify
 root=Path(__file__).resolve().parents[1];verify(root)
 destination=Path(destination);destination.mkdir(parents=True,exist_ok=False)
 hashes={}
 for relative in sorted(EXPECTED):
  target=destination/relative;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/relative,target);hashes[relative]=sha(target)
 manifest={'schema':'local-audit-bundle-v1','files':hashes,'authenticated':False,'scope':'Trusted local Python code plus replay dependencies. Do not execute unauthenticated third-party bundles.'}
 (destination/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 return manifest

def verify_bundle(directory,*,execute=False):
 directory=Path(directory);manifest=json.loads((directory/'manifest.json').read_text())
 if manifest.get('schema')!='local-audit-bundle-v1' or set(manifest.get('files',{}))!=EXPECTED:raise ValueError('bundle manifest mismatch')
 for relative,expected in manifest['files'].items():
  p=directory/relative
  if not p.is_file() or p.is_symlink() or sha(p)!=expected:raise ValueError('missing/altered bundle file: '+relative)
 result={'consistent':True,'authenticated':False,'executed':False}
 if execute:
  # Explicit opt-in: the caller must trust the copied Python code.
  code="import sys,json; from pathlib import Path; sys.path.insert(0,sys.argv[1]); from semantic_replay import semantic_replay; print(json.dumps(semantic_replay(json.loads(Path(sys.argv[2]).read_text())))); assert 'scanning_set_program' not in sys.modules"
  run=subprocess.run([sys.executable,'-I','-c',code,str((directory/'checkers').resolve()),str((directory/'results/replay-example.json').resolve())],cwd=directory,capture_output=True,text=True,check=True,timeout=120)
  result.update(executed=True,replay=json.loads(run.stdout))
 return result

if __name__=='__main__':
 print(json.dumps(verify_bundle(sys.argv[1],execute='--execute-trusted' in sys.argv[2:])))
