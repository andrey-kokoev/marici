"""Exact 39->40 extension test for the stored witness only. Enumerate maximal blue neighborhoods; keep explicit nine-set witnesses with Hall 6 + 3 extra vertices."""
import csv,json,runpy
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parents[2];base=root/'chatgpt/ramsey';h=runpy.run_path(str(base/'ramsey_cyclic_quotient_constructor.py'));bundles=[b for b in h['B'] if b<=h['outputs'][0]];P=h['P']
rows=[[int(s) for s in row] for row in csv.reader((base/'ramsey_3_10_witness_39.csv').read_text().splitlines()) if row];n=len(rows);assert n==39 and all(len(row)==n for row in rows);full=(1<<n)-1;adj=[sum(x<<i for i,x in enumerate(row)) for row in rows];assert all(x in (0,1) and x==rows[j][i] and (i!=j or not x) and (not x or not(adj[i]&adj[j])) for i,row in enumerate(rows) for j,x in enumerate(row));blue=[full^(a|1<<i) for i,a in enumerate(adj)];maximal=[]
def walk(a,p,x):
 if not(p|x):maximal.append(a);return
 u=((p|x)&-(p|x)).bit_length()-1;c=p&~blue[u]
 while c:
  b=c&-c;c-=b;d=blue[b.bit_length()-1];walk(a|b,p&d,x&d);p^=b;x|=b
walk(0,full,0);assert max(a.bit_count() for a in maximal)==9;ss=sorted(a for a in maximal if a.bit_count()==9);cs=sorted(a for a in maximal if a.bit_count()>=4);remaining=(1<<len(cs))-1;occ=[sum(1<<j for j,a in enumerate(cs) if a>>i&1) for i in range(n)];covers=[]
for s in ss:
 c=remaining
 while s:
  b=s&-s;s-=b;c&=~occ[b.bit_length()-1]
 covers.append(c)
keep=[];pairs=set()
while remaining:
 j=max(range(len(ss)),key=lambda i:(remaining&covers[i]).bit_count());assert remaining&covers[j], 'uncovered candidate';remaining&=~covers[j];v=[i for i in range(n) if ss[j]>>i&1];keep.append(v);tested={(v[P[i][0]],v[P[i][1]]) for b in bundles for i,_ in b}|{(v[i],v[j]) for j in range(6,9) for i in range(j)};assert len(tested)==36 and all(not rows[i][j] for i,j in tested);pairs.update(tested)
D=sum(1<<i for i,a in enumerate(adj) if a.bit_count()==9);out=dict(degrees=dict(Counter(a.bit_count() for a in adj)),maximal_sizes=dict(Counter(a.bit_count() for a in maximal)),tested=len(cs),without_degree9=sum(not(a&D) for a in cs),nines=len(ss),cover_size=len(keep),distinct_pairs=len(pairs),retained=keep);print({k:v for k,v in out.items() if k!='retained'});(root/'voevodsky/results/ramsey310_hall_extension_cover.json').write_text(json.dumps(out,indent=1)+'\n')
