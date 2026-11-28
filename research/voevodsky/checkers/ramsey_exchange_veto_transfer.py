"""Fixed first embedding per record. Generate legal one-cut exchange siblings at the completed cube, then test the early branch with no access to other cuts. Certificate checks use integers only."""
from ramsey_cut_exchange_three_tests import sets,packing,np,linprog,Q,combinations,json,D
from ramsey_cube_retention_floor import induced,G,iso
from ramsey_retention_slice import check
from collections import Counter

def flip(g,e):
    i,j=e;h=g[:];h[i]^=1<<j;h[j]^=1<<i;return h

def candidates(g,adds):
    fixed=g[:];six=sets(g,6)
    for i,j in combinations(range(26),2):
        if g[i]>>j&1 and (i,j) not in adds and not any(not q&(g[i]|g[j]) for q in six):fixed[i]^=1<<j;fixed[j]^=1<<i
    return sets(fixed,7),sets(g,7)

def certify(rows,qs):
    A=np.array([[int(not s&q) for s in rows] for q in qs]);zero=np.flatnonzero(A.sum(axis=0)==0)
    if len(zero):return dict(primal=[[rows[zero[0]],8]],den=1)
    res=linprog(-np.ones(len(rows)),A_ub=A,b_ub=np.ones(len(qs)),bounds=(0,None),method='highs');assert res.success
    if -res.fun>=8-1e-8:
        for scale in (10**6,10**9,10**12):
            x=[max(0,round(scale*v)) for v in res.x];tot=sum(x);bound=max(sum(w for w,s in zip(x,rows) if not s&q) for q in qs)
            if tot>=8*bound and tot>0:return dict(primal=[[s,8*w] for s,w in zip(rows,x) if w],den=tot)
        # On the boundary (optimum eight), rounding can break a tight constraint. Recover the basic solution over Q.
        from scipy.linalg import qr
        from sympy import Matrix,ones
        from math import lcm
        cols=np.flatnonzero(res.x>1e-8);tight=A[np.abs(A@res.x-1)<1e-7][:,cols];piv=qr(tight.T,pivoting=True,mode='economic')[2][:len(cols)];v=Matrix(tight[piv].tolist()).inv()*ones(len(cols),1);den=lcm(*(int(t.q) for t in v));num=[int(t*den) for t in v];assert min(num)>=0 and sum(num)==8*den and all(sum(w for w,j in zip(num,cols) if not rows[j]&q)<=den for q in qs);return dict(primal=[[rows[j],w] for j,w in zip(cols,num) if w],den=den)
    y=[max(0,round(10**8*v)) for v in -res.ineqlin.marginals];den=min(sum(w for w,q in zip(y,qs) if not s&q) for s in rows);assert den>0 and sum(y)<8*den;return dict(dual=[[q,w] for q,w in zip(qs,y) if w],den=den,bound=str(Q(sum(y),den)))

def run():
    T=D.parent;labels=json.loads((T/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,labels);src=json.loads((T/'ramsey_double_cross_paths.json').read_text())['cases'];cases={};cache={};F=(1<<26)-1
    for r in sorted(src,key=lambda r:r['record']!=448077):
        idx=r['record'];
        if idx in cases:continue
        adds=set(map(tuple,r['pair']));rm=set(map(tuple,r['removed']));forced=set(map(tuple,r['correct'][0]));pre=a[:];pairs=[];cases[idx]=dict(route=r,exchanges=pairs)
        for e in rm-forced:pre=flip(pre,e)
        old=len(sets(pre,7))
        for good in sorted(rm-forced):
            h=flip(a,good)
            for bad in combinations(range(26),2):
                i,j=bad
                if bad in adds or not a[i]>>j&1:continue
                b=flip(h,bad);key=(good,bad)
                if max(map(int.bit_count,b))>7 or not check(b,F,3,8) or iso(b,a) is not None:continue
                # All roots of the classified circulant are equivalent; nonisomorphic 76-core cannot admit eight ports.
                wrong=flip(pre,bad);right=flip(pre,good);rows,qs=candidates(wrong,adds);w=packing(rows,qs);assert w is None or all(sum(not s&q for s in w)<=1 for q in qs)
                if key not in cache:
                    ss=sets(b,7);cache[key]=certify(ss,ss)
                cert=certify(rows,qs);x=dict(good=good,bad=bad,early_integer=w,early_fractional=cert,finished_fractional=cache[key],new_sevens=[len(sets(right,7))-old,len(qs)-old]);pairs.append(x);print(idx,key,x['new_sevens'],bool(w),cert.get('bound','feasible'),cache[key].get('bound','feasible'),flush=True)
    stats=Counter()
    for r in cases.values():
        for e in r['exchanges']:
            x,y=e['new_sevens'];stats.update(dict(exchanges=1,early_integer_feasible=e['early_integer'] is not None,early_fractional_feasible='primal' in e['early_fractional'],finished_fractional_feasible='primal' in e['finished_fractional'],count_predicts=x<y,count_tie=x==y,count_reversed=x>y))
    print('records',len(cases),'applicable',sum(bool(v['exchanges']) for v in cases.values()),stats);(T/'ramsey_exchange_veto_transfer.json').write_text(json.dumps(dict(core_labels=labels,counts=stats,cases=cases),indent=1)+'\n')
if __name__=='__main__':run()
