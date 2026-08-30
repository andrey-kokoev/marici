import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-g5-complement-soft-divided-log.json').read_text())
assert src['source_coefficient_certified_nonzero']

# Sym^2 occurrence basis: (e1^2,e1*e2,e2^2).
swap=[[0,0,1],[0,1,0],[1,0,0]]
physical=[0,1,0]
transport=[sum(swap[i][j]*physical[j] for j in range(3)) for i in range(3)]
assert transport==physical
diagonal_trace=[1,1,1]
image=sum(a*b for a,b in zip(diagonal_trace,physical))
assert image==1

packet={
 'schema':'marici.five_site_g5_complement_soft_occurrence_trace.v1',
 'occurrence_pair':['g_15','g_234'],
 'scalar_occurrence_space':'Sym^2<e1,e2>',
 'physical_scalar_class':[0,1,0],
 'complement_swap_eigenvalue':1,
 'physical_diagonal_image':image,
 'antisymmetric_wedge_is_scalar_class':False,
 'relative_sign_scalar_excess_dimension':0,
 'cyclic_orbit_size':5,
 'cyclic_character':[5,0,0,0,0],
 'diagonal_nilpotent_rank_per_occurrence':1,
 'assembled_nilpotent_rank':5,
 'assembled_nilpotent_square_zero':True,
 'classification':'one regular C5 family of complement-invariant pole-twisted logarithms',
}
Path('research/benincasa/results/five-site-g5-complement-soft-occurrence-trace.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
