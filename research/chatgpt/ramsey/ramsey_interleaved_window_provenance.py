"""Restore intermediate Hall partitions. Compare exposing only each partition's unique unvisited duad with exposing its entire support, using at most one event per Hall position."""
from ramsey_diagonal_window_provenance import cycle,m,r,orient,X,P,D,json,tours,permutations
from ramsey_first_fan_rim_probe import T
from itertools import combinations

def run():
    c=cycle(m);out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        for t in (c,[r[i] for i in c]):
            a,b=orient(t[::2],X)[-1]['arrow'];win=t[-2:]+t[:3];reports={}
            for mode in ('unused','whole','shared'):
                slots=[]
                for i,j in enumerate(win):
                    if j<15:q=P[j]
                    else:
                        ds=T[j-15];un,=set(ds)-{P[win[i-1]],P[win[i+1]]};q=un if mode=='unused' else sum(ds,())
                        if mode=='shared':
                            q,=set(ds)&set(T[win[4-i]-15]);assert q==P[win[2]]
                    slots.append({frozenset(p[v-1] for v in X[k]) for k in q})
                fits=[]
                for tr in tours():
                    w=tr['word'];k,=[k for k,e in enumerate(w) if e[0]==p[a-1]];w=w[k:]+w[:k];j,=[k for k,e in enumerate(w) if e[1]==p[b-1]];arc=w[:j+1];seq=[s for s in combinations(range(5),len(arc)) if all(frozenset(e) in slots[i] for e,i in zip(arc,s))];fits.append(dict(length=len(arc),slots=seq))
                reports[mode]=sorted(fits,key=lambda x:x['length'])
            assert [bool(f['slots']) for f in reports['shared']]==[True,False]
            out.append(dict(binding=''.join(p),window=win,reports=reports))
    return out
if __name__=='__main__':
    out=run();print(out[:2]);(D/'ramsey_interleaved_window_provenance.json').write_text(json.dumps(out)+'\n')
