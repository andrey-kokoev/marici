"""Paired proton edge traces and exact support of their PN pullbacks."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize,decode_A
from check_twelve_triangle_positive_geometry import POINTS
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def restore(m):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in m]
def main():
    paths={'geometry':S+'tetrahedral-field-attachment/verification.json',
      'p':S+'common-three-carrier-protocol/proton.json','n':S+'common-three-carrier-protocol/neutron.json',
      'pn':S+'global-PN-transport/verification.json','grid':S+'baryon-tensor-grid/verification.json',
      'q':V+'results/ramsey-world-frame-action-v1.json'}
    d={k:load(p) for k,p in paths.items()}
    for key in ['geometry','pn']:
        for p,h in d[key]['sourceHashes'].items():assert sha(p)==h,'stale input '+p
    for p,h in d['q']['source_sha256'].items():assert sha(p)==h,'stale action '+p
    labels=d['p']['source']['coordinates'];patches={x['outerArrow']:x for x in d['geometry']['gridGeometry']}
    descriptors=[];h=[]
    for a,b in combinations('ABCD',2):
        direction=[POINTS[b][i]-POINTS[a][i] for i in range(3)]
        assert sum(x*x for x in direction)==8
        assert patches[a+b]['surfaceTriangle'][0]!=patches[b+a]['surfaceTriangle'][0]
        for arrow in [a+b,b+a]:
            row=[R() for _ in labels]
            for axis,x in zip('xyz',direction):row[labels.index(arrow+':'+axis)]=R(x)
            h.append(row);descriptors.append({'edge':a+b,'patch':arrow,'parentFace':patches[arrow]['surfaceTriangle'][0],
                                            'tangent':list(map(str,direction))})
    assert len(h)==12
    # Disjoint patch supports prove rank12. Six paired differences have disjoint
    # edge supports and squared row norm16, hence independent constraints.
    assert mm(h,adj(h))==[[R(8*int(i==j)) for j in range(12)] for i in range(12)]
    differences=[[x-y for x,y in zip(h[i],h[i+1])] for i in range(0,12,2)]
    assert mm(differences,adj(differences))==[[R(16*int(i==j)) for j in range(6)] for i in range(6)]
    rename=dict(zip('ABCD','BADC'));w=[[R() for _ in range(12)] for _ in range(12)]
    for old,desc in enumerate(descriptors):
        a,b=map(rename.get,desc['edge']);edge=''.join(sorted(a+b));arrow=''.join(rename[x] for x in desc['patch'])
        new=next(i for i,x in enumerate(descriptors) if x['edge']==edge and x['patch']==arrow)
        w[new][old]=R(1 if a<b else -1)
    q=restore(d['q']['protonAction'])
    assert mm(h,q)==mm(w,h) and mm(w,w)==identity(12)
    assert mm(adj(w),w)==identity(12)
    # A simple raw field disproves equality of the two adjacent occurrences.
    j=next(i for i,x in enumerate(differences[0]) if x!=R())
    witness=[[R(int(i==j))] for i in range(36)]
    traces=mm(h,witness);assert traces[0]!=traces[1]
    z=[[decode_A(x)] for x in d['grid']['carriers']['proton']['sourceReturnColumn']]
    return_differences=mm(differences,z)
    t=restore(d['pn']['matrix']);metric=list(map(F,d['n']['source']['metric']))
    tinv=[[t[i][j].conj()*metric[i] for i in range(36)] for j in range(36)]
    hn=mm(h,tinv)
    supports=[[j for j,x in enumerate(row) if x!=R()] for row in hn]
    nlabels=d['n']['source']['coordinates']
    triangle_supports=[sorted({int(nlabels[j].split(':')[0].split('-')[1]) for j in row}) for row in supports]
    # Exact support is reported, not presumed to be a geometric edge.
    inputs=list(paths.values())+[V+'contracts/ramsey-geometric-edge-readout-attempt.v1.json',
      V+'checkers/check_ramsey_geometric_edge_readout.py','research/strominger/checkers/exact_multiradical.py',
      'research/nima/checkers/check_twelve_triangle_positive_geometry.py']
    out={'schema':'marici.ramsey-geometric-edge-readout.verification.v1','status':'passed',
      'scope_id':'proton-two-occurrence-edge-tangent-readout-v1',
      'edgeCount':6,'retainedOccurrenceReadouts':12,'readoutRank':12,'strictEqualizerCodimension':6,
      'markingCovariance':True,'readout':serialize(h),'edgeAction':serialize(w),'descriptors':descriptors,
      'fixedOccurrenceCounterexample':{'inputCoordinate':labels[j],'first':traces[0][0].record(),'second':traces[1][0].record()},
      'sourceReturnOccurrenceDifferences':serialize(return_differences),
      'PNPulledReadout':serialize(hn),'PNPullbackCoordinateSupportCounts':list(map(len,supports)),
      'PNPullbackTriangleSupports':triangle_supports,
      'PNPullbackIdentity':'H_N T=H_P follows from imported metric-unitary T inverse; no fresh dense inverse proof claimed',
      'sourceSelectedPhysicalDetector':False,'geometricNeutronEdgeBindingProved':False,
      'nativeWGReadoutInterpretationProved':False,'parentDescentResolved':False,
      'source_sha256':{p:sha(p) for p in inputs}}
    (ROOT/(V+'results/ramsey-geometric-edge-readout-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['readout','edgeAction','PNPulledReadout','source_sha256','PNPullbackTriangleSupports']},indent=2))
if __name__=='__main__':main()
