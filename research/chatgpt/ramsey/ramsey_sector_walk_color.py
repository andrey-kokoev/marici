"""See frozen protocol. Reconstruct directed dual walks before opening the color table."""
from ramsey_cube_pair_rules import D,V,G,json,combinations
from collections import Counter,defaultdict,deque
src=json.loads((D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json').read_text());p=dict(zip('ABCD',('111','100','010','001')));opp=lambda v:''.join(str(1-int(x)) for x in v);coord=lambda f:opp(p[next(iter(set(p)-set(f[2:])))])
T={t['outer_arrow']:t['triangle'] for t in src['triangles_and_transports']};step={};sides={}
for e,(f,a,b) in T.items():
    n,=[k for k,(ff,y,z) in T.items() if ff==f and y==b];step[e]=(n,e[::-1]);side=''.join(i if i==j else '*' for i,j in zip(coord(f),p[b]));assert side.count('*')==1;sides[side]=(e,n)
assert len(sides)==12;dist={}
for start in T:
    q=deque([start]);d={start:0}
    while q:
        s=q.popleft()
        for t in step[s]:
            if t not in d:d[t]=d[s]+1;q.append(t)
    assert len(d)==12;dist[start]=d
R=[g for g in G if set(map(g,p.values()))==set(p.values()) and all(g(x)==g(x,state=True) for x in V)];assert len(R)==12
P=[(a,b) for a,b in combinations(sorted(sides),2) if any({x,y}=={'0','1'} for x,y in zip(a,b))];L={(a,b):tuple(sorted([dist[sides[a][1]][sides[b][0]],dist[sides[b][1]][sides[a][0]]])) for a,b in P};rules=json.loads((D/'ramsey_cube_pair_rules.json').read_text());truth={}
for s,cs in rules.items():
    for g in G:truth[tuple(sorted(map(g,s.split()))) ]={g(c,state=True) for c in cs}
def score(k,c):
    B=defaultdict(list)
    for pair in P:B[k(pair)].append(pair)
    err=0;example=None
    for pairs in B.values():
        r=[x for x in pairs if c in truth[x]];b=[x for x in pairs if c not in truth[x]];err+=min(len(r),len(b))
        if r and b and example is None:example=dict(red=r[0],blue=b[0],key=k(r[0]))
    return dict(classes=len(B),min_errors=err,collision=example)
rows={}
for c in V:
    orbit=lambda H:lambda ab:min(tuple(sorted(map(g,ab))) for g in H);rows[c]=dict(walk=score(L.get,c),unmarked=score(orbit(R),c),point_marked=score(orbit([g for g in R if g(c)==c]),c))
r=dict(disjoint_pairs=len(P),all_pairs=66,states=rows);print(r['disjoint_pairs'],rows['000'],[(c,[v['min_errors'] for v in a.values()]) for c,a in rows.items()]);(D/'ramsey_sector_walk_color.json').write_text(json.dumps(r,indent=2)+'\n')
