"""Exact defect on a reproducible edge-stratified subset, not a catalogue-wide minimum. For each edge count choose 16 evenly spaced catalogue indices within the stratum (all if smaller)."""
from pathlib import Path
from collections import defaultdict
import gzip,json
base=Path(__file__).resolve().parents[2];p=base/'chatgpt/ramsey/pauli-realization-catalogues/r38_27.g6.gz'
rows=gzip.decompress(p.read_bytes()).splitlines();groups=defaultdict(list)
for i,b in enumerate(rows):groups[sum((c-63).bit_count() for c in b[1:])].append(i)
out=[]
for m,inds in sorted(groups.items()):
 for idx in sorted({inds[t*(len(inds)-1)//15] for t in range(16)}):
    b=rows[idx];adj=[0]*27;k=0
    for j in range(27):
        for i in range(j):
            if (b[1+k//6]-63)>>(5-k%6)&1:adj[i]|=1<<j;adj[j]|=1<<i
            k+=1
    sevens=[];leaves=[]
    def walk(a,c):
        if not c:
            leaves.append(a)
            if a.bit_count()==7:sevens.append(a)
            assert a.bit_count()<=7
        while c:
            v=c&-c;c-=v;walk(a|v,c&~adj[v.bit_length()-1])
    walk(0,(1<<27)-1)
    # Every maximal independent set is a leaf; nonmaximal leaves cannot improve the optimum.
    avoid=[sum(1<<j for j,s in enumerate(sevens) if not s>>i&1) for i in range(27)]
    def defect(a):
        h=(1<<len(sevens))-1
        while a:
            v=a&-a;a-=v;h&=avoid[v.bit_length()-1]
        return h.bit_count()
    d,a=min((defect(a),a) for a in leaves);out.append(dict(edges=m,record=idx+1,defect=d,neighbors=[i for i in range(27) if a>>i&1],sevens=len(sevens)))
 print(m,len(inds),min(x['defect'] for x in out if x['edges']==m),max(x['defect'] for x in out if x['edges']==m))
print(len(out),min(out,key=lambda x:x['defect']));(base/'voevodsky/results/ramsey38_stratified_defect.json').write_text(json.dumps(out,indent=1)+'\n')
