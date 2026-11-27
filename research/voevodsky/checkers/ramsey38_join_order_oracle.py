"""Upper bound under one shared seven-label order per root. Only targets determine the oracle, never call this blind."""
from ramsey38_tabulated_join_transfer import table,R,gzip,graph,prev,json,Counter
from itertools import permutations
from fractions import Fraction

def run():
    ref=json.loads(R.read_text());roots={e['record']:e['root'] for e in ref['per_record']};pat=[s for s in table() if 1 not in s];perms=list(permutations(range(7)));flags={};n=len(perms);allframes=(1<<n)-1
    for j,order in enumerate(perms):
        for s in pat:
            m=sum(1<<order[k-2] for k in s);flags[m]=flags.get(m,0)|(1<<j)
    assert len(flags)==35 and all(v.bit_count()==1728 for v in flags.values());tot=Counter();hist=Counter();report=[];hidden=Fraction()
    with gzip.open(prev.catalogue,'rt') as f:
        for i,w in enumerate(f,1):
            if i not in roots:
                if i>max(roots):break
                continue
            g=graph(w.strip());u=roots[i];L=sorted(g[u]);O=sorted(set(g)-set(L)-{u});rows={v:sum(1<<j for j,x in enumerate(L) if x in g[v]) for v in O if len(g[v]&set(L))==4};masks=list(rows.values());assert len(masks)==len(set(masks));hist[len(rows)]+=1
            common=allframes
            for m in masks:common&=flags[m]
            if common:best=len(rows);opt=common
            else:
                scores=[sum((flags[m]>>j)&1 for m in masks) for j in range(n)];best=max(scores);opt=sum(1<<j for j,s in enumerate(scores) if s==best)
            j=(opt&-opt).bit_length()-1;columns=[u,*[L[k] for k in perms[j]]];tot['targets']+=len(rows);tot['covered']+=best;tot['nonempty']+=bool(rows);tot['full_nonempty']+=bool(rows) and bool(common)
            if rows:tot['min_optima']=min(tot.get('min_optima',n),opt.bit_count())
            for m in masks:
                frames=allframes
                for t in masks:
                    if m!=t:frames&=flags[t]
                if frames:hidden+=Fraction((frames&flags[m]).bit_count(),frames.bit_count());tot['loo_evaluable']+=1
            # Direct replay of the selected example with one order for the entire root.
            have={frozenset(columns[k-1] for k in s) for s in pat};assert sum(g[v]&set(L) in have for v in rows)==best
            report.append(dict(record=i,root=u,target_rows=list(rows),best=best,optima=opt.bit_count(),columns=columns))
    assert tot['targets']==ref['counts']['true_fours'];print(tot,hist,float(hidden));prev.save(prev.out/'ramsey38_join_order_oracle.json',dict(source_sha=prev.sha(R.read_bytes()),stats=dict(tot),rows_per_root=dict(hist),expected_hits_uniform_among_frames_fitting_other_fours=float(hidden),roots=report))
if __name__=='__main__':run()
