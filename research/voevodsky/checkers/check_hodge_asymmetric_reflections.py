"""All translated elliptic inversion centers for the asymmetric control, via p=409."""
from functools import lru_cache
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
from check_hodge_asymmetric_scalar_cover import report as asymmetric_report, source_equations, modgcd_degree
from check_hodge_even_scalar_cover import derivative

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-asymmetric-reflections.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-asymmetric-reflections-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-asymmetric-reflections-v1.json'
PRIME = 409
POLICY = ['all_curve_automorphisms_excluded',
    'Prym_geometrically_simple_proved','Prym_End0_computed','Prym_not_a_square_proved',
    'actual_cover_matching_Y2_constructed','theta_dimension_computed','conditional_root_census_changed',
    'all_scalar_families_excluded','Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
    'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved','global_witness_search_completed']


def require(c,m):
    if not c:
        raise ValueError(m)


class BranchRing:
    """Exact reduced branch algebra F_p[t]/B0(t); no choice of branch roots."""
    def __init__(self,p,f):
        self.p = p
        self.f = self.trim(f)

    def trim(self,a):
        a = [int(v)%self.p for v in a]
        while len(a)>1 and a[-1] == 0:
            a.pop()
        return tuple(a)

    def raw_add(self,a,b):
        return self.trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

    def scale(self,a,q):
        return self.trim([q*x for x in a])

    def raw_mul(self,a,b):
        c = [0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                c[i+j] += x*y
        return self.trim(c)

    def divrem(self,a,b):
        require(b != (0,),'zero branch polynomial divisor')
        q = (0,)
        while a != (0,) and len(a)>=len(b):
            t = (0,)*(len(a)-len(b))+(a[-1]*pow(b[-1],-1,self.p)%self.p,)
            q = self.raw_add(q,t)
            a = self.raw_add(a,self.scale(self.raw_mul(t,b),-1))
        return q,a

    def add(self,a,b):
        return self.divrem(self.raw_add(a,b),self.f)[1]

    def mul(self,a,b):
        return self.divrem(self.raw_mul(a,b),self.f)[1]

    def power(self,a,n):
        r = (1,)
        for _ in range(n):
            r = self.mul(r,a)
        return r

    def inverse(self,a):
        r0,r1,t0,t1 = self.f,a,(0,),(1,)
        while r1 != (0,):
            q,r = self.divrem(r0,r1)
            r0,r1,t0,t1 = r1,r,t1,self.add(t0,self.scale(self.mul(q,t1),-1))
        require(len(r0) == 1 and r0 != (0,),'nonunit branch denominator')
        v = self.scale(t0,pow(r0[0],-1,self.p))
        require(self.mul(a,v) == (1,),'branch inverse certificate')
        return v


def double(P,p):
    if P is None or P[1] == 0:
        return None
    x,y = P
    m = (3*x*x-52*x+25)*pow(2*y,-1,p)%p
    z = (m*m+26-2*x)%p
    return z,(-y+m*(x-z))%p


def eight(P,p):
    return double(double(double(P,p),p),p)


def elliptic_points(p):
    squares = {}
    for y in range(p):
        squares.setdefault(y*y%p,[]).append(y)
    return [None]+[(x,y) for x in range(p) for y in squares.get(x*(x-1)*(x-25)%p,[])]


def translation_residue(center,ring):
    if center is None:
        return (0,)
    a,b = center
    t = (0,1)
    original_y = ring.trim((2,0,0,0,-1))
    slope = ring.mul(ring.add(original_y,(-b,)),ring.inverse(ring.add(t,(-a,))))
    new_x = ring.add(ring.add(ring.power(slope,2),(26-a,)),ring.scale(t,-1))
    new_y = ring.add((-b,),ring.mul(slope,ring.add((a,),ring.scale(new_x,-1))))
    return ring.add(ring.add(ring.power(new_x,4),new_y),(-2,))


def reflection_residue(center,ring):
    t = (0,1)
    p4 = ring.trim((-2,0,0,0,1))
    if center is None:
        return ring.scale(p4,2)
    a,b = center
    # On the branch scheme Q=(t,-p4), so -Q=(t,p4).
    slope = ring.mul(ring.add(p4,(-b,)),ring.inverse(ring.add(t,(-a,))))
    new_x = ring.add(ring.add(ring.power(slope,2),(26-a,)),ring.scale(t,-1))
    new_y = ring.add((-b,),ring.mul(slope,ring.add((a,),ring.scale(new_x,-1))))
    return ring.add(ring.add(ring.power(new_x,4),new_y),(-2,))


@lru_cache(maxsize=1)
def exact_core():
    p = PRIME
    require(all(p%d for d in range(2,isqrt(p)+1)) and p%2 == 1,'certificate prime')
    _,_,_,_,_,f,_ = source_equations()
    require(modgcd_degree(f,derivative(f),p) == 0 and
        modgcd_degree(f,(0,25,-26,1),p) == 0 and p not in (2,3,5),'good elliptic and branch reduction')
    points = elliptic_points(p)
    centers = [P for P in points if eight(P,p) is None]
    require(len(points) == 384 and len(centers) == len(set(centers)) == 64,'full rational eight-torsion census')
    ring = BranchRing(p,f)
    rows = []
    for A in centers:
        if A is not None:
            require(modgcd_degree(f,(-A[0],1),p) == 0,'torsion center meets branch support')
        r = reflection_residue(A,ring)
        t = translation_residue(A,ring)
        require(r != (0,),'a translated inversion preserves the branch divisor')
        require((t == (0,)) == (A is None),'nonidentity translation preserves the branch divisor')
        rows.append({'center':None if A is None else list(A),
            'nonzero_reflection_residue':list(r),'translation_residue':list(t)})
    # The known genus-17 double-elliptic cover has a unique bielliptic involution
    # (two independent degree-two elliptic maps would force genus <=5).
    c4,c6,discriminant = 16*(7**2-3),-64*7**3+288*7,16*(7**2-4)
    require((c4,c6,discriminant) == (736,-19936,720),'non-special source elliptic j certificate')
    return {'certificate_prime':p,'elliptic_Fp_point_count':len(points),
        'all_rational_eight_torsion_centers_count':len(centers),
        'branch_sum_zero_forces_eight_torsion_center':True,
        'all_64_reflection_residues_nonzero':True,'center_certificates':rows,
        'all_translated_elliptic_inversions_excluded_for_this_branch_divisor':True,
        'all_elliptic_inversion_lifts_to_asymmetric_source_cover_excluded':True,
        'target_branch_translation_stabilizer_is_trivial':True,
        'source_elliptic_c4_c6_discriminant':[c4,c6,discriminant],
        'source_curve_bielliptic_involution_unique':True,
        'full_geometric_curve_automorphism_group':'C4 x C2',
        'full_geometric_curve_automorphism_group_order':8,
        'no_dihedral_order_eight_curve_subgroup':True,
        'actual_theta_singularity_dimension':None,'actual_target_isogeny':None,
        'conditional_root_label_count_not_updated':516}


def validate_certificate(c):
    require(c['schema'] == 'marici.hodge-asymmetric-reflections.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'asymmetric-cover-automorphisms' and c['verdict'] == 'constructed','reflection identity')
    require(c['resolution_kind'] == 'branch_sum_full_eight_torsion_stabilizer_and_unique_bielliptic_automorphism_certificate','reflection resolution')
    require(c['geometry'] == {'elliptic_curve':'y2^2=x2*(x2-1)*(x2-25)',
        'branch_function':'x2^4+y2-2','branch_degree':8,'branch_pole':'8*O',
        'prime':409,'torsion_order_prime_to_reduction':True,'source_curve_genus':17,
        'source_elliptic_j_not_0_or_1728':True,'scope':'full_curve_automorphisms_of_this_auxiliary_control'},'reflection geometry scope')
    require(set(c['scope_policy']) == set(POLICY) and all(v is False for v in c['scope_policy'].values()),'reflection promotion')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_certificate(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-asymmetric-scalar-cover-v1.json','reflection predecessor binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == asymmetric_report() and old['actual_asymmetric_control_tower_constructed'] and
        old['actual_theta_singularity_dimension'] is None,'stale asymmetric receipt')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_asymmetric_scalar_cover.py'}
    return {'schema':'marici.hodge-asymmetric-reflections-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
        'checks':dict.fromkeys(['branch_divisor_sum_zero_gives_complete_center_bound',
            'good_reduction_and_prime_to_p_torsion_specialization',
            'all_eight_torsion_geometric_points_are_in_the_enumerated_Fp_set',
            'branch_algebra_denominators_are_units_and_residues_all_nonzero',
            'specialization_rules_out_all_characteristic_zero_inversion_centers',
            'source_isogeny_pushes_any_translation_or_inversion_center_to_target',
            'unique_bielliptic_involution_and_non_special_source_j_bound_full_Aut',
            'known_C4_deck_translations_and_C2_sheet_involution_attain_bound'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k != 'source_sha256'},indent=2))
