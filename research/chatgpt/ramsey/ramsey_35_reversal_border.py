"""Fixed end-row comparison; count legal borders on each normalized positive Hamilton order."""
from itertools import combinations
from ramsey_35_min_nonjoins import adj
from collections import Counter

def run():
    stats=Counter()
    def test(o):
        old=o[:-1];n=len(old);target=[adj(i,o[-1]) for i in old]
        def link(i,j):return i!=j and adj(old[i],old[j])
        p=[link(n-1,i)^link(0,n-1-i) for i in range(n)]
        # The last position compares diagonals. Supply its known positive chain join.
        p[-1]=True
        tri=any(p[i] and p[j] and link(i,j) for i,j in combinations(range(n),2))
        five=any(all(not p[i] for i in t) and not any(link(i,j) for i,j in combinations(t,2)) for t in combinations(range(n),4))
        stats['tested']+=1;stats['exact']+=p==target;stats['legal']+=not(tri or five);stats['triangle']+=tri;stats['negative five']+=five
    def walk(o):
        if len(o)==13:test(o);return
        for v in range(13):
            if v not in o and adj(v,o[-1]):walk(o+[v])
    walk([0,1]);print(stats)
if __name__=='__main__':run()
