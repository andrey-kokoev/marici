"""Online feasibility benchmark (not full next-support enumeration). uv run --with python-sat python ..."""
from ramsey_blind_forcing import *
from pysat.solvers import Solver
import random
from time import perf_counter as now

def main():
 p=json.loads((K/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);qs=json.loads((K/'ramsey_compulsory_kernel_test.json').read_text())['triples'];t=now();I=prepare(A);lib=sorted((s for s in I if 6<=s.bit_count()<=8),key=lambda x:(x.bit_count(),x));rows=[]
 for r in qs:
    a,b,c=r['triple'];rows.append([s for s in lib if s.bit_count()+(not s&a)+(not s&b)+(not s&c)==9])
 prep=now()-t;ref=json.loads((D/'ramsey_all_branch_forcing.json').read_text())['cases'];edges=[[-i-1,-j-1] for i,a in enumerate(A) for j in range(i) if a>>j&1];out=[]
 def shrink(raw):
    with Solver(name='g4',bootstrap_with=edges) as sl:
        for j,r in enumerate(raw):sl.add_clause([-35-j]+[i+1 for i in range(34) if r>>i&1]);
        cs=list(range(35,35+len(raw)));assert not sl.solve(assumptions=cs);cs=sorted(sl.get_core())
        for j in cs.copy():
            test=[k for k in cs if k!=j]
            if not sl.solve(assumptions=test):cs=test
        return tuple(raw[k-35] for k in cs)
 for ordername in ['listed','shuffled']:
    order=list(range(len(qs)));
    if ordername=='shuffled':random.Random(4339).shuffle(order)
    for mode in ['blind','raw','shrunk','directSAT']:
        start=now();bank=[];hits=[];solved=[];dead=set();T=Counter()
        for i in order:
            rs=rows[i];t=now()
            if mode in ('raw','shrunk'):
                R=set(rs);source=next((j for j,cert in bank if all(x in R for x in cert)),None);T['lookup']+=now()-t
                if source is not None:dead.add(i);hits.append((i,source));continue
            t=now()
            if mode=='directSAT':
                with Solver(name='g4',bootstrap_with=edges) as sl:
                    for s in rs:sl.add_clause([v+1 for v in range(34) if s>>v&1]);
                    failed=not sl.solve()
            else:
                result=search(A,rs,feasibility_only=True);failed=not result['witnesses']
            T['solve']+=now()-t
            if failed:
                dead.add(i)
                if mode in ('raw','shrunk'):
                    t=now();raw=result['dead_certificate'];cert=shrink(raw) if mode=='shrunk' else tuple(raw);bank.append((i,cert));T['learn']+=now()-t
        elapsed=now()-start;assert dead=={r[0] for r in ref if r[-1]==0};s=dict(order=ordername,mode=mode,seconds=elapsed,phases=T,hits=hits,learned=[(i,list(c)) for i,c in bank]);out.append(s);print(ordername,mode,round(elapsed,3),len(hits),len(bank),{k:round(v,3) for k,v in T.items()},flush=True)
 (D/'ramsey_online_dead_cache.json').write_text(json.dumps(dict(preparation_seconds=prep,runs=out)))
if __name__=='__main__':main()
