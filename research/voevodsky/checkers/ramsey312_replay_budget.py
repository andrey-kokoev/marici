"""Replay capacity certificates from the matrix, without the enumerator's support list. Search for an independent red support hitting all independent elevens but none of the classes."""
from ramsey312_google_two_step import *
from collections import Counter

def main():
 el=list(sets(F,11));catalog=set(el);stats=Counter();result=[]
 for r in json.loads((D/'ramsey312_budget_cover.json').read_text()):
    d=r['d'];h=F^sum(1<<i for i in d);cert=r['cert'];assert cert is not None;C=[[-(i+1),-(j+1)] for i in bits(h) for j in bits(h&adj[i]&((1<<i)-1))]+[[i+1 for i in bits(t)] for t in el if not t&~h];ks=[];groups=[]
    for m,b,t in cert:
        k=11-t.bit_count();assert b.bit_count()==1 and not (t|b)&~h and all(not adj[i]&t for i in bits(t));ks.append(k);C.append([-b.bit_length(),*[i+1 for i in bits(t)]]);groups.append([z for z in d if adj[z]&b and not adj[z]&t]);assert len(groups[-1])==k
    shadows=[t|sum(1<<z for z in group) for (m,b,t),group in zip(cert,groups)];assert all(u in catalog for u in shadows);assert sum(ks)==6
    with Solver(name='g4',bootstrap_with=C) as sl:assert not sl.solve()
    stats[tuple(sorted(ks))]+=1;result.append(dict(d=d,replayed=True,double=groups[ks.index(2)],original_elevens=shadows))
 print('replayed',stats);(D/'ramsey312_budget_replay.json').write_text(json.dumps(result))
if __name__=='__main__':main()
