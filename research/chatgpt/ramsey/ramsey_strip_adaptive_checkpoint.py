"""Given the full outward path and matched gates 1 and 10, compute all minimum certificates against arbitrary simple, disjoint return paths at the literal poles. Neither mark readings nor closure used for the certificate."""
from itertools import combinations
from pathlib import Path
import json
from ramsey_strip_transport_recognition import paths,r,s,t
rows=[z for z in json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text()) if (z['path'][0],z['path'][-1])==(s,t)]
for n,z in enumerate(rows,1):
    p=tuple(z['path']);rp=tuple(r[x] for x in p)
    def test(p,rp):
        mates=[q for q in paths if q[1]==rp[1] and q[10]==rp[10] and set(p[1:-1]).isdisjoint(q[1:-1])];assert rp in mates
        diff=[{i for i in range(2,10) if q[i]!=rp[i]} for q in mates if q!=rp]
        for k in range(3):
            tests=[c for c in combinations(range(2,10),k) if all(set(c)&v for v in diff)]
            if tests:return len(diff),tests
        raise AssertionError('fixed girth certificate missing')
    a=test(p,rp);assert a==test(rp,p)
    from ramsey_strip_prism_proof import labels,rep
    toward=labels[rep(p[3])][0].upper()==labels[rep(p[10])][0].upper();chosen=7 if toward else 4;assert (chosen,) in a[1];print(n,z['closes'],'false returns',a[0],'optimal checkpoints',a[1]);
