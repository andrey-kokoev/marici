"""Eight-singleton unsaturated search, now with global red codegree <=4. Choose the exceptional quartets first; all residual cells are triples. Enumerate pair-graph and quartet multiset orbits without endpoint data. Screen jointly on the fixed subgraph with exact future row quotas and degree-budget relaxation. An induced impossibility is hereditary; retain any timeout. List actual feasible triple additions, up to stabilizer, for each accepted quartet prefix."""
from ramsey_unsaturated_ten import P,json,sym,graphs,fixed,local,options_for,itertools,collections,ProcessPoolExecutor,trips,ig,sys,V
from functools import lru_cache
quarts=[t for t in range(256) if t.bit_count()==4]
@lru_cache(None)
def perm(e):return sym(e)
def step(t):
 i,e,q=t;m=fixed(e)+q;g=perm(e);goal=len(e)-6
 if not q and not local(m):return dict(i=i,q=q,next=[])
 if len(q)<goal:
  domain=[s for s in quarts if (not q or s>=q[-1]) and all(tuple(sorted(p[x] for x in q+(s,)))>=q+(s,) for p in g)]
 else:
  g=[p for p in g if tuple(sorted(p[x] for x in q))==q];domain=[s for s in trips if s==min(p[s] for p in g)]
 # Any two newcomers have the root as common red neighbor. At most three core cells can carry both labels.
 forbidden=[a for a in range(256) if a.bit_count()==2 and sum((x&a)==a for x in m)>=3];domain=[s for s in domain if not any(s&a==a for a in forbidden)];ok,unk=options_for(m,domain,residual=True,slots=True) if domain else ([],0)
 if len(q)==goal:ok=sorted({p[s] for p in g for s in ok})
 return dict(i=i,q=q,next=ok,unknown=unk)
if __name__=='__main__':
 d,k=map(int,sys.argv[1:3]);gs=graphs(d);path=lambda j:P/f'ramsey_exception_first_{d}_{j}.json';es=lambda i:tuple(map(tuple,gs[i]));ts=[(i,es(i),()) for i in range(len(gs))] if k==0 else [(r['i'],es(r['i']),tuple(r['q']+[s])) for r in json.loads(path(k-1).read_text()) for s in r['next']];print(d,k,len(ts),flush=True)
 with ProcessPoolExecutor(8) as ex:out=list(ex.map(step,ts,chunksize=6))
 print('nonempty',sum(bool(z['next']) for z in out),'allowed',sum(len(z['next']) for z in out),flush=True);path(k).write_text(json.dumps(out)+'\n')
