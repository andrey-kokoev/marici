"""One-residual A/B timing. Build and scope the request cache to this exact pack and side order."""
import json,itertools,subprocess as sp,tempfile,time,statistics,re
from pathlib import Path
from ramsey310_matching_sides import decode,instances,sets,F
D=Path(__file__).resolve().parents[1]/'results';K=D.parent/'checkers'
def main():
 rec=json.loads((D/'ramsey310_smallset_parent12_23.json').read_text());p,h=rec['edit'];A=next(itertools.islice(instances(decode((D/'ramsey38_26_e73_hog.g6').read_bytes().splitlines()[p-1])),h,None));e=rec['survivors'][0]['E'];
 with tempfile.TemporaryDirectory() as temp:
  w=Path(temp);pack=w/'pack';side=w/'side';pack.write_text(''.join(' '.join(map(str,[len(a),*a]))+'\n' for a in [A,*[list(sets(A,F,k)) for k in (5,6,7)]]));src=(K/'ramsey310_matching_indexed.rs').read_text();
  def build(name,text):
   f=w/(name+'.rs');f.write_text(re.sub(r'include!\("([^"/]+)"\)',lambda m:'include!(r"'+str(K/m[1])+'")',text));exe=w/(name+'.exe');sp.run(['rustc','--edition=2021','-O','-C','target-cpu=native',f,'-o',exe],check=True);return exe
  bulk=build('bulk',(K/'ramsey310_matching_bulk.rs').read_text());base=build('base',src)
  with side.open('w') as f:sp.run([bulk,pack],stdout=f,check=True)
  t=time.perf_counter();sp.run(['python',K/'ramsey310_pair_request.py'],stdout=sp.DEVNULL,check=True);req=json.loads((D/'ramsey310_pair_request.json').read_text());rows=[tuple(map(int,l.split())) for l in side.read_text().splitlines()];ids={frozenset(r):i for i,r in enumerate(rows)};bans={}
  for r in req['ports']:
   for x in r['baseline_excluded']:
    E=e.copy();E[r['port']]=x;l,rhs=E[:3],E[3:];i=ids.get(frozenset(l));j=ids.get(frozenset(rhs));
    if None in (i,j):continue
    if i<j:i,j,l,rhs=j,i,rhs,l
    perm=tuple(rows[j].index(rhs[l.index(v)]) for v in rows[i]);key=(i,perm,j//64);bans[key]=bans.get(key,0)|(1<<(j%64))
  setup=time.perf_counter()-t
  # Clear only certified bits before visiting the candidate in the original join.
  ins=''.join(f'if i=={i} && perm=={list(perm)} && b=={b} {{let mask={m}u64;hits+=(h&mask).count_ones();h &= !mask;}}' for (i,perm,b),m in bans.items());cached=build('cached',src.replace('let mut joined=','let mut hits=0u32;let mut joined=').replace('while h!=0{let j=',ins+'while h!=0{let j=').replace('eprintln!("sides','eprintln!("cache_hits {hits}");eprintln!("sides'));times={'base':[],'cached':[]};logs={};outputs={}
  for step in range(11):
   for tag in (('base','cached') if step%2==0 else ('cached','base')):
    start=time.perf_counter();r=sp.run([base if tag=='base' else cached,pack,side],capture_output=True,text=True,check=True);dt=time.perf_counter()-start
    if step:times[tag].append(dt)
    logs[tag]=r.stderr.strip();outputs[tag]=r.stdout.strip()
  assert outputs['base']==' '.join(map(str,e)) and not outputs['cached'];result=dict(setup_seconds=setup,times=times,median={k:statistics.median(v) for k,v in times.items()},logs=logs,outputs=outputs);print(result);(D/'ramsey310_request_timing.json').write_text(json.dumps(result))
if __name__=='__main__':main()
