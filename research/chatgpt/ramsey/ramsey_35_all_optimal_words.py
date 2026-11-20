"""All four-correction endpoint words and all distinct labelled target repairs.
Normalize endpoints by first occurrence. Do not quotient by reversal.
"""
from collections import defaultdict,Counter
from ramsey_35_min_nonjoins import N,adj
from ramsey_35_blind_repair import solve

def enumerate_repairs():
    repairs=defaultdict(set);orders=0
    def audit(order):
        nonlocal orders
        orders+=1; target=[sum(1<<i for i in range(j) if adj(v,order[i])) for j,v in enumerate(order)]
        def rec(w,used,fix):
            j=len(w)-1
            if j==N:
                assert len(fix)==4;repairs[w].add(fix);return
            enders=sum(1<<i for i in range(j) if w[i+1]==w[j]);want=target[j]
            if enders&~want:return
            for y in range(used+1):
                p=enders|sum(1<<i for i in range(j) if w[i]==y);missing=want&~p
                if p&~want or len(fix)+missing.bit_count()>4:continue
                rec(w+(y,),max(used,y+1),fix+tuple((i+1,j+1) for i in range(j) if missing>>i&1))
        rec((0,),1,())
    def walk(order):
        if len(order)==N:audit(order);return
        for v in range(N):
            if v not in order and adj(order[-1],v):walk(order+[v])
    walk([0,1]);return orders,repairs

def main():
    orders,repairs=enumerate_repairs();print('orders',orders,'words',len(repairs),'repairs per word',Counter(map(len,repairs.values())))
    w=min(repairs,key=lambda w:(len(repairs[w]),w));word=''.join(chr(65+i) for i in w);print('example',word,repairs[w]);assert {frozenset(r) for r in solve(word)}=={frozenset(r) for r in repairs[w]}
if __name__=='__main__':main()
