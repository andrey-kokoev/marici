"""Construct from a square and observed bits; use degree feasibility to prove edge colors."""
from itertools import combinations, permutations
from collections import Counter
import json
from ramsey_square_repair_counts import ways,predict
from ramsey_plan_total_probes import plan
from ramsey_inherited_swap_selector import D


def construct(sq,tests,bits):
    W=sorted(set(range(1,11))-set().union(*sq))
    blue={e for e,b in zip(tests,bits) if b};red=set(tests)-blue
    def forced_blue(e):return not ways(W,red|{e},blue)
    def forced_red(e):return not ways(W,red,blue|{e})
    return from_forced_colors(sq,forced_blue,forced_red)


def from_forced_colors(sq,forced_blue,forced_red):
    U=set().union(*sq);W=sorted(set(range(1,11))-U);f,=set.intersection(*map(set,sq));mov=U-{f}
    for e in predict(sq)[0]:
        if not forced_blue(e):continue
        u,v=e;x,z=u+1,v-1;Y=sorted(mov-{x,z});K=set(W)-set(e)
        for ab in combinations(sorted(K),2):
            a,b=ab;h,=K-{a,b}
            if forced_red(ab):
                y,w=next((j,k) for j,k in permutations(Y) if abs(a-j)!=1 and abs(b-k)!=1)
                return 'fixed red pair',e,ab,[(x,h,b),(z,y,a),(x,h,a),(z,w,b)]
        if min(abs(f-u),abs(f-v))==1:continue
        for ab in combinations(sorted(K),2):
            a,b=ab;h,=K-{a,b}
            if forced_blue(ab) and all(abs(h-y)!=1 for y in Y):
                y,w=Y;return 'fixed blue pair',e,ab,[(x,a,b),(z,y,h),(z,a,b),(x,w,h)]


def audit():
    ref=json.loads((D/'ramsey_common_quartet_readout.json').read_text())['classes'];out=[];summary=Counter()
    from ramsey_two_repairs_opposite import run
    keys=run()
    from ramsey_pentagon_selector import charts
    charts_by_square={sq:cs for sq,_,cs in charts()}
    for r in ref:
        sq=tuple(map(tuple,r['square']));edges,_,_,_=plan(sq);bits=tuple(r['bits']);ans=construct(sq,edges,bits);assert bool(ans)==bool(r['common_count'])
        if not ans:continue
        tag,e,ab,rs=ans;rows=tuple(tuple(sorted(s)) for s in rs);quartet=tuple(sorted(rows));cs=[c for c in charts_by_square[sq] if tuple(p not in c for p in edges)==bits];assert all((sq,tuple(sorted(c)),quartet) in keys for c in cs)
        summary[len(cs),tag]+=1;out.append(dict(square=sq,probes=r['tests'],bits=bits,cycles=len(cs),rule=tag,missed=e,inner=ab,repairs=[rows[:2],rows[2:]]))
    print(summary);print(next(t for t in out if t['cycles']>1));(D/'ramsey_readout_forced_quartet.json').write_text(json.dumps(dict(summary={str(k):v for k,v in summary.items()},plans=out),indent=2)+'\n')
if __name__=='__main__':audit()
