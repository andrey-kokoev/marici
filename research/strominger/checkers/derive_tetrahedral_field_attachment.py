"""Rebuild native P from surface geometry; bind its grid to geometric frames."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import check_twelve_triangle_positive_geometry as geo
from assemble_metric_coefficient_protocol import A,read_operator,product,ZERO
BASE=ROOT/'research/strominger/results'
def lift(z):
    c=[F(0)]*16;c[0],c[10]=z;return A(tuple(c))
group={(0,1,2,3)};q=list(group)
for p in q:
    for g in [(1,2,0,3),(3,0,2,1)]:
        h=geo.compose(g,p)
        if h not in group:group.add(h);q.append(h)
assert len(group)==12
points=dict(geo.POINTS)
for face in combinations('ABCD',3):points['F_'+''.join(face)]=geo.mean([points[k] for k in face])
coeff=(geo.ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA));patches={}
for p in sorted(group):
    a,b,c=('ABCD'[p[i]] for i in range(3));triangle=('F_'+''.join(sorted((a,b,c))),a,b);X=geo.transpose(tuple(points[k] for k in triangle));v=geo.zmv(X,coeff);R=geo.rotation(p)
    patches[a+b]={'triangle':triangle,'v':v,'P':geo.projector(v),'R':R}
source=json.loads((BASE/'common-three-carrier-protocol/proton.json').read_text());labels=source['source']['coordinates'];L={};G={};z={}
for i,label in enumerate(labels):
    name,axis=label.split(':');a='xyz'.index(axis);z[i]=lift(patches[name]['v'][a])
    for j,other in enumerate(labels):
        target,bxis=other.split(':');b='xyz'.index(bxis)
        if name==target:
            value=lift(patches[name]['P'][a][b])
            if value!=ZERO:L[i,j]=value
        value=A(geo.mm(patches[name]['R'],geo.transpose(patches[target]['R']))[a][b]/12)
        if value!=ZERO:G[i,j]=value
assert L==read_operator(source['operators']['L'],36);assert G==read_operator(source['operators']['G'],36)
N=product(L,G);assert N==read_operator(source['operators']['N'],36)
gridData=json.loads((BASE/'baryon-tensor-grid/verification.json').read_text());grid=gridData['carriers']['proton']['grid'];binding=[]
for row in grid:
    names={labels[i].split(':')[0] for i in row};assert len(names)==1;name=names.pop();R=patches[name]['R'];axes=[]
    for i in row:
        axis='xyz'.index(labels[i].split(':')[1]);referenceAxis=next(j for j in range(3) if R[axis][j]);axes.append(referenceAxis)
    assert axes==[0,1,2]
    binding.append({'outerArrow':name,'surfaceTriangle':patches[name]['triangle'],'gridCoordinates':row,'coMovingAxes':axes,'rotation':[[str(x) for x in r] for r in R]})
# Actual P facet has edge squares 2, exactly the source tetrahedron scaled by 1/2.
metric=json.loads((BASE/'T-metric-gluing/verification.json').read_text());pFacet=metric['facets']['proton'];assert all(all(row['metric']['|'.join(sorted(e))]==2 for e in combinations(pFacet,2)) for row in metric['rows'])
# Scaling X by 1/2 changes vectors but not any projectors or rotation transport.
for patch in patches.values():assert geo.projector(tuple(geo.zscale(x,F(1,2)) for x in patch['v']))==patch['P']
# Simple facet relabelling + diagonal phase/amplitude rescaling cannot match N:
# it preserves the multiset of diagonal entries of the return projector.
neutron=json.loads((BASE/'common-three-carrier-protocol/neutron.json').read_text());nReturn=read_operator(neutron['operators']['N'],36)
pDiagonal=Counter(str(N[i,i].record()) for i in range(36));nDiagonal=Counter(str(nReturn[i,i].record()) for i in range(36));assert pDiagonal!=nDiagonal
paths=[Path(__file__).resolve(),Path(geo.__file__),BASE/'common-three-carrier-protocol/proton.json',BASE/'common-three-carrier-protocol/neutron.json',BASE/'baryon-tensor-grid/verification.json',BASE/'T-metric-gluing/verification.json'];hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
result={'status':'proton-geometric-field-attachment-derived','geometricConstruction':'12 outward centroid-edge triangles; local cyclic eigenline X(1,omega,omega^2); proper tetrahedral rotation transport; uniform group average','nativeFullCoefficientsReconstructed':{'L':True,'G':True,'return':True},'gridGeometry':binding,'TFacetBinding':{'facet':pFacet,'chosenMarking':dict(zip('ABCD',['a','b','u','v'])),'sourceScale':'1/2','nativePMetricMatches':True,'savedMetricSamples':len(metric['rows']),'meaning':'Marked regular tetrahedron identification; marker is an explicit choice, not canonically selected by unmarked T.'},'neutronExtension':{'pureRelabellingAndDiagonalGaugeWorks':False,'obstruction':'Return diagonal multisets differ; invariant under monomial similarity even after exchanging L and G. Additional mixing or neutron-specific geometric/occupation input required.','protonReturnDiagonal':dict(pDiagonal),'neutronReturnDiagonal':dict(nDiagonal)},'sourceHashes':hashes,'scope':'Reconstruction and attachment of existing native P geometric law, not a novel derivation of that prior construction. Choice of cyclic character, seed frame and marked vertex assignment remains explicit. Does not produce a global PNE field or edge sewing; N/E native geometry must be bound separately. Production/viewer unchanged.'}
out=BASE/'tetrahedral-field-attachment';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'patches':len(binding),'nativeCoefficientsMatch':True,'coMovingGridColumnsMatch':True,'PFacetMetricsChecked':len(metric['rows']),'neutronMonomialExtension':False}))
