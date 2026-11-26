"""Seed phases with a certified endpoint; never fix old join bits. Remaining outer vertices can change all edges."""
import sys,random,time,threading,json
from itertools import combinations
from pathlib import Path
from pysat.solvers import Solver
from ramsey_retention_slice import check
D=Path(__file__).resolve().parents[1]/'results';src,n,method,seed,secs=sys.argv[1:];n,seed,secs=map(int,(n,seed,secs));a=json.loads((D/src).read_text())['red_masks'];rng=random.Random(seed);pairs=list(combinations(range(n),2));rng.shuffle(pairs);var={e:v+1 for v,e in enumerate(e for e in pairs if e[1]>=31 or 17<=e[0]<24<=e[1])};start=time.monotonic()
with Solver(name=method) as s:
 for k in range(6):
  for u in combinations(range(31),k):
   fixed={a[i]>>j&1 for i,j in combinations(u,2) if (i,j) not in var}
   if len(fixed)>1:continue
   base=[var[e] for e in combinations(u,2) if e in var]
   for v in combinations(range(31,n),5-k):
    lits=base+[var[i,j] for i in u for j in v]+[var[e] for e in combinations(v,2)]
    if 0 not in fixed:s.add_clause([-w for w in lits])
    if 1 not in fixed:s.add_clause(lits)
 s.set_phases([v if (a[i]>>j&1 if j<len(a) else rng.randrange(2)) else -v for (i,j),v in var.items()]);timer=threading.Timer(secs,s.interrupt);timer.start()
 try:ok=s.solve_limited(expect_interrupt=True)
 finally:timer.cancel();timer.join()
 out=dict(order=n,status=ok,seconds=time.monotonic()-start)
 if ok:
  pos=set(s.get_model());b=[0]*n
  for i,j in pairs:
   if (var[i,j] in pos if (i,j) in var else a[i]>>j&1):b[i]|=1<<j;b[j]|=1<<i
  assert check(b,(1<<n)-1,5,5) and check(b,2**24-1,4,5) and check(b,2**17-1|(127<<24),5,4);out['red_masks']=b
 print(n,method,seed,ok);(D/f'ramsey_square_warm_{n}_{method}_{seed}_{secs}.json').write_text(json.dumps(out)+'\n')
