"""Source-derived operator comparisons, exact recovery and alignment phase fiber."""
from pathlib import Path
import ast,contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_field_rotation_rigidity as r
from check_pentachoron_spin_interfaces import root
A,F,Z,O=r.A,r.F,r.ZERO,r.ONE
edges=sorted(r.patches);metric=[F(1)]*36
conj=lambda z:z.flip(8)
dot=lambda a,b:sum((conj(x)*y for x,y in zip(a,b)),Z)
outer=lambda a,b:{(i,j):a[i]*conj(b[j]) for i in range(len(a)) for j in range(len(b)) if a[i]*conj(b[j])!=Z}
mv=lambda M,v:[sum((x*v[j] for (ii,j),x in M.items() if ii==i),Z) for i in range(36)]
matvec=lambda M,v:[sum((A(M[i][j])*v[j] for j in range(3)),Z) for i in range(3)]
frames={e:tuple(tuple(map(F,row)) for row in r.patches[e]['rotation']) for e in edges}
def spatial(q):
    v=[Z]*36
    for e in edges:
        for axis,x in zip('xyz',matvec(frames[e],q[e])):v[r.labels.index(e+':'+axis)]=x
    return v

def comoving(v):return {e:matvec(r.geo.transpose(frames[e]),[v[r.labels.index(e+':'+a)] for a in 'xyz']) for e in edges}

def prepare(v,mark='AB'):
    q=comoving(v);blocks={(a,b):outer(q[a],q[b]) for a in edges for b in edges}
    anchor=next(((e,i,q[e][i]) for e in edges for i in range(3) if q[e][i]!=Z),None)
    return {'mark':mark,'counted':{k:x for k,x in blocks.items() if mark not in k},'reference':{k:x for k,x in blocks.items() if mark in k},'anchor':anchor}

def recover(p):
    blocks={**p['counted'],**p['reference']};assert set(blocks)=={(a,b) for a in edges for b in edges}
    if p['anchor'] is None:
        assert not any(blocks.values());return [Z]*36
    e,j,value=p['anchor'];assert value!=Z
    q={a:[blocks[a,e].get((i,j),Z)/conj(value) for i in range(3)] for a in edges}
    assert q[e][j]==value
    assert all(outer(q[a],q[b])==blocks[a,b] for a in edges for b in edges)
    return spatial(q)

I=root(8);sqrt12=A(2)*root(2)
normal=[A(1)/root(2),A(1)/root(2),A(-1)/root(2)]
X=r.geo.transpose(tuple(r.points[k] for k in r.patches['AB']['surfaceTriangle']))
z=list(map(r.lift,r.geo.zmv(X,r.coeff)));nz=A(2)*root(2)*root(4)/A(3)
selected=[x/nz for x in z]
cross=lambda a,b:[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
other=[x/nz for x in cross(normal,[conj(x) for x in z])]
assert dot(normal,normal)==dot(selected,selected)==dot(other,other)==O
assert dot(normal,selected)==dot(other,selected)==dot(normal,other)==Z
aligned=lambda w:spatial({e:[x/sqrt12 for x in w] for e in edges})
a,b=aligned(normal),aligned(other)
for v in [a,b]:
    assert dot(v,v)==O and mv(r.Pop['G'],v)==v and mv(r.Pop['N'],v)==[Z]*36
qa,qb=comoving(a),comoving(b)
assert all(dot(qa[e],qa[f])==dot(qb[e],qb[f]) for e in edges for f in edges)
pa,pb=prepare(a),prepare(b)
assert pa['counted']!=pb['counted'] and recover(pa)==a and recover(pb)==b
# Complete reconstruction, including zero and source-reference-only inputs.
dense=spatial({e:[A(i+1),I*A(i+2),A(i%3-1)] for i,e in enumerate(edges)})
referenceOnly=spatial({e:([O,Z,Z] if e=='AB' else [Z]*3) for e in edges})
fixtures=[[Z]*36,a,b,dense,referenceOnly,[I*x for x in dense]]
for v in fixtures:
    p=prepare(v);assert len(p['counted'])==121 and len(p['reference'])==23;assert recover(p)==v
assert prepare(referenceOnly)['counted']==prepare([Z]*36)['counted']
assert prepare(dense)['counted']==prepare([I*x for x in dense])['counted']
assert prepare(dense)['reference']==prepare([I*x for x in dense])['reference']
assert prepare(dense)['anchor']!=prepare([I*x for x in dense])['anchor']
# Rotations act independently on geometry; comparisons transport the mark too.
original=prepare(dense);covariance=0
for row in r.Prows:
    if row['orientation']!=1:continue
    g=row['vertices'];R=r.geo.rotation(g);rename=lambda e:''.join('ABCD'[g['ABCD'.index(c)]] for c in e);v=[Z]*36
    for e in edges:
        image=matvec(R,[dense[r.labels.index(e+':'+axis)] for axis in 'xyz'])
        for axis,x in zip('xyz',image):v[r.labels.index(rename(e)+':'+axis)]=x
    actual=prepare(v,rename('AB'));assert recover(actual)==v
    for section in ['counted','reference']:
        assert {(rename(e),rename(f)):block for (e,f),block in original[section].items()}==actual[section]
    covariance+=1
# Read the existing numerical multiplication, without running its fixtures.
legacy=r.ROOT/'research/nima/checkers/check_shared_leg_dg_realization.py'
node=next(x for x in ast.parse(legacy.read_text(encoding='utf8')).body if isinstance(x,ast.FunctionDef) and x.name=='mul')
namespace={'F':F};exec(compile(ast.Module(body=[node],type_ignores=[]),str(legacy),'exec'),namespace)
P3=tuple(tuple(F(i==j==2) for j in range(3)) for i in range(3))
legacyProduct=namespace['mul'](P3,P3);assert legacyProduct==((F(0),F(0)),(F(0),F(0)))
# Alignment embedding: this is a state subspace, not a new symmetry group.
J={}
for col,w in enumerate([selected,normal,other]):
    for i,x in enumerate(aligned(w)):
        if x!=Z:J[i,col]=x
Jstar={(j,i):conj(x) for (i,j),x in J.items()}
assert r.product(Jstar,J)=={(i,i):O for i in range(3)}
assert r.product(J,Jstar)==r.Pop['G']
assert r.product(r.Pop['N'],J)=={(i,j):x for (i,j),x in J.items() if j==0}
# The native dimensionless projector defect on the alignment sector is
# diag(0,1,1). Fixing it gives a different four-dimensional object than the
# horizontal distribution of the projective readout.
I36={(i,i):O for i in range(36)};P0={(0,0):O}
H=r.plus(r.scaled(A(2),I36),r.scaled(A(-1),r.Pop['L']),r.scaled(A(-1),r.Pop['G']))
assert r.product(r.product(Jstar,H),J)=={(1,1):O,(2,2):O}
wmid=[O/root(1),O/root(1),Z]
generators=[{(0,0):I},{(1,1):I},{(2,1):O,(1,2):-O},{(2,1):I,(1,2):I}]
smallmv=lambda M,v:[sum((x*v[j] for (ii,j),x in M.items() if ii==i),Z) for i in range(3)]
tangents=[]
for K in generators:
    assert r.sharp(K,[F(1)]*3)==r.scaled(A(-1),K)
    assert r.product(K,P0)==r.product(P0,K)
    d=smallmv(K,wmid);assert dot(wmid,d)+dot(d,wmid)==Z
    assert conj(wmid[0])*d[0]+conj(d[0])*wmid[0]==Z
    tangents.append(d)
assert tangents==[[I/root(1),Z,Z],[Z,I/root(1),Z],[Z,Z,O/root(1)],[Z,Z,I/root(1)]]
assert smallmv({(2,2):I},wmid)==[Z]*3
# At w=e0 the sphere tangent has five real basis vectors; projective readout
# kills i e0 and detects the four other vectors independently.
w=[O,Z,Z];vertical=[I,Z,Z];horizontal=[[Z,O,Z],[Z,I,Z],[Z,Z,O],[Z,Z,I]]
drho=lambda d:r.plus(outer(d,w),outer(w,d))
assert drho(vertical)=={}
assert all(dot(w,d)==Z for d in horizontal)
assert [drho(d).get((1,0),Z) for d in horizontal]==[O,I,Z,Z]
assert [drho(d).get((2,0),Z) for d in horizontal]==[Z,Z,O,I]
# d alpha(delta,epsilon) = -i(<delta,epsilon>-<epsilon,delta>).
curvature=-I*(dot(horizontal[0],horizontal[1])-dot(horizontal[1],horizontal[0]));assert curvature==A(2)
result={'status':'operator-comparison-preparation-retains-relative-modes-with-reference-and-phase-anchor','comparisonType':'q_j q_i* : C^3 -> C^3; factorization C^3 -> C -> C^3','countedArrowBlocks':121,'retainedReferenceBlocks':23,'stateBranch16':'not constructed from the field; historical independent state preparation remains separate','reconstructionFixtures':len(fixtures),'rotationCovarianceCases':covariance,'controls':{'equal_scalar_Gram_different_relative_modes':True,'operator_blocks_distinguish_relative_modes':True,'counted_only_loses_reference_only_field':True,'unanchored_blocks_lose_common_phase':True,'anchor_restores_full_field':True,'legacy_2_by_2_mul_erases_third_coordinate_if_misfed':True},'alignmentGeometry':{'complexRank':3,'embedding':'J*J=I3, JJ*=G_P; return is first coordinate','normalizedStateSpace':'S^5 in C^3','unanchoredProjectiveReadout':'CP^2, real dimension 4','nonzeroUnnormalizedReadout':'positive norm scale times CP^2','fiber':'U(1) on nonzero states; zero is a separate stratum','fullyLocalAndAlignedCoherentNormalizedStates':'S^1 on the rank-one return, not S^5','fixedDefectLevels':{'defect':'c=1-|w0|^2 in native dimensionless Hhat units','generic_0<c<1':'S^1 x S^3, real dimension 4, an actual codimension-one level set in S^5','c=0':'S^1','c=1':'S^3','independentProjectorPreservingTangentGeneratorsChecked':4,'unfixedLieStabilizerAtGenericStateDimension':1,'cycleBoundary':'These four directions preserve the metric and projectors, not all ordered corner-cycle data; full cycle rigidity still leaves common phase only.'},'sphereTangentRealDimension':5,'metricHorizontalRealDimension':4,'verticalPhaseRealDimension':1,'readoutDifferentialRealRankAtDeclaredPoint':4,'horizontalCurvatureWitness':curvature.record(),'integrability':'fails: d alpha is nonzero on two horizontal tangent vectors','boundary':'The normalized alignment sector is not the whole C^36 field. Horizontal state variations are not all symmetries preserving L and ordered cycles. The four-dimensional readout is a quotient, not an embedded spacetime layer; phase is not native realization grade or physical time.'},'scope':'A chosen operator-valued comparison constructed from native frames. Exact field recovery requires the 23 reference blocks and an amplitude anchor. Not a numerical assignment into the existing 2-by-2 T9 fixture, not an automatic 137-state preparation, not a physical observer or a Postnikov/rung identification.'}
files=[Path(__file__),Path(r.__file__),legacy,r.ROOT/'research/strominger/field-comparison-preparation-protocol-v1.md',r.BASE/'field-rotation-rigidity/verification.json'];result['sourceHashes']={p.resolve().relative_to(r.ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};out=r.BASE/'field-comparison-preparation';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({'status':result['status'],'countedBlocks':121,'referenceBlocks':23,'rotationChecks':covariance,'normalizedAlignment':'S5 -> CP2 with U1 fiber','horizontalCurvature':2,'nativeT9Bound':False}))
