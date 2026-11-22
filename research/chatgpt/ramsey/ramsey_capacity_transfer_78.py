"""Transfer frozen two-rule four-port screen to k=8. Count full multisets and classify missed smaller rows after the screen, independently of stored successful schedules."""
from itertools import combinations
from collections import Counter
from ramsey_hall_center_conjecture import decode
from ramsey_fork_audit_uniform import inds,verify,grow,D,json
from ramsey_final_miss_levels import bits

def check(H,on_assignment=None):
    I=inds(H);assert max(map(int.bit_count,I))==6;M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(H))];miss={}
    for k in (4,5,6):
        T=[s for s in I if s.bit_count()==k];hit=[sum(1<<j for j,t in enumerate(T) if t>>i&1) for i in range(22)];ms=[]
        for s in M:
            a=0
            for i in bits(s):a|=hit[i]
            ms.append(((1<<len(T))-1)^a)
        miss[k]=(T,ms)
    hot=lambda k:sum(1<<v for v,r in enumerate(H) if r.bit_count()>=k);d6,d5,d4=map(hot,(6,5,4));p=miss[6][1];adj=[sum(1<<j for j in range(i,len(M)) if not (m&p[j] or M[i]&M[j]&d6)) for i,m in enumerate(p)];cnt=Counter();examples={}
    for i,row in enumerate(adj):
        for j in bits(row):
            common=row&adj[j];ab=M[i]&M[j];ij=M[i]|M[j]
            for k in bits(common):
                triple=ab&M[k];twice=ab|(ij&M[k]);
                if triple&d5:continue
                ban=(twice&d5)|(triple&d4)
                for l in bits(common&adj[k]):
                    if M[l]&ban:continue
                    q=[i,j,k,l];obs=0;tag='valid'
                    for level,num in ((5,3),(4,4)):
                        T,ms=miss[level];
                        for sub in combinations(q,num):
                            a=ms[sub[0]]
                            for h in sub[1:]:a&=ms[h]
                            if a:obs=T[(a&-a).bit_length()-1];break
                        if obs:tag=f'miss{level}';break
                    cnt[tag]+=1
                    if on_assignment is not None:on_assignment([M[h] for h in q],tag)
                    if tag not in examples:
                        S=[M[h] for h in q];examples[tag]=dict(supports=S,missed=obs)
                        if not obs:verify(grow(H,S),8)
    return dict(counts=cnt,examples=examples)

def run():
    from ramsey_row_quotient_constructor import final,P,T
    m,=final;omit={tuple(sorted(P.index(d) for d in T[j-15] if d!=P[i])) for i,j in m};G=[0]*22
    for x,y in [(0,1+i) for i in range(6)]+[(1+v,7+i) for i,d in enumerate(P) for v in d]+[(7+i,7+j) for i,j in combinations(range(15),2) if set(P[i]).isdisjoint(P[j]) and (i,j) not in omit]:G[x]|=1<<y;G[y]|=1<<x
    s=json.loads((D/'ramsey_pure_short_fork.json').read_text());A=[2,1]
    for U in s[:5]:A=grow(A,U)
    named={k:check(h) for k,h in [('short',A),('hall',G)]};rows=[check(decode(line)) for line in (D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()];print({k:v['counts'] for k,v in named.items()},Counter((bool(r['counts']),bool(r['counts'].get('valid'))) for r in rows),sum((Counter(r['counts']) for r in rows),Counter()));return dict(named=named,catalogue=rows)
if __name__=='__main__':(D/'ramsey_capacity_transfer_78.json').write_text(json.dumps(run())+'\n')
