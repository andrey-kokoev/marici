"""For each marked triple pair, flex one extra cell over every 3..5 mask. One incremental SAT per branch for the induced graph: triangle constraints, <=5 label clique demands, per-cell residual degrees and edge budget. Reuse learned clauses across candidate masks. Then join 2+3 allowed masks for the last five cells against the residual eight column sums. All timeouts carried forward."""
from ramsey_unsaturated_eleven import *
from functools import lru_cache
path=P/'ramsey_eleven_extend.json'
def options_for(m,candidates,budget=30000,residual=False,slots=False):
 N=len(m);edges={p:k+1 for k,p in enumerate(p for p in pairs(range(N+1),2) if p[1]==N or not m[p[0]]&m[p[1]])};n=len(edges);cs=[];L=list(range(n+1,n+9));n+=8
 def card(xs,k,atleast=True):
  nonlocal n
  if k<=0 and atleast or k>=len(xs) and not atleast:return
  if k>len(xs) and atleast or k<0 and not atleast:cs.append([]);return
  z=(CardEnc.atleast if atleast else CardEnc.atmost)(xs,k,top_id=n);cs.extend(z.clauses);n=max(n,z.nv)
 for i,s in enumerate(m):
  for j in V:
   if s>>j&1:cs.append([-edges[i,N],-L[j]])
 for q in pairs(range(N+1),3):
  es=list(pairs(q,2));
  if all(p in edges for p in es):cs.append([-edges[p] for p in es])
 D=[];left=25-N
 for i in range(N+1):
  xs=[v for p,v in edges.items() if i in p];k=8-m[i].bit_count() if i<N else 8
  if i==N:xs+=L
  if slots:
   d=list(range(n+1,n+left+1));n+=left;D.append([0]+d);xs+=d
   for a,b in zip(d,d[1:]):cs.append([-b,a])
   card(xs,k,False);card(xs,k)
  else:card(xs,k,False);card(xs,k-left)
 if slots:
  # q-th deficit slot means >=q red neighbors among the left omitted cells.
  # Adjacent vertices must use disjoint subsets of that same pool.
  for (i,j),e in edges.items():
   for q in range(1,left+1):cs.append([-e,-D[i][q],-D[j][left+1-q]])
 if residual:
  left=25-N;need=[7-sum(x>>j&1 for x in m) for j in V]
  for j,u in enumerate(need):
   if u>left:cs.append([L[j]])
   if u<=0:cs.append([-L[j]])
   if u>left+1 or u<0:cs.append([])
  for i,s in enumerate(m):
   xs=[v for p,v in edges.items() if i in p];k=8-s.bit_count()
   # Every missing carrier of any label in s is forbidden as a red neighbor of i.
   for j in V:
    if not s>>j&1:continue
    if not slots:card(xs+[L[j]],k-left+need[j]);continue
    for value in (0,1):
     lim=left-need[j]+value
     if 0<=lim<left:cs.append([L[j] if value==0 else -L[j],-D[i][1+lim]])
  if slots:
   for j in V:
    lim=left-need[j]+1
    if 0<=lim<left:cs.append([-L[j],-D[N][1+lim]])
 # e(induced) + |extra mask| >= sum(old prescribed degrees)+8-76.
 card(list(edges.values())+L,sum(8-s.bit_count() for s in m)+8-76)
 for t in range(256):
  k=t.bit_count();vs=[i for i,x in enumerate(m) if not x&~t];outside=[L[i] for i in V if not t>>i&1];
  if len(vs)>=cap[k]:cs.append(outside)
  if k>5:continue
  for size in (k,k+1):
   for q in pairs(vs,size):
    ps=q+(N,) if size==k else q;cs.append(([ *outside] if size==k else [])+[edges[p] for p in pairs(ps,2) if p in edges])
 opts=[];unknown=0
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  for s in candidates:
   sl.conf_budget(budget);v=sl.solve_limited(assumptions=[x if s>>i&1 else -x for i,x in enumerate(L)]);unknown+=v is None
   if v is not False:opts.append(s)
 return opts,unknown

def work(task):
 idx,e,a,b,allowed_tr=task;m=fixed(e)+(a,b);opts,unknown=options_for(m,[s for s in sizes if s.bit_count()!=3 or s in allowed_tr]);code=lambda s:sum(16**i for i in V if s>>i&1);target=7*code(255)-sum(code(s) for s in m);B=collections.defaultdict(list)
 for t in itertools.combinations_with_replacement(opts,2):B[sum(code(s) for s in t)].append(t)
 G=[p for p in group(e) if sorted((p[a],p[b]))==sorted((a,b))];seen=set();cnt=collections.Counter();win=[];nraw=0
 for t in itertools.combinations_with_replacement(opts,3):
  for u in B.get(target-sum(code(s) for s in t),[]):
   v=u+t
   if u[-1]>t[0]:continue
   nraw+=1
   if v in seen:continue
   seen.update(tuple(sorted(p[x] for x in v)) for p in G);r=run(m+v);cnt[r[0]]+=1
   if r[0] not in ('unsat4','forced4'):win.append(dict(v=v,gate=r))
 return dict(idx=idx,a=a,b=b,options=len(opts),unknown=unknown,nraw=nraw,counts=cnt,win=win)
if __name__=='__main__':
 from concurrent.futures import as_completed
 src=json.loads((P/'ramsey_unsaturated_eleven.json').read_text());out=json.loads(path.read_text()) if path.exists() else [];done={(z['idx'],z['a'],z['b']) for z in out};tasks=[(i,z['edges'],a,b,z['triples']) for i,z in enumerate(src) for a,b in z.get('pairs',[]) if (i,a,b) not in done];print(len(tasks),flush=True)
 with ProcessPoolExecutor(8) as ex:
  for f in as_completed([ex.submit(work,t) for t in tasks]):z=f.result();out.append(z);path.write_text(json.dumps(out)+'\n');print(z['idx'],z['options'],z['nraw'],len(z['win']),flush=True)
