"""Enforce warning-free transport computation separately from type acceptance."""
from pathlib import Path
import hashlib,json,re,subprocess
root=Path(__file__).resolve().parent;repo=root.parents[2]
roots=[root/'agda',repo/'research/voevodsky/resolution-net-v1/agda',repo/'research/nima/agda',Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')]
results=root/'results';results.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory():
 seen=set();todo=[root/'agda/ObserverOperationalCheckpoint.agda'];external=set()
 while todo:
  p=todo.pop()
  if p in seen:continue
  seen.add(p)
  for module in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)',p.read_text(encoding='utf-8'),re.M):
   rel=Path(*module.split('.')).with_suffix('.agda')
   match=next((r/rel for r in roots if (r/rel).exists()),None)
   if match is None:external.add(module)
   else:todo.append(match)
 seen.update(root.glob('*.py'))
 return {str(p):sha(p) for p in sorted(seen)},sorted(external)
before,external=inventory()
report={'passed':False,'source_sha256':before,'unresolved_toolchain_imports':external,'agda_version':subprocess.check_output(['agda','--version'],text=True).strip(),'checks':[]}
receipt=results/'transport-gate.json'
def save():receipt.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
save()
base=['agda','--safe','--cubical','--guardedness','--ignore-interfaces','--transliterate']
for path in roots:base+=['-i',str(path)]
for name,module,strict in [('local','ObserverTransportRegression',True),('whole-accepted','ObserverOperationalCheckpoint',False),('whole-strict','ObserverOperationalCheckpoint',True)]:
 command=base+(['-Werror'] if strict else [])+[str(root/'agda'/f'{module}.agda')]
 run=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=360)
 log=results/f'agda-transport-gate-{name}.log';text=run.stdout+'\n'+run.stderr;log.write_text(text,encoding='utf-8')
 report['checks'].append({'name':name,'command':command,'exit_code':run.returncode,'unsupported_indexed_match':'UnsupportedIndexedMatch' in text,'log_sha256':sha(log)})
 save()
after,remaining=inventory();stable=before==after and external==remaining
local,accepted,strict=report['checks']
report.update(source_unchanged=stable,local_repair_verified=stable and local['exit_code']==0 and not local['unsupported_indexed_match'],whole_typecheck_accepted=accepted['exit_code']==0,whole_warning_free=strict['exit_code']==0)
report['passed']=stable and all(c['exit_code']==0 for c in report['checks'])
report['scope']='Local internal-observer transport regression repaired; whole-programme warning-free gate is independent and must not be inferred from ordinary type acceptance.'
save();print(json.dumps({k:report[k] for k in ('passed','source_unchanged','local_repair_verified','whole_typecheck_accepted','whole_warning_free')},indent=2))
raise SystemExit(0 if report['passed'] else 1)
