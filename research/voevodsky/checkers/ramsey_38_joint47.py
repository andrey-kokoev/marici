"""Cross-check Rust joint census against Python survivor counts, then run on all 3647 deletable cores with feasible sixes. Resume an interrupted run by core ID."""
import json,sys,subprocess,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';E=[(i,j) for j in range(20) for i in range(j)]
def run(rows):
 lines=[]
 for h,d in rows:
  a=[0]*20;m=int(h,16)
  for k,(i,j) in enumerate(E):
   if m>>k&1:a[i]|=1<<j;a[j]|=1<<i
  lines.append(' '.join(map(str,a)))
 raw=subprocess.check_output([sys.argv[1]],input='\n'.join(lines)+'\n',text=True).splitlines();assert len(rows)==len(raw);return [list(map(int,l.split())) for l in raw]
refs=sum([json.loads((P/f).read_text()) for f in ('ramsey_38_small_demands47.json','ramsey_38_d3_resistant47_small.json')],[]);assert all(c[:5]==[r['counts'][str(k)] for k in range(1,6)] and c[5]>0 for c,r in zip(run([(r['core'],0) for r in refs]),refs))
rows=json.loads((P/'ramsey_38_deletable47_sixes.json').read_text())['survivors'];path=P/'ramsey_38_deletable47_joint.jsonl';done={json.loads(l)['core'] for l in path.read_text().splitlines()} if path.exists() else set();left=[r for r in rows if r[0] not in done]
with path.open('a') as f:
 for i in range(0,len(left),32):
  batch=left[i:i+32];vs=run(batch)
  for (h,d),c in zip(batch,vs):assert c[5]>0;f.write(json.dumps(dict(core=h,degree=d,counts=c))+'\n')
  f.flush()
res=[json.loads(l) for l in path.read_text().splitlines()];assert len(res)==len(rows)==len(set(r['core'] for r in res));print({d:[sum(r['counts'][k]>0 for r in res if r['degree']==d) for k in range(6)] for d in (3,4)})
