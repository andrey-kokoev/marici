"""Use only traversed incidence flags with their matching identities. One event per flag, in path order. No expansion of a partition into unselected members."""
from itertools import combinations
from ramsey_diagonal_window_provenance import cycle,m,r,orient,X,P,D,json,tours,permutations

def run():
    c=cycle(m);n={(r[i],r[j]) for i,j in m};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        rows=[]
        for t in (c,[r[i] for i in c]):
            a,b=orient(t[::2],X)[-1]['arrow'];win=t[-2:]+t[:3];flags=[tuple(sorted(z)) for z in zip(win,win[1:])];owners=['m' if f in m else 'n' for f in flags];assert all((f in m)^(f in n) for f in flags);supports=[{frozenset(p[v-1] for v in X[k]) for k in P[d]} for d,j in flags];fits=[]
            for tr in tours():
                w=tr['word'];i,=[k for k,e in enumerate(w) if e[0]==p[a-1]];w=w[i:]+w[:i];j,=[k for k,e in enumerate(w) if e[1]==p[b-1]];arc=w[:j+1]
                for s in combinations(range(4),len(arc)):
                    if all(frozenset(e) in supports[k] for k,e in zip(s,arc)):fits.append(dict(arc=arc,slots=s,owner_order=[owners[k] for k in s],seam=tr['seam']))
            f,=fits;rows.append(dict(flags=flags,owners=owners,fit=f))
        assert rows[0]['fit']['owner_order']==rows[1]['fit']['owner_order'] and rows[0]['fit']['seam']!=rows[1]['fit']['seam'];out.append(dict(binding=''.join(p),rows=rows))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_handoff_flag_owners.json').write_text(json.dumps(out)+'\n')
