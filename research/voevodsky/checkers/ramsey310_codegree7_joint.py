"""uv run --with ortools python ... ; joint degree/attachment feasibility, not a Ramsey verdict."""
import json
from ortools.sat.python import cp_model as cp
from ramsey310_codegree7_test import P,F,sets,gzip

def residuals():
    for n,line in enumerate(gzip.open(P,'rb'),1):
        b=[v-63 for v in line.strip()];
        if sum(v.bit_count() for v in b[1:])!=85:continue
        A=[0]*27;k=0
        for j in range(27):
            for i in range(j):
                if b[1+k//6]>>(5-k%6)&1:A[i]|=1<<j;A[j]|=1<<i
                k+=1
        yield n,A

def run(A, five_hits=False, seconds=12):
    m=cp.CpModel(); H=list(sets(A,F,7)); c=[m.new_int_var(0,7,'') for h in H];m.add(sum(c)==7)
    E=[[m.new_bool_var('') for i in A] for j in range(4)]
    for row in E:
        m.add(sum(row)==6)
        for j,a in enumerate(A):
            for i in range(j):
                if a>>i&1:m.add(row[i]+row[j]<=1)
    for i,a in enumerate(A):
        for l in E[:2]:
            for r in E[2:]:m.add(l[i]+r[i]<=1)
        m.add(sum(c[j] for j,h in enumerate(H) if h>>i&1)+sum(row[i] for row in E)==9-a.bit_count())
    for h in H:
        for pair in [E[:2],E[2:]]:m.add(sum(row[i] for row in pair for i in range(27) if h>>i&1)>=1)
        if five_hits:m.add(sum(v for s,v in zip(H,c) if not s&h)<=2)
    solver=cp.CpSolver();solver.parameters.max_time_in_seconds=seconds;solver.parameters.num_search_workers=6
    status=solver.solve(m); result={'status':solver.status_name(status)}
    if status in (cp.FEASIBLE,cp.OPTIMAL):
        rows=[h for h,v in zip(H,c) for _ in range(solver.value(v))]+[sum(solver.value(x)<<i for i,x in enumerate(r)) for r in E]; result['rows']=rows
        assert all(sum(mask>>i&1 for mask in rows)==9-a.bit_count() for i,a in enumerate(A));assert not (rows[7]|rows[8])&(rows[9]|rows[10]);assert all(h&(rows[7]|rows[8]) and h&(rows[9]|rows[10]) for h in H)
        # Exact independence test via independent choices in the 13-vertex outside graph.
        outer=rows+[0,0]; adj=[0]*13
        for i,j in [(i,11) for i in range(9)]+[(i,12) for i in [*range(7),9,10]]+[(i,j) for i in (7,8) for j in (9,10)]:adj[i]|=1<<j;adj[j]|=1<<i
        for s in range(1<<13):
            ids=[i for i in range(13) if s>>i&1];
            if any(adj[i]&s for i in ids):continue
            avail=F
            for i in ids:avail &= ~outer[i]
            t=next(sets(A,avail,10-len(ids)),None)
            if t is not None:result['blue10']=[*ids,*[13+i for i in range(27) if t>>i&1]];break
    return result
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--five-hits',action='store_true');p.add_argument('--seconds',type=int,default=12);args=p.parse_args()
    for n,A in residuals():print(json.dumps({'record':n,**run(A,args.five_hits,args.seconds)}),flush=True)
