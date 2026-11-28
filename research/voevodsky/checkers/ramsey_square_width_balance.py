"""Does the actual width-step multiplicity pick the two graph orientations?"""
from itertools import product,combinations
from collections import Counter
from pathlib import Path
import json
from ramsey_matrix_width_step import matrix


def audit():
    old,ix=matrix(7);new,iy=matrix(8);U=set(iy);faces=[]
    for a in sorted(U):
        for i,j in combinations(range(3),2):
            def move(x,y):return tuple(v+(k==i)*x+(k==j)*y for k,v in enumerate(a))
            c=[move(x,y) for x,y in [(0,0),(1,0),(1,1),(0,1)]]
            if not set(c)<=U or not any(8 in r for r in c):continue
            w=[len(iy[r]) for r in c];prev=[len(ix.get(r,())) for r in c];choices=list(product(*[[(t+2)%4,(t+3)%4] for t in range(4)]));cyc={h for h in choices if len(set(h))==4};assert len(cyc)==2
            def test(weights):
                def passed(h,cols):return sum(weights)*sum(all(v in c[b] for v in cols) for b in h)==4*sum(f for r,f in zip(c,weights) if all(v in r for v in cols))
                margin={h for h in choices if all(passed(h,[v]) for v in range(1,9))};joint={h for h in margin if passed(h,[a[i]+1,a[j]+1])};return [len(margin),len(margin&cyc),len(joint),len(joint&cyc)],sorted(margin-cyc)
            uniform,extra=test([1]*4);actual,_=test(w);faces.append(dict(corners=c,width7=prev,width8=w,distinct_results=uniform,occurrence_results=actual,false_positive=extra[:1]))
    graph=json.loads((Path(__file__).resolve().parents[1]/'results/ramsey_square_coverage_assignment.json').read_text());assert graph['stats']['squares']==81 and graph['by_largest_witness']['0']==162
    out=dict(result_order=['margin_pass','of_which_cyclic','joint_pass','of_which_cyclic'],cases=faces);print(len(faces),Counter(tuple(t['occurrence_results']) for t in faces),Counter(tuple(t['distinct_results']) for t in faces));print(faces[0]);(Path(__file__).resolve().parents[1]/'results/ramsey_square_width_balance.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
