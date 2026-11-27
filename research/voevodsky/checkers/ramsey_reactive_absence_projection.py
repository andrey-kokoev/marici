"""Benchmark only: each lower computed resolves true iff no positive response on its side."""
from collections import Counter,defaultdict
from fractions import Fraction
from pathlib import Path
import json
from ramsey_reactive_masked_mirror import tally


def distribution(c):return tuple(sorted((t,Fraction(n,sum(c.values()))) for t,n in c.items()))

def run():
    counts=tally();joint=Counter();out={}
    keep=(6<<7)|126
    for (x,y),n in counts.items():
        # These masks are observations at full resolution, not stored role values.
        r,b=not x,not y
        assert r==(not (x & keep)) and b==(not (y & keep))
        joint[f'{int(r)}{int(b)}']+=n
    for name,reverse in [('red_view',False),('blue_view',True)]:
        full=defaultdict(Counter);small=defaultdict(Counter);mirror_empty=defaultdict(set)
        for (x,y),n in counts.items():
            t=(not x,not y);v=(y if reverse else x);full[v][t]+=n;small[v&keep][t]+=n
        for v,c in full.items():
            assert distribution(c)==distribution(small[v&keep]);i=int(not reverse)
            has_overlap=bool(v & ((6<<7) if reverse else 126));mirror_empty[has_overlap].add(str(Fraction(sum(n for t,n in c.items() if t[i]),sum(c.values()))))
        out[name]=dict(full_views=len(full),reduced_views=len(small),mirror_absence_probability={str(k):sorted(vals) for k,vals in mirror_empty.items()})
    assert joint=={'00':2**21-134,'01':6,'10':126,'11':2};out.update(terminal_counts=joint,or_true=sum(joint[k] for k in ('01','10','11')),assumption='no positive response anywhere on that side; uniform shared gate; one neutral responder on each side');print(out);p=Path(__file__).resolve().parents[1]/'results/ramsey_reactive_absence_projection.json';p.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
