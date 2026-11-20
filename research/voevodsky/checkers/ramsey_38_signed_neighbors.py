"""Delete each edge of first catalogued K27 witness; compare exact SQL blocker masks to direct subset incidence."""
from pathlib import Path
from itertools import combinations
from collections import Counter,defaultdict
import gzip,json,sqlite3
H=Path(__file__).resolve().parents[1];src=H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r38_27.g6.gz';g=gzip.open(src,'rt').readline().strip();n=ord(g[0])-63;assert n==27;bits=''.join(f'{ord(c)-63:06b}' for c in g[1:]);edge={(i,j):int(bits[j*(j-1)//2+i]) for j in range(n) for i in range(j)};V=range(n);u=(1<<n)-1
# Direct rule enumeration. Only subsets one edge short of a violation can block a change.
ref=defaultdict(set)
for k,sign,exception in [(3,'+',0),(8,'-',1)]:
    for subset in combinations(V,k):
        bad=None
        for pair in combinations(subset,2):
            if edge[pair]==exception:
                if bad is not None:break
                bad=pair
        else:
            assert bad is not None,'invalid starting coloring';ref[bad].add((sign,sum(1<<v for v in subset)))
p=[sum(1<<w for w in V if w!=v and edge[tuple(sorted((v,w)))]) for v in V];m=[u^(1<<v)^p[v] for v in V];db=sqlite3.connect(':memory:');db.execute('create table nb(v integer primary key,plus integer,minus integer)');db.executemany('insert into nb values(?,?,?)',zip(V,p,m));sql=(H/'sql/ramsey_38_signed_neighbors.sql').read_text();counts=Counter();example={}
for (a,b),original in edge.items():
    for v,w in ((a,b),(b,a)):db.execute('update nb set plus=?,minus=? where v=?',(p[v]&~(1<<w),m[v]&~(1<<w),v))
    got=set(db.execute(sql,dict(a=a,b=b)));assert got==ref[a,b];label=next(iter(got))[0] if got else 'neither';counts[label]+=1
    if got and label not in example:example[label]=dict(edge=[a,b],subset=[i for i in V if min(mask for _,mask in got)>>i&1])
    for v in (a,b):db.execute('update nb set plus=?,minus=? where v=?',(p[v],m[v],v))
out=dict(catalogue=src.name,graph_index=0,compared_edges=len(edge),blocked_sign=counts,examples=example);print(json.dumps(out));(H/'results/ramsey_38_signed_neighbors.json').write_text(json.dumps(out,indent=2)+'\n')
