"""Census natural monomial-square orbits of the nonmarked K-derivative core."""
from __future__ import annotations
import json
from itertools import product
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; V=ROOT/'research'/'voevodsky'/'results'; OUT=V/'cosmology_nonmarked_K_orbit_census.json'
def exponents(max_degree):return [(i,d-i) for d in range(max_degree+1) for i in range(d+1)]
def main():
 levels=list(product((1,2),repeat=5));marked=(1,1,2,1,1);nonmarked=[x for x in levels if x!=marked];exps=exponents(10)
 desc=[(kp,lv,e) for kp in range(2) for lv in nonmarked for e in exps]
 assert len(levels)==32 and len(nonmarked)==31 and len(exps)==66 and len(desc)==4092
 orbits=Counter((kp,lv,(e[0]%2,e[1]%2)) for kp,lv,e in desc)
 assert len(orbits)==2*31*4 and set(orbits.values())=={15,21}
 seeds=[(kp,lv,par) for kp in range(2) for lv in nonmarked for par in product((0,1),repeat=2)]
 assert len(seeds)==248 and all(sum(par)<=2 for _,_,par in seeds)
 out={'schema':'marici.voevodsky.cosmology-nonmarked-K-orbit-census.v1','status':'4092_nonmarked_rows_reduce_to_248_square_monomial_seed_orbits','ambient_degree_censused':14,'level_patterns_total':32,'excluded_marked_level':list(marked),'nonmarked_level_patterns':31,'K_poles':2,'exponents_degree_at_most_10':66,'nonmarked_rows':len(desc),'natural_orbit_key':'(K pole, five-level pattern, exponent parity pair)','orbit_count':len(orbits),'orbit_sizes':{str(k):v for k,v in sorted(Counter(orbits.values()).items())},'minimal_seed_exponents':[[0,0],[0,1],[1,0],[1,1]],'exact_rational_seed_systems_required':len(seeds),'coverage_statement':'Once one exact T+S_K identity exists for each of the 248 parity seeds at A12, unchanged and axis-square natural maps reach every nonmarked K target at every even A>=12.','decision':'The unresolved 4092-row modular core is reduced to 248 exact rational seed existence tests; no modular membership is promoted.','next_gate':'exact-solve the 248 A12 nonmarked parity seeds over Q and record true failures/denominators','limitations':['orbit reduction uses the already proved constructor naturality','does not establish any of the 248 exact seed identities','does not exploit possible symmetries between level patterns or poles'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
