"""Exact-ten saturation screen: eight remaining cells use 28 labels so >=4 are triples. Mark four triples via canonical sorted augmentation; test extensions on one flexible cell with the five-label/degree relaxation. Preserve unknowns. Finally meet in the middle on the remaining four cells. Each layer is resumable from the preceding completed JSON."""
from ramsey_eleven_extend import options_for
from ramsey_unsaturated_eleven import *
from functools import lru_cache
from concurrent.futures import as_completed
code=lambda s:sum(16**i for i in V if s>>i&1);codes=list(map(code,range(256)))
@lru_cache(None)
def sym(es):return group(es)
def test(t):
 i,es,pr,opts=t;g=sym(es);f=fixed(es);m=f+pr;nexts=[];cnt=collections.Counter();win=[];k=len(pr)
 if k==0 and not local(f):return dict(i=i,pr=pr,base=False,children=[])
 if k<24-2*len(es):
  lo=pr[-1] if k else 0;c=[s for s in opts if s>=lo and all(tuple(sorted(p[x] for x in pr+(s,)))>=pr+(s,) for p in g)];
  if not c:return dict(i=i,pr=pr,children=[])
  ok,un=options_for(m,c,residual=(len(es)==9 and k>=3),slots=(len(es)==9 and k>=4));return dict(i=i,pr=pr,children=ok,unknown=un)
 # Remaining four need total size 16. For each label exact residual column sum. Cheap quota test before SAT; screen companions only if a full tuple is possible.
 target=7*codes[255]-sum(codes[x] for x in m);B=collections.defaultdict(list)
 for a,b in itertools.combinations_with_replacement(sizes,2):B[codes[a]+codes[b]].append((a,b))
 if len(es)==10:groups=[u+v for k1,ls in B.items() for u in ls for v in B.get(target-k1,[]) if u[-1]<=v[0]]
 elif len(es)==9:groups=[(s,)+v for s in sizes for v in B.get(target-codes[s],[]) if s<=v[0]]
 else:raise ValueError(len(es))
 domain=sorted({x for v in groups for x in v});ok,un=options_for(m,domain,residual=(len(es)==9),slots=(len(es)==9)) if domain else ([],0);ok=set(ok);groups=[u for u in groups if ok.issuperset(u)];seen=set();stab=[p for p in g if tuple(sorted(p[x] for x in pr))==pr]
 for u in groups:
  if u in seen:continue
  seen.update(tuple(sorted(p[x] for x in u)) for p in stab);r=run(m+u);cnt[r[0]]+=1
  if r[0] not in ('unsat4','forced4'):win.append(dict(u=u,r=r))
 return dict(i=i,pr=pr,unknown=un,complete=len(groups),hist=cnt,win=win)
if __name__=='__main__':
 k=int(sys.argv[1]);d=int(sys.argv[2]) if len(sys.argv)>2 else 10;name={9:'nine',10:'ten'}[d];gs=graphs(d);tasks=[];scope=sys.argv[3] if len(sys.argv)>3 else '';assert scope in ('','isolated','regularish','twoleaf','oneleaf');filename=lambda j:P/f"ramsey_unsaturated_{name}{('_'+scope) if scope and j>=3 else ''}_{j}.json";path=filename(k);prev=lambda j:json.loads(filename(j).read_text());es=lambda i:tuple(tuple(e) for e in gs[i]);
 if k==0:tasks=[(i,es(i),(),trips) for i in range(len(gs))]
 else:
  for z in prev(k-1):
   i=z['i'];
   for s in z['children']:tasks.append((i,es(i),tuple(z['pr']+[s]),trips))
 if scope=='isolated':tasks=[t for t in tasks if min(ig.Graph(8,gs[t[0]]).degree())==0]
 if scope=='regularish':tasks=[t for t in tasks if min(ig.Graph(8,gs[t[0]]).degree())>=2]
 if scope in ('twoleaf','oneleaf'):
  old=json.loads((P/'ramsey_nine_leaf_gate.json').read_text());take={i for i in old['open'] if ig.Graph(8,gs[i]).degree().count(1)==(2 if scope=='twoleaf' else 1)};tasks=[t for t in tasks if t[0] in take]
 if 2<=k<24-2*d:
  good={(r['i'],tuple(r['pr']+[s])) for r in prev(k-1) for s in r['children']};cache={}
  def supported(i,e,u):
   if (i,u) not in cache:cache[i,u]=(i,min(tuple(sorted(p[x] for x in u)) for p in sym(e))) in good
   return cache[i,u]
  tasks=[(i,e,pr,[s for s in opts if s>=pr[-1] and all(supported(i,e,tuple(sorted(u+(s,)))) for u in itertools.combinations(pr,k-1))]) for i,e,pr,opts in tasks]
 if k==4 and d==9 and scope=='oneleaf':
  # A five-triple family needs some sixth triple (not necessarily later in sorted order).
  # Precompute all extensions of supported triples to a supported four-set, modulo label relabelings.
  supports=collections.defaultdict(int);idx={s:j for j,s in enumerate(trips)}
  for i,u in good:
   for p_ in sym(es(i)):
    b=tuple(sorted(p_[x] for x in u))
    for j in range(4):supports[(i,b[:j]+b[j+1:])]|=1<<idx[b[j]]
  contains=[sum(1<<idx[s] for s in trips if s>>j&1) for j in V];quotas={i:[7-sum(x>>j&1 for x in fixed(es(i))) for j in V] for i in take}
  def extendible(i,u):
   poss=(1<<56)-1
   for b in itertools.combinations(u,3):
    poss &= supports.get((i,b),0)
    if not poss:return False
   for j,t in enumerate(quotas[i]):
    r=t-sum(x>>j&1 for x in u)
    if not 0<=r<=4:return False
    if not r:poss &= ~contains[j]
    if r==4:poss &= contains[j]
   return bool(poss)
  tasks=[(i,e,pr,[s for s in opts if extendible(i,pr+(s,))]) for i,e,pr,opts in tasks]
 out=prev(k) if path.exists() else [];done={(z['i'],tuple(z['pr'])) for z in out};tasks=[t for t in tasks if (t[0],t[2]) not in done];print(k,len(gs),len(tasks),flush=True)
 with ProcessPoolExecutor(8) as ex:
  for z in ex.map(test,tasks,chunksize=12):
   out.append(z)
   if len(out)%25000==0:path.write_text(json.dumps(out)+'\n')
  path.write_text(json.dumps(out)+'\n')
 print('records',len(out),'children',sum(len(r.get('children',[])) for r in out),'complete',sum(r.get('complete',0) for r in out),'unknowns',sum(r.get('unknown',0) for r in out),flush=True)
