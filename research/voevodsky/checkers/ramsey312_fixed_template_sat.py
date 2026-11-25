"""Exact SAT encoding for a fixed triangle-free eight-newcomer template with alpha=3. Every independent subset of newcomers must hit all corresponding core independent sets. Low-degree and total degree constraints are redundant accelerators."""
from ramsey312_exact_four_cover import *
from itertools import combinations
import threading,time,igraph as ig

def main():
 idx,j,seconds=map(int,sys.argv[1:4]);template=[r for r in json.loads((D/'ramsey312_eight_templates.json').read_text()) if r['alpha']==3][j];edges=list(map(tuple,template['edges']));z=(D/'ramsey312_release26_two_targets.txt').read_text().splitlines()[idx].split();h=F^int(z[2]);a=adj.copy()
 for e in z[5:]:u,v=map(int,e.split(':'));a[u]^=1<<v;a[v]^=1<<u
 lo=sum(1<<v for v in bits(h) if (a[v]&h).bit_count()<11);pool=IDPool();lit=lambda i,v:pool.id((i,v));vs=list(bits(lo));
 def indep(p,k,x):
    if not k:yield x;return
    while p.bit_count()>=k:
        b=p&-p;p-=b;yield from indep(p&~a[b.bit_length()-1],k-1,x|b)
 def minimal(k):
    masks={t&lo for t in indep(h,k,0)};out=[]
    for t in masks:
        y=(t-1)&t
        while y and y not in masks:y=(y-1)&t
        if not y:out.append(list(bits(t)))
    return out
 gr=ig.Graph(n=8,edges=edges);autos=gr.get_isomorphisms_vf2(gr);status=None
 with Solver(name='g4') as sl:
    for i in range(8):
        for v in vs:
            for w in bits(lo&a[v]&((1<<v)-1)):sl.add_clause([-lit(i,v),-lit(i,w)])
        sl.append_formula(CardEnc.atmost([lit(i,v) for v in vs],11-template['deg'][i],vpool=pool).clauses)
    for v in vs:
        for i,jj in edges:sl.add_clause([-lit(i,v),-lit(jj,v)])
        k=11-(a[v]&h).bit_count()
        if k<3:sl.append_formula(CardEnc.atmost([lit(i,v) for i in range(8)],k,vpool=pool).clauses)
    for i in range(8):
        for jj in sorted({p[i] for p in autos}-{i}):
            prev=pool.id();sl.add_clause([prev]);
            for v in reversed(vs):
                x,y=lit(i,v),lit(jj,v);sl.add_clause([-prev,-x,y]);nxt=pool.id();sl.add_clause([-prev,-x,-y,nxt]);sl.add_clause([-prev,x,y,nxt]);prev=nxt
        autos=[p for p in autos if p[i]==i]
    for size in (1,2,3):
        req=minimal(12-size)
        for U in combinations(range(8),size):
            if any(p in edges for p in combinations(U,2)):continue
            group={v:lit(U[0],v) if size==1 else pool.id() for v in vs}
            if size>1:
                for v,y in group.items():sl.add_clause([-y,*[lit(i,v) for i in U]])
            for mask in req:sl.add_clause([group[v] for v in mask])
    timer=threading.Timer(seconds,sl.interrupt);timer.start();status=sl.solve_limited(expect_interrupt=True);timer.cancel();res=dict(k=idx,template=j,status=status,stats=sl.accum_stats());
    if status:
        m=set(sl.get_model());res['s']=[sum(1<<v for v in vs if lit(i,v) in m) for i in range(8)]
 print(res,flush=True);(D/f'ramsey312_fixed27_{idx}_{j}.json').write_text(json.dumps(res))
if __name__=='__main__':main()
