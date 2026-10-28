"""Endpoint relations are not the untruncated native paths they forget."""
from pathlib import Path
from itertools import product
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def relation(a,b):return set(product(a,b))
def diagonal(a):return {(x,x) for x in a}
def compose(r,s):return {(a,c) for a,b in r for b2,c in s if b==b2}
def encode(r):return [list(x) for x in sorted(r)]
def main():
    paths=[BASE/'results/ramsey-edge-law-domain-v1.json',BASE/'results/ramsey-four-facet-vertex-cells-v1.json',
      BASE/'results/ramsey-attachment-fiber-equivalence-v1.json']
    law,cover,fibers=[json.loads(p.read_text()) for p in paths]
    for d in [law,cover,fibers]:
        for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale relation input '+p
    charts={x['chart']:x for x in law['charts']};assignment=cover['facetCharts'];assert assignment==[0,7,0,7]
    vertices=['1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1'];triangles=associations=selected_triangles=0
    roundtrips=[];self_records=[];sections={};retained_paths=[]
    for vi,v in enumerate(vertices):
        choices={c:next(x['parentFaces'] for x in charts[c]['vertices'] if x['vertex']==v) for c in [0,7]}
        for a,b in product([0,7],repeat=2):
            ab=relation(choices[a],choices[b]);ba=relation(choices[b],choices[a]);rt=compose(ab,ba);ident=diagonal(choices[a])
            assert rt==relation(choices[a],choices[a])
            assert compose(diagonal(choices[a]),ab)==ab and compose(ab,diagonal(choices[b]))==ab
            paths_here=[(x,y,z) for x,y in ab for y2,z in ba if y==y2]
            assert {(x,z) for x,y,z in paths_here}==rt
            multiplicities=[{'endpoints':[x,z],'middleParents':[y for u,y,w in paths_here if u==x and w==z]} for x,z in sorted(rt)]
            assert all(len(item['middleParents'])==len(choices[b]) for item in multiplicities)
            record={'vertex':v,'sourceChart':a,'viaChart':b,'sourceParents':choices[a],'middleParents':choices[b],
              'roundTripRelation':encode(rt),'diagonalIdentity':encode(ident),'offDiagonalParentChanges':encode(rt-ident),
              'endpointRelationIsIdentity':rt==ident,'retainedPathMultiplicity':multiplicities}
            roundtrips.append(record)
            if a!=b and rt==ident:
                assert len(paths_here)==2 and len(rt)==1
                retained_paths.append(record)
        for a in [0,7]:
            self_records.append({'vertex':v,'chart':a,'completeSelfRelationIsIdentity':relation(choices[a],choices[a])==diagonal(choices[a])})
        for a,b,c in product([0,7],repeat=3):
            assert compose(relation(choices[a],choices[b]),relation(choices[b],choices[c]))==relation(choices[a],choices[c]);triangles+=1
        for a,b,c,d in product([0,7],repeat=4):
            ab=relation(choices[a],choices[b]);bc=relation(choices[b],choices[c]);cd=relation(choices[c],choices[d])
            assert compose(compose(ab,bc),cd)==compose(ab,compose(bc,cd));associations+=1
            # The untruncated associator preserves every middle parent, not just endpoints.
            left=[((x,y,z),w) for x,y in ab for yy,z in bc if y==yy for zz,w in cd if z==zz]
            right=[(x,(y,z,w)) for x,y in ab for yy,z in bc if y==yy for zz,w in cd if z==zz]
            assert sorted((x,(y,z,w)) for (x,y,z),w in left)==sorted(right)
        facets=[f for f in range(4) if f!=vi]
        for f in facets:
            assert f in choices[assignment[f]]
            sections.setdefault((assignment[f],v),set()).add(f)
        for a,b,c in product(facets,repeat=3):
            assert compose({(a,b)},{(b,c)})=={(a,c)}
            assert compose({(a,b)},{(b,a)})=={(a,a)};selected_triangles+=1
    conflicts=[{'chart':c,'vertex':v,'requiredParentFaces':sorted(fs)} for (c,v),fs in sections.items() if len(fs)>1]
    cross=[r for r in roundtrips if r['sourceChart']!=r['viaChart']]
    assert (triangles,associations,selected_triangles)==(32,64,108)
    assert len(conflicts)==4 and len(retained_paths)==4
    assert sum(not r['endpointRelationIsIdentity'] for r in cross)==4
    assert sum(r['endpointRelationIsIdentity'] for r in cross)==4
    controls=[]
    def reject(name,predicate):
        assert not predicate,name+' unexpectedly valid';controls.append(name)
    reject('all complete cross-chart round trips are diagonal',all(r['endpointRelationIsIdentity'] for r in cross))
    reject('endpoint identity implies unique retained middle',all(len(m['middleParents'])==1 for r in retained_paths for m in r['retainedPathMultiplicity']))
    reject('one chart-vertex choice realizes every selected facet attachment',not conflicts)
    files=paths+[Path(__file__),BASE/'contracts/ramsey-attachment-relations-attempt.v1.json']
    out={'schema':'marici.ramsey-attachment-relations.verification.v1','status':'passed',
      'scope_id':'selected-cover-parent-correspondence-relations-and-witnesses-v1',
      'verification_level':'exact finite relation and untruncated path enumeration over validated parent choices; no new kernel replay',
      'relationTriangles':triangles,'relationAssociativityAndPathRebracketingCases':associations,
      'diagonalsActAsRelationIdentities':True,'completeSelfCorrespondences':self_records,'roundTrips':roundtrips,
      'crossChartRoundTripIdentityFailures':4,'crossChartEndpointIdentitiesWithTwoRetainedPaths':4,
      'selectedFacetComponentTriangles':selected_triangles,'selectedFacetRoundTripsAreIdentities':True,
      'chartVertexSectionConflicts':conflicts,'facetIndexCanBeForgottenWhilePreservingAllSelections':False,
      'completeCorrespondencesAreInvertible':False,'retainedNativeSpansRefuted':False,
      'negativeControlsRejected':controls,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files}}
    (BASE/'results/ramsey-attachment-relations-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','roundTrips','completeSelfCorrespondences']},indent=2))
if __name__=='__main__':main()
