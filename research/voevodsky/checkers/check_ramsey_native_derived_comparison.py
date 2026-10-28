"""Fresh native comparison and composition proofs, not matrix semantics."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    # Mutable progress receipt is checked before extending its formal boundary.
    previous=BASE/'results/ramsey-retained-observation-v1.json'
    d=json.loads(previous.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale retained observation '+p
    owner=BASE/'agda';fixture=BASE/'fixtures/ramsey-native-derived-comparison'
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe';library=tools/'cubical-0.9'
    dirs=[owner,ROOT/'research/nima/agda',fixture,library,
          ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda)
    args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,directory,positive in [('RamseyNativeDerivedComparison',owner,True),
      ('RamseyDerivedComparisonExamples',fixture,True),('RamseyDerivedComparisonBadRoot',fixture,False)]:
        run=subprocess.run(args+[str(directory/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8')
        codes[name]=run.returncode
        if positive:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[previous,Path(__file__),BASE/'contracts/ramsey-native-derived-comparison-attempt.v1.json',
      owner/'RamseyNativeDerivedComparison.agda',*fixture.glob('*.agda')]
    out={'schema':'marici.ramsey-native-derived-comparison.verification.v1','status':'passed',
      'scope_id':'native-derived-presentation-comparison-over-retained-root-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,
      'moduleExitCodes':codes,'explicitDerivedFiberEquivalence':True,'nativeCompareConstructor':True,
      'nativeComposeConstructor':True,'parentValuePreserved':True,'comparisonActionCocycle':True,
      'bothCompositionPremisesRetained':True,'falseRootChangeRejected':True,
      'matrixFieldEquivalenceInterpreted':False,'rolePermitTransportBetweenDistinctRoots':False,
      'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-native-derived-comparison-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()
