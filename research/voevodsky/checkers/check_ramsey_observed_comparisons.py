"""Fixed-observation gate, distinct from unguarded native package equality."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    prior=BASE/'results/ramsey-atomic-seed-path-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale atomic signature '+p
    owner=BASE/'agda';fixture=BASE/'fixtures/ramsey-observed-comparisons'
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,fixture,ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyObservedComparisons',owner,True),('RamseyObservedBadGuard',fixture,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[prior,Path(__file__),owner/'RamseyObservedComparisons.agda',owner/'RamseyAtomicSeedPaths.agda',
      BASE/'contracts/ramsey-observed-comparisons-attempt.v1.json',*fixture.glob('*.agda')]
    out={'schema':'marici.ramsey-observed-comparisons.verification.v1','status':'passed',
      'scope_id':'fixed-observation-preserving-native-atomic-comparison-gate-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'guardedIdentityInverseComposition':True,'guardedTaggedPackagePath':True,
      'visibleBooleanChangeImpossible':True,'constantObservationSwapAccepted':True,'hostileSwapGuardRejected':True,
      'owningNativeSignatureChanged':False,'rawPathClosedSeedAdmissionReplaced':False,
      'allNativeOperationsGuarded':False,'actualPacketReferenceObservationInstantiated':False,
      'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-observed-comparisons-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()
