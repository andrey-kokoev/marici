"""Compare the type-reversed rule with forward and inverse at first intermediates. Change type using a correlation, apply the same operator, then pull back; vary the correlation by every six-letter relabeling."""
from itertools import permutations
from ramsey_antipode_extension import run as polarity
from ramsey_iterated_thread_operator import step,final,move,R,D,json
from ramsey_row_quotient_constructor import action

def run():
    rec,=polarity();f=rec['map'];m,=final;p=(m,move(m,R));orbit=[p];
    for _ in range(3):orbit.append(step(*orbit[-1]))
    out=[]
    for p in orbit:
        direct=step(*p);inverse=direct[::-1];counts=[0,0,0];first=None
        for s in permutations(range(6)):
            h=action(s);c=[h[f[x]] for x in range(30)];ci={y:x for x,y in enumerate(c)};q=tuple(move(t,ci) for t in step(*(move(t,c) for t in p)));counts[0 if q==direct else 1 if q==inverse else 2]+=1
            if first is None:first=[next(d for d,j in t if j==26) for t in q]
        out.append(dict(same_inverse_other=counts,dual_at26=first))
    from ramsey_all_thread_row_reversals import run as local
    a,b=local();shifts=[]
    for left,right in ((a,b),(b,a)):
        lookup={tuple(v['output']):v['source'][1] for v in left};shifts.append({v['source'][1]:lookup[tuple(sorted(f[x] for x in v['output']))] for v in right})
    assert all(shifts[1][v]==k for k,v in shifts[0].items());return dict(states=out,dual_to_direct_source=shifts)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_dual_thread_operator.json').write_text(json.dumps(out)+'\n')
