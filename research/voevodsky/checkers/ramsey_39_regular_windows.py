"""No assumed host symmetry or prescribed 13-core: each cyclic consecutive window of 13 induces a 4-regular plus graph. Exact upper ceiling for (3,9) under this condition. See accompanying proof."""
from itertools import combinations
from pathlib import Path
from math import gcd
import json
from ramsey_39_interval_order_ceiling import independent9
D=Path(__file__).resolve().parents[1]/'results'
def main():
    rows=[];passes=[]
    # Coprime case: all short edges translation-invariant, long edges forced minus.
    for a,b in combinations(range(1,7),2):
        ds={a,b,13-a,13-b};m=max(ds)
        # A fixed line obstruction beyond a finite bound. Multiples of m+1 suffice as fallback.
        for L in range(8,8*(m+1)+1):
            w=independent9([sum(1<<j for j in range(L+1) if abs(i-j) in ds) for i in range(L+1)])
            if w is not None:break
        assert w is not None and all(j-i not in ds for i,j in combinations(w,2));tail=L+m+1;finite={}
        for n in range(25,tail):
            if gcd(n,13)!=1:continue
            S=ds|{n-x for x in ds};assert len(S)==8
            plus=lambda i,j:(j-i)%n in S
            N=[sum(1<<j for j in range(n) if plus(i,j)) for i in range(n)];tri=next(([0,i,j] for i,j in combinations(sorted(S),2) if plus(i,j)),None)
            if tri:finite[n]=dict(plus3=tri);continue
            z=independent9(N)
            if z is None:passes.append((n,sorted(ds)));finite[n]='legal'
            else:assert all(not plus(i,j) for i,j in combinations(z,2));finite[n]=dict(minus9=z)
        rows.append(dict(distances=sorted(ds),finite=finite,tail_from=tail,line_witness=w))
    assert max(n for n,_ in passes)==35
    out=dict(window_size=13,window_degree=4,coprime_patterns=len(rows),at_35=[s for n,s in passes if n==35],coprime_max=35,cases=rows);print(len(rows),out['at_35']);(D/'ramsey_39_regular_windows.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
