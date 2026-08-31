"""Assemble marked and nonmarked exact results into the full unbounded K-family theorem."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; V=ROOT/'research'/'voevodsky'/'results'; OUT=V/'cosmology_full_K_characteristic_zero_absorption.json'
def load(n):return json.loads((V/n).read_text())
def main():
 seed=load('cosmology_nonmarked_K_exact_seeds_a12.json');orbit=load('cosmology_nonmarked_K_orbit_census.json');marked=load('cosmology_rank26_p_normal_unbounded_quotient_colimit_gate.json');law=load('cosmology_rank26_p_normal_uniform_constructor_law.json');reach=load('cosmology_rank26_p_normal_uniform_target_reachability.json');assert all(x['passed'] for x in [seed,orbit,marked,law,reach])
 assert seed['targets_verified']==248 and orbit['orbit_count']==248 and marked['components']==8
 components=248+8;assert components==2*32*4
 sample_counts={str(A):32*(A-3)*(A-2) for A in (12,14,16,18,20)}
 out={'schema':'marici.voevodsky.cosmology-full-K-characteristic-zero-absorption.v1','status':'full_K_derivative_family_absorbed_exactly_for_all_even_ambient_degrees_at_least_12','ambient_degrees':'all even A>=12','target_count_formula':'2 K poles * 32 level patterns * binomial(A-2,2) exponents = 32(A-3)(A-2)','sample_target_counts':sample_counts,'nonmarked_sector':{'level_patterns':31,'source_families':['T','S_K'],'exact_A12_parity_seeds':248,'transport_components':248},'marked_sector':{'level_pattern':[1,1,2,1,1],'source_families':['T','S_K','Q'],'transport_components':8},'total_directed_components':components,'representative_independence':'Every nonempty contraction fiber modulo the exact source kernel is a singleton; commuting unchanged/x-square/y-square maps make the transported quotient class path-independent.','decision':'Every K-family p-normal derivative target has an exact rational source contraction at every even A>=12. The canonical object is its absorption class modulo source syzygies, not a coefficient word.','scope_boundary':'This is the full K-derivative family, not yet the complete IBP+K+q rank-26 derivative module. It proves absorption and supplies no surviving horn line.','next_gate':'establish exact arbitrary-degree absorption for the non-K derivative families, or isolate a surviving non-K target','limitations':['nonmarked exact closures selected using F_32003 pivot order with exact rational post-verification','no canonical representative word','no horn, Bockstein, contour, or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
