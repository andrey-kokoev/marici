"""Compare start, coordinated-switch incumbents, and alternate roots. Independent replay of all structural invariants, joint region verdicts, and absolute blue-nine count. Do not treat local score as a Ramsey witness."""
import json,sys,subprocess,itertools,collections,math,concurrent.futures as cf
from ramsey_retention_slice import D
P=D.parent;src=json.loads((P/'ramsey_incidence_five_frontier.json').read_text());a=[0]*35
for i,j in src['edges']:a[i]|=1<<j;a[j]|=1<<i
for i,m in enumerate(src['m']):
 for j in range(8):
  if m>>j&1:a[i]|=1<<(26+j);a[26+j]|=1<<i
for j in range(26,34):a[j]|=1<<34;a[34]|=1<<j

def audit(g,root):
 assert all(v.bit_count()==8 for v in g) and all(g[i]>>j&1==(g[j]>>i&1) and (not g[i]>>j&1 or not g[i]&g[j]) for i in range(35) for j in range(35));N=[j for j in range(35) if g[root]>>j&1];C=[i for i in range(35) if i!=root and i not in N];m=[sum((g[i]>>v&1)<<j for j,v in enumerate(N)) for i in C];I=[(0,0)]
 for i in range(26):
  red=sum((g[C[i]]>>v&1)<<j for j,v in enumerate(C));I.extend([(q|1<<i,u|m[i]) for q,u in I if not q&red]);
 regions=set();nines=0;alph=0;mix=collections.Counter()
 for q,u in I:
  k=q.bit_count();h=u.bit_count();alph=max(alph,k+max(1,8-h));cnt=(int(k==8)+ (math.comb(8-h,9-k) if k<=9 else 0));nines+=cnt;mix[k]+=cnt
  if k<=min(7,h):continue
  for t in range(256):
   if u&~t==0 and k>min(7,t.bit_count()):regions.add(t)
 prof=[sum(max(4,t.bit_count())==i for t in regions) for i in range(4,9)];return dict(prof=prof,nines=nines,alpha=alph,mix={k:v for k,v in mix.items() if v})

def run(seed):
 p=subprocess.run([sys.argv[1],str(seed),sys.argv[2]],input=' '.join(str(v&((1<<34)-1)) for v in a[:34]),text=True,capture_output=True,check=True);h,g=p.stdout.splitlines()[-1].split(';');g=list(map(int,g.split()))+[a[-1]]
 for i in range(26,34):g[i]|=1<<34
 z=audit(g,34);assert z['prof']==list(map(int,h.split()));return dict(seed=seed,stats=p.stderr.strip(),adj=g,**z)
if __name__=='__main__':
 start=audit(a,34);others=[audit(a,i) for i in range(35)];assert all(z['nines']==start['nines'] for z in others);print('start',start,'best same graph',min(z['prof'] for z in others),flush=True)
 with cf.ThreadPoolExecutor(8) as ex:rows=list(ex.map(run,range(351701,351709)))
 best=min(rows,key=lambda z:(z['prof'],z['nines']));roots=[audit(best['adj'],i) for i in range(35)];assert all(z['nines']==best['nines'] for z in roots);print([(z['prof'],z['nines']) for z in rows],best['stats'],'best reroot',min(z['prof'] for z in roots));(P/'ramsey_incidence_walk35.json').write_text(json.dumps(dict(start=start,start_roots=others,rows=rows,best_roots=roots))+'\n')
