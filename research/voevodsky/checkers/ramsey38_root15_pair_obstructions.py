"""Budget-independent necessary tests on oriented boundary embeddings at root 15."""
from itertools import combinations,permutations,product
from ramsey38_root15_release_cost import P,rows,short,sub

facets=set(map(frozenset,rows.values()));tri=set.union(*(sub(r,3) for r in facets));all_edges=set.union(*(sub(r,2) for r in facets));tet={r for r in facets if len(r)==4}
def rotations(req):
    E=set.union(*(sub(r,2) for r in req));faces={r for r in req if len(r)==3};opts=[];vs=sorted(P);assert set.union(set(),*E)==P
    for v in vs:
        n=sorted(w for e in E if v in e for w in e-{v});cand=[]
        for tail in permutations(n[1:]):
            c=(n[0],)+tail;rim={frozenset((a,c[i-1])) for i,a in enumerate(c)}
            if all(f-{v} in rim for f in faces if v in f):cand.append(c)
        opts.append(cand)
    for cs in product(*opts):
        R=dict(zip(vs,cs));fs=[];seen=set()
        for v in vs:
            for w in R[v]:
                if (v,w) in seen:continue
                a,b=v,w;f=[]
                while (a,b) not in seen:
                    seen.add((a,b));f.append(a);n=R[b];a,b=b,n[(n.index(a)+1)%len(n)]
                fs.append(f)
        if len(P)-len(E)+len(fs)==2 and faces<={frozenset(f) for f in fs if len(f)==3}:yield R,E

def cut_test(R,E):
    # A required triangle whose three edges are on the shell separates its
    # two shell sides. Every connected component off the triangle must stay
    # on one side, including edges through interior (non-boundary) supports.
    for t in tri:
        if not sub(t,2)<=E:continue
        c=sorted(t);sides=[set(),set()]
        for i,v in enumerate(c):
            n=R[v];j=n.index(c[i-1]);order=n[j+1:]+n[:j];k=order.index(c[(i+1)%3]);sides[0].update(order[:k]);sides[1].update(order[k+1:])
        seen=set(sides[0]);
        for _ in P:
            for e in all_edges:
                if not e&t and e&seen:seen.update(e)
        if seen&sides[1]:return sorted(t)

def fan_test(R,E):
    for e in E:
        seg=[t-e for t in tet if e<=t];tips=set.union(set(),*seg)
        if not seg:continue
        u,v=sorted(e)
        def after(a,b):
            n=R[a];i=n.index(b);return tuple(z for z in n[i+1:]+n[:i] if z in tips)
        x,y=after(u,v),after(v,u)[::-1]
        if not any(tuple(z for z in o if z in x)==x and tuple(z for z in o if z in y)==y and all(abs(o.index(a)-o.index(b))==1 for a,b in seg) for o in permutations(tips)):return sorted(e)

def audit(pair):
    req={frozenset(r) for v,r in short.items() if v not in pair};out=[]
    for R,E in rotations(req):out.append((cut_test(R,E),fan_test(R,E)))
    return out
if __name__=='__main__':
    for pair in [(5,27),(5,18),(5,21),(5,25),(18,27),(20,21),(20,25),(25,27),(5,20)]:
        a=audit(pair);print(pair,len(a),sum(c is None and f is None for c,f in a),set(map(str,a)),flush=True)
