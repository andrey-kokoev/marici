"""Generic kernel origin invariant plus actual exhausted zero-increment source closure."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    prior=BASE/'results/ramsey-native-PN-overlap-span-v1.json';d=json.loads(prior.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale local signature '+p
    run=subprocess.run(['node',str(BASE/'checkers/check_ramsey_origin_zero_source.mjs')],cwd=ROOT,capture_output=True,text=True,timeout=180)
    assert run.returncode==0,run.stdout+'\n'+run.stderr
    runtime=BASE/'results/ramsey-origin-zero-source-runtime-v1.json';raw=json.loads(runtime.read_text())
    assert raw['exhaustedWithoutDepthCutoff'] and not raw['canonicalComplementInClosure'] and not raw['resourceGuardTriggered']
    assert raw['targetIsValidSeparateSeed'] and len(raw['controls'])==2
    owner=BASE/'agda';fix=BASE/'fixtures/ramsey-origin-zero-source';tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,fix,tools/'cubical-0.9']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyOriginZeroPaths',owner,True),('RamseyOriginZeroExamples',fix,True),('RamseyOriginZeroBadReference',fix,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[prior,runtime,Path(__file__),BASE/'checkers/check_ramsey_origin_zero_source.mjs',owner/'RamseyOriginZeroPaths.agda',
      BASE/'contracts/ramsey-origin-zero-source-attempt.v1.json',BASE/'ramsey-native-word-trace.mjs',
      ROOT/'research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs',*fix.glob('*.agda')]
    out={'schema':'marici.ramsey-origin-zero-source.verification.v1','status':'passed',
      'scope_id':'canonical-origin-zero-complement-under-declared-local-rules-v1',
      'verification_level':'fresh safe Cubical abstract finite-walk invariant plus exact JavaScript source closure/signature binding; not verified JavaScript semantics',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'zeroEndingWalkPreservesReferences':True,'zeroIncrementClosureExhausted':True,
      'zeroIncrementReachablePacketCount':len(raw['zeroIncrementReachablePackets']),
      'zeroIncrementOperationCount':len(raw['zeroIncrementOperations']),
      'positiveIncrementOperationsExcludedByOriginInvariant':len(raw['excludedPositiveIncrementOperations']),
      'canonicalComplementOriginZeroReachable':False,'complementValidAsSeparateSeed':True,
      'higherOriginComplementReachabilityDecided':False,'extraOperationsRefuted':False,
      'javascriptSemanticsKernelVerified':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-origin-zero-source-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()
