"""Challenge every five-class result directly against the original graph, without enumerated support lists."""
from ramsey312_google_two_step import *
from collections import Counter

def main():
 el=list(sets(F,11));expected={tuple(map(int,l.split())) for l in (D/'ramsey312_five_targets.txt').read_text().splitlines()};seen=set();counts=Counter();largest=None;total=0
 for f in sorted(D.glob('ramsey312_five_repair_*.jsonl')):
    for l in f.open():
        r=json.loads(l);d=tuple(r['d']);assert d in expected-seen;seen.add(d);h=F^sum(1<<v for v in d);lo=sum(1<<v for v in bits(h) if (adj[v]&h).bit_count()<11);cert=r['cert'];assert cert and len(cert)==5;total+=r['n'];largest=max(largest or (0,()),(r['n'],d));
        with Solver(name='g4',bootstrap_with=[[-1-v,-1-u] for v in bits(lo) for u in bits(adj[v]&lo&((1<<v)-1))]) as sl:
            for t in {s&lo for s in el if not s&~h}:sl.add_clause([v+1 for v in bits(t)])
            for (b,t),owner in zip(cert,d):
                assert b.bit_count()==1 and b&lo and b&adj[owner] and not t&adj[owner] and t.bit_count()==10 and not t&~h and all(not adj[v]&t for v in bits(t));sl.add_clause([-b.bit_length(),*[v+1 for v in bits(t&lo)]])
            assert not sl.solve();counts['exact_repair' if r['raw'] else 'nearest']+=1
 assert seen==expected;res=dict(counts=counts,supports=total,largest=largest,verified=len(seen));(D/'ramsey312_five_stress_summary.json').write_text(json.dumps(res));print(res)
if __name__=='__main__':main()
