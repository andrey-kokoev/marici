"""All free row-swap pairs disjoint from the constant flags. Include only vertex-disjoint assignments (otherwise not a residual matching). Independently enumerate spanning two-factors by deleting a perfect matching on degree-three vertices."""
from collections import Counter
from ramsey_long_residual_inverse import R,flags,check,D,json

def factors(adj):
    if min(map(len,adj.values()))<2:return []
    def omit(rem,cuts):
        if rem:
            x=min(rem)
            for y in adj[x]&rem:yield from omit(rem-{x,y},cuts|{tuple(sorted((x,y)))})
        else:yield cuts
    out=[]
    for cuts in omit({x for x,s in adj.items() if len(s)==3},set()):
        left=set(adj);sizes=[]
        while left:
            q=[min(left)];left.remove(q[0]);
            for x in q:
                for y in adj[x]&left:
                    if tuple(sorted((x,y))) not in cuts:q.append(y);left.remove(y)
            sizes.append(len(q))
        out.append(dict(sizes=sorted(sizes),omitted=sorted(cuts),swap_invariant={tuple(sorted((R[x],R[y]))) for x,y in cuts}==cuts))
    return out

def run():
    base={(9,26),(14,15)};seen=set();out=[]
    for e in sorted(flags):
        u=frozenset([e,tuple(R[x] for x in e)]);z={x for a in base|u for x in a}
        if len(z)!=8 or len(u)!=2 or u in seen:continue
        seen.add(u);assert not z&{0,29};a={x:set() for x in set(range(30))-z}
        for x,y in flags:
            if x in a and y in a:a[x].add(y);a[y].add(x)
        r=check(u);out.append(dict(extra=sorted(u),min_degree=min(map(len,a.values())),overload=r['forced_overload'],factors=factors(a),reflected=len(r['paths']),pruning=r['pruning']))
    return out
if __name__=='__main__':
    out=run();print(Counter((r['min_degree'],str([f['sizes'] for f in r['factors']]),r['reflected']) for r in out));print([r for r in out if r['min_degree']==2 and not r['reflected']]);(D/'ramsey_all_extra_deadends.json').write_text(json.dumps(out)+'\n')
