"""Source feasibility: compare two actual rows on the same ordered column or prefix.
Differences describe two readings, not updates. No sign mask, graph or N binding.
"""
from itertools import combinations, accumulate
from collections import Counter
import json
from pathlib import Path


def read_pair(a,b):
    def counts(row,red):return [int((i in row)==red) for i in range(1,8)]
    def channel(red):return [x-y for x,y in zip(counts(a,red),counts(b,red))]
    r,bv=channel(True),channel(False);out={}
    for name,x,y in [('column',r,bv),('prefix',list(accumulate(r)),list(accumulate(bv)))]:
        assert all(p==-q for p,q in zip(x,y));out[name]=dict(red=x,blue=y,no_red_minus=min(x)>=0,no_blue_plus=max(y)<=0)
    return out


def run():
    rows=[s for s in combinations(range(1,8),3) if min(s[1]-s[0],s[2]-s[1])>=2];stats=Counter();example=None
    for a,b in combinations(rows,2):
        z=read_pair(a,b);stats['pairs']+=1
        for c in z.values():assert c['no_red_minus']==c['no_blue_plus']
        if sum(abs(p-q) for p,q in zip(a,b))!=1:continue
        stats['swaps']+=1;assert z['prefix']['red'].count(1)==1 and z['prefix']['red'].count(0)==6 and not z['column']['no_red_minus'] and z['prefix']['no_red_minus'];rev=read_pair(b,a);assert rev['prefix']['red']==[-v for v in z['prefix']['red']]
        if example is None:example=dict(a=a,b=b,readings=z)
    out=dict(scope='Column and left-prefix signed contrasts, lexicographically earlier row minus later row; absence values only conditional candidate interpretations.',counts=stats,example=example);print(out);p=Path(__file__).resolve().parents[1]/'results/ramsey_excel_signed_cut.json';p.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
