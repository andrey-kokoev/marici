"""Incremental boundary fan connectivity on a branch. Each fan partitions five labels.
After a merge, precisely the segments between the merged blocks become forbidden.
"""
from ramsey38_shared_twist10 import combinations,faces

def search(labs,bd,req):
    ts=list(map(frozenset,combinations(sorted(labs),4)));bits={t:1<<i for i,t in enumerate(ts)};allbits=(1<<len(ts))-1;carrier=lambda f:sum(b for t,b in bits.items() if f<=t);tri=[(1 if f in bd else 2,carrier(f)) for f in map(frozenset,combinations(labs,3))];needs=[carrier(f) for f in req];rim={frozenset(e) for f in bd for e in combinations(f,2)};moves={b:[] for b in bits.values()};initial=[]
    for j,e in enumerate(sorted(rim,key=sorted)):
        vs=sorted(set(labs)-e);n=len(vs);initial.append(tuple(1<<k for k in range(n)));pairs={(a,b):bits[e|{vs[a],vs[b]}] for a,b in combinations(range(n),2)};memo={}
        for (a,b),bit in pairs.items():moves[bit].append((j,a,b,pairs,memo))
    def add(bit,state,ban):
        for j,a,b,pairs,memo in moves[bit]:
            old=state[j];A=old[a];B=old[b];assert A!=B
            key=(A,B) if A<B else (B,A)
            extra=memo.get(key)
            if extra is None:
                extra=sum(w for (u,v),w in pairs.items() if (A>>u&1 and B>>v&1) or (B>>u&1 and A>>v&1));memo[key]=extra
            ban|=extra^bit;state[j]=tuple(A|B if x==A or x==B else x for x in old)
        return ban
    leaves=[];nodes=0
    def visit(m,n,state,ban,install):
        nonlocal nodes
        nodes+=1
        while True:
            while install:
                bit=install&-install;install^=bit
                if bit&ban:return
                ban=add(bit,state,ban);m|=bit
            forced=blocked=0
            for k,c in tri:
                count=(m&c).bit_count();free=c&~(m|n);possible=count+free.bit_count()
                if count>k or (count or k==1) and possible<k:return
                if count==k or possible<k:blocked|=free
                elif possible==k and (count or k==1):forced|=free
            for c in needs:
                if c&m:continue
                free=c&~n
                if not free:return
                if free.bit_count()==1:forced|=free
            if not (forced|blocked):blocked=ban&~(m|n)
            if not (forced|blocked):break
            if forced&blocked:return
            install=forced;n|=blocked
        free=allbits&~(m|n)
        if not free:leaves.append(faces(t for t,b in bits.items() if m&b));return
        bit=free&-free;visit(m,n,state.copy(),ban,bit);visit(m,n|bit,state,ban,0)
    visit(0,0,initial,0,sum(bits[r] for r in req if len(r)==4));return dict(nodes=nodes,leaves=leaves)
