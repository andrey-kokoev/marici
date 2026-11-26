"""One-deletion shells, including illegal intermediate cores (later additions can restore alpha<=7). Check stronger fork in parallel. Save resumable per-edge results."""
import json,sys,subprocess,ast,concurrent.futures as cf
from ramsey_retention_slice import D
P=D.parent;r=next(x for x in json.loads((P/'ramsey_gain26_edge_descend.json').read_text())['passing'] if x['rows']);a=r['adj'];E=[(i,j) for i,v in enumerate(a) for j in range(i) if v>>j&1];path=P/'ramsey_gain26_release_all.json';out=json.loads(path.read_text()) if path.exists() else [];done={tuple(x['deleted']) for x in out}
def run(e):
 i,j=e;b=a[:];b[i]^=1<<j;b[j]^=1<<i;p=subprocess.run([sys.argv[1]],input=' '.join(map(str,b+[j,i]))+'\n',capture_output=True,text=True,check=True);return dict(deleted=e,stats=ast.literal_eval(p.stderr.strip()),leaves=[list(map(int,l.split())) for l in p.stdout.splitlines()])
with cf.ThreadPoolExecutor(8) as ex:
 for f in cf.as_completed([ex.submit(run,e) for e in E if e not in done]):
  out.append(f.result());path.write_text(json.dumps(out)+'\n');
  if len(out)%10==0:print(len(out),flush=True)
print('total',list(map(sum,zip(*(x['stats'] for x in out)))))
