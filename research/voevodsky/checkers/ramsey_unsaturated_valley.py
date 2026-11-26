"""Two-step repair with a temporarily failed single region. Enumerate nonisomorphic order-feasible two-cell neighbors, keeping all baseline-feasible intermediates that fix the starting pair but fail one or more single-region demands. Then repeat from each such intermediate. No budgeted UNSAT. A symmetry quotient must preserve the starting pair until its joint test is complete."""
import json,itertools,collections,sys
from ramsey_unsaturated_regenerate import P,cap,ProcessPoolExecutor
from ramsey_unsaturated_cycle_repair import key
from ramsey_unsaturated_archive_ladder import run
from ramsey_incidence_first35 import CardEnc,Solver
pairs=itertools.combinations

def neighbors(m):
 base=[sum(not s&~t for s in m) for t in range(256)];out=set()
 for i,j in pairs(range(26),2):
  a,b=m[i],m[j];u=a^b;c=a&b;v=u;lim=[(t,cap[t.bit_count()]-base[t]+int(not a&~t)+int(not b&~t)) for t in range(256) if base[t]>=cap[t.bit_count()]-1];lim=[(t,k) for t,k in lim if k<2]
  while True:
   w=u^v;x,y=c|v,c|w
   if 0<x<=y and {x,y}!={a,b} and all(int(not x&~t)+int(not y&~t)<=k for t,k in lim):out.add(tuple(sorted(m[:i]+m[i+1:j]+m[j+1:]+(x,y))))
   if not v:break
   v=(v-1)&u
 return out

def paircheck(arg):
 m,regions=arg;E={p:i+1 for i,p in enumerate(p for p in pairs(range(26),2) if not m[p[0]]&m[p[1]])};n=len(E);cs=[]
 for t in range(256):
  k=t.bit_count()
  if k>4 and t not in regions:continue
  for s in pairs([i for i,x in enumerate(m) if not x&~t],k+1):
   clause=[E[p] for p in pairs(s,2) if p in E];
   if not clause:return False
   cs.append(clause)
 for i,s in enumerate(m):
  b=CardEnc.equals([v for p,v in E.items() if i in p],8-s.bit_count(),top_id=n);n=max(n,b.nv);cs+=b.clauses
 for x in pairs(range(26),3):
  es=list(pairs(x,2));
  if all(p in E for p in es):cs.append([-E[p] for p in es])
 with Solver(name='cadical195',bootstrap_with=cs) as sl:return sl.solve()
if __name__=='__main__':
 roots=json.loads((P/'ramsey_unsaturated_regenerate.json').read_text())[0]['parents'];gates={tuple(z['m']):z['gate'][1:] for z in json.loads((P/'ramsey_unsaturated_archive_ladder.json').read_text()) if z['gate'][0]=='pair'};roots=list(map(tuple,roots));known={key(m) for m in roots};records=[]
 with ProcessPoolExecutor(8) as ex:
  for i,m in enumerate(roots):
   t=gates[m];ns=sorted(neighbors(m));passed=[x for x,ok in zip(ns,ex.map(paircheck,((x,t) for x in ns),chunksize=8)) if ok];temp={key(x):x for x in passed if key(x) not in known};print(i,t,len(ns),len(passed),len(temp),flush=True);records.append(dict(i=i,t=t,order_pass=len(ns),fix_pair=len(passed),mid=list(temp.values())))
  mids={key(tuple(x)):tuple(x) for z in records for x in z['mid']};uniq={};
  for x in mids.values():
   for s in neighbors(x):
    k=key(s)
    if k not in known:uniq[k]=s
  ms=list(uniq.values());print('second layer',len(mids),len(ms),flush=True);res=list(ex.map(run,ms,chunksize=8));surv=[dict(m=m,gate=g) for m,g in zip(ms,res) if g[0] in ('pair','higher','sat5')];counts=collections.Counter(g[0] for g in res);print(counts,flush=True);(P/'ramsey_unsaturated_valley.json').write_text(json.dumps(dict(first=records,middle_types=len(mids),second_counts=counts,survivors=surv))+'\n')
