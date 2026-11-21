"""Target-independent deletion-core chain test on generated witnesses. Pair-clique pruning and exact higher subset checks."""
import json,sys
from pathlib import Path
from collections import Counter
from itertools import combinations
from ramsey_port_clique_transfer import induce,independent
D=Path(__file__).parent

def search(H,k,d,visit=None):
    n=len(H);inds=[0];F=(1<<n)-1
    for v,r in enumerate(H):inds += [s|1<<v for s in inds if not s&r]
    M=[s for s in inds if all(s>>i&1 or s&r for i,r in enumerate(H))];top=[t for t in inds if t.bit_count()==k-2];assert max(t.bit_count() for t in inds)<=k-2
    flags=[sum(1<<j for j,t in enumerate(top) if t>>v&1) for v in range(n)];miss=[]
    for s in M:
        h=0
        for v in range(n):
            if s>>v&1:h|=flags[v]
        miss.append(((1<<len(top))-1)^h)
    saturated=sum(1<<v for v,row in enumerate(H) if row.bit_count()==k-2)
    adj=[0]*len(M);pairs=0
    for i,a in enumerate(miss):
        for j in range(i,len(M)):
            if not (a&miss[j] or M[i]&M[j]&saturated):adj[i]|=1<<j;adj[j]|=1<<i;pairs+=1
    loops=sum(1<<i for i,a in enumerate(miss) if not a and not M[i]&saturated);hist=Counter();reject=Counter()
    def dfs(opts,B,ids):
        hist[len(ids)]+=1
        if len(ids)==d:
            if visit is None:return ids,B
            G=[r|((v>=n)<<len(B)) for v,r in enumerate(B)]+[((1<<d)-1)<<n]
            visit([M[i] for i in ids],G);return None
        while opts:
            if not opts&loops and opts.bit_count()<d-len(ids):break
            b=opts&-opts;i=b.bit_length()-1;opts^=b;s=M[i];nxt=(opts|b)&adj[i];need=d-len(ids)-1
            if not nxt&loops and nxt.bit_count()<need:continue
            if len(ids)>=2 and independent(B,((1<<len(B))-1)^s,k-1):reject[len(ids)+1]+=1;continue
            C=[r|((s>>v&1)<<len(B)) for v,r in enumerate(B)]+[s];ans=dfs(nxt,C,ids+[i]);
            if ans:return ans
    ans=dfs((1<<len(M))-1,H,[]);out={'maximal':len(M),'pairs':pairs,'loops':loops.bit_count(),'visited':dict(hist),'higher_rejections':dict(reject)}
    if ans:
        ids,B=ans;G=[r|((v>=n)<<len(B)) for v,r in enumerate(B)]+[((1<<d)-1)<<n];assert not independent(G,(1<<len(G))-1,k) and all(not(G[i]&G[j]) for i,j in combinations(range(len(G)),2) if G[i]>>j&1);out.update(supports=[M[i] for i in ids],graph=G)
    return out
if __name__=='__main__':
    k=int(sys.argv[1]);A=json.loads((D/f'ramsey_port_clique_k{k-1}.json').read_text())['graph'];d={8:4,9:8,10:4}[k];rows=[]
    for v in ([-1] if k==8 else range(len(A))):
        H=induce(A,[i for i in range(len(A)) if i!=v]);r=search(H,k,d);r['deleted']=v;rows.append(r);print(k,v,r,flush=True);(D/f'ramsey_port_deletion_chain_{k}.json').write_text(json.dumps(rows)+'\n')
        if 'graph' in r:break
