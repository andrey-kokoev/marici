"""Determine maximum host order in the constant-stride 13-interval circulant model without using R(3,9). For n>=25 the four forced distances give eight distinct plus neighbors. Any extra distance violates triangle-freeness or yields nine independent neighbors. Finite tail certificate: a line-independent nine-set of span L remains independent for all n>L+max(D)."""
from itertools import combinations
from pathlib import Path
import json
H=Path(__file__).resolve().parents[1]
def independent9(N):
    def rec(av,k):
        if not k:return []
        while av.bit_count()>=k:
            v=av&-av;av-=v;i=v.bit_length()-1;tail=rec(av&~N[i],k-1)
            if tail is not None:return [i,*tail]
        return None
    return rec((1<<len(N))-1,9)

def run():
    out=[]
    for ds in sorted({tuple(d for d in range(1,13) if a*d%13 in (1,5,8,12)) for a in range(1,7)}):
        # Finite termination: multiples of max(ds)+1 always work on the line.
        for L in range(8,8*(max(ds)+1)+1):
            w=independent9([sum(1<<j for j in range(L+1) if abs(i-j) in ds) for i in range(L+1)])
            if w is not None:break
        assert w is not None and max(w)==L and all(b-a not in ds for a,b in combinations(w,2));tail_from=L+max(ds)+1;checks={};passing=[]
        for n in range(25,tail_from):
            S=set(ds)|{n-d for d in ds};assert len(S)==8
            N=[sum(1<<((i+s)%n) for s in S) for i in range(n)];t=next(([0,a,b] for a,b in combinations(sorted(S),2) if b-a in S),None)
            if t:checks[n]={'plus3':t};continue
            z=independent9(N)
            if z is not None:assert all((b-a) not in S for a,b in combinations(z,2));checks[n]={'minus9':z}
            else:checks[n]='admissible';passing.append(n)
        out.append(dict(distances=ds,passing_orders_ge25=passing,finite_checks=checks,tail_minus9=w,tail_from=tail_from))
    largest=max(n for r in out for n in r['passing_orders_ge25']);assert largest==35;return dict(min_tested=25,maximum=largest,classes=out)
if __name__=='__main__':
    res=run();print([(r['distances'],r['passing_orders_ge25'],r['tail_from'],r['tail_minus9']) for r in res['classes']]);(H/'results/ramsey_39_interval_order_ceiling.json').write_text(json.dumps(res,indent=2)+'\n')
