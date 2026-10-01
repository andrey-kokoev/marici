"""A twelve-triangle tetrahedral surface with transported cyclic eigenlines.

The two seed face rotations generate the twelve proper tetrahedral rotations.
Their orbit of a centroid-edge triangle triangulates the boundary. Exact
arithmetic distinguishes frame-transported alignment from ambient coincidence.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from check_triangle_half_phase import (
    I, mm, mv, transpose, power, zadd, zmul, zconj, zscale,
    znorm, zmv, zmm, zreal,
)

LABELS='ABCD'
POINTS={k:tuple(map(F,v)) for k,v in zip(LABELS,((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)))}
ONE=(F(1),F(0));ZERO=(F(0),F(0));OMEGA=(F(-1,2),F(1,2))
C=((F(0),F(1),F(0)),(F(0),F(0),F(1)),(F(1),F(0),F(0)))


def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(m): return dot(m[0],cross(m[1],m[2]))
def inv(m):
    a=[list(r)+list(I[i]) for i,r in enumerate(m)]
    for j in range(3):
        p=next(i for i in range(j,3) if a[i][j])
        a[j],a[p]=a[p],a[j];v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(3):
            if i!=j:
                c=a[i][j];a[i]=[x-c*y for x,y in zip(a[i],a[j])]
    out=tuple(tuple(r[3:]) for r in a)
    assert mm(m,out)==I
    return out

def compose(p,q): return tuple(p[q[i]] for i in range(4))
def rotation(p):
    old=tuple(POINTS[k] for k in LABELS)
    return tuple(tuple(sum(old[p[k]][i]*old[k][j] for k in range(4))/4 for j in range(3)) for i in range(3))
def mean(vs): return tuple(sum(v[i] for v in vs)/len(vs) for i in range(3))
def projector(v):
    norm=sum(znorm(z) for z in v)
    return tuple(tuple(zscale(zmul(a,zconj(b)),1/norm) for b in v) for a in v)
def boundary(triangles):
    counts=Counter()
    for a,b,c in triangles:
        for u,v in ((a,b),(b,c),(c,a)):
            counts[tuple(sorted((u,v)))]+=1 if u<v else -1
    return {e:n for e,n in counts.items() if n}
def zsum(vs):
    out=[ZERO]*3
    for v in vs:
        out=[zadd(a,b) for a,b in zip(out,v)]
    return tuple(out)


def main():
    # Original two oriented triangles: A->B->C->A and B->A->D->B.
    generators=((1,2,0,3),(3,0,2,1))
    group={(0,1,2,3)};front=list(group)
    while front:
        q=front.pop()
        for g in generators:
            p=compose(g,q)
            if p not in group: group.add(p);front.append(p)
    assert len(group)==12
    points=dict(POINTS)
    for face in combinations(LABELS,3):
        points['F_'+''.join(face)]=mean([POINTS[k] for k in face])
    reference=('F_ABC','A','B')
    X0=transpose(tuple(points[k] for k in reference))
    A0=mm(mm(X0,C),inv(X0))
    coeff=(ONE,OMEGA,zmul(OMEGA,OMEGA))
    v0=zmv(X0,coeff);P0=projector(v0)
    assert power(A0,3)==I
    assert zmv(A0,v0)==tuple(zmul(OMEGA,z) for z in v0)
    triangles=[];vectors=[];projectors=[];normals=[];rows=[];volume=F(0)
    transported=[];transported_projectors=[]
    for p in sorted(group):
        R=rotation(p)
        assert det(R)==1 and mm(transpose(R),R)==I
        for i,k in enumerate(LABELS): assert mv(R,POINTS[k])==POINTS[LABELS[p[i]]]
        a,b,c=(LABELS[p[i]] for i in range(3))
        centre='F_'+''.join(sorted((a,b,c)))
        tri=(centre,a,b);triangles.append(tri)
        X=transpose(tuple(points[k] for k in tri))
        assert X==mm(R,X0)
        u,w=(sub(points[k],points[centre]) for k in (a,b))
        normal=cross(u,w);normals.append(normal)
        assert dot(normal,points[centre])>0
        # Every triangle lies in an outward supporting plane of the convex tetrahedron.
        assert all(dot(normal,sub(q,points[centre]))<=0 for q in points.values())
        cell_volume=det(X)/6
        assert cell_volume==F(2,9);volume+=cell_volume
        v=zmv(X,coeff);P=projector(v);vectors.append(v);projectors.append(P)
        A=mm(mm(X,C),inv(X))
        assert A==mm(mm(R,A0),transpose(R)) and power(A,3)==I
        assert zmv(A,v)==tuple(zmul(OMEGA,z) for z in v)
        assert zmm(P,P)==P
        assert sum(P[i][i][0] for i in range(3))==1
        back=zmv(transpose(R),v);transported.append(back)
        backP=zmm(zmm(zreal(transpose(R)),P),zreal(R))
        transported_projectors.append(backP)
        assert back==v0 and backP==P0
        rows.append({'outer_arrow':a+b,'triangle':list(tri),'rotation':[list(map(str,r)) for r in R],
                     'signed_origin_cone_volume':str(cell_volume),'transported_eigenline_matches':True})
    assert len(set(triangles))==12 and boundary(triangles)=={}
    edges={tuple(sorted((a,b))) for t in triangles for a,b in zip(t,t[1:]+t[:1])}
    directed={(a,b) for t in triangles for a,b in zip(t,t[1:]+t[:1])}
    assert len(points)==8 and len(edges)==18 and len(directed)==36
    assert len(points)-len(edges)+len(triangles)==2
    assert {r['outer_arrow'] for r in rows}=={a+b for a in LABELS for b in LABELS if a!=b}
    assert volume==F(8,3) and tuple(sum(n[i] for n in normals) for i in range(3))==(0,0,0)
    assert len(set(projectors))==12 and len(set(transported_projectors))==1
    assert zsum(vectors)==(ZERO,)*3
    assert tuple(zscale(z,F(1,12)) for z in zsum(transported))==v0
    # Projector alignment alone does not impose relative amplitude phases.
    signed=tuple(tuple(zscale(z,(-1)**i) for z in v) for i,v in enumerate(transported))
    assert zsum(signed)==(ZERO,)*3
    assert all(projector(v)==P0 for v in signed)
    # The coherent assembled mode lives in the direct sum of twelve local spaces.
    assembled=tuple(z for v in vectors for z in v)
    assert sum(znorm(z) for z in assembled)==80
    collective=projector(assembled)
    assert zmm(collective,collective)==collective
    assembled_column=tuple((z,) for z in assembled)
    assert zmm(collective,assembled_column)==assembled_column
    opposite_column=tuple((zscale(z,(-1)**i),) for i,v in enumerate(vectors) for z in v)
    assert zmm(collective,opposite_column)==tuple((ZERO,) for _ in assembled)
    # Symmetry averaging and local mode selection commute. Their intersection
    # is precisely the rank-one assembled identity, not an extra phase tag.
    rotations=[tuple(tuple(F(x) for x in r) for r in row['rotation']) for row in rows]
    blocks=[[mm(R,transpose(S)) for S in rotations] for R in rotations]
    symmetry=tuple(tuple(blocks[i//3][j//3][i%3][j%3]/12 for j in range(36)) for i in range(36))
    local=tuple(tuple(projectors[i//3][i%3][j%3] if i//3==j//3 else ZERO for j in range(36)) for i in range(36))
    assert mm(symmetry,symmetry)==symmetry and sum(symmetry[i][i] for i in range(36))==3
    assert zmm(zreal(symmetry),local)==collective
    assert zmm(local,zreal(symmetry))==collective
    # Explicit THREE-STAGE realization: local selection -> symmetry transport
    # -> dense collective-projector feedback. Stage labels are distinct ports.
    matrices=(local,zreal(symmetry),collective)
    stage_arrows=[]
    for stage,m in enumerate(matrices):
        stage_arrows.append({((stage,i),((stage+1)%3,j)):m[j][i]
                             for i in range(36) for j in range(36) if m[j][i]!=ZERO})
    stage_counts=list(map(len,stage_arrows))
    assert stage_counts==[108,432,1296]
    all_arrows=set().union(*(set(a) for a in stage_arrows))
    assert len(all_arrows)==1836
    assert len({v for e in all_arrows for v in e})==108
    used=set();closed_weight=ZERO;closed_cycles=0
    for closing,z in stage_arrows[2].items():
        k=closing[0][1];i=closing[1][1]
        middle=[b for b in range(36) if ((0,i),(1,b)) in stage_arrows[0]
                and ((1,b),(2,k)) in stage_arrows[1]]
        assert len(middle)==1
        b=middle[0];e0=((0,i),(1,b));e1=((1,b),(2,k))
        weight=zmul(zmul(stage_arrows[0][e0],stage_arrows[1][e1]),z)
        assert weight[1]==0 and weight[0]>0
        closed_weight=zadd(closed_weight,weight);closed_cycles+=1
        used.update((e0,e1,closing))
    assert used==all_arrows and closed_cycles==1296 and closed_weight==ONE
    # Identifying the three stage-port types collapses the union to 1296;
    # dense feedback is a real construction choice, not forced minimality.
    untyped={(a[1],b[1]) for a,b in all_arrows}
    assert len(untyped)==1296
    # Negative controls: an orientation error and a flat realization.
    bad=list(triangles);a,b,c=bad[0];bad[0]=(a,c,b)
    assert len(boundary(bad))==3
    flat={k:(v[0],v[1],F(0)) for k,v in points.items()}
    flat_volume=sum(det(transpose(tuple(flat[k] for k in t)))/6 for t in triangles)
    assert flat_volume==0
    # Barycentric coordinates and canonical simplex density of the enclosed body.
    def barycentric(x): return tuple((1+dot(POINTS[k],x))/4 for k in LABELS)
    assert all(barycentric(POINTS[k])==tuple(F(k==j) for j in LABELS) for k in LABELS)
    assert det(tuple(tuple(x/4 for x in POINTS[k]) for k in 'ABC'))==F(1,16)
    for x in ((F(0),)*3,(F(1,10),F(1,20),F(1,30))):
        lam=barycentric(x)
        assert sum(lam)==1 and all(l>0 for l in lam)
        density=F(1,16)
        for l in lam: density/=l
        assert density>0
    dest=Path(__file__).resolve().parents[1]/'results'
    report={'status':'passed','construction':'A4 orbit of a face-centroid/edge triangle',
            'seed_cycles':['ABC','ADB'],'proper_rotations':len(group),
            'vertices':len(points),'undirected_edges':len(edges),'directed_surface_arrows':len(directed),
            'triangles':len(triangles),'euler_characteristic':2,'boundary_chain_zero':True,
            'positive_volume':str(volume),'supporting_plane_checks':True,
            'ambient_distinct_eigenlines':len(set(projectors)),'transported_distinct_eigenlines':1,
            'ambient_vector_sum_zero':True,'coherent_transported_mean_equals_reference':True,
            'opposite_phase_control_cancels_with_identical_projectors':True,
            'assembled_identity':{'ambient_direct_sum_dimension':36,'rank':1,'formula':'P_new=u u_dagger/80','idempotence_exact':True,
                                  'symmetry_projector_rank':3,'local_mode_projector_rank':12,
                                  'commuting_intersection':'P_new = P_symmetry P_local = P_local P_symmetry'},
            'three_stage_net':{'stages':['local spectral selection','symmetry averaging','dense collective feedback'],
                               'arrows_per_stage':stage_counts,'unique_directed_arrows':len(all_arrows),
                               'port_nodes':108,'closed_three_step_cycles':closed_cycles,
                               'closed_cycle_weights_positive':True,'closed_cycle_weight_sum':'1',
                               'closed_walk_union_covers_every_arrow':True,
                               'cycle_operator':'P_new P_symmetry P_local = P_new',
                               'union_after_identifying_stage_ports':len(untyped),
                               'smaller_identity_wire_feedback_count':108+432+36,
                               'count_convention':'Distinct input/local/symmetry port stages, natural tetrahedral axis basis, dense P_new feedback. Not minimality.'},
            'canonical_form':'16 dx dy dz / product_k(1+v_k dot x), inside lambda_k=(1+v_k dot x)/4 > 0',
            'triangles_and_transports':rows,
            'controls':{'one_flipped_triangle_nonzero_boundary_edges':3,'flat_volume':str(flat_volume)},
            'scope':'Closed convex carrier and collective eigenline derived by local-mode/symmetry projection. Explicit three-stage dense-feedback implementation has 1836 unique arrows. No minimality, phase-locking dynamics, or physical mass claim.'}
    (dest/'twelve-triangle-positive-geometry.json').write_text(json.dumps(report,indent=2)+'\n')
    def port(v):
        stage,i=v
        return (('raw','local','aligned')[stage],rows[i//3]['outer_arrow'],'xyz'[i%3])
    manifest=[]
    for stage,arrows in enumerate(stage_arrows):
        for (src,dst),weight in sorted(arrows.items()):
            manifest.append({'source':port(src),'target':port(dst),
                             'weight_real':str(weight[0]),'weight_imag_sqrt3':str(weight[1])})
    assert len(manifest)==1836
    (dest/'twelve-triangle-1836-arrows.json').write_text(json.dumps(manifest,indent=2)+'\n')
    names=list(points)
    obj=['# Twelve-triangle oriented tetrahedral boundary; exact coordinates in JSON/checker.']
    obj+=['v '+' '.join(str(float(x)) for x in points[k]) for k in names]
    obj+=['f '+' '.join(str(names.index(k)+1) for k in t) for t in triangles]
    (dest/'twelve-triangle-positive-geometry.obj').write_text('\n'.join(obj)+'\n')
    print('PASS: 12 seed-generated triangles; closed positive volume 8/3; collective eigenline; 1836 unique three-stage arrows covering positive closed cycles. Stage typing and dense feedback explicit.')

if __name__=='__main__': main()
