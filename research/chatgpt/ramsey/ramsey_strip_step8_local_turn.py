"""Predict visit 8 from the seven folded visits, with no matching or endpoint input. Only the verification phase counts Hall completions for each adjacent raw position."""
from ramsey_strip_prefix_geometry import labels,rep,r,N
from ramsey_strip_prefix_forks import rows,count,flag,Counter

def next_label(s):
    # Lowercase + digit: rim corner and layer; capital: midpoint / switch.
    first=next(i for i,x in enumerate(s[1:],2) if len(x)==1)
    if first==4:
        assert len(s[-1])==1
        return s[-1].lower()+str(1-int(s[-2][1]))
    if first==5 and s[-1][0]==s[2][0]:return s[-1][0].upper()
    assert first in (5,6);return s[0].lower()+s[-1][1]
seen=set();h=Counter()
for z in rows:
    p=z['path'];q=p[:8];dest=next_label([labels[rep(x)] for x in q[1:]]);v,=[v for v in N[q[-1]] if labels.get(rep(v))==dest];assert (p[8]==v)==z['closes'];h[z['closes']]+=1
    for parity in range(2):
        key=tuple(q),parity
        if key in seen:continue
        seen.add(key);obs=[flag(x,y) if i%2==parity else flag(r[x],r[y]) for i,(x,y) in enumerate(zip(q,q[1:]))];poss=[]
        for y in N[q[-1]]:
            edge=flag(q[-1],y) if 7%2==parity else flag(r[q[-1]],r[y]);trial=set(obs)|{edge}
            if len({i for i,j in trial})==len({j for i,j in trial})==len(trial) and count(trial):poss.append(y)
        assert poss==[v]
print('Verified unique raw neighbor:',len(seen),'oriented prefixes; follows rule by closure:',h)
