"""Reduced-side selector: project the output cell into the source block by midpoint pairing. Require that (root,m) and (m,paired output) have the same within-block decoder adjacency. No target-map lookup until selection. Test all 5 choices of root."""
from ramsey_pentagon_contrast_transport import L,orbits,neighborhood_tests
from itertools import permutations
from pathlib import Path
import hashlib,json

def main():
    labels=[(3*(a+b)%5,int((a-b)%5 not in (1,4))) for a,b in L]; at={x:i for i,x in enumerate(labels)};out=[]
    for mask in range(1<<len(orbits)):
        E=set().union(*(o for i,o in enumerate(orbits) if mask>>i&1));S=neighborhood_tests(E)
        if S is None:continue
        for root in range(5):
            roots=[f for f in permutations(range(5)) if all(f[f[m]]==(2*root-m)%5 for m in range(5))];assert len(roots)==2
            def linked(m,n,t):return tuple(sorted([at[m,t],at[n,t]])) in E
            # Neither the adjacency test nor its two branches use directed displacements.
            score=lambda f:sum(linked(root,m,t)==linked(m,f[m],t) for m in range(5) if m!=root for t in (0,1))
            scores=[score(f) for f in roots];assert sorted(scores)==[0,8];f=roots[scores.index(8)];p=tuple(at[f[m],1-t] for m,t in labels)
            # Independent input-side target on actual chord endpoints, now compared.
            target=tuple(L.index(tuple(sorted(((2*a-root)%5,(2*b-root)%5)))) for a,b in L);assert p==target
            assert {tuple(sorted((p[a],p[b]))) for a,b in E}==E;assert {sum(1<<p[i] for i in range(10) if s>>i&1) for s in S}==S
            out.append(dict(mask=mask,root=root,selected=f,agreement_scores=scores))
    assert len(out)==20;r=dict(cases=out,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(Path(__file__).resolve().parents[1]/'results/ramsey_pentagon_step_selector.json').write_text(json.dumps(r,indent=2)+'\n');print(len(out),'unique selections')
if __name__=='__main__':main()
