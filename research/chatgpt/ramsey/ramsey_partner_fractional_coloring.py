"""Certified upper bounds on the fractional chromatic number of hard rooted links. Fold dominated vertices, then cover the remainder by sampled incompatible families. The dual is for the restricted LP only and is not a global lower bound."""
from ramsey_fractional_partner_barrier import run,D,json,bits,np,linprog,Q,Counter

def audit():
    hard={(r['parent'],r['first']):r for r in json.loads((D/'ramsey_fractional_partner_barrier.json').read_text()) if Q(r['lower'])>=3};out=[]
    def visit(r,A,M,link,T):
        if (r['parent'],A) not in hard:return
        live=sum(1<<x for x in link);fold=[]
        while True:
            pair=next(((x,y) for x in bits(live) for y in bits(live) if x!=y and not link[x]&live&~link[y]),None)
            if pair is None:break
            x,y=pair;assert not link[x]>>y&1;live^=1<<x;fold.append((M[x],M[y]))
        V=list(bits(live));G={x:live&~(link[x]|1<<x) for x in V}
        def cl(q,p,x):
            if not p|x:yield q;return
            v=max(bits(p|x),key=lambda i:(G[i]&p).bit_count())
            for u in bits(p&~G[v]):
                b=1<<u;yield from cl(q|b,p&G[u],x&G[u]);p^=b;x|=b
        # For a strict upper bound no exhaustive family enumeration is needed.
        from random import Random
        rng=Random(92611); pool=set()
        for _ in range(500):
            order=V.copy();rng.shuffle(order);s=0
            for i in order:
                if not s&link[i]:s|=1<<i
            pool.add(s)
        fam=sorted(pool);mat=np.array([[s>>v&1 for s in fam] for v in V]);lp=linprog(np.ones(len(fam)),A_ub=-mat,b_ub=-np.ones(len(V)),method='highs');assert lp.success;rat=lambda x:Q(float(x)).limit_denominator(100000);c={s:rat(x) for s,x in zip(fam,lp.x) if x>1e-8};y={v:rat(-x) for v,x in zip(V,lp.ineqlin.marginals) if x< -1e-8};lo=sum(y.values())/max(sum(w for i,w in y.items() if s>>i&1) for s in fam);hi=sum(c.values())/min(sum(w for s,w in c.items() if s>>i&1) for i in V);assert all(not s&link[i] for s in c for i in bits(s));out.append(dict(parent=r['parent'],first=A,original=len(link),folds=fold,vertices=[M[v] for v in V],edges=sum((link[v]&live).bit_count() for v in V)//2,upper=str(hi),cover=[([M[i] for i in bits(s)],str(w)) for s,w in c.items()],dual={M[i]:str(w) for i,w in y.items()}))
    run(on_triangle_free=visit);return out
if __name__=='__main__':
    z=audit();print(Counter(Q(r['upper'])<3 for r in z));print(Counter(len(r['vertices']) for r in z));(D/'ramsey_partner_fractional_coloring.json').write_text(json.dumps(z)+'\n')
