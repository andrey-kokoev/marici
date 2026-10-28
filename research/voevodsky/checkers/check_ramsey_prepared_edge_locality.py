"""Exact prepared-domain kernel witness and explicitly nonlocal repair."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize,rational
V='research/voevodsky/';S='research/strominger/results/'
def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def restore(m):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in m]
def sharp(a,metric):return [[x*metric[j] for j,x in enumerate(row)] for row in adj(a)]
def main():
    paths={'edge':V+'results/ramsey-geometric-edge-readout-v1.json',
      'five':S+'full-five-channel-candidate/verification.json',
      'reader':S+'neutron-reader-field-interface/verification.json',
      'n':S+'common-three-carrier-protocol/neutron.json',
      'native':V+'results/belt_three_by_twelve_store.json',
      'ambient':V+'results/coupled_six_piece_belt_store.json'}
    d={k:load(p) for k,p in paths.items()}
    for p,h in d['edge']['source_sha256'].items():assert sha(p)==h,'stale edge input '+p
    for p,h in d['five']['sourceHashes'].items():assert sha(p)==h,'stale five input '+p
    assert d['native']['source_root']==d['ambient']['root']
    bn=restore(d['five']['neutronFiveEmbedding']);bp=restore(d['five']['protonFiveEmbedding'])
    m=list(map(F,d['n']['source']['metric']))
    hp=restore(d['edge']['readout']);indices=[i for i,x in enumerate(d['edge']['descriptors']) if x['edge']=='CD'];assert len(indices)==2
    pi=[3,1,2,0,4];pimat=[[R(int(j==pi[i])) for j in range(5)] for i in range(5)]
    desired=mm(mm([hp[i] for i in indices],bp),adj(pimat))
    slots_by_sector=[];edges=[]
    for chart in d['reader']['charts']:
        sector=chart['sector'];patches=chart['readerPatches']
        positions=[i for i,t in enumerate(patches) if set(t[1:])=={'u','v'}]
        assert len(positions)==2
        slots=[12*sector+2*i+axis for i in positions for axis in range(2)]
        inverse={value:key for key,value in chart['vertexMap'].items()}
        for i in positions:
            triangle=d['native']['coordinates'][12*sector+2*i]['triangle']
            ordered=d['ambient']['record']['triangles'][triangle]
            assert set(ordered[1:])=={inverse['u'],inverse['v']}
        slots_by_sector.append(slots);edges.append(sorted([inverse['u'],inverse['v']]))
    assert slots_by_sector[0]==[0,1,6,7] and len({tuple(e) for e in edges})==3
    local=[bn[i] for i in slots_by_sector[0]];local_metric=[m[i] for i in slots_by_sector[0]]
    gram=mm(sharp(local,local_metric),local)
    assert all(gram[i][j]==R() for i in range(5) for j in range(5) if i!=j)
    rank=sum(gram[i][i]!=R() for i in range(5));assert rank==3
    lost=[]
    for j in range(5):
        if all(row[j]==R() for row in local):
            values=[row[j] for row in desired]
            if any(x!=R() for x in values):
                state=[[row[j]] for row in bn]
                assert mm(sharp(state,m),state)==[[R(1)]]
                lost.append({'coefficientBasis':j,'localReadout':[{} for _ in local],
                    'requiredReadout':[x.record() for x in values],'fullPreparedNorm':'1'})
    assert lost, 'no basis kernel witness: a general factorization solver is required'
    # Explicit repair: both uv patches in each of THREE different sector edges.
    expanded_slots=sum(slots_by_sector,[]);expanded=[bn[i] for i in expanded_slots];em=[m[i] for i in expanded_slots]
    g=mm(sharp(expanded,em),expanded)
    assert all(g[i][j]==R() for i in range(5) for j in range(5) if i!=j)
    assert all(rational(g[i][i])>0 for i in range(5))
    left=sharp(expanded,em)
    decoder=[[x*(1/rational(g[i][i])) for x in row] for i,row in enumerate(left)]
    assert mm(decoder,expanded)==identity(5)
    enlarged_readout=mm(desired,decoder)
    assert mm(enlarged_readout,expanded)==desired
    inputs=list(paths.values())+[V+'contracts/ramsey-prepared-edge-locality-attempt.v1.json',
      V+'checkers/check_ramsey_prepared_edge_locality.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-prepared-edge-locality.verification.v1','status':'local-prepared-factorization-obstructed-with-enlarged-support-repair',
      'scope_id':'five-prepared-coefficients-shared-uv-edge-locality-v1',
      'localIntrinsicSlots':slots_by_sector[0],'localGeometricEdge':edges[0],
      'localPreparedRank':rank,'localPreparedGram':serialize(gram),'lostPreparedDirections':lost,
      'requiredPreparedReadout':serialize(desired),'localFactorizationExists':False,
      'expandedSlots':expanded_slots,'expandedDistinctGeometricEdges':edges,
      'expandedPreparedRank':5,'expandedDecoder':serialize(decoder),'expandedReadout':serialize(enlarged_readout),
      'expandedFactorizationChecked':True,'expandedInstrumentIsOneGeometricEdge':False,
      'sourceSelectedPhysicalDetector':False,'parentDescentResolved':False,
      'source_sha256':{p:sha(p) for p in inputs}}
    (ROOT/(V+'results/ramsey-prepared-edge-locality-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','requiredPreparedReadout','expandedDecoder','expandedReadout']},indent=2))
if __name__=='__main__':main()
