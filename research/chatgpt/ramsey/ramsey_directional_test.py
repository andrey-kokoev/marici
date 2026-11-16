from itertools import combinations, product
from math import comb
from collections import Counter

def cyclic_graph(n):
    assert n%2==0
    m=n//2
    E={tuple(sorted((i,(i+1)%n))) for i in range(n)}
    E |= {tuple(sorted((i,(i+m)%n))) for i in range(m)}
    return E

def cycles_of_length(n,E,length):
    adj={i:set() for i in range(n)}
    for i,j in E:
        adj[i].add(j);adj[j].add(i)
    cycles=set()
    for v0 in range(n):
        def dfs(p):
            if len(p)==length:
                if p[-1] in adj[v0]:
                    tup=tuple(p)
                    arr=[tup[i:]+tup[:i] for i in range(length)]
                    rev=tup[::-1]
                    arr += [rev[i:]+rev[:i] for i in range(length)]
                    cycles.add(min(arr))
                return
            for w in adj[p[-1]]:
                if w not in p:dfs(p+[w])
        dfs([v0])
    return cycles

def independence_number(n, E):
    adj=[0]*n
    for i,j in E:
        adj[i] |= 1<<j;adj[j] |= 1<<i
    best=0
    # max independent set via DFS with pruning; small n only
    def go(mask, count):
        nonlocal best
        if count+mask.bit_count()<=best:return
        if not mask:
            best=max(best,count);return
        v=(mask&-mask).bit_length()-1
        go(mask & ~(1<<v) & ~adj[v], count+1)
        go(mask & ~(1<<v),count)
    go((1<<n)-1,0)
    return best

def word_graph(k):
    # exactly two r letters, k-2 s letters
    words=[''.join('r' if i in ix else 's' for i in range(k)) for ix in combinations(range(k),2)]
    ws=set(words)
    edges=set()
    for w in words:
        for j in range(k-1):
            if w[j]!=w[j+1]:
                v=w[:j]+w[j+1]+w[j]+w[j+2:]
                assert v in ws
                edges.add(tuple(sorted((w,v))))
    fixes=sum(w==w[::-1] for w in words)
    # all words evaluate to same element of C8
    evaluations={sum(1 if x=='r' else 4 for x in w)%8 for w in words}
    adj={w:[] for w in words}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    seen=set(); c=0
    for w in words:
        if w not in seen:
            c+=1; stack=[w];seen.add(w)
            while stack:
                for v in adj[stack.pop()]:
                    if v not in seen:seen.add(v);stack.append(v)
    return dict(k=k,V=len(words),E=len(edges),components=c,cycle_rank=len(edges)-len(words)+c,reverse_fixed=fixes,reverse_orbits=(len(words)+fixes)//2,endpoint_residue=list(evaluations))

if __name__=='__main__':
    print('CAYLEY')
    for n in (6,8,10,12,14,16,18,20,22):
        e=cyclic_graph(n)
        a=independence_number(n,e)
        p5=cycles_of_length(n,e,5)
        vcounts=Counter(v for p in p5 for v in p)
        print(dict(n=n,edges=len(e),alpha=a,triangles=len(cycles_of_length(n,e,3)),pentagons=len(p5),pentagons_per_vertex=sorted(vcounts.values()),coherence_polygon_halfnplus1=n//2+1))
    print('WORDS')
    for k in range(3,11): print(word_graph(k))


def relation_matrix(m):
    # e_i:i->i+1, c_i:i->i+m for i<m.
    import sympy as sp
    n=2*m
    # rows e0..e(2m-1), c0..c(m-1)
    mat=sp.zeros(3*m,2*m)
    for i in range(n):
        for t in range(m):mat[(i+t)%n,i]+=1
        mat[2*m+(i%m),i]+= -1 if i<m else +1
    return mat

if __name__=='__main__':
    print('COHERENCE SYZYGIES')
    import sympy as sp
    for m in range(3,9):
        M=relation_matrix(m)
        rank=M.rank()
        vs=[]
        for j in range(1,m):
            z=sp.zeros(2*m,1)
            for index,coef in ((j,1),(j+m,1),(0,-1),(m,-1)):z[index]=coef
            assert M*z==sp.zeros(3*m,1)
            vs.append(z)
        Z=sp.Matrix.hstack(*vs)
        assert Z.rank()==m-1 and rank==m+1
        print(dict(n=2*m,relation_polygons=2*m,polygon_sides=m+1,rank_boundary=rank,NN_independent=m-1,all_generated_nn_closed=True))
