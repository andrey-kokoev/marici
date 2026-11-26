"""Two passes: predict candidates from boundary spheres, then certify shellable fillings.
All simplices use original labels. A short support is retained even after release.
"""
from functools import lru_cache
from itertools import combinations
from collections import Counter
from ramsey38_global_shell import N,sub
from ramsey38_support_ball_completion import shelling
from ramsey38_compare_support_fillings import boundary

# Enumerate the labelled spheres on at most seven points once. Begin with one
# edge set of size 3n-6, then solve for its triangles. Connectedness, two
# faces per edge, and cyclic vertex links certify a closed surface; its Euler
# characteristic is two by the edge count, so it is a sphere.
@lru_cache(None)
def abstract_spheres(n):
    V=frozenset(range(n));E=sub(V,2);out=set()
    for missing in combinations(E,len(E)-(3*n-6)):
        graph=E-set(missing)
        if any(sum(v in e for e in graph)<3 for v in V):continue
        tri=[t for t in sub(V,3) if sub(t,2)<=graph];by={e:[i for i,t in enumerate(tri) if e<=t] for e in graph}
        if any(len(a)<2 for a in by.values()):continue
        # Binary face choices, with exactly two triangles at every edge.
        def choose(yes,no):
            while True:
                y=set();z=set();branch=None
                for a in by.values():
                    free=set(a)-yes-no;need=2-len(yes.intersection(a))
                    if need<0 or need>len(free):return
                    if not need:z.update(free)
                    elif need==len(free):y.update(free)
                    elif branch is None:branch=next(iter(free))
                if y&z:return
                if y or z:yes=yes|y;no=no|z;continue
                break
            if branch is not None:
                choose(yes|{branch},no);choose(yes,no|{branch});return
            fs=frozenset(tri[i] for i in yes)
            for v in V:
                es=[t-{v} for t in fs if v in t];seen=set(es[0]);
                for _ in es:
                    for e in es:
                        if e&seen:seen.update(e)
                if seen!=set.union(set(),*es):return
            seen={next(iter(V))}
            for _ in V:
                for e in graph:
                    if seen&e:seen.update(e)
            if seen==V:out.add(fs)
        choose(set(),set())
    return out

@lru_cache(None)
def templates():
    out=[]
    for n in range(4,8):
        for fs in abstract_spheres(n):
            for labels in combinations(range(7),n):
                faces=frozenset(sum(1<<labels[i] for i in f) for f in fs)
                closure=set(faces)|{0}
                for f in faces:
                    a=f
                    while a:closure.add(a);a=(a-1)&f
                out.append((faces,closure))
    return out

T=tuple(sum(1<<i for i in t) for t in combinations(range(7),4)); F=tuple(sum(1<<i for i in t) for t in combinations(range(7),3)); carriers={f:sum(1<<i for i,t in enumerate(T) if t&f==f) for f in F};bits=lambda a:frozenset(i for i in range(7) if a>>i&1)

def first_ball(bd,rows):
    forced=sum(1<<i for i,t in enumerate(T) if t in rows)
    @lru_cache(None)
    def search(mask):
        ban=mask;needs=[]
        for f,h in carriers.items():
            quota=1 if f in bd else 2;n=(h&mask).bit_count()
            if n>quota:return
            if n==quota:ban|=h
            elif n or f in bd:needs.append(h)
        if not needs:
            ts=[t for i,t in enumerate(T) if mask>>i&1]
            if all(any(r&t==r for t in ts) for r in rows):
                order=shelling(frozenset(map(bits,ts)))
                if order:
                    assert boundary(order)==frozenset(map(bits,bd));return order
            return
        h=min((h&~ban for h in needs),key=int.bit_count)
        while h:
            b=h&-h;h-=b;ans=search(mask|b)
            if ans:return ans
    return search(forced)

def predict(root):
    labels=sorted(N[root]);rows={v:sum(1<<i for i,w in enumerate(labels) if w in nbr) for v,nbr in N.items() if v!=root and v not in labels}
    assert max(x.bit_count() for x in rows.values())<=4
    short={v:r for v,r in rows.items() if r.bit_count()<4}; buckets={v:[] for v in short};buckets[0]=[]
    for faces,closure in templates():
        hidden=[v for v,r in short.items() if r not in closure]
        if len(hidden)<=1:buckets[hidden[0] if hidden else 0].append(faces)
    return labels,rows,buckets

if __name__=='__main__':
    # Previously untested roots of degree seven with no all-exposed filling.
    roots=[3,5,6,10,14,15,16,17,18,19,20,21,22,23,25]
    import json,argparse
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args();data={}
    for r in roots:
        labels,rows,buckets=predict(r);data[r]={'labels':labels,'shell_counts':{v:len(bs) for v,bs in buckets.items() if bs},'solutions':{}}
        print('boundary',r,data[r]['shell_counts'],flush=True)
    for r in roots:
        labels,rows,buckets=predict(r)
        for v,bs in buckets.items():
            for bd in bs:
                order=first_ball(bd,set(rows.values()))
                if order:
                    data[r]['solutions'][v]=dict(support=sorted(labels[i] for i in bits(rows.get(v,0))),shelling=[sorted(labels[i] for i in t) for t in order]);break
        print('ball',r,{v:d['support'] for v,d in data[r]['solutions'].items()},flush=True)
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
