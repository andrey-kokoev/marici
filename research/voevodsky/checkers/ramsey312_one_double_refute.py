"""Independent SAT refutation for each anchored one-double partition. Activations give small challenge lists; positives replayed by an uncovered-support SAT search."""
from ramsey312_exact_four_cover import *
from itertools import combinations
from functools import reduce
from operator import or_,and_

def refute(h,d,s,p,allow_cover=False,slack_at=None):
 pool=IDPool();base=[];bt=[];gate={};A={i:adj[i]&h for i in d}
 for j,g in enumerate(p):
    common=reduce(and_,(A[i] for i in g));un=reduce(or_,(A[i] for i in g));B={v:pool.id(('b',j,v)) for v in bits(common)};T={v:pool.id(('t',j,v)) for v in bits(h&~un)};k=11-len(g)-int(j==slack_at);base.append(list(B.values()));base.extend(CardEnc.atleast(list(T.values()),k,vpool=pool).clauses);base.extend([-T[v],-T[w]] for v in T for w in bits(adj[v]&((1<<v)-1)) if w in T);bt.append((B,T,k))
 with Solver(name='g4',bootstrap_with=base) as sl:
    while sl.solve(assumptions=list(gate)):
        model=set(sl.get_model());rect=[(1<<next(v for v,l in b.items() if l in model),sum(1<<v for v in [v for v,l in t.items() if l in model][:k])) for b,t,k in bt];miss=[x for x in s if not any(x&b and not x&t for b,t in rect)]
        if not miss:
            assert allow_cover,'one-double cover unexpectedly exists';return dict(cert=rect)
        for x in miss[::max(1,len(miss)//18)][:19]:
            a=pool.id(('gate',x));assert a not in gate;gate[a]=x;pick=[pool.id(('p',x,j)) for j in range(len(p))];sl.add_clause([-a,*pick]);
            for z,(b,t,k) in zip(pick,bt):
                for v,l in b.items():
                    if not x>>v&1:sl.add_clause([-z,-l])
                for v,l in t.items():
                    if x>>v&1:sl.add_clause([-z,-l])
    core=sl.get_core() or [];assert not sl.solve(assumptions=core)
    for a in core[:]:
        sub=[z for z in core if z!=a]
        if not sl.solve(assumptions=sub):core=sub
    return [gate[a] for a in core]

def main():
 z=json.loads((D/'ramsey312_double_double.json').read_text());mask=z['d'];d=list(bits(mask));h=F^mask;el=list(sets(h,11));s=list(map(int,open(sys.argv[1]).read().split()));assert s.pop(0)==mask and len(s)==z['n'];parts=[[(i,) for i in d]]+[[g]+[(i,) for i in d if i not in g] for g in combinations(d,2)];out=[]
 for p in parts:
    small=refute(h,d,s,p);assert all(not x&~h and all(not adj[i]&x for i in bits(x)) and all(x&t for t in el) for x in small);out.append(dict(groups=p,obstruction=small));print(p[0],len(small),flush=True)
 cs=[[-i-1,-j-1] for i in bits(h) for j in bits(h&adj[i]&((1<<i)-1))]+[[v+1 for v in bits(t)] for t in el];budget=0
 for g,b,t in z['cert']:
    assert g&mask==g and b.bit_count()==1 and not (b|t)&~h and all(not adj[v]&t for v in bits(t));k=11-t.bit_count();budget+=k;assert k==g.bit_count();cs.append([-b.bit_length(),*[i+1 for i in bits(t)]])
 assert budget==6
 with Solver(name='g4',bootstrap_with=cs) as sl:assert not sl.solve()
 (D/'ramsey312_one_double_refutation.json').write_text(json.dumps(dict(d=d,partitions=out)))
if __name__=='__main__':main()
