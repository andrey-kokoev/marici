"""Hostile controls for exact certification by individual pair-color queries on an unrestricted marked header/rim. Toggle each nonrim chord of an otherwise monochromatic clique. No assumption about unqueried reads through aggregate observables."""
import itertools,json
from ramsey_retention_slice import D,check
out=[]
for n in range(5,13):
 p=(1<<n)-1;full=[p^(1<<i) for i in range(n)];rim=list(range(1,n));cycle={tuple(sorted((v,rim[(j+1)%len(rim)]))) for j,v in enumerate(rim)};chords=sorted(set(itertools.combinations(rim,2))-cycle);assert not check(full,p,n,3)
 for i,j in chords:
  a=full.copy();a[i]^=1<<j;a[j]^=1<<i;assert check(a,p,n,3) and not check(full,p,n,3);assert check([p^(v|1<<h) for h,v in enumerate(a)],p,3,n)
 out.append(dict(target=n,chords=len(chords),examples=chords));assert len(chords)==(n-1)*(n-4)//2
print([(r['target'],r['chords']) for r in out]);(D.parent/'ramsey_header_chord_lower_bound.json').write_text(json.dumps(out,indent=1)+'\n')
