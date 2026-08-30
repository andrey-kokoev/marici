import contextlib, io, json
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
 from five_site_g5_source_residue import CI,L0,NN,HH,ci,ivecadd,ivecscale,idot,sqrti

active=sorted({tuple(q['walls']) for q in json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-exact-coefficients.json').read_text())['certificates'] if q['sheet']==-1})
assert len(active)==22
def sites(q):return {int(c)-1 for c in q[2:]}
def cuts(q):
 A=sites(q);return [e for e in range(5) if (e in A)!=((e+1)%5 in A)]
records=[]
for sheet in (-1,1):
 ll=ivecadd(L0,ivecscale(sheet*HH,NN));ne=ivecscale(ci.inv(),ll);gr={}
 for q in sorted({x for p in active for x in p}):
  g=(ci-ci,ci-ci,ci-ci)
  for e in cuts(q):
   d=tuple(a-b for a,b in zip(ll,CI[e]));g=ivecadd(g,ivecscale(sqrti(idot(d,d)).inv(),d))
  gr[q]=ivecadd(g,ivecscale(-idot(g,ne),ne))
 for a,b in active:
  ga,gb=gr[a],gr[b]
  cross=(ga[1]*gb[2]-ga[2]*gb[1],ga[2]*gb[0]-ga[0]*gb[2],ga[0]*gb[1]-ga[1]*gb[0])
  triple=idot(ne,cross);assert triple.l>0 or triple.h<0
  sign=1 if triple.l>0 else -1
  records.append({'sheet':sheet,'ordered_walls':[a,b],'oriented_jacobian_interval':[str(triple.l),str(triple.h)],
   'physical_intersection_index':sign,'determinant_line_normalized_pairing':1})
assert len(records)==44
packet={'schema':'marici.five_site_g5_transverse_pair_physical_intersections.v1',
 'physical_current':'Entry 1216 oriented Euclidean d^3 ell current',
 'physical_sheet':'Entry 1217 y_i>=0 sheet','certificate_count':44,
 'all_intersections_transverse_and_nonzero':True,
 'determinant_line_normalized_pairing_per_occurrence':1,
 'physical_pairing_constructed':True,
 'scope':'local Betti/de Rham intersection pairing; no global analytic-continuation monodromy claim',
 'records':records}
Path('research/benincasa/results/five-site-g5-transverse-pair-physical-intersections.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('certificate_count','all_intersections_transverse_and_nonzero','determinant_line_normalized_pairing_per_occurrence','physical_pairing_constructed')},sort_keys=True))
