"""Deduplicate degree-3 presentations in the supplied 49-edge strata. Replay the generic six-clique screen followed by exact regular-support enumeration on positives. Degree constraints never remove any true 7-regular extension."""
import sys,json,gzip,concurrent.futures,subprocess
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';ns=list(map(int,sys.argv[3:]));keys=sorted(set.union(*(set(json.load(gzip.open(P/f'ramsey_38_d3_49_{n}_{n}.json.gz'))) for n in ns)));E=[(i,j) for j in range(20) for i in range(j)]
def run(cmd,lines):return subprocess.check_output(cmd,input='\n'.join(lines)+'\n',text=True).splitlines() if lines else []
def part(i):
 hs=keys[i:i+1024];lines=[]
 for h in hs:
  a=[0]*20;m=int(h,16);assert m.bit_count()==49
  for k,(u,v) in enumerate(E):
   if m>>k&1:a[u]|=1<<v;a[v]|=1<<u
  assert min(v.bit_count() for v in a)==3;lines.append(' '.join(map(str,a)))
 v=list(map(int,run([sys.argv[1]],lines)));assert len(v)==len(hs);ix=[j for j,b in enumerate(v) if b];reg=run([sys.argv[2],'--regular'],[lines[j] for j in ix]);assert len(reg)==len(ix);return {hs[j]:list(map(int,c.split())) for j,c in zip(ix,reg)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:surv={h:c for partrows in ex.map(part,range(0,len(keys),1024)) for h,c in partrows.items()}
counts=[sum(c[k]>0 for c in surv.values()) for k in range(6)];print(len(keys),len(surv),counts,flush=True);(P/('ramsey_38_regular49_'+'_'.join(map(str,ns))+'.json')).write_text(json.dumps(dict(types=len(keys),counts=counts,generic_six_pass=surv))+'\n')
