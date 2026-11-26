"""Sound reusable pruning across complete six-cell census: solve the <=4 demands on the retained 20 plus a subset of released cells. Exact prescribed degrees on partial graph relaxed to interval [d-missing,d]; remove vertices without forcing red edges or incidence on remaining cells. An UNSAT partial subset excludes every extension, not only sorted-prefix extensions. Full survivors checked by exact single and pair ladder. Read canonical tuples from C++ enumerator stdout."""
from ramsey_unsaturated_archive_ladder import P,CardEnc,Solver,itertools,collections,ProcessPoolExecutor,json,run
import sys,time
pairs=itertools.combinations
fixed=tuple(json.loads((P/'ramsey_unsaturated_quartets.json').read_text())['fixed'])
def partial(t):
 m=fixed+t;N=len(m);E={p:i+1 for i,p in enumerate(p for p in pairs(range(N),2) if not m[p[0]]&m[p[1]])};cs=[];n=len(E)
 for l in range(256):
  k=l.bit_count()
  if k>4:continue
  for s in pairs([i for i,x in enumerate(m) if not x&~l],k+1):
   c=[E[p] for p in pairs(s,2) if p in E]
   if not c:return False
   cs.append(c)
 for i,s in enumerate(m):
  d=8-s.bit_count();xs=[v for p,v in E.items() if i in p];lo=max(0,d-(26-N));
  if len(xs)<lo:return False
  for fn,k in [(CardEnc.atleast,lo),(CardEnc.atmost,min(d,len(xs)))]:
   b=fn(xs,k,top_id=n);cs+=b.clauses;n=max(n,b.nv)
 for x in pairs(range(N),3):
  es=list(pairs(x,2));
  if all(e in E for e in es):cs.append([-E[e] for e in es])
 with Solver(name='cadical195',bootstrap_with=cs) as sl:return sl.solve()
def full(t):return run(fixed+t)
if __name__=='__main__':
 ms=[tuple(map(int,l.split())) for l in open(sys.argv[1])];assert len(set(ms))==len(ms);st=[];path=P/'ramsey_unsaturated_free_six.json';out=dict(total=len(ms),stages=st)
 with ProcessPoolExecutor(8) as ex:
  for k in (1,2,3,4,5):
   h=collections.Counter(s for t in ms for s in set(pairs(t,k)));pop=[s for s,n in h.items() if n>=max(3,2**k)];z=list(ex.map(partial,pop,chunksize=10));bad={s for s,v in zip(pop,z) if not v};ms=[t for t in ms if not any(s in bad for s in pairs(t,k))];st.append(dict(k=k,tested=len(pop),unsat=len(bad),remain=len(ms)));print(st[-1],flush=True);path.write_text(json.dumps(out)+'\n');
   if len(ms)<12000:break
  rs=list(ex.map(full,ms,chunksize=8));out.update(counts=collections.Counter(r[0] for r in rs),survivors4=[dict(t=t,gate=r) for t,r in zip(ms,rs) if r[0] not in ('forced4','unsat4')]);print(out['counts'],flush=True);path.write_text(json.dumps(out)+'\n')
