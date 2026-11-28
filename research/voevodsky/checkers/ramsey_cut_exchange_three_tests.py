"""Frozen cut exchange on 448077. A fractional verdict requires an exact rational certificate; floating point selects a candidate only. Run with uv run --no-project --with scipy."""
from ramsey_port_descendants import D,CAT,decode,gzip,islice,json,induced,combinations
from fractions import Fraction as Q
from scipy.optimize import linprog
import numpy as np

def sets(a,k):
    rows=[0]
    for i,v in enumerate(a):rows.extend([s|1<<i for s in rows if not s&v and s.bit_count()<k]);
    return [s for s in rows if s.bit_count()==k]

def packing(rows,qs):
    # Merge equal missed-demand sets. Repeats are possible only for zero misses.
    d={sum(1<<i for i,q in enumerate(qs) if not q&s):s for s in rows}
    if 0 in d:return [d[0]]*8
    order=sorted(d,key=int.bit_count)
    def visit(opts,k):
        if not k:return []
        for j,m in enumerate(opts):
            if len(opts)-j<k:break
            w=visit([x for x in opts[j+1:] if not x&m],k-1)
            if w is not None:return [d[m]]+w
    return visit(order,8)

def early(g,adds):
    fixed=g[:];six=sets(g,6);qs=sets(g,7)
    for i,j in combinations(range(26),2):
        if g[i]>>j&1 and (i,j) not in adds and not any(not s&(g[i]|g[j]) for s in six):fixed[i]^=1<<j;fixed[j]^=1<<i
    rows=sets(fixed,7);w=packing(rows,qs)
    if w is not None:assert len(w)==8 and all(s in rows for s in w) and all(sum(not s&q for s in w)<=1 for q in qs)
    return dict(demands=len(qs),optimistic_rows=len(rows),witness=w)

def fractional(g):
    rows=sets(g,7);A=np.array([[int(not q&s) for s in rows] for q in rows]);zero=np.where(A.sum(axis=0)==0)[0]
    if len(zero):return dict(primal=[[rows[zero[0]],'8']])
    p=linprog(-np.ones(len(rows)),A_ub=A,b_ub=np.ones(len(rows)),bounds=(0,None),method='highs');assert p.success
    weights=lambda v:[Q(float(x)).limit_denominator(100000) for x in v]
    if -p.fun>=8-1e-8:
        w=weights(p.x);assert sum(w)>=8;w=[x*8/sum(w) for x in w];assert min(w)>=0 and all(sum(x for x,s in zip(w,rows) if not s&q)<=1 for q in rows);return dict(primal=[[s,str(x)] for s,x in zip(rows,w) if x])
    # Round to a common denominator, then normalize by the least exact row cover.
    y=[max(0,round(10**7*x)) for x in -p.ineqlin.marginals];floor=min(sum(x for x,q in zip(y,rows) if not s&q) for s in rows);assert floor>0 and sum(y)<8*floor;return dict(upper_bound=str(Q(sum(y),floor)),denominator=floor,dual_numerators=[[q,x] for q,x in zip(rows,y) if x])

def run():
    T=D.parent;r=json.loads((T/'ramsey_cross_residual_propagation.json').read_text())['survivors'][0]['start'];z=r['z'];vs=[i for i in range(27) if i!=z]
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,448077,None)).strip())
    for i,j in r['pair']+r['forced']:b[i]^=1<<j;b[j]^=1<<i
    g=induced(b,vs);adds={tuple(vs.index(i) for i in e) for e in r['pair']};old=set(sets(g,7));trials=[]
    for e in [(0,17),(14,19)]:
        i,j=map(vs.index,e);h=g[:];h[i]^=1<<j;h[j]^=1<<i;out=early(h,adds);out.update(cut=e,new_sevens=len(set(sets(h,7))-old));print(e,out,flush=True);trials.append(out)
    src=json.loads((T/'ramsey_free_cross_profile.json').read_text());ends=[]
    for c in src['core_candidates']:
        if c['z']==z and c['additions']==r['pair']:
            f=fractional(c['core']);ends.append(dict(success=c['passes_seven'],certificate=f));print('LP',c['passes_seven'],{k:(len(v) if isinstance(v,list) else v) for k,v in f.items()},flush=True)
    assert len(ends)==2;out=dict(record=448077,core_labels=vs,mandatory_prefix=r,base_blue_sevens=len(old),trials=trials,finished=ends);(T/'ramsey_cut_exchange_three_tests.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
