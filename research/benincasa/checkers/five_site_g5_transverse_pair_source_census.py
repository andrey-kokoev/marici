import itertools, json, math
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
base=json.loads(Path('research/benincasa/results/five-site-g5-source-residue.json').read_text())
pairs=json.loads(Path('research/benincasa/results/five-site-g5-region-pair-gradient-census.json').read_text())
cm=json.loads(Path('research/benincasa/results/five-site-g5-cm-domain.json').read_text())
t=-math.sqrt(cm['x']); E=5*t
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4): C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda u,v:sum(a*b for a,b in zip(u,v))
norm=lambda u:math.sqrt(dot(u,u))
def sites(label): return {int(c)-1 for c in label[2:]}
def cuts(A): return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
def wall(label,X,y):
 if label=='G': return sum(X)
 if label.startswith('G_minus_e'): return sum(X)+2*y[int(label[-2])-1]
 A=sites(label); return sum(X[i] for i in A)+sum(y[e] for e in cuts(A))
def solve3(A,b):
 M=[list(map(float,A[i]))+[float(b[i])] for i in range(3)]
 for c in range(3):
  p=max(range(c,3),key=lambda r:abs(M[r][c]))
  if abs(M[p][c])<1e-12:return None
  M[c],M[p]=M[p],M[c]; z=M[c][c]
  M[c]=[q/z for q in M[c]]
  for r in range(3):
   if r!=c:
    z=M[r][c];M[r]=[M[r][j]-z*M[c][j] for j in range(4)]
 return [M[i][3] for i in range(3)]

records=[]
for sh,prec in zip(base['records'],pairs['records']):
 l=sh['loop_point'];y=[norm(tuple(l[k]-q[k] for k in range(3))) for q in C]
 for pr in prec['pairs']:
  a,b=pr['walls']
  if pr['collinear_numerically']:continue
  count=pr['source_cooccurrence_term_count']
  if count==0:
   records.append({'sheet':sh['sheet'],'walls':[a,b],'source_term_count':0,'status':'source_absent'})
   continue
  candidates=[]
  for inds in itertools.combinations(range(5),3):
   fixed=[i for i in range(5) if i not in inds]
   Aa,Ab=sites(a),sites(b)
   mat=[[1,1,1],[int(i in Aa) for i in inds],[int(i in Ab) for i in inds]]
   rhs=[E-sum(t for _ in fixed),
        -sum(y[e] for e in cuts(Aa))-sum(t for i in fixed if i in Aa),
        -sum(y[e] for e in cuts(Ab))-sum(t for i in fixed if i in Ab)]
   sol=solve3(mat,rhs)
   if sol is None:continue
   X=[t]*5
   for i,z in zip(inds,sol):X[i]=z
   if max(abs(sum(X)-E),abs(wall(a,X,y)),abs(wall(b,X,y)))>1e-7:continue
   common=[q for q in src['common_prefactor'] if q!='g_5']; vals=[]; terms=[]
   for term in src['terms']:
    if not {'G_minus_e12',a,b}.issubset(term):continue
    labs=common+[q for q in term if q not in {'G_minus_e12',a,b}]
    zs=[wall(q,X,y) for q in labs]
    if any(abs(z)<1e-8 for z in zs):terms=[];break
    vals.extend(zs);terms.append(math.prod(1/z for z in zs))
   if terms:candidates.append((min(abs(z) for z in vals),inds,X,sum(terms)/2,len(terms)))
  if not candidates:
   records.append({'sheet':sh['sheet'],'walls':[a,b],'source_term_count':count,'status':'forced_deeper_incidence'})
  else:
   sep,inds,X,total,n=max(candidates)
   records.append({'sheet':sh['sheet'],'walls':[a,b],'source_term_count':count,'status':'isolated',
    'adjusted_sites':[i+1 for i in inds],'term_count':n,'minimum_remaining_wall_abs':sep,
    'double_residue_coefficient':total,'discovery_nonzero':abs(total)>1e-11})

hist={s:sum(r['status']==s for r in records)//2 for s in sorted(set(r['status'] for r in records))}
packet={'schema':'marici.five_site_g5_transverse_pair_source_census.discovery.v1','records':records,
 'one_sheet_status_histogram':hist,
 'all_isolated_discovery_nonzero':all(r.get('discovery_nonzero',True) for r in records),
 'precision':'f64 discovery; exact certification required'}
Path('research/benincasa/results/five-site-g5-transverse-pair-source-census.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({'histogram':hist,'all_isolated_discovery_nonzero':packet['all_isolated_discovery_nonzero'],
 'zero_candidates':[r for r in records if r.get('discovery_nonzero') is False]},sort_keys=True))
