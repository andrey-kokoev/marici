"""Partition ALL ordered single-decagon matching pairs into S6 orbits; test one representative per orbit. Dual reading via the same fixed correlation on both input and output (need not stabilize the pair)."""
from itertools import permutations
from ramsey_dual_shift_successor import direct,flags,action,move,polarity,D,json
from ramsey_history_matching_provenance import enum

def run():
    ms=list(enum());idx={s:i for i,s in enumerate(ms)};pairs={(i,j) for i,s in enumerate(ms) for j,t in enumerate(ms) if len(s&t)==10};f=polarity()[0]['map'];hs=[action(p) for p in permutations(range(6))];out=[]
    while pairs:
        i,j=min(pairs);s,t=ms[i],ms[j];orb={(idx[move(s,h)],idx[move(t,h)]) for h in hs};assert orb<=pairs;pairs-=orb
        adj={x:set() for x in range(30)}
        for x,y in flags-(s|t):adj[x].add(y);adj[y].add(x)
        lengths=[];ends=set()
        for y in range(30):
            if y in ends or len(adj[y])!=1:continue
            p=None;x=y;k=0
            while adj[x]-{p}:p,x=x,next(iter(adj[x]-{p}));k+=1
            ends.update((x,y));lengths.append(k)
        a={v:k for k,v in t};b=dict(s);z=next(iter(v for k,v in s^t));u=z;period=0
        while True:
            u=b[a[u]];period+=1
            if u==z:break
        ok=None
        if lengths==[3]*5:
            dd=direct(s,t);rev=direct(move(s,f),move(t,f));ok=sum(tuple(sorted(f[v] for v in rev[f[i0]][1]))==dd[b[a[y]]][1] for y,(i0,_) in dd.items())
        out.append(dict(representative=[i,j],size=len(orb),turn_period=period,lengths=sorted(lengths),correct=ok))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_ten_cycle_shift_census.json').write_text(json.dumps(out)+'\n')
