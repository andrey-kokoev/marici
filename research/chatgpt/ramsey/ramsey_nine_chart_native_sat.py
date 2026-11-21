"""Classification-free synthesis. Input ONLY 26 subset addresses; no regularity assumption. Learn obstruction clauses from premature SAT solutions, blocking verified completions one by one."""
from itertools import combinations
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from pysat.formula import IDPool
from ramsey_address_to_cube import S,probes,D,json
import time

def run(audit=False):
    E=[e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]]];X={e:i for i,e in enumerate(E,1)};pool=IDPool(start_from=194);s=Solver(name='cadical195');cl=lambda J:[X[e] for e in combinations(J,2) if e in X];
    for J in combinations(range(26),3):
        t=cl(J)
        if len(t)==3:s.add_clause([-i for i in t])
    for i,m in enumerate(S):
        vs=[x for e,x in X.items() if i in e];s.append_formula(CardEnc.atmost(vs,8-m.bit_count(),vpool=pool,encoding=EncType.seqcounter).clauses)
    pos=set()
    for mask in range(256):
        n=mask.bit_count()
        if n>6:continue
        for J in combinations([i for i,m in enumerate(S) if not m&~mask],n+1):pos.add(tuple(cl(J)))
    for t in sorted(pos):s.add_clause(t)
    print('initial positive clauses',len(pos),flush=True);rounds=0;models=[];learned=0;t0=time.monotonic();stages=[];local=[]
    while s.solve():
        m=s.get_model();B=[0]*26;w=0
        for x,(i,j) in enumerate(E,1):
            if m[x-1]>0:w|=1<<(x-1);B[i]|=1<<j;B[j]|=1<<i
        defects=[]
        def visit(V,J,U):
            while V:
                b=V&-V;V-=b;i=b.bit_length()-1;K=J+(i,);u=U|S[i]
                if len(K)==8 or len(K)>u.bit_count():defects.append(cl(K))
                else:visit(V&~B[i],K,u)
        visit((1<<26)-1,(),0)
        if audit:
            missed=[]
            for j in range(8):
                star=sum(1<<i for i,m0 in enumerate(S) if m0>>j&1);assert star.bit_count()==7
                missed.extend((j,i) for i in range(26) if not star>>i&1 and not B[i]&star)
            local.append(dict(wiring=w,valid=not defects,missed_stars=missed,degree_range=[min(B[i].bit_count()+v.bit_count() for i,v in enumerate(S)),max(B[i].bit_count()+v.bit_count() for i,v in enumerate(S))]))
        if not defects:
            models.append(w);s.add_clause([-x if w>>(x-1)&1 else x for x in range(1,194)]);print('valid',len(models),'round',rounds,flush=True)
        else:
            if audit:s.add_clause([-x if w>>(x-1)&1 else x for x in range(1,194)])
            else:
                for c in defects:s.add_clause(c)
            learned+=len(defects)
        rounds+=1
        if rounds%100==0:print(rounds,learned,round(time.monotonic()-t0,2),flush=True)
    print('EXHAUSTED',len(models),rounds,learned,flush=True);return dict(local_audit=local,wirings=models,initial_positive=len(pos),rounds=rounds,learned_clauses=learned,probe_words=[sum(((w>>(X[e]-1))&1)<<i for i,e in enumerate(probes)) for w in models])
if __name__=='__main__':
    import sys
    audit='--audit' in sys.argv;(D/('ramsey_nine_chart_local_audit.json' if audit else 'ramsey_nine_chart_native_sat.json')).write_text(json.dumps(run(audit))+'\n')
