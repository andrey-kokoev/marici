"""Count oriented prefix completions by subset DP with separate deterministic zipper-frontier filters. No middle-cycle lists, known successful moves, edge hints, or joint-fit test. Edge deletion counts give all Boolean bins on <=2 edges by subtraction. Pools and the list of hard prefix queries are supplied by the prior audit."""
from functools import lru_cache
from itertools import permutations,combinations,product
from ramsey_38_joint_annuli import D,load,red,bits
import json

def solver(H,Z,start,curves):
    # Each cursor starts at a cut on a fixed comparison cycle; mask bit t = t advances from that cut. Union of accepting cursors is one acceptance, not multiple triangulations.
    lanes=[]
    for L in curves:
        b=bits(L)
        if b is None:continue
        n=len(L)
        for c,k in product((0,1),range(n)):
            masks={v:sum(1<<i for i in range(n+1) if red(v,L[(k+i)%n])==(b[(k+i)%n]^c)) for v in H}
            if masks[start]&1:lanes.append((n,masks))
    plain=not curves;initial=tuple(1 for _ in lanes);key=lambda u,v:tuple(sorted((u,v)))
    @lru_cache(None)
    def advance(x,y,state):
        ans=[]
        for (n,mask),t in zip(lanes,state):
            f=t
            for _ in range(n-1):
                new=f|((f<<1)&mask[x]);
                if new==f:break
                f=new
            ans.append(f&mask[y])
        return tuple(ans)
    def count(pre,ban):
        st=initial
        for x,y in zip(pre,pre[1:]):
            if key(x,y) in ban:return 0
            st=advance(x,y,st)
        @lru_cache(None)
        def recur(x,free,st):
            if not plain and not any(st):return 0
            if not free:
                if red(x,start) or (x in Z)==(start in Z) or key(x,start) in ban:return 0
                return int(plain or any(t>>n for t,(n,_) in zip(advance(x,start,st),lanes)))
            return sum(recur(y,free^(1<<y),advance(x,y,st)) for y in H if free>>y&1 and (y in Z)!=(x in Z) and not red(x,y) and key(x,y) not in ban)
        result=recur(pre[-1],sum(1<<y for y in H-set(pre)),st);recur.cache_clear();return result
    return count
out=[]
for old,rec in zip(load('ramsey_38_edge_conditioned_counts'),load('ramsey_38_joint_frontier')):
    H=set(rec['middle']);Z=set(rec['middle'][::2]);U=sorted(rec['last']);I=rec['ring'];start=rec['middle'][0];edges=sorted({tuple(sorted((z,w))) for z in Z for w in H-Z if not red(z,w)});curves=[list((U[0],)+p) for p in permutations(U[1:])];counts=[solver(H,Z,start,L) for L in ([],[I,I[::-1]],curves)];certs=[]
    for query in old['hard']:
        pre=query['prefix'];candidates=sorted(y for y in H-set(pre) if (y in Z)!=(pre[-1] in Z) and not red(y,pre[-1]));
        @lru_cache(None)
        def totals(v,ban):return tuple(f(pre+[v],set(ban)) for f in counts)
        def bin_counts(v,es,vals):
            no=[e for e,bit in zip(es,vals) if not bit];yes=[e for e,bit in zip(es,vals) if bit];acc=[0,0,0]
            for k in range(len(yes)+1):
                for s in combinations(yes,k):
                    for j,num in enumerate(totals(v,tuple(sorted(no+list(s))))):acc[j]+=(-1)**k*num
            return acc
        def find():
            for k in (0,1,2):
                for v in candidates:
                    T=totals(v,())[0];active=[e for e in edges if 0<totals(v,(e,))[0]<T] if k else []
                    for es in combinations(active,k):
                        for vals in product((False,True),repeat=k):
                            t,i,o=bin_counts(v,es,vals)
                            if i+o>t:return dict(next=v,edges=es,present=vals,T=t,I=i,O=o)
        cert=find();assert cert;ref=query['certificate'];ee=[tuple(e) for e,_ in ref['bits']];assert bin_counts(ref['next'],ee,[val for _,val in ref['bits']])==[ref[z] for z in ('T','I','O')];assert len(cert['edges'])==len(ee);certs.append(dict(prefix=pre,**cert));totals.cache_clear()
    out.append(certs)
print('DP certificates',sum(map(len,out)),'example',next(c[0] for c in out if c));(D/'ramsey_38_conditional_transfer_dp.json').write_text(json.dumps(out,indent=2)+'\n')
