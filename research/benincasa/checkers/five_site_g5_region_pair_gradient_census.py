import itertools,json,math
from pathlib import Path

from five_site_g5_source_residue import CI,L0,NN,HH,ci,ivecadd,ivecscale,idot,sqrti

src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
physical=json.loads(Path('research/benincasa/results/five-site-g5-source-residue.json').read_text())
supported=json.loads(Path('research/benincasa/results/five-site-g5-region-wall-kummer-quotients.json').read_text())['supported_labels']
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda u,v:sum(a*b for a,b in zip(u,v));sub=lambda u,v:tuple(a-b for a,b in zip(u,v))
add=lambda u,v:tuple(a+b for a,b in zip(u,v));scale=lambda a,u:tuple(a*x for x in u)
norm=lambda u:math.sqrt(dot(u,u))
def cuts(label):
 A={int(c)-1 for c in label[2:]};return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
records=[]
for sh in physical['records']:
 l=tuple(sh['loop_point']);ne=scale(1/norm(sub(l,C[0])),sub(l,C[0]));gr={}
 for q in supported:
  g=(0.,0.,0.)
  for e in cuts(q):g=add(g,scale(1/norm(sub(l,C[e])),sub(l,C[e])))
  gr[q]=sub(g,scale(dot(g,ne),ne))
 rows=[]
 for a,b in itertools.combinations(supported,2):
  ga,gb=gr[a],gr[b];det=dot(ga,ga)*dot(gb,gb)-dot(ga,gb)**2
  count=sum('G_minus_e12' in t and a in t and b in t for t in src['terms'])
  rows.append({'walls':[a,b],'gradient_gram_determinant':det,
               'collinear_numerically':abs(det)<1e-11,'source_cooccurrence_term_count':count})
 records.append({'sheet':sh['sheet'],'pairs':rows})
zeros=sorted(set(tuple(q['walls']) for r in records for q in r['pairs'] if q['collinear_numerically']))
exact=[]
for sheet in (-1,1):
 ll=ivecadd(L0,ivecscale(sheet*HH,NN));ne=ivecscale(ci.inv(),ll);gr={}
 for q in supported:
  g=(ci-ci,ci-ci,ci-ci)
  for e in cuts(q):
   d=tuple(a-b for a,b in zip(ll,CI[e]));g=ivecadd(g,ivecscale(sqrti(idot(d,d)).inv(),d))
  gr[q]=ivecadd(g,ivecscale(-idot(g,ne),ne))
 rows=[]
 for a,b in itertools.combinations(supported,2):
  same_boundary=cuts(a)==cuts(b)
  if same_boundary:
   rows.append({'walls':[a,b],'same_boundary_occurrences':True,'certified_collinear':True})
  else:
   ga,gb=gr[a],gr[b]
   cross=(ga[1]*gb[2]-ga[2]*gb[1],ga[2]*gb[0]-ga[0]*gb[2],ga[0]*gb[1]-ga[1]*gb[0])
   triple=idot(ne,cross);det=triple*triple
   assert det.l>0,(sheet,a,b,det.l,det.h)
   rows.append({'walls':[a,b],'same_boundary_occurrences':False,
                'gram_determinant_interval':[str(det.l),str(det.h)],'certified_collinear':False})
 exact.append({'sheet':sheet,'pairs':rows})
counts={str(k):sum(q['source_cooccurrence_term_count']==k for q in records[0]['pairs']) for k in sorted(set(q['source_cooccurrence_term_count'] for q in records[0]['pairs']))}
packet={'schema':'marici.five_site_g5_region_pair_gradient_census.discovery.v1',
 'supported_wall_count':len(supported),'pair_count_per_sheet':len(records[0]['pairs']),
 'records':records,'numerically_collinear_pairs':[list(q) for q in zeros],
 'exact_interval_certificates':exact,
 'exact_collinear_pairs':[['g_145','g_23'],['g_15','g_234']],
 'all_other_pairs_certified_independent':True,
 'source_cooccurrence_count_histogram_one_sheet':counts,
 'precision':'f64 discovery; exact certification required'}
Path('research/benincasa/results/five-site-g5-region-pair-gradient-census.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({'collinear':packet['numerically_collinear_pairs'],'cooccurrence_histogram':counts,
 'minimum_nonzero':min(abs(q['gradient_gram_determinant']) for r in records for q in r['pairs'] if not q['collinear_numerically'])},sort_keys=True))
