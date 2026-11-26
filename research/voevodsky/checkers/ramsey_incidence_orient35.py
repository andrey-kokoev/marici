"""Profile-stratified search with singleton and repeated masks; build marginal skeleton before assigning binary orientations. Source of all structures is the incidence generator, not a 35-witness. Compare Hall-only vs forced-edge saturation. Replay gate survivors in unrestricted completion model."""
import random,json,sys,subprocess,ast,collections
from ramsey_incidence_first35 import solve,P
rng=random.Random(350814);inputs=[];profiles=[]
for i in range(int(sys.argv[2])):
 s=i%4+1;f=(i//4)%3;ds=[1]*s+[2]*(11-2*s+f)+[3]*(s+2-2*f)+[4]*f
 if len(ds)!=13 or sum(ds)!=28:continue
 while True:
  st=[j for j in range(4) for _ in range(7)];rng.shuffle(st);ms=[];k=0
  for d in ds:
   bits=st[k:k+d];k+=d
   if len(set(bits))<d-1 and d<4 or any(bits.count(h)>2 for h in bits):break
   m=0
   for h in bits:
    t=2*h+rng.randrange(2);t^=(m>>t)&1;m|=1<<t
   ms.append(m)
  else:break
 # interleave sizes; high constraints early. Avoid many copies of an identical singleton orbit.
 rng.shuffle(ms);ms.sort(key=lambda v:ds.count(v.bit_count()));inputs.append(ms);profiles.append(ds)
p=subprocess.run([sys.argv[1],sys.argv[3]],input=''.join(' '.join(map(str,m))+'\n' for m in inputs),text=True,capture_output=True,check=True);out=[];lines=iter(p.stdout.splitlines());
for sk,ds,l in zip(inputs,profiles,p.stderr.splitlines(),strict=True):
 h=ast.literal_eval(l);surv=[]
 for _ in range(h[2]):
  m=list(map(int,next(lines).split()));surv.append(dict(m=m,verdict=solve(m,False)))
 out.append(dict(sk=sk,ds=ds,h=h,surv=surv))
assert next(lines,None) is None;print('skeletons',len(out),'total',list(map(sum,zip(*(z['h'] for z in out)))),'surv',collections.Counter(v['verdict']['status'] for z in out for v in z['surv']));(P/'ramsey_incidence_orient35.json').write_text(json.dumps(out)+'\n')
