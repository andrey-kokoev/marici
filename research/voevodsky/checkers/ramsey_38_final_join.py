"""Pass the independent four-row enumerator's output to paired-side join. Replay 32-edge control by core ID. Batch files are restartable."""
import json,sys,collections,subprocess,concurrent.futures
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';e=int(sys.argv[3]);hs=sorted(h for h in json.loads((P/'ramsey_38_common49.json').read_text())['triples'] if int(h,16).bit_count()==e);E=[(i,j) for j in range(15) for i in range(j)];work=P/f'ramsey_38_final_join_{e}_parts';work.mkdir(exist_ok=True)
def run(cmd,ls):return subprocess.check_output(cmd,input='\n'.join(ls)+'\n',text=True).splitlines()
def batch(i):
 ids=hs[i:i+16];path=work/f'{i}.json';
 if path.exists():rows=json.loads(path.read_text());assert list(rows)==ids;return rows
 lines=[]
 for h in ids:
  a=[0]*15;m=int(h,16)
  for k,(v,w) in enumerate(E):
   if m>>k&1:a[v]|=1<<w;a[w]|=1<<v
  lines.append(' '.join(map(str,a)))
 sides=[[] for _ in ids]
 for l in run([sys.argv[1],'49'],lines):j,t=l.split(' ',1);sides[int(j)].append(t)
 vals=run([sys.argv[2],str(e)],[' '.join([l]+s) for l,s in zip(lines,sides)]);assert len(vals)==len(ids);out={h:[len(s)]+list(map(int,v.split())) for h,s,v in zip(ids,sides,vals)};tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(out));tmp.replace(path);return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:rows={h:r for d in ex.map(batch,range(0,len(hs),16)) for h,r in d.items()};counts=[sum(r[j]>0 for r in rows.values()) for j in range(7)];print(e,len(rows),counts);assert len(rows)==len(hs)
if e==32:
 old=json.loads((P/'ramsey_38_cross49_32.json').read_text())['rows'];assert all([bool(x) for x in r[:4]]==[bool(x) for x in old[h]] for h,r in rows.items())
(P/f'ramsey_38_final_join_{e}.json').write_text(json.dumps(dict(cores=len(rows),counts=counts,totals=[sum(r[j] for r in rows.values()) for j in range(7)]))+'\n')
