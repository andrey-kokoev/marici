"""CEGAR: solve exactly for four anchored (common vertex, missed independent ten) certificates. Uncovered support adds a necessary coverage clause."""
from ramsey312_google_two_step import *
from pysat.card import CardEnc
from pysat.formula import IDPool

def solve(d,s):
 h=F^sum(1<<i for i in d);anchors=[adj[i]&h for i in d];pool=IDPool();base=[];B=[];T=[]
 for j,m in enumerate(anchors):
    b={v:pool.id(('b',j,v)) for v in bits(m)};t={v:pool.id(('t',j,v)) for v in bits(h&~m)};base.append(list(b.values()));base.extend(CardEnc.atleast(list(t.values()),10,vpool=pool).clauses);base.extend([-id,-t[w]] for v,id in t.items() for w in bits(adj[v]&((1<<v)-1)) if w in t);B.append(b);T.append(t)
 with Solver(name='g4',bootstrap_with=base) as sl:
    pending=[]
    while sl.solve():
        model={i for i in sl.get_model() if i>0};c=[(1<<next(v for v,l in b.items() if l in model),sum(1<<v for v in [v for v,l in t.items() if l in model][:10])) for b,t in zip(B,T)]
        missed=[x for x in s if not any(x&b and not x&t for b,t in c)]
        if not missed:return dict(cert=c,challenges=len(pending))
        # Enforce exact model semantics (all chosen b's present, all chosen t's missed).
        for x in missed[:12]:
            assert x not in pending;pending.append(x);p=[pool.id(('p',x,j)) for j in range(len(d))];sl.add_clause(p)
            for z,b,t in zip(p,B,T):
                for v,l in b.items():
                    if not x>>v&1:sl.add_clause([-z,-l])
                for v,l in t.items():
                    if x>>v&1:sl.add_clause([-z,-l])
    return dict(cert=None,obstructing_supports=pending)
if __name__=='__main__':
 rows=[l.split() for l in (D/'ramsey312_stress4_results.txt').read_text().splitlines()];out=[]
 for x in sorted((x for x in rows if x[5]=='RAW'),key=lambda x:int(x[4]))[:int(sys.argv[1])]:
    d=list(map(int,x[:4]));res=solve(d,list(map(int,x[6:])));out.append(dict(d=d,**res));
    if res['cert'] is None:print('FIRST UNSAT',d,len(res['obstructing_supports']),flush=True);break
 (D/'ramsey312_exact_four_cover.json').write_text(json.dumps(out));print('tested',len(out))
