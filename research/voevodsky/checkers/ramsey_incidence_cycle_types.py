"""Census for specified cycle types of a SINGLE label permutation; no transitivity or red-core symmetry. Complete multiset enumeration by orbit multiplicity and per-cycle marginals. Compare up to arbitrary relabeling. Output keeps explicit masks, gate reason and solver witness/status. Covers any cycle of length >=5 via the 5-cycle power for partitions 5+3 and 5+2+1."""
import sys,json,itertools,functools,collections,subprocess,igraph as ig
from ramsey_incidence_first35 import solve,P
classes={};stats={}
def key(m):
 g=ig.Graph(34,[(i,26+j) for i,s in enumerate(m) for j in range(8) if s>>j&1]);p=g.canonical_permutation(color=[1]*26+[2]*8);return tuple(sorted(tuple(sorted(e)) for e in g.permute_vertices(p).get_edgelist()))
for text in sys.argv[2:]:
 cycles=list(map(int,text));assert sum(cycles)==8;starts=list(itertools.accumulate([0]+cycles))[:-1];p=[s+(j+1)%n for s,n in zip(starts,cycles) for j in range(n)];O=set()
 for s in range(1,256):
  if s.bit_count()>5:continue
  o=set()
  while s not in o:o.add(s);s=sum(1<<v for i,v in enumerate(p) if s>>i&1)
  O.add(tuple(sorted(o)))
 O=sorted(O,key=lambda o:(-len(o),min(o)));cols=[(len(o),o[0].bit_count(),[sum(s>>v&1 for s in o) for v in starts]) for o in O]
 @functools.cache
 def ways(i,n,d):
  if min(d)<0 or n<0 or not n<=sum(k*j for k,j in zip(cycles,d))<=5*n:return 0
  if i==len(O):return int(n==0 and not any(d))
  l,k,h=cols[i];return sum(ways(i+1,n-j*l,tuple(x-j*y for x,y in zip(d,h))) for j in range(k+1))
 raw=ways(0,26,(7,)*len(starts));types=set();print(text,'raw',raw,flush=True)
 def gen(i,n,d,m):
  if i==len(O):
   assert len(m)==26 and all(sum(s>>j&1 for s in m)==7 for j in range(8));h=key(m);types.add(h);cl=classes.setdefault(h,dict(m=m,cycles=[]));
   if text not in cl['cycles']:cl['cycles'].append(text)
   return
  l,k,h=cols[i];
  for j in range(k+1):
   D=tuple(x-j*y for x,y in zip(d,h));N=n-j*l
   if ways(i+1,N,D):gen(i+1,N,D,m+list(O[i])*j)
 if raw:gen(0,26,(7,)*len(starts),[])
 stats[text]=dict(raw=raw,types=len(types));ways.cache_clear()
rs=list(classes.values());out=[];path=P/('ramsey_incidence_cycles_'+'_'.join(sys.argv[2:])+'.json');
for off in range(0,len(rs),256):
 chunk=rs[off:off+256];gs=subprocess.check_output([sys.argv[1],'8'],input=''.join(' '.join(map(str,r['m']))+'\n' for r in chunk),text=True).splitlines()
 for r,s in zip(chunk,gs,strict=True):
  r['gate'],r['rounds']=map(int,s.split())
  if r['gate']==0:r['solve']=solve(r['m'],False)
  out.append(r)
 path.write_text(json.dumps(dict(stats=stats,rows=out),separators=(',',':'))+'\n')
print(stats,len(rs),collections.Counter(r.get('solve',{}).get('status','gate') for r in rs))
