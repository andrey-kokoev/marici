import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-exact-coefficients.json').read_text())
pairs=sorted({tuple(q['walls']) for q in src['certificates'] if q['sheet']==-1})
assert len(pairs)==22
def rot_region(q,k):
 A=sorted(((int(c)-1+k)%5)+1 for c in q[2:])
 return 'g_'+''.join(map(str,A))
def rot_threshold(k):
 a=(0+k)%5+1;b=(1+k)%5+1
 return f'G_minus_e{a}{b}'
def packet(pair,k):return (rot_threshold(k),)+tuple(sorted(rot_region(q,k) for q in pair))
orbits=[];seen=set()
for pair in pairs:
 orb=[packet(pair,k) for k in range(5)]
 assert len(set(orb))==5
 assert not (set(orb)&seen)
 seen.update(orb);orbits.append({'representative':['G_minus_e12',*pair],'orbit':[list(q) for q in orb],'orbit_size':5})
assert len(seen)==110
packet_out={'schema':'marici.five_site_g5_transverse_pair_cyclic_assembly.v1','local_active_pair_count':22,
 'free_orbit_count':22,'global_labelled_occurrence_count':110,'cyclic_character':[110,0,0,0,0],
 'rational_representation':'Q[C5]^22','orbits':orbits}
Path('research/benincasa/results/five-site-g5-transverse-pair-cyclic-assembly.json').write_text(
 json.dumps(packet_out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet_out[k] for k in ('local_active_pair_count','free_orbit_count','global_labelled_occurrence_count','cyclic_character','rational_representation')},sort_keys=True))
