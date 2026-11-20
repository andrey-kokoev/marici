"""Exact endpoint-error search on the unique (3,5) host, circulant C13(1,5).
Every ordering is a positive Hamilton path. For a fixed path, an endpoint equality
is forbidden iff it joins a negative pair of arrows. Enumerate partitions as
restricted growth strings; accumulate positive joins, pruning by the incumbent.
"""
N=13
adj=lambda a,b:(a-b)%N in (1,5,8,12)
best=27;answer=None;paths=0

def audit(order):
    global best,answer,paths
    paths+=1
    # Introduce endpoints left to right. As soon as arrow j is complete, count
    # all missing positive links to earlier arrows. Never allow a negative join.
    w=[0]
    def rec(j,maximum,cost):
        global best,answer
        if cost>=best:return
        if j==N:
            best=cost;answer=(order[:],w[:]);return
        for y in range(maximum+2):
            p=0
            for i in range(j):
                if w[i+1]==w[j] or w[i]==y:p|=1<<i
            want=target[j]
            if p&~want:continue
            w.append(y);rec(j+1,max(maximum,y),cost+(want^p).bit_count());w.pop()
    target=[sum(1<<i for i in range(j) if adj(order[i],order[j])) for j in range(N)]
    rec(0,0,0)

def walk(order):
    if len(order)==N:audit(order);return
    for v in range(N):
        if v not in order and adj(order[-1],v):walk(order+[v])
if __name__=='__main__':
    # Translation and multiplication by a unit in {1,-1,5,-5} preserve the host
    # and move any ordered first edge to (0,1).
    walk([0,1]);order,w=answer
    joins=lambda i,j:w[i+1]==w[j] or w[j+1]==w[i]
    extra=[(i+1,j+1) for j in range(N) for i in range(j) if adj(order[i],order[j]) and not joins(i,j)]
    assert len(extra)==best and all(not joins(i,j) or adj(order[i],order[j]) for j in range(N) for i in range(j))
    print(paths,best,order,w,extra)
