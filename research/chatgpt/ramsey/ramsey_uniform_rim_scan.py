"""Compare apex-only projection with a uniform move-if-available, otherwise hold scan of actual duads. The scan convention is a hypothesis, not native execution. Test all boundary-compatible matchings."""
from ramsey_first_fan_rim_probe import P,T,r,X,apex,m,D,json,Counter
from collections import defaultdict
rim={(1,2),(2,4),(3,4),(1,3)}
def cycle(M):
    adj=defaultdict(set)
    for i,j in set(M)^{(r[i],r[j]) for i,j in M}:adj[i].add(j);adj[j].add(i)
    t=[0,16]
    while True:
        u,=adj[t[-1]]-{t[-2]}
        if u==0:return t
        t.append(u)
def scan(ds):
    ps=[[1]]
    for d in ds:
        ps=[p+[v] for p in ps for v in ([sum(X[k])-p[-1] for k in P[d] if X[k] in rim and p[-1] in X[k]] or [p[-1]])]
    return ps
def circuit(p):
    reduced=[p[0]]+[b for a,b in zip(p,p[1:]) if a!=b];return len(reduced)==5 and reduced[-1]==1 and len(set(reduced))==4

def run():
    t=cycle(m);ds=t[::2];z=[scan(ds),scan(list(map(lambda i:r[i],ds)))];assert all(sum(map(circuit,q))==1 for q in z);h=Counter()
    def dfs(i,used,M):
        if i==15:
            c=cycle(M);paths=scan(c[::2]);h[(len(c),29 in c,apex(c[2]),sum(map(circuit,paths)))]+=1;return
        for j,u in enumerate(T,15):
            if P[i] in u and j not in used and (i!=0 or j==16) and (i!=7 or j==29):dfs(i+1,used|{j},M+[(i,j)])
    dfs(0,set(),[]);out=dict(cycle=t,duads=ds,apex_sequence=[apex(i) for i in ds],scan_paths=z,boundary_histogram=[[list(k),v] for k,v in sorted(h.items())]);print(out);return out
if __name__=='__main__':(D/'ramsey_uniform_rim_scan.json').write_text(json.dumps(run())+'\n')
