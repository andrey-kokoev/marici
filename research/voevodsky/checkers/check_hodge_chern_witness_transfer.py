"""Rank-sensitive higher-Chern witness audit. Formal probes are not bundles.
The actual singular-sheaf control is licensed by Bertini, Koszul and depth in
its written note; no nonzero Weil source is manufactured by this computation.
"""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
from check_hodge_eightfold_hodge_kernel import (
    report as kernel_report, exceptional_projector, channels, insertion, generators,
    DIVISORS, wedge, combine, scale, DS, weil_filter)

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-chern-witness-transfer.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-chern-witness-transfer-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-chern-witness-transfer-v1.json'
ZERO = (0,0,0,0)


def require(condition,message):
    if not condition:
        raise ValueError(message)


def mono(exponents,coefficient=1):
    return {tuple(exponents):Q(coefficient)} if coefficient else {}


def psum(a,b,factor=1):
    result = dict(a)
    for s,v in b.items():
        result[s] = result.get(s,Q(0))+factor*v
    return {s:v for s,v in result.items() if v}


def times(a,b):
    result = {}
    for s,v in a.items():
        for t,w in b.items():
            key = tuple(x+y for x,y in zip(s,t))
            if sum((j+1)*x for j,x in enumerate(key)) <= 4:
                result[key] = result.get(key,Q(0))+v*w
    return {s:v for s,v in result.items() if v}


def pscale(a,c):
    return {s:v*c for s,v in a.items() if v*c}


def power(a,n):
    result = mono(ZERO)
    for _ in range(n):
        result = times(result,a)
    return result


def chern_character(rank):
    require(isinstance(rank,int) and rank > 0,'positive integral bundle rank required')
    return [mono(ZERO,rank),mono((1,0,0,0)),
        psum(mono((2,0,0,0),Q(1,2)),mono((0,1,0,0),-1)),
        psum(psum(mono((3,0,0,0),Q(1,6)),mono((1,1,0,0),Q(-1,2))),mono((0,0,1,0),Q(1,2))),
        psum(psum(psum(psum(mono((4,0,0,0),Q(1,24)),mono((2,1,0,0),Q(-1,6))),
            mono((0,2,0,0),Q(1,12))),mono((1,0,1,0),Q(1,6))),mono((0,0,0,1),Q(-1,6)))]


def normalized_chern(rank,degree):
    ch = chern_character(rank)
    result = {}
    for i in range(degree+1):
        result = psum(result,pscale(times(ch[i],mono((degree-i,0,0,0))),
            Q((-1)**(degree-i),rank**(degree-i)*factorial(degree-i))))
    return result


def locally_free_restriction(poly,rank):
    # This is NOT licensed for a coherent/reflexive sheaf just by its rank.
    return {s:v for s,v in poly.items() if not any(s[rank:])}


def normalized_forms(ch,rank,degree):
    """Cohomological normalization for a supplied formal Chern-character series."""
    require(ch[0] == {():Q(rank)} and rank > 0,'wrong formal series rank')
    result,powers = {},[{():Q(1)}]
    for k in range(1,degree+1):
        powers.append(wedge(powers[-1],scale(ch[1],Q(-1,rank))))
    for i in range(degree+1):
        result = combine(result,scale(wedge(ch[i],powers[degree-i]),Q(1,factorial(degree-i))))
    return result


@lru_cache(maxsize=1)
def exact_core():
    for rank in range(1,17):
        k3,k4 = normalized_chern(rank,3),normalized_chern(rank,4)
        require(k3.get((0,0,1,0)) == Q(1,2),'projected third Chern coefficient')
        require(k4.get((1,0,1,0),Q(0)) == Q(rank-3,6*rank) and
                k4.get((0,0,0,1)) == Q(-1,6),'exceptional fourth Chern coefficients')
        if rank <= 2:
            require(not locally_free_restriction(k3,rank),'low-rank locally free third Chern hostile')
        if rank <= 3:
            k2 = locally_free_restriction(normalized_chern(rank,2),rank)
            require(locally_free_restriction(k4,rank) == pscale(times(k2,k2),Q(1,12)),
                    'rank at most three normalized fourth identity')
    # Actual Koszul rank-two reflexive control: ch(F)=3 exp(-2t)-exp(-3t).
    fch = [Q(3*(-2)**k-(-3)**k,factorial(k)) for k in range(5)]
    fk3 = sum(fch[i]*Q(3,2)**(3-i)/factorial(3-i) for i in range(4))
    c1 = fch[1]
    c2 = (c1*c1-2*fch[2])/2
    c3 = (6*fch[3]-c1**3+3*c1*c2)/3
    require(fch[0] == 2 and (c1,c2,c3,fk3) == (-3,3,1,Q(1,2)),
            'rank-two reflexive control incorrectly truncated')
    ideal = [Q(3*(-1)**k-3*(-2)**k+(-3)**k,factorial(k)) for k in range(4)]
    require(ideal == [1,0,0,-1],'rank-one non-reflexive ideal control')
    E = {(2*j,2*j+1):Q(d) for j,d in enumerate(DS)}
    epowers = [{():Q(1)}]
    for _ in range(4):
        epowers.append(wedge(epowers[-1],E))
    require(epowers[3] and not weil_filter(scale(epowers[3],Q(1,2)),6),
            'actual singular control falsely called a Weil witness')
    r6,i6 = generators(6)
    w = combine(scale(r6,2),scale(i6,-3))
    require(not wedge(E,w),'source Weil plane is not primitive')
    records = []
    for n in (3,4,5,8,16,32):
        # Arbitrary formal Hodge character, NOT an asserted bundle on X.
        source = [{():Q(n)},scale(E,Q(2,3)),scale(epowers[2],Q(-1,5)),
                  combine(scale(epowers[3],Q(1,7)),w),scale(epowers[4],Q(3,11))]
        require(weil_filter(normalized_forms(source,n,3),6) == w,'formal source normalized third probe')
        twisted = [source[0]]+[combine(source[k],wedge(source[k-1],DIVISORS[0])) for k in range(1,5)]
        require(not exceptional_projector(normalized_forms(twisted,n,4)),
                'twisting alone manufactured normalized fourth witness')
        enlarged = list(twisted)
        enlarged[0] = {():Q(n+1)}
        value = exceptional_projector(normalized_forms(enlarged,n+1,4))
        expected = insertion(scale(w,Q(1,n+1)),0)
        require(value == expected and channels(value)[0] == scale(w,Q(1,n+1)) and
                not any(channels(value)[1:]),'direct-sum normalization transfer factor')
        require(not weil_filter(value,8),'old P8 is not blind to this transfer sector')
        records.append({'source_rank':n,'target_rank':n+1,'formal_input_only':True,
                        'exceptional_transfer_factor':str(Q(1,n+1)),'old_P8_image_nonzero':False})
    return {'formal_rank_identity_controls':16,'source_locally_free_rank_lower_bound':3,
        'target_normalized_fourth_locally_free_rank_lower_bound':4,
        'projected_kappa3_c3_coefficient':'1/2',
        'projected_kappa4_coefficients':{'c1_c3':'(rank-3)/(6*rank)','c4':'-1/6'},
        'reflexive_control_rank':2,'reflexive_control_chern_coefficients':[-3,3,1],
        'reflexive_control_normalized_third_coefficient':str(fk3),
        'reflexive_control_Weil_projection_nonzero':False,
        'rank_one_ideal_normalized_third_coefficient':'-1',
        'conditional_transfer_controls':records,'conditional_bundle_transfer_constructed':True,
        'normalized_fourth_existence_equivalent_to_alpha_algebraicity':True}


def validate_transfer(c):
    require(c['schema'] == 'marici.hodge-chern-witness-transfer.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'higher-chern-witness-transfer' and c['verdict'] == 'constructed','Chern transfer identity')
    require(c['resolution_kind'] == 'rank_sensitive_normalized_Chern_audit_and_conditional_bundle_transfer',
        'Chern transfer resolution')
    require(c['rank_policy'] == {'X_locally_free_kappa3_minimum_possible_rank':3,
        'A_locally_free_exceptional_kappa4_minimum_possible_rank':4,
        'bounds_apply_to_arbitrary_reflexive_sheaves':False,'normalization_is_additive':False},'Chern rank policy')
    require(c['transfer'] == {'input':'supplied algebraic bundle G on X of rank n with nonzero P6 kappa3(G)',
        'construction':'H=(pX*G tensor pB*M) direct_sum O_A, c1(M)=D1',
        'target_rank':'n+1','exceptional_factor':'1/(n+1)',
        'tensor_twist_alone_suffices':False,'input_bundle_supplied':False,
        'rank_four_witness_guaranteed':False},'conditional bundle transfer scope')
    require(c['singular_control'] == {'kind':'rank-two reflexive, not locally free along a smooth codimension-three complete intersection',
        'construction':'0 -> L^-3 -> (L^-2)^3 -> F -> 0; L sufficiently ample',
        'kappa3':'c1(L)^3/2','nonzero_Weil_projection':False,
        'sections_numerically_supplied':False},'singular control scope')
    require(c['projected_formulas'] == {'X':'P6 kappa3(G)=P6 c3(G)/2',
        'A':'Pi_exc kappa4(H)=(rank(H)-3)/(6*rank(H))*Pi_exc(c1(H)c3(H))-Pi_exc(c4(H))/6',
        'low_rank_identity':'For locally free rank at most three, kappa4=kappa2^2/12; this has zero exceptional projection on the fixed A.'},'projected Chern formula binding')
    require(c['equivalence_proved'] is True and c['equivalence_branch_decided'] is False,'Chern existence branch not decided')
    require(len(c['boundary']) == 7 and all(v is False for v in c['boundary'].values()),'Chern transfer promoted')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_transfer(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-eightfold-hodge-kernel-v1.json','previous Hodge kernel binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == kernel_report() and old['candidate_id'] == c['candidate_id'],'stale Hodge kernel input')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_eightfold_hodge_kernel.py',
        'research/voevodsky/hodge-tautological-witness-search-v1.md',
        'research/voevodsky/checkers/check_hodge_eightfold_weil_filter.py',
        'research/voevodsky/checkers/check_hodge_split_eightfold_stabilization.py'}
    return {'schema':'marici.hodge-chern-witness-transfer-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
        'checks':dict.fromkeys(['exact_Newton_and_normalization_identities',
            'locally_free_rank_bounds_not_reflexive_sheaf_bounds',
            'Bertini_Koszul_depth_control_has_nonzero_kappa3_but_zero_Weil_projection',
            'normalization_not_additive_and_tensor_twist_alone_fails',
            'explicit_direct_sum_transfer_with_correct_n_plus_one_denominator',
            'four_channel_detection_and_old_P8_blind_sector',
            'existence_equivalence_without_a_supplied_nonzero_Weil_bundle'],True),
        'nonzero_Weil_bundle_constructed':False,'algebraic_representative_of_alpha_constructed':False,
        'all_cycle_annihilation_proved':False,'alpha_nonalgebraic_proved':False,
        'equivalence_branch_decided':False,'all_reflexive_sheaf_routes_excluded':False,
        'Hodge_proved':False,'Hodge_refuted':False,'verification_level':c['trust_scope'],
        'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
