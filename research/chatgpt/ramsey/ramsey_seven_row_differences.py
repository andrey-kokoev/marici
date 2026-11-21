"""Project all legal wirings onto the vector of mismatched link-orbits of the literal row exchange. Block projections, not labeled wirings."""
from ramsey_seven_transport_synthesis import D,json,z3,S,E,solver
from collections import Counter
from itertools import combinations

def run():
    perm=(0,1,4,5,2,3,6);m=[S.index(sum(1<<perm[i] for i in range(7) if s>>i&1)) for s in S];orb=[];X=[]
    for (a,b),e in E.items():
        t=tuple(sorted((m[a],m[b])))
        if (a,b)<t:orb.append(((a,b),t));X.append(e!=E[t])
    rows=[];best=None
    while (res:=solver.check())==z3.sat:
        mod=solver.model();Y=[z3.is_true(mod.eval(x,model_completion=True)) for x in X];mismatch=sum(1<<i for i,b in enumerate(Y) if b);rows.append(mismatch)
        if best is None or sum(Y)<best['size']:best=dict(size=sum(Y),mask=mismatch,red_links=[p for p,x in E.items() if z3.is_true(mod.eval(x))]);
        solver.add(z3.Or(*[z3.Not(x) if b else x for x,b in zip(X,Y)]))
    assert res==z3.unsat
    # Find an exact minimum diagnostic list: in every wiring, some pair on this list must differ.
    Z=[z3.Bool('choose'+str(i)) for i in range(len(X))];s=z3.Solver();s.add(*[z3.Or(*[x for i,x in enumerate(Z) if q>>i&1]) for q in rows]);covers=[]
    for d in range(1,len(Z)+1):
        s.push();s.add(z3.PbLe([(x,1) for x in Z],d));
        while s.check()==z3.sat:
            c=[i for i,x in enumerate(Z) if z3.is_true(s.model().eval(x))];covers.append(c);s.add(z3.Or(*[z3.Not(Z[i]) for i in c]))
        s.pop()
        if covers:break
    return dict(address_masks=S,edge_orbits=orb,mismatch_masks=rows,histogram=dict(sorted(Counter(x.bit_count() for x in rows).items())),best=best,minimum_diagnostic_lists=covers)
if __name__=='__main__':
    r=run();print(len(r['edge_orbits']),len(r['mismatch_masks']),r['histogram'],len(r['minimum_diagnostic_lists']),r['minimum_diagnostic_lists'][:5]);(D/'ramsey_seven_row_differences.json').write_text(json.dumps(r)+'\n')
