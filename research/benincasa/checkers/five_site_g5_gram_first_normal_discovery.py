import json,math
from pathlib import Path

active=sorted({tuple(q['walls']) for q in json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-exact-coefficients.json').read_text())['certificates'] if q['sheet']==-1})
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda a,b:sum(x*y for x,y in zip(a,b));sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
add=lambda a,b:tuple(x+y for x,y in zip(a,b));scale=lambda z,a:tuple(z*x for x in a)
cross=lambda a,b:(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
norm=lambda a:math.sqrt(dot(a,a));unit=lambda a:scale(1/norm(a),a)
def sites(q):return {int(c)-1 for c in q[2:]}
def cuts(q):
 A=sites(q);return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
def planar_f(x,y):
 l=(x,y,0.); c3=(C[3][0],C[3][1],0.);c4=(C[4][0],C[4][1],0.)
 g=add(unit(sub(l,c3)),unit(sub(l,c4)))
 return x*g[1]-y*g[0]
def roots_at_x(x):
 ys=[-5+i*.025 for i in range(401)];out=[]
 for a,b in zip(ys,ys[1:]):
  try:fa,fb=planar_f(x,a),planar_f(x,b)
  except ZeroDivisionError:continue
  if fa*fb>0:continue
  for _ in range(60):
   m=(a+b)/2;fm=planar_f(x,m)
   if fa*fm<=0:b,fb=m,fm
   else:a,fa=m,fm
  y=(a+b)/2
  if all(abs(y-z)>1e-5 for z in out):out.append(y)
 return out
def det_at(pair,x,y,s):
 # First-order lifted threshold point.  zeta follows the vertical stationarity equation.
 l0=(x,y,0.);r0=norm(l0);r3=norm(sub(l0,(C[3][0],C[3][1],0.)));r4=norm(sub(l0,(C[4][0],C[4][1],0.)))
 gp=add(unit(sub(l0,(C[3][0],C[3][1],0.))),unit(sub(l0,(C[4][0],C[4][1],0.))))
 lam=dot(gp,unit(l0));den=1/r3+1/r4-lam/r0
 if abs(den)<1e-8:return None
 zeta=(C[3][2]/r3+C[4][2]/r4)/den
 l=(x,y,s*zeta);cs=[(q[0],q[1],s*q[2]) for q in C];ne=unit(l)
 t1=unit((-ne[1],ne[0],0.));t2=cross(ne,t1)
 rows=[]
 for q in pair:
  g=(0.,0.,0.)
  for e in cuts(q):g=add(g,unit(sub(l,cs[e])))
  rows.append((dot(g,t1),dot(g,t2)))
 return (rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0])/s,zeta

samples=[]
for x in (-1.3,-.7,.25,.8,1.4,2.1):
 for y in roots_at_x(x):
  if min(norm(sub((x,y,0.),(q[0],q[1],0.))) for q in C)<1e-3:continue
  samples.append((x,y))
records=[]
for pair in active:
 vals=[]
 for x,y in samples:
  q=det_at(pair,x,y,1e-6)
  if q is not None:vals.append({'point':[x,y],'j1':q[0],'zeta':q[1]})
 nonzero=any(abs(q['j1'])>1e-5 for q in vals)
 records.append({'walls':list(pair),'nonzero_first_normal_discovered':nonzero,'samples':vals})
packet={'schema':'marici.five_site_g5_gram_first_normal_discovery.v1','stationary_sample_count':len(samples),
 'active_pair_count':22,'pairs_with_nonzero_first_normal':sum(q['nonzero_first_normal_discovered'] for q in records),
 'pairs_requiring_further_audit':[q['walls'] for q in records if not q['nonzero_first_normal_discovered']],
 'records':records,'precision':'f64 discovery on source-labelled rank-drop family; exact certification required'}
Path('research/benincasa/results/five-site-g5-gram-first-normal-discovery.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('stationary_sample_count','active_pair_count','pairs_with_nonzero_first_normal','pairs_requiring_further_audit','precision')},sort_keys=True))
