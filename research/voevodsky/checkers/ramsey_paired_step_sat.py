"""Fixed Paley17 plus n-17 free vertices; exact forbidden-five SAT with optional safe symmetry breaking. Timeouts are unknown."""
from itertools import combinations
import argparse,json,threading,time
from pathlib import Path
from pysat.solvers import Solver
from ramsey_retention_slice import check
D=Path(__file__).resolve().parents[1]/'results'

def run(n,seconds,solver,order=True):
    seed=17;res={i*i%17 for i in range(1,17)};edge={};counter=0
    for j in range(seed,n):
        for i in range(j):counter+=1;edge[i,j]=counter
    def check5(q,red):
        return [(-1 if red else 1)*e for e in q]
    t=time.monotonic();ct=0
    with Solver(name=solver) as sl:
        # Enumerate monochromatic seed subsets only. Red (blue) K5 prohibited by a clause over the free edges.
        for m in range(0,4):
            for u in combinations(range(seed),m):
                colors={(j-i)%17 in res for i,j in combinations(u,2)};red=False not in colors;blue=True not in colors
                if not (red or blue):continue
                for v in combinations(range(seed,n),5-m):
                    q=[edge[i,j] for i in u for j in v]+[edge[i,j] for i,j in combinations(v,2)]
                    if red:sl.add_clause(check5(q,True));ct+=1
                    if blue:sl.add_clause(check5(q,False));ct+=1
        if order:
            # Sort outside vertices lexicographically by their seed columns; ties are allowed.
            for j in range(seed,n-1):
                prev=None
                for i in range(seed):
                    x,y=edge[i,j],edge[i,j+1];p=[] if prev is None else [-prev];sl.add_clause(p+[-x,y]);counter+=1;eq=counter
                    sl.add_clause(p+[x,y,eq]);sl.add_clause(p+[-x,-y,eq]);prev=eq
        timer=threading.Timer(seconds,sl.interrupt);start=time.monotonic();timer.start()
        try:status=sl.solve_limited(expect_interrupt=True)
        finally:timer.cancel();timer.join()
        r=dict(n=n,seed=17,solver=solver,ordered=order,forbidden_clauses=ct,build_seconds=round(start-t,2),solve_seconds=round(time.monotonic()-start,2),status=status,stats=sl.accum_stats());
        if status:
            pos=set(sl.get_model());a=[0]*n
            for i,j in combinations(range(n),2):
                if ((j-i)%17 in res if j<seed else edge[i,j] in pos):a[i]|=1<<j;a[j]|=1<<i
            assert check(a,(1<<n)-1,5,5);r['red_masks']=a
        return r
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('n',type=int);p.add_argument('seconds',type=int);p.add_argument('solver');p.add_argument('--unsorted',action='store_true');args=p.parse_args();r=run(args.n,args.seconds,args.solver,not args.unsorted);print({k:v for k,v in r.items() if k!='red_masks'});(D/f"ramsey_paired_step_sat_{args.n}_{args.solver}_{int(r['ordered'])}.json").write_text(json.dumps(r,indent=1)+'\n')
