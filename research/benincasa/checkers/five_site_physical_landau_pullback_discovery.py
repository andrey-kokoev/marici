import contextlib,io,json,math
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
 from five_site_disjoint_mixed_pair_real_branches import cases

branches=json.loads(Path('research/benincasa/results/five-site-disjoint-mixed-pair-real-branches.json').read_text())['records']
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda a,b:sum(x*y for x,y in zip(a,b));sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
add=lambda a,b:tuple(x+y for x,y in zip(a,b));scale=lambda z,a:tuple(z*x for x in a)
cross=lambda a,b:(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
norm=lambda a:math.sqrt(max(0,dot(a,a)));unit=lambda a:scale(1/norm(a),a)
def sites(q):return {int(c)-1 for c in q[2:]}
def cuts(q):
 A=sites(q);return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
def sphere_points(i,j,a,b,c):
 vi,vj=C[i],C[j];rhs=[(c*c+dot(vi,vi)-a*a)/2,(c*c+dot(vj,vj)-b*b)/2]
 G=[[dot(vi,vi),dot(vi,vj)],[dot(vi,vj),dot(vj,vj)]];D=G[0][0]*G[1][1]-G[0][1]**2
 if abs(D)<1e-10:return []
 co=[(rhs[0]*G[1][1]-rhs[1]*G[0][1])/D,(G[0][0]*rhs[1]-G[0][1]*rhs[0])/D]
 l0=add(scale(co[0],vi),scale(co[1],vj));cr=cross(vi,vj);nh=norm(cr);h2=c*c-dot(l0,l0)
 if h2<-1e-8 or nh<1e-10:return []
 n=scale(1/nh,cr);h=math.sqrt(max(0,h2));return [add(l0,scale(s*h,n)) for s in (-1,1)]

case_map={q[0]:q for q in cases};records=[]
for br in branches:
 label=br['label'];m=case_map[label][1];i,j=cuts(label);candidates=[]
 for xb in br['positive_real_x_branches']:
  x=xb['x']
  for cp in xb['compatible_real_critical_points']:
   if not (cp['same_sign_multipliers'] and cp['negative_t_positive_internal_pair']):continue
   p=cp['p'];s=m*math.sqrt(x);disc=s*s-4*p
   if disc<0:continue
   roots=((s-math.sqrt(disc))/2,(s+math.sqrt(disc))/2);c=2.5*math.sqrt(x)
   for assignment,(a,b) in enumerate((roots,roots[::-1])):
    for sheet,l in enumerate(sphere_points(i,j,a,b,c)):
     uq=unit(sub(l,C[0]));gg=add(unit(sub(l,C[i])),unit(sub(l,C[j])))
     cr=cross(scale(2,uq),gg);n2=dot(cr,cr)
     candidates.append({'x':x,'p':p,'assignment':assignment,'sheet':sheet,'loop_point':list(l),
      'physical_gradient_cross_norm_squared':n2,'physical_gradient_dependent':n2<1e-10})
 records.append({'label':label,'cut_edges':[i,j],'candidate_count':len(candidates),'candidates':candidates,
  'physical_survivor_count':sum(q['physical_gradient_dependent'] for q in candidates)})
packet={'schema':'marici.five_site_physical_landau_pullback_discovery.v1','representative_count':6,
 'reconstructed_physical_candidate_count':sum(q['candidate_count'] for q in records),
 'physical_survivor_count':sum(q['physical_survivor_count'] for q in records),
 'records':records,'precision':'f64 reconstruction discovery; exact certification required for any survivor or exclusion'}
Path('research/benincasa/results/five-site-physical-landau-pullback-discovery.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('representative_count','reconstructed_physical_candidate_count','physical_survivor_count','precision')},sort_keys=True))
