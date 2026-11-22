"""Use only the unordered fan left at the two row-related entry partitions. Swap its tips in the tetrahedron, not its apex or unused corner. Test the predicted common assignment against all boundary completions."""
from ramsey_join_flag_phase import lift,P,T,X,D,json
from ramsey_row_quotient_constructor import R,move

def prediction(j,d):
    e,f=[set(X[k]) for k in P[d]];u,v=sorted(e^f);g=lift(tuple(v if i==u else u if i==v else i for i in range(1,5)));assert g[d]==d
    return dict(entry=j,unused=d,tips=[u,v],predicted=g[j],incident=[k for k,t in enumerate(T,15) if P[d] in t],fixed=[k for k,t in enumerate(T,15) if P[d] in t and g[k]==k])

def run():
    rows=json.loads((D/'ramsey_literal_swap_polarity_controls.json').read_text());sel=next(q for q in rows if q['selected']);res=[]
    for q in rows:
        m=frozenset(map(tuple,q['matching']));c=m&move(m,R);out=[]
        for j in (16,R[16]):
            d,={P.index(e) for e in T[j-15]}-{x for x,y in m|move(m,R) if y==j};r=prediction(j,d);out.append(r|dict(common=(d,r['predicted']) in c))
        res.append(dict(entries=out,selected=q['selected'],same_strip=q['entry_cycle']==sel['entry_cycle'] and len(c)==10,same_return=q['exit_thread']==sel['exit_thread']))
    return res
if __name__=='__main__':
    out=run();print(next(q for q in out if q['selected']));print(sum(all(r['common'] for r in q['entries']) for q in out));(D/'ramsey_fan_tip_exchange.json').write_text(json.dumps(out)+'\n')
