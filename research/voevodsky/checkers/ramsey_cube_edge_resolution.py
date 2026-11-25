"""Compare equal-tail simplification with general edge resolution, and verify all closures against exact legal supports."""
from itertools import combinations,product
from functools import lru_cache
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
def absorb(C):return tuple(sorted(x for x in set(C) if not any(y!=x and y&x==y for y in C)))
def run(E,prior):
 edges=[(1<<(i-1),1<<(j-1)) for i,j in E];I=[m for m in range(256) if not any(m&x and m&y for x,y in edges)];corners=[sum(1<<(v-1) for v in c) for c in product((1,2),(4,5),(7,8))]
 @lru_cache(None)
 def close(raw,general):
    C=raw
    while True:
        derived=set(C)
        for a,b in combinations(C,2):
            for x,y in edges:
                for l,r in ((x,y),(y,x)):
                    if a&l and b&r and (general or a^l==b^r):derived.add((a^l)|(b^r))
        nxt=absorb(derived)
        if nxt==C:return C
        C=nxt
 stats=[0,0,0];gaps=[];tested=0
 for row in prior['rows']:
    T=row['T'];rows=[]
    for s in corners:
        b=[x for x in I if x.bit_count()==4 and not x&s];raw=(0,) if any(not x&T for x in b) else absorb(b+[x for x in I if x.bit_count()==4 and not x&T or x.bit_count()==3 and not x&(s|T)]);sig=[u for u in I if all(u&x for x in raw)];small=close(raw,False);full=close(raw,True)
        # On arbitrary masks the saturated list must recognize precisely the upward closure of the legal supports.
        assert all(all(m&x for x in full)==any(u&m==u for u in sig) for m in range(256));rows.append((raw,small,full,sig))
    for i,j in combinations(range(8),2):
        tested+=1;a,b=rows[i],rows[j];equal=a[3]==b[3];assert equal==(a[2]==b[2]);
        for z in range(3):stats[z]+=equal and a[z]!=b[z]
        if equal and a[1]!=b[1]:gaps.append(dict(T=T,corners=[i,j],small=[a[1],b[1]],general=a[2]))
 return dict(comparisons=tested,missed_raw_small_full=stats,residual_gaps=gaps)
if __name__=='__main__':
 prior=json.loads((D/'ramsey_cube_conditional_folds.json').read_text());cores=json.loads((D/'ramsey_cube_exterior_test.json').read_text());out={k:run(cores[k]['edges'],v) for k,v in prior.items()};print(out);(D/'ramsey_cube_edge_resolution.json').write_text(json.dumps(out,indent=1))
