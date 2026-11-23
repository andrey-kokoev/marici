"""Two 13-cycles normalized to unit step; common origin/reflection; enumerate all symmetric cross offsets. No prior successful D required. Classify by exact largest independent set."""
import json,itertools,collections
from pathlib import Path
n=13;U=set(range(n));X=[set(x) for k in range(7) for x in itertools.combinations(range(n),k) if all((v+1)%n not in x for v in x)]
def alpha(s):
 if len(s)==n:return n//2
 j=next(iter(U-s));return sum((len(list(g))+1)//2 for val,g in itertools.groupby((j+i)%n in s for i in range(1,n+1)) if val)
rows=[]
for bits in itertools.product((0,1),repeat=7):
 D={v for i,b in enumerate(bits) if b for v in (i,-i%n)}
 if any((v+1)%n in D for v in D):continue
 best={k:max(alpha(U-{(v+d)%n for v in x for d in D}) for x in X if len(x)==k) for k in range(7)};rows.append(dict(D=sorted(D),best=best,alpha=max(k+a for k,a in best.items())))
out=dict(triangleFree=len(rows),success=[r for r in rows if r['alpha']<8]);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_38_cycle_cross_offsets.json').write_text(json.dumps(out,indent=2)+'\n')
