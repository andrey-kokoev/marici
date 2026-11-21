"""Classify pair-compatible no-reuse tuples, and cover survivors with explicit smaller rows."""
from ramsey_final_miss_levels import D,json,attach,bits
from itertools import combinations,combinations_with_replacement
from collections import Counter

def classify(H,k,old,include_rows=False):
    I=[0]
    for i,r in enumerate(H):I += [s|1<<i for s in I if not s&r]
    allowed=set(I)-set(old);M=sorted(s for s in allowed if not any(s!=t and s&t==s for t in [s|1<<v for v in range(len(H)) if not s>>v&1] if t in allowed));assert all(any(t&s==s for t in M) for s in allowed)
    T=[s for s in I if s.bit_count()==k-2];hit=[sum(1<<i for i,t in enumerate(T) if t>>j&1) for j in range(len(H))];miss=[]
    for s in M:
        h=0
        for j in bits(s):h|=hit[j]
        miss.append(((1<<len(T))-1)^h)
    adj=[sum(1<<j for j in range(i,len(M)) if not x&miss[j]) for i,x in enumerate(miss)];Q=[]
    for i,a in enumerate(adj):
        for j in bits(a):
            b=a&adj[j]
            for t in bits(b):Q.extend((M[i],M[j],M[t],M[u]) for u in bits(b&adj[t]))
    print('M, pairwise Q',len(M),len(Q),flush=True);rows={};U=(1<<len(Q))-1
    col=[[sum(1<<j for j,q in enumerate(Q) if q[h]>>v&1) for v in range(len(H))] for h in range(4)]
    for s in I:
        z=k-1-s.bit_count()
        if z not in (2,3):continue
        x=[]
        for c in col:
            m=U
            for v in bits(s):m&=~c[v]
            x.append(m)
        a,b,c,d=x;mask=(a&b&c&d) if z==3 else ((a&b&(c|d))|(c&d&(a|b)))
        if mask:rows[s]=mask
    greedy=[]
    while U:
        s=max(rows,key=lambda s:(U&rows[s]).bit_count());assert U&rows[s];U&=~rows[s];greedy.append(s)
    tri=0
    for s,r in rows.items():
        if s.bit_count()==k-3:tri|=r
    full=(1<<len(Q))-1;distinct=set(rows.values());shorter=any(a==full for a in distinct) or (len(greedy)>2 and any(a|b==full for a,b in combinations(distinct,2)))
    return dict(at_most_two_rows_suffice=shorter,after_triples=len(Q)-tri.bit_count(),M=M,number_quads=len(Q),greedy=greedy,number_rows=len(rows),candidate_quads=Q if include_rows or len(Q)<200 else None,row_masks={s:r for s,r in rows.items()} if include_rows or len(Q)<200 else None)
if __name__=='__main__':
    R=json.loads((D/'ramsey_reuse_stress.json').read_text());n=13;steps=(1,12,5,8);H=[sum(1<<(j-1) for j in range(1,n) if (j-i)%n in steps) for i in range(1,n)];u,v=R['13'][0]['edge'];H[u-1]^=1<<(v-1);H[v-1]^=1<<(u-1);r=classify(H,6,R['13'][0]['old']);print(r);(D/'ramsey_integral_obstruction.json').write_text(json.dumps(r)+'\n')
