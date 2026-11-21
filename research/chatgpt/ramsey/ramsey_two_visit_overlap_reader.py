"""Intrinsic 2-duad lookahead reader: successive Hall partitions through a duad are different pairings of its four unused ground labels. No move/hold simulation or color test."""
from ramsey_uniform_rim_scan import *
from itertools import permutations

def tokens(ds):
    out=[]
    for i,d in enumerate(ds):
        x,=set(P[d])&set(P[ds[(i+2)%len(ds)]]);out.append(X[x])
    return out

def project(ds):
    w=tokens(ds);v=1;vis=[v];why=[]
    for e in w:
        if e not in rim:why.append('diagonal');continue
        if v not in e:return w,None
        v=sum(e)-v;vis.append(v)
    return w,vis

def run():
    ds=cycle(m)[::2];selected=[]
    for t in (ds,[r[d] for d in ds]):
        w,walk=project(t);assert circuit(walk);selected.append(dict(duads=t,tokens=w,rim_walk=walk))
    h=Counter();words=Counter();
    def dfs(i,used,M):
        if i==15:
            c=cycle(M);w,walk=project(c[::2]);ok=bool(walk and circuit(walk));h[len(c),29 in c,ok]+=1
            if ok:words[tuple(c)]+=1
            return
        for j,u in enumerate(T,15):
            if P[i] in u and j not in used and (i!=0 or j==16) and (i!=7 or j==29):dfs(i+1,used|{j},M+[(i,j)])
    dfs(0,set(),[]);# Independently enumerate all simple five-hop pole paths with both boundary flags; no matching data.
    mids=[(0,16,P.index(d),j,7,29) for d in T[1] if d!=P[0] for j,t in enumerate(T,15) if j not in (16,29) and d!=P[7] and d in t and P[7] in t];assert len(mids)==1
    out=dict(selected=selected,passing_cycles=list(words.items()),controls=[[list(k),n] for k,n in sorted(h.items())],possible_short_halves=mids);print(out);return out
if __name__=='__main__':(D/'ramsey_two_visit_overlap_reader.json').write_text(json.dumps(run())+'\n')
