"""Content freshness, not authenticity or evidence of universal correctness."""
from pathlib import Path
import hashlib,json

def hashes(paths,root):return {str(p.relative_to(root)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}
def sources(root):return hashes((root/'checkers').glob('*.py'),root)
def verify(root):
 report=json.loads((root/'results/recurrent-program-closure.json').read_text())
 if not report.get('passed') or not report.get('sources_stable'):raise ValueError('closure not successful/stable')
 if sources(root)!=report['source_snapshot']:raise ValueError('source drift')
 for name,expected in report['dependency_artifacts'].items():
  p=root/name
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:raise ValueError('artifact drift: '+name)
 from offline_replay import contract,digest
 if digest(contract())!=report['replay_contract_digest']:raise ValueError('contract drift')
 return {'fresh':True,'suites':len(report['suites']),'authenticated':False}

if __name__=='__main__':print(json.dumps(verify(Path(__file__).resolve().parents[1])))
