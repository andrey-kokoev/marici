"""Geometric attachment domains induced by the already validated PN face ports."""
from itertools import combinations
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';V='research/voevodsky/'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
    path=V+'results/ramsey-native-PN-overlap-span-v1.json';d=json.loads((ROOT/path).read_text())
    for p,h in d['source_sha256'].items():assert sha(p)==h,'stale law domain '+p
    frames=d['witness']['frames'];ports=d['witness']['ports'];assert len(frames)==24 and len(ports)==48
    vertices=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1'];edges=list(combinations(vertices,2))
    charts=[]
    for frame in frames:
        c=frame['chart'];own=[p for p in ports if p['chart']==c];assert len(own)==2
        records=[]
        for e in edges:
            parents=[p for p in own if set(e)<=set(p['faceVertices'])]
            cc=sum(frame['roles'][v]=='C' for v in e)
            assert len(parents)==2-cc
            records.append({'edge':list(e),'roles':[frame['roles'][v] for v in e],
              'parentPorts':[{'chart':p['chart'],'face':p['face']} for p in parents],
              'parentMultiplicity':len(parents)})
        vrecords=[]
        for v in vertices:
            parents=[p for p in own if v in p['faceVertices']]
            assert len(parents)==(1 if frame['roles'][v]=='C' else 2)
            vrecords.append({'vertex':v,'role':frame['roles'][v],'parentFaces':[p['face'] for p in parents]})
        support={i for i,r in enumerate(records) if r['parentMultiplicity']}
        assert len(support)==5
        charts.append({'chart':c,'roles':frame['roles'],'edges':records,'vertices':vrecords,'supportedEdgeIndices':sorted(support)})
    included=lost=0;witness=None;role_same=0
    for a in charts:
        for b in charts:
            sa=set(a['supportedEdgeIndices']);sb=set(b['supportedEdgeIndices']);same=a['roles']==b['roles']
            role_same+=int(same)
            assert (sa<=sb)==same
            if sa<=sb:included+=1
            else:
                lost+=1;missing=sorted(sa-sb);assert len(missing)==1
                if witness is None:
                    i=missing[0];e=edges[i]
                    source_ports=[p for p in ports if p['chart']==a['chart'] and set(e)<=set(p['faceVertices'])]
                    absent=[]
                    for face in combinations(vertices,3):
                        if set(e)<=set(face):
                            count=sum(b['roles'][v]=='M' for v in face)
                            assert count!=2
                            absent.append({'geometricFace':list(face),'targetMCount':count,'requiredMCount':2})
                    assert len(absent)==2
                    witness={'sourceChart':a['chart'],'targetChart':b['chart'],'edge':list(e),
                      'sourceFullPorts':source_ports,'sourceRoles':a['roles'],'targetRoles':b['roles'],
                      'targetAbsentPermits':absent}
    assert included==role_same==96 and lost==480
    # The independently admitted union covers every edge and vertex.
    union=set().union(*(set(c['supportedEdgeIndices']) for c in charts));assert len(union)==6
    files=[path,V+'contracts/ramsey-edge-law-domain-attempt.v1.json',V+'checkers/check_ramsey_edge_law_domain.py']
    out={'schema':'marici.ramsey-edge-law-domain.verification.v1','status':'passed',
      'scope_id':'PN-face-induced-edge-and-vertex-law-domains-v1',
      'verification_level':'exhaustive exact finite attachment-domain audit of validated full ports; no new kernel replay',
      'chartCount':24,'chartPairCount':576,'charts':charts,
      'identityEdgeDomainInclusions':included,'identityEdgeDomainFailures':lost,
      'edgeDomainInclusionExactlySameRolePartition':True,'everyChartVertexSupportComplete':True,
      'eachChartSupportedEdges':5,'independentContextUnionEdges':6,'lostEdgeWitness':witness,
      'supportInclusionIsNativeWitness':False,'higherContextIncidenceRefuted':False,
      'scalarFieldConventionRequiredByThisTest':False,'parentDescentResolved':False,
      'source_sha256':{p:sha(p) for p in files}}
    (BASE/'results/ramsey-edge-law-domain-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['charts','lostEdgeWitness','source_sha256']},indent=2))
if __name__=='__main__':main()
