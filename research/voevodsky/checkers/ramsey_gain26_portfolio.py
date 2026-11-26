"""All-additions forecast for every pilot core. Optionally release one original edge per five-capacity parent. Never consult endpoint data. Save records by index; complete lower-demand verification of any surviving leaves is a separate step."""
import sys,json,ast,itertools,concurrent.futures as cf,subprocess,collections
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_gain26_rewire.json').read_text())['records'];five={r['idx'] for r in json.loads((P/'ramsey_gain26_verify_five.json').read_text()) if not r['min_nines']};mode=sys.argv[2];tasks=[];path=P/f'ramsey_gain26_portfolio_{mode}.json';out=json.loads(path.read_text()) if path.exists() else [];done={(r['idx'],tuple(r['del'])) for r in out}
for idx,r in enumerate(R):
 if mode=='one' and idx not in five:continue
 a=r['adj'];eds=[(i,j) for i,v in enumerate(a) for j in range(i) if v>>j&1] if mode=='one' else [()]
 for e in eds:
  if (idx,e) in done:continue
  b=a[:]
  if e:i,j=e;b[i]^=1<<j;b[j]^=1<<i;b.extend((j,i))
  tasks.append((idx,e,b))
def run(chunk):
 p=subprocess.run([sys.argv[1]],input=''.join(' '.join(map(str,b))+'\n' for _,_,b in chunk),capture_output=True,text=True,check=True);ls=iter(p.stdout.splitlines());ans=[]
 for (idx,e,_),st in zip(chunk,map(ast.literal_eval,p.stderr.splitlines()),strict=True):ans.append(dict(idx=idx,del_edge=e,stats=st,leaves=[list(map(int,next(ls).split())) for _ in range(st[-1])]))
 assert next(ls,None) is None
 for r in ans:r['del']=r.pop('del_edge')
 return ans
with cf.ThreadPoolExecutor(8) as ex:
 for f in cf.as_completed([ex.submit(run,tasks[i:i+8]) for i in range(0,len(tasks),8)]):out.extend(f.result());path.write_text(json.dumps(out)+'\n')
print(mode,len(out),list(map(sum,zip(*(r['stats'] for r in out)))),sum(r['stats'][0]>1 for r in out))
