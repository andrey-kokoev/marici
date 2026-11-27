"""Resolve what the overlap projection loses under the fixed masked-mirror measure."""
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd
import json
from pathlib import Path
from ramsey_reactive_masked_mirror import tally


def inspect(dist,extra):
    by=defaultdict(Counter);boxes=defaultdict(list)
    for (x,y),w in dist.items():by[x][y]=w
    def law(c):
        g=gcd(*c.values());return tuple(sorted((y,v//g) for y,v in c.items()))
    for x in by:boxes[x & ~extra].append(x)
    stats=Counter();examples=[];patterns=Counter()
    for k,xs in boxes.items():
        if len(xs)==1:stats['bit_forced']+=1;continue
        a,b=sorted(xs);assert b==a+extra
        u,v=by[a],by[b];different=law(u)!=law(v);stats['different' if different else 'equal']+=1
        names=(k>>7).bit_count() if extra==1 else (k&127).bit_count()
        assert different==(names>=2)
        patterns[(bool(different),(k>>7).bit_count(),(k&127).bit_count())]+=1
        if not different:continue
        # Look for a single named role whose mirror membership changes probability.
        for role in range(10):
            pr=lambda c:Fraction(sum(n for y,n in c.items() if y>>role&1),sum(c.values()))
            if pr(u)!=pr(v):
                examples.append((k.bit_count(),k,role,str(pr(u)),str(pr(v)),set(u)==set(v)));break
    return dict(counts=dict(stats),possible_full=len(by),overlap_keys=len(boxes),smallest_example=min(examples) if examples else None,by_size={'/'.join(map(str,k)):v for k,v in sorted(patterns.items())})


def run():
    # Two fully specified terminal relations (one-based row,column); role 1 is N as responder on each side.
    A={(2,2),(3,2)};B={(2,1),(3,2)}
    def footprints(es):
        def code(links):return sum(1<<(6+i) for i in {i for i,j in links}) | sum(1<<(j-1) for j in {j for i,j in links})
        return code([(i,j) for i,j in es if i!=1]),code([(i,j) for i,j in es if j!=1])
    (x,y),(xx,yy)=map(footprints,(A,B));assert x==770 and xx==771 and y&(1<<8) and not yy&(1<<8)
    j=tally();out={name:inspect(dist,extra) for name,dist,extra in [('red_to_blue',j,1),('blue_to_red',{(y,x):n for (x,y),n in j.items()},1<<7)]};print(out);p=Path(__file__).resolve().parents[1]/'results/ramsey_reactive_neutral_residue.json';p.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
