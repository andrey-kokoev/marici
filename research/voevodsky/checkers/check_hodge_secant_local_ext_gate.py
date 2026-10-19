"""Conditional local geometry/Ext of the corrected secant object, not deformation."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
from check_hodge_eightfold_literature_audit import report as literature_report, secant_character

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-secant-local-ext-gate.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-secant-local-ext-gate-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-secant-local-ext-gate-v1.json'
POLICY=['generic_incidence_verified_at_fixed_X','candidate_is_a_coherent_sheaf',
    'transformed_object_is_a_sheaf_proved','local_Ext2_length_is_global_Ext2_dimension',
    'local_to_global_edge_map_surjective_assumed','nonzero_local_Ext2_proves_obstructed_deformation',
    'semiregularity_proved','question_11_4_used_as_theorem','target_cycle_constructed',
    'actual_target_cover_constructed','Hodge_proved','Hodge_refuted',
    'all_cycle_annihilation_proved','global_witness_search_completed']


def require(c,m):
    if not c: raise ValueError(m)


def incidence(n):
    require(type(n) is int and n>=6,'cycle length at least six')
    edges=[frozenset((i,(i+1)%n)) for i in range(n)]
    census={'double_curve_types':0,'triple_point_types':0,'isolated_node_types':0}
    for size in range(5):
        for vertices in combinations(range(n),size):
            active=[e for e in edges if e.issubset(vertices)]
            require(len(active)<=3,'unexpected four-surface intersection')
            if size==3 and len(active)==2:
                require(len(active[0]&active[1])==1,'adjacent double curve')
                census['double_curve_types']+=1
            if size==4 and len(active)==3:
                census['triple_point_types']+=1
            if size==4 and len(active)==2 and active[0].isdisjoint(active[1]):
                census['isolated_node_types']+=1
    require(census=={'double_curve_types':n,'triple_point_types':n,
                    'isolated_node_types':n*(n-5)//2},'cycle incidence census')
    return census


def local_lengths(n,normalized,intersection_degree=24):
    require(type(normalized) is int and type(intersection_degree) is int and
            intersection_degree>0,'normalization count types')
    c=incidence(n);total=c['isolated_node_types']*intersection_degree
    require(0<=normalized<=total,'normalization exceeds isolated nodes')
    remaining=total-normalized
    return dict(c,isolated_nodes=total,triple_points=c['triple_point_types']*intersection_degree,
        normalized_nodes=normalized,remaining_nodes=remaining,
        H1_length=normalized,dual_sheaf_Ext3_length=remaining,
        local_self_Ext2_length=2*normalized+4*remaining)


def minimal(gens):
    gens=set(gens)
    return sorted(g for g in gens if not any(h!=g and all(a<=b for a,b in zip(h,g)) for h in gens))


def ideal_intersection(*ideals):
    result=list(ideals[0])
    for ideal in ideals[1:]:
        result=minimal(tuple(max(a,b) for a,b in zip(g,h)) for g in result for h in ideal)
    return result


def add(p,q):
    r=dict(p)
    for m,c in q.items(): r[m]=r.get(m,0)+c
    return {m:c for m,c in r.items() if c}


def neg(p): return {m:-c for m,c in p.items()}


def mul(p,q):
    r={}
    for a,c in p.items():
        for b,d in q.items():
            m=tuple(x+y for x,y in zip(a,b));r[m]=r.get(m,0)+c*d
    return {m:c for m,c in r.items() if c}


def mm(a,b):
    require(len(a[0])==len(b),'matrix shape')
    return [[sum_poly(mul(x,y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def sum_poly(ps):
    r={}
    for p in ps:r=add(r,p)
    return r


def variables():
    return [{tuple(int(i==j) for i in range(4)):1} for j in range(4)]


def generates_maximal(entries):
    variables_set={tuple(int(i==j) for i in range(4)) for j in range(4)}
    return all(not p or (len(p)==1 and next(iter(p)) in variables_set and
                        abs(next(iter(p.values())))==1) for p in entries) and {
                            next(iter(p)) for p in entries if p}==variables_set


def local_models():
    a,b,c,d=variables();z={}
    # Normalized node: cancellation of the diagonal O -> R^2 in the two Koszul resolutions.
    normal_d0=[[neg(a),neg(b),c,d]]
    normal_dm1=[[neg(b),z],[a,z],[z,neg(d)],[z,c]]
    # Unnormalized node: tensor the two resolutions of (a,b) and (c,d).
    node_gens=[[mul(a,c),mul(a,d),mul(b,c),mul(b,d)]]
    node_d1=[[d,b,z,z],[neg(c),z,b,z],[z,neg(a),z,d],[z,z,neg(a),neg(c)]]
    node_d2=[[b],[neg(d)],[c],[neg(a)]]
    triple_hb=[[b,z],[neg(a),d],[z,neg(c)]]
    return normal_d0,normal_dm1,node_gens,node_d1,node_d2,triple_hb


def exact_local_checks():
    d0,dm1,gens,d1,d2,hb=local_models()
    require(not any(p for row in mm(d0,dm1)+mm(gens,d1)+mm(d1,d2) for p in row),'local complex differential')
    require(generates_maximal(d0[0]) and generates_maximal([r[0] for r in d2]),'maximal-ideal cokernels')
    require(all(not p or all(sum(m)==1 for m in p) for row in dm1 for p in row),'minimal normalized complex')
    v=[next(iter(x)) for x in variables()]
    def prod(x,y):return tuple(a+b for a,b in zip(x,y))
    node=ideal_intersection([v[0],v[1]],[v[2],v[3]])
    triple=ideal_intersection([v[0],v[1]],[v[1],v[2]],[v[2],v[3]])
    minors=[]
    for i,j in combinations(range(3),2):
        p=add(mul(hb[i][0],hb[j][1]),neg(mul(hb[i][1],hb[j][0])))
        require(len(p)==1 and abs(next(iter(p.values())))==1,'Hilbert Burch minor')
        minors.append(next(iter(p)))
    require(node==sorted(prod(x,y) for x in v[:2] for y in v[2:]) and
            triple==sorted(minors),'local monomial ideals')
    require(ideal_intersection([v[0],v[1]],[v[1],v[2]])==minimal([v[1],prod(v[0],v[2])]),'double-curve CI')
    return {'local_complexes':True,'maximal_ideal_cokernels':True,
            'Hilbert_Burch_and_intersection_ideals':True}


def validate_gate(c):
    require(c['schema']=='marici.hodge-secant-local-ext-gate.v1' and
            c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
            c['node']=='secant-local-ext-gate','local Ext identity')
    require(c['geometry']=={'secant_d':9,'theta_translates':9,'normalized_isolated_nodes':306,
        'corrected_twist':3,'ambient_dimension':4,'four_theta_intersection_degree':24,
        'fivefold_intersections_empty':True,'all_intersections_through_four_translates_transverse':True,
        'complex_degrees':[0,1],'K_class':'[O]-[nu_*O_Ztilde]'},'local Ext hypotheses')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'local Ext promotion')
    for n in range(6,16):incidence(n)
    checks=exact_local_checks()
    require(local_lengths(9,306)['local_self_Ext2_length']==1116,'local Ext census')
    require([str(x) for x in secant_character(9,3)]==['1','3','-9/2','-9/2','27/8'],'corrected character retained')
    return dict(checks,incidence_census=True,normalization_and_local_lengths=True,
                corrected_character_retained=True,scope=True)


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));checks=validate_gate(c)
    prior=literature_report()
    receipt=ROOT/'research/voevodsky/results/hodge-eightfold-literature-audit-v1.json'
    require(json.loads(receipt.read_text(encoding='utf-8'))==prior and prior['passed'],'prior literature receipt stale')
    names={CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
           Path(__file__).relative_to(ROOT).as_posix(),receipt.relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-secant-local-ext-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed','checks':checks,
        'verification_level':'Conditional transverse local models, exact complexes and written local algebra; no global obstruction or semiregularity proof.',
        **local_lengths(9,306),'double_curve_genus':37,
        'normalized_node_self_Ext2_fibre_length':2,'remaining_node_self_Ext2_fibre_length':4,
        **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
