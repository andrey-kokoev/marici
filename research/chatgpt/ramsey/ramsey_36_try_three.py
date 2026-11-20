"""Exhaust the order-13 prediction. Rust hash rejects only impossible matches;
compare exact coloured incidence structures for mixed eligibility buckets."""
from ramsey_36_try_deck import data, unpack, Path, TemporaryDirectory, run, os
from ramsey_border_order import key
from itertools import combinations,combinations_with_replacement
from collections import defaultdict,Counter
import igraph as ig

def exact(g):
    I=[0]
    for i,ns in enumerate(g.get_adjlist()):
        a=sum(1<<j for j in ns);I += [s|1<<i for s in I if not s&a]
    sets=lambda k:[s for s in I if s.bit_count()==k]
    five,four,three=map(sets,(5,4,3));o=[s for s in I if all(s&t for t in five)];n=len(o)
    t=[[int(not(p&q))+2*int(all((p|q)&s for s in four)) for q in o] for p in o]
    color=[row[i] for i,row in enumerate(t)];edges=[]
    def node(c):i=len(color);color.append(c);return i
    for i,j in combinations(range(n),2):
        if t[i][j]:v=node(4+t[i][j]);edges.extend([(v,i),(v,j)])
    for i,j,k in combinations_with_replacement(range(n),3):
        if t[i][j]&t[i][k]&t[j][k]&2 and all((o[i]|o[j]|o[k])&s for s in three):
            v=node(8)
            for q,m in Counter((i,j,k)).items():
                u=node(8+m);edges.extend([(v,u),(u,q)])
    h=ig.Graph(len(color),edges);h.vs['c']=color;h=h.permute_vertices(h.canonical_permutation(color=color));return tuple(h.vs['c']),tuple(sorted(tuple(sorted(e)) for e in h.get_edgelist()))

def main(n=13):
    hosts=list(map(unpack,data(17).splitlines()));eligible=set()
    for h in hosts:
        for keep in combinations(range(17),n):eligible.add(key(h.induced_subgraph(keep)))
    raw=data(n)
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/('filter.exe' if os.name=='nt' else 'filter');run(['rustc','-O',str(Path(__file__).with_name('ramsey_36_three_filter.rs')),'-o',str(exe)],check=True)
        hashes=run([str(exe)],input=raw,capture_output=True,check=True).stdout.splitlines()
    groups=defaultdict(list);records=raw.splitlines();assert len(records)==len(hashes)
    for s,h in zip(records,hashes):groups[h].append(s)
    mixed=0
    for group in groups.values():
        if len(group)<2:continue
        yes=[];no=[]
        for s in group:(yes if key(unpack(s)) in eligible else no).append(s)
        if not yes or not no:continue
        mixed+=1;eq={exact(unpack(s)):s for s in yes}
        for s in no:
            e=exact(unpack(s))
            if e in eq:
                for x in [eq[e],s]:print(x,[i+1 for i,h in enumerate(hosts) if h.subisomorphic_lad(unpack(x),induced=True)])
                return
    print('no counterexample',len(records),'eligible',len(eligible),'mixed filter buckets',mixed)
if __name__=='__main__':
    import sys
    main(int(sys.argv[1]) if len(sys.argv)>1 else 13)
