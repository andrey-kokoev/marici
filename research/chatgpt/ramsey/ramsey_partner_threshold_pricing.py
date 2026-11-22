"""Column generation for threshold chi_f<3, rational certificates. Price the restricted dual exactly on positive-weight vertices using a memoized weighted independent-set recurrence."""
from ramsey_fractional_partner_barrier import D,json,bits,Q,linprog,np,Counter,lcm
from ramsey_capacity_transfer_78 import decode,inds
from functools import lru_cache
from random import Random

def classify(r,H):
    V=r['vertices'];n=len(V);A=r['first'];I=inds(H);rows=[t for t in I if t.bit_count()==6 or t.bit_count()==5 and not t&A];miss=[sum(1<<j for j,t in enumerate(rows) if not s&t) for s in V];E=[sum(1<<j for j,u in enumerate(miss) if not u&v) for v in miss];assert sum(e.bit_count() for e in E)==2*r['edges'];rng=Random(71317);pool=set();idx={s:i for i,s in enumerate(V)}
    for fam,_ in r['cover']:pool.add(sum(1<<idx[s] for s in fam))
    def extend(s):
        order=list(range(n));rng.shuffle(order)
        for i in order:
            if not E[i]&s:s|=1<<i
        return s
    for _ in range(1200):pool.add(extend(0))
    for it in range(1000):
        fs=sorted(pool);mat=np.array([[s>>i&1 for s in fs] for i in range(n)]);lp=linprog(np.ones(len(fs)),A_ub=-mat,b_ub=-np.ones(n),method='highs');assert lp.success;rat=lambda f:Q(float(f)).limit_denominator(100000);x={s:rat(f) for s,f in zip(fs,lp.x) if f>1e-8};scale=min(sum(f for s,f in x.items() if s>>i&1) for i in range(n));upper=sum(x.values())/scale
        if upper<3:
            assert all(not s&E[i] for s in x for i in bits(s));return dict(upper=str(upper),priced=it,cover=[([V[i] for i in bits(s)],str(f/scale)) for s,f in x.items()])
        y=[rat(max(0,-f)) for f in lp.ineqlin.marginals];den=lcm(*(q.denominator for q in y));w=[int(q*den) for q in y];live=sum(1<<i for i,v in enumerate(w) if v)
        @lru_cache(None)
        def best(b):
            if not b:return 0,0
            i=max(bits(b),key=lambda j:(E[j]&b).bit_count());z=b^(1<<i);value,s=best(z&~E[i]);take=(value+w[i],s|1<<i);return max(take,best(z)) if E[i]&b else take
        val,s=best(live);best.cache_clear();lower=Q(sum(w),val)
        if lower>=3:return dict(lower=str(lower),upper=str(upper),priced=it,dual={V[i]:str(Q(w[i],val)) for i in bits(live)},max_family=[V[i] for i in bits(s)])
        before=len(pool)
        for _ in range(16):pool.add(extend(s))
        assert len(pool)>before
    raise RuntimeError('pricing limit')
if __name__=='__main__':
    hist=json.loads((D/'ramsey_partner_fractional_coloring.json').read_text());base={r['parent']:r['deleted'] for r in json.loads((D/'ramsey_bare_core_rank.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in sorted((r for r in hist if Q(r['upper'])>=3),key=lambda r:len(r['vertices'])):
        p=r['parent'];G=decode(lines[p-1]);V=[i for i in range(22) if i!=base[p]];H=[sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V];res=classify(r,H);out.append(dict(parent=p,first=r['first'],n=len(r['vertices']),**res));print(p,r['first'],len(r['vertices']),float(Q(res['upper'])),res.get('lower'),res['priced'],flush=True);(D/'ramsey_partner_threshold_pricing.json').write_text(json.dumps(out)+'\n')
