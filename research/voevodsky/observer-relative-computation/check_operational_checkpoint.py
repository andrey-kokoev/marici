"""Fresh strict aggregate closure, exact entry coverage, and two negative controls."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,tempfile,time
root=Path(__file__).resolve().parent;repo=root.parents[2]
previous=repo/'research/voevodsky/resolution-net-v1/agda'
cubical=Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')
roots=[root/'agda',previous,repo/'research/nima/agda',cubical]
aggregate=root/'agda/ObserverOperationalCheckpoint.agda'
bridges=['ResolutionNetInterpretation','ResolutionNetDependentSubstitution','ResolutionNetDependentInterface','ResolutionNetDependentMachine','ResolutionNetObservation','ResolutionNetObservationGluing']
results=root/'results';results.mkdir(exist_ok=True);receipt=results/'operational-checkpoint.json'
start=time.monotonic();report={'passed':False,'scope':'Fresh safe aggregate import closure, not a compiler/OS proof or physical interpretation. Prior foundation-audit.json is retained as historical evidence.'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def label(p):
 try:return str(p.relative_to(repo))
 except ValueError:return str(p)
def imports(p):return re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)',p.read_text(encoding='utf-8'),re.M)
def entries():return {p.stem for p in (root/'agda').glob('*.agda') if p!=aggregate}|set(bridges)
def inventory():
 seen=set();todo=[aggregate];external=set()
 while todo:
  p=todo.pop()
  if p in seen:continue
  seen.add(p)
  for module in imports(p):
   rel=Path(*module.split('.')).with_suffix('.agda')
   candidate=next((r/rel for r in roots if (r/rel).exists()),None)
   if candidate is None:external.add(module)
   else:todo.append(candidate)
 seen.update(root.glob('*.py'))
 return {label(p):sha(p) for p in sorted(seen)},sorted(external)
def save():receipt.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
save()
try:
 expected=entries();declared=imports(aggregate)
 if set(declared)!=expected or len(declared)!=len(expected):raise RuntimeError('aggregate entry inventory is not exact')
 before,external=inventory()
 report.update(source_sha256=before,unresolved_toolchain_imports=external,entry_modules=sorted(expected),agda_version=subprocess.check_output(['agda','--version'],text=True).strip(),python_version=sys.version)
 command=['agda','--safe','--cubical','--guardedness','--ignore-interfaces','--transliterate','-Werror']
 for p in roots:command+=['-i',str(p)]
 report['command']=command+[str(aggregate)];save()
 print('Fresh aggregate check:',len(expected),'entry modules',flush=True)
 checked=subprocess.run(report['command'],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=360)
 log=results/'agda-operational-checkpoint.log';text=checked.stdout+'\n'+checked.stderr;log.write_text(text,encoding='utf-8')
 report.update(positive_exit_code=checked.returncode,positive_log_sha256=sha(log))
 seen=set(re.findall(r'Checking\s+([\w.]+)\s+\(',text));missing=expected-seen
 report['missing_fresh_entry_checks']=sorted(missing)
 if checked.returncode or missing:raise RuntimeError('positive closure or fresh-entry coverage failed')
 negative='{-# OPTIONS --safe --cubical --guardedness #-}\nmodule RejectObserverAudit where\nopen import Cubical.Foundations.Prelude\nopen import Cubical.Data.Bool.Base\ninvalid : true ≡ false\ninvalid = refl\n'
 retained=results/'rejected-observer-audit.agda.txt';retained.write_text(negative,encoding='utf-8')
 with tempfile.TemporaryDirectory(prefix='observer-audit-') as directory:
  source=Path(directory)/'RejectObserverAudit.agda';source.write_text(negative,encoding='utf-8')
  rejected=subprocess.run(command+['-i',directory,str(source)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
 rejection=rejected.stdout+'\n'+rejected.stderr;badlog=results/'agda-rejected-observer-audit.log';badlog.write_text(rejection,encoding='utf-8')
 report.update(negative_exit_code=rejected.returncode,negative_source_sha256=sha(retained),negative_log_sha256=sha(badlog))
 if rejected.returncode==0 or '[UnequalTerms]' not in rejection:raise RuntimeError('negative control did not fail by type inequality')
 semantic_negative='{-# OPTIONS --safe --cubical --guardedness #-}\nmodule RejectSignedWinding where\nopen import Cubical.Foundations.Prelude\nopen import Cubical.Data.Int.Base using (pos)\nimport ObserverSignedNormalization as N\nimport ObserverSignedCyclicCover as S\ninvalid : N.integer (S.path S.up) ≡ pos 0\ninvalid = refl\n'
 semantic_source=results/'rejected-signed-winding.agda.txt';semantic_source.write_text(semantic_negative,encoding='utf-8')
 with tempfile.TemporaryDirectory(prefix='observer-signed-control-') as directory:
  source=Path(directory)/'RejectSignedWinding.agda';source.write_text(semantic_negative,encoding='utf-8')
  rejected_signed=subprocess.run(command+['-i',directory,str(source)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
 signed_text=rejected_signed.stdout+'\n'+rejected_signed.stderr
 signed_log=results/'agda-rejected-signed-winding.log';signed_log.write_text(signed_text,encoding='utf-8')
 report.update(signed_negative_exit_code=rejected_signed.returncode,signed_negative_source_sha256=sha(semantic_source),signed_negative_log_sha256=sha(signed_log))
 if rejected_signed.returncode==0 or '[UnequalTerms]' not in signed_text:raise RuntimeError('signed winding negative control did not fail by type inequality')
 report['negative_control_count']=2
 after,remaining=inventory()
 if before!=after or remaining!=external or entries()!=expected:raise RuntimeError('source or entry inventory changed during audit')
 report.update(passed=True,source_unchanged=True,entry_count=len(expected),source_count=len(before),negative_control_passed=True)
except Exception as error:
 report['error']=str(error)
 raise
finally:
 report['seconds']=round(time.monotonic()-start,3);save()
print(json.dumps({k:report[k] for k in ('passed','entry_count','source_count','source_unchanged','negative_control_passed','seconds')},indent=2))
