"""Exact convex-cell coverage, continuity and whole-domain envelope bands.

No candidate constructor or source-coordinate adapter is imported.
"""
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib
from pathlib import Path
if not __debug__:raise RuntimeError('Assertions required')
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def area(p):return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1])) if p else Q(0)
def value(f,p):return f[0]*p[0]+f[1]*p[1]+f[2]
def intersection(subject,clip):
    out=list(subject)
    for a,b in zip(clip,clip[1:]+clip[:1]):
        old=out;out=[]
        if not old:break
        for p,q in zip(old,old[1:]+old[:1]):
            u,v=cross(a,b,p),cross(a,b,q)
            if u>=0:out.append(p)
            if (u<0<v) or (v<0<u):
                t=u/(u-v);out.append(tuple(p[k]+t*(q[k]-p[k]) for k in range(2)))
        out=list(dict.fromkeys(out))
    return out

def domain(n):
    assert type(n) is int and n>=3
    return [(Q(i,n),Q(i*i,n*n)) for i in range(1,n+1)]
def envelopes(n):
    ts=[Q(i,n) for i in range(1,n+1)];vertices=domain(n);lower=[];upper=[]
    for a,b,c in combinations(ts,3):
        f=(-(a*b+a*c+b*c),a+b+c,a*b*c)
        gaps=[t**3-value(f,p) for t,p in zip(ts,vertices)]
        if min(gaps)>=0:lower.append(f)
        if max(gaps)<=0:upper.append(f)
    assert lower and upper
    return lower,upper

def check(request,packet):
    assert packet['request']==request
    polygon=domain(request['n']);eta=Q(request['eta']);assert eta>=0
    lower,upper=envelopes(request['n']);cells=[]
    assert packet['cells']
    for cell in packet['cells']:
        p=[tuple(map(Q,v)) for v in cell['vertices']];f=tuple(map(Q,cell['formula']))
        assert len(f)==3 and len(p)>=3 and all(len(v)==2 for v in p) and len(set(p))==len(p)
        assert area(p)>0
        # Every oriented edge supports the entire cell: a convex CCW polygon.
        assert all(cross(a,b,v)>=0 for a,b in zip(p,p[1:]+p[:1]) for v in p)
        assert all(cross(a,b,v)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1]) for v in p)
        for v in p:
            h=value(f,v)
            assert all(value(l,v)-eta<=h for l in lower)
            assert all(h<=value(u,v)+eta for u in upper)
        cells.append((p,f))
    for (p,f),(q,g) in combinations(cells,2):
        common=intersection(p,q)
        assert area(common)==0  # no overlapping interiors
        assert all(value(f,v)==value(g,v) for v in common)
    assert sum(area(p) for p,f in cells)==area(polygon)
    # Closed convex subsets, disjoint interiors, equal area and containment
    # imply exact coverage; a missing point would have a relative open gap.
    return {'cells':len(cells),'formulas':len({f for p,f in cells}),
            'cell_vertices':sum(len(p) for p,f in cells),
            'plane_vertex_checks':sum(len(p)*(len(lower)+len(upper)) for p,f in cells),
            'certificate_bytes':len(json.dumps(packet,sort_keys=True,separators=(',',':')).encode())}

def main():
    out=Path(__file__).resolve().parents[1]/'results'
    cp=out/'scalar-envelope-band-contract.json';pp=out/'scalar-envelope-band-packets.json'
    contract=json.loads(cp.read_text());packets=json.loads(pp.read_text());report=json.loads((out/'scalar-envelope-band.json').read_text())
    assert contract['family']=='owning-m4-moment-curve-two-history-v1'
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==report['contract_sha256']
    assert hashlib.sha256(pp.read_bytes()).hexdigest()==report['packets_sha256']
    for p,h in contract['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    assert len(contract['requests'])==len(packets)==len(report['cases'])
    for request,packet,claimed in zip(contract['requests'],packets,report['cases']):
        metrics=check(request,packet)
        assert all(claimed[k]==v for k,v in request.items())
        assert all(claimed[k]==v for k,v in metrics.items())
        needed=max(abs(value(tuple(map(Q,c['formula'])),tuple(map(Q,v)))-Q(v[0])**3) for c in packet['cells'] for v in c['vertices'])
        assert Q(claimed['boundary_error_bound'])==needed
    wp=out/'scalar-envelope-band-width-packets.json';width_packets=json.loads(wp.read_text())
    assert hashlib.sha256(wp.read_bytes()).hexdigest()==report['width_packets_sha256']
    assert len(width_packets)==len(contract['requests'])==len(report['width_rule_cases'])
    for request,packet,claimed in zip(contract['requests'],width_packets,report['width_rule_cases']):
        metrics=check(request,packet);n=request['n'];eta=Q(request['eta'])
        assert all(claimed[k]==v for k,v in metrics.items())
        assert all(claimed[k]==v for k,v in request.items())
        assert metrics['cells']<=n-2 and (metrics['cells']-1)**3*eta<=8
        assert claimed['stride']==max([1]+[s for s in range(2,n) if Q(s**3,8*n**3)<=eta])
    assert report['whole_polygon_certificates']==len(packets)+len(width_packets)
    result={'passed':True,'whole_polygon_certificates':len(packets)+len(width_packets),
      'scope':'Independent exact coverage, continuity, all-envelope inequalities and representation counts; no vertex-only acceptance.'}
    (out/'scalar-envelope-band-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
