"""For every minimum bisection and every disjoint red-edge pair, classify diagonal placement. Control = pairs sharing one footprint vertex (near-square)."""
import sys,json,subprocess,itertools,collections
from ramsey_retention_slice import CAT,D,decode
P=D.parent;A=[decode(l) for l in (CAT/'r37_22.g6').read_text().splitlines()];audit=json.loads((P/'ramsey_gain22_square_audit.json').read_text())['rows'];ls=subprocess.check_output([sys.argv[1]],input=''.join(' '.join(map(str,a))+'\n' for a in A),text=True).splitlines();out=[];tot=collections.defaultdict(collections.Counter);patterns=collections.Counter()
for row,(a,l) in enumerate(zip(A,ls,strict=True)):
 cost,*ms=map(int,l.split());E=[(1<<i|1<<j,a[i]|a[j]) for i in range(22) for j in range(i) if a[i]>>j&1];rows=[]
 for (e,b),(f,c) in itertools.combinations(E,2):
  h=(b&c).bit_count();
  if h>1 or e&f:continue
  cnt=collections.Counter();
  for m in ms:
   u=(e&m).bit_count();v=(f&m).bit_count();kind=('both_cross' if u==v==1 else 'one_cross' if 1 in (u,v) else 'same_side' if u==v else 'opposite_sides');cnt[kind]+=1
  rows.append(dict(e=e,f=f,h=h,placements=cnt));tot[h].update(cnt)
  if h==0:patterns[tuple(sorted(cnt))]+=1
 assert sum(r['h']==0 for r in rows)==audit[row]['cycles'];out.append(dict(row=row,cost=cost,mincuts=ms,pairs=rows))
print(tot,patterns);(P/'ramsey_bisection_square22.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
