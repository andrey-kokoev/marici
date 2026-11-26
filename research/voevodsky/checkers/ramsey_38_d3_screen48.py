"""Union rooted sublayers before screening. Run six-clique test on every type, then exact joint census only on its survivors. Batch checkpoints keyed by first/last graph."""
import gzip,json,sys,subprocess,concurrent.futures,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';d=4 if len(sys.argv)>3 else 3;ns=list(map(int,sys.argv[3:])) if d==4 else list(range(32,40));name='ramsey_38_d3_screen48' if d==3 else 'ramsey_38_d4_screen48_'+'_'.join(map(str,ns));work=P/(name+'_parts');work.mkdir(exist_ok=True);seen=set();strata={}
for n in ns:
 rows=json.load(gzip.open(P/(f'ramsey_38_d3_48_{n}_{n}.json.gz' if d==3 else f'ramsey_38_d4_48_{n}.json.gz')));strata[n]=len(rows);seen.update(rows)
keys=sorted(seen);print('strata',strata,'union',len(keys),flush=True);E=[(u,v) for v in range(20) for u in range(v)]
def run(cmd,lines):return subprocess.check_output([cmd],input='\n'.join(lines)+'\n',text=True).splitlines() if lines else []
def part(i):
 batch=keys[i:i+2048];path=work/f'{i}.json';
 if path.exists():
  r=json.loads(path.read_text());assert (r['first'],r['last'])==(batch[0],batch[-1]);return r
 lines=[]
 for h in batch:
  a=[0]*20;m=int(h,16);assert m.bit_count()==48
  for k,(u,v) in enumerate(E):
   if m>>k&1:a[u]|=1<<v;a[v]|=1<<u
  assert min(v.bit_count() for v in a)==d;lines.append(' '.join(map(str,a)))
 s=run(sys.argv[1],lines);assert len(s)==len(batch);ix=[j for j,b in enumerate(s) if int(b)];cs=[list(map(int,l.split())) for l in run(sys.argv[2],[lines[j] for j in ix])];assert len(cs)==len(ix) and all(c[-1] for c in cs);r=dict(first=batch[0],last=batch[-1],types=len(batch),survivors={batch[j]:c for j,c in zip(ix,cs)});tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(r));tmp.replace(path);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:parts=list(ex.map(part,range(0,len(keys),2048)))
surv={h:c for p in parts for h,c in p['survivors'].items()};counts=[sum(c[j]>0 for c in surv.values()) for j in range(6)];print('remaining one through six',counts);(P/(name+'.json')).write_text(json.dumps(dict(types=len(keys),strata=strata,counts=counts,survivors=surv))+'\n')
