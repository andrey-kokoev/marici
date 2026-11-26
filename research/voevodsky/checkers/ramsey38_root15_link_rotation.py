"""Necessary compatible link rotations for a ball plus its outside boundary cone."""
from itertools import permutations,product,combinations
from functools import lru_cache
from ramsey38_root15_pair_obstructions import P,short,facets,sub

def canon(c):
    i=c.index(min(c));return c[i:]+c[:i]

@lru_cache(None)
def link_domains(cells):
    es=set.union(set(),*(sub(s,2) for s in cells));tris=set.union(set(),*(sub(s,3) for s in cells));vs=sorted(set.union(set(),*es));cand=[]
    for a in vs:
        n=sorted(w for e in es if a in e for w in e-{a});opts=[]
        for tail in permutations(n[1:]):
            c=(n[0],)+tail
            if all(t-{a} in {frozenset((w,c[i-1])) for i,w in enumerate(c)} for t in tris if a in t):opts.append(c)
        cand.append(opts)
    if any(not o for o in cand):return []
    adj={a:set(cand[i][0]) for i,a in enumerate(vs) if cand[i]};seen=set();components=0
    for a in vs:
        if a not in seen:
            components+=1;stack=[a];seen.add(a)
            while stack:
                b=stack.pop();stack.extend(adj[b]-seen);seen.update(adj[b])
    out=[]
    for cs in product(*cand):
        R=dict(zip(vs,cs));walks=[];vis=set()
        for a in vs:
            for b in R[a]:
                if (a,b) in vis:continue
                i,j=a,b;face=[]
                while (i,j) not in vis:
                    vis.add((i,j));face.append(i);c=R[j];i,j=j,c[(c.index(i)+1)%len(c)]
                walks.append(face)
        if len(vs)-len(es)+len(walks)==2*components and tris<={frozenset(f) for f in walks if len(f)==3}:out.append(R)
    return out

def test(pair,core=False):
    fs=facets|{frozenset(r|{0}) for i,r in short.items() if i not in pair};vs=sorted(P|{0});dom={v:link_domains(frozenset(s-{v} for s in fs if v in s)) for v in vs}
    def solve(d):
        if not d:return True
        v=min(d,key=lambda w:len(d[w]))
        for R in d[v]:
            nxt={w:[S for S in opts if w not in R or S[v]==canon(R[w][::-1])] for w,opts in d.items() if w!=v}
            if all(nxt.values()) and solve(nxt):return True
        return False
    if core:
        for n in range(1,len(vs)+1):
            for ss in combinations(vs,n):
                if not solve({v:dom[v] for v in ss}):return ss
    return solve(dom)
if __name__=='__main__':
    predicted=[pair for pair in combinations(sorted(short),2) if set(pair)&{5,20,27} and test(pair)]
    print('compatible pairs:',predicted);print('first minimum conflict for (5,27):',test((5,27),True))
    witnessed=[(2,27),(5,7),(5,20),(7,27),(11,20),(11,27),(18,20),(20,27),(21,27)]
    assert predicted==witnessed
