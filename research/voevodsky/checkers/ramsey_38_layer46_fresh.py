"""Fit fresh (5,6) weights; append integer-verifiable certificates, resume by key. --limit caps new solves."""
import argparse,json,itertools
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from threadpoolctl import threadpool_limits
P=Path(__file__).resolve().parents[1]/'results';E=list((i,j) for j in range(20) for i in range(j))
def fit(h):
 a=[0]*20
 for k,(i,j) in enumerate(E):
  if int(h,16)>>k&1:a[i]|=1<<j;a[j]|=1<<i
 I=[0];F=(1<<20)-1
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q=[q for q in I if q.bit_count() in (5,6)];A=np.array((np.array(Q)[:,None]&np.array(S))!=0,dtype=int);d=np.array([q.bit_count() for q in Q]);lp=linprog(np.ones(len(S)),A_ub=-A,b_ub=-d);assert lp.success
 y=np.maximum(0,np.rint(-lp.ineqlin.marginals*10**7)).astype('int64');den=int(max(A.T@y));num=int(d@y);assert min(y)>=0
 return dict(core=h,num=num,den=den,weights={q:int(w) for q,w in zip(Q,y) if w},lp=lp.fun)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=7874);ap.add_argument('--shard',type=int,choices=range(6));args=ap.parse_args();cores=json.loads((P/'ramsey_38_layer46_inherited.json').read_text())['unresolved'];path=P/'ramsey_38_layer46_fresh.jsonl';done={json.loads(l)['core'] for l in path.read_text().splitlines()} if path.exists() else set()
 if args.shard is not None:
  cores=cores[args.shard::6];path=path.with_suffix(f'.{args.shard}.jsonl');done.update(json.loads(l)['core'] for l in path.read_text().splitlines()) if path.exists() else None
 with path.open('a') as f,threadpool_limits(limits=1):
  for h in itertools.islice((c for c in cores if c not in done),args.limit):
   r=fit(h);f.write(json.dumps(r)+'\n');f.flush()
   if r['num']<=7*r['den']:print('inspect',h,r['lp']);break
