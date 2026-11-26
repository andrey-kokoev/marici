"""Exact two-deletion shell. Apply first-deletion blue-eight gate both ways. Check second-deletion upper blue-eight gate independently. Run remaining full addition trees. Batches per child (no fresh process per pair); per-pair attribution from graph differences and per-input stats."""
import json,sys,itertools,subprocess,ast,concurrent.futures as cf,collections
from ramsey_retention_slice import D
P=D.parent;a=next(x['adj'] for x in json.loads((P/'ramsey_gain26_edge_descend.json').read_text())['passing'] if x['rows']);E=[(i,j) for i in range(26) for j in range(i) if a[i]>>j&1];gate={tuple(r['first']):set(map(tuple,r['seconds'])) for r in json.loads((P/'ramsey_gain26_release_pair_gate.json').read_text())};tasks=[];out=[]
for p in itertools.combinations(E,2):
 if any(x in gate and y not in gate[x] for x,y in (p,p[::-1])):continue
 b=a[:]
 for i,j in p:b[i]^=1<<j;b[j]^=1<<i
 u=b[:];edges=[]
 for i in range(26):
  for j in range(i):
   if (i,j) not in p and not b[i]>>j&1 and not b[i]&b[j]:u[i]|=1<<j;u[j]|=1<<i;edges.append((i,j))
 I=[0];bad=0
 for i,v in enumerate(u):
  t=[s|1<<i for s in I if not s&v];bad=next((s for s in t if s.bit_count()==8),0)
  if bad:break
  I.extend(t)
 if bad:out.append(dict(pair=p,eight=bad))
 else:tasks.append((p,b+[v for i,j in p for v in (j,i)]))
print('unavoidable eights',len(out),'trees',len(tasks),flush=True);path=P/'ramsey_gain26_double_release.json'
def run(chunk):
 s=subprocess.run([sys.argv[1]],input=''.join(' '.join(map(str,b))+'\n' for p,b in chunk),capture_output=True,text=True,check=True);vals=iter(s.stdout.splitlines());ans=[]
 for (p,b),st in zip(chunk,map(ast.literal_eval,s.stderr.splitlines()),strict=True):
  leaves=[list(map(int,next(vals).split())) for _ in range(st[-1])];ans.append(dict(pair=p,stats=st,leaves=leaves))
 assert next(vals,None) is None;return ans
with cf.ThreadPoolExecutor(8) as ex:
 for fut in cf.as_completed([ex.submit(run,tasks[i:i+5]) for i in range(0,len(tasks),5)]):out+=fut.result();path.write_text(json.dumps(out)+'\n')
print('tested',len(out),'stats',list(map(sum,zip(*(r['stats'] for r in out if 'stats' in r)))))
