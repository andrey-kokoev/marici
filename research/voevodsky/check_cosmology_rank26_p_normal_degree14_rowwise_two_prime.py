"""Aggregate the two degree-14 rowwise p-normal reduction certificates."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_degree14_rowwise_two_prime.json'
def main():
    certs={}
    for p in (32003,32009):
        x=json.loads((RES/f'cosmology_rank26_p_normal_rowwise_reduction_certificate_p{p}.json').read_text())
        assert x['passed'] and x['field']==p and x['ambient_relation_degree']==14
        assert x['rowwise_reduction']['nx']['zero_remainders']==29904
        assert x['rowwise_reduction']['ny']['zero_remainders']==29904
        assert x['rowwise_reduction']['nx']['nonzero_remainders']==x['rowwise_reduction']['ny']['nonzero_remainders']==0
        certs[str(p)]={'pivot_sha256':x['normalized_S_plus_T_pivot_sha256'],'special_rank':x['special_rank'],'S_plus_T_rank':x['S_plus_T_rank'],'T_over_S_rank':x['T_over_S_rank'],'nx_zero_remainders':29904,'ny_zero_remainders':29904}
    out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-degree14-rowwise-two-prime.v1','status':'all_59808_normal_rows_per_prime_reduce_to_zero_against_fixed_S_plus_T_basis','primes':[32003,32009],'certificates':certs,'total_rows_reduced_per_prime':59808,'nonzero_remainders_per_prime':0,'interpretation':'The degree-14 absorption is certified row-by-row against a fixed S+T basis; no nx or ny row is adjoined during reduction.','limitations':['reduction coefficients not retained','finite degree 14 only','no uniform chain homotopy'],'relative_bockstein_constructed':False,'physical_period_constructed':False,'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
