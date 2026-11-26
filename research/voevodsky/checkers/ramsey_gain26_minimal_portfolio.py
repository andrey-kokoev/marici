"""Repeat addition-only search on deletion-minimal cores, per-item timeout and resumable exact verdicts. Do not treat a timeout as exclusion."""
import json,subprocess,sys,concurrent.futures as cf,ast,time,collections
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_gain26_minimal.json').read_text());path=P/'ramsey_gain26_minimal_portfolio.json';out=json.loads(path.read_text()) if path.exists() else [];done={z['idx'] for z in out};todo=[i for i in range(len(R)) if i not in done]
def run(i):
 t=time.perf_counter()
 try:p=subprocess.run([sys.argv[1]],input=' '.join(map(str,R[i]['adj']))+'\n',text=True,capture_output=True,check=True,timeout=float(sys.argv[2]))
 except subprocess.TimeoutExpired:return None
 st=ast.literal_eval(p.stderr.strip());leaves=[list(map(int,l.split())) for l in p.stdout.splitlines()];assert len(leaves)==st[-1];return dict(idx=i,seconds=round(time.perf_counter()-t,3),stats=st,leaves=leaves)
with cf.ThreadPoolExecutor(int(sys.argv[3])) as ex:
 for f in cf.as_completed([ex.submit(run,i) for i in todo]):
  z=f.result()
  if z:out.append(z);path.write_text(json.dumps(out)+'\n')
print(len(out),sum(len(z['leaves']) for z in out),collections.Counter(R[z['idx']]['source'] for z in out))
