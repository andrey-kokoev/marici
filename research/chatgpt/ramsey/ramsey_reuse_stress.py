"""Test the old-neighborhood cover on smaller vertex-transitive parents; then test the role of maximality at 34."""
from ramsey_final_miss_levels import levels,bits,attach,D,json
from ramsey_port_deletion_chain import search,induce,independent,combinations
from itertools import product
from collections import Counter
from functools import lru_cache

def smaller(n,k,steps,d):
    A=[sum(1<<((i+j)%n) for j in steps) for i in range(n)];V=list(range(1,n));H=induce(A,V);F=(1<<len(H))-1;out=[]
    for i,j in combinations(range(n-1),2):
        if not H[i]>>j&1:continue
        B=H[:];B[i]^=1<<j;B[j]^=1<<i
        if independent(B,F,k-1):continue
        old=[A[0]>>1,H[i],H[j]];stats=Counter();ex={}
        def visit(S,G):
            count=sum(s in old for s in S);stats[count]+=1
            if count==0 and not ex:ex.update(supports=S,graph=G)
        search(B,k,d,visit)
        I=[0]
        for v,r in enumerate(B):I += [s|1<<v for s in I if not s&r]
        rows=[(s,k-1-s.bit_count()) for s in I];avoid=[s for s in I if s not in old]
        def dfs(S,room,lo,goal):
            if len(S)==goal:return S
            for j in range(lo,len(avoid)):
                x=avoid[j];nxt=[z-int(not x&t) for z,(t,_) in zip(room,rows)]
                if min(nxt)<0:continue
                ans=dfs(S+[x],nxt,j,goal)
                if ans is not None:return ans
        witnesses={g:dfs([], [z for _,z in rows],0,g) for g in (d,d-1)}
        out.append(dict(edge=[V[i],V[j]],old=old,counts=dict(stats),avoider=ex,any_avoider=witnesses))
    return out

def large():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());a=p['alternate'];H=attach(p['stem_graphs'][-1],a['to34']);v=26+a['thinned_port_index_among_retained'];u=a['removed_incidence'];old=[p['to35'][a['omitted_port']]|1<<33,H[v]|1<<u,H[u]|1<<v];Q=[];levels(H,Q.append);F=(1<<34)-1
    @lru_cache(None)
    def safe(U,k):return not independent(H,F^U,k)
    def valid(S):
        for d in (2,3,4):
            for group in combinations(S,d):
                mask=0
                for s in group:mask|=s
                if not safe(mask,10-d):return False
        return True
    stats=Counter();ex={}
    for q in Q:
        found=False
        for t in product(*[[s^(1<<i) for i in bits(s)] if s in old else [s] for s in q]):
            if valid(t):
                found=True
                if not ex:ex.update(maximal=q,shrunk=t)
                break
        stats['avoidable' if found else 'forced']+=1
    return dict(old=old,counts=dict(stats),example=ex)
if __name__=='__main__':
    out={}
    for n,k,steps,d in [(5,4,[1,-1],3),(13,6,[1,-1,5,-5],4)]:
        r=smaller(n,k,steps,d);out[str(n)]=r;print(n,[(x['edge'],x['counts']) for x in r],flush=True)
    out['35']=large();print(out['35']);(D/'ramsey_reuse_stress.json').write_text(json.dumps(out)+'\n')
