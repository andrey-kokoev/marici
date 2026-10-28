"""Complete two-coordinate repair census on the fixed prepared domain."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize,rational
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def restore(m):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in m]
def sharp(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def inv(x):return x.conj()*(1/rational(x.conj()*x))

def main():
    paths={'prior':V+'results/ramsey-prepared-edge-locality-v1.json',
      'five':S+'full-five-channel-candidate/verification.json',
      'n':S+'common-three-carrier-protocol/neutron.json',
      'native':V+'results/belt_three_by_twelve_store.json',
      'ambient':V+'results/coupled_six_piece_belt_store.json'}
    d={k:load(p) for k,p in paths.items()}
    for p,h in d['prior']['source_sha256'].items():assert sha(p)==h,'stale locality input '+p
    bn=restore(d['five']['neutronFiveEmbedding']);m=list(map(F,d['n']['source']['metric']))
    local=d['prior']['localIntrinsicSlots'];assert local==[0,1,6,7]
    a=[bn[i] for i in local];g=mm(sharp(a,[m[i] for i in local]),a)
    known=[0,1,4];missing=[2,3]
    assert all(g[i][j]==R() for i in range(5) for j in range(5) if i!=j)
    assert [i for i in range(5) if g[i][i]!=R()]==known
    pre=sharp(a,[m[i] for i in local])
    recover=[[x*(1/rational(g[i][i])) for x in pre[i]] if i in known else [R()]*4 for i in range(5)]
    assert mm(recover,a)==[[R(int(i==j and i in known)) for j in range(5)] for i in range(5)]
    outside=[i for i in range(36) if i not in local]
    # Rank on the two-dimensional local kernel decides each extension.
    singles={i:[bn[i][j] for j in missing] for i in outside}
    pairs=[];failed=[];first=None
    target=restore(d['prior']['requiredPreparedReadout'])
    for i,j in combinations(outside,2):
        x,y=singles[i],singles[j];det=x[0]*y[1]-x[1]*y[0]
        if det==R():failed.append([i,j]);continue
        # Source sector sparsity makes the admitted 2x2 kernel block diagonal
        # in sorted coordinates, avoiding an arbitrary field-valued solver.
        assert x[1]==R() and y[0]==R() and x[0]!=R() and y[1]!=R()
        decoder=[row+[R(),R()] for row in recover]
        for row,slot,observation,pivot in [(2,i,4,x[0]),(3,j,5,y[1])]:
            decoder[row]=[-sum((bn[slot][k]*recover[k][c] for k in known),R())*inv(pivot) for c in range(4)]+[R(),R()]
            decoder[row][observation]=inv(pivot)
        extended=[bn[k] for k in local+[i,j]]
        assert mm(decoder,extended)==identity(5)
        pairs.append([i,j])
        if first is None:
            readout=mm(target,decoder);assert mm(readout,extended)==target
            first={'additionalSlots':[i,j],'allSlots':local+[i,j],
                'decoder':serialize(decoder),'traceReadout':serialize(readout),
                'additionalCoordinates':[{'index':k,**d['native']['coordinates'][k],
                    'orderedTriangle':d['ambient']['record']['triangles'][d['native']['coordinates'][k]['triangle']]} for k in [i,j]]}
    assert len(pairs)+len(failed)==496 and len(pairs)==144
    assert pairs==[[i,j] for i in range(12,24) for j in range(24,36)]
    assert first['additionalSlots']==[12,24]
    # Determine trace-only demand on the local kernel independently.
    fkernel=[[row[j] for j in missing] for row in target]
    determinant=fkernel[0][0]*fkernel[1][1]-fkernel[0][1]*fkernel[1][0]
    rank=2 if determinant!=R() else (1 if any(x!=R() for row in fkernel for x in row) else 0)
    # Every existing single coordinate misses one kernel axis. Record whether
    # that already obstructs these particular trace readings.
    single_trace_possible=[]
    for i in outside:
        x=singles[i]
        if x==[R(),R()]:possible=rank==0
        elif x[0]!=R() and x[1]==R():possible=all(row[1]==R() for row in fkernel)
        elif x[0]==R() and x[1]!=R():possible=all(row[0]==R() for row in fkernel)
        else:raise AssertionError('unexpected mixed-sector scalar coordinate')
        if possible:single_trace_possible.append(i)
    files=list(paths.values())+[V+'contracts/ramsey-minimal-edge-context-attempt.v1.json',
        V+'checkers/check_ramsey_minimal_edge_context.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-minimal-edge-context.verification.v1','status':'passed',
      'scope_id':'minimal-off-edge-coordinate-repair-five-prepared-v1',
      'localSlots':local,'localPreparedRank':3,'candidateAdditionalCoordinates':32,
      'testedPairs':496,'successfulPairs':pairs,'rejectedPairs':failed,
      'exactDecoderChecks':len(pairs),'minimalAdditionalScalarsForFullPreparation':2,
      'minimalTotalScalarsWithFixedLocalSupport':6,'selectedRepair':first,
      'traceKernelRank':rank,'traceKernelDeterminant':determinant.record(),
      'singleSourceCoordinateTraceRepairs':single_trace_possible,
      'traceReadoutRestrictedToKernel':serialize(fkernel),
      'minimalityIsForFixedLocalSupport':True,'repairIsGeometricallyLocal':False,
      'fullFieldRecoveryProved':False,'physicalDetectorConstructed':False,'parentDescentResolved':False,
      'source_sha256':{p:sha(p) for p in files}}
    (ROOT/(V+'results/ramsey-minimal-edge-context-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['successfulPairs','rejectedPairs','selectedRepair','source_sha256','traceReadoutRestrictedToKernel','traceKernelDeterminant']},indent=2))
if __name__=='__main__':main()
