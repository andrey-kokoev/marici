"""Fixed observation is not a sector-rotation congruence; moving observation is covariant."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def restore(m):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in m]
def nonzero(m):return any(x!=R() for row in m for x in row)
def main():
    paths={'channel':V+'results/ramsey-trace-only-context-channel-v1.json',
      'prior':V+'results/ramsey-prepared-edge-locality-v1.json',
      'five':S+'full-five-channel-candidate/verification.json'}
    d={k:load(p) for k,p in paths.items()}
    for p,h in d['channel']['source_sha256'].items():assert sha(p)==h,'stale channel '+p
    for p,h in d['five']['sourceHashes'].items():assert sha(p)==h,'stale field '+p
    bn=restore(d['five']['neutronFiveEmbedding']);o=restore(d['channel']['fullFieldObservation'])
    decoder=restore(d['channel']['traceDecoder']);kernel=restore(d['channel']['lostPreparedVector'])
    target=restore(d['prior']['requiredPreparedReadout']);a=mm(o,bn)
    cycle=[0,3,1,2,4];c=[[R(int(j==cycle[i])) for j in range(5)] for i in range(5)]
    sector=[[R(int(i==(j+12)%36)) for j in range(36)] for i in range(36)]
    assert mm(sector,bn)==mm(bn,c)
    cp=[identity(5),c,mm(c,c)];rp=[identity(36),sector,mm(sector,sector)]
    assert mm(cp[2],c)==identity(5) and mm(rp[2],sector)==identity(36)
    assert mm(a,kernel)==[[R()] for _ in range(5)]
    future=mm(a,mm(c,kernel));trace_future=mm(target,mm(c,kernel))
    assert nonzero(future)
    # A fixed output map cannot take the equal inputs A k=A 0 to unequal A C k.
    # At t=1 and t=2 use freshly constructed co-rotating physical observation rows.
    observations=[mm(o,rp[(-t)%3]) for t in range(3)]
    for t in range(3):
        assert mm(mm(observations[t],bn),cp[t])==a
        assert mm(decoder,mm(observations[t],bn))==mm(target,cp[(-t)%3])
    squares=triangles=0
    for t in range(3):
        for u in range(3):
            comparison=rp[(u-t)%3]
            assert mm(observations[u],comparison)==observations[t];squares+=1
            for v in range(3):
                assert mm(rp[(v-u)%3],comparison)==rp[(v-t)%3];triangles+=1
    # The very first local sample after one cycle sees the residual direction.
    next_scalar=[mm(bn,c)[0]]
    separation=mm(next_scalar,kernel);assert nonzero(separation)
    # Since ker(A) is exactly span(k) from the prior rank4 certificate,
    # adjoining this row gives zero kernel on the five-dimensional preparation.
    assert d['channel']['preparedObservationRank']==4 and d['channel']['unrecoveredPreparedDimension']==1
    supports=[]
    for t,obs in enumerate(observations):
        supports.append({'context':t,'rowSupports':[[i for i,x in enumerate(row) if x!=R()] for row in obs]})
    assert supports[0]['rowSupports']!=supports[1]['rowSupports']
    files=list(paths.values())+[V+'contracts/ramsey-trace-channel-transport-attempt.v1.json',
       V+'checkers/check_ramsey_trace_channel_transport.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-trace-channel-transport.verification.v1','status':'passed',
      'scope_id':'trace-only-channel-under-source-sector-cycle-v1',
      'sourcePreparedIntertwinerChecked':True,'sectorRotationOrder':3,
      'fixedObservationKernelInvariant':False,'fixedObservationFutureFactorizationExists':False,
      'fixedCurrentKernel':serialize(kernel),'fixedObservationAfterOneCycle':serialize(future),
      'requiredTraceAfterOneCycle':serialize(trace_future),'requiredTraceWitnessBecomesVisible':nonzero(trace_future),
      'coRotatingContexts':3,'framePairSquares':squares,'frameCompositionTriangles':triangles,
      'observationSupports':supports,'coRotatingObservations':[serialize(x) for x in observations],
      'additionalFutureScalar':{'sourceCoordinate':0,'afterSectorCycles':1,'preparedRow':serialize(next_scalar),
          'kernelSeparation':serialize(separation)},
      'preparedRankWithAdditionalFutureScalar':5,
      'futureScalarInferredFromCurrentObservation':False,'contextsAreAutonomousTimeSteps':False,
      'sectorRotationIdentifiedWithPacketReader':False,'physicalInstrumentConstructed':False,
      'parentDescentResolved':False,'source_sha256':{p:sha(p) for p in files}}
    (ROOT/(V+'results/ramsey-trace-channel-transport-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['fixedCurrentKernel','fixedObservationAfterOneCycle','requiredTraceAfterOneCycle','coRotatingObservations','additionalFutureScalar','source_sha256']},indent=2))
if __name__=='__main__':main()
