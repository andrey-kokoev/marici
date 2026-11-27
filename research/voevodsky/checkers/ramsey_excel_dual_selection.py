"""Candidate source reading: one width-seven column is a state on ten row labels."""
from itertools import combinations
from pathlib import Path
import json

rows=[s for s in combinations(range(1,8),3) if min(s[1]-s[0],s[2]-s[1])>=2]
assert len(rows)==10
out=[]
for polarity in [1,-1]:
    for j in range(1,8):
        red=[polarity*(1 if j in s else -1) for s in rows];blue=[-x for x in red]
        # Optimize each computed on its own pool; overlap is allowed.
        r=max(min(t) for t in combinations(red,3));b=min(max(t) for t in combinations(blue,7));n=red.count(1)
        assert (r>=0,b<=0)==(n>=3,n>=7)
        out.append(dict(column=j,R_value=polarity,favorable=n,best_red_min=r,best_blue_max=b,no_red_minus=r>=0,no_blue_plus=b<=0,final=(r>=0 or b<=0)))
print([(z['column'],z['favorable'],z['no_red_minus'],z['no_blue_plus']) for z in out[:7]])
p=Path(__file__).resolve().parents[1]/'results/ramsey_excel_dual_selection.json';p.write_text(json.dumps(dict(scope='candidate only: labeled row positions, column sign, exact pointwise sign dual, independently selectable subsets',rows=rows,states=out),indent=2)+'\n')
