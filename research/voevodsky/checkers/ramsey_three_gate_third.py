"""Exact partition for the last (2,2,2) central shape. Condition a second retained singleton-label block of size three. Test all subcases modulo permutations preserving earlier blocks, rejecting partial forced blue cliques directly."""
from ramsey_three_gate_refine import P,subdata,encode,perms,V,Solver,itertools,cf,json,collections,time,sys,functools
f=(0,3,5);fm,h,gs=subdata(f);pre=[(gs[0],(1,2,4)),(next(g for g in gs if h[g[0]]==2),(0,1,2,4))];g=next(g for g in gs if h[g[0]]==4);ps=[p for p in perms if all(sorted(p[v] for v in x)==list(x) for _,x in pre)];opts=[];raw=0
for x in itertools.combinations_with_replacement(range(8),len(g)):
 if list(x)!=min(sorted(p[v] for v in x) for p in ps):continue
 raw+=1;ms=[h[i]|sum(((v>>j)&1)<<l for j,l in enumerate(f)) for b,xx in pre+[(g,x)] for i,v in zip(b,xx)];cl=[(0,0)]
 for i,s in enumerate(ms):
  bad=sum(1<<j for j,t in enumerate(ms[:i]) if not s&t);cl.extend([(q|1<<i,u|s) for q,u in cl if not q&bad]);
 if not any(q.bit_count()>min(7,u.bit_count()) for q,u in cl):opts.append(x)
def part(t):
 xs,k=t;cs,E,_,_=encode(f,5);out=[]
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  for x in xs:
   ass=[V(i,j)*(1 if val>>j&1 else -1) for g1,xx in pre+[(g,x)] for i,val in zip(g1,xx) for j in range(3)];sl.conf_budget(k);ok=sl.solve_limited(assumptions=ass);out.append(dict(x=x,ok=ok))
 return out
if __name__=='__main__':
 k=int(sys.argv[1]);path=P/f'ramsey_three_gate_third_{k}.json';todo=opts[:];
 if len(sys.argv)>2:
  done={tuple(x['x']) for x in json.loads((P/sys.argv[2]).read_text()) if x['ok'] is False};todo=[x for x in todo if x not in done]
 out=[];print(raw,len(opts),len(todo),flush=True)
 with cf.ProcessPoolExecutor(6) as ex:
  for z in cf.as_completed([ex.submit(part,(todo[i::6],k)) for i in range(min(6,len(todo)))]):out+=z.result();path.write_text(json.dumps(out)+'\n')
 print(collections.Counter(x['ok'] for x in out))
