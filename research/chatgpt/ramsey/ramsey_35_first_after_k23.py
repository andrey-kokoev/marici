"""Find the first legal K2,3-free bases absent from the complete order-13 deletion map."""
from ramsey_bottom_up_compare import children,graph,key
from itertools import combinations
from pathlib import Path
import gzip

def free(g):
    ns=list(map(set,g.get_adjlist()))
    return all(len(a&b)<3 for a,b in combinations(ns,2))

def main():
    eligible={}
    with gzip.open(Path(__file__).with_name('ramsey_border_35_13_to_0.tsv.gz'),'rt') as f:
        next(f)
        for line in f:
            n,c,p,_=line.split();n=int(n);eligible.setdefault(n,set()).add(int(c,16));eligible.setdefault(n+1,set()).add(int(p,16))
    pool={0}
    for n in range(14):
        assert eligible[n]<=pool
        missing=pool-eligible[n];print(n,len(pool),len(missing))
        if missing:
            for m in sorted(missing):
                g=graph(n,m);print(hex(m),g.get_edgelist());
                for v in range(n):
                    h=g.copy();h.delete_vertices(v);assert key(h) in eligible[n-1]
            return
        pool={c for m in pool for c in children(n,m,5) if free(graph(n+1,c))}
if __name__=='__main__':main()
