"""Contrast deletion repairs with reconstruction: erase ALL exterior links before imposing label-star coverage, triangle freedom and regular degree 8."""
from ramsey_eight_label_star_test import A,label,outside,verts,D,combinations,Counter,json
import z3
W=verts(outside);L=verts(label);sig={v:A[v]&label for v in W};E=[(a,b) for a,b in combinations(W,2) if not sig[a]&sig[b]];X={e:z3.Bool('e%d_%d'%e) for e in E};s=z3.SolverFor('QF_FD');sizes=Counter()
for v in W:
    domain=[e for e in E if v in e];s.add(z3.PbEq([(X[e],1) for e in domain],8-sig[v].bit_count()))
    for j in L:
        if sig[v]>>j&1:continue
        row=[X[e] for e in domain if any(sig[t]>>j&1 for t in e)];sizes[len(row)]+=1;s.add(z3.Or(*row))
for a,b,c in combinations(W,3):
    t=((a,b),(a,c),(b,c));
    if all(e in X for e in t):s.add(z3.Or(*[z3.Not(X[e]) for e in t]))
ref={e:bool(A[e[0]]>>e[1]&1) for e in E}
def fixed_links():
    assert s.check()==z3.sat;fixed=set(E);runs=0
    while fixed:
        s.push();s.add(z3.Or(*[X[e]!=ref[e] for e in sorted(fixed)]));ans=s.check()
        if ans==z3.unsat:s.pop();break
        assert ans==z3.sat;m=s.model();fixed={e for e in fixed if z3.is_true(m.eval(X[e]))==ref[e]};runs+=1;s.pop()
    return fixed,runs
if __name__=='__main__':
    fixed,runs=fixed_links();out={'eligible_links':len(E),'star_widths':dict(sizes),'forced':sorted(fixed),'countermodels_sampled':runs};print(out);(D/'ramsey_eight_label_blind_stars.json').write_text(json.dumps(out)+'\n')
