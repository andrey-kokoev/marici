"""Complete shell of one bipartite degree-preserving switch around six near-miss assignments. Do NOT enforce label pairing or red completion symmetry. Dedup by colored incidence graph canonical labeling. Four-label gate then SAT on survivors; resolve progressively larger label scopes."""
import itertools,json,sys,subprocess,collections,igraph as ig
from ramsey_incidence_first35 import P,solve
R=json.loads((P/'ramsey_incidence_mismatch.json').read_text());pool={};raw=0
def key(m):
 g=ig.Graph(34,[(i,26+j) for i,s in enumerate(m) for j in range(8) if s>>j&1]);p=g.canonical_permutation(color=[1]*26+[2]*8);return tuple(sorted(tuple(sorted(e)) for e in g.permute_vertices(p).get_edgelist()))
mode=sys.argv[2] if len(sys.argv)>2 else 'switch'
for ix,r in enumerate(R):
 m=r['m'];
 if mode=='transfer':
  for i,j in itertools.permutations(range(26),2):
   if m[i].bit_count()<2 or m[j].bit_count()>=7:continue
   for l in range(8):
    if not (m[i]&~m[j])>>l&1:continue
    n=m[:];n[i]^=1<<l;n[j]^=1<<l;raw+=1;k=key(n);pool.setdefault(k,dict(parent=ix,trade=[i,j,l],m=n))
  continue
 for i,j in itertools.combinations(range(26),2):
  for a in range(8):
   if not (m[i]&~m[j])>>a&1:continue
   for b in range(8):
    if not (m[j]&~m[i])>>b&1:continue
    flip=1<<a|1<<b;n=m[:];n[i]^=flip;n[j]^=flip;raw+=1;k=key(n);pool.setdefault(k,dict(parent=ix,trade=[i,j,a,b],m=n))
rs=list(pool.values());lines=lambda rs:''.join(' '.join(map(str,r['m']))+'\n' for r in rs);gates=list(map(lambda l:int(l.split()[0]),subprocess.check_output([sys.argv[1],'4'],input=lines(rs),text=True).splitlines()));assert len(gates)==len(rs)
for z,s in zip(rs,gates):
 z['gate4']=s
 if s:continue
 z['sat4']=solve(z['m'],False,True,4,False)['status'];
 if z['sat4']=='sat_local':
  for h in [5,6]:
   z[f'sat{h}']=solve(z['m'],False,True,h,False)['status'];
   if z[f'sat{h}']!='sat_local':break
  if z.get('sat6')=='sat_local':z['full']=solve(z['m'],False)
print('raw',raw,'types',len(rs),'gate4',gates.count(0),'sat4',collections.Counter(z.get('sat4') for z in rs if z['gate4']==0),'sat5',collections.Counter(z['sat5'] for z in rs if 'sat5' in z),'sat6',collections.Counter(z['sat6'] for z in rs if 'sat6' in z));(P/('ramsey_incidence_trade35.json' if mode=='switch' else 'ramsey_incidence_transfer35.json')).write_text(json.dumps(dict(raw=raw,records=rs),separators=(',',':'))+'\n')
