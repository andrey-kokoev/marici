"""Four-stage paw closure: Cl(3,0) rotors versus matrix/packet execution.

Supplied choices: flat seed, axes, rotation angles, and two-step path completion.
The constructor tests the conjectured diagram; these choices are not derived.
No external numerical dependencies.
"""
from itertools import combinations
from math import cos, sin, sqrt, pi, isclose
from pathlib import Path
import json

EPS=1e-10

def gp(a,b):
    out=[0.0]*8
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            inversions=sum((j & ((1<<k)-1)).bit_count() for k in range(3) if i & (1<<k))
            out[i^j]+=(-1 if inversions%2 else 1)*x*y
    return out

def reverse(a):
    return [x*((-1)**(i.bit_count()*(i.bit_count()-1)//2)) for i,x in enumerate(a)]
def vector(v):
    out=[0.0]*8
    for i,x in enumerate(v): out[1<<i]=x
    return out

def rotor(axis,angle):
    norm=sqrt(sum(x*x for x in axis)); x,y,z=(v/norm for v in axis)
    c,s=cos(angle/2),sin(angle/2)
    out=[0.0]*8;out[0]=c;out[6]=-x*s;out[5]=y*s;out[3]=-z*s
    assert close(gp(out,reverse(out)),[1,0,0,0,0,0,0,0])
    return out

def act(r,v):
    out=gp(gp(r,vector(v)),reverse(r))
    assert all(abs(out[i])<EPS for i in (0,3,5,6,7))
    return tuple(out[1<<i] for i in range(3))

def close(a,b): return all(abs(x-y)<EPS for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def rotate_matrix(v,n,angle):
    # Independent Rodrigues construction, without Clifford products.
    norm=sqrt(dot(n,n));n=tuple(x/norm for x in n)
    c,s=cos(angle),sin(angle);nv=cross(n,v);proj=dot(n,v)
    return tuple(c*v[i]+s*nv[i]+(1-c)*proj*n[i] for i in range(3))

A=(0.,0.,0.);B=(1.,0.,0.);C=(0.,1.,0.);D=(-1.,0.,0.)
initial={'A':A,'B':B,'C':C,'D':D}
base_edges={('A','B'),('A','C'),('B','C'),('A','D')}
base_packets={u+v:(u,v) for edge in base_edges for u,v in (edge,edge[::-1])}
assert len(base_packets)==8
# Completion is determined independently by the original incidence graph.
new_paths={}
for u,v in combinations(sorted(initial),2):
    if (u,v) in base_edges: continue
    middle=[m for m in initial if u+m in base_packets and m+v in base_packets]
    assert len(middle)==1
    new_paths[u+v]=(u+middle[0],middle[0]+v)
assert new_paths=={'BD':('BA','AD'),'CD':('CA','AD')}

rows=[]
for phi_deg in (0,45,90,180,360):
    phi=phi_deg*pi/180
    H=rotor(D,phi)  # leg axis, through A
    body={name:act(H,v) for name,v in initial.items()}
    assert close(body['A'],A) and close(body['D'],D)
    assert abs(dot(sub(body['B'],A),cross(sub(body['C'],A),sub(body['D'],A))))<EPS
    for theta_deg in (0,30,45,60,90,135,180):
        theta=theta_deg*pi/180
        L=rotor(C,theta)  # triangle-attached AC axis
        transported_L=gp(gp(H,L),reverse(H))
        # Body first, then leg rotation about the transported triangle axis.
        ga=dict(body)
        ga['D']=act(transported_L,D)
        # Leg first, followed by the frame rotation. These close the square.
        other=dict(body)
        other['D']=act(H,act(L,D))
        assert all(close(ga[k],other[k]) for k in ga)
        assert close(gp(transported_L,H),gp(H,L))
        # Independent mechanical matrix route.
        mechanical={name:rotate_matrix(v,D,phi) for name,v in initial.items()}
        mechanical['D']=rotate_matrix(D,rotate_matrix(C,D,phi),theta)
        assert all(close(ga[k],mechanical[k]) for k in ga)
        # Both orders induce equal displacements for every completed edge.
        completed=dict(base_packets)
        witnesses={}
        for label,(p,q) in new_paths.items():
            u,m=base_packets[p];m2,v=base_packets[q];assert m==m2
            composed=add(sub(mechanical[m],mechanical[u]),sub(mechanical[v],mechanical[m]))
            assert close(composed,sub(ga[v],ga[u]))
            completed[label]=(u,v);completed[v+u]=(v,u)
            witnesses[label]=[p,q]
        assert len(completed)==12
        assert {tuple(sorted(e)) for e in completed.values()}==set(combinations(sorted(initial),2))
        for u,v in completed.values():
            assert close(sub(ga[v],ga[u]),sub(mechanical[v],mechanical[u]))
        signed_volume=dot(sub(ga['B'],A),cross(sub(ga['C'],A),sub(ga['D'],A)))/6
        assert isclose(signed_volume,sin(theta)/6,abs_tol=EPS)
        # Independent GA trivector volume and oriented triangular-face closure.
        ga_volume=gp(gp(vector(sub(ga['B'],A)),vector(sub(ga['C'],A))),vector(sub(ga['D'],A)))[7]/6
        assert isclose(ga_volume,signed_volume,abs_tol=EPS)
        boundary=[0.0]*8
        for u,v,w,sign in [('B','C','D',1),('A','C','D',-1),('A','B','D',1),('A','B','C',-1)]:
            x,y=vector(sub(ga[v],ga[u])),vector(sub(ga[w],ga[u]))
            xy,yx=gp(x,y),gp(y,x)
            # Half the wedge gives the oriented triangle's area bivector.
            for j in range(8): boundary[j]+=sign*(xy[j]-yx[j])/4
        assert close(boundary,[0]*8)
        lengths={u+v:dot(sub(ga[v],ga[u]),sub(ga[v],ga[u])) for u,v in combinations(sorted(initial),2)}
        assert isclose(lengths['BD'],2+2*cos(theta),abs_tol=EPS)
        assert isclose(lengths['CD'],2,abs_tol=EPS)
        rows.append({'body_angle_degrees':phi_deg,'leg_angle_degrees':theta_deg,
                     'signed_volume':signed_volume,'nondegenerate':abs(signed_volume)>EPS,
                     'edge_squared_lengths':lengths,'new_path_witnesses':witnesses})
# Same relative theta, varying body orientation preserves all geometric readouts.
for theta in (0,30,45,60,90,135,180):
    variants=[r for r in rows if r['leg_angle_degrees']==theta]
    reference=variants[0]
    assert all(isclose(r['signed_volume'],reference['signed_volume'],abs_tol=EPS) for r in variants)
    assert all(isclose(r['edge_squared_lengths'][e],reference['edge_squared_lengths'][e],abs_tol=EPS)
               for r in variants for e in reference['edge_squared_lengths'])
# A full turn preserves vector positions while retaining a distinct spin rotor.
assert close(rotor(D,2*pi),[-1,0,0,0,0,0,0,0])
assert all(close(act(rotor(D,2*pi),v),v) for v in initial.values())

result={'status':'passed','algebra':'Euclidean Cl(3,0)',
        'seed':initial,'base_edges':sorted(base_edges),
        'supplied_rule':'rotate body about AD; rotate leg about transported AC; add witnessed two-step connections',
        'cases_checked':len(rows),'cases':rows,
        'homotopy_square':'F(s,t): B,C rotate by H(s*phi), D=H(s*phi)L(t*theta)D0, A fixed; its boundary gives the two routes.',
        'conclusion':'The rotation square commutes and path completion gives K4. Nonzero volume requires sin(theta)!=0. Same-theta body orientations are congruent; different theta values need not be. Rotations alone keep8 packets; completion adds4.',
        'scope':'Conditional geometric construction and independent numerical cross-check, not a formal homotopy proof or derived particle dynamics.'}
path=Path(__file__).resolve().parents[1]/'results/paw-rotor-tetrahedron.json'
path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
for r in rows:
    if r['body_angle_degrees']==0:
        print(r['leg_angle_degrees'],round(r['signed_volume'],6),r['nondegenerate'])
print('PASS:35 rotor/matrix comparisons, witnessed edge completion, and orientation controls.')
