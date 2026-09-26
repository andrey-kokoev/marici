"""Fresh whole-prototype regression and source/import inventory audit."""
from pathlib import Path
import ast,hashlib,json,platform,re,subprocess,sys,time
root=Path(__file__).resolve().parent;repo=root.parents[2];legacy=root.parent/'checkers'
cubical=Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9');results=root/'results'
start=time.monotonic();out=results/'trust-surface-audit.json'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def label(p):
 try:return str(p.relative_to(repo))
 except ValueError:return str(p)
def inventory():
 files=set(root.glob('*.py'))|set((root/'agda').glob('*.agda'));pending=list(files);external=set()
 while pending:
  p=pending.pop()
  if p.suffix=='.py':
   tree=ast.parse(p.read_text(encoding='utf-8'))
   modules=[]
   for node in ast.walk(tree):
    if isinstance(node,ast.Import):modules.extend(a.name.split('.')[0] for a in node.names)
    elif isinstance(node,ast.ImportFrom) and node.module:modules.append(node.module.split('.')[0])
   for module in modules:
    candidates=[p.parent/(module+'.py'),root/(module+'.py'),legacy/(module+'.py')]
    candidate=next((x for x in candidates if x.exists()),None)
    if candidate is not None and candidate not in files:files.add(candidate);pending.append(candidate)
  else:
   for module in re.findall(r'^(?:open\s+)?import\s+([A-Za-z0-9_.]+)',p.read_text(encoding='utf-8'),re.M):
    relative=Path(*module.split('.')).with_suffix('.agda')
    candidate=next((base/relative for base in (root/'agda',repo/'research/nima/agda',cubical) if (base/relative).exists()),None)
    if candidate is None:external.add(module)
    elif candidate not in files:files.add(candidate);pending.append(candidate)
 return {label(p):digest(p) for p in sorted(files)},sorted(external)
before,externals=inventory()
report={'passed':False,'python_version':platform.python_version(),'source_before':before,'unresolved_agda_imports':externals,'stages':[],'scope':'Fresh local source/import closure and regressions, not a proof of the Python interpreter/compiler or authenticity of external grants.'}
def save():out.write_text(json.dumps(report,indent=2)+'\n')
save()
stages=[('check_reference.py','reference.json'),('check_admission.py','admission.json'),('check_local_net.py','local-net.json'),('check_tree_soundness.py','tree-soundness.json'),('check_pending.py','pending.json'),('check_open_net.py','open-net.json'),('check_open_diamonds.py','open-diamonds.json'),('check_ticket_forks.py','ticket-forks.json'),('check_resource_signature.py','resource-signature.json'),('check_legacy_join_fixture.py','legacy-join-fixture.json'),('check_online_legacy_observation.py','online-legacy-observation.json'),('check_port_refinement.py','port-refinement.json'),('check_port_certificates.py','port-certificates.json'),('check_indexed_port_certificates.py','indexed-port-certificates.json'),('check_domain_admission_export.py','domain-admission.json'),('check_agda_substitution.py','agda-substitution.json'),('check_agda_local_simulation.py','agda-local-simulation.json'),('check_agda_termination.py','agda-termination.json'),('check_agda_footprints.py','agda-footprints.json')]
if {p.name for p in root.glob('check_*.py')}!={s for s,_ in stages}|{Path(__file__).name}:raise RuntimeError('uncovered checker source')
def run_stage(name,command,artifact=None):
 print('RUN',name,flush=True);t=time.monotonic();run=subprocess.run(command,capture_output=True,text=True,timeout=240)
 log=results/('audit-'+name+'.log');log.write_text(run.stdout+'\n'+run.stderr)
 if run.returncode!=0:raise RuntimeError((name,'failed',str(log)))
 if artifact and not json.loads((results/artifact).read_text())['passed']:raise RuntimeError((name,'report failed'))
 report['stages'].append({'name':name,'seconds':round(time.monotonic()-t,3),'artifact':artifact,'log_sha256':digest(log)});save()
for script,artifact in stages:run_stage(script,[sys.executable,str(root/script)],artifact)
run_stage('admission-optimized',[sys.executable,'-O',str(root/'check_admission.py')],'admission-optimized.json')
# Check EVERY live prototype Agda module, including generated examples and
# the one-resource module that has no dedicated Python runner.
for source in sorted((root/'agda').glob('*.agda')):
 run_stage(source.stem,['agda','--ignore-interfaces','--transliterate','-i',str(root/'agda'),'-i',str(repo/'research/nima/agda'),'-i',str(cubical),str(source)])
after,external_after=inventory()
if before!=after or externals!=external_after:raise RuntimeError('source changed during audit (including generated source)')
report['source_inventory_count']=len(after);report['all_source_bytes_unchanged']=True
report['runtime_modules']=['reference.py','admission.py','local_net.py','open_net.py','pending.py']
report['runtime_nonblank_lines']={name:sum(bool(line.strip()) for line in (root/name).read_text().splitlines()) for name in report['runtime_modules']}
report['formal_scope']=['reference substitution laws','abstract contextual simulation and pure compression','abstract all-schedule termination and exact rewrite count','generic pointwise resource conservation','finite exported abstract trace certificates and domain interpretations']
report['unproved_boundaries']=['Python wire-to-term decoder/exporter correctness','general concrete port refinement','authenticated seed grants and world interpretation','cross-realm single-use commitment','higher dependent package/index transport','performance superiority or drop-in legacy timing equivalence']
report['result_sha256']={p.name:digest(p) for p in sorted(results.glob('*.json')) if p!=out}
report['passed']=True;report['seconds']=round(time.monotonic()-start,3);save()
print(json.dumps({k:report[k] for k in ('passed','seconds','source_inventory_count','all_source_bytes_unchanged','runtime_nonblank_lines')},indent=2))
