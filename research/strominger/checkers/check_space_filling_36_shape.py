"""Exact polyhedral census, truncated-octahedral Voronoi tile and native gate."""
from pathlib import Path
from itertools import combinations,permutations,product
from fractions import Fraction as F
from math import gcd
from functools import reduce
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/strominger/results/space-filling-36-shape'
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
cross=lambda a,b:(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def primitive(n):
    g=reduce(gcd,map(abs,n));return tuple(x//g for x in n) if g else None

def unoriented(n):
    n=primitive(n)
    return tuple(-x for x in n) if next(x for x in n if x)!=abs(next(x for x in n if x)) else n

def hull(vertices):
    v=sorted(set(vertices));facets={}
    for a,b,c in combinations(v,3):
        n=primitive(cross(sub(b,a),sub(c,a)))
        if n is None:continue
        d=dot(n,a);s=[dot(n,x)-d for x in v]
        if max(s)<=0:pass
        elif min(s)>=0:n=tuple(-x for x in n);d=-d
        else:continue
        facets[n,d]=tuple(i for i,x in enumerate(v) if dot(n,x)==d)
    edges=[(i,j) for i,j in combinations(range(len(v)),2) if sum(i in face and j in face for face in facets.values())==2]
    assert len(v)-len(edges)+len(facets)==2
    volume=F(0)
    for (n,d),face in facets.items():
        adjacency={i:[j if a==i else a for a,j in edges if a==i or j==i if (j if a==i else a) in face] for i in face}
        assert all(len(x)==2 for x in adjacency.values())
        cycle=[face[0],adjacency[face[0]][0]]
        while len(cycle)<len(face):cycle.append(next(j for j in adjacency[cycle[-1]] if j!=cycle[-2]))
        assert cycle[0] in adjacency[cycle[-1]]
        if dot(cross(sub(v[cycle[1]],v[cycle[0]]),sub(v[cycle[2]],v[cycle[0]])),n)<0:cycle=[cycle[0]]+list(reversed(cycle[1:]))
        for k in range(1,len(cycle)-1):volume+=F(dot(v[cycle[0]],cross(v[cycle[k]],v[cycle[k+1]])),6)
    return v,facets,edges,volume

cube=list(product([-1,1],repeat=3))
cubocta=list({p for signs in product([-1,1],repeat=2) for p in permutations((0,*signs))})
truncated=list({p for s,t in product([-1,1],repeat=2) for p in permutations((0,s,2*t))})
rhombic=cube+[tuple(2*s if j==i else 0 for j in range(3)) for i in range(3) for s in [-1,1]]
rows={}
for name,points in [('cube',cube),('cuboctahedron',cubocta),('rhombic_dodecahedron',rhombic),('truncated_octahedron',truncated)]:
    v,faces,edges,vol=hull(points);groups={str(i):0 for i in range(3)};other=0
    for a,b in edges:
        d=sub(v[a],v[b]);zero=[i for i,x in enumerate(d) if x==0]
        if len(zero)==1:groups[str(zero[0])]+=1
        else:other+=1
    rows[name]={'vertices':len(v),'edges':len(edges),'faces':len(faces),'faceSizes':sorted(map(len,faces.values())),'volume':str(vol),'edgesGroupedByUniqueZeroDisplacementCoordinate':groups,'otherEdgeDirections':other}
    if name=='truncated_octahedron':tv,tf,te=v,faces,edges
assert (len(tv),len(tf),len(te))==(24,14,36)
assert rows['truncated_octahedron']['edgesGroupedByUniqueZeroDisplacementCoordinate']=={'0':12,'1':12,'2':12}
assert rows['truncated_octahedron']['volume']=='32'
assert all(max(map(abs,v))<=2 and sum(map(abs,v))==3 for v in tv)
# Relevant Voronoi vectors: axis translations +/-4e_i and all (+/-2)^3.
relevant=[tuple(4*s if j==i else 0 for j in range(3)) for i in range(3) for s in [-1,1]]+list(product([-2,2],repeat=3))
voronoi={}
for t in relevant:
    g=reduce(gcd,map(abs,t));n=tuple(x//g for x in t);d=F(dot(t,t),2*g);assert d.denominator==1;voronoi[n,int(d)]=True
assert set(voronoi)==set(tf)
# All other lattice vectors are redundant, by the inequalities stated below.
# Bounded checks are regression controls, not the infinite-lattice proof.
controls=0
for offset in [0,2]:
    for abc in product(range(-3,4),repeat=3):
        t=tuple(4*a+offset for a in abc)
        if t==(0,0,0):continue
        assert max(dot(t,v) for v in tv)<=F(dot(t,t),2);controls+=1
# Native fixed-template face normals in the same physical tetrahedral chart.
source=json.loads((OUT/'native-templates.json').read_text(encoding='utf8'))
for path,digest in source['sourceHashes'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'stale native template export: '+path
base=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
normals=set()
for item in source['items']:
    for component in item['components']:
        v=[tuple(sum(p[i]*base[i][j] for i in range(4)) for j in range(3)) for p in component]
        for a,b,c in combinations(v,3):normals.add(unoriented(cross(sub(b,a),sub(c,a))))
assert len(normals)==6
candidateNormals={unoriented(n) for n,d in tf};assert len(candidateNormals)==7
missing=sorted(candidateNormals-normals);assert missing==[(0,1,0)]
# For a convex full-cell union F<=12. Euler and minimum degree3 give E<=3F-6.
assert 3*(2*len(normals))-6==30<36
result={'status':'36-edge-tiler-found-but-fixed-native-whole-cell-assembly-obstructed','candidates':rows,'truncatedOctahedron':{'edgePartition':'12 edges in each of the three coordinate-plane direction families','center':'origin in the fixed symmetric realization','translationLattice':'(4 Z)^3 union ((2,2,2)+(4 Z)^3)','covolume':32,'body':'|x_i|<=2 and |x|+|y|+|z|<=3','tilingProof':'These14 facets are Voronoi bisectors. For vectors in (4Z)^3, |t|^2/2>=2 sum|t_i| bounds the box support. In the odd coset each |t_i|>=2; if all equal2 the l1 constraint gives support<=6=|t|^2/2. Otherwise at least one |t_i|>=6: its contribution t_i^2/2-2|t_i|>=6 compensates the other two contributions >=-2 each. Hence every other lattice bisector is redundant. A full-rank lattice has a nearest point everywhere, so its closed Voronoi cells cover R3 with disjoint interiors.','boundedBisectorRegressionCases':controls,'nativeWholeCellAssembly':False},'nativeGate':{'sourceTemplateCount':6,'unorientedFaceNormals':sorted(normals),'maximumConvexFacets':12,'maximumConvexGeometricEdges':30,'candidateUnorientedNormalClasses':7,'missingAlignedCandidateNormal':missing,'orientationIndependentObstruction':'Any rigidly rotated or affinely transformed truncated octahedron still has7 distinct facet-normal classes, whereas this fixed native subdivision permits only6. No convex36-edge solid can be an exact union of its complete primitive cells.','scope':'No cuts, changed subdivision, new orientations or nonconvex boundary allowed. Degree-two subdivision edges are not counted as geometric solid edges. This does not reject36 field coordinates or every nonconvex PNE assembly.'},'PNEAssignment':'not constructed','fieldSewing':'not tested or admitted','atomicNumberIdentification':False}
files=[Path(__file__),ROOT/'research/strominger/checkers/export_native_solid_templates.mjs',ROOT/'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',ROOT/'research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs',ROOT/'research/strominger/space-filling-36-shape-protocol-v1.md',OUT/'native-templates.json'];result['sourceHashes']={p.resolve().relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};(OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({'status':result['status'],'candidateCounts':[24,36,14],'edgeGroups':[12,12,12],'nativeNormalClasses':6,'candidateNormalClasses':7,'nativeConvexEdgeBound':30}))
