"""Compare eligibility signatures on all legal unlabelled (3,5) bases."""
import gzip
from pathlib import Path
from collections import defaultdict
from ramsey_bottom_up_compare import children,graph

def signatures(n,m):
    ind=[0]
    for i,nb in enumerate(graph(n,m).get_adjlist()):
        row=sum(1<<j for j in nb);ind += [s|1<<i for s in ind if not row&s]
    def coeff(omit):
        a=[0]*5
        for s in ind:
            if not s&omit:a[s.bit_count()]+=1
        return tuple(a)
    base=coeff(0);return base,(base,tuple(sorted(coeff(1<<v) for v in range(n))))

def main():
    eligible=defaultdict(set)
    with gzip.open(Path(__file__).with_name('ramsey_border_35_13_to_0.tsv.gz'),'rt') as f:
        next(f)
        for line in f:
            n,c,p,_=line.split();n=int(n);eligible[n].add(int(c,16));eligible[n+1].add(int(p,16))
    pool={0};first=True;tot=[0,0];count=0
    for n in range(14):
        groups=[defaultdict(dict),defaultdict(dict)];count+=len(pool);assert eligible[n]<=pool
        for m in sorted(pool):
            for g,sig in zip(groups,signatures(n,m)):g[sig].setdefault(m in eligible[n],m)
        for i,g in enumerate(groups):
            for sig,reps in g.items():
                if len(reps)<2:continue
                tot[i]+=1
                if i==0 and first:
                    print('first mixed signature:',n,sig)
                    for label,m in reps.items():print(label,graph(n,m).get_edgelist())
                    first=False
        if n<13:pool={c for m in pool for c in children(n,m,5)}
    print('bases, mixed signatures (plain, with vertex deletions)',count,tot)
if __name__=='__main__':main()
