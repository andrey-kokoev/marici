"""Source-scoped Schoen audit and exact secant arithmetic; no target cycle."""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-eightfold-literature-audit.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-eightfold-literature-audit-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-eightfold-literature-audit-v1.json'
SNAPSHOT = ROOT/'research/voevodsky/inputs/hodge-eightfold-literature-v1/sources.json'
SNAPSHOT_SHA = 'a1c1ee7b75d52bb75b600c5327482c49eea577251979008e6ebb0101d6592800'
POLICY = ['author_confirmed_erratum', 'secant_semiregularity_proved',
    'question_11_4_used_as_theorem', 'actual_target_cover_constructed',
    'target_matching_from_signature_only', 'ramified_trigonal_theorem_imported',
    'cyclic_action_transported_by_triality_assumed',
    'elliptic_degrees_preserved_under_arbitrary_isogenies',
    'actual_theta_dimension_computed', 'exceptional_cycle_on_target_constructed',
    'Hodge_proved', 'Hodge_refuted', 'all_cycle_annihilation_proved',
    'global_witness_search_completed']


def require(c, m):
    if not c:
        raise ValueError(m)


def source_paths():
    data = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
    return {SNAPSHOT.relative_to(ROOT).as_posix()} | {
        f['path'] for s in data['sources'] for f in s['files']}


def validate_sources():
    require(sha256(SNAPSHOT.read_bytes()).hexdigest() == SNAPSHOT_SHA, 'literature manifest drift')
    data = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
    for s in data['sources']:
        for f in s['files']:
            p = (ROOT/f['path']).resolve()
            require(p.is_relative_to(ROOT) and sha256(p.read_bytes()).hexdigest() == f['sha256'],
                    'literature source drift')
    base = SNAPSHOT.parent
    # Retain the original extractor bytes; scope anchors below are ASCII.
    schoen = (base/'schoen-1988.txt').read_text(encoding='latin-1')
    markman = (base/'markman-pp20-22.txt').read_text(encoding='latin-1')
    require('THEOREM 2.0:' in schoen and 'CORROLLARY 3.1:' in schoen and
            'simplicity hypothesis is automatically satisfied' in schoen, 'Schoen source scope')
    require('Question 11.4.' in markman and 'It is yet to be checked' in markman and
            'partial normalization' in markman, 'Markman unresolved source scope')


def secant_character(d, twist, normalized=True):
    require(type(d) is int and d >= 3 and d % 2 == 1, 'odd secant parameter')
    require(type(twist) is int and type(normalized) is bool, 'twist and normalization types')
    n = (d+9)//2
    nodes = (d+9)*(2*d-1)
    # n surfaces; n adjacent curves; n(n-3)/2 nonadjacent pairs;
    # n consecutive triples. Top intersections are 24 point classes.
    z4 = Q(7*n,12)+Q(3*n,2)-Q(n*(n-3),2)+n
    if normalized:
        z4 += Q(nodes,24)
    base = [Q(1), Q(0), Q(-n), Q(2*n), -z4]
    exp = [Q(twist**i, factorial(i)) for i in range(5)]
    return [sum((base[j]*exp[i-j] for j in range(i+1)), Q(0)) for i in range(5)]


def in_secant_plane(ch, d):
    require(type(d) is int and d > 0 and len(ch) == 5, 'secant plane inputs')
    # For a exp(s*t)+b exp(-s*t), s^2=-d, coefficients obey this recurrence.
    return all(Q(ch[k+2]) == -Q(d)*Q(ch[k])/((k+1)*(k+2)) for k in range(3))


def cyclic_genera(bottom, monodromies):
    require(type(bottom) is int and bottom >= 2 and
            tuple(monodromies) == (1,3), 'paired fully ramified quartic branches')
    # RH for degree four, and for each intermediate degree-two map.
    top = (4*(2*bottom-2)+6+2)//2
    middle = (2*(2*bottom-2)+2+2)//2
    require(2*top-2 == 2*(2*middle-2)+2, 'top double ramification')
    return [top, middle, bottom]


def validate_audit(c):
    require(c['schema'] == 'marici.hodge-eightfold-literature-audit.v1' and
            c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
            c['node'] == 'eightfold-literature-and-secant-audit' and
            c['sources'] == SNAPSHOT.relative_to(ROOT).as_posix(), 'literature identity')
    require(c['geometry'] == {'field':'Q(i)', 'secant_d':9, 'displayed_twist':1,
        'proposed_corrected_twist':3,
        'correction_status':'independent_arithmetic_correction_not_author_erratum',
        'secant_rank_convention':'[O]-[nu_*O_Ztilde]', 'ramified_bottom_genus':4,
        'branch_monodromies':[1,3], 'primitive_multiplicity':8}, 'literature geometry')
    require(set(c['scope_policy']) == set(POLICY) and
            all(v is False for v in c['scope_policy'].values()), 'literature promotion')
    require([(x['id'],x['status']) for x in c['research_queue']] == [
        ('corrected-secant-deformation','open'),
        ('ramified-generalized-prym-matching','open'),
        ('ramified-trigonal-primary-verification','pending_primary_verification')] and
        all(x['requires'] for x in c['research_queue']), 'research queue promotion')
    validate_sources()
    for d in range(3, 42, 2):
        corrected = secant_character(d, 3)
        require(corrected == [Q(1), Q(3), Q(-d,2), Q(-d,2), Q(d*d,24)] and
                in_secant_plane(corrected,d), 'corrected character')
        require(not in_secant_plane(secant_character(d,1),d) and
                not in_secant_plane(secant_character(d,3,False),d), 'negative character controls')
    require(cyclic_genera(4,[1,3]) == [16,8,4], 'ramified tower arithmetic')
    return {'source_snapshot_verified':True, 'secant_character_controls':True,
            'displayed_twist_negative_control':True, 'normalization_negative_control':True,
            'ramified_Riemann_Hurwitz':True, 'scope_and_open_queue':True}


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    checks = validate_audit(c)
    names = source_paths() | {CONTRACT.relative_to(ROOT).as_posix(), NOTE.relative_to(ROOT).as_posix(),
                             Path(__file__).relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-eightfold-literature-result.v1', 'passed':True,
        'candidate_id':c['candidate_id'], 'node':c['node'], 'verdict':'constructed',
        'verification_level':'Retained source-scope audit and exact arithmetic; no target-cycle or deformation proof.',
        'checks':checks, 'Schoen_eightfold_cycle_mechanism_conditional_on_realization':True,
        'd9_corrected_character':[str(x) for x in secant_character(9,3)],
        'd9_theta_translates':9, 'd9_normalized_nodes':306,
        'ramified_tower_genera':cyclic_genera(4,[1,3]), 'primitive_Prym_dimension':8,
        'research_queue':c['research_queue'], **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))
