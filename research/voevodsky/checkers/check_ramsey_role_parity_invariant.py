"""Finite local normal forms for a source-level all-origin role invariant."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    prior=BASE/'results/ramsey-origin-zero-source-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale local rule '+p
    folder=ROOT/'research/strominger/demos/particle-overlap-tetrahedron'
    files=[prior,Path(__file__),BASE/'checkers/check_ramsey_role_parity_invariant.mjs',
      BASE/'contracts/ramsey-role-parity-invariant-attempt.v1.json',BASE/'ramsey-role-parity-invariant-v1.md']+[folder/n for n in ['local-reference-rules.mjs','lattice-items.mjs','simplex-components.mjs','window-construction-model.mjs','phase-advance-model.mjs','phase-discipline-model.mjs']]
    before={p:sha(p) for p in files}
    run=subprocess.run(['node',str(BASE/'checkers/check_ramsey_role_parity_invariant.mjs')],cwd=ROOT,capture_output=True,text=True,timeout=600)
    (BASE/'results/ramsey-role-parity-invariant-run.log').write_text(run.stdout+'\n'+run.stderr,encoding='utf-8')
    assert run.returncode==0,run.stdout[-3000:]+'\n'+run.stderr[-10000:]
    runtime=BASE/'results/ramsey-role-parity-invariant-runtime-v1.json';raw=json.loads(runtime.read_text())
    assert raw['status']=='passed' and raw['geometricParityForms']==48 and raw['markings']==1152
    assert before=={p:sha(p) for p in files}
    files.append(runtime)
    out={'schema':'marici.ramsey-role-parity-invariant.verification.v1','status':'passed',
      'scope_id':'default-source-reference-role-parity-under-local-operations-v1',
      'verification_level':'exact finite geometric/parity normal forms with source-level translation covariance and phase-independence argument; not kernel-verified JavaScript semantics',
      **{k:raw[k] for k in ['geometricParityForms','markings','totals','ruleKindCoverage','translationControls','phaseControls','defaultSeedSatisfiesInvariant','complementarySeedViolations']},
      'candidateInvariant':'C iff (x0+x2) mod 2 = 1; M iff (x0+x2) mod 2 = 0',
      'allOriginConclusionUsesSourceLevelCoverageArgument':True,'finiteDepthSearchUsedAsProof':False,
      'javascriptSemanticsKernelVerified':False,'independentComplementaryInputsRefuted':False,
      'additionalRoleChangingOperatorsRefuted':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files}}
    (BASE/'results/ramsey-role-parity-invariant-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
