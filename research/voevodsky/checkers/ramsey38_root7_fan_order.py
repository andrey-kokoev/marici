"""Necessary shared-edge fan order in a PL ball, independent of mesh budget."""
from itertools import permutations,product
from ramsey38_root7_single_release import p,rows,short,sub

def rotations(drop):
    req={r for i,r in short.items() if i!=drop};edges=set.union(*(sub(r,2) for r in req));tris={r for r in req if len(r)==3}
    points=sorted(p); options=[]
    for v in points:
        n=sorted({w for e in edges if v in e for w in e-{v}});opts=[]
        for tail in permutations(n[1:]):
            c=(n[0],)+tail
            if all(t-{v} in {frozenset((c[i-1],w)) for i,w in enumerate(c)} for t in tris if v in t):opts.append(c)
        options.append(opts)
    for cc in product(*options):
        rot=dict(zip(points,cc));seen=set();faces=[]
        for v in points:
            for w in rot[v]:
                if (v,w) in seen:continue
                a,b=v,w;f=[]
                while (a,b) not in seen:
                    seen.add((a,b));f.append(a);n=rot[b];a,b=b,n[(n.index(a)+1)%len(n)]
                faces.append(tuple(f))
        if len(points)-len(edges)+len(faces)==2 and tris<={frozenset(f) for f in faces if len(f)==3}:yield rot

def limits(rot,v,w):
    c=rot[v];i=c.index(w);return tuple(a for a in c[i+1:]+c[:i] if a in {3,9,11,13})

def audit(drop):
    orders=[a+b for g,h in [((3,9),(11,13)),((11,13),(3,9))] for a in permutations(g) for b in permutations(h)]
    counts=[0,0,0];profiles=set()
    for rot in rotations(drop):
        counts[0]+=1;a=limits(rot,6,21);b=limits(rot,21,6)[::-1];profiles.add((a,b));
        if not any(tuple(i for i in o if i in a)==a and tuple(i for i in o if i in b)==b for o in orders):continue
        counts[1]+=1
        if drop==8:
            # Triangle 3,6,21 is an intact face with its whole boundary on the shell.
            # Rim rays to 9 and 11 lie on opposite sides of the rays to 3 and 21.
            assert {3,6,21}<=rows[23] and all(any(e<=r for v,r in short.items() if v!=8) for e in sub({3,6,21},2))
            assert rows[1]=={11,27} and rows[8]=={9,27}
            if min(a.index(9),a.index(11)) < a.index(3) < max(a.index(9),a.index(11)):continue
        counts[2]+=1
    return counts,profiles
if __name__=='__main__':
    for d,expected in [(5,[4,0,0]),(8,[4,2,0]),(17,[2,0,0])]:
        counts,profiles=audit(d);assert counts==expected;print(d,counts,profiles,flush=True)
