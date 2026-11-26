"""Release two whole incidence masks of the four-level witness. Preserve label totals only. Region coverage is a ranking (old local unsatisfiability was conditional on global premises); never reject a move solely on its ranking. Deduplicate by the multiset of masks in the original label coordinates. Solve unrestricted degree/triangle/four constraints, then the 18 old regions separately and all scope-five constraints."""
import sys,json,itertools,collections,subprocess
from ramsey_incidence_first35 import P,solve
from ramsey_incidence_mismatch import base
from pysat.card import CardEnc
from pysat.solvers import Solver
R=json.loads((P/'ramsey_incidence_transfer_pivots.json').read_text());m=R['m'];old=R['single_bad'];pool={};raw=0
for i,j in itertools.combinations(range(26),2):
 common=m[i]&m[j];var=m[i]^m[j];t=var
 while True:
  a=common|t;b=common|(var^t)
  if a and b and a.bit_count()<=7 and b.bit_count()<=7 and (a,b)!=(m[i],m[j]) and a<=b and {a,b}!={m[i],m[j]}:
   n=m[:];n[i]=a;n[j]=b;k=tuple(sorted(n));raw+=1
   if k not in pool:
    score=sum(sorted(s for s in (a,b) if not s&~q)!=sorted(s for s in (m[i],m[j]) if not s&~q) for q in old);pool[k]=dict(pair=[i,j],new=[a,b],score=score,m=n)
  if not t:break
  t=(t-1)&var

def test(n):
 E,cs=base(n);top=max(E.values());
 for i,s in enumerate(n):
  xs=[v for e,v in E.items() if i in e];k=8-s.bit_count()
  if len(xs)<k:return dict(status='degree')
  f=CardEnc.equals(xs,k,top_id=top);cs.extend(f.clauses);top=max(top,f.nv)
 acts={}
 for labels in itertools.combinations(range(8),5):
  L=sum(1<<h for h in labels);qs=itertools.combinations([i for i,s in enumerate(n) if not s&~L],6);top+=1;acts[L]=top
  for q in qs:cs.append([-top]+[E[e] for e in itertools.combinations(q,2) if e in E]);
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  if not sl.solve():return dict(status='fail4')
  singles=[L for L in acts if not sl.solve(assumptions=[acts[L]])];ok=not singles and sl.solve(assumptions=list(acts.values()));return dict(status='pass5' if ok else 'pass4',bad=singles)
rs=sorted(pool.values(),key=lambda z:-z['score']);g=subprocess.check_output([sys.argv[1],'4'],input=''.join(' '.join(map(str,z['m']))+'\n' for z in rs),text=True).splitlines();
for z,l in zip(rs,g,strict=True):
 if int(l.split()[0]):z['status']='unit4';continue
 z.update(test(z['m']));
 if z['status']=='pass5':z['full']=solve(z['m'],False)
print(raw,len(rs),collections.Counter(z['status'] for z in rs),collections.Counter(len(z['bad']) for z in rs if 'bad' in z));(P/'ramsey_incidence_release_pairs35.json').write_text(json.dumps(dict(raw=raw,rows=rs),separators=(',',':'))+'\n')
