"""Same lexicographic peel with local vs batch-wide normalized remainder cache."""
from ramsey38_surface_fiber_profile import base,parallel_chains,parity_basis,median,perf_counter_ns,gc
from itertools import combinations,permutations
from collections import Counter,defaultdict

class Peeler:
    def __init__(self,shared,track=False):
        self.shared=shared;self.track=track;self.memo={};self.count=Counter();self.owners=defaultdict(set);self.roots=set();self.ts=list(map(frozenset,combinations(range(7),4)));self.idx={tuple(sorted(t)):i for i,t in enumerate(self.ts)};self.tab=[]
        for t in self.ts:
            fs=list(map(frozenset,combinations(t,3)));adj=[sum(1<<j for j,u in enumerate(self.ts) if u!=t and f<=u) for f in fs];rules=[]
            for k in range(16):
                hits=[f for i,f in enumerate(fs) if k>>i&1];rules.append(sum(1<<j for j,u in enumerate(self.ts) if not any((u&t)<=f for f in hits)) if 0<k<15 else -1)
            self.tab.append((adj,rules))
    def peel(self,m,root):
        if m in self.memo:return self.memo[m]
        if self.track:self.owners[m].add(root)
        self.count['expanded']+=1;bits=m;ans=()
        while bits:
            b=bits&-bits;bits-=b;i=b.bit_length()-1;rest=m^b
            if not rest:ans=(i,);break
            adj,rules=self.tab[i];k=0
            for j,a in enumerate(adj):
                h=a&rest
                if h:
                    if h&(h-1):break
                    k|=1<<j
            else:
                if not rules[k]&rest:
                    o=self.peel(rest,root)
                    if o:ans=o+(i,);break
        self.memo[m]=ans;return ans
    def __call__(self,ts):
        labs=sorted(set().union(*ts));rename={v:i for i,v in enumerate(labs)};m=sum(1<<self.idx[tuple(sorted(rename[v] for v in t))] for t in ts);self.roots.add(m)
        if not self.shared:self.memo.clear()
        o=self.peel(m,m);return tuple(frozenset(labs[i] for i in self.ts[j]) for j in o)

def run():
    data=base.json.loads(base.P.read_text());base.templates();orig=base.shelling;old=base.face_assignments;gold=None;ref=None;times=[];stats={};capt={};modes=('original','local','shared')
    try:
        base.face_assignments=parallel_chains
        for order in permutations(modes):
            rnd={}
            for k in order:
                gc.collect();parity_basis.cache_clear();seen=[];start=perf_counter_ns();solver=orig if k=='original' else Peeler(k=='shared');
                def check(ts):
                    o=solver(ts);seen.append(o);return o
                base.shelling=check;result=base.run(data,'join');rnd[k]=(perf_counter_ns()-start)/1e6
                if gold is None:gold=result;ref=seen
                assert result==gold and seen==ref
                if k!='original':stats[k]=dict(expanded=solver.count['expanded'],unique_roots=len(solver.roots))
            times.append(rnd);print(rnd,flush=True)
        probe=Peeler(False,True);base.shelling=probe;assert base.run(data,'join')==gold
        hist=Counter(len(rr) for rr in probe.owners.values());stats['overlap']=dict(unique_states=len(hist) and len(probe.owners),shared_across_distinct_roots=sum(n for k,n in hist.items() if k>1),shared_proper_remainders=sum(sum(m!=r for r in rr)>=2 for m,rr in probe.owners.items()),owners_histogram=dict(hist));med={k:median(r[k] for r in times) for k in modes};print(stats,med,len(ref),sum(bool(o) for o in ref));base.prev.save(base.prev.out/'ramsey38_shared_peel_trial.json',dict(sample_sha=base.prev.sha(base.P.read_bytes()),mode_stats=stats,median_ms=med,rounds_ms=times,calls=len(ref),shellable=sum(bool(o) for o in ref),protocol='All 6 mode orders. Timed full joined batch including basis and peel table construction; warm universal sphere library. Exact deterministic shelling orders checked per call, including empty failures. Overlap instrumentation in a separate untimed replay.'))
    finally:base.shelling=orig;base.face_assignments=old
if __name__=='__main__':run()
