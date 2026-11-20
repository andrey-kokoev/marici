"""Pole link sensitivity: recompute signed flag table, duplex decoding and legal one-edge toggles in both states, without changing any other adjacency. Report graph colors separately from ordered overlap signs."""
from pathlib import Path
from itertools import combinations
import json
D=Path(__file__).resolve().parents[1]/'results';load=lambda f:json.loads((D/(f+'.json')).read_text());w=load('ramsey_37_dual_stars');V=set(range(22));p,q=0,6;orig=set(map(tuple,w['red_edges']));out=[]
def test(E):
    N={u:{v for v in V if tuple(sorted((u,v))) in E} for u in V};Z=N[p]-{q};W=N[q]-{p};M=V-Z-W-{p,q};stars={v:N[v]&M for v in Z|W};obs=[]
    for X,Y in [(Z,W),(W,Z)]:
        def pick(v,n):t,=[y for y in Y if len(stars[v]&stars[y])==n];return t
        mate={pick(v,0):v for v in X};succ={v:mate[pick(v,1)] for v in X}
        for v in sorted(X):
            for a in sorted(stars[v]):
                j,= [i for i in X-{v} if a in stars[i]];opp=[i for i in Y if a in stars[i]];support=lambda x:sum(len(stars[x]&stars[i]) for i in opp);k=v
                for h in range(5):
                    if k==j:break
                    k=succ[k]
                assert h in range(1,5);target,=stars[succ[v]]&stars[succ[j]];obs.append([v,a,j,h if h<=2 else h-5,support(j)-support(v),int(target in N[a])])
    def common(t):return sorted(set.intersection(*(N[v] for v in t)))
    marks=[(7,5,12),(7,15,12),(9,5,13),(9,15,13)];ind=[frozenset()];
    for v in sorted(V):ind += [s|{v} for s in ind if not s&N[v]]
    assert max(map(len,ind))==6 and not any(N[a]&N[b] for a,b in E);fives=[s for s in ind if len(s)==5];flips=[]
    for a,b in combinations(sorted(V),2):
        if (a,b) in E:
            if not any(not(s&(N[a]|N[b]|{a,b})) for s in fives):flips.append((a,b))
        elif not N[a]&N[b]:flips.append((a,b))
    return dict(pole_edge_red=(p,q) in E,observations=obs,mark_decoders=[common(t) for t in marks],legal_flips=flips,blue_sixes=sum(len(s)==6 for s in ind))
out=[test(orig),test(orig-{(p,q)})];assert len(out[0]['observations'])==40 and all(out[0][k]==out[1][k] for k in ('observations','mark_decoders'));print([(r['pole_edge_red'],len(r['legal_flips']),r['blue_sixes'],r['mark_decoders']) for r in out]);print(out[0]['legal_flips']);(D/'ramsey_37_pole_bit_readout.json').write_text(json.dumps(out,indent=2)+'\n')
