"""Generate 27-address seeds by offset rules; no catalogue graph or deleted rows.
Use a period of 35 (target order), four distinct undirected positive offsets.
Keep the same rule when bordering. Test for a forbidden set at each new vertex.
"""
from itertools import combinations

def unwitnessed(D):
    A=[{j for j in range(27) if min(abs(i-j),35-abs(i-j)) in D} for i in range(27)]
    return sum(j not in A[i] and not A[i]&A[j] for i,j in combinations(range(27),2))

def sizes(D,limit=35):
    S=set(D)|{35-d for d in D};rows=[]
    # A forbidden set is invariant under translation of its least address to 0.
    # Track independent sets containing 0 only. Likewise a triangle can start at 0.
    indep=[1]
    for j in range(1,limit):
        p=sum(1<<i for i in range(j) if j-i in S)
        if j in S and any(i in S and j-i in S for i in range(1,j)):return j
        new=[s|1<<j for s in indep if not s&p]
        if any(s.bit_count()==9 for s in new):return j
        indep+=new
    return limit

if __name__=='__main__':
    seeds=[d for d in combinations(range(1,18),4) if sizes(d,27)==27];rank=sorted((unwitnessed(d),d) for d in seeds);print('top seeds',rank[:2], 'winner reaches',sizes(rank[0][1]))
    from collections import Counter
    c=Counter();wins=[]
    for d in combinations(range(1,18),4):
        n=sizes(d);c[n]+=1
        if n==35:wins.append(d)
    print('rules',sum(c.values()),'valid at 27',sum(v for n,v in c.items() if n>=27),'reach 35',len(wins),'first',wins[:1])
