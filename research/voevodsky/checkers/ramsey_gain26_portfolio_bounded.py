"""Finish independent items of a batched portfolio. Timeouts never treated as exclusions; each invocation saves individual completed trees. Optionally test one released edge per core (deterministic first, then second, by number of colorable additions opened)."""
import json,sys,subprocess,concurrent.futures as cf,ast
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_gain26_rewire.json').read_text())['records'];mode=sys.argv[2];path=P/f'ramsey_gain26_portfolio_{mode}.json';out=json.loads(path.read_text()) if path.exists() else [];done={(r['idx'],tuple(r['del'])) for r in out};five={r['idx'] for r in json.loads((P/'ramsey_gain26_verify_five.json').read_text()) if not r['min_nines']};tasks=[]
for idx,r in enumerate(R):
 a=r['adj'];opts=[]
 if mode=='zero':opts=[(0,(),a)]
 elif idx in five:
  for i in range(26):
   for j in range(i):
    if a[i]>>j&1:
     b=a[:];b[i]^=1<<j;b[j]^=1<<i;score=sum(not b[x]>>y&1 and not b[x]&b[y] for x in range(26) for y in range(x));opts.append((score,(i,j),b+[j,i]))
  opts=sorted(opts,reverse=True)[:3]
 for _,e,b in opts:
  if (idx,e) not in done:tasks.append((idx,e,b))
def run(t):
 idx,e,b=t
 try:p=subprocess.run([sys.argv[1]],input=' '.join(map(str,b))+'\n',text=True,capture_output=True,check=True,timeout=int(sys.argv[3]))
 except subprocess.TimeoutExpired:return None
 return {'idx':idx,'del':e,'stats':ast.literal_eval(p.stderr.strip()),'checker':sys.argv[1].replace('\\','/').split('/')[-1],'leaves':[list(map(int,l.split())) for l in p.stdout.splitlines()]}
with cf.ThreadPoolExecutor(6) as ex:
 for f in cf.as_completed([ex.submit(run,t) for t in tasks]):
  z=f.result()
  if z:out.append(z);path.write_text(json.dumps(out)+'\n')
print(mode,len(out),sum(len(r['leaves']) for r in out),[r['idx'] for r in out if r['leaves']])
