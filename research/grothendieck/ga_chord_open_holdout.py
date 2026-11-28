"""Search one-support toggles of the unique-triple parent for an essential reopened gap."""
from ga_chord_restore import S,graph,check,fivegate,demands,mask,combinations,minimal,cost
from unittest.mock import patch

def run():
    counts=[0,0,0];c=192
    for port in range(5):
        for site in range(9):
            T=list(S);T[port]=tuple(sorted(set(T[port])^{site}));a=graph(9,T,c)
            if not check(a,16383,3,7):continue
            counts[0]+=1;D=demands(T,c);gates={g for g in range(1,9) if fivegate(a,g)}
            for i,j in combinations(range(9),2):
                if j==i+1 or a[i]&a[j]:continue
                counts[1]+=1;h=a.copy();h[i]|=1<<j;h[j]|=1<<i;opened={g for g in gates if not fivegate(h,g)}
                if not opened:continue
                counts[2]+=1
                with patch('ga_seam_residual.graph',return_value=h):H=demands(T,c)
                old=minimal({w for (g,p),w in H.items() if g not in opened});new=minimal(set(H.values()));extra=new-old
                if extra:
                    w=min(extra,key=lambda w:(len(w),sorted(w)));m=next(m for m in H if H[m]==w);assert m[0] in opened and m not in D and not any(q<=w for q in old)
                    k=cost(old);pool=sorted(set().union(*old,*new));opts=[t for t in combinations(pool,k) if all(not v.isdisjoint(t) for v in old)];print('other-gaps optima and full validity',[(t,all(not v.isdisjoint(t) for v in new)) for t in opts]);assert check(h,16383,3,7)
                    print('counts to first',counts,'port/site/remove?',port+1,site+1,site in S[port],'chord',i+1,j+1,'opened',opened,'move',m,'blades',sorted(w),'old versus full cost',cost(old),cost(new));print('supports',[[i+1 for i in t] for t in T]);return
    print('no separating case',counts)
if __name__=='__main__':run()
