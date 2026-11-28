"""Compare labeled port neighborhoods before and after erasing width-eight sheet labels."""
from itertools import product,combinations
from collections import Counter
import json
from ramsey_excel_corner_predecessor_readout import squares,CAT,decode,check,D
from ramsey_matrix_width_step import matrix

def audit():
    # Sheet end: two-swap cycles touching the new column; directed turn = follow the listed cycle.
    _,idx=matrix(8);sheet=[]
    for r in sorted(idx):
        for i,j in combinations(range(3),2):
            cs=tuple(tuple(v+x*(k==i)+y*(k==j) for k,v in enumerate(r)) for x,y in [(0,0),(1,0),(1,1),(0,1)])
            if set(cs)<=idx.keys() and any(8 in q for q in cs):sheet.append(cs)
    cases=[];parents=0
    for rec,line in enumerate((CAT/'r37_22.g6').read_text().splitlines(),1):
        a=decode(line);worked=False
        for c in squares(a):
            worked=True;C=sum(1<<v for v in c);outside=[a[v]&~C for v in c];side=[(1<<v)|(1<<c[(i+1)%4]) for i,v in enumerate(c)];family=set()
            for js in product(range(4),repeat=4):
                rows=tuple(side[i]|outside[j] for i,j in enumerate(js));g=a.copy()+[0]*5;g[26]=sum(1<<k for k in range(22,26))
                for i,s in enumerate(rows,22):
                    g[i]=s|(1<<26)
                    for v in range(22):
                        if s>>v&1:g[v]|=1<<i
                if check(g,(1<<27)-1,3,8):family.add(rows)
            assert len(family)==2;mult=Counter()
            for face in sheet:
                local=Counter()
                for start,sgn in product(range(4),(-1,1)):
                    # No sheet-to-graph orientation anchor is supplied. Test every side-preserving binding.
                    bind={r:(start+sgn*i)%4 for i,r in enumerate(face)};rows=[None]*4
                    for k in range(4):
                        i,j,h=[bind[face[(k+b)%4]] for b in (0,1,2)];slot=i if (i+1)%4==j else j
                        rows[slot]=(1<<c[i])|(1<<c[j])|(a[c[h]]&~C)
                    local[tuple(rows)]+=1
                assert set(local)==family and set(local.values())=={4};mult.update(local)
            cases.append(dict(record=rec,square=c,graph_only_rows=sorted(family),sheet_multiplicities=[mult[f] for f in sorted(family)]))
        parents+=worked
    out=dict(sheet_squares=len(sheet),qualifying_parents=parents,graph_squares=len(cases),input_parents=rec,cases=cases);print({k:v for k,v in out.items() if k!='cases'},cases[0]);(D.parent/'ramsey_square_sheet_ablation.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
