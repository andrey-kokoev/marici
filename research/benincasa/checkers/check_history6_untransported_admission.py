#!/usr/bin/env python3
"""Fresh full-normalization admission screen for history6's omitted update.

Reuses the read-only owner-library scanner, not the historical producer.
Same eta rows are checked independently for F0, so its exhaustive fermionic
candidate set is exactly the freshly scanned transported set.
"""
import json
from hashlib import sha256
from pathlib import Path
from check_history6_seed_admission import run, s, MATCHER
from check_history6_endpoint_boundary import coefficient, evaluate
ROOT=Path(__file__).resolve().parents[3]
ENDPOINT='research/benincasa/results/history6_endpoint_boundary.json'


def main():
    prior=json.loads((ROOT/ENDPOINT).read_text());assert prior['passed']
    for p,h in prior['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert prior['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_endpoint_boundary.py').read_bytes()).hexdigest()
    t=s.Symbol('t');c,_=coefficient(t)
    assert str(c)==prior['slice']['reduced_c']
    fixtures=[]
    for shift in (0,1,2):
        scan=run(shift)
        # evaluate checks endpoint-independent eta rows and every inner sparse
        # polynomial coefficient, including the full unupdated prefactor.
        endpoint=evaluate(shift,c,t);weight=s.Rational(endpoint['c'])
        assert weight==s.Rational(prior['runs'][shift]['c'])
        assert scan['evaluated']==320 and not scan['singular']
        matches=[]
        for m in scan['matches']:
            transported=s.Rational(m['transported_full_superfunction_ratio'])
            full=s.factor(weight*transported)
            assert full not in (1,-1)
            matches.append(m|{'untransported_full_superfunction_ratio':str(full),
                'untransported_numerator_rows_identical_to_transported':True,
                'unit_or_orientation_reversed_admission':False})
        assert len(matches)==6 and scan['distinct_matched_cell_keys']==1
        fixtures.append({'shift':shift,'candidate_embeddings':320,'nonsingular_evaluations':320,
            'singular_candidates':[],'fermionic_matches':matches,
            'transported_unit_positive_controls':len(matches),
            'untransported_unit_or_sign_admissions':0,'endpoint_coefficient':str(weight)})
    num,den=s.fraction(c)
    plus=s.factor(num-den);minus=s.factor(num+den)
    assert plus!=0 and minus!=0
    assert all(plus.subs(t,j)!=0 and minus.subs(t,j)!=0 for j in (0,1,2))
    paths=[ENDPOINT,MATCHER,'research/benincasa/checkers/check_history6_seed_admission.py',
        'research/benincasa/checkers/check_history6_endpoint_boundary.py',
        'research/benincasa/checkers/check_untransported_simple_root_seed_admission.py',
        'research/nima/dual_r_invariant.py','research/nima/nnmhv_coherence_paths.py']
    out={'schema':'marici.benincasa.history6-untransported-admission.v1',
        'history_index':6,'root':[2,2],'fixtures':fixtures,
        'symbolic_slice_unit_obstructions':{'c_minus_one_numerator':str(plus),'c_plus_one_numerator':str(minus),
            'localization':'Original endpoint/generalized-R domain retained; zero loci of these polynomials do not imply a generic canonical admission.'},
        'checks':{'fresh_960_nonsingular_owner_library_evaluations':True,
            'same_unupdated_eta_rows_and_all_inner_polynomial_scaling':True,
            'eighteen_transported_unit_embedding_controls':True,
            'one_fermionic_cell_per_fixture_six_cyclic_embeddings_not_six_cells':True,
            'zero_unit_or_orientation_reversed_untransported_matches':True,
            'symbolic_nonunit_and_non_sign_slice_obstructions':True},
        'passed':True,'verdict':'rejected_single_ordinary_rational_seed_admission_in_tested_owner_library',
        'claim_boundary':'Three exact nonsingular fixtures reject a generic F0=plus_or_minus_single_seed identity among all 320 order-preserving cyclic A-H embeddings. This is not rejection of coefficient-valued forms, sums, new pushforwards, or the weighted descent conjecture.',
        'boundary_implication':'The relative c6-weighted CZ corner square cannot be upgraded to ordinary canonical extraction merely by reusing the transported F chart or reversing its orientation. Physical spinor-to-bosonized boundary extraction remains unconstructed.',
        'excluded':['algebraic four-mass branch','multi-cell combinations','new pushforwards','coefficient-valued relative differential realization'],
        'next_action':'Analyze the source momentum-twistor endpoint coefficient as an external bosonized coefficient rather than fitting a unit seed: identify whether it has a GL(2)-invariant external extension and determine its restriction/poles on the actual target corner. Until that map is specified, keep relative differential and supercomponent extraction distinct.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_untransported_admission.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'evaluations':960,'admissions':0,'unit_obstructions':out['symbolic_slice_unit_obstructions'],
        'verdict':out['verdict'],'next_action':out['next_action']},indent=2))

if __name__=='__main__':main()
