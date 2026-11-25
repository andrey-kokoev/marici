"""Exact four-exclusive-support count before common-port constraints. Row repeats allowed."""
from collections import Counter
from ramsey310_fixed_exclusive_kernel import residual, sets, F

def index(n):
    A=residual(n);six=list(sets(A,F,6));seven=list(sets(A,F,7));N=len(six);full=(1<<N)-1
    inc=[sum(1<<i for i,s in enumerate(six) if s>>v&1) for v in range(27)]
    def avoids(s):
        m=full
        while s:
            b=s&-s;s^=b;m&=~inc[b.bit_length()-1]
        return m
    dis=[avoids(s) for s in six];missed=[avoids(t) for t in seven];partner=[]
    for i,s in enumerate(six):
        ok=(1<<(i+1))-1
        for t,miss in zip(seven,missed):
            if not s&t:ok &= ~miss
        partner.append(ok)
    return six,dis,partner

def census(n):
    six,dis,partner=index(n)
    totals=Counter();first=0;live=0;zero=0
    for i,p in enumerate(partner):
        while p:
            b=p&-p;p^=b;j=b.bit_length()-1;first+=1
            opts=dis[i]&dis[j];o=opts;count=0
            while o:
                z=o&-o;o^=z;count+=(opts&partner[z.bit_length()-1]).bit_count()
            if count:live+=1;totals[(six[i]&six[j]).bit_count()]+=count
            else:zero+=1
    assert sum(totals.values())%2==0
    return dict(record=n,admissible_pairs=first,pairs_with_disjoint_partner=live,ordered_by_first_overlap=dict(sorted(totals.items())),unoriented_quadruples=sum(totals.values())//2)
if __name__=='__main__':
    import json
    for n in (49241,49289,49915,49939):print(json.dumps(census(n)),flush=True)
