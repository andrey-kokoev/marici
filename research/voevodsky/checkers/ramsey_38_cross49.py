"""Screen paired exclusive groups over surviving 15-cores. Enumerate every labeled 4x4 cross mask of prescribed size, degree <=3 and perfect matching (otherwise the three common neighbors complete an independent eight). Side coordinate sorting is safe: masks remain labeled and all row permutations of opposite side are considered."""
import itertools,json,sys,subprocess,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';e=int(sys.argv[2]);src=json.loads((P/'ramsey_38_common49.json').read_text())['triples'];hs=[h for h in src if int(h,16).bit_count()==e];E=[(i,j) for j in range(15) for i in range(j)];A=[];lines=[]
for h in hs:
 m=int(h,16);a=[0]*15
 for k,(i,j) in enumerate(E):
  if m>>k&1:a[i]|=1<<j;a[j]|=1<<i
 A.append(a);lines.append(' '.join(map(str,a)))
perms=list(itertools.permutations(range(4)));graphs=collections.defaultdict(list);orbits=set()
for c in itertools.combinations(range(16),e-21):
 M=sum(1<<i for i in c);L=tuple(M>>(4*i)&15 for i in range(4));R=tuple(sum((L[j]>>i&1)<<j for j in range(4)) for i in range(4));deg=tuple(6-v.bit_count() for v in L)
 if min(deg)<3 or any(v.bit_count()>3 for v in R) or not any(all(L[j]>>p[j]&1 for j in range(4)) for p in perms):continue
 graphs[deg].append((L,R));orbits.add(min(tuple(sorted(sum((v>>j&1)<<p[j] for j in range(4)) for v in X)) for X in (L,R) for p in perms))
def one(t,L,a):
 return all((t[i]&t[j]).bit_count()+(L[i]&L[j]).bit_count()<=2 for i,j in itertools.combinations(range(4),2)) and all((a[u]&a[v]).bit_count()+sum((s>>u&s>>v)&1 for s in t)<=3 for u,v in E)
out={};
for start in range(0,len(hs),64):
 raw=subprocess.check_output([sys.argv[1],'49'],input='\n'.join(lines[start:start+64])+'\n',text=True);bucket=collections.defaultdict(list)
 for l in raw.splitlines():
  i,*s=map(int,l.split());bucket[i].append(tuple(s))
 for i,h in enumerate(hs[start:start+64]):
  a=A[start+i];sides=bucket[i];opp=collections.defaultdict(set);first=False;both=False;pair=False
  for t in sides:
   for q in itertools.permutations(t):opp[tuple(x.bit_count() for x in q)].add(q)
  for t in sides:
   for L,R in graphs[tuple(x.bit_count() for x in t)]:
    if not one(t,L,a):continue
    first=True
    for q in opp[tuple(6-v.bit_count() for v in R)]:
     if not one(q,R,a):continue
     both=True
     if all(not(L[j]>>k&1 and t[j]&q[k]) for j in range(4) for k in range(4)):pair=True;break
    if pair:break
   if pair:break
  out[h]=[len(sides),first,both,pair]
print(e,len(orbits),len(hs),[sum(bool(r[j]) for r in out.values()) for j in range(4)]);(P/f'ramsey_38_cross49_{e}.json').write_text(json.dumps(dict(orbits=len(orbits),rows=out))+'\n')
