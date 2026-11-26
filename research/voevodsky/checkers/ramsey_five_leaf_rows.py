"""Any five neighbors of a vertex of the pair graph give five mutually blue singleton vertices (a pair mask forces its singleton endpoints red). No additional cell has a mask wholly among these five: that cell plus its singleton labels would violate the clique-union bound. There are exactly 18 nonsingleton cells and exactly 18 incidences on the complementary three labels. Thus every nonsingleton carries EXACTLY ONE of those three labels, splitting the construction into three 6-cell rows. Six blue singletons are already impossible by counting. At degree five each remaining triple is determined by its row and two of the five leaves. Generate row multisets independently, test each partially, then join exact leaf totals before full-core SAT. Unknowns retained."""
from ramsey_exception_first import *
from ramsey_unsaturated_skeleton_budget import budget
from ramsey_unsaturated_archive_ladder import run
from ramsey_unsaturated_pair_graphs import cap
from functools import reduce
bits=lambda s:[1<<j for j in V if s>>j&1];code=lambda s:sum(16**j for j in V if s>>j&1);codeall=code(255)
def solve(t):
 i,e,q=t;g=ig.Graph(8,e);f=fixed(e)+q;deg=g.degree();c=deg.index(max(deg));leaves=sum(1<<j for j in g.neighbors(c));outside=bits(255^leaves);base=dict(i=i,q=q)
 if len(outside)<3 or any((s&~leaves).bit_count()!=1 for s in f if s.bit_count()>1):return dict(**base,status='transversal')
 G=[p for p in sym(e) if p[leaves]==leaves and tuple(sorted(p[x] for x in q))==q];pools=[];checks={};unknown=0;stats=[];demand=7*codeall-sum(code(s) for s in f)
 for l in outside:
  R=[s for s in f if s&l];n=7-len(R);pool=[];raw=0
  if n<0:return dict(**base,status='quota')
  for u in itertools.combinations_with_replacement([l+x+y for x,y in itertools.combinations(bits(leaves),2)],n):
   # Sort to agree with canonical keys in row exchange tests.
   u=tuple(sorted(u));m=f+u;row=R+list(u)
   if any(sum(not x&~mask for x in row)>mask.bit_count() for mask in set(reduce(int.__or__,subset,0) for k in range(1,8) for subset in itertools.combinations(row,k))):continue
   if any(sum(x&s==s for x in m)>3 for s in range(256) if s.bit_count()==2):continue
   if any(sum(not x&~s for x in m)>cap[s.bit_count()] for s in range(256)):continue
   raw+=1;k=min(tuple(sorted(p[x] for x in u)) for p in G)
   if k not in checks:checks[k]=budget(m);unknown+=checks[k] is None
   if checks[k] is not False:pool.append((sum(code(x) for x in u),u))
  pools.append(pool);stats.append([raw,len(pool)])
  if not pool:return dict(**base,status='empty_row',stats=stats,unknown=unknown)
 pools.sort(key=len);B=collections.defaultdict(list)
 for k,u in pools[2]:B[k].append(u)
 seen=set();cnt=collections.Counter();win=[];raw=0
 for ka,a in pools[0]:
  for kb,b in pools[1]:
   for d in B.get(demand-ka-kb,[]):
    raw+=1;u=tuple(sorted(a+b+d));
    if u in seen:continue
    seen.update(tuple(sorted(p[x] for x in u)) for p in G);m=f+u
    if any(sum(x&s==s for x in m)>3 for s in range(256) if s.bit_count()==2):cnt['codegree']+=1;continue
    r=run(m);cnt[r[0]]+=1
    if r[0] not in ('forced4','unsat4','single','pair'):win.append(dict(m=m,gate=r))
 return dict(**base,status='join',stats=stats,unknown=unknown,full=raw,hist=cnt,win=win)
if __name__=='__main__':
 d=int(sys.argv[1]);gs=graphs(d);j=max(0,d-7);z=json.loads((P/f'ramsey_exception_first_{d}_{j}.json').read_text());tasks=[]
 for r in z:
  i=r['i'];e=tuple(map(tuple,gs[i]));
  if max(ig.Graph(8,e).degree())<5:continue
  for q in ([( )] if d==6 else [tuple(r['q']+[s]) for s in r['next']]):tasks.append((i,e,q))
 print(d,len(tasks),flush=True);out=[];path=P/f'ramsey_five_leaf_rows_{d}.json'
 with ProcessPoolExecutor(8) as ex:
  for v in ex.map(solve,tasks,chunksize=1):out.append(v)
 path.write_text(json.dumps(out)+'\n');print(collections.Counter(v['status'] for v in out),sum(v.get('full',0) for v in out),flush=True)
