"""Isolated source-copy mutations; non-assertion failures are not detections."""
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import shutil
import sys
import json
import hashlib
base=Path(__file__).resolve().parent
cases=[
 ('duplicate-boundary','scanning_set_program.py',"(n+'.b',g+'.u')","(n+'.f',g+'.u')",'check_combined_signature.py'),
 ('swap-fuel-cursor','scanning_set_program.py',"(n+'.f',g+'.p'),(n+'.b',g+'.u')","(n+'.b',g+'.p'),(n+'.f',g+'.u')",'check_scanning_set_program.py'),
 ('false-as-true','scanning_set_program.py',"value=kind=='TRUE'","value=kind=='FALSE'",'check_scanning_set_program.py'),
 ('early-completion','fuel_scanner.py',"complete=peer.endswith('.p') and self.kind(peer.split('.')[0])=='DONE'","complete=outcome is not None",'check_scanner_observation.py'),
]
def hashes():return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in base.glob('*.py')}
before=hashes();results=[]
for label,source,old,new,checker in cases:
 with TemporaryDirectory(prefix='recurrent-mutation-') as temp:
  target=Path(temp)/'checkers';target.mkdir();(Path(temp)/'results').mkdir()
  for p in base.glob('*.py'):shutil.copy2(p,target/p.name)
  command=[sys.executable,'-E',str(target/checker)]
  baseline=subprocess.run(command,cwd=target,capture_output=True,text=True,timeout=120)
  assert baseline.returncode==0,(label,baseline.stderr)
  file=target/source;text=file.read_text();assert text.count(old)==1
  changed=text.replace(old,new);compile(changed,str(file),'exec');file.write_text(changed)
  # Remove bytecode caches so equal-size edits cannot reuse timestamp-based pyc.
  shutil.rmtree(target/'__pycache__',ignore_errors=True)
  run=subprocess.run(command,cwd=target,capture_output=True,text=True,timeout=120)
  detected=run.returncode!=0 and 'AssertionError' in run.stderr
  results.append({'mutation':label,'source':source,'old':old,'new':new,'checker':checker,'baseline_passed':True,'detected_by_assertion':detected,'returncode':run.returncode,'stderr':run.stderr[-6000:]})
assert before==hashes(),'production sources changed'
report={'passed':all(r['detected_by_assertion'] for r in results),'cases':results,'production_sources_unchanged':True,'scope':'Four explicit mutations; baseline rerun in isolated copy per case. Not comprehensive fault coverage or correctness certification.'}
p=base.parent/'results/closure-mutations.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'detected':sum(r['detected_by_assertion'] for r in results),'total':len(results)}))
assert report['passed']
