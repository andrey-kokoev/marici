"""Stronger control: preserve EVERY one- and two-site continuation before probing a blue triple. Equal single supports and disjointness decide the red case; five-row coverage decides the blue case. Include repeated supports."""
from ramsey_pin_depth import *
from itertools import combinations_with_replacement as cr

def run3():
    data=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()
    for rec,line in enumerate(data,1):
        n=19;g=nx.from_graph6_bytes(line);h=[sum(1<<j for j in g[i] if j<n) for i in range(n)];B,T=borders(h);U=sorted(B);tab={a|b:not any(t&(a|b)==0 for t in T) for a,b in cr(U,2)};four=[s for s in sets(h) if s.bit_count()==4]
        for i,j in combinations(range(n),2):
            flip=(1<<i)|(1<<j);sw=lambda s:s^flip if (s>>i^s>>j)&1 else s
            if any(sw(s) not in B for s in B) or any(tab[sw(u)]!=v for u,v in tab.items()) or not (h[i]^h[j])&~flip:continue
            for a,b,c in cr(U,3):
                if not all(tab[x|y] for x,y in combinations((a,b,c),2)):continue
                u=a|b|c;f=next((t for t in four if not t&u),0)
                if not f or any(not t&sw(u) for t in four):continue
                hh=[sw(h[j if k==i else i if k==j else k]) for k in range(n)];B2,T2=borders(hh);assert B==B2 and all(v==(not any(not t&u for t in T2)) for u,v in tab.items());ext=[]
                for old in (h,hh):
                    H=add(old,a,b);ext.append(check([v|((c>>k&1)<<len(H)) for k,v in enumerate(H)]+[c]))
                assert ext==[dict(alpha=7,triangles=0),dict(alpha=6,triangles=0)];return dict(record=rec,n=n,swap=[i,j],borders=len(B),two_support_multisets=len(list(cr(U,2))),red_supports=list(map(labels,(a,b,c))),missed_four=labels(f),extended=ext)
    return dict(records_without_example=len(data))
if __name__=='__main__':
    r=run3();print(r);(D/'ramsey_pin_depth_three.json').write_text(json.dumps(r,indent=2)+'\n')
