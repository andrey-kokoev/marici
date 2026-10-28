"""Native generic retention theorem plus exact source-bound runtime instances."""
from pathlib import Path
from fractions import Fraction as F
import subprocess,sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,identity,serialize
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def restore(m):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in m]
def main():
    paths=[V+'results/ramsey-trace-channel-transport-v1.json',V+'results/ramsey-trace-only-context-channel-v1.json',S+'full-five-channel-candidate/verification.json']
    transport,channel,five=map(load,paths)
    for receipt in [transport,channel]:
        for p,h in receipt['source_sha256'].items():assert sha(ROOT/p)==h,'stale observation '+p
    bn=restore(five['neutronFiveEmbedding']);o=restore(channel['fullFieldObservation'])
    observers=[restore(m) for m in transport['coRotatingObservations']]
    rotation=[[R(int(i==(j+12)%36)) for j in range(36)] for i in range(36)]
    powers=[identity(36),rotation,mm(rotation,rotation)]
    kernel=restore(channel['lostPreparedVector'])
    roots=[[[R()] for _ in range(5)]]+[[[R(int(i==j))] for i in range(5)] for j in range(5)]+[kernel]
    histories=[[0],[0,1],[0,1,2],[0,1,2,0]];records=[]
    for rid,a in enumerate(roots):
        rootfield=mm(bn,a);views=[]
        for history in histories:
            t=history[-1];state=mm(powers[t],rootfield);value=mm(observers[t],state)
            assert value==mm(o,rootfield)
            record={'rootId':rid,'rootCoefficients':serialize(a),'fullRootField':serialize(rootfield),
               'history':history,'frame':t,'fullFramedField':serialize(state),
               'observationSupport':transport['observationSupports'][t],
               'observationValue':serialize(value),'sourceContextPins':paths}
            views.append(record);records.append(record)
        assert views[0]['observationValue']==views[3]['observationValue']
        assert views[0]['fullFramedField']==views[3]['fullFramedField'] and views[0]!=views[3]
    invisible=mm(bn,kernel)
    assert mm(o,invisible)==[[R()] for _ in range(5)]
    assert any(row[0]!=R() for row in mm(o,mm(rotation,invisible)))
    owner=BASE/'agda';fixture=BASE/'fixtures/ramsey-retained-observation'
    tools=Path.home()/'tools/cubical-agda';agda=tools/'agda-2.8.0/agda.exe';library=tools/'cubical-0.9'
    dirs=[owner,ROOT/'research/nima/agda',fixture,library,
          ROOT/'research/nima/adapters/native-application',ROOT/'research/nima/adapters/application-extension']
    def inventory():return {str(p):sha(p) for folder in dirs for p in folder.rglob('*.agda')}
    before=inventory();compiler=sha(agda)
    args=[str(agda),'--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
    for folder in dirs:args+=['-i',str(folder)]
    codes={}
    for name,directory,positive in [('RamseyNativeRetainedObservation',owner,True),
      ('RamseyRetainedObservationExamples',fixture,True),('RamseyRetainedObservationBadReadout',fixture,False)]:
        run=subprocess.run(args+[str(directory/(name+'.agda'))],cwd=ROOT,capture_output=True,text=True,timeout=600)
        text=run.stdout+'\n'+run.stderr;(BASE/('results/agda-'+name+'.log')).write_text(text,encoding='utf-8')
        codes[name]=run.returncode
        if positive:assert run.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-6000:]
        else:assert run.returncode!=0 and name+'.agda' in text and ('!=' in text or 'not equal' in text),text[-6000:]
    assert before==inventory() and compiler==sha(agda)
    files=[ROOT/p for p in paths]+[Path(__file__),BASE/'contracts/ramsey-retained-observation-attempt.v1.json',
      owner/'RamseyNativeRetainedObservation.agda',*fixture.glob('*.agda')]
    out={'schema':'marici.ramsey-retained-observation.verification.v1','status':'passed',
      'scope_id':'native-full-parent-frame-history-observation-v1',
      'freshSafeCubical':True,'ignoreInterfaces':True,'inputsStable':True,'compiler_sha256':compiler,
      'moduleExitCodes':codes,'nativeFullRootRetentionProved':True,'typedDerivedObservationIndex':True,
      'historyRetentionProved':True,'genericCompressedUpdateObstructionProved':True,
      'fabricatedObservationRejected':True,'runtimeRootCases':7,'runtimeRetainedPackages':28,
      'runtimeFrameRecurrencePreservesHistory':True,'runtimeFixedFutureSeparatesLostDirection':True,
      'sourceMatrixInterpretationInKernel':False,'nativeMatrixEquivalenceProved':False,
      'physicalAcquisitionAuthority':False,'parentDescentResolved':False,
      'runtimeInstances':records,'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files},
      'formalSourceInventory':before}
    (BASE/'results/ramsey-retained-observation-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['runtimeInstances','source_sha256','formalSourceInventory']},indent=2))
if __name__=='__main__':main()
