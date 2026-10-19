"""Explicit b=2 toroidal-map realizations and comparison with the field map B.
Primal tetrahedron; collapsed dual tetrahedron; faithful dual cube/Petrie map.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations,permutations
import contextlib,io,json,hashlib
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):import check_toroidal_rung12 as torus
source=torus.source;s=source.s;g=source.g;geo=s.r.geo;A,Z,O=source.A,source.Z,source.O
V=torus.V;labels='ABCD';arrows=torus.arrows;faces=torus.faces
phi=[tuple(F(v) for v in ((-1)**a,(-1)**b,(-1)**(a+b))) for a,b in V]
minus=lambda v:tuple(-x for x in v)
assert all(geo.dot(geo.sub(x,y),geo.sub(x,y))==8 for x,y in combinations(phi,2))
assert geo.mean(phi)==(0,0,0)
H=((F(0),F(1),F(0)),(F(1),F(0),F(0)),(F(0),F(0),F(1)))
assert geo.det(H)==-1
assert all(geo.mv(H,phi[i])==geo.POINTS[labels[i]] for i in range(4))
face_vertices=[tuple(V.index(torus.mod(v)) for v in face['lifted_vertices']) for face in faces]
missing=[next(iter(set(range(4))-set(vs))) for vs in face_vertices]
face_sign=[face['boundary'][0][1] for face in faces]
assert all(all(sign==face_sign[j] for _,sign in face['boundary']) for j,face in enumerate(faces))
assert all(missing.count(i)==2 for i in range(4))
left={};right={}
for j,face in enumerate(faces):
    for e,sign in face['boundary']:(left if sign==1 else right)[e]=j
assert len(left)==len(right)==12
# Primal centroid-edge sectors: choose the already declared left face, not a
# fitted per-channel face. All twelve reproduce the source patch declarations.
Bphi={};Bwrong={};Bdual={};J={}
def block(M,idx,X):
    for i in range(3):
        for j in range(3):
            if X[i][j]:M[idx[i],idx[j]]=A(X[i][j])
for e,arrow in enumerate(arrows):
    a,b=torus.labels[arrow];idx=torus.index[arrow];left_vertices=face_vertices[left[e]]
    expected=s.r.patches[labels[a]+labels[b]]['surfaceTriangle']
    assert expected==['F_'+''.join(labels[i] for i in sorted(left_vertices)),labels[a],labels[b]]
    centroid=geo.mean([phi[i] for i in left_vertices])
    X=geo.transpose((centroid,phi[a],phi[b]));assert geo.det(X)!=0
    block(Bphi,idx,X);block(J,idx,H)
    wrong=geo.transpose((geo.mean([phi[i] for i in face_vertices[right[e]]]),phi[a],phi[b]))
    block(Bwrong,idx,geo.mm(H,wrong))
Brealized=g.mul(J,Bphi)
assert Brealized==s.B
assert g.mul(s.adjoint(Bphi),Bphi)==s.K
assert Bwrong!=s.B and g.mul(Bwrong,source.Lp)!=g.mul(g.L,Bwrong)
# Derive the local projector from the realized sector and the supplied positive
# cyclic Fourier line, rather than merely reusing its matrix entries.
mode=(O,source.omega,source.omega*source.omega);derivedL={}
for arrow in arrows:
    idx=torus.index[arrow]
    value=tuple(sum((Brealized.get((idx[i],idx[j]),Z)*mode[j] for j in range(3)),Z) for i in range(3))
    norm=sum((x.flip(8)*x for x in value),Z)
    for i in range(3):
        for j in range(3):
            x=value[i]*value[j].flip(8)/norm
            if x!=Z:derivedL[idx[i],idx[j]]=x
assert derivedL==g.L
assert g.scale(O/12,g.add(*s.targetActions.values()))==g.G
assert g.mul(s.B,s.sourceCycle)==g.mul(s.r.cycleP,s.B)
# The eight dual vertices are the eight primal faces. Two alternative maps:
# - collapsed dual tetrahedron, two-to-one;
# - cube vertices, injective, with four skew hexagonal (Petrie) faces.
dual_tetra=[minus(phi[m]) for m in missing]
cube=[tuple(face_sign[j]*v for v in phi[missing[j]]) for j in range(8)]
assert len(set(dual_tetra))==4 and len(set(cube))==8
assert set(cube)==set(product((F(-1),F(1)),repeat=3))
for label in range(4):
    i,j=[f for f in range(8) if missing[f]==label]
    assert cube[i]==minus(cube[j])
    assert dual_tetra[i]==dual_tetra[j] and dual_tetra[i]!=(0,0,0)
    # A linear map cannot send antipodal vectors to the same nonzero vector.
for j,vs in enumerate(face_vertices):
    assert dual_tetra[j]==tuple(3*x for x in geo.mean([phi[i] for i in vs]))
dual_edges=[(left[e],right[e]) for e in range(12)]
assert len({frozenset(e) for e in dual_edges})==12
assert all(sum(x!=y for x,y in zip(cube[i],cube[j]))==1 for i,j in dual_edges)
# Recover each hexagonal face of the abstract dual from incidence, not a drawing.
hexagons=[]
for vertex in range(4):
    incident={j for j,vs in enumerate(face_vertices) if vertex in vs};assert len(incident)==6
    adj={j:set() for j in incident}
    for e,(i,j) in enumerate(dual_edges):
        if vertex in torus.labels[arrows[e]]:adj[i].add(j);adj[j].add(i)
    assert all(len(v)==2 for v in adj.values())
    path=[min(incident)];previous=None
    while len(path)<6:
        nxt=min(adj[path[-1]]-({previous} if previous is not None else set()))
        assert nxt not in path;previous=path[-1];path.append(nxt)
    assert path[0] in adj[path[-1]] and set(path)==incident
    sequence=[missing[j] for j in path];assert sequence[:3]==sequence[3:]
    assert geo.mean([cube[j] for j in path])==(0,0,0)
    assert geo.mean([dual_tetra[j] for j in path])==tuple(x/3 for x in phi[vertex])
    # Not a planar regular hexagon: all four-point differences span R^3.
    diffs=[geo.sub(cube[j],cube[path[0]]) for j in path[1:]]
    assert any(geo.det(rows)!=0 for rows in combinations(diffs,3))
    hexagons.append(path)
# Dual channel bijection via left-face -> right-face. This is not a relabelling
# of the primal endpoints, even though it is a bijection of twelve channels.
dual_map={};D={};cube_frame_ranks=[]
for e,arrow in enumerate(arrows):
    a,b=torus.labels[arrow];u,v=missing[left[e]],missing[right[e]]
    dual_map[a,b]=(u,v)
    assert {a,b,u,v}==set(range(4))
    target_arrow=next(x for x in arrows if torus.labels[x]==(u,v));target_idx=torus.index[target_arrow]
    assert s.r.patches[labels[u]+labels[v]]['surfaceTriangle'][0]=='F_'+''.join(labels[i] for i in range(4) if i!=a)
    # Face around primal vertex a; mean six collapsed vertices equals mean
    # the three distinct dual-tetra vertices. Same normalization as the primal.
    dual_centroid=geo.mean([dual_tetra[j] for j in hexagons[a]])
    X=geo.transpose((dual_centroid,dual_tetra[left[e]],dual_tetra[right[e]]))
    block(Bdual,target_idx,X)
    for i in range(3):D[target_idx[i],torus.index[arrow][i]]=O
    Y=geo.transpose(((F(0),)*3,cube[left[e]],cube[right[e]]))
    assert geo.det(Y)==0 and geo.cross(cube[left[e]],cube[right[e]])!=(0,0,0)
    cube_frame_ranks.append(2)
assert len(set(dual_map.values()))==12
assert g.mul(J,Bdual)==g.scale(A(-1),s.B)
assert g.mul(s.adjoint(Bdual),Bdual)==s.K
assert all(dual_map[dual_map[e]]==e for e in dual_map)
assert not any(all(dual_map[e]==tuple(p[i] for i in e) for e in dual_map) for p in permutations(range(4)))
for named in (source.Lp,source.Gp,s.sourceCycle):assert g.mul(D,named)==g.mul(named,D)
assert g.mul(g.mul(s.adjoint(D),s.K),D)==s.K
for p,U in s.sourceActions.items():assert g.mul(D,U)==g.mul(U,D)
# Full unoriented torus group: four translations times D6. Its action on
# vertices has kernel two; its dual cube realization is faithful.
def compose2(M,N):return tuple(tuple(sum(M[i][k]*N[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def apply2(M,v):return tuple(sum(M[i][j]*v[j] for j in range(2)) for i in range(2))
def facekey(vs):
    shift=tuple(2*(min(v[i] for v in vs)//2) for i in range(2))
    return tuple(sorted(tuple(v[i]-shift[i] for i in range(2)) for v in vs))
face_keys={facekey(face['lifted_vertices']):j for j,face in enumerate(faces)}
S=((0,-1),(1,1));reflection=((0,1),(1,0));I2=((1,0),(0,1));linear=[];power=I2
for k in range(6):linear.extend([power,compose2(power,reflection)]);power=compose2(S,power)
assert len(set(linear))==12 and power==I2
vertex_actions=[];face_actions=[];cube_actions=[]
for M in linear:
    for t in V:
        vp=tuple(V.index(torus.mod(torus.add(apply2(M,v),t))) for v in V)
        fp=tuple(face_keys[facekey([torus.add(apply2(M,v),t) for v in face['lifted_vertices']])] for face in faces)
        assert all(missing[fp[j]]==vp[missing[j]] for j in range(8))
        flips={face_sign[fp[j]]*face_sign[j] for j in range(8)};assert len(flips)==1;flip=flips.pop()
        Rphi=geo.mm(geo.transpose(tuple(phi[vp[i]] for i in range(3))),geo.inv(geo.transpose(tuple(phi[i] for i in range(3)))))
        U=tuple(tuple(flip*x for x in row) for row in Rphi)
        assert geo.mm(geo.transpose(U),U)==geo.I
        assert all(geo.mv(U,cube[j])==cube[fp[j]] for j in range(8))
        assert all(geo.mv(Rphi,dual_tetra[j])==dual_tetra[fp[j]] for j in range(8))
        vertex_actions.append(vp);face_actions.append(fp);cube_actions.append(U)
assert len(vertex_actions)==48 and len(set(vertex_actions))==24
assert sum(p==(0,1,2,3) for p in vertex_actions)==2
assert len(set(face_actions))==48 and len(set(cube_actions))==48
report={'schema':'marici.toroidal-tetrahedral-realizations.v1','status':'pass',
 'primal_vertices':phi,'native_coordinate_identification':H,'coordinate_identification_determinant':-1,
 'primal_left_face_sectors_match_B':True,'metric_recovered_from_realized_sectors':True,
 'L_recovered_with_declared_positive_cyclic_mode':True,'G_recovered_from_proper_group_average':True,
 'wrong_right_face_choice_rejected':True,
 'full_map_group_order':48,'tetrahedral_vertex_image_order':24,'vertex_action_kernel_order':2,
 'dual_tetrahedron_vertices':dual_tetra,'dual_cube_vertices':cube,'dual_hexagon_cycles':hexagons,
 'dual_cube_is_faithful':True,'dual_cube_geometric_group_order':48,
 'dual_tetrahedron_vertex_map_is_two_to_one':True,'dual_tetrahedron_B_in_common_coordinates':'-B',
 'dual_cube_centroid_edge_frame_ranks':cube_frame_ranks,
 'edge_duality':[{'primal':e,'dual':f} for e,f in dual_map.items()],
 'edge_duality_preserves_metric_L_G_C_and_A4':True,'edge_duality_preserves_primal_source_fibers':False,
 'scope':'Explicit realizations of {3,6}_{(2,0)} and its dual; field-frame comparison. Coordinate equivalences and geometric collapses, not native mirror/PN laws, isotope assignments or helix/separator evidence.',
 'prerequisite_replay':log.getvalue()}
out=ROOT/'research/strominger/results/toroidal-tetrahedral-realizations';out.mkdir(parents=True,exist_ok=True)
paths=[Path(__file__),Path(torus.__file__),ROOT/'research/strominger/toroidal-tetrahedral-realizations-v1.md',ROOT/'references/realizations-of-regular-toroidal-maps.pdf',ROOT/'research/strominger/results/toroidal-rung12/verification.json']
report['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def serialize(v):
    if isinstance(v,F):return str(v)
    raise TypeError(type(v))
(out/'verification.json').write_text(json.dumps(report,indent=2,default=serialize)+'\n')
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="550" viewBox="0 0 1000 550">','<rect width="1000" height="550" fill="white"/>','<text x="25" y="30" font-family="sans-serif" font-size="19">Two distinct dual realizations: geometric collapse versus cube/Petrie map</text>']
def xy(v,offset):return (offset+110*float(v[0]+F(2,5)*v[2]),270-110*float(v[1]+F(1,4)*v[2]))
for points,color in ((phi,'#2471a3'),([minus(v) for v in phi],'#d35400')):
    for u,v in combinations(points,2):
        a,b=xy(u,250),xy(v,250);svg.append(f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="{color}" stroke-width="2"/>')
for i,j in dual_edges:
    a,b=xy(cube[i],750),xy(cube[j],750);svg.append(f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="#aaa" stroke-width="2"/>')
cycle=hexagons[0]+[hexagons[0][0]]
svg.append(f'<polyline points="{" ".join(f"{xy(cube[i],750)[0]},{xy(cube[i],750)[1]}" for i in cycle)}" fill="none" stroke="#8e44ad" stroke-width="3"/>')
svg.extend(['<text x="55" y="465" font-family="sans-serif" font-size="15">Primal and collapsed dual: stella octangula</text>','<text x="555" y="465" font-family="sans-serif" font-size="15">Faithful dual: cube edges, one skew hexagon</text>','<text x="25" y="510" font-family="sans-serif" font-size="14">Left recovers the field frames up to sign. Right has zero hexagon centroids: the same frame recipe is singular.</text>','</svg>'])
(out/'primal-and-dual.svg').write_text('\n'.join(svg)+'\n')
print(json.dumps({k:report[k] for k in ('status','primal_left_face_sectors_match_B','metric_recovered_from_realized_sectors','full_map_group_order','tetrahedral_vertex_image_order','dual_cube_is_faithful','dual_tetrahedron_B_in_common_coordinates','edge_duality_preserves_primal_source_fibers')},indent=2))
