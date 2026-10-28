"""Do moving scalar rows implement geometric edge restrictions?"""
from itertools import permutations
from check_ramsey_prepared_edge_locality import ROOT,V,S,load,sha,restore,R,F,mm,serialize,identity,adj
import json

def main():
    paths=[V+'results/ramsey-signed-invariant-core-v1.json',V+'results/ramsey-geometric-edge-readout-v1.json',
      S+'common-three-carrier-protocol/proton.json',V+'results/ramsey-world-frame-action-v1.json']
    core,edge,proton,marking=[load(p) for p in paths]
    for d in [core,edge,marking]:
        for p,h in d['source_sha256'].items():assert sha(p)==h,'stale geometric test '+p
    h=restore(edge['readout']);desc=edge['descriptors'];labels=proton['source']['coordinates']
    assert mm(h,adj(h))==[[R(8*int(i==j)) for j in range(12)] for i in range(12)]
    rotation=[[R(int(i==(j+12)%36)) for j in range(36)] for i in range(36)]
    powers=[identity(36),rotation,mm(rotation,rotation)];assert mm(powers[2],rotation)==identity(36)
    domains=[restore(x) for x in core['movingEmbeddings']]
    def row_action(perm):
        rename=dict(zip('ABCD',perm));action=[[R() for _ in range(12)] for _ in range(12)]
        for old,d in enumerate(desc):
            a,b=[rename[x] for x in d['edge']];arrow=''.join(rename[x] for x in d['patch'])
            new=next(i for i,x in enumerate(desc) if x['edge']==''.join(sorted(a+b)) and x['patch']==arrow)
            action[new][old]=R(1 if a<b else -1)
        return action
    relabelings=[(''.join(p),row_action(p)) for p in permutations('ABCD')]
    positive=row_action('BADC')
    assert mm(h,restore(marking['protonAction']))==mm(positive,h)
    records=[]
    for t in range(3):
        moving=mm(h,powers[(-t)%3]);domain=domains[t]
        assert mm(moving,domain)==mm(h,domains[0])
        full=[];restricted=[];support_matches=[]
        supports=[sorted({labels[j].split(':')[0] for j,x in enumerate(row) if x!=R()}) for row in moving]
        assert all(len(s)==1 for s in supports)
        for name,w in relabelings:
            wh=mm(w,h)
            if moving==wh:full.append(name)
            if mm(moving,domain)==mm(wh,domain):restricted.append(name)
            # w's row labels select exactly one original occurrence, sign ignored.
            selected=[next(j for j,x in enumerate(row) if x!=R()) for row in w]
            if all(supports[i]==[desc[j]['patch']] for i,j in enumerate(selected)):support_matches.append(name)
        # Exact projection into row(H); H has independent real rows of norm^2=8.
        coefficients=[[x*F(1,8) for x in row] for row in mm(moving,adj(h))]
        projection=mm(coefficients,h)
        residual=[[x-y for x,y in zip(a,b)] for a,b in zip(moving,projection)]
        witness=None
        if any(x!=R() for row in residual for x in row):
            i=next(i for i,row in enumerate(residual) if any(x!=R() for x in row))
            k=adj([residual[i]])
            assert mm(h,k)==[[R()] for _ in range(12)]
            value=mm(moving,k);assert value[i][0]!=R()
            witness={'movingRow':i,'descriptor':desc[i],'fieldVector':serialize(k),
              'fixedReadouts':serialize(mm(h,k)),'movingReadouts':serialize(value),
              'scope':'full36-coordinate field space, not asserted to belong to the moving preparation'}
        if t==0:assert full and restricted and support_matches and witness is None
        else:assert not full and not restricted and not support_matches and witness is not None
        records.append({'frame':t,'fullFieldGeometricRelabelings':full,'movingPreparationGeometricRelabelings':restricted,
          'patchSupportGeometricRelabelings':support_matches,'movingRowPatchSupports':supports,
          'fullFieldFactorsThroughFixedTraceChannels':witness is None,'fullFieldNonfactorWitness':witness,
          'movingObservation':serialize(moving)})
    files=paths+[V+'contracts/ramsey-moving-edge-geometry-attempt.v1.json',V+'checkers/check_ramsey_moving_edge_geometry.py',
      V+'checkers/check_ramsey_prepared_edge_locality.py','research/strominger/checkers/exact_multiradical.py']
    out={'schema':'marici.ramsey-moving-edge-geometry.verification.v1','status':'passed',
      'scope_id':'moving-proton-edge-observations-versus-tetrahedral-relabeling-v1',
      'verification_level':'exact finite runtime support, row-action and fiber checks; no new kernel numerical interpretation',
      'geometricRelabelingsPerFrame':24,'geometricMarkingPositiveControlPassed':True,
      'frames':records,'movingReadoutIdentityOnMovingPreparation':True,
      'nontrivialFramesAreFixedGeometryEdgeRelabelings':False,
      'eachMovingRowSupportedOnOnePatch':True,'additionalFieldsOrChangedGeometryRefuted':False,
      'parentDescentResolved':False,'source_sha256':{p:sha(p) for p in files}}
    (ROOT/(V+'results/ramsey-moving-edge-geometry-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({**{k:v for k,v in out.items() if k not in ['frames','source_sha256']},
      'frames':[{k:v for k,v in r.items() if k not in ['movingObservation','fullFieldNonfactorWitness']} for r in records]},indent=2))
if __name__=='__main__':main()
