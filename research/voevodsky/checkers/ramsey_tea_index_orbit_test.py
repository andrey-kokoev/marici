"""All invariant undirected binary readings of the 40-record interest index, by SAT + exact blue-clique separation. uv run --with python-sat python <file>."""
from itertools import combinations,product
from pysat.solvers import Solver

def run():
    rows=list(product(range(3),range(10)))+[(3,p) for p in combinations(range(5),2)]
    def perm(i,a,b):return b if i==a else a if i==b else i
    def action(r,t):
        c,p=r
        if t=='customers':return (perm(c,0,2),p)
        a,b=t
        return (c,tuple(sorted(perm(x,a,b) for x in p)) if c==3 else perm(p,a,b))
    gens=[(i,i+1) for i in range(4)]+[(5,6),(7,8),'customers'] # products: five tea, two coffee, two cocoa, one juice
    pp=[tuple(rows.index(action(x,t)) for x in rows) for t in gens];allpairs=list(combinations(range(40),2));orb={}
    for e in allpairs:
        if e in orb:continue
        j=max(orb.values(),default=0)+1;stack=[e];orb[e]=j
        while stack:
            a,b=stack.pop()
            for g in pp:
                f=tuple(sorted((g[a],g[b])))
                if f not in orb:orb[f]=j;stack.append(f)
    def clauses(S):return tuple(sorted({orb[e] for e in combinations(S,2)}))
    tri={tuple(-x for x in clauses(s)) for s in combinations(range(40),3)}
    def blue10(model):
        red=set(model);adj=[0]*40
        for (a,b),j in orb.items():
            if j not in red:adj[a]|=1<<b;adj[b]|=1<<a
        def rec(mask,sel):
            if len(sel)==10:return sel
            while mask.bit_count()>=10-len(sel):
                bit=mask&-mask;mask^=bit;v=bit.bit_length()-1;ans=rec(mask&adj[v],sel+[v])
                if ans:return ans
        return rec((1<<40)-1,[])
    cuts=[]
    with Solver(name='cadical195',bootstrap_with=sorted(tri)) as sol:
        while sol.solve():
            w=blue10(sol.get_model());
            if w is None:raise AssertionError('admissible model: '+str(sol.get_model()))
            cuts.append(w);sol.add_clause(clauses(w))
    with Solver(name='glucose4',bootstrap_with=[*tri,*(clauses(w) for w in cuts)]) as s:assert not s.solve()
    print('records',len(rows),'pair orbits',max(orb.values()),'triangle clauses',len(tri),'blue 10-set cuts',len(cuts),'UNSAT (CaDiCaL and Glucose)')
if __name__=='__main__':run()
