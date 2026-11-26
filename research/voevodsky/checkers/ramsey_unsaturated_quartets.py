"""Same 20 fixed cube skeleton cells; release the six degree-four cells with NO complementary pairing assumption. Meet in the middle on eight column sums, sort six masks to avoid permuting cells, canonicalize by all cube skeleton automorphisms. Keep repetitions. Confirm counts independently before and after quotient."""
from ramsey_unsaturated_six_cell import P,cap,run,pairs,json,itertools,collections,ProcessPoolExecutor

def generate():
 fixed=tuple(json.loads((P/'ramsey_unsaturated_six_cell.json').read_text())['fixed']);edges={x for x in fixed if x.bit_count()==2};opts=[x for x in range(256) if x.bit_count()==4];G=[]
 for p in itertools.permutations(range(8)):
  img=lambda s:sum(1<<p[i] for i in range(8) if s>>i&1)
  if {img(x) for x in edges}==edges:G.append({x:img(x) for x in opts})
 # No incidence on an already full four-label region. Necessary for unsaturation, independent of core edges.
 opts=[x for x in opts if sum(not v&~x for v in fixed)<8];assert len(opts)==64;code={x:sum(8**i for i in range(8) if x>>i&1) for x in opts};target=3*sum(8**i for i in range(8));bucket=collections.defaultdict(list)
 for t in itertools.combinations_with_replacement(opts,3):bucket[sum(code[x] for x in t)].append(t)
 seen=set();types=[];total=0
 for u,ls in bucket.items():
  rs=bucket.get(target-u,[])
  for l in ls:
   for r in rs:
    if r[0]<l[-1]:continue
    t=l+r;total+=1
    if t in seen:continue
    orbit={tuple(sorted(g[x] for x in t)) for g in G};seen.update(orbit);types.append((t,len(orbit)))
 assert total==len(seen);return fixed,types,total

def task(arg):
 fixed,t=arg;m=fixed+t
 for l in range(256):
  if sum(not x&~l for x in m)>cap[l.bit_count()]:return ['order',l]
 return run(m)
if __name__=='__main__':
 f,ts,n=generate();print(n,len(ts),flush=True)
 with ProcessPoolExecutor(8) as ex:rs=list(ex.map(task,((f,t) for t,_ in ts),chunksize=8))
 h=collections.Counter(r[0] for r in rs);win=[dict(t=t,orbit=n,gate=r) for (t,n),r in zip(ts,rs) if r[0] in ('single','pair','higher','sat5')];print(h,flush=True);(P/'ramsey_unsaturated_quartets.json').write_text(json.dumps(dict(fixed=f,total=n,types=len(ts),status=h,survivors4=win))+'\n')
