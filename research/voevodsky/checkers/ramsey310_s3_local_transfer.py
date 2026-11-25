"""Hold E and the S3 score fixed. Change one red edge of H at constant edge count.
Check every local edit (including delete-first edits); no use of scores in generation.
"""
from collections import Counter
from itertools import permutations,product
import json
from ramsey310_matching_sides import bits,F,sets,Path
from ramsey310_six_set_parent_test import independent
D=Path(__file__).resolve().parents[1]/'results'
E=(13117600,33825944,34097697,34652242,4264289,29492304)

def examine(A):
    if any(independent(A,F&~(a|b),7) for side in [E[:3],E[3:]] for i,a in enumerate(side) for b in side[:i]):return 'root',None
    if any(independent(A,F&~(a|b|c),6) for a,b,c in [E[:3],E[3:]]):return 'root',None
    need=[9-a.bit_count()-sum(s>>i&1 for s in E) for i,a in enumerate(A)]
    if min(need)<1 or max(need)>6 or any(need[i]+need[j]>6 for i in range(26) for j in bits(A[i])):return 'capacity',None
    singles=sum(1<<i for i,x in enumerate(need) if x==1);C=list(sets(A,F,7))
    for a,b,c in product(*zip(E[:3],E[3:])):
        g=singles&~(a|b|c)
        if g.bit_count()>6:return 'gap',None
        C=[s for s in C if (s&g).bit_count()<=1]
    for k in (6,7):
        for t in sets(A,F,k):
            limit=6-k+sum(bool(t&a and t&b) for a,b in zip(E[:3],E[3:]))
            if limit<0:return 'outside',None
            if not limit:C=[s for s in C if s&t]
    if len(C)<6 or any(sum(s>>i&1 for s in C)<x for i,x in enumerate(need)):return 'individual',None
    def coord(w):return [sum(w[v]*(((l|r)>>v&1) if a.bit_count()==5 else (l>>v&1)*((a.bit_count()==4)-(a.bit_count()==7))) for v,a in enumerate(A)) for l,r in zip(E[:3],E[3:])]
    d=coord(need);cs=[coord([s>>i&1 for i in range(26)]) for s in C]
    for i,j in permutations(range(3),2):
        top=sorted((v[i]-v[j] for v in cs),reverse=True)[:6]
        if d[i]-d[j]>sum(top):return 'contrast',dict(rows=len(C),demand=d,pair=[i,j],top=top)
    return 'pass',None

def neighbors(A):
    for i in range(26):
        for j in bits(A[i]&((1<<i)-1)):
            B=A.copy();B[i]^=1<<j;B[j]^=1<<i
            for x in range(26):
                for y in range(x):
                    m=1<<x|1<<y
                    if (x,y)==(i,j) or B[x]>>y&1 or B[x]&B[y] or any(s&m==m for s in E):continue
                    Z=B.copy();Z[x]|=1<<y;Z[y]|=1<<x
                    if independent(Z,F,8):continue
                    yield tuple(Z),(i,j,x,y)

if __name__=='__main__':
    from ramsey310_matching_scope import key
    import sys
    known=json.loads((D/'ramsey310_matching_degree3_types.json').read_text());old={key(a) for a in known};queue={tuple(known[0]):[]};seen=set(queue);types=set();hist=Counter();found=[];sizes=[];passing=[]
    for depth in range(int(sys.argv[1]) if len(sys.argv)>1 else 1):
        nxt={}
        for A,path in queue.items():
            for Z,edit in neighbors(list(A)):
                if Z in seen:continue
                seen.add(Z);q=path+[edit];nxt[Z]=q;k=key(Z)
                if k in old:continue
                types.add(k);tag,cert=examine(Z);hist[tag]+=1
                if cert:found.append(dict(path=q,key=k.hex(),**cert))
                if tag=='pass':passing.append(dict(path=q,key=k.hex()))
        sizes.append(len(nxt));queue=nxt
    print(json.dumps(dict(shell_sizes=sizes,new_types=len(types),counts=hist,certificates=found,uncut=passing)))
