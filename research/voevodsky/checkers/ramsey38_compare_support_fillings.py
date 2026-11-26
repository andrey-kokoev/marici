"""Compare the seven minimum completions. Vertex labels refer to catalogue record 1."""
from itertools import combinations, permutations
from collections import Counter
from ramsey38_support_ball_completion import forced, pool, rows, shelling

def boundary(ts):
    hits=Counter(frozenset(f) for t in ts for f in combinations(t,3))
    return frozenset(f for f,n in hits.items() if n==1)

def fmt(ss):return sorted(tuple(sorted(s)) for s in ss)

def main():
    sols=[]
    for extra in combinations(pool,5):
        ts=forced.union(extra)
        if all(any(r<=t for t in ts) for r in rows) and shelling(ts):sols.append(ts)
    assert len(sols)==7
    common=set.intersection(*sols); print('shared tetrahedra',fmt(common),'shared boundary triangles',fmt(set.intersection(*(set(boundary(s)) for s in sols))))
    for i,s in enumerate(sols):print('ABCDEFG'[i],fmt(s-common))
    for i,j in combinations(range(7),2):
        a,b=sols[i],sols[j]; old,new=a-b,b-a
        print('ABCDEFG'[i]+'ABCDEFG'[j],len(old),'boundary changes',len(boundary(a)-boundary(b)), 'local vertices',len(set.union(*(set(x) for x in old|new))))
    labels=sorted(set.union(*(set(r) for r in rows)))
    def shape(faces):
        def code(p):
            m=dict(zip(labels,p));return tuple(sorted(sum(1<<m[v] for v in f) for f in faces))
        return min(code(p) for p in permutations(range(len(labels))))
    for name,families in [('boundary',list(map(boundary,sols))),('ball',sols)]:
        classes={}
        for letter,f in zip('ABCDEFG',families): classes.setdefault(shape(f),[]).append(letter)
        print(name,'unlabeled isomorphism classes',list(classes.values()))
    return sols
if __name__=='__main__': main()
