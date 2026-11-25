"""Independent SAT replay on the complete unfiltered support family. Accepts shadow shard or nearest-shard receipts. No original support list needed."""
from ramsey312_google_two_step import *
import gzip
from collections import Counter

def main():
 E=list(sets(F,11));catalog=set(E);n=0;hist=Counter();f=sys.argv[1];near='nearest' in f
 for idx,l in enumerate(gzip.open(f,'rt')):
    if len(sys.argv)>2 and idx%int(sys.argv[3])!=int(sys.argv[2]):continue
    if near:
        z=l.split();d=sum(1<<int(i) for i in z[:6]);v=list(map(int,z[8:]));cs=list(zip(v[::2],v[1::2]))
    else:r=json.loads(l);d=r['d'];cs=[(b,t) for g,b,t in r['cert']]
    h=F^d;low=sum(1<<v for v in bits(h) if (adj[v]&h).bit_count()<11);budget=0
    # Restriction to low-degree red neighbors is sound: adding a red neighbor to a degree-11 vertex would create twelve independent neighbors.
    clauses=[[-i-1,-j-1] for i in bits(low) for j in bits(low&adj[i]&((1<<i)-1))];clauses.extend([v+1 for v in bits(t)] for t in {e&low for e in E if not e&d});
    for b,t in cs:
        k=11-t.bit_count();assert k>0 and b.bit_count()==1 and not (b|t)&d;grp=sum(1<<i for i in bits(d) if b&adj[i] and not t&adj[i]);assert grp.bit_count()==k and grp|t in catalog;budget+=k;clauses.append(([-b.bit_length()] if b&low else [])+[i+1 for i in bits(t&low)] if b&low else [-b.bit_length()]);
    assert budget==6
    with Solver(name='g4',bootstrap_with=clauses) as sl:assert not sl.solve()
    n+=1;hist[len(cs)]+=1
 print(Path(f).name,n,hist,flush=True)
if __name__=='__main__':main()
