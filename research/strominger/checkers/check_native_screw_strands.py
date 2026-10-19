"""Exact native-edge strand audit of the finite screw core.
Scope: one-block screw-periodic, strictly axially increasing paths through
occupied vertices. Display traversal may be reversed without changing curves.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
source=ROOT/'research/strominger/results/native-screw-patch/verification.json'
data=json.loads(source.read_text())
assert data['status']=='pass' and data['inspection']['certifiedExit']
for path,digest in data['sourceHashes'].items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest, f'Stale screw receipt: {path}'
T=data['screw']['matrix'];d=tuple(data['screw']['direction']);a=tuple(F(str(x)) for x in data['screw']['axisPoint'])
def point(s):return tuple(F(x) for x in s.split(','))
def add(u,v):return tuple(x+y for x,y in zip(u,v))
def sub(u,v):return tuple(x-y for x,y in zip(u,v))
def scale(t,v):return tuple(t*x for x in v)
def dot(u,v):return sum(x*y for x,y in zip(u,v))
def screw(v):return tuple(dot(row,v) for row in T)
def iterate(v,k):
    # T^-1(v)=T(v)-2d, since T^2 is translation by 2d.
    for _ in range(abs(k)):v=screw(v) if k>=0 else sub(screw(v),scale(2,d))
    return v
axial=lambda v:dot(sub(v,a),d)/dot(d,d)
R=(1,-1,1,-1);B=(0,1,0,-1)
radial=lambda v:(dot(sub(v,a),R),dot(sub(v,a),B))
edges=set();vertices=set()
for cell in data['cells']:
    vs=list(map(point,cell['vertices']));vertices.update(vs)
    edges.update(frozenset(pair) for pair in combinations(vs,2))
neighbor={v:set() for v in vertices}
for edge in edges:
    u,v=edge;neighbor[u].add(v);neighbor[v].add(u)
packets={p['id']:p for p in data['packets']};charts={c['id']:c for c in data['charts']}
root_chart=charts['chart-'+str(packets[data['boundaries'][0]]['chart'])]
seeds={name:point(root_chart['aliases'][name]) for name in ('C0','C1','M0','M1')}
# These are geometric roles, not an identification with field-tower components.
roles={}
for chart in data['charts']:
    for name,text in chart['aliases'].items():
        v=point(text)
        if v in vertices:
            assert v not in roles or roles[v]==name[0]
            roles[v]=name[0]
assert all((axial(v)*2).denominator==1 for v in vertices)
orbits={iterate(v,k):(name,k) for name,v in seeds.items() for k in range(-8,13)}
assert vertices<=orbits.keys(), 'An occupied vertex lies outside the four tested screw orbits'

def intersect(p,q,r,s):
    """Exact closed-segment intersection in four dimensions; returns a point.
    Parallel overlapping segments return one point of their intersection.
    """
    p,q,r,s=(tuple(map(F,x)) for x in (p,q,r,s))
    u=sub(q,p);v=sub(s,r);w=sub(r,p)
    for i,j in combinations(range(4),2):
        det=u[j]*v[i]-u[i]*v[j]
        if det:
            t=(v[i]*w[j]-v[j]*w[i])/det
            z=(u[i]*w[j]-u[j]*w[i])/det
            if 0<=t<=1 and 0<=z<=1 and add(p,scale(t,u))==add(r,scale(z,v)):
                return add(p,scale(t,u))
            return None
    # Collinear or parallel; nondegenerate native edges only.
    i=next(i for i in range(4) if u[i])
    if sub(w,scale(w[i]/u[i],u))!=(0,0,0,0):return None
    t0=(r[i]-p[i])/u[i];t1=(s[i]-p[i])/u[i]
    lo=max(F(0),min(t0,t1));hi=min(F(1),max(t0,t1))
    return add(p,scale(lo,u)) if lo<=hi else None

# Controls: crossing, overlapping, disjoint and skew segments.
assert intersect((0,0,0,0),(2,0,0,0),(1,-1,0,0),(1,1,0,0))==(1,0,0,0)
assert intersect((0,0,0,0),(2,0,0,0),(1,0,0,0),(3,0,0,0))==(1,0,0,0)
assert intersect((0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0)) is None
assert intersect((0,0,0,0),(2,0,0,0),(1,-1,1,0),(1,1,1,0)) is None

def path(candidate,blocks):
    v,m=candidate['start'],candidate['middle'];result=[v]
    for k in range(blocks):result.extend([iterate(m,k),iterate(v,k+1)])
    return result

def hits(left,right):
    return sorted({x for p,q in zip(left,left[1:]) for r,s in zip(right,right[1:]) if (x:=intersect(p,q,r,s)) is not None})

candidates=[]
for name,v in seeds.items():
    target=screw(v);assert target in vertices
    assert frozenset((v,target)) not in edges
    # Every lattice axial coordinate is a half-integer. A unit axial advance
    # with strict progress can therefore have at most one intermediate vertex.
    mids=sorted(m for m in neighbor[v]&neighbor[target] if axial(v)<axial(m)<axial(target))
    assert len(mids)==2
    for mid in mids:
        vv=[v,mid,target];signs=[]
        for x,y in zip(vv,vv[1:]):
            rx,ry=radial(x),radial(y);cross=rx[0]*ry[1]-rx[1]*ry[0]
            assert cross!=0;signs.append(1 if cross>0 else -1)
        assert signs[0]==signs[1]
        c={'id':name+('+' if signs[0]>0 else '-'),'seed':name,'start':v,'middle':mid,'target':target,'winding_sign':signs[0],
           'roles':[roles[x] for x in vv]}
        full=path(c,data['repeats'])
        assert all(frozenset((x,y)) in edges for x,y in zip(full,full[1:]))
        assert all(axial(x)<axial(y) for x,y in zip(full,full[1:]))
        candidates.append(c)
assert len(candidates)==8
pair_results=[]
for left,right in combinations(candidates,2):
    lp=path(left,2);rp=path(right,2);collisions=[]
    # A two-block period translates by 2d. Axial ranges of these fundamental
    # paths differ by <=1; shifts beyond +/-2 cannot intersect.
    for shift in range(-2,3):
        moved=[add(v,scale(2*shift,d)) for v in rp]
        collisions.extend(hits(lp,moved))
    finite=hits(path(left,4),path(right,4))
    opposite=left['winding_sign']!=right['winding_sign']
    pair_results.append({'left':left['id'],'right':right['id'],'opposite_handedness':opposite,
                         'periodically_disjoint':not collisions,'finite_four_block_intersections':finite,
                         'periodic_collision_witnesses':sorted(set(collisions))})
opp=[p for p in pair_results if p['opposite_handedness']]
disjoint=[p for p in pair_results if p['periodically_disjoint']]
assert len(opp)==16 and all(not p['periodically_disjoint'] for p in opp)
assert len(disjoint)==8 and all(not p['opposite_handedness'] for p in disjoint)
# Reversing traversal is not a geometric cure for collisions or handedness.
by_id={c['id']:c for c in candidates}
example=next(p for p in opp if p['left']=='C0+' and p['right']=='C1-')
l=path(by_id[example['left']],4);rr=path(by_id[example['right']],4)
assert hits(l,rr)==hits(l,list(reversed(rr))) and hits(l,rr)
assert all(axial(x)>axial(y) for x,y in zip(reversed(rr),list(reversed(rr))[1:]))
# The native role-homogeneous rails are planar, unlike the tested mixed-role paths.
assert all(dot(sub(v,a),R)==0 for v in vertices if roles[v]=='M')
assert all(dot(sub(v,a),B)==0 for v in vertices if roles[v]=='C')
report={'schema':'marici.native-screw-strands.v1','status':'pass',
 'candidate_scope':'Four occupied vertex screw orbits; one-block screw periodicity; native straight edges; strict axial progress; four finite blocks checked',
 'candidates':candidates,'pair_tests':pair_results,'candidate_count':8,'pair_count':28,
 'opposite_handed_pairs':16,'disjoint_opposite_handed_pairs':0,'disjoint_same_handed_candidate_pairs':8,
 'opposite_axial_traversal_removes_collisions':False,
 'middle_sheet_can_separate_tested_intersecting_pair_without_rerouting':False,
 'C_only_and_M_only_paths_are_planar':True,'mixed_role_paths_are_field_transport_laws':False,
 'scope':'Exact bounded native-edge strand test, not a no-go theorem for larger cells, radial layers, nonmonotone paths or arbitrary curves inside cells.'}
out=ROOT/'research/strominger/results/native-screw-strands';out.mkdir(parents=True,exist_ok=True)
paths=[Path(__file__),source,ROOT/'research/strominger/native-screw-strands-v1.md']
report['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def serial(x):
    if isinstance(x,F):return str(x)
    raise TypeError(type(x))
(out/'verification.json').write_text(json.dumps(report,indent=2,default=serial)+'\n')
# Two actual polygonal paths; no fitted smooth interpolation.
same=next(p for p in disjoint if p['left']=='C0+' and p['right']=='C1+')
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="620" viewBox="0 0 1050 620">','<rect width="1050" height="620" fill="white"/>', '<defs><marker id="direction" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#333"/></marker></defs>']
for row,pair in enumerate((same,example)):
    top=40+290*row
    title='Same handedness: disjoint native-edge paths' if row==0 else 'Opposite handedness: shared native vertices (red); reverse traversal does not help'
    svg.append(f'<text x="20" y="{top}" font-family="sans-serif" font-size="17">{title}</text>')
    def xy(v):
        x,y=radial(v);return (100+175*float(axial(v))+12*float(y),top+120-45*float(x)-25*float(y))
    for name,color in ((pair['left'],'#2471a3'),(pair['right'],'#d35400')):
        vs=path(by_id[name],4)
        if row==1 and name==pair['right']:vs=list(reversed(vs))
        svg.append(f'<polyline points="{" ".join(f"{xy(v)[0]},{xy(v)[1]}" for v in vs)}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#direction)"/>')
        for v in vs:
            x,y=xy(v);svg.append(f'<circle cx="{x}" cy="{y}" r="3" fill="{color}"/>')
    for v in pair['finite_four_block_intersections']:
        x,y=xy(v);svg.append(f'<circle cx="{x}" cy="{y}" r="7" fill="none" stroke="red" stroke-width="3"/>')
svg.append('</svg>');(out/'strand-comparison.svg').write_text('\n'.join(svg)+'\n')
print(json.dumps({k:report[k] for k in ('status','candidate_count','pair_count','opposite_handed_pairs','disjoint_opposite_handed_pairs','disjoint_same_handed_candidate_pairs')},indent=2))
