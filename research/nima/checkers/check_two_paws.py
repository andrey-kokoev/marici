"""Two paws sharing AD: explicit local versus global two-step closure."""
from itertools import combinations
from math import sqrt, cos, sin, pi, acos, isclose
from pathlib import Path
import json

NAMES = 'ABCDEF'
SEED = {'AB', 'AC', 'AD', 'BC', 'AE', 'AF', 'EF'}
PAWS = ['ABCD', 'AEFD']

def edge(a, b):
    return ''.join(sorted((a, b)))

def complete(edges, scopes):
    witnesses = {}
    for scope in scopes:
        for a, b in combinations(sorted(scope), 2):
            key = edge(a, b)
            if key in edges:
                continue
            paths = [a+m+b for m in sorted(scope) if m not in (a,b)
                     and edge(a,m) in edges and edge(m,b) in edges]
            if paths:
                witnesses.setdefault(key, []).extend(paths)
    return edges | set(witnesses), witnesses

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def rotate(v, axis, angle):
    n = tuple(x/sqrt(dot(axis,axis)) for x in axis)
    w = cross(n,v)
    return tuple(cos(angle)*v[i]+sin(angle)*w[i]+(1-cos(angle))*dot(n,v)*n[i] for i in range(3))
def distance(a,b): return sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def points(t):
    h=sqrt(3)/2
    a=(0.,0.,0.); b=(1.,0.,0.); c=(.5,h,0.); d=(-.5,h,0.)
    smooth=lambda x: (lambda y:y*y*(3-2*y))(max(0,min(1,x)))
    phi=pi/3*smooth((t-.15)/.30)
    theta=acos(-1/3)*smooth((t-.45)/.30)
    # Shared D is fixed: fold the triangle vertex rather than moving D twice.
    b1=rotate(rotate(b,c,theta),d,phi); c1=rotate(c,d,phi)
    b2=rotate(rotate(b,c,-theta),d,pi-phi); c2=rotate(c,d,pi-phi)
    return dict(zip(NAMES,[a,b1,c1,d,b2,c2]))

def volume(p, keys):
    a,b,c,d=(p[k] for k in keys)
    sub=lambda x:tuple(v-u for v,u in zip(x,a))
    return abs(dot(sub(b),cross(sub(c),sub(d))))/6

def main():
    local,lw=complete(SEED,PAWS)
    glob,gw=complete(SEED,[NAMES])
    assert local-SEED == {'BD','CD','DE','DF'}
    assert glob-local == {'BE','BF','CE','CF'}
    assert len(local)==11 and len(glob)==15
    assert complete(local,PAWS)[0]==local
    assert complete(glob,[NAMES])[0]==glob
    assert complete(local,[NAMES])[0]==glob
    for i in range(101):
        p=points(i/100)
        assert all(isclose(distance(p[k[0]],p[k[1]]),1,abs_tol=1e-10) for k in SEED)
        assert p['A']==(0.,0.,0.) and p['D']==(-.5,sqrt(3)/2,0.)
    p=points(1)
    assert all(isclose(distance(p[k[0]],p[k[1]]),1,abs_tol=1e-10) for k in local)
    vols={paw:volume(p,paw) for paw in PAWS}
    assert all(isclose(v,sqrt(2)/12,abs_tol=1e-10) for v in vols.values())
    assert all(distance(p[a],p[b])>1e-8 for a,b in combinations(NAMES,2))
    assert any(not isclose(distance(p[k[0]],p[k[1]]),1,abs_tol=1e-10) for k in glob-local)
    assert all(volume(points(0),paw)<1e-10 for paw in PAWS)
    report={'seed_edges':sorted(SEED),'local':{'edges':sorted(local),'new_witnesses':lw},
            'global':{'edges':sorted(glob),'new_witnesses':gw},'final_points':p,
            'individual_tetrahedron_volumes':vols,
            'cross_edge_lengths':{k:distance(p[k[0]],p[k[1]]) for k in sorted(glob-local)},
            'note':'Supplied 3D folding and graph closure; cross edges need not be unit. No automatic simplex fillers or union-volume claim.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'two-paws.json'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: 101 motion samples; local 7 -> 11; global 7 -> 15; both closures fixed; two regular tetrahedra.')
if __name__=='__main__': main()
