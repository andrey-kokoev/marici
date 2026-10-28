"""Distinguish canonical-input factorization from uniform source-only transport."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    previous=BASE/'results/ramsey-source-bound-comparison-v1.json';receipt=json.loads(previous.read_text())
    for p,h in receipt['source_sha256'].items():assert sha(ROOT/p)==h,'stale fixed input '+p
    source=BASE/'fixtures/ramsey-source-bound-comparison/RamseySourceBoundComparison.agda'
    assert 'Valid a = a ≡ actual' in source.read_text(encoding='utf-8'),'admission predicate changed'
    owner=BASE/'agda';fix=BASE/'fixtures/ramsey-comparison-forgetting'
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe';library=tools/'cubical-0.9'
    dirs=[owner,ROOT/'research/nima/agda',fix,BASE/'fixtures/ramsey-source-bound-comparison',
      BASE/'fixtures/ramsey-native-incidence',library,ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,directory,positive in [('RamseyComparisonForgetting',owner,True),('RamseyComparisonForgettingExamples',fix,True),('RamseyComparisonForgettingBadUniform',fix,False)]:
        run=subprocess.run(args+[str(directory/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if positive:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[previous,source,Path(__file__),BASE/'contracts/ramsey-comparison-forgetting-attempt.v1.json',
      owner/'RamseyComparisonForgetting.agda',*fix.glob('*.agda')]
    out={'schema':'marici.ramsey-comparison-forgetting.verification.v1','status':'passed',
      'scope_id':'fixed-versus-independent-comparison-input-forgetting-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,
      'moduleExitCodes':codes,'actualFixedPolicySourceOnlyFactorExists':True,
      'fixedFactorUsesGloballySuppliedTarget':True,'independentProductCriterionBothDirections':True,
      'abstractDistinctCompletionNoFactor':True,'invalidUniformConstantFactorRejected':True,
      'actualDistinctRoleCompletionsExhibited':False,'sourceGeneratedNativeRoleTransportProved':False,
      'actualFixedPolicyNonDescentClaimed':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-comparison-forgetting-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()
