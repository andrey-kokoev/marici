"""Search all integer branches for root-relaxation survivors, resumable by edge stratum. Exact negatives only for terminated trees without leaves."""
import json,sys,subprocess,ast,concurrent.futures as cf,collections
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_gain26_minimal.json').read_text());lp=json.loads((P/'ramsey_gain26_budget_joint.json').read_text());cap=sys.argv[4] if len(sys.argv)>4 else '80';path=P/('ramsey_gain26_budget_tree.json' if cap=='80' else f'ramsey_gain26_budget_tree{cap}.json');out=json.loads(path.read_text()) if path.exists() else [];done={z['idx'] for z in out};todo=[s['idx'] for s in lp if not s['excluded'] and s['idx'] not in done and R[s['idx']]['edges']>=int(sys.argv[2])]
def run(i):
 try:p=subprocess.run([sys.argv[1],cap],input=' '.join(map(str,R[i]['adj']))+'\n',capture_output=True,text=True,timeout=int(sys.argv[3]),check=True)
 except subprocess.TimeoutExpired:return None
 st=ast.literal_eval(p.stderr.strip());ls=[list(map(int,l.split())) for l in p.stdout.splitlines()];assert len(ls)==st[4];return dict(idx=i,stats=st,passing=ls)
with cf.ThreadPoolExecutor(8) as ex:
 for f in cf.as_completed([ex.submit(run,i) for i in todo]):
  z=f.result()
  if z:out.append(z);path.write_text(json.dumps(out)+'\n')
print('completed',len(out),'leaves',sum(len(x['passing']) for x in out),'strata',collections.Counter(R[x['idx']]['edges'] for x in out))
