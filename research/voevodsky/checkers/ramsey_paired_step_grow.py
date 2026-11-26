"""Try to grow a retained 17-in-24 chain. At each step solve exactly the one-new-vertex clauses; failure of a sampled branch is not a global bound."""
import json,random,sys
from pathlib import Path
from itertools import combinations
from pysat.solvers import Solver
from ramsey_retention_slice import decode,check
D=Path(__file__).resolve().parents[1]/'results';src=json.loads((D/'ramsey_retention_slice.json').read_text())[-1];rng=random.Random(4345)
def fours(a):
    red=[];blue=[]
    for q in combinations(range(len(a)),4):
        t=sum(a[i]>>j&1 for i,j in combinations(q,2))
        if t==6:red.append(q)
        if t==0:blue.append(q)
    return red,blue

def encode(a):
    bs=[a[i]>>j&1 for j in range(len(a)) for i in range(j)];bs += [0]*(-len(bs)%6);return chr(63+len(a))+''.join(chr(63+sum(b<<(5-i) for i,b in enumerate(bs[j:j+6]))) for j in range(0,len(bs),6))

def main():
    f=D/'ramsey_paired_step_growth.json';best=24;A=decode(src['graph6']);red,blue=fours(A);cache=[A];
    if f.exists():
        old=json.loads(f.read_text());best=old['order'];h=decode(old['graph6']);cache=[ [b&((1<<k)-1) for b in h[:k]] for k in range(24,best+1)]
    for trial in range(int(sys.argv[1])):
        a=rng.choice(cache[:max(1,len(cache)-2)]).copy();R,B=(red,blue) if len(a)==24 else fours(a);R=R.copy();B=B.copy()
        while len(a)<46:
            n=len(a);order=list(range(1,n+1));rng.shuffle(order)
            with Solver(name='g4',bootstrap_with=[[-order[i] for i in q] for q in R]+[[order[i] for i in q] for q in B]) as sl:
                sl.set_phases([x*rng.choice([-1,1]) for x in order]);
                # Disallow a disconnected or nearly monochromatic new star. The optional random pins only diversify samples.
                pins=rng.sample(order,4);pins=[x if i%2 else -x for i,x in enumerate(pins)]
                if not sl.solve(assumptions=pins) and not sl.solve():break
                pos=set(sl.get_model());m=sum(1<<i for i in range(n) if order[i] in pos)
            for q in combinations(range(n),3):
                bits=sum(m>>i&1 for i in q)
                if bits in (0,3) and all((a[i]>>j&1)==int(bits==3) for i,j in combinations(q,2)):(R if bits else B).append((*q,n))
            for i in range(n):a[i]|=(m>>i&1)<<n
            a.append(m)
            if len(a)>best:
                assert check(a,(1<<len(a))-1,5,5);best=len(a);cache=[[b&((1<<k)-1) for b in a[:k]] for k in range(24,best+1)];f.write_text(json.dumps(dict(order=best,graph6=encode(a),seed24=(1<<24)-1,seed17=src['seed17'],trial=trial),indent=1)+'\n');print('chain reaches',best,flush=True)
if __name__=='__main__':main()
