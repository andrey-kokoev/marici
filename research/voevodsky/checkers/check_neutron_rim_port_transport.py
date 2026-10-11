"""Exact port matching, reversible boundary-phase transport, and obstruction
controls. A conditional interface construction, not a binding/flow law.
"""
from fractions import Fraction as Q
from itertools import permutations,combinations
from pathlib import Path
from hashlib import sha256
import json
from assemble_relative_geometry import apply,dot_metric,subtract

BASE=Path(__file__).resolve().parents[1]
ZERO=(Q(0),Q(0));ONE=(Q(1),Q(0));W=(Q(0),Q(1))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def scale(s,a):return (s*a[0],s*a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def conj(a):return (a[0]-a[1],-a[1])
def total(xs):
    out=ZERO
    for x in xs:out=add(out,x)
    return out
def power(n):return (ONE,W,mul(W,W))[n%3]
def norm(a):return mul(a,conj(a))[0]
def encode(x):return [scale(Q(1,3),total(mul(power(-k*i),x[i]) for i in range(3))) for k in range(3)]
def decode(z):return [total(mul(power(k*i),z[k]) for k in range(3)) for i in range(3)]
def mean(points):return tuple(sum(p[i] for p in points)/len(points) for i in range(len(points[0])))
def generators(source):return [(tuple(tuple(map(Q,r)) for r in g['matrix']),tuple(map(Q,g['translation']))) for g in source['generators']]
def d2(a,b,G):return dot_metric(subtract(a,b),subtract(a,b),G)
def source_vertices(d):
    return {**{chr(65+i):tuple(Q(i==j) for j in range(d)) for i in range(d)},chr(65+d):tuple(Q(0) for _ in range(d))}
def group(points,gens):
    labels=tuple(points);inverse={p:k for k,p in points.items()}
    actions=[{k:inverse[apply(g,p)] for k,p in points.items()} for g in gens]
    identity=tuple(labels);seen={identity:[]};todo=[identity]
    while todo:
        p=todo.pop(0)
        for i,g in enumerate(actions):
            q=tuple(g[k] for k in p)
            if q not in seen:seen[q]=seen[p]+[i];todo.append(q)
    return [(dict(zip(labels,p)),word) for p,word in seen.items()]
def small_triangle_mode_norm(center,a,b,G):
    real=subtract(center,mean([a,b]));delta=subtract(a,b)
    return dot_metric(real,real,G)+Q(3,4)*dot_metric(delta,delta,G)


def main():
    paths=[BASE/'inputs/relative-proton.json',BASE/'inputs/relative-electron.json',BASE/'inputs/mode-neutron.json',BASE/'results/four_six_center_cones.json']
    psrc,esrc,nsrc,geometry=[json.loads(p.read_text(encoding='utf-8')) for p in paths]
    P=source_vertices(3);E=source_vertices(4)
    N={k:tuple(map(Q,v)) for k,v in geometry['belt_scaled_coordinates'].items() if k!='O'}
    GP=[[Q(v) for v in r] for r in psrc['metric']];GE=[[Q(v) for v in r] for r in esrc['metric']];GN=[[Q(v) for v in r] for r in nsrc['metric']]
    pg=group(P,generators(psrc));eg=group(E,generators(esrc))
    assert len(pg)==12 and len(eg)==5
    R=generators(nsrc)[0];inverse={v:k for k,v in N.items()}
    nr={k:inverse[apply(R,p)] for k,p in N.items()}
    scale2=Q(8,3);interfaces=[]
    for prefix,points,G,name in [('L',P,GP,'proton.ABC'),('U',E,GE,'electron.ABC_in_ABCD')]:
        rim=[prefix+str(i) for i in range(3)];target=list('ABC')
        raw={d2(N[a],N[b],GN) for a,b in combinations(rim,2)}
        target_lengths={d2(points[a],points[b],G) for a,b in combinations(target,2)}
        assert raw=={Q(3)} and target_lengths=={Q(8)}
        # Equality of the complete two-vector Gram matrices certifies an affine
        # isometry of the port plane AFTER the explicit source metric rescaling.
        v=[subtract(N[k],N[rim[0]]) for k in rim[1:]]
        w=[subtract(points[k],points['A']) for k in 'BC']
        assert [[scale2*dot_metric(a,b,GN) for b in v] for a in v]==[[dot_metric(a,b,G) for b in w] for a in w]
        centroid=mean([N[k] for k in rim]);assert apply(R,centroid)==centroid
        for axis in range(3):
            x=[(N[k][axis],Q(0)) for k in rim];assert decode(encode(x))==x
        corner_modes=[encode([(N[k][axis],Q(0)) for k in rim]) for axis in range(3)]
        assert all(any(corner_modes[a][k]!=ZERO for a in range(3)) for k in (1,2))
        induced={target[i]:target[rim.index(nr[rim[i]])] for i in range(3)}
        own_group=pg if prefix=='L' else eg
        witnesses=[word for action,word in own_group if all(action[k]==induced[k] for k in target)]
        assert bool(witnesses)==(prefix=='L')
        interfaces.append(dict(source_rim=rim,target=name,vertex_map=dict(zip(rim,target)),raw_edge_squared='3',target_edge_squared='8',required_length_scale='sqrt(8/3)',induced_port_action=induced,source_action_words=witnesses,fixed_centroid=True,moving_corner_channels=[1,2]))
    assert not any({action[k] for k in 'ABC'}==set('ABC') for action,word in eg if word)
    assert not any({action[k] for k in 'ABCD'}==set('ABCD') for action,word in eg if word)
    # All six triangle bijections transport the full Fourier record exactly.
    # Odd orientation swaps k=1 and k=2; it is not automatically charge conjugation.
    probes=[[ONE if i==j else ZERO for i in range(3)] for j in range(3)]
    probes += [[(Q(1),Q(2)),(Q(-3),Q(1)),(Q(2),Q(-1))]]
    checks=0
    for pi in permutations(range(3)):
        a=pi[0];s=1 if pi[1]==(a+1)%3 else -1
        assert all(pi[i]==(a+s*i)%3 for i in range(3))
        for x in probes:
            z=encode(x);assert decode(z)==x
            assert sum(norm(v) for v in x)==3*sum(norm(v) for v in z)
            y=[ZERO]*3
            for i in range(3):y[pi[i]]=x[i]
            expected=[mul(power(-k*a),z[(s*k)%3]) for k in range(3)]
            assert encode(y)==expected and decode(expected)==y
            checks+=1
    fixed=encode([ONE]*3);assert fixed==[ONE,ZERO,ZERO]
    assert decode([ZERO,fixed[1],fixed[2]])!=[ONE]*3
    # Independent amplitudes cannot be identified losslessly by averaging.
    # Retain the difference channel explicitly to obtain a reversible interface.
    for j in range(6):
        x=[ONE if i==j else ZERO for i in range(3)]
        y=[ONE if i+3==j else ZERO for i in range(3)]
        average=[scale(Q(1,2),add(a,b)) for a,b in zip(x,y)]
        difference=[scale(Q(1,2),add(a,scale(-1,b))) for a,b in zip(x,y)]
        assert [add(a,b) for a,b in zip(average,difference)]==x
        assert [add(a,scale(-1,b)) for a,b in zip(average,difference)]==y
        assert sum(map(norm,x+y))==2*sum(map(norm,average+difference))
        assert decode(encode(average))==average and decode(encode(difference))==difference
    assert scale(Q(1,2),add(ONE,scale(-1,ONE)))==ZERO
    # Adjacent native centroid triangles are not congruent merely because their
    # boundary edge matches. Compare phase-mode norms in the matched metric.
    belt_face=next(f for f in geometry['belt_faces'] if 'L0' in f and 'L1' in f)
    belt_norm=scale2*small_triangle_mode_norm(mean([N[k] for k in belt_face]),N['L0'],N['L1'],GN)
    pnorm=small_triangle_mode_norm(mean([P[k] for k in 'ABC']),P['A'],P['B'],GP)
    enorm=small_triangle_mode_norm(mean([E[k] for k in 'ABC']),E['A'],E['B'],GE)
    assert belt_norm==Q(4198,675) and pnorm==enorm==Q(20,3) and belt_norm!=pnorm
    # Topology check is only for the boundary surface using ABCD on the electron
    # side, NOT for the entire 4D electron or the singular center-cone volume.
    faces=[tuple(f) for f in geometry['belt_faces']]
    for prefix,apex in [('L','P_D'),('U','E_D')]:
        rim=[prefix+str(i) for i in range(3)]
        faces += [(apex,rim[(i+1)%3],rim[i]) for i in range(3)]
    # Keep constituent provenance and the two temporarily hidden attachment
    # faces. Identification is a quotient of labels, not erasure of occurrences.
    port_maps={'N':{k:k for k in N},'P':dict(zip('ABCD',['L0','L1','L2','P_D'])),
               'E':dict(zip('ABCD',['U0','U1','U2','E_D']))}
    original=[('N',tuple(f)) for f in geometry['belt_faces']]
    original += [(owner,('D','ABC'[(i+1)%3],'ABC'[i])) for owner in ('P','E') for i in range(3)]
    joined=[(owner,tuple(port_maps[owner][v] for v in face)) for owner,face in original]
    assert [face for owner,face in joined]==faces
    inverses={owner:{v:k for k,v in mapping.items()} for owner,mapping in port_maps.items()}
    replay=json.loads(json.dumps(joined))
    detached=[(owner,tuple(inverses[owner][v] for v in face)) for owner,face in replay]
    assert detached==original
    retained_caps={'P':tuple('ABC'),'E':tuple('ABC')}
    for owner in ('P','E'):
        restored=[face for tag,face in detached if tag==owner]+[retained_caps[owner]]
        assert {frozenset(f) for f in restored}=={frozenset(f) for f in combinations('ABCD',3)}
    vertices=set().union(*map(set,faces));edge_faces={}
    for index,f in enumerate(faces):
        for e in combinations(sorted(f),2):edge_faces.setdefault(e,[]).append(index)
    assert (len(vertices),len(edge_faces),len(faces))==(8,18,12)
    assert all(len(fs)==2 for fs in edge_faces.values())
    signed_edges={}
    for face in faces:
        for i in range(3):
            a,b=face[i],face[(i+1)%3];edge=tuple(sorted((a,b)))
            signed_edges[edge]=signed_edges.get(edge,0)+(1 if a<b else -1)
    assert all(value==0 for value in signed_edges.values())
    # Every vertex link is a single cycle, and the face adjacency is connected.
    for v in vertices:
        link={}
        for f in faces:
            if v in f:
                a,b=[x for x in f if x!=v];link.setdefault(a,set()).add(b);link.setdefault(b,set()).add(a)
        assert all(len(ns)==2 for ns in link.values())
        seen={next(iter(link))}
        while True:
            expanded=seen|set().union(*(link[x] for x in seen))
            if expanded==seen:break
            seen=expanded
        assert seen==set(link)
    seen={0}
    while True:
        expanded=seen|{j for fs in edge_faces.values() if seen.intersection(fs) for j in fs}
        if expanded==seen:break
        seen=expanded
    assert len(seen)==len(faces)
    result=dict(verification_passed=True,interfaces=interfaces,raw_isometric_match=False,explicitly_scaled_port_match=True,
        phase_transport_bijection_checks=checks,reversible_join_requires_retained_difference_channel=True,
        tagged_boundary_attach_detach_roundtrip=True,attachment_faces_restored_after_detach=True,
        opposite_boundary_orientations_checked=True,
        fixed_channel_deletion_loses_information=True,centroid_fixed_does_not_mean_corners_fixed=True,
        proton_face_action_available_as_generated_word=True,electron_five_cycle_preserves_fixed_ABC_port=False,
        native_incident_triangle_mode_norms={'scaled_belt':str(belt_norm),'proton_ABC':str(pnorm),'electron_ABC':str(enorm)},
        direct_native_mode_identification_is_isometric=False,
        boundary_surface={'vertices':8,'edges':18,'faces':12,'euler_characteristic':2,'connected_closed_surface_with_circular_vertex_links':True,'type':'sphere; attachment tetrahedral boundary patches only'},
        not_established=['physical binding or flow','unscaled metric matching','a native belt-to-carrier phase adapter','a fixed-port intertwiner with the electron source five-cycle','a passage through center-cone volumes','different real/complex roles for the two rims'],
        source_hashes={p.name:sha256(p.read_bytes()).hexdigest() for p in paths+[Path(__file__)]})
    (BASE/'results/neutron_rim_port_transport.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
