"""Cold, single-cut R(3,3) cache benchmark. python ramsey_signed_early_cuts.py"""
from itertools import combinations
from pathlib import Path
from statistics import median
from time import perf_counter_ns
import json, sqlite3, random

E=[(i,j) for j in range(1,5) for i in range(j)]
T=[sum(1<<E.index(e) for e in combinations(t,2)) for t in combinations(range(5),3)]
def legal(p,k):return all(p&t not in (0,t) for t in T if t<1<<k)
# Newly completed triangles after each decision
NEW=[[t for t in T if t.bit_length()==k] for k in range(11)]
def solve(p,k):
    if k==10:return [0]
    out=[]
    for b in (0,1):
        q=p|(b<<k)
        if all(q&t not in (0,t) for t in NEW[k+1]):out.extend((s<<1)|b for s in solve(q,k+1))
    return out

def run(k,ps,mode):
    db=None;cache={};answers={};hits=0;mask=(1<<k)-1;flip=(1<<(10-k))-1
    if mode=='sqlite':
        db=sqlite3.connect(':memory:');db.execute('CREATE TABLE f(k INTEGER PRIMARY KEY,v BLOB NOT NULL)')
    for p in ps:
        if mode=='direct':answers[p]=sorted(solve(p,k));continue
        key=min(p,p^mask)
        if db:
            row=db.execute('SELECT v FROM f WHERE k=?',(key,)).fetchone();v=None if row is None else json.loads(row[0])
        else:v=cache.get(key)
        if v is None:
            v=solve(key,k)
            if db:db.execute('INSERT INTO f VALUES (?,?)',(key,json.dumps(v).encode()))
            else:cache[key]=v
        else:hits+=1
        answers[p]=sorted((s^flip if p!=key else s) for s in v)
    if db:db.close()
    return answers,hits

def main():
    valid=[p for p in range(1024) if legal(p,10)];results=[];rng=random.Random(17)
    for k in range(1,7):
        ps=[p for p in range(1<<k) if legal(p,k)];oracle={p:sorted(x>>k for x in valid if x%(1<<k)==p) for p in ps};times={m:[] for m in ('direct','dict','sqlite')}
        for m in times:
            a,h=run(k,ps,m);assert a==oracle and h==(0 if m=='direct' else len(ps)//2)
        for _ in range(25):
            order=list(times);rng.shuffle(order)
            for m in order:
                start=perf_counter_ns()
                for _ in range(10):run(k,ps,m)
                times[m].append((perf_counter_ns()-start)/10000)
        results.append(dict(edges=k,prefixes=len(ps),hits=len(ps)//2,median_us={m:round(median(v),1) for m,v in times.items()}))
    out=dict(target='K5 avoiding both monochromatic triangles',edge_order=E,rounds=25,cold_runs_per_batch=10,results=results);print(json.dumps(results));(Path(__file__).resolve().parents[1]/'results/ramsey_signed_early_cuts.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
