"""Assemble exact IBP, K, and q results into the full rank-26 theorem."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research'/'voevodsky'/'results';OUT=V/'cosmology_full_rank26_characteristic_zero_absorption.json'
def load(n):return json.loads((V/n).read_text())
def counts(A):
 ibp=2*(A+1)*(A+2);k=32*(A-3)*(A-2);q=120*A*(A+1)
 return {'IBP':ibp,'K':k,'q':q,'total':ibp+k+q}
def main():
 ibp=load('cosmology_IBP_corrected_transport_exact_seeds_a12.json');k=load('cosmology_full_K_characteristic_zero_absorption.json');q=load('cosmology_q_exact_seeds_a12.json');assert all(x['passed'] for x in (ibp,k,q));assert ibp['targets_verified']==16 and q['targets_verified']==960 and k['total_directed_components']==256
 samples={str(A):counts(A) for A in (12,14,16,18,20)};assert samples['14']['total']==29904
 out={'schema':'marici.voevodsky.cosmology-full-rank26-characteristic-zero-absorption.v2','status':'complete_rank26_relation_family_absorption_exact_for_all_even_A_at_least_12','ambient_degrees':'all even A>=12','family_count_formulas':{'IBP':'2(A+1)(A+2)','K':'32(A-3)(A-2)','q':'120A(A+1)','total':'154A^2-34A+196'},'sample_counts':samples,'exact_sources':{'IBP':'T only; 16 A12 parity seeds plus derivative-level square transport','K':'T+S_K for nonmarked and T+S_K+Q for marked; 256 transport components','q':'T+Q only; 960 integral A12 parity seeds'},'decision':'Every source relation in the complete rank-26 IBP+K+q presentation has zero p-normal derivative class modulo exact source relations over Q for every even A>=12.','supported_DNC_comparison':{'status':'unverified','required':['named supported target complex','chain map from the rank26 derivative presentation','support-localization map','differential-commutation check','factorization check'],'consequence':'No DNC-image or horn obstruction is emitted by this aggregate.'},'scope_boundary':'This is a relation-presentation absorption theorem only. It does not establish a geometric DNC comparison, supported Xi projection, horn obstruction, source enlargement, Bockstein, contour, or physical period.','next_gate':'construct and verify the typed rank26-to-exceptional-supported DNC comparison','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
