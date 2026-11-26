"""Look for a uniform obstruction over *all* order- and four-demand-feasible two-cell repairs of a fixed labeled parent. Test each inherited pair separately; exact smallest cover over this list of conflicts. An empty repair cannot evade its own conflicts."""
from ramsey_unsaturated_valley import neighbors,P,pairs,CardEnc,Solver,json,itertools,ProcessPoolExecutor
from ramsey_unsaturated_switches import work

def classify(arg):
 m,regions=arg;E={p:i+1 for i,p in enumerate(p for p in pairs(range(26),2) if not m[p[0]]&m[p[1]])};n=len(E);cs=[];rg={}
 for t in range(256):
  k=t.bit_count();guard=[]
  if k==5 and any(t in pair for pair in regions):n+=1;rg[t]=n;guard=[-n]
  elif k>4:continue
  for s in pairs([i for i,x in enumerate(m) if not x&~t],k+1):
   c=guard+[E[p] for p in pairs(s,2) if p in E];
   if not c:return None
   cs.append(c)
 for i,s in enumerate(m):
  b=CardEnc.equals([v for p,v in E.items() if i in p],8-s.bit_count(),top_id=n);n=max(n,b.nv);cs+=b.clauses
 for x in pairs(range(26),3):
  es=list(pairs(x,2));
  if all(p in E for p in es):cs.append([-E[p] for p in es])
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  if not sl.solve():return None
  return [j for j,(a,b) in enumerate(regions) if sl.solve(assumptions=[rg[a],rg[b]])]
if __name__=='__main__':
 roots=list(map(tuple,json.loads((P/'ramsey_unsaturated_regenerate.json').read_text())[0]['parents']));out=[]
 with ProcessPoolExecutor(8) as ex:
  for i,m in enumerate(roots):
   r=work((i,m));regs=[v[:2] for v in r['other']+r['switch']];ns=list(neighbors(m));rows=[x for x in ex.map(classify,((s,regs) for s in ns),chunksize=8) if x is not None];Q=[set(x) for x in rows];covers=[]
   for k in range(1,1+(len(regs) if len(regs)<=16 else 3)):
    covers=[s for s in itertools.combinations(range(len(regs)),k) if not any(set(s)<=q for q in Q)]
    if covers:break
   z=dict(all_old_pairs_fixed=sum(len(q)==len(regs) for q in Q),i=i,baseline_neighbors=len(rows),pairs=len(regs),minimum=k if covers else None,covers=len(covers),certificate=[regs[j] for j in covers[0]] if covers else None,most_repairs=max(sum(j in q for q in Q) for j in range(len(regs))));print(z,flush=True);out.append(z);(P/'ramsey_unsaturated_barriers.json').write_text(json.dumps(out)+'\n')
