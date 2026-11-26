"""Per marked pair of triple cells, list all size-4/5 masks admissible on one more flexible cell. Orbits under the pair stabilizer share a status. Progress by graph; conserve prior unknowns as possible. Together with cached triple-of-triples tests these domains are necessary for full multisets, with no commitment to a shared core yet."""
from ramsey_unsaturated_ten import *
from concurrent.futures import ProcessPoolExecutor,as_completed
@lru_cache(None)
def initial(e):
 f=fixed(e);G=sym(e);out=set();seen=set()
 for s in sizes:
  if s.bit_count()==3 or s in seen:continue
  orbit={p[s] for p in G};seen.update(orbit)
  if local(f+(s,)):out.update(orbit)
 return sorted(out)
def probe(t):
 i,e,pr=t;G=[p for p in sym(e) if tuple(sorted(p[x] for x in pr))==pr];opts=initial(e);reps=[s for s in opts if s==min(p[s] for p in G)];ok,n=options_for(fixed(e)+pr,reps);return dict(i=i,pr=pr,extra=sorted({p[s] for p in G for s in ok}),unknown=n)
if __name__=='__main__':
 gs=graphs(9);path=P/'ramsey_nine_domains.json';out=json.loads(path.read_text()) if path.exists() else [];done={(z['i'],tuple(z['pr'])) for z in out};rows=json.loads((P/'ramsey_unsaturated_nine_2.json').read_text());# pairs not themselves extendible to a larger sorted canonical triple may still be subpairs of a full multiset
 tasks=[(z['i'],tuple(map(tuple,gs[z['i']])),tuple(z['pr'])) for z in rows if (z['i'],tuple(z['pr'])) not in done];
 if len(sys.argv)>1:tasks=[t for t in tasks if str(t[0]) in sys.argv[1:]]
 print(len(tasks),flush=True)
 with ProcessPoolExecutor(8) as ex:
  for r in ex.map(probe,tasks,chunksize=8):out.append(r)
 path.write_text(json.dumps(out)+'\n')
