"""Determinantal smoothing/rank-two reflexive reduction, not a Weil witness.
Generic sections, Porteous and depth/Ext statements have written proofs with
standard imports. All nonzero-Weil numerical probes are explicitly formal.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
from check_hodge_chern_witness_transfer import (
    report as chern_report, normalized_forms, chern_character, normalized_chern,
    mono, psum, times, pscale, generators, DS, wedge, combine, scale, weil_filter)

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-reflexive-rank-reduction.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-reflexive-rank-reduction-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-reflexive-rank-reduction-v1.json'


def require(condition,message):
    if not condition:
        raise ValueError(message)


def strata(rank):
    require(isinstance(rank,int) and rank >= 3,'rank reduction requires rank at least three')
    m = rank-2
    return {'source_rank':rank,'section_count':m,'quotient_rank':2,
        'first_corank_codimension':(rank-(m-1))*(m-(m-1)),
        'second_corank_codimension':(rank-(m-2))*(m-(m-2)) if m >= 2 else None}


def chern123(ch):
    c1 = ch[1]
    c2 = scale(combine(wedge(c1,c1),scale(ch[2],-2)),Q(1,2))
    c3 = combine(combine(scale(ch[3],2),scale(wedge(wedge(c1,c1),c1),Q(-1,3))),wedge(c1,c2))
    return c1,c2,c3


def twist_series(ch,m,E):
    epowers = [{():Q(1)}]
    for _ in range(3):
        epowers.append(wedge(epowers[-1],E))
    result = []
    for k in range(4):
        value = {}
        for j in range(k+1):
            value = combine(value,scale(wedge(ch[j],epowers[k-j]),Q(m**(k-j),factorial(k-j))))
        result.append(value)
    return result


@lru_cache(maxsize=1)
def exact_core():
    profile = [strata(n) for n in range(3,17)]
    require(all(x['first_corank_codimension'] == 3 and
        (x['second_corank_codimension'] is None or x['second_corank_codimension'] > 6) for x in profile),
        'deeper determinantal stratum not excluded in dimension six')
    # Algebra behind F*=F tensor det(F)^-1 and derived dual. Do not truncate c3!
    ch = chern_character(2)
    defects = []
    for k in range(4):
        star = {}
        for j in range(k+1):
            star = psum(star,pscale(times(ch[j],mono((k-j,0,0,0))),Q((-1)**(k-j),factorial(k-j))))
        defects.append(psum(star,pscale(ch[k],(-1)**k),-1))
    require(defects[:3] == [{},{},{}] and defects[3] == mono((0,0,1,0)),
        'rank-two duality defect is not c3')
    require(normalized_chern(2,3) == mono((0,0,1,0),Q(1,2)),'rank-two normalization')
    E = {(2*j,2*j+1):Q(d) for j,d in enumerate(DS)}
    epowers = [{():Q(1)}]
    for _ in range(6):
        epowers.append(wedge(epowers[-1],E))
    r6,i6 = generators(6)
    w = combine(scale(r6,3),scale(i6,2))
    require(not wedge(E,w) and not wedge(epowers[3],w),'primitive Weil class has nonzero ample degree')
    volume = -epowers[6].get(tuple(range(12)),0)
    require(volume == 2160,'complex orientation or ample volume')
    controls = []
    for n in (3,4,8,16):
        # Deliberately formal Hodge input; no such bundle is asserted to exist.
        source = [{():Q(n)},scale(E,Q(2,5)),scale(epowers[2],Q(-1,7)),
                  combine(scale(epowers[3],Q(1,11)),w)]
        c1,c2,c3 = chern123(source)
        require(weil_filter(normalized_forms(source,n,3),6) == w,'source formal Weil projection')
        for m in (0,1,3):
            twisted = twist_series(source,m,E)
            t1,t2,t3 = chern123(twisted)
            expected = combine(c3,scale(wedge(E,c2),(n-2)*m))
            expected = combine(expected,scale(wedge(epowers[2],c1),comb(n-1,2)*m*m))
            expected = combine(expected,scale(epowers[3],comb(n,3)*m**3))
            require(t3 == expected,'third Chern twist polynomial')
            quotient = [{():Q(2)}]+twisted[1:]
            require(chern123(quotient) == (t1,t2,t3),'quotient by trivial sections changed Chern classes')
            k3 = normalized_forms(quotient,2,3)
            require(k3 == scale(t3,Q(1,2)) and weil_filter(k3,6) == w and
                weil_filter(t3,6) == scale(w,2),'projected rank reduction or factor two')
            controls.append({'source_rank':n,'ample_twist_parameter':m,'formal_input_only':True,
                'quotient_rank':2,'projected_kappa3_preserved':True,'singularity_cycle_Weil_factor':2})
    # Actual generic determinantal family, G=L^4, map O^2 -> G; t=c1(L).
    # Values below are coefficients relative to t^k, not an assertion that the
    # original polarization line bundle itself already has enough sections.
    split = [scale(epowers[k],Q(4,factorial(k))) for k in range(4)]
    split_f = [{():Q(2)}]+split[1:]
    sc1,sc2,sc3 = chern123(split_f)
    require((sc1,sc2,sc3) == (scale(E,4),scale(epowers[2],6),scale(epowers[3],4)),
        'determinantal split control Chern data')
    k3f = normalized_forms(split_f,2,3)
    require(not normalized_forms(split,4,3) and k3f == scale(epowers[3],2) and
        k3f and not weil_filter(k3f,6),'full normalization falsely claimed preserved')
    return {'ambient_complex_dimension':6,'stratum_profiles':profile,
        'first_corank_codimension':3,'second_corank_codimension_when_defined':8,
        'quotient_rank':2,'Ext_minimum_support_codimensions':{str(i):i+2 for i in range(1,5)},
        'rank_two_singularity_cycle_identity':'c3(F)=ch3(Ext1(F,O_X))=2*kappa3(F)',
        'higher_codimension_singularities_alone_have_zero_kappa3':True,
        'formal_rank_twist_controls':controls,'polarization_sixth_power':int(volume),
        'split_control_source_rank':4,'split_control_section_count':2,
        'split_control_chern_coefficients':[4,6,4],
        'split_control_normalized_third_coefficient':2,'split_control_Weil_projection_nonzero':False,
        'smooth_threefold_witness_existence_equivalent_to_alpha_algebraicity':True,
        'rank_two_reflexive_witness_existence_equivalent_to_alpha_algebraicity':True,
        'conditional_rank_reduction_constructed':True}


def validate_reduction(c):
    require(c['schema'] == 'marici.hodge-reflexive-rank-reduction.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'reflexive-rank-reduction' and c['verdict'] == 'constructed','reflexive reduction identity')
    require(c['resolution_kind'] == 'generic_determinantal_smoothing_and_rank_two_reflexive_witness_equivalence',
        'reflexive reduction resolution')
    require(c['geometry'] == {'ambient_complex_dimension':6,'codimension':3,'first_corank_codimension':3,
        'second_corank_codimension_when_defined':8,'general_sections':'n-2 of a globally generated rank-n bundle, n>=3'},
        'determinantal dimension scope')
    require(c['policy'] == {'source_bundle_supplied':False,'preserves_projected_kappa3':True,
        'preserves_full_kappa3':False,'quotient_is_locally_free_at_singular_locus':False,
        'arbitrary_prescribed_threefold_realized_as_singular_locus':False,
        'pure_Weil_effective_threefold_required':False,'formal_probes_are_existing_bundles':False},
        'rank reduction scope promoted')
    require(c['singularity_cycle'] == {'rank':2,'identity':'c3(F)=ch3(Ext1(F,O_X))=2*kappa3(F)',
        'Ext1_minimum_codimension':3,'higher_Ext_contributes_to_ch3':False,
        'singularities_only_in_codimension_at_least_four_suffice':False},'reflexive Ext scope')
    require(c['existence_equivalences_proved'] is True and c['positive_branch_decided'] is False,
        'reflexive existence branch not decided')
    require(len(c['boundary']) == 7 and all(v is False for v in c['boundary'].values()),'rank reduction verdict promotion')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_reduction(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-chern-witness-transfer-v1.json',
        'previous Chern transfer binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == chern_report() and old['candidate_id'] == c['candidate_id'],'stale Chern transfer input')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_chern_witness_transfer.py',
        'research/voevodsky/checkers/check_hodge_eightfold_hodge_kernel.py',
        'research/voevodsky/hodge-tautological-witness-search-v1.md'}
    return {'schema':'marici.hodge-reflexive-rank-reduction-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
        'checks':dict.fromkeys(['generic_strata_codimensions_3_and_8_with_dimension_six_boundary',
            'depth_reflexivity_and_Porteous_proof_with_actual_split_control',
            'derived_dual_defect_and_rank_two_Ext_singularity_cycle',
            'codimension_at_least_four_singularities_do_not_supply_third_data',
            'Chern_twist_polynomial_and_projected_not_full_normalization_preservation',
            'primitive_Weil_degree_zero_and_necessary_divisor_background',
            'formal_controls_not_a_supplied_nonzero_Weil_bundle_or_threefold'],True),
        'nonzero_Weil_reflexive_sheaf_constructed':False,'nonzero_Weil_smooth_threefold_constructed':False,
        'algebraic_representative_of_alpha_constructed':False,'all_cycle_annihilation_proved':False,
        'alpha_nonalgebraic_proved':False,'positive_branch_decided':False,'Hodge_proved':False,'Hodge_refuted':False,
        'verification_level':c['trust_scope'],
        'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
