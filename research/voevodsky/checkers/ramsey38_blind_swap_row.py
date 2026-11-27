"""Predict an entire masked row from a visible swap repeated on a disjoint tail."""
from ramsey38_visible_swap_path import prev,gzip,json,graph,Counter,combinations,sys
from collections import defaultdict
from fractions import Fraction
P=prev.out/'ramsey38_blind_swap_row_protocol.json';R=prev.out/'ramsey38_blind_swap_row_results.json'
protocol=dict(start=310449,records=128,root='Least degree-seven root of each consecutive record, all outside rows masked in turn, no requirement on hidden size or overlap.',prediction='From visible distinct triples U+x,U+y record unordered exchange x,y. Apply it to a third visible triple V+x or V+y with U disjoint V. Predict the unseen opposite triple. Exclude already visible supports; exclude any proposal making a red triangle with a visible core neighbor of the hidden vertex. No hidden row colors used in proposal.',control='Uniform equal-sized subset of all novel triangle-safe triples one swap from a visible triple, same query. Exact expected hits (no Monte Carlo). Count proposal occurrences and exact reconstruction, including abstentions. No claim alternatives are illegal Ramsey completions.')
def propose(L,rows,neighbors):
    triples={s for s in rows.values() if len(s)==3};tails=defaultdict(set)
    for a,b in combinations(triples,2):
        if len(a&b)==2:tails[a^b].add(a&b)
    forbidden=set().union(*(rows[v] for v in neighbors));base=set();choices=set()
    for s in triples:
        for x in s:
            v=s-{x}
            for y in L-s:
                q=v|{y}
                if q in triples or q&forbidden:continue
                base.add(q)
                if any(not(v&u) for u in tails[frozenset((x,y))]):choices.add(q)
    return choices,base

def run():
    assert json.loads(P.read_text())==protocol;cnt=Counter();expected=Fraction();out=[];example=None
    with gzip.open(prev.catalogue,'rt') as f:
        for i,w in enumerate(f,1):
            if i<protocol['start']:continue
            if i>=protocol['start']+protocol['records']:break
            g=graph(w.strip());u=next((v for v in sorted(g) if len(g[v])==7),None);cnt['records']+=1
            if u is None:continue
            L=g[u];outside=set(g)-L-{u};c=Counter();null=Fraction()
            for v in sorted(outside):
                vis={j:frozenset(g[j]&L) for j in outside-{v}};choices,base=propose(L,vis,g[v]&outside);truth=g[v]&L
                assert choices<=base;c['masked']+=1;c['triple_truth']+=len(truth)==3;c['baseline_recoverable']+=truth in base;c['issued']+=bool(choices);c['proposals']+=len(choices);c['hits']+=truth in choices
                if truth in base:null+=Fraction(len(choices),len(base))
                if truth in choices and example is None:example=dict(record=i,root=u,hidden_row=v,truth=sorted(truth),proposals=sorted(map(sorted,choices)),control_pool=len(base))
            out.append(dict(record=i,root=u,counts=dict(c),control_expected=float(null)));cnt.update(c);expected+=null
    print(cnt,float(expected),example);prev.save(R,dict(protocol_sha=prev.sha(P.read_bytes()),counts=dict(cnt),expected_same_budget=float(expected),example=example,per_root=out))
if __name__=='__main__':{'freeze':lambda:prev.save(P,protocol),'test':run}[sys.argv[1]]()
