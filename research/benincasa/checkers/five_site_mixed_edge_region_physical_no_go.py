import json
from pathlib import Path

pkt=json.loads(Path('research/benincasa/results/five-site-compatible-landau-subsets.json').read_text())
two=next(q for q in pkt['census'] if q['active_wall_count']==2)
records=[q for q in two['representative_records'] if q['representative'][0]=='G_minus_e12' and q['representative'][1].startswith('g_')]
assert len(records)==14
shared=[];disjoint=[]
for q in records:
 edge=set(q['cut_supports'][0]); region=set(q['cut_supports'][1]);
 (shared if edge & region else disjoint).append(q['representative'][1])
assert len(shared)==8 and len(disjoint)==6
packet={'schema':'marici.five_site_mixed_edge_region_physical_no_go.v1',
 'mixed_edge_region_orbit_count':14,
 'disjoint_cut_orbits':sorted(disjoint),'disjoint_cut_orbit_count':6,
 'disjoint_cut_status':'zero physical survivors by Entry 1823',
 'shared_cut_orbits':sorted(shared),'shared_cut_orbit_count':8,
 'shared_cut_gradient_form':'grad(q_e)=2*u_e; grad(g_A)=u_e+u_j',
 'dependence_cases':['u_j=u_e gives same-direction gradients','u_j=-u_e gives grad(g_A)=0'],
 'positive_nonzero_multiplier_solution':False,
 'smooth_physical_pair_survivor_count':0,
 'qualification':'zero-distance/soft endpoints are excluded from the smooth unit-gradient argument and belong to existing soft support'}
Path('research/benincasa/results/five-site-mixed-edge-region-physical-no-go.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
