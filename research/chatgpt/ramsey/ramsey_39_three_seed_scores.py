"""Compare three seed-only selection rules; use forward growth only for evaluation."""
from itertools import combinations
from ramsey_39_seed_offsets import sizes, unwitnessed

def scores(d):
    adj=[sum(1<<j for j in range(27) if min(abs(i-j),35-abs(i-j)) in d) for i in range(27)]
    ind=[0]
    for i,a in enumerate(adj):ind += [s|1<<i for s in ind if not s&a]
    deg=[a.bit_count() for a in adj]
    return unwitnessed(d),sum(s.bit_count()==8 for s in ind),27*sum(x*x for x in deg)-sum(deg)**2

if __name__=='__main__':
    pool={d:scores(d) for d in combinations(range(1,18),4) if sizes(d,27)==27}
    for i,name in enumerate(('unwitnessed links','negative octets','degree variance times 27^2')):
        best=min(v[i] for v in pool.values());print(name,best,[(d,sizes(d)) for d,v in pool.items() if v[i]==best])
