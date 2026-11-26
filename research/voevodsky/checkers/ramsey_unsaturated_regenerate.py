"""Repair search from each all-single-feasible unsaturated archived parent. Release all labels on TWO core cells; exhaust every redistribution preserving label degrees (not just swaps). Rebuild every red edge separately for each region test. Follow newly generated all-single survivors through additional passes. Sort masks but do not identify label permutations. Skip already screened inputs."""
from ramsey_unsaturated_archive_ladder import P,pairs,run,json,collections,ProcessPoolExecutor
import sys
T=[t for t in range(256) if t.bit_count()==4];B=list(range(1,256));cap=[0,1,3,5,8,12,16,19,26]
def gen(m):
 for i,j in pairs(range(26),2):
  a,b=m[i],m[j];u=a^b;common=a&b;v=u
  while True:
   w=u^v
   if v<=w and common|v and common|w and {v|common,w|common}!={a,b}:yield tuple(sorted(m[:i]+m[i+1:j]+m[j+1:]+(v|common,w|common)))
   if not v:break
   v=(v-1)&u

def work(m):
 for t in range(1,255):
  if sum(not x&~t for x in m)>cap[t.bit_count()]:return ['order',t]
 return run(m)
if __name__=='__main__':
 prev=json.loads((P/'ramsey_unsaturated_archive_ladder.json').read_text());seen={tuple(r['m']) for r in prev};front=[tuple(r['m']) for r in prev if r['gate'][0]=='pair'];out=[];path=P/'ramsey_unsaturated_regenerate.json';
 with ProcessPoolExecutor(8) as ex:
  for it in range(int(sys.argv[1])):
   where={m:i for i,s in enumerate(front) for m in gen(s) if m not in seen};seen.update(where);ms=list(where);print('round',it,len(front),len(ms),flush=True);rs=list(ex.map(work,ms,chunksize=12));counts=collections.Counter(r[0] for r in rs);nexts=[dict(m=m,parent=where[m],gate=r) for m,r in zip(ms,rs) if r[0] in ('pair','higher','sat5')];out.append(dict(parents=front,counts=counts,survivors=nexts));path.write_text(json.dumps(out)+'\n');print(counts,flush=True);front=[r['m'] for r in nexts];
   if not front or any(r['gate'][0]!='pair' for r in nexts):break
