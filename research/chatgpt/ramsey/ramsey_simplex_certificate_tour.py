"""A finite no-reset offline certificate tour; no per-phase choice of representative."""
from ramsey_39_simplex_phase_depth import layer,phase,M
from ramsey_mutual_repair_conjecture import sevens

def tour(n):
    adj={x:[] for x in layer(n)}
    for x,row in adj.items():
        for i in range(4):
            if x[i]:
                y=list(x);y[i]-=1;y[(i+1)%4]+=1;row.append(tuple(y))
    length=sum(map(len,adj.values()));stack=[next(iter(adj))];rev=[]
    while stack:
        if adj[stack[-1]]:stack.append(adj[stack[-1]].pop())
        else:rev.append(stack.pop())
    path=rev[::-1];assert len(path)==length+1 and path[0]==path[-1]
    A=[0]*M
    for x,y in zip(path,path[1:]):
        assert any(all(y[j]-x[j]==int(j==(i+1)%4)-int(j==i) for j in range(4)) for i in range(4))
        p,q=phase(x),phase(y);A[p]|=1<<q;A[q]|=1<<p
    return A,length
if __name__=='__main__':
    for n in (6,7):
        A,l=tour(n);assert all(not A[i]&A[j] for i in range(M) for j in range(i) if A[i]>>j&1)
        bad=next(sevens(A,k=9),None);print(n,l,'edges',sum(a.bit_count() for a in A)//2,'independent nine',None if bad is None else [v for v in range(M) if bad>>v&1]);
        if n==7:
            assert bad is None;ct=0
            for I in sevens(A,k=8):
                for p in range(M):
                    if not I>>p&1:assert A[p]&I;ct+=1
            print('offline blocker queries covered',ct)
