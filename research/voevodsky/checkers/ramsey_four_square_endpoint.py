"""Order-42 endpoint test for the saved seed identification. Leave all 49 join bits free, not just the exterior bits."""
from pathlib import Path
import json,threading,time,argparse
parser=argparse.ArgumentParser();parser.add_argument('--order',type=int,default=42,choices=range(31,46));parser.add_argument('--seconds',type=int,default=30);parser.add_argument('--solver',default='g4');args=parser.parse_args()
from itertools import combinations
from pysat.solvers import Solver
from ramsey_retention_slice import check
D=Path(__file__).resolve().parents[1]/'results';a=json.loads((D/'ramsey_four_witness_square.json').read_text())['red_masks'];n=args.order
var={(i,j):t for t,(i,j) in enumerate(((i,j) for i,j in combinations(range(n),2) if j>=31 or 17<=i<24<=j),1)}
with Solver(name=args.solver) as sl:
 ct=0
 for r in range(6):
    for u in combinations(range(31),r):
        fixed={a[i]>>j&1 for i,j in combinations(u,2) if (i,j) not in var};
        if len(fixed)>1:continue
        base=[var[e] for e in combinations(u,2) if e in var]
        for v in combinations(range(31,n),5-r):
            lits=base+[var[i,j] for i in u for j in v]+[var[e] for e in combinations(v,2)]
            if 0 not in fixed:sl.add_clause([-x for x in lits]);ct+=1
            if 1 not in fixed:sl.add_clause(lits);ct+=1
 timer=threading.Timer(args.seconds,sl.interrupt);timer.start();start=time.monotonic()
 try:ok=sl.solve_limited(expect_interrupt=True)
 finally:timer.cancel();timer.join()
 out=dict(order=n,status=ok,clauses=ct,unknown_edges=len(var),solve_seconds=time.monotonic()-start,stats=sl.accum_stats());
 if ok:
    m=set(sl.get_model());b=a+[0]*(n-31)
    for (i,j),e in var.items():
        b[i]&=~(1<<j);b[j]&=~(1<<i)
        if e in m:b[i]|=1<<j;b[j]|=1<<i
    assert check(b,(1<<n)-1,5,5) and check(b,(1<<24)-1,4,5) and check(b,((1<<17)-1)|(127<<24),5,4);out['red_masks']=b
 print(out);(D/f'ramsey_four_square_endpoint_{n}_{args.solver}_{args.seconds}s.json').write_text(json.dumps(out,indent=1)+'\n')
