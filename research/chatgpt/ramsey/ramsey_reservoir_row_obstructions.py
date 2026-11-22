"""Fixed matched leftover R. Project old sixes onto V-R: forbid monochrome traces. Exact minimum witness family covering all candidate balanced colourings, and test whether unary/binary traces alone suffice."""
from ramsey_inverse_five_motifs import D,json,graph,inds,bits,combinations,Counter
from functools import lru_cache

def audit(H,items):
    I=inds(H);T=[s for s in I if s.bit_count()==6];P=[s for s in I if s.bit_count()==5];out=[];F=(1<<len(H))-1
    for d in items:
        R=d['R'];E=[1<<a|1<<b for a,b in combinations(bits(R),2) if H[a]>>b&1];
        if not any((a|b|c).bit_count()==6 for a,b,c in combinations(E,3)):continue
        V=F^R;pool={s for s in P if not s&R};part=[(s,t,V^s^t) for s,t in combinations(sorted(pool),2) if not s&t and V^s^t>t and V^s^t in pool];full=(1<<len(part))-1;traces=sorted({t&V for t in T},key=int.bit_count);ms={};sh=[0]*7
        for tr in traces:
            if tr.bit_count()>5:continue
            mask=sum(1<<i for i,p in enumerate(part) if any(not tr&~s for s in p));sh[tr.bit_count()]|=mask
            if mask:ms.setdefault(mask,tr)
        union=0;arity=None
        for size,m in enumerate(sh):
            union|=m
            if union==full and arity is None:arity=size
        assert (union!=full)==(d['depth']==8);cover=None
        if union==full:
            maximal=[m for m in ms if not any(m!=n and not m&~n for n in ms)];
            @lru_cache(None)
            def choose(left):
                if not left:return ()
                pivot=left&-left;return min(((ms[m],)+choose(left&~m) for m in maximal if m&pivot),key=len)
            cover=choose(full)
        out.append(dict(R=R,partitions=len(part),arity=arity,cover=cover))
    return out
if __name__=='__main__':
    ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();z=json.loads((D/'ramsey_residual_hall.json').read_text());out={i:audit(graph(ls[int(i)-1]),r['details']) for i,r in z.items()};r=sum(out.values(),[]);print(Counter(x['arity'] for x in r),Counter(len(x['cover']) if x['cover'] is not None else None for x in r));(D/'ramsey_reservoir_row_obstructions.json').write_text(json.dumps(out)+'\n')
