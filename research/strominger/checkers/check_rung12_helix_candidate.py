"""Three-helix field layout: exact algebraic encoding and geometric obstructions.
No isotope or native spatial identification is inferred from this layout.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,product
import contextlib,io,json,hashlib,math
from field_refibration import EDGES
from field_metric_comparisons import pairing,rank
from field_reconstruction import solve,positive_real
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):import check_rung_automorphism_classification as source
A,Z,O=source.A,source.Z,source.O;K,P,C=source.K,source.P,source.C;g=source.g
I={(i,j):A(int(i==j)) for i in range(3) for j in range(3)}
Q={key:I[key]-P[key] for key in I}
conj=lambda x:x.flip(8)
dot=lambda x,y:pairing(x,y,K,Z)
column=lambda M,j:tuple(M.get((i,j),Z) for i in range(3))
u0=next(column(P,j) for j in range(3) if any(v!=Z for v in column(P,j)))
u1=next(column(Q,j) for j in range(3) if any(v!=Z for v in column(Q,j)))
u2=None
for j in range(3):
    v=column(Q,j);candidate=tuple(v[i]-u1[i]*dot(u1,v)/dot(u1,u1) for i in range(3))
    if any(x!=Z for x in candidate):u2=candidate;break
assert u2 is not None
basis=(u0,u1,u2);S={(i,j):basis[j][i] for i in range(3) for j in range(3)}
rows=tuple(tuple(S[i,j] for j in range(3)) for i in range(3))
assert rank(rows,Z)==3
inverse_columns=[solve(rows,tuple(A(int(i==j)) for i in range(3)),Z) for j in range(3)]
Sinv={(i,j):inverse_columns[j][i] for i in range(3) for j in range(3)}
clean=lambda M:{key:v for key,v in M.items() if v!=Z}
assert g.mul(Sinv,S)==clean(I)
D=g.mul(g.mul(source.s.adjoint(S),K),S)
assert all(i==j for i,j in D) and all(positive_real(D[i,i]) for i in range(3))
Pstrand=g.mul(g.mul(Sinv,P),S);Cstrand=g.mul(g.mul(Sinv,C),S)
assert Pstrand=={(0,0):O}
assert g.mul(g.mul(Cstrand,Cstrand),Cstrand)==clean(I)
assert g.mul(source.s.adjoint(Cstrand),D)!=g.mul(D,g.mul(Cstrand,Cstrand))
assert any(sum((i,j) in Cstrand for i in range(3))>1 for j in range(3))

def apply(M,v):return tuple(sum((M.get((i,j),Z)*v[j] for j in range(3)),Z) for i in range(3))

imaginary=A(tuple(F(int(i==8)) for i in range(16)))
field={edge:tuple(A(((k+2)*(j+3))%7)+imaginary*A(((k+1)**(j+1))%11) for j in range(3)) for k,edge in enumerate(EDGES)}
encoded={edge:apply(Sinv,v) for edge,v in field.items()}
assert {edge:apply(S,v) for edge,v in encoded.items()}==field
field_norm=sum((dot(v,v) for v in field.values()),Z)
strand_norm=sum((sum((conj(v[i])*D[i,i]*v[i] for i in range(3)),Z) for v in encoded.values()),Z)
assert field_norm==strand_norm
for edge in EDGES:
    assert apply(S,apply(Pstrand,encoded[edge]))==apply(P,field[edge])
    assert apply(S,apply(Cstrand,encoded[edge]))==apply(C,field[edge])
mean=lambda values:tuple(sum((v[i] for v in values.values()),Z)/12 for i in range(3))
assert apply(S,mean(encoded))==mean(field) # G still averages each component over arrows.
# No normalization square roots are needed; D retains the exact positive weights.
# A projector-preserving unitary can mix the two helix amplitudes continuously.
mixing=None
for coefficient in (2,3):
    v=(Z,O,A(coefficient));norm=sum((conj(v[i])*D[i,i]*v[i] for i in range(3)),Z)
    T={key:I[key]-A(2)*v[key[0]]*conj(v[key[1]])*D[key[1],key[1]]/norm for key in I}
    if any(sum(T[i,j]!=Z for i in range(3))>1 for j in range(3)):mixing=T;break
assert mixing is not None
assert g.mul(g.mul(source.s.adjoint(mixing),D),mixing)==D
assert g.mul(mixing,Pstrand)==g.mul(Pstrand,mixing)
# Geometry: h(t)=(R cos(2 pi t),R sin(2 pi t),pitch*t).
# Components 1 and 2 have opposite handedness AND opposite axial motion.
strands=({'component':0,'sector':'P','radius':2,'pitch':2},
         {'component':1,'sector':'Q-first','radius':1,'pitch':1},
         {'component':2,'sector':'Q-second','radius':3,'pitch':-1})
assert strands[1]['pitch']*strands[2]['pitch']<0
assert sorted(s['radius'] for s in strands)==[1,2,3]
# Disjointness for ALL real parameters follows from the distinct fixed radii.
# Exact phase samples for the twelve labelled channels, not floating geometry.
sqrt3=A(tuple(F(int(i==2)) for i in range(16)))
cs=[O,sqrt3/2,O/2,Z,-O/2,-sqrt3/2,-O,-sqrt3/2,-O/2,Z,O/2,sqrt3/2]
sn=[Z,O/2,sqrt3/2,O,sqrt3/2,O/2,Z,-O/2,-sqrt3/2,-O,-sqrt3/2,-O/2]
samples={}
for k,edge in enumerate(EDGES):
    for strand in strands:
        R,p=strand['radius'],strand['pitch'];point=(R*cs[k],R*sn[k],A(F(p*k,12)))
        assert point[0]*point[0]+point[1]*point[1]==A(R*R)
        samples[edge,strand['component']]=point
assert len(samples)==36 and len(set(tuple(v.c for v in point) for point in samples.values()))==36
# Independently generate the canonical tetrahedron's proper rotations.
vertices=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def integer_apply(M,v):return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))
rotations=[]
for p in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        if parity(p)*math.prod(signs)!=1:continue
        M=tuple(tuple(signs[i]*int(j==p[i]) for j in range(3)) for i in range(3))
        images=tuple(integer_apply(M,v) for v in vertices)
        if set(images)!=set(vertices):continue
        action=tuple(vertices.index(v) for v in images);assert parity(action)==1
        rotations.append((M,action))
assert len(rotations)==12
# At t=0 the inner helix contains (1,0,0). Every rotation preserves its norm.
# Among all three helices, the ONLY point of norm one is that point:
# radius 1 gives norm^2=1+t^2, while the other radii already exceed 1.
# Thus an ambient symmetry must fix it. Exactly I and half-turn about x do.
possible=[M for M,_ in rotations if integer_apply(M,(1,0,0))==(1,0,0)]
assert len(possible)==2
identity=((1,0,0),(0,1,0),(0,0,1));halfturn=((1,0,0),(0,-1,0),(0,0,-1))
assert set(possible)=={identity,halfturn}
# The half-turn maps h(t) to h(-t), preserving the un-oriented curves but
# reversing their chosen traversal. Check angular and axial tangent parts.
assert integer_apply(halfturn,(0,1,0))==(0,-1,0)
assert integer_apply(halfturn,(0,0,1))==(0,0,-1)
assert [M for M in possible if integer_apply(M,(0,1,0))==(0,1,0) and integer_apply(M,(0,0,1))==(0,0,1)]==[identity]
# Label-covariance remains possible, but it is NOT the ambient spatial action.
for _,p in rotations:
    moved={tuple(p[i] for i in edge):v for edge,v in field.items()}
    moved_encoded={tuple(p[i] for i in edge):v for edge,v in encoded.items()}
    assert {edge:apply(S,v) for edge,v in moved_encoded.items()}==moved
# Separator control: z=0 meets middle helix only at (2,0,0).
# gamma(s)=(2-cos(pi*s),sin(pi*s),0) joins inner/outer points at s=0,1;
# its squared distance from (2,0,0) is identically one, so it avoids the helix.
assert (2-1,0,0)==(1,0,0) and (2+1,0,0)==(3,0,0)
for u in (F(0),F(1,2),F(1),F(2)):
    cos=(1-u*u)/(1+u*u);sin=2*u/(1+u*u)
    assert (2-cos-2)**2+sin*sin==1  # exact points on the bypass arc
sample_keys={tuple(v.c for v in point) for point in samples.values()}
sample_symmetries=[]
for M,_ in rotations:
    image={tuple(sum((A(M[i][j])*point[j] for j in range(3)),Z).c for i in range(3)) for point in samples.values()}
    if image==sample_keys:sample_symmetries.append(M)
assert sample_symmetries==[identity]
report={'schema':'marici.rung12-helix-candidate.v1','status':'pass','strands':strands,
 'directed_edge_labels':12,'complex_amplitude_samples':36,'all_parameter_nonintersection':'distinct fixed radii',
 'opposite_Q_handedness_and_axial_traversal':True,'opposite_angular_traversal':False,
 'middle_helix_is_radially_between':True,'middle_helix_is_a_separating_barrier':False,
 'barrier_counterexample':'gamma(s)=(2-cos(pi*s),sin(pi*s),0); distance to the middle helix intersection at z=0 is 1',
 'exact_field_recovery':True,'coefficient_metric_preserved_with_explicit_weights':True,
 'named_L_G_C_transported_exactly':True,'corner_cycle_is_not_a_pure_strand_permutation':True,
 'tetrahedral_label_covariance_checks':12,'ambient_A4_rotations_preserving_unoriented_curves':2,
 'ambient_A4_rotations_preserving_directed_curves':1,'ambient_A4_rotations_preserving_36_sample_positions':1,'full_A4_spatial_realization':False,
 'basis_convention':'one nonzero P column and Gram-Schmidt on Q columns; not a physically selected complementary basis',
 'diagonal_coefficient_metric':{str(i):D[i,i].record() for i in range(3)},
 'scope':'Explicit labelled field layout, not a faithful geometric realization of all rung-12 symmetries, a physical separator, or an isotope geometry.',
 'prerequisite_replay':log.getvalue()}
out=ROOT/'research/strominger/results/rung12-helix-candidate';out.mkdir(parents=True,exist_ok=True)
# Illustrative SVG only; exact claims above do not depend on this sampled plot.
colors=['#16a085','#2471a3','#d35400']
project=lambda x,y,z:(340+52*(x-.55*y),300-52*(z+.30*y))
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="780" height="650" viewBox="0 0 780 650">',
 '<rect width="780" height="650" fill="white"/>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker></defs>',
 '<text x="25" y="30" font-family="sans-serif" font-size="18">Three-helix layout — NOT a spatial A4 realization</text>',
 '<text x="25" y="55" font-family="sans-serif" font-size="13">Q strands: opposite handedness and axial travel; P helix: radial middle, not a barrier.</text>']
for strand,color in zip(strands,colors):
    R,p=strand['radius'],strand['pitch'];points=[]
    for i in range(481):
        t=-2+4*i/480;x,y=project(R*math.cos(2*math.pi*t),R*math.sin(2*math.pi*t),p*t);points.append(f'{x:.3f},{y:.3f}')
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-width="2" opacity="0.8"/>')
    for t in (-.3,.3):
        x1,y1=project(R*math.cos(2*math.pi*t),R*math.sin(2*math.pi*t),p*t)
        t2=t+.045;x2,y2=project(R*math.cos(2*math.pi*t2),R*math.sin(2*math.pi*t2),p*t2)
        parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#222" stroke-width="2" marker-end="url(#arrow)"/>')
    parts.append(f'<text x="560" y="{110+35*strand["component"]}" fill="{color}" font-family="sans-serif" font-size="14">{strand["sector"]}: R={R}, pitch={p}</text>')
parts+=['<text x="25" y="620" font-family="sans-serif" font-size="13">Metric preservation refers to complex amplitudes with retained weights, not distances in this drawing.</text>','</svg>']
(out/'helix-layout.svg').write_text('\n'.join(parts)+'\n',encoding='utf8')
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v3.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))['geometric_candidates']['three_helix_layout']
assert atlas['exact_labelled_field_encoding'] and atlas['coefficient_metric_preserved']
assert not atlas['full_A4_as_ambient_rotations'] and not atlas['middle_helix_is_separating_barrier']
paths=[Path(__file__),Path(source.__file__),atlas_path,ROOT/'research/strominger/rung12-helix-candidate-v1.md']
report['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prerequisite_replay','sourceHashes')},indent=2))
