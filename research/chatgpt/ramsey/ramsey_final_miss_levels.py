"""Separate top-row, triple and quadruple obstructions on matched 34-cores. Count ALL sorted maximal-support multisets (repetitions allowed)."""
from ramsey_slack_ladder_replay import attach,D,json
from itertools import combinations
from collections import Counter
from functools import lru_cache

def bits(b):
    while b:
        a=b&-b;b^=a;yield a.bit_length()-1

def levels(H,on_valid=None):
    I=[0];F=(1<<len(H))-1
    for i,r in enumerate(H):I += [s|1<<i for s in I if not s&r]
    M=[s for s in I if all(s>>i&1 or s&r for i,r in enumerate(H))];T=[s for s in I if s.bit_count()==8];assert max(map(int.bit_count,I))==8
    flags=[sum(1<<i for i,t in enumerate(T) if t>>v&1) for v in range(len(H))];miss=[]
    for s in M:
        hit=0
        for v in bits(s):hit|=flags[v]
        miss.append(((1<<len(T))-1)^hit)
    adj=[sum(1<<j for j in range(i,len(M)) if not x&miss[j]) for i,x in enumerate(miss)]
    @lru_cache(maxsize=50000)
    def witness(b,k):
        if not k:return 0
        while b.bit_count()>=k:
            a=b&-b;b^=a;w=witness(b&~H[a.bit_length()-1],k-1)
            if w is not None:return a|w
    cnt=Counter();examples={}
    for i,row in enumerate(adj):
        for j in bits(row):
            common=row&adj[j]
            for k in bits(common):
                tail=common&adj[k];cnt['pairwise_quads']+=tail.bit_count()
                if not tail:continue
                for l in bits(tail):
                    S=[M[q] for q in (i,j,k,l)];U=S[0]|S[1]|S[2]|S[3];obs=None
                    for a,b,c in combinations(S,3):
                        obs=witness(F^(a|b|c),7)
                        if obs is not None:break
                    if obs is not None:tag='fails_triple'
                    else:
                        obs=witness(F^U,6);tag='fails_four' if obs is not None else 'valid'
                    if tag=='valid' and on_valid is not None:on_valid(S)
                    cnt[tag]+=1;examples.setdefault(tag,{'supports':S,'missed_core_set':obs})
    return {'maximal_supports':len(M),'top_rows':len(T),'counts':dict(cnt),'examples':examples}
if __name__=='__main__':
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());B=p['stem_graphs'][-1];S=p['alternate']['to34'];T=p['to35'][:];T.pop(p['alternate']['omitted_port']);out={}
    for name,P in [('unthinned',T),('thinned',S)]:
        out[name]=levels(attach(B,P));print(name,out[name],flush=True)
    (D/'ramsey_final_miss_levels.json').write_text(json.dumps(out)+'\n')
