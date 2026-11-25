"""Exact S3 standard-representation certificate for the last degree-three attachment.
Reuses the independently reconstructed individual support library; no optimizer needed.
"""
from collections import Counter
from ramsey310_d3_last_supply import A,E,C,need

def coordinates(weights):
    out=[]
    for l,r in zip(E[:3],E[3:]):
        h=0
        for v,w in enumerate(weights):
            d=A[v].bit_count()
            h+=w*((((l|r)>>v)&1) if d==5 else ((l>>v)&1)*((d==4)-(d==7)))
        out.append(h)
    return out

demand=coordinates(need)
score=Counter()
for row in C:
    a,b,c=coordinates([row>>i&1 for i in range(26)])
    score[a-c]+=1
assert len(C)==103 and max(score)==0 and demand[0]-demand[2]==1
print('demand coordinates',demand,'row contrast histogram',dict(sorted(score.items())))
