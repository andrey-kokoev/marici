"""Minimal linear rotation-closed observation space, with exact certificates."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky';V='research/voevodsky/'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def mul(a,b):return [[sum(x*b[k][j] for k,x in enumerate(row)) for j in range(len(b[0]))] for row in a]
def enc(a):return [[str(x) for x in row] for row in a]
def rref(a):
    a=[list(map(F,row)) for row in a];trans=eye(len(a));pivots=[];r=0
    for j in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][j]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];trans[r],trans[p]=trans[p],trans[r]
        divisor=a[r][j];a[r]=[x/divisor for x in a[r]];trans[r]=[x/divisor for x in trans[r]]
        for i in range(len(a)):
            if i==r:continue
            factor=a[i][j]
            if factor:
                a[i]=[x-factor*y for x,y in zip(a[i],a[r])]
                trans[i]=[x-factor*y for x,y in zip(trans[i],trans[r])]
        pivots.append(j);r+=1
        if r==len(a):break
    return a[:r],trans[:r],pivots

def main():
    paths=[V+'results/ramsey-moving-edge-geometry-v1.json',V+'results/ramsey-geometric-edge-readout-v1.json',
      'research/strominger/results/common-three-carrier-protocol/proton.json']
    moving,edge,proton=[json.loads((ROOT/p).read_text()) for p in paths]
    for d in [moving,edge]:
        for p,h in d['source_sha256'].items():assert sha(p)==h,'stale observation input '+p
    def scalar(x):
        assert set(x)<= {'1'},'nonrational observation coefficient'
        return F(x.get('1','0'))
    h=[[scalar(x) for x in row] for row in edge['readout']]
    rotation=[[F(i==(j+12)%36) for j in range(36)] for i in range(36)]
    square=mul(rotation,rotation);assert mul(square,rotation)==eye(36)
    orbit=h+mul(h,rotation)+mul(h,square)
    o,combination,pivots=rref(orbit);rank=len(o)
    assert 12<rank<=36 and mul(combination,orbit)==o
    def coordinates(rows):return [[row[j] for j in pivots] for row in rows]
    orbit_decoder=coordinates(orbit);assert mul(orbit_decoder,o)==orbit
    decoder=coordinates(h);assert mul(decoder,o)==h
    action=coordinates(mul(o,rotation))
    assert mul(action,o)==mul(o,rotation) and mul(action,mul(action,action))==eye(rank)
    labels=proton['source']['coordinates'];patches=list(dict.fromkeys(x.split(':')[0] for x in labels))
    patch_records=[]
    for patch in patches:
        slots=[j for j,x in enumerate(labels) if x.split(':')[0]==patch]
        local=[row for row in orbit if any(row[j] for j in slots)]
        assert len(local)==3 and all(not row[j] for row in local for j in range(36) if j not in slots)
        basis,_,_=rref([[row[j] for j in slots] for row in local])
        patch_records.append({'patch':patch,'coordinateSlots':slots,'rank':len(basis),'localCovectors':enc(basis)})
    assert sum(p['rank'] for p in patch_records)==rank
    supports=[[labels[j] for j,x in enumerate(row) if x] for row in o]
    assert all(len({x.split(':')[0] for x in support})==1 for support in supports)
    free=[j for j in range(36) if j not in pivots]
    kernel=[[F(0) for _ in free] for _ in range(36)]
    for k,j in enumerate(free):
        kernel[j][k]=F(1)
        for i,p in enumerate(pivots):kernel[p][k]=-o[i][j]
    if free:
        zero=[[F(0) for _ in free] for _ in o]
        assert mul(o,kernel)==zero and mul(o,mul(rotation,kernel))==zero
        kernel_action=[row[:] for i,row in enumerate(mul(rotation,kernel)) if i in free]
        assert mul(kernel,kernel_action)==mul(rotation,kernel)
        assert mul(kernel_action,mul(kernel_action,kernel_action))==eye(len(free))
    else:kernel_action=[]
    files=paths+[V+'contracts/ramsey-edge-observation-closure-attempt.v1.json',V+'checkers/check_ramsey_edge_observation_closure.py']
    out={'schema':'marici.ramsey-edge-observation-closure.verification.v1','status':'passed',
      'scope_id':'minimal-linear-sector-closed-proton-edge-observation-v1',
      'verification_level':'exact rational RREF and two-way row-space/action certificates; no new kernel replay',
      'originalObservationDimension':12,'closedObservationDimension':rank,'additionalIndependentCovectors':rank-12,
      'discardedFieldDimension':len(free),'orbitObservation':enc(orbit),'closedObservation':enc(o),
      'orbitToClosedRowCombination':enc(combination),'closedToOrbitDecoder':enc(orbit_decoder),
      'originalTraceDecoder':enc(decoder),'outputSectorAction':enc(action),'outputActionOrderDividesThree':True,
      'pivotCoordinates':pivots,'patches':patch_records,'closedRowSupports':supports,
      'discardedFieldBasis':enc(kernel),'discardedFieldSectorAction':enc(kernel_action),
      'discardedSubspaceRotationInvariant':True,'minimalAmongLinearInvariantObservationSpaces':True,
      'eachClosedRowSinglePatchSupported':True,'closureIsOriginalScalarEdgeConvention':False,
      'geometricVertexTransportProved':False,'parentDescentResolved':False,
      'source_sha256':{p:sha(p) for p in files}}
    (BASE/'results/ramsey-edge-observation-closure-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','closedObservationDimension','additionalIndependentCovectors','discardedFieldDimension','outputActionOrderDividesThree','discardedSubspaceRotationInvariant','patches','parentDescentResolved']},indent=2))
if __name__=='__main__':main()
