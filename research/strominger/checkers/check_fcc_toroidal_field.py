"""FCC quotient, native subdivision gates and pose-dependent field frames."""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,subprocess,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
run=subprocess.run(['node',str(Path(__file__).with_name('check_fcc_toroidal_geometry.mjs'))],cwd=ROOT,capture_output=True,text=True,check=True)
geometry_path=ROOT/'research/strominger/results/fcc-toroidal-geometry/verification.json'
geometry=json.loads(geometry_path.read_text())
for path,digest in geometry['sourceHashes'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest
log=io.StringIO()
with contextlib.redirect_stdout(log):import check_toroidal_rung12 as torus
source=torus.source;s=source.s;g=source.g;geo=s.r.geo;A,Z,O=source.A,source.Z,source.O
labels='ABCD';classes=[tuple(map(F,v)) for v in geometry['classes']]
# Root FCC edge length sqrt(2), source field tetrahedron edge length 2sqrt(2).
# Use one declared factor two in local centered coordinates, not fitted scales.
Q=((F(0),F(0),F(-1)),(F(0),F(-1),F(0)),(F(-1),F(0),F(0)))
assert geo.det(Q)==1 and geo.mm(geo.transpose(Q),Q)==geo.I
center=geo.mean(classes)
assert all(tuple(2*x for x in geo.sub(classes[i],center))==geo.mv(Q,geo.POINTS[labels[i]]) for i in range(4))
def idx(edge):return [source.labels.index(edge+':'+axis) for axis in 'xyz']
def put(M,rows,cols,X):
    for i in range(3):
        for j in range(3):
            if X[i][j]:M[rows[i],cols[j]]=A(X[i][j])
def pose_frames(vertices,p):
    B={};center=geo.mean(vertices)
    for edge,patch in s.r.patches.items():
        face=[labels.index(c) for c in patch['surfaceTriangle'][0][2:]]
        a,b=map(labels.index,edge)
        points=(geo.mean([vertices[i] for i in face]),vertices[a],vertices[b])
        X=geo.transpose(tuple(tuple(2*x for x in geo.sub(v,center)) for v in points))
        target=labels[p[a]]+labels[p[b]];put(B,idx(target),idx(target),X)
    return B
Q36={}
for edge in s.r.patches:put(Q36,idx(edge),idx(edge),Q)
B0=pose_frames(classes,(0,1,2,3));assert B0==g.mul(Q36,s.B)
assert g.mul(s.adjoint(B0),B0)==s.K
L0=g.mul(g.mul(Q36,g.L),s.adjoint(Q36));G0=g.mul(g.mul(Q36,g.G),s.adjoint(Q36));C0=g.mul(g.mul(Q36,s.r.cycleP),s.adjoint(Q36))
rho=((F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(0),F(1),F(0)))
results=[]
assert {tuple(row['vertexPermutation']) for row in geometry['affineActions']}==set(s.sourceActions)
for row in geometry['affineActions']:
    p=tuple(row['vertexPermutation']);k=row['rotationPower'];R=geo.I
    for _ in range(k):R=geo.mm(rho,R)
    V=s.sourceActions[p];W={}
    for edge in s.r.patches:
        target=''.join(labels[p[labels.index(c)]] for c in edge)
        put(W,idx(target),idx(edge),R)
    vertices=[tuple(map(F,v)) for v in row['transformedRootVertices']]
    Bt=pose_frames(vertices,p)
    assert g.mul(s.adjoint(W),W)==s.I
    assert g.mul(s.adjoint(Bt),Bt)==s.K
    # Bt was rebuilt from actual translated/rotated vertices, not defined by
    # conjugation merely to force the square to commute.
    assert g.mul(W,B0)==g.mul(Bt,V)
    unchanged=g.mul(W,B0)==g.mul(B0,V)
    assert unchanged==(row['translation']==[0,0,0])
    for corner,spatial in ((source.Lp,L0),(source.Gp,G0),(s.sourceCycle,C0)):
        transported=g.mul(g.mul(W,spatial),s.adjoint(W))
        assert g.mul(Bt,corner)==g.mul(transported,Bt)
    results.append({'translation':row['translation'],'rotationPower':k,'vertexPermutation':p,
                    'targetCenter':[str(x) for x in geo.mean(vertices)],'fixedGlobalFrameSquare':unchanged,
                    'poseDependentFrameSquare':True,'metricPreserved':True,'namedOperatorsTransported':True})
assert sum(not row['fixedGlobalFrameSquare'] for row in results)==9
report={'schema':'marici.fcc-toroidal-field.v1','status':'pass',
 'fourClassesAndA4ChannelsVerified':True,'affineA4Order':12,'unrefinedBoundarySquares':geometry['unrefinedBoundarySquares'],
 'nativeFixedSubdivisionPreservingAffineElements':geometry['affineActionsPreservingFixedSubdivision'],
 'nativeFixedSubdivisionPreservingProperRootRotations':geometry['properRootA4ActionsPreservingFixedSubdivision'],
 'rootSubdivisionAndCMStabilizer':geometry['properRootActionsPreservingSubdivisionAndNamedCMPartition'],
 'threeRefinementFamilyEquivariant':geometry['threeChoiceRefinementFamilyEquivariant'],
 'centerStarIsNative':geometry['centerStarAlternative']['nativePrimitive'],
 'fixedGlobalFrameFailures':9,'poseDependentSquares':12,'sourceMetricPreserved':True,'fieldUnitScale':2,
 'poseTests':results,'deckCompositionsRetained':len(geometry['products']),
 'nonzeroDeckCompositions':sum(any(p['deck']) for p in geometry['products']),
 'nativeGrammarChanged':False,'nativeTransferLiftEstablished':False,
 'scope':'Geometry and field-pose correspondence for the FCC quotient. Not a native move between refinements, an invariant marked assembly, or a five-coefficient/absolute-origin transfer witness.',
 'geometryReplay':run.stdout,'fieldReplay':log.getvalue()}
out=ROOT/'research/strominger/results/fcc-toroidal-field';out.mkdir(parents=True,exist_ok=True)
paths=[Path(__file__),geometry_path,ROOT/'research/strominger/results/toroidal-rung12/verification.json',ROOT/'research/strominger/fcc-toroidal-field-v1.md']
report['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','affineA4Order','nativeFixedSubdivisionPreservingAffineElements','rootSubdivisionAndCMStabilizer','threeRefinementFamilyEquivariant','fixedGlobalFrameFailures','poseDependentSquares','nativeGrammarChanged')},indent=2))
