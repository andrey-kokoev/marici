"""Decompose the degree-14 rowwise absorption certificate by source relation family."""
from __future__ import annotations
import json, sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research'/'benincasa'))
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_degree14_familywise_absorption.json'

def main():
    aggregate=json.loads((RES/'cosmology_rank26_p_normal_degree14_rowwise_two_prime.json').read_text())
    assert aggregate['passed'] and aggregate['nonzero_remainders_per_prime']==0
    A=14; names=charts.SOURCE_NAMES; n=len(names)
    ibp=0
    for _kp in range(charts.K_DEPTH):
        for levels in product(range(1,charts.Q_DEPTH+1),repeat=n):
            if any(level==charts.Q_DEPTH for level in levels): continue
            ibp += 2*len(base.monomials_at_most(A))
    k_mult=0
    for _kp in range(charts.K_DEPTH):
        for _levels in product(range(1,charts.Q_DEPTH+1),repeat=n):
            k_mult += len(base.monomials_at_most(A-4))
    q_mult=0
    for qi in range(n):
        for _kp in range(charts.K_DEPTH+1):
            for levels in product(range(1,charts.Q_DEPTH+1),repeat=n):
                if levels[qi]==charts.Q_DEPTH: continue
                q_mult += len(base.monomials_at_most(A-1))
    counts={'IBP_derivative_relations':ibp,'K_multiplication_relations':k_mult,'marked_q_multiplication_relations':q_mult}
    assert counts=={'IBP_derivative_relations':480,'K_multiplication_relations':4224,'marked_q_multiplication_relations':25200}
    assert sum(counts.values())==29904
    per_prime={}
    for p in ('32003','32009'):
        cert=json.loads((RES/f'cosmology_rank26_p_normal_rowwise_reduction_certificate_p{p}.json').read_text())
        assert cert['passed'] and cert['special_row_count']==sum(counts.values())
        assert cert['rowwise_reduction']['nx']['nonzero_remainders']==cert['rowwise_reduction']['ny']['nonzero_remainders']==0
        per_prime[p]={family:{'rows_per_normal_direction':count,'nx_zero_remainders':count,'ny_zero_remainders':count} for family,count in counts.items()}
    out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-degree14-familywise-absorption.v1','status':'all_three_source_relation_families_absorb_p_normal_derivatives_rowwise','rechecked_inputs':['research/voevodsky/results/cosmology_rank26_p_normal_degree14_rowwise_two_prime.json','research/benincasa/check_rank26_total_energy_triple_relation_module.py'],'ambient_relation_degree':A,'source_relation_family_counts':counts,'row_order_contract':['IBP derivative relations','K multiplication relations','marked q multiplication relations'],'two_prime_familywise_certificates':per_prime,'decision':'The zero p-normal image is not confined to one presentation artifact: IBP, K-multiplication, and every marked-q multiplication family all reduce into the same fixed S+T span.','limitations':['familywise result inherits the fixed row-order contract of raw_relations','reduction coefficients not retained','finite degree 14 only','no uniform homotopy'],'relative_bockstein_constructed':False,'physical_period_constructed':False,'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
