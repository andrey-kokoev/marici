"""Split exact deletion-deck collision classes by five-set overlap, then test eligibility."""
from ramsey_36_try_deck import data,unpack,Path,TemporaryDirectory,run,os
from itertools import combinations
from collections import defaultdict,Counter

def records(g):
    ind=[0];adj=unpack(g).get_adjlist()
    for i,nb in enumerate(adj):
        mask=sum(1<<j for j in nb);ind += [s|1<<i for s in ind if not s&mask]
    five=[s for s in ind if s.bit_count()==5];counts=Counter((s&t).bit_count() for s,t in combinations(five,2));overlap=tuple(counts[i] for i in range(5))
    def poly(v):
        c=[0]*6
        for s in ind:
            if not s&v:c[s.bit_count()]+=1
        return tuple(c)
    return poly(0),tuple(sorted(poly(1<<i) for i in range(len(adj)))),overlap

def main():
    hosts=list(map(unpack,data(17).splitlines()))
    def hits(g):return [i+1 for i,h in enumerate(hosts) if h.subisomorphic_lad(unpack(g),induced=True)]
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/('deck.exe' if os.name=='nt' else 'deck');run(['rustc','-O',str(Path(__file__).with_name('ramsey_36_deck_collision.rs')),'-o',str(exe)],check=True)
        for n in range(1,18):
            d=data(n);pairs=run([str(exe)],input=d,capture_output=True,check=True).stdout.splitlines();groups=defaultdict(list)
            for row in pairs:
                a,b=row.split();groups[a].append(b)
            for a,others in groups.items():
                by=defaultdict(list)
                for g in [a,*others]:by[records(g)].append(g)
                for rec,gs in by.items():
                    if len(gs)<2:continue
                    first=hits(gs[0]);
                    for g in gs[1:]:
                        second=hits(g)
                        if bool(first)!=bool(second):
                            print('order',n,'pair',gs[0],first,g,second,'polynomial',rec[0],'overlap',rec[2]);return
            print('exhausted',n,len(d.splitlines()),flush=True)
if __name__=='__main__':main()
