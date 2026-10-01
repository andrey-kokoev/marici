"""Finite Machian body -> source-selected eigenlines -> body calculation.

Inputs: four labelled seed states, the two seed cycles, the counting inner
product on state records, and positive source weights. Trial response law:
follow the lowest eigenline of the rest-of-body source on the contrast space.
No independent spatial atlas is supplied. No mass/force normalization is fit.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json


def mm(a,b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
                       for j in range(len(b[0]))) for i in range(len(a)))
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c): return tuple(tuple(c*x for x in r) for r in a)
def tr(a): return sum(a[i][i] for i in range(len(a)))
def trans(a): return tuple(zip(*a))
def compose(p,q): return tuple(p[q[i]] for i in range(4))
def parity(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
# Exact Q(sqrt(2)) for the perturbed eigenprojectors and oriented volume.
def qa(x,y): return (x[0]+y[0],x[1]+y[1])
def qm(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qs(x,c): return (c*x[0],c*x[1])
def positive(x):
    a,b=x
    if a>=0 and b>=0: return a>0 or b>0
    if a<=0 and b<=0: return False
    return a*a>2*b*b if a>=0 else 2*b*b>a*a

def qdet(a):
    total=(F(0),F(0));n=len(a)
    for p in permutations(range(n)):
        term=(F(parity(p)),F(0))
        for i in range(n): term=qm(term,a[i][p[i]])
        total=qa(total,term)
    return total

def fmt(x): return f'{x[0]} + ({x[1]})*sqrt(2)'


def main():
    I=tuple(tuple(F(i==j) for j in range(4)) for i in range(4))
    group={(0,1,2,3)};front=list(group)
    while front:
        p=front.pop()
        for g in ((1,2,0,3),(3,0,2,1)):
            q=compose(g,p)
            if q not in group: group.add(q);front.append(q)
    assert len(group)==12
    E=tuple(tuple(F(sum(p[j]==i for p in group),12) for j in range(4)) for i in range(4))
    assert E==tuple(tuple(F(1,4) for _ in range(4)) for _ in range(4))
    H=add(I,scale(E,-1));assert mm(H,H)==H and tr(H)==3
    # Body points q_p=H e_p in the intrinsic three-dimensional contrast space.
    points=trans(H)
    P=[]
    for q in points:
        assert sum(q)==0 and sum(x*x for x in q)==F(3,4)
        P.append(tuple(tuple(F(4,3)*x*y for y in q) for x in q))
    S=tuple(tuple(sum(p[i][j] for p in P) for j in range(4)) for i in range(4))
    assert S==scale(H,F(4,3))
    zero=scale(I,0)
    base_sources=[]
    for p in range(4):
        K=add(S,scale(P[p],-1));base_sources.append(K)
        assert mm(K,P[p])==scale(P[p],F(1,3))
        assert mm(K,add(H,scale(P[p],-1)))==scale(add(H,scale(P[p],-1)),F(4,3))
        recovered=add(scale(H,F(4,3)),scale(K,-1))
        assert recovered==P[p] and mm(recovered,recovered)==recovered
        assert tuple(recovered[i][p] for i in range(4))==points[p]
    # Adapter audit: all remote anchors contribute, not just primitive seed
    # edges. Restricting those dependencies to seed incidence changes the law.
    from check_natural_tower_return import PACKETS
    from biclique_complex import rank
    seed_support={(s,t) for _,s,t in PACKETS}
    remote_support={(s,t) for s in 'ABCD' for t in 'ABCD' if s!=t}
    assert len(remote_support)==12 and len(seed_support)==6
    assert seed_support<remote_support
    masked_ranks=[]
    for target in 'ABCD':
        masked=zero
        for source,label in enumerate('ABCD'):
            if (label,target) in seed_support: masked=add(masked,P[source])
        columns=[{i:masked[i][j] for i in range(4) if masked[i][j]} for j in range(4)]
        masked_ranks.append(rank(columns))
    assert masked_ranks==[2,2,1,1]
    # Radial scale is erased BEFORE K is assembled. Retaining every eigenvalue
    # of K cannot recover it: the full K itself is unchanged.
    for factor in (F(2),F(3,2)):
        scaled_points=tuple(tuple(factor*x for x in q) for q in points)
        scaled_P=tuple(tuple(tuple(x*y/sum(z*z for z in q) for y in q) for x in q)
                       for q in scaled_points)
        assert scaled_P==tuple(P)
        for p in range(4):
            scaled_K=zero
            for q in range(4):
                if q!=p: scaled_K=add(scaled_K,scaled_P[q])
            assert scaled_K==base_sources[p]
    print('Adapter audit: all-to-all remote support12 versus seed6; seed-masked source ranks',masked_ranks)
    print('Scale control: full normalized source matrices, hence all their spectral data, are radius-blind.')
    # A metric on the contrast space is obtained directly from the rest's modes.
    # Its determinant there is (1/3)*(4/3)^2=16/27>0.
    source_determinant=F(16,27);assert source_determinant>0
    edges=[tuple(points[j][i]-points[0][i] for i in range(4)) for j in (1,2,3)]
    edge_gram=tuple(tuple(sum(x*y for x,y in zip(a,b)) for b in edges) for a in edges)
    assert edge_gram==((F(2),F(1),F(1)),(F(1),F(2),F(1)),(F(1),F(1),F(2)))
    assert qdet(tuple(tuple((z,F(0)) for z in r) for r in edge_gram))==(F(4),F(0))
    # Original volume is sqrt(det Gram)/6=1/3 in counting-metric units.
    # Perturb only the remote source B: weight 1 -> 2.
    changed=1;new_projectors=[];response=[]
    weights=(F(1),F(2),F(1),F(1))
    weighted_sources=[]
    for p in range(4):
        K=zero
        for q in range(4):
            if q!=p: K=add(K,scale(P[q],weights[q]))
        weighted_sources.append(K)
    source_total=zero
    for K in weighted_sources: source_total=add(source_total,K)
    source_total=scale(source_total,F(1,3))
    for p,K in enumerate(weighted_sources):
        recovered=scale(add(source_total,scale(K,-1)),1/weights[p])
        assert recovered==P[p]
        assert tuple(recovered[i][p] for i in range(4))==points[p]
    for p in range(4):
        if p==changed:
            U=P[p];V=zero
            response.append({'anchor':'ABCD'[p],'lowest_eigenvalue':'1/3','line_changed':False})
        else:
            K=add(base_sources[p],P[changed])
            D=add(P[changed],scale(P[p],-1));D2=mm(D,D)
            assert mm(D2,D)==scale(D,F(8,9)) and tr(D)==0
            assert tr(D2)==F(16,9)
            # Lowest eigenprojector U+sqrt(2)*V; no eigensolver tolerance.
            U=scale(D2,F(9,16));V=scale(D,F(-3,8))
            assert add(mm(U,U),scale(mm(V,V),2))==U
            assert add(mm(U,V),mm(V,U))==V
            assert tr(U)==1 and tr(V)==0
            assert mm(K,U)==add(scale(U,F(4,3)),scale(V,F(-4,3)))
            assert mm(K,V)==add(scale(V,F(4,3)),scale(U,F(-2,3)))
            assert V!=zero
            assert positive((F(4,3),F(-2,3)))
            response.append({'anchor':'ABCD'[p],'lowest_eigenvalue':'(4-2*sqrt(2))/3','line_changed':True})
        new_projectors.append((U,V))
    # Rebuild the body from its selected lines using the retained seed labels:
    # q'_p=P'_p e_p. Labels choose the representative without a spatial atlas.
    newpoints=[tuple((U[i][p],V[i][p]) for i in range(4)) for p,(U,V) in enumerate(new_projectors)]
    assert all(qa(qa(q[0],q[1]),qa(q[2],q[3]))==(F(0),F(0)) for q in newpoints)
    # Add the centroid record to obtain the affine transformation from the old
    # labelled simplex to the new one. Each column sums to one.
    W=tuple(tuple(qa(newpoints[p][i],(F(1,4),F(0))) for p in range(4)) for i in range(4))
    volume_ratio=qdet(W)
    assert positive(volume_ratio)
    volume=qs(volume_ratio,F(1,3))
    assert positive(volume)
    # The three equivalent lighter anchors give two transverse scales and one
    # axial scale about fixed vertex B. Both are positive, so the affine homotopy
    # (1-t)I+tW stays orientation-preserving for every 0<=t<=1.
    a=qa(W[0][0],qs(W[0][2],-1))
    b=qa((F(1),F(0)),qs(W[1][0],-1))
    assert positive(a) and positive(b)
    for p in (0,2,3):
        assert W[1][p]==W[1][0]
        for j in (0,2,3):
            assert W[j][p]==(W[0][0] if j==p else W[0][2])
    assert tuple(W[j][1] for j in range(4))==tuple((F(j==1),F(0)) for j in range(4))
    assert qm(qm(a,a),b)==volume_ratio
    # Explicit twelve-triangle boundary and its twelve positive interior cones.
    faces=((0,1,2),(0,3,1),(0,2,3),(1,3,2))
    # Use the boundary orientation selected by the seed faces ABC and ADB.
    # Barycentric boundary cancellation is unchanged by the affine map W.
    boundary={};triangles=[]
    for face in faces:
        f='F'+''.join(map(str,sorted(face)))
        for i in range(3):
            t=(f,str(face[i]),str(face[(i+1)%3]));triangles.append(t)
            for a,b in zip(t,t[1:]+t[:1]):
                key=tuple(sorted((a,b)));boundary[key]=boundary.get(key,0)+(1 if a<b else -1)
    assert len(triangles)==12 and len(boundary)==18 and all(v==0 for v in boundary.values())
    # Each cone is the affine image of 1/12 of the original simplex volume.
    cone=qs(volume,F(1,12));assert positive(cone)
    assert qs(cone,12)==volume
    # Body -> its collective identity line: null vector of the centered new Gram.
    centre=tuple(qs(qa(qa(newpoints[0][i],newpoints[1][i]),qa(newpoints[2][i],newpoints[3][i])),F(1,4)) for i in range(4))
    centered=[tuple(qa(q[i],qs(centre[i],-1)) for i in range(4)) for q in newpoints]
    gram=[]
    for a in centered:
        row=[]
        for b in centered:
            z=(F(0),F(0))
            for x,y in zip(a,b): z=qa(z,qm(x,y))
            row.append(z)
        gram.append(row)
    for row in gram:
        total=(F(0),F(0))
        for z in row: total=qa(total,z)
        assert total==(F(0),F(0))
    # Positive oriented volume ensures affine independence, so centered Gram
    # has rank 3 and its kernel is exactly the common identity line.
    # Negative control: omitting another source destroys a 3D-positive source metric.
    deficient=add(base_sources[0],scale(P[1],-1))
    assert tr(deficient)==2
    assert qdet(tuple(tuple((deficient[i][j]+E[i][j],F(0)) for j in range(4)) for i in range(4)))==(F(0),F(0))
    result={'audit_assertions_passed':True,
            'inputs':['four labelled states','seed cycles ABC and ADB','counting inner product','positive source weights'],
            'trial_response_rule':'Select the smallest contrast-space eigenline of K_p=sum_{q!=p} w_q P_q; rebuild q_p=P_p e_p.',
            'seed_group_order':12,'collective_identity_projector':'E=J_4/4','contrast_projector':'H=I-E',
            'symmetric_fixed_point':{'source_spectrum_on_contrast':['1/3','4/3','4/3'],
                                     'own_line_recovered_exactly':True,'source_metric_determinant':str(source_determinant),
                                     'positive_body_volume':'1/3'},
            'remote_perturbation':{'weights':[1,2,1,1],'response':response,
                                   'oriented_body_volume_ratio':fmt(volume_ratio),'positive_new_volume':fmt(volume),
                                   'positive_transverse_scale':fmt(a),'positive_axial_scale':fmt(b),
                                   'positive_affine_homotopy':True,
                                   'each_of_12_positive_cone_volumes':fmt(cone),'boundary_cancels':True,
                                   'new_collective_identity_line':'span(1,1,1,1) in centered Gram kernel'},
            'stage_witnesses':{'source_metrics':'positive on contrast space; sum of three positive rank-one sources spanning it',
                               'source_stage_body_decoder':'S=sum_p K_p/3; P_p=(S-K_p)/w_p; q_p=P_p e_p. Exact source body recovery from current stage data.',
                               'eigenline_collection':'explicit Q(sqrt(2)) projectors reconstruct the positive simplex by labelled anchors',
                               'reconstructed_body':'positive affine determinant; twelve positive cones; exact boundary cancellation'},
            'negative_control':'Removing a remote source gives singular local contrast metric.',
            'scope':'Finite source-dependent frame/geometry response. Source weights and eigenline response law are declared inputs. Force law, physical units, iteration stability and total primitive construction-arrow count remain to be calculated.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'machian-thing-eigenline-cycle.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: four-state body -> rest-selected eigenlines -> reconstructed body. Symmetric fixed point exact; doubled remote weight changes three lines; new oriented volume = '+fmt(volume)+'. All twelve cone volumes positive; shared boundary closes.')

if __name__=='__main__': main()
