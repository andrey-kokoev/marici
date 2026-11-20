"""Joint border search. Sort the new vertices by their links to the fixed prefix."""
from collections import Counter
from ramsey_39_pattern_three_choices import Random, add, options

def main():
    base=25; mask=(1<<base)-1; pairs=[]; ind=[0]; rng=Random(39)
    for n in range(21):pairs,ind=add(n,rng.choice(options(n,pairs,ind)),pairs,ind)
    for n,L in enumerate([[1,4,6,8,13,19],[1,7,8,11,13,18],[7,9,10,16,18,20,22],[7,9,10,17,18,19]],21):
        p=sum(1<<(i-1) for i in L);assert p in options(n,pairs,ind);pairs,ind=add(n,p,pairs,ind)
    choices=sorted(options(base,pairs,ind));levels=[[s for s in ind if s.bit_count()==k] for k in range(8)]
    counts=Counter();winning=set();best=[]
    def visit(n,opts,fam,path):
        nonlocal best
        counts[n]+=1
        if len(path)>len(best):best=path
        if n==30:
            winning.update(p&mask for p in path);return
        for p in opts:
            # A + between the two new vertices needs disjoint positive neighborhoods;
            # a - needs their positive neighborhoods to hit each old negative seven.
            miss=[s for s in fam[7] if not s&p] if n<29 else []
            child=[]
            if n<29:
                for q in opts:
                    if (q&mask)<(p&mask):continue
                    if not p&q:child.append(q|1<<n)
                    if all(q&s for s in miss):child.append(q)
            nxt=[fam[0]]+[fam[k]+[s|1<<n for s in fam[k-1] if not s&p] for k in range(1,8)] if child else None
            visit(n+1,child,nxt,path+[p])
    visit(base,choices,levels,[]);print(sorted(counts.items()),'first choices reaching 30',len(winning))
    for n,p in enumerate(best,base):
        assert p in options(n,pairs,ind);pairs,ind=add(n,p,pairs,ind);print(n+1,[i+1 for i in range(n) if p>>i&1])
if __name__=='__main__':main()
