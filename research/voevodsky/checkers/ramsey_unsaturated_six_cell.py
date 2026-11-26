"""Release six cells together. Keep the eight singleton masks and twelve pair masks of the fourth seed. Generate three arbitrary complementary pairs of nonempty proper subsets, repetitions allowed, so row degrees stay seven. Enumerate modulo the FULL automorphism group of the retained pair graph before any rating; even a pair need not be balanced 4+4. Apply necessary predecessor order bounds and exact SAT ladder. This is not unrestricted six-cell completion."""
from ramsey_unsaturated_regenerate import P,cap,run,pairs,json,collections,ProcessPoolExecutor
import itertools,math

def enumerate_types():
 z=json.loads((P/'ramsey_unsaturated_regenerate.json').read_text())[0]['parents'][3];fixed=tuple(s for s in z if s.bit_count()<=2);edges={s for s in fixed if s.bit_count()==2};assert len(fixed)==20 and all(sum(s>>i&1 for s in fixed)==4 for i in range(8));G=[]
 for p in itertools.permutations(range(8)):
  def img(s):return sum(1<<p[i] for i in range(8) if s>>i&1)
  if {img(s) for s in edges}==edges:G.append([min(v:=img(s),255^v) for s in range(128)])
 assert len(G)==48;seen=set();out=[]
 for triple in itertools.combinations_with_replacement(range(1,128),3):
  if triple in seen:continue
  orbit={tuple(sorted(g[i] for i in triple)) for g in G};seen.update(orbit);out.append((triple,len(orbit)))
 assert len(seen)==math.comb(129,3);return fixed,out

def task(arg):
 m,t=arg;m=m+tuple(v for x in t for v in (x,255^x));
 for l in range(256):
  if sum(not x&~l for x in m)>cap[l.bit_count()]:return ['order',l]
 return run(m)
if __name__=='__main__':
 fixed,types=enumerate_types();print('types',len(types),flush=True)
 with ProcessPoolExecutor(8) as ex:rs=list(ex.map(task,((fixed,t) for t,n in types),chunksize=12))
 cnt=collections.Counter(r[0] for r in rs);win=[dict(t=t,orbit=n,gate=r) for (t,n),r in zip(types,rs) if r[0] in ('single','pair','higher','sat5')];print(cnt,flush=True);(P/'ramsey_unsaturated_six_cell.json').write_text(json.dumps(dict(fixed=fixed,total=sum(n for _,n in types),types=len(types),status=cnt,survivors4=win))+'\n')
