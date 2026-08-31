"""Locate the exact remaining gap in a full characteristic-zero DNC absorption theorem."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; V=ROOT/'research'/'voevodsky'/'results'; OUT=V/'cosmology_DNC_full_family_factorization_gate.json'
def load(n):return json.loads((V/n).read_text())
def main():
 nec=load('cosmology_rank26_p_normal_K_family_necessity.json');census=load('cosmology_rank26_p_normal_K_residual_census.json');unb=load('cosmology_rank26_p_normal_unbounded_quotient_colimit_gate.json');law=load('cosmology_rank26_p_normal_uniform_constructor_law.json');assert all(x['passed'] for x in [nec,census,unb,law])
 core=nec['candidates']['T_plus_S_K']['target_nx_K'];assert core['rows']==4224 and core['absorbed']==4092 and core['nonabsorbed']==132
 c=census['censuses']['T_plus_S_K'];assert c['nonabsorbed_rows']==132 and c['distinct_level_patterns']==1 and c['level_patterns'][0]['levels']==[1,1,2,1,1]
 out={'schema':'marici.voevodsky.cosmology-DNC-full-family-factorization-gate.v1','status':'full_unbounded_factorization_reduced_to_exact_nonmarked_core_seed_problem','degree14_decomposition':{'total_K_derivative_rows':4224,'T_plus_S_K_absorbed_mod_32003':4092,'marked_residual_rows':132,'marked_residual_level':[1,1,2,1,1]},'proved_unbounded_part':'the entire marked residual family has exact rational contractions and a canonical quotient-class colimit for every even A>=12','remaining_part':'the 4092 nonmarked rows are known to lie in T+S_K only by finite-field degree-14 containment in the cited family census; no complete exact rational seed family or arbitrary-degree contraction theorem has been materialized','constructor_status':'uniform source-constructor naturality can transport exact identities once seeds exist, but cannot replace seed existence','decision':'A full characteristic-zero DNC absorption theorem is not yet established. Its only remaining K-family gap is exact nonmarked T+S_K seed existence and coverage.','next_gate':'census nonmarked rows by level/pole/exponent orbit, exact-solve one seed per natural orbit over Q, then prove monomial-shift coverage','limitations':['classification uses the degree-14 F_32003 census for the unresolved core','does not promote modular containment to characteristic zero','no horn, Bockstein, or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
