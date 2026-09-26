"""Fresh headless check and source-bound receipt for positivity distinctions."""
from pathlib import Path
import hashlib,json,re,subprocess
root=Path(__file__).resolve().parent;repo=root.parents[2]
cubical=Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')
roots=[root/'agda',repo/'research/voevodsky/resolution-net-v1/agda',repo/'research/nima/agda',cubical]
source=root/'agda/ObserverPositivity.agda';results=root/'results';results.mkdir(exist_ok=True)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory():
 seen=set();todo=[source];unresolved=set()
 while todo:
  p=todo.pop()
  if p in seen:continue
  seen.add(p)
  for module in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)',p.read_text(encoding='utf-8'),re.M):
   rel=Path(*module.split('.')).with_suffix('.agda')
   match=next((r/rel for r in roots if (r/rel).exists()),None)
   if match is None:unresolved.add(module)
   else:todo.append(match)
 return {str(p):digest(p) for p in sorted(seen)},sorted(unresolved)
before,external=inventory();command=['agda','--ignore-interfaces','--transliterate']
for p in roots:command+=['-i',str(p)]
command.append(str(source));run=subprocess.run(command,capture_output=True,text=True,timeout=240)
log=results/'agda-observer-positivity.log';log.write_text(run.stdout+'\n'+run.stderr,encoding='utf-8')
after,external_after=inventory()
report={'passed':run.returncode==0 and before==after and external==external_after,'exit_code':run.returncode,'command':command,'agda_version':subprocess.check_output(['agda','--version'],text=True).strip(),'source_sha256':before,'unresolved_toolchain_imports':external,'source_unchanged':before==after,'checker_sha256':digest(Path(__file__)),'log_sha256':digest(log),'claims':['participation implies support','supported observation implies participation','nonempty support can have empty content','actual coherent participation need not yield distinguishable states','every double-cover fibre is merely inhabited','double cover has actual local participation but no global observation'],'scope':'Typed distinctions for observer positivity; nonempty support is not positive geometric measure; no physical or temporal interpretation proved.'}
(results/'positivity.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ('passed','exit_code','source_unchanged','claims')},indent=2))
if not report['passed']:raise SystemExit(1)
