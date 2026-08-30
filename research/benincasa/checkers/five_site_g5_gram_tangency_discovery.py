import json,math,random
from pathlib import Path

active=sorted({tuple(q['walls']) for q in json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-exact-coefficients.json').read_text())['certificates'] if q['sheet']==-1})
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),0.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
scale=lambda s,a:tuple(s*x for x in a)
cross=lambda a,b:(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
norm=lambda a:math.sqrt(dot(a,a))
unit=lambda a:scale(1/norm(a),a)
def sites(q):return {int(c)-1 for c in q[2:]}
def cuts(q):
 A=sites(q);return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
def tangent_frame(ne):
 axis=(0.,0.,1.) if abs(ne[2])<.8 else (1.,0.,0.)
 t1=unit(cross(ne,axis));return t1,cross(ne,t1)
def gradwall(q,l):
 g=(0.,0.,0.)
 for e in cuts(q):g=add(g,unit(sub(l,C[e])))
 return g
def funcs(l,pair):
 if min(norm(sub(l,q)) for q in C)<1e-5:return None
 ne=unit(sub(l,C[0]));t1,t2=tangent_frame(ne)
 gg=add(unit(sub(l,C[3])),unit(sub(l,C[4])))
 gs=[]
 for q in pair:
  g=gradwall(q,l);gs.append(sub(g,scale(dot(g,ne),ne)))
 return [dot(gg,t1),dot(gg,t2),dot(ne,cross(gs[0],gs[1]))]
def solve(A,b):
 M=[A[i][:]+[b[i]] for i in range(3)]
 for c in range(3):
  p=max(range(c,3),key=lambda r:abs(M[r][c]))
  if abs(M[p][c])<1e-10:return None
  M[c],M[p]=M[p],M[c];z=M[c][c];M[c]=[q/z for q in M[c]]
  for r in range(3):
   if r!=c:
    z=M[r][c];M[r]=[M[r][j]-z*M[c][j] for j in range(4)]
 return [M[i][3] for i in range(3)]
def newton(x,pair):
 for _ in range(40):
  f=funcs(x,pair)
  if f is None:return None
  if max(map(abs,f))<1e-9:return x
  h=1e-5;J=[]
  for i in range(3):
   xp=list(x);xp[i]+=h;fp=funcs(tuple(xp),pair)
   if fp is None:return None
   J.append([(fp[j]-f[j])/h for j in range(3)])
  J=list(map(list,zip(*J)));dx=solve(J,[-q for q in f])
  if dx is None:return None
  if norm(dx)>2:dx=scale(2/norm(dx),dx)
  x=tuple(x[i]+dx[i] for i in range(3))
  if norm(x)>20:return None
 return None

rng=random.Random(1820);records=[]
for pair in active:
 roots=[]
 for _ in range(240):
  x=(rng.uniform(-3,3),rng.uniform(-3,3),rng.choice([-1,1])*rng.uniform(.05,4))
  z=newton(x,pair)
  if z is None:continue
  if abs(z[2])<1e-4:continue
  if any(norm(sub(z,r))<1e-4 for r in roots):continue
  roots.append(z)
  if len(roots)>=4:break
 records.append({'walls':list(pair),'candidate_count':len(roots),'candidates':[list(q) for q in roots]})
packet={'schema':'marici.five_site_g5_gram_tangency_discovery.v1','gram_chart':'external five-cycle flattened to z=0',
 'active_pair_count':22,'pairs_with_candidate':sum(bool(q['candidate_count']) for q in records),
 'candidate_count_total':sum(q['candidate_count'] for q in records),'records':records,
 'precision':'f64 Newton discovery only; exact and source-support certification required'}
Path('research/benincasa/results/five-site-g5-gram-tangency-discovery.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('active_pair_count','pairs_with_candidate','candidate_count_total','precision')},sort_keys=True))
