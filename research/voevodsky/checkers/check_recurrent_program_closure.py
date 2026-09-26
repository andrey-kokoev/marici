"""Fresh subprocess closure; requires assertions, reports categories separately."""
from pathlib import Path
import subprocess
import sys
import json
import hashlib

if not __debug__:
 raise RuntimeError('Verification requires Python assertions (no -O).')
base=Path(__file__).resolve().parent
suites={
 'public_boundary':['check_public_inputs.py','check_program_runtime.py','check_program_preflight.py','check_constructor_resources.py','check_runtime_admission.py'],
 'schedule_independence':['check_all_schedules.py','check_local_diamonds.py','check_concurrency_invariant.py'],
 'interfaces':['check_combined_signature.py','check_strict_return_interfaces.py'],
 'replacement_reference':['check_pure_replacement.py','check_certified_replacement.py','check_rule_templates.py','check_full_certificates.py','check_whole_run_certificates.py','check_initial_recognizer.py','check_offline_replay.py','check_replay_semantics.py','check_semantic_replay.py','check_bounded_replay.py'],
 'observations':['check_program_observation.py','check_scanner_observation.py'],
 'resource_preparation':['check_acknowledged_unary_copy.py','check_triple_cursor.py'],
 'semantics_and_composition':['check_strict_set_program.py','check_conditional_set_program.py','check_fuel_scanner.py','check_scanner_successor.py','check_scanning_set_program.py'],
}
from evidence_freshness import sources,hashes
source_before=sources(base.parent)
results=[]
for category,names in suites.items():
 for name in names:
  run=subprocess.run([sys.executable,'-E',str(base/name)],cwd=base,text=True,capture_output=True,timeout=180)
  results.append({'category':category,'checker':name,'passed':run.returncode==0,'stdout':run.stdout.strip(),'stderr':run.stderr.strip()})
report={'passed':all(r['passed'] for r in results),'suites':results,'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(base.glob('*.py'))},'scope':'Fresh subprocess execution of named bounded audits/regressions. Source hashes identify local Python files, not formal proof or full dependency/environment provenance.'}
from offline_replay import contract,digest
source_after=sources(base.parent)
report.update(source_snapshot=source_after,sources_stable=source_before==source_after,replay_contract_digest=digest(contract()),dependency_artifacts=hashes([base.parent/'results/combined-signature.json',base.parent/'results/replay-example.json'],base.parent))
report['passed']=report['passed'] and report['sources_stable']
path=base.parent/'results/recurrent-program-closure.json';path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':report['passed'],'suites':len(results),'failures':[r['checker'] for r in results if not r['passed']],'report':str(path)}))
sys.exit(0 if report['passed'] else 1)
