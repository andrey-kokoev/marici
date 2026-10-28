"""One coherent output from two actual off-edge legs; trace sufficiency only."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,adj,serialize
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def restore(m):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in m]
def main():
    paths={'prior':V+'results/ramsey-minimal-edge-context-v1.json',
      'locality':V+'results/ramsey-prepared-edge-locality-v1.json',
      'five':S+'full-five-channel-candidate/verification.json'}
    d={k:load(p) for k,p in paths.items()}
    for p,h in d['prior']['source_sha256'].items():assert sha(p)==h,'stale repair input '+p
    for p,h in d['locality']['source_sha256'].items():assert sha(p)==h,'stale local input '+p
    prior=d['prior'];repair=prior['selectedRepair'];assert repair['allSlots']==[0,1,6,7,12,24]
    bn=restore(d['five']['neutronFiveEmbedding']);f=restore(d['locality']['requiredPreparedReadout'])
    six=restore(repair['traceReadout']);weights=six[0][4:]
    assert len(weights)==2 and all(x!=R() for x in weights)
    assert six[1][4:]==[-x for x in weights]
    # Actual field observation has four local outputs and one coherent remote sum.
    observe=[]
    for slot in repair['allSlots'][:4]:observe.append([R(int(j==slot)) for j in range(36)])
    mixed=[R() for _ in range(36)];mixed[12],mixed[24]=weights;observe.append(mixed)
    output=[six[0][:4]+[R(1)],six[1][:4]+[R(-1)]]
    prepared=mm(observe,bn)
    assert mm(output,prepared)==f
    # Local rows already have rank3; the fifth row sees a previously invisible
    # coefficient, so prepared rank is4. Give its nonzero one-dimensional kernel.
    alpha,beta=f[0][2],f[0][3]
    assert alpha!=R() and beta!=R()
    kernel=[[R()],[R()],[-beta],[alpha],[R()]]
    assert mm(prepared,kernel)==[[R()] for _ in range(5)]
    assert mm(f,kernel)==[[R()],[R()]]
    assert any(row[0]!=R() for row in mm(bn,kernel))
    assert mm(adj(kernel),kernel)[0][0]!=R()
    # Explicit controls on both remote legs and their relative phase.
    controls=[]
    for name,slot,factor in [('drop leg12',12,0),('drop leg24',24,0),('flip leg24 phase',24,-1)]:
        hostile=[row[:] for row in observe];hostile[4][slot]=hostile[4][slot]*factor
        assert mm(output,mm(hostile,bn))!=f;controls.append(name)
    # e2 and -e2 have identical local data and identical per-leg powers,
    # but nonzero opposite complex-linear trace outputs.
    plus=[[R(int(i==2))] for i in range(5)];minus=[[-x for x in row] for row in plus]
    yplus=mm(bn,plus);yminus=mm(bn,minus)
    assert all(yplus[i]==yminus[i]==[R()] for i in repair['allSlots'][:4])
    for i in [12,24]:assert yplus[i][0].conj()*yplus[i][0]==yminus[i][0].conj()*yminus[i][0]
    assert mm(f,plus)!=mm(f,minus)
    controls.append('power-only remote readout loses complex-linear sign')
    # Verify the new channel is not itself an edge-local row.
    assert [i for i,x in enumerate(mixed) if x!=R()]==[12,24]
    assert prepared[4][2]!=R() and prepared[4][3]!=R()
    files=list(paths.values())+[V+'contracts/ramsey-trace-only-context-channel-attempt.v1.json',
       V+'checkers/check_ramsey_trace_only_context_channel.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-trace-only-context-channel.verification.v1','status':'passed',
      'scope_id':'one-output-two-leg-prepared-edge-trace-channel-v1',
      'localOutputCoordinates':[0,1,6,7],'remoteInputCoordinates':[12,24],
      'remoteInputGeometry':repair['additionalCoordinates'],'addedComplexScalarOutputs':1,
      'totalComplexScalarOutputs':5,'preparedObservationRank':4,'unrecoveredPreparedDimension':1,
      'mixedWeights':[x.record() for x in weights],'fullFieldObservation':serialize(observe),
      'traceDecoder':serialize(output),'preparedObservation':serialize(prepared),
      'lostPreparedVector':serialize(kernel),'traceFactorizationChecked':True,
      'minimalAddedScalarOutputsForTraces':1,'controls':controls,
      'fullPreparedRecovery':False,'edgeLocalInstrument':False,'physicalCoherentMixerConstructed':False,
      'parentDescentResolved':False,'source_sha256':{p:sha(p) for p in files}}
    (ROOT/(V+'results/ramsey-trace-only-context-channel-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['mixedWeights','fullFieldObservation','traceDecoder','preparedObservation','lostPreparedVector','source_sha256']},indent=2))
if __name__=='__main__':main()
