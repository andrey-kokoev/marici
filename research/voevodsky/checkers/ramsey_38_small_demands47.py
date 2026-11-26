"""Enumerate every seven-support multiset passing (5,6), then filter jointly by smaller cliques. Maximal independent supports suffice by monotonicity. Count labeled multisets, not orderings."""
import json,itertools,collections,sys
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results'
def audit(h):
 a=[0]*20
 for k,(i,j) in enumerate((i,j) for j in range(20) for i in range(j)):
  if int(h,16)>>k&1:a[i]|=1<<j;a[j]|=1<<i
 I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q={n:[q for q in I if q.bit_count()==n] for n in range(1,7)};M={n:[sum(1<<j for j,q in enumerate(qs) if not q&s) for s in S] for n,qs in Q.items()};adj=[sum(1<<j for j in range(i,len(S)) if not x&M[6][j]) for i,x in enumerate(M[6])];counts={n:0 for n in range(1,6)};conflicts=[];examples={}
 def visit(p,c,once,twice):
  if len(p)==7:
   counts[5]+=1
   for n in range(4,0,-1):
    b=[-1]+[0]*(8-n)
    for j in p:
     for t in range(8-n,0,-1):b[t]|=b[t-1]&M[n][j]
    if b[-1]:conflicts.append((n,b[-1]));break
    counts[n]+=1;examples[n]=[S[j] for j in p]
   return
  while c:
   bit=c&-c;c^=bit;j=bit.bit_length()-1;m=M[5][j]
   if not twice&m:visit(p+[j],(c|bit)&adj[j],once|m,twice|(once&m))
 visit([],2**len(S)-1,0,0)
 # Greedily select explicit extra demands hitting every recorded failure. Not claimed minimum.
 cuts=[];remaining=conflicts.copy()
 while remaining:
  n,_=remaining[0];q=max(range(len(Q[n])),key=lambda j:sum((bits>>j)&1 for level,bits in remaining if level==n));cuts.append(Q[n][q]);remaining=[(level,bits) for level,bits in remaining if level!=n or not(bits>>q&1)]
 assert len(conflicts)+counts[1]==counts[5];return dict(core=h,counts=counts,extra_demands=cuts,examples=examples)
if '--d3' in sys.argv:
 rows=json.loads((P/'ramsey_38_degree3_inventory_0_38_47.json').read_text())['resistant'];ids=json.loads((P/'ramsey_38_d3_resistant47_sixes.json').read_text())['surviving_row_indices'];out=[]
 for i in ids:
  a=rows[i];h=hex(sum(1<<k for k,(u,v) in enumerate((u,v) for v in range(20) for u in range(v)) if a[u]>>v&1));out.append(dict(row=i,**audit(h)))
 print('survivors by floor',[(n,sum(r['counts'][n]>0 for r in out)) for n in range(5,0,-1)]);print('cuts',collections.Counter(len(r['extra_demands']) for r in out));(P/'ramsey_38_d3_resistant47_small.json').write_text(json.dumps(out)+'\n');sys.exit()
rows=[json.loads(f.read_text()) for f in sorted(P.glob('ramsey_38_integer47_0x*.json'))];rows=[r for r in rows if r['joint']['example']];assert len(rows)==5;out=[audit(r['core']) for r in rows];print([(r['counts'],len(r['extra_demands'])) for r in out]);(P/'ramsey_38_small_demands47.json').write_text(json.dumps(out)+'\n')
