"""Eliminate port colors at fixed rows/seam, not across different endpoints."""
from ramsey_repair_next_seam import graph,grow,sevens,check,D,combinations,sha256,json
from collections import Counter

def run():
    src=D.parent/'ramsey_port_repair_orbits.json';r=json.loads(src.read_text());S=[tuple(x-1 for x in s) for s in r['supports']];T=grow(S,r['gap']);pairs=list(combinations(range(5),2));eligible={i for i,(a,b) in enumerate(pairs) if set(S[a]).isdisjoint(S[b])};cl={frozenset(i for i in eligible if all(x+9 in q for x in pairs[i])) for q in sevens(graph(9,T,0))};cl=[s for s in cl if not any(r<s for r in cl)];assert len(cl)==2 and cl[0].isdisjoint(cl[1])
    choices=[];legal=Counter()
    for m in range(1<<10):
        bits={i for i in range(10) if m>>i&1};direct=check(graph(8,S,m),8191,3,7) and check(graph(9,T,m),16383,3,7);pred=bits<=eligible and all(bits&s for s in cl);assert direct==pred
        if direct:
            legal[len(bits)]+=1
            if len(bits)==2:
                edge=lambda i,j:int(pairs.index((i-1,j-1)) in bits);choices.append((edge(2,4)-edge(3,4),edge(2,5)-edge(3,5)))
    assert sorted(choices)==[(-1,-1),(-1,1),(1,-1),(1,1)];out=dict(protocol_sha=sha256((D.parent/'ramsey_relative_sign_protocol.md').read_bytes()).hexdigest(),clauses=sorted(sorted([a+1,b+1] for a,b in [pairs[i] for i in s]) for s in cl),legal_by_cost=legal,min_signs=sorted(choices),colorings_checked=1024);print(out);p=D.parent/'ramsey_relative_sign.json';s=json.dumps(out,indent=2)+'\n';assert not p.exists() or p.read_text()==s;p.write_text(s)
if __name__=='__main__':run()
