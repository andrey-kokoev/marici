"""Explicit P/E comparison compiler; no raw equality or source authorization."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';FIX=BASE/'fixtures/ramsey-pe-constructor-comparison'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    prior=BASE/'results/ramsey-different-edge-transport-v1.json';data=json.loads(prior.read_text())
    for p,h in data['source_sha256'].items():assert sha(ROOT/p)==h,'stale frontier '+p
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[BASE/'agda',FIX,ROOT/'research/nima/agda',tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyPEConstructorComparison',BASE/'agda',True),('RamseyPEConstructorExamples',FIX,True),('RamseyPEConstructorBadSelection',FIX,False),('RamseyPEConstructorBadLeaf',FIX,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=900)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-7000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-7000:]
    assert before==inventory() and compiler==sha(agda)
    files=[prior,Path(__file__),BASE/'contracts/ramsey-pe-constructor-comparison-attempt.v1.json',BASE/'agda/RamseyPEConstructorComparison.agda',BASE/'agda/RamseyExternalPE.agda',ROOT/'research/nima/agda/NativeTableResolution.agda',ROOT/'research/nima/agda/NativeTableRules.agda',*FIX.glob('*.agda')]
    out={'schema':'marici.ramsey-pe-constructor-comparison.verification.v1','status':'passed','scope_id':'explicit-PE-constructor-comparison-and-native-premises-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      'genericConstructorComparisonCompiler':True,'actualCompiledNativeProofIndices':True,
      'allProductPremisesCompared':True,'allSelectionPremisesCompared':True,'unselectedPremisePositiveControl':True,
      'wrongSelectedIndexHostileRejected':True,'unauthorizedLeafRelationHostileRejected':True,
      'nativeComparisonIsOwnerLocalRelation':True,'actualFourFacetComparisonInstantiated':False,
      'rawPackageOrDerivationEqualityClaimed':False,'arbitraryNativeResolveTransportClaimed':False,
      'independentTargetInputsEliminated':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},'formalSourceInventory':before}
    (BASE/'results/ramsey-pe-constructor-comparison-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()
