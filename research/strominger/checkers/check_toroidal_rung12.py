"""Exact decorated triangular-torus model of the candidate rung-12 field.
Spatial quotient only: no realization-origin quotient or physical torus claim.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import contextlib,io,json,hashlib
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):
    import check_rung_automorphism_classification as source
    import check_field_36_to_137_refibration as tower
from field_refibration import EDGES,encode,recover,relabel
A,Z,O=source.A,source.Z,source.O;g=source.g;s=source.s
V=((0,0),(1,0),(0,1),(1,1));directions=((1,0),(-1,1),(0,-1))
R=((-1,-1),(1,0))
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
neg=lambda x:tuple(-a for a in x)
mod=lambda x:tuple(a%2 for a in x)
rotate=lambda x:(-x[0]-x[1],x[0])
def power(x,k):
    for _ in range(k):x=rotate(x)
    return x
assert all(power(v,3)==v for v in ((1,0),(0,1)))
assert tuple(rotate(v) for v in directions)==directions[1:]+directions[:1]
# Twice the triangular-lattice metric, avoiding irrational coordinates.
metric=lambda x,y:2*x[0]*y[0]+x[0]*y[1]+x[1]*y[0]+2*x[1]*y[1]
assert all(metric(rotate(x),rotate(y))==metric(x,y) for x in V for y in V)
arrows=tuple((u,k) for u in V for k in range(3))
end=lambda edge:mod(add(edge[0],directions[edge[1]]))
labels={edge:(V.index(edge[0]),V.index(end(edge))) for edge in arrows}
assert len(set(labels.values()))==12 and set(labels.values())==set(EDGES)
# Semidirect-product affine maps x -> R^k x + t, modulo 2 Lambda.
actions={};edge_actions={}
for t in V:
    for k in range(3):
        p=tuple(V.index(mod(add(power(u,k),t))) for u in V)
        assert sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0
        actions[t,k]=p
        moved={e:(mod(add(power(e[0],k),t)),(e[1]+k)%3) for e in arrows}
        assert all(labels[moved[e]]==tuple(p[x] for x in labels[e]) for e in arrows)
        edge_actions[t,k]=moved
assert len(set(actions.values()))==12 and set(actions.values())==set(g.U)
for (t,k),p in actions.items():
    for (u,j),q in actions.items():
        composite=(mod(add(t,power(u,k))),(k+j)%3)
        assert actions[composite]==tuple(p[q[i]] for i in range(4))
# A4 acts freely and transitively on the twelve directed channels.
assert all(len({m[e] for m in edge_actions.values()})==12 for e in arrows)
assert sum(p[0]==0 and p[1]==1 for p in actions.values())==1
# Exact toroidal cell complex: distinct parallel edges must not be merged.
b1=[[F(0) for _ in arrows] for _ in V];b2=[[F(0) for _ in range(8)] for _ in arrows]
for j,e in enumerate(arrows):b1[V.index(e[0])][j]-=1;b1[V.index(end(e))][j]+=1
faces=[]
for u in V:
    x=add(u,(1,0));y=add(u,(0,1));z=add(u,(1,1))
    for tri in ((u,x,y),(x,z,y)):
        boundary=[]
        for v,w in zip(tri,tri[1:]+tri[:1]):
            step=tuple(b-a for a,b in zip(v,w))
            if step in directions:e=(mod(v),directions.index(step));sign=1
            else:e=(mod(w),directions.index(neg(step)));sign=-1
            boundary.append((arrows.index(e),sign));b2[arrows.index(e)][len(faces)]+=sign
        faces.append({'lifted_vertices':tri,'boundary':boundary})
assert all(sum(b1[i][k]*b2[k][j] for k in range(12))==0 for i in range(4) for j in range(8))
assert all(sum(abs(v) for v in row)==2 for row in b2)
def rank(rows):
    rows=[list(map(F,row)) for row in rows];r=0
    for col in range(len(rows[0])):
        pivot=next((i for i in range(r,len(rows)) if rows[i][col]),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r];value=rows[r][col];rows[r]=[v/value for v in rows[r]]
        for i in range(len(rows)):
            if i!=r:
                value=rows[i][col];rows[i]=[v-value*w for v,w in zip(rows[i],rows[r])]
        r+=1
    return r
face_columns={tuple(b2[i][j] for i in range(12)) for j in range(8)}
assert len(face_columns)==8
for moved in edge_actions.values():
    for j in range(8):
        image=[F(0)]*12
        for i,e in enumerate(arrows):image[arrows.index(moved[e])]=b2[i][j]
        assert tuple(image) in face_columns
assert rank(b1)==3 and rank(b2)==7
assert [4-rank(b1),12-rank(b1)-rank(b2),8-rank(b2)]==[1,2,1]
assert all(sum(set(labels[e])==set(pair) for e in arrows)==2 for pair in combinations(range(4),2))
# Return along the other directed channel is NOT reversal of the same lifted
# torus edge: two successive +d steps carry a nonzero 2d deck translation.
deck_loops=[]
for e in arrows:
    back=(end(e),e[1]);assert labels[back]==labels[e][::-1]
    lift=add(directions[e[1]],directions[back[1]]);assert lift!=(0,0) and mod(lift)==(0,0)
    deck_loops.append({'arrow':labels[e],'return_arrow':labels[back],'lifted_displacement':lift})
# Relabel corner triples, retaining the source's actual fiber metric and ops.
index={e:[source.labels.index('ABCD'[labels[e][0]]+'ABCD'[labels[e][1]]+':'+axis) for axis in 'xyz'] for e in arrows}
Ktor={(index[e][i],index[e][j]):value for e in arrows for (i,j),value in source.K.items() if value!=Z}
Ltor={(index[e][i],index[e][j]):value for e in arrows for (i,j),value in source.P.items() if value!=Z}
Ctor={(index[e][i],index[e][j]):value for e in arrows for (i,j),value in source.C.items() if value!=Z}
Gtor={(index[e][i],index[f][i]):O/12 for e in arrows for f in arrows for i in range(3)}
assert Ktor==s.K and Ltor==source.Lp and Gtor==source.Gp and Ctor==s.sourceCycle
assert g.mul(Ctor,g.mul(Ctor,Ctor))==s.I
exact_squares=0
for key,p in actions.items():
    moved=edge_actions[key]
    U={(index[moved[e]][i],index[e][i]):O for e in arrows for i in range(3)}
    assert U==s.sourceActions[p]
    assert g.mul(g.mul(s.adjoint(U),Ktor),U)==Ktor
    for named in (Ltor,Gtor,Ctor):assert g.mul(U,named)==g.mul(named,U)
    assert g.mul(s.targetActions[p],s.B)==g.mul(s.B,U)
    exact_squares+=1
spatial=s.sourceActions[actions[((0,0),1)]]
assert spatial!=Ctor
assert g.mul(g.mul(s.adjoint(Ctor),Ktor),Ctor)!=Ktor
# Distinguish the chosen subgroup from the full tessellation symmetry.
# Sixty-degree rotation maps a positive directed channel to a negative one;
# it preserves the unoriented triangular lattice, not this arrow orientation.
sixty=lambda v:(-v[1],v[0]+v[1])
assert all(sixty(v) not in directions for v in directions)
assert all(mod(neg(u))==u for u in V) # inversion invisible on vertex classes
assert neg((1,0))!=(1,0)             # but not on lifted positions/directions
# Original ordered-parent comparison protocol, not the eight torus faces.
field={edge:tuple(A((i+1)*(j+2)) for j in range(3)) for i,edge in enumerate(EDGES)}
torus_field={e:field[labels[e]] for e in arrows}
restored={labels[e]:v for e,v in torus_field.items()};assert restored==field
comparison_squares=0
for reference in EDGES:
    packet=encode(restored,reference,tower.owner)
    assert len(packet.slots)==137 and recover(packet,tower.owner)==field
    for p in actions.values():
        moved={tuple(p[x] for x in e):v for e,v in field.items()}
        assert relabel(packet,p)==encode(moved,tuple(p[x] for x in reference),tower.owner)
        comparison_squares+=1
report={'schema':'marici.toroidal-rung12.v1','status':'pass',
 'vertex_classes':V,'directions':directions,'rotation_matrix':R,
 'channels':[{'start':e[0],'direction':directions[e[1]],'end':end(e),'field_edge':labels[e]} for e in arrows],
 'A4_elements':[{'translation':t,'rotation_power':k,'vertex_permutation':p} for (t,k),p in actions.items()],
 'group_products_checked':144,'oriented_face_images_checked':96,'field_equivariance_squares':exact_squares,'comparison_equivariance_squares':comparison_squares,
 'cell_complex':{'vertices':4,'edges':12,'faces':8,'boundary_ranks':[3,7],'betti_numbers':[1,2,1],'faces_data':faces},
 'deck_loops':deck_loops,
 'metric_and_L_G_C_preserved':True,'metric_and_internal_operators_derived_from_flat_torus':False,
 'spatial_C3_equals_internal_corner_cycle':False,'fixed_directed_reference_A4_stabilizer_order':1,
 'torus_faces_implement_137_comparison_slots':False,'realization_origins_quotiented':False,
 'scope':'Exact A4-equivariant decorated field encoding on the triangular torus; not a tetrahedral cell-complex isomorphism, native isotope geometry, helix/separator proof or physical torus.',
 'prerequisite_replay':log.getvalue()}
out=ROOT/'research/strominger/results/toroidal-rung12';out.mkdir(parents=True,exist_ok=True)
paths=[Path(__file__),Path(source.__file__),Path(tower.__file__),ROOT/'research/strominger/toroidal-rung12-v1.md']
paths += [ROOT/'research/strominger/results'/name/'verification.json' for name in ('rung-automorphism-classification','field-36-to-137-refibration','rotation-realization-square')]
report['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
# Fundamental parallelogram; boundary copies carry equal class labels.
xy=lambda u:(100+180*u[0]+90*u[1],430-156*u[1])
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="850" height="540" viewBox="0 0 850 540">','<rect width="850" height="540" fill="white"/>','<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#333"/></marker></defs>','<text x="25" y="28" font-family="sans-serif" font-size="18">Triangular torus: four vertex classes, twelve directed channels</text>']
for face in faces:
    svg.append(f'<polygon points="{" ".join(f"{xy(u)[0]},{xy(u)[1]}" for u in face["lifted_vertices"])}" fill="#eaf2f8" stroke="#aaa"/>')
for i,j in product(range(2),repeat=2):
    for u,v in (((i,j),(i+1,j)),((i+1,j),(i,j+1)),((i,j+1),(i,j))):
        p,q=xy(u),xy(v);start=tuple(.88*x+.12*y for x,y in zip(p,q));endp=tuple(.12*x+.88*y for x,y in zip(p,q))
        svg.append(f'<path d="M{start[0]},{start[1]} L{endp[0]},{endp[1]}" stroke="#333" stroke-width="2" marker-end="url(#a)"/>')
colors=['#2471a3','#148f77','#d35400','#8e44ad']
for i,j in product(range(3),repeat=2):
    u=(i,j);k=V.index(mod(u));x,y=xy(u)
    svg.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{colors[k]}"/><text x="{x+11}" y="{y-9}" font-family="sans-serif" font-size="16">{"ABCD"[k]} {mod(u)}</text>')
svg.extend(['<text x="25" y="490" font-family="sans-serif" font-size="14">Opposite boundaries identified spatially; field metric and named operators retained as decorations.</text>','<text x="25" y="515" font-family="sans-serif" font-size="14">No realization-history quotient. Eight faces are not the 137 ordered comparison slots.</text>','</svg>'])
(out/'torus-channels.svg').write_text('\n'.join(svg)+'\n')
print(json.dumps({k:report[k] for k in ('status','group_products_checked','field_equivariance_squares','comparison_equivariance_squares','metric_and_L_G_C_preserved','metric_and_internal_operators_derived_from_flat_torus','spatial_C3_equals_internal_corner_cycle')},indent=2))
