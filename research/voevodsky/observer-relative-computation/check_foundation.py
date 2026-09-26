"""Fresh, source-bound audit of the observer programme and its bridge modules."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,time
root=Path(__file__).resolve().parent;repo=root.parents[2]
previous=repo/'research/voevodsky/resolution-net-v1/agda'
cubical=Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')
roots=[root/'agda',previous,repo/'research/nima/agda',cubical]
bridges=['ResolutionNetInterpretation','ResolutionNetDependentSubstitution','ResolutionNetDependentInterface','ResolutionNetDependentMachine','ResolutionNetObservation','ResolutionNetObservationGluing']
entries=sorted((root/'agda').glob('*.agda'))+[previous/(name+'.agda') for name in bridges]
results=root/'results';results.mkdir(exist_ok=True);receipt=results/'foundation-audit.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def label(p):
 try:return str(p.relative_to(repo))
 except ValueError:return str(p)
def inventory():
 seen=set();todo=list(entries);unresolved=set()
 while todo:
  p=todo.pop()
  if p in seen:continue
  seen.add(p)
  for module in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)',p.read_text(encoding='utf-8'),re.M):
   rel=Path(*module.split('.')).with_suffix('.agda')
   match=next((r/rel for r in roots if (r/rel).exists()),None)
   if match is None:unresolved.add(module)
   else:todo.append(match)
 seen.update(root.glob('*.py'))
 return {label(p):sha(p) for p in sorted(seen)},sorted(unresolved)
before,unresolved=inventory();start=time.monotonic()
report={'passed':False,'agda_version':subprocess.check_output(['agda','--version'],text=True).strip(),'python_version':sys.version,'source_sha256':before,'unresolved_toolchain_imports':unresolved,'stages':[],'scope':'All current observer modules plus six foundational bridge modules, with recursively resolved Agda imports and local Python checker sources. Not a binary/OS proof, geometric model, global operational-net audit, or physical interpretation.'}
def save():receipt.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
save()
command=['agda','--safe','--cubical','--guardedness','--ignore-interfaces','--transliterate','-Werror']
for p in roots:command+=['-i',str(p)]
try:
 for source in entries:
  print('CHECK',source.stem,flush=True);t=time.monotonic()
  run=subprocess.run(command+[str(source)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=240)
  log=results/('audit-'+source.stem+'.log');log.write_text(run.stdout+'\n'+run.stderr,encoding='utf-8')
  report['stages'].append({'module':source.stem,'exit_code':run.returncode,'command':command+[str(source)],'seconds':round(time.monotonic()-t,3),'log_sha256':sha(log)})
  save()
  if run.returncode:raise RuntimeError('failed: '+source.stem)
 after,remaining=inventory()
 if before!=after or unresolved!=remaining:raise RuntimeError('inventoried source changed during audit')
 if sorted((root/'agda').glob('*.agda'))!=entries[:len(entries)-len(bridges)]:raise RuntimeError('entry modules changed during audit')
 report.update(passed=True,source_unchanged=True,source_count=len(before),module_count=len(entries))
except Exception as error:
 report['error']=str(error)
 raise
finally:
 report['seconds']=round(time.monotonic()-start,3);save()
print(json.dumps({k:report[k] for k in ('passed','module_count','source_count','source_unchanged','seconds')},indent=2))
