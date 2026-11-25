"""Same edge-stratified sample as ramsey38_stratified_defect. Cover maximal neighborhoods (which dominate all their subsets). Hall lift on six of seven, plus six spokes. Report reusable pair tests."""
from pathlib import Path
import gzip,json,runpy
from collections import Counter
root=Path(__file__).resolve().parents[2];base=root/'chatgpt/ramsey';res=root/'voevodsky/results';h=runpy.run_path(str(base/'ramsey_cyclic_quotient_constructor.py'));P=h['P'];bundles=[b for b in h['B'] if b<=h['outputs'][0]];assert len(bundles)==3
rows=gzip.decompress((base/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();out=[]
for sample in json.loads((res/'ramsey38_stratified_defect.json').read_text()):
 idx=sample['record'];row=rows[idx-1];adj=[0]*27;k=0
 for j in range(27):
  for i in range(j):
   if ((row[1+k//6]-63)>>(5-k%6))&1:adj[i]|=1<<j;adj[j]|=1<<i
   k+=1
 sets=[];ss=[]
 def walk(a,c,eligible):
  if not eligible:
   if a.bit_count()>=5:sets.append(a)
   if a.bit_count()==7:ss.append(a)
  while c:
   b=c&-c;c-=b;allow=~(adj[b.bit_length()-1]|b);walk(a|b,c&allow,eligible&allow)
 walk(0,(1<<27)-1,(1<<27)-1);assert len(ss)==sample['sevens'];full=(1<<len(sets))-1;contains=[sum(1<<j for j,a in enumerate(sets) if a>>i&1) for i in range(27)];covers=[]
 for s in ss:
  bits=full
  while s:
   b=s&-s;s-=b;bits&=~contains[b.bit_length()-1]
  covers.append(bits)
 left=full;keep=[];pairs=set()
 while left:
  j=max(range(len(ss)),key=lambda j:(left&covers[j]).bit_count());assert left&covers[j];left&=~covers[j];v=[i for i in range(27) if ss[j]>>i&1];keep.append(v);checks={(v[P[i][0]],v[P[i][1]]) for b in bundles for i,_ in b}|{(i,v[-1]) for i in v[:-1]};assert len(checks)==21 and all(not(adj[i]>>j&1) for i,j in checks);pairs.update(checks)
 out.append(dict(record=idx,maximal=len(sets),keep=keep,distinct_pairs=len(pairs)))
(res/'ramsey38_hall_extension_cover.json').write_text(json.dumps(out)+'\n');print('records',len(out),'maximal',sum(x['maximal'] for x in out),'sizes',sorted(Counter(len(x['keep']) for x in out).items()),'total pair occurrences',sum(21*len(x['keep']) for x in out),'distinct per parent summed',sum(x['distinct_pairs'] for x in out))
