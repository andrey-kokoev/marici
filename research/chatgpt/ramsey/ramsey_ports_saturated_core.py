"""Delete one vertex from the 35-cycle witness, then saturate some newly exposed pairs. No 39-input. Test four-port completion exactly."""
from functools import lru_cache
from itertools import combinations
from math import gcd
from collections import Counter
from pathlib import Path
import json
from ramsey_port_clique_transfer import graph,induce,independent
D=Path(__file__).parent

def four(H):
    n=len(H);F=(1<<n)-1;I=[0]
    for v,row in enumerate(H):I += [s|1<<v for s in I if not s&row]
    assert max(map(int.bit_count,I))==8
    M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(H))];T=[s for s in I if s.bit_count()==8];hit=[sum(1<<j for j,t in enumerate(T) if t>>v&1) for v in range(n)];allsets=(1<<len(T))-1;miss=[]
    for s in M:
        h=0
        for v in range(n):
            if s>>v&1:h|=hit[v]
        miss.append(allsets^h)
    sat=sum(1<<v for v,r in enumerate(H) if r.bit_count()==8);cnt=Counter();adj=[]
    for i,x in enumerate(M):
        hot=x&sat;a=miss[i];adj.append(sum(1<<j for j in range(i,len(M)) if not(hot&M[j] or a&miss[j])))
    @lru_cache(maxsize=100000)
    def ok(mask,k):return not independent(H,F^mask,k)
    def choices(bits):
        while bits:
            b=bits&-bits;bits-=b;yield b.bit_length()-1
    proof=None
    for i in range(len(M)):
        for j in choices(adj[i]):
            common=adj[i]&adj[j];s=M[i]|M[j]
            for k in choices(common):
                nxt=common&adj[k]
                if not nxt or not ok(s|M[k],7):continue
                cnt['extendible_pairwise_triples_passing_three_test']+=1
                for l in choices(nxt):
                    t=M[k]|M[l]
                    if not(ok(s|M[l],7) and ok(M[i]|t,7) and ok(M[j]|t,7)):continue
                    cnt['quads_passing_triple_tests']+=1
                    if ok(s|t,6):proof=[M[z] for z in (i,j,k,l)];break
                if proof:break
            if proof:break
        if proof:break
    if proof:
        A=H[:]+[0]*5
        for v,s in enumerate(proof,n):
            for u in range(n):
                if s>>u&1:A[u]|=1<<v
            A[v]=s|1<<(n+4);A[-1]|=1<<v
        assert not independent(A,(1<<39)-1,10) and all(not A[i]&A[j] for i,j in combinations(range(39),2) if A[i]>>j&1)
    return {'maximal':len(M),'single_hitting_neighborhood_exists':0 in miss,'pair_count':sum(a.bit_count() for a in adj),'stats':dict(cnt),'supports':proof}
if __name__=='__main__':
    G=graph((1,7,11,16));V=list(range(1,35));H=induce(G,V);E=[(a,b) for a,b in combinations(range(34),2) if not(H[a]>>b&1 or H[a]&H[b])];assert len(E)==4;rows=[]
    for k in range(4,-1,-1):
        for S in combinations(E,k):
            B=H[:]
            for a,b in S:B[a]|=1<<b;B[b]|=1<<a
            assert all(not B[a]&B[b] for a,b in S);r=four(B);r['added']=[(V[a],V[b]) for a,b in S];rows.append(r);print(r,flush=True);(D/'ramsey_ports_saturated_core.json').write_text(json.dumps(rows,indent=2)+'\n')
            if r['supports']:raise SystemExit
