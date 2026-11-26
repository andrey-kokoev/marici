"""Seed-preserving repair: delete exterior vertices and SAT-replace them jointly. A found graph is checked on all vertices; failed individual repairs do not bound P."""
from itertools import combinations
from pathlib import Path
import json,random,sys
from pysat.solvers import Solver
from ramsey_retention_slice import check
D=Path(__file__).resolve().parents[1]/'results'
def cliques(a,p,k,prefix=()):
    if not k:yield prefix;return
    while p.bit_count()>=k:
        b=p&-p;p^=b;i=b.bit_length()-1;yield from cliques(a,p&a[i],k-1,prefix+(i,))
def repair(a,discard,add,rng):
    ids=[i for i in range(len(a)) if i not in discard];n=len(ids);C=[sum(1<<j for j,v in enumerate(ids) if a[i]>>v&1) for i in ids];h=(1<<n)-1;m=n+add;E={(i,j):j*(j-1)//2+i+1 for j in range(n,m) for i in range(j)}
    with Solver(name='g4') as sl:
        for sign,A in [(-1,C),(1,[~x for x in C])]:
            for k in range(1,min(5,add)+1):
                outside=[(q,[sign*E[i,j] for i,j in combinations(q,2)]) for q in combinations(range(n,m),k)]
                for u in cliques(A,h,5-k):
                    for q,c in outside:sl.add_clause(c+[sign*E[i,j] for i in u for j in q])
        sl.set_phases([e*rng.choice([-1,1]) for e in E.values()]);sl.conf_budget(4000);b=sl.solve_limited()
        if b:
            model=set(sl.get_model());C.extend([0]*add)
            for (i,j),e in E.items():
                if e in model:C[i]|=1<<j;C[j]|=1<<i
            assert check(C,(1<<m)-1,5,5);return C

def main():
    seed=int(sys.argv[1]);rng=random.Random(seed);trials=int(sys.argv[2]);f=D/f'ramsey_paired_step_repair_{seed}.json';src=json.loads((D/'ramsey_paired_step_sat_34_g4_1.json').read_text())['red_masks'];best=cur=src
    for j in range(trials):
        if j%17==0:cur=best
        d=rng.choice([1,2,2,3]);plus=int(j%3!=1);r=repair(cur,rng.sample(range(17,len(cur)),d),d+plus,rng)
        if r:
            cur=r
            if len(r)>len(best):best=r;print(seed,'trial',j,'order',len(r),flush=True);f.write_text(json.dumps(dict(n=len(r),seed=17,red_masks=r,trial=j),indent=1)+'\n')
if __name__=='__main__':main()
