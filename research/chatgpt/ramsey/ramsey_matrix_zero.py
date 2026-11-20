"""Direct finite matrix proof for the joined-center two-square model. No SAT library.
Bit masks represent sets; a column-edge variable denotes an entire reflection orbit.
"""
from itertools import combinations,product
from collections import Counter

def bits(m):
    while m:
        b=m&-m;yield b;m^=b

def matrices(parity=0):
    marks=[[i for i in range(3) if m>>i&1]+([3] if m&4 else []) for m in (1,2,4,5,6,7,7)]
    tree=[];extra=[];parent=list(range(11))
    def root(a):
        while parent[a]!=a:a=parent[a]
        return a
    for j,rs in enumerate(marks):
        for i in rs:
            if root(i)!=root(j+4):parent[root(i)]=root(j+4);tree.append((i,j))
            else:extra.append((i,j))
    for val in product(range(2),repeat=len(extra)):
        s=dict.fromkeys(tree,0);s.update(zip(extra,val))
        if parity is not None and (s[2,3]^s[3,3]^s[2,4]^s[3,4])!=parity:continue
        B=[0]*8
        for (i,j),h in s.items():
            for t in (0,1):B[2*i+t]|=1<<(2*j+(h^t))
        yield B

def orbit_table(neighbors,row_side=False):
    n=len(neighbors);tab={}; ids={}
    for i,j in combinations(range(n),2):
        if neighbors[i]&neighbors[j]:continue  # off-diagonal Gram entry positive
        if row_side and j>=6 and i<6:continue # Z has no edges to A,B,C
        k=(i//2,j//2,(i^j)&1);tab[i,j]=1<<ids.setdefault(k,len(ids))
    def edges(t):return sum(set(tab.get(p,0) for p in combinations(t,2)))
    tris={edges(t) for t in combinations(range(n),3) if all(p in tab for p in combinations(t,2))}
    return tab,edges,sorted(tris,key=int.bit_count)

def maximal_rows(tab,tris):
    full=sum(set(tab.values()));seen=set();leaves=set()
    def cut(m):
        if m in seen:return
        seen.add(m)
        for t in tris:
            if m&t==t:
                for b in bits(t):cut(m^b)
                return
        if m&tab[6,7]:leaves.add(m)
    cut(full);return [m for m in leaves if not any(m!=v and m&v==m for v in leaves)]

def impossible(hits,tris,stats):
    # Require at least one edge per hit mask, and not all edges of any triangle.
    def visit(on,off):
        stats['nodes']+=1
        while True:
            old=on,off
            for t in tris:
                needed=t&~on
                if not needed:return True
                if needed.bit_count()==1:off|=needed
            pivot=None
            for h in hits:
                if h&on:continue
                candidates=h&~off
                if not candidates:return True
                if candidates.bit_count()==1:on|=candidates
                elif pivot is None or candidates.bit_count()<pivot.bit_count():pivot=candidates
            if on&off:return True
            if old==(on,off):break
        if pivot is None:return False
        for b in bits(pivot):
            if not visit(on|b,off):return False
            off|=b
        return True
    return visit(0,0)

def main():
    stats=Counter(); hardest=0
    for B in matrices():
        stats['incidences']+=1
        Bt=[sum(1<<i for i,m in enumerate(B) if m>>j&1) for j in range(14)]
        rt,re,tr=orbit_table(B,True);ct,ce,tc=orbit_table(Bt)
        for row in maximal_rows(rt,tr):
            stats['row cases']+=1; hits=set()
            for k,l in ((4,3),(2,5)):
                for I in combinations(range(8),k):
                    if re(I)&row:continue
                    touched=0
                    for i in I:touched|=B[i]
                    for J in combinations([j for j in range(14) if not touched>>j&1],l):hits.add(ce(J))
            minimal=[]
            for h in sorted(hits,key=lambda h:(h.bit_count(),h)):
                if not any(a&h==a for a in minimal):minimal.append(h)
            forced=sum(h for h in minimal if h.bit_count()==1)
            if 0 in minimal:stats['empty hit']+=1
            elif any(t&forced==t for t in tc):stats['forced triangle in first round']+=1
            else:stats['further propagation']+=1
            before=stats['nodes'];assert impossible(minimal,tc,stats);nodes=stats['nodes']-before
            if nodes==1:stats['no branching']+=1
            hardest=max(hardest,nodes)
    print(dict(stats),'max nodes in a case',hardest)

if __name__=='__main__':main()
