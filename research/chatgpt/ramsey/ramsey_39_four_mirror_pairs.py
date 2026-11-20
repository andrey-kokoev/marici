"""Complete signed 3x9 block using inversion and (3,9) tests, no regularity or host lookup in search."""
from collections import Counter
from ramsey_39_rotate_reflect_completion import sign


def extend(I,b,p):return I+[s|b for s in I if not s&p]
def search(rows):
    I=[0];n0=len(rows);mask=(1<<n0)-1
    for i,p in enumerate(rows):
        assert p in I;I=extend(I,1<<i,p)
    assert max(s.bit_count() for s in I)<9
    nodes=Counter();sol=[];initial=None
    def visit(I,perm,path,lo):
        nonlocal initial
        nodes[len(path)]+=1
        if len(path)==4:sol.append(path);return
        n=len(perm);bit=1<<n
        opts=I
        for s in I:
            if s.bit_count()==8:opts=[p for p in opts if p&s]
        legal=set(opts);seven=[s for s in I if s.bit_count()==7]
        if not path:initial=len(opts)
        for p in opts:
            r=sum(((p>>i)&1)<<j for i,j in enumerate(perm));assert r in legal
            # Set orientation of each pair and order pairs by old-base pattern.
            if (p&mask)<lo or (p&mask)>(r&mask):continue
            for b in (0,1):
                if (p&r if b else any(not s&(p|r) for s in seven)):continue
                new=extend(extend(I,bit,p),bit<<1,r|(b<<n))
                visit(new,perm+[n+1,n],path+[(p,r|(b<<n))],p&mask)
    visit(I,list(reversed(range(n0))),[],0);return initial,nodes,sol

if __name__=='__main__':
    outer=list(range(-13,14));rows=[sum(sign(v,u)<<i for i,u in enumerate(outer[:j])) for j,v in enumerate(outer)];start,nodes,sol=search(rows)
    print('first column choices',start,'normalized paths to depth',nodes,'solutions',len(sol))
    for path in sol[:2]:
        pairs=[(p&((1<<27)-1),r&((1<<27)-1)) for p,r in path];print('distinct oriented outer types',len(set(x for pr in pairs for x in pr)))
        # Compare to the withheld host only after construction.
        expected={sum(sign(t,v)<<i for i,v in enumerate(outer)):t for t in (14,-14,15,-15,16,-16,17,-17)};order=outer.copy()
        for col in [x for pr in path for x in pr]:
            t=expected[col&((1<<27)-1)];assert col==sum(sign(t,v)<<i for i,v in enumerate(order));order.append(t)
        print('reconstructed labels',order[27:])
