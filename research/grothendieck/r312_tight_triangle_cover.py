"""Search the equality case of the neighborhood-cover triangle bound."""
from r312_nearmiss_cover import old,adj,n
from itertools import combinations
assert set(old)==set(adj) and len(set(adj))==49
# Each edge must hit neighborhoods; each hit makes its own old-old-new triangle.
E={}
for a,b in combinations(range(n),2):
    m=adj[a]&adj[b]
    if m:E[a,b]=m

def partition(U,k,chosen):
    if not U:
        if k:return
        g=adj.copy()
        for a,b in chosen:g[a]|=1<<b;g[b]|=1<<a
        if sum((g[a]&g[b]).bit_count() for a,b in combinations(range(n),2) if g[a]>>b&1)==147:
            return chosen
        return
    if U.bit_count()>8*k or not k:return
    bit=U&-U
    for e,m in E.items():
        if m&bit and m&U==m and U.bit_count()-m.bit_count()<=8*(k-1):
            r=partition(U^m,k-1,chosen+[e])
            if r:return r

if __name__=='__main__':
    for d in range(1,25):
        if (0,d) not in E:continue
        r=partition(((1<<49)-1)^E[0,d],6,[(0,d)])
        if r:print('tight cover',r);break
    else:print('no tight seven-edge cover')
