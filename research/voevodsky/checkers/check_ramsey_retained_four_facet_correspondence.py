"""Fresh closure for the exact retained-correspondence scoped result."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
LEVEL='fresh safe Cubical source-bound native retained four-facet edge/vertex correspondence cells; runtime port binding, not complete-domain equivalence or parent descent'
SCOPE='independently-admitted-retained-four-facet-native-correspondence-v1'
NODE='native-retained-four-facet-correspondence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    contract=BASE/'contracts/ramsey-retained-four-facet-correspondence-attempt.v1.json';claim=json.loads(contract.read_text())
    paths=[BASE/'results'/name for name in ['ramsey-native-edge-attachments-v1.json','ramsey-four-facet-vertex-cells-v1.json','ramsey-attachment-relations-v1.json']]
    pins={};data=[]
    for path in paths:
        d=json.loads(path.read_text());data.append(d)
        for p,h in d['source_sha256'].items():
            assert sha(ROOT/p)==h,'stale construction '+p
            assert p not in pins or pins[p]==h
            pins[p]=h
        pins[path.relative_to(ROOT).as_posix()]=sha(path)
    edge,cover,relations=data
    assert edge['sourceBoundEdgeAttachments']==144 and cover['facetCharts']==[0,7,0,7]
    counts={k:cover[k] for k in ['directedNativeEdgeSelections','nativeVertexTripleCompositions','differentEdgeRestrictionCells','fullMiddleDerivationSeams']}
    assert list(counts.values())==[12,24,72,24]
    assert relations['crossChartRoundTripIdentityFailures']==4 and not relations['completeCorrespondencesAreInvertible']
    owner=BASE/'agda';fixture=BASE/'fixtures/ramsey-four-facet-vertex-cells'
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe'
    dirs=[owner,ROOT/'research/nima/agda',fixture,BASE/'fixtures/ramsey-native-edge-attachments',BASE/'fixtures/ramsey-requested-port',
      tools/'cubical-0.9',ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda);args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,folder,ok in [('RamseyNativeEdgeAttachments',owner,True),('RamseyFourFacetVertexCells',fixture,True),('RamseyFourFacetBadMiddle',fixture,False)]:
        run=subprocess.run(args+[str(folder/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-retained-correspondence-'+name+'.log')).write_text(text,encoding='utf-8');codes[name]=run.returncode
        if ok:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    for path in [contract,Path(__file__),BASE/'ramsey-retained-four-facet-correspondence-v1.md']:
        pins[path.relative_to(ROOT).as_posix()]=sha(path)
    out={'schema':'marici.ramsey-retained-four-facet-correspondence.verification.v1','status':'passed','outcome':'++',
      'scope_id':SCOPE,'claim_sha256':hashlib.sha256(claim['statement'].encode()).hexdigest(),'verification_level':LEVEL,
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,'moduleExitCodes':codes,
      **counts,'independentFullPortPolicy':True,'differentMiddleParentErasureRejected':True,
      'completeDomainEquivalence':False,'physicalRoleMotion':False,'scalarFieldGluing':False,'wholeSpaceAdmission':False,
      'parentDescentResolved':False,'rootResolved':False,'source_sha256':pins,'formalSourceInventory':before}
    (BASE/'results/ramsey-retained-four-facet-correspondence-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()
