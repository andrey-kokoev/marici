"""Conditional model: 10 aligned positions, disjoint 3/7 choices, Boolean suitability."""
from collections import Counter
from itertools import combinations
from math import comb
import json
from pathlib import Path

FULL=(1<<10)-1
cuts=[sum(1<<i for i in s) for s in combinations(range(10),3)]

def direct(r,b):
    pairs=[(s&r==s,(FULL^s)&b==(FULL^s)) for s in cuts]
    return any(x for x,y in pairs),any(y for x,y in pairs),any(x and y for x,y in pairs),any(x or y for x,y in pairs)

def run():
    counts=Counter();classes=0
    # Counts of positions suitable for neither, red only, blue only, and both.
    for n in range(11):
        for a in range(11-n):
            for c in range(11-n-a):
                d=10-n-a-c;r=((1<<a)-1)<<n | ((1<<d)-1)<<(10-d);b=((1<<(c+d))-1)<<(n+a)
                x,y,j,o=direct(r,b);assert (x,y,j,o)==(a+d>=3,c+d>=7,a+d>=3 and c+d>=7 and n==0,x or y)
                count=comb(10,n)*comb(10-n,a)*comb(10-n-a,c);counts[f'{int(x)}{int(y)}{int(j)}']+=count;classes+=1
    assert sum(counts.values())==2**20
    example=direct(7,127);assert example==(True,True,False,True)
    out=dict(scope='hypothetical complementary split and Boolean suitability, not an Excel decoder',cut_count=len(cuts),role_count_classes=classes,states_by_red_blue_joint=dict(counts),example=dict(red_suitable=[1,2,3],blue_suitable=list(range(1,8)),red=True,blue=True,joint=False,disjunction=True));p=Path(__file__).resolve().parents[1]/'results/ramsey_ten_role_comparison.json';p.write_text(json.dumps(out,indent=2)+'\n');print(out)

if __name__=='__main__':run()
