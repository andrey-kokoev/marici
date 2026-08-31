"""Audit every currently materialized candidate for a sourced surviving p-normal quotient line."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research';OUT=RES/'voevodsky'/'results'/'cosmology_rank26_p_normal_surviving_line_candidate_gate.json'
def load(p):return json.loads((RES/p).read_text())
def main():
 tau=load('voevodsky/results/cosmology_tau_source_map_contract.json');c=load('voevodsky/results/cosmology_c_kernel_p_normal_mismatch.json');absorb=load('voevodsky/results/cosmology_rank26_p_normal_absorption_not_tautological.json');unbounded=load('voevodsky/results/cosmology_rank26_p_normal_unbounded_quotient_colimit_gate.json');prior=load('nima/results/cosmology_p_normal_rank26_relation_bockstein_prior_art.json')
 assert tau['current_source_generators_matching_contract']==[] and c['rank_of_p_and_c_covectors']==2 and unbounded['passed'] and prior['typing_restrictions']
 witnesses=absorb['two_prime_degree_witnesses'];assert all(all(v['common_normal_image_zero_mod_special_plus_tangent'] for v in ps.values()) for ps in witnesses.values())
 candidates=[
 {'candidate':'abstract tau_p','source_admissible':False,'survives':None,'disposition':'no source object or chain map; importing it would be circular'},
 {'candidate':'retained c-kernel','source_admissible':True,'survives':None,'disposition':'not p-normal: covectors have rank 2'},
 {'candidate':'rank-26 nx/ny common normal image','source_admissible':True,'survives':False,'disposition':'zero modulo S+T at every tested degree/two primes; marked K residual has unbounded exact absorption class'},
 {'candidate':'total-energy Rees class','source_admissible':True,'survives':None,'disposition':'different normal sector; p=0 test point has nonzero total energy and transfer is forbidden'},
 {'candidate':'gamma-normal Bockstein vector','source_admissible':True,'survives':None,'disposition':'different normal sector; only algorithm transfers'},
 ]
 assert not any(x['source_admissible'] and x['survives'] is True for x in candidates)
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-surviving-line-candidate-gate.v1','status':'no_currently_materialized_candidate_is_a_sourced_surviving_p_normal_line','candidates':candidates,'required_new_source':'resolved/Rees exceptional object, logarithmic Cech-de Rham cone cell, or Cayley-Menger/relative-face cone with chain map and primitive integral differential column (1,1)','decision':'The present candidate domain is exhausted: admissible p-normal images are absorbed, while nonabsorbed named classes are unsourced or belong to different normal sectors.','limitations':['does not prove that no new relative-face source object can exist','full unbounded characteristic-zero theorem was proved only for the marked K residual','no horn or Bockstein is constructed'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
