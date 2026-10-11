"""Iteration 8: natural inward realization, not a physical time evolution.
For each fixed s, the square maps are PL. The full parameterized homotopy
and radial blowdown are continuous semialgebraic, not silently claimed PL.
"""
from fractions import Fraction as Q
from copy import deepcopy
from pathlib import Path
from hashlib import sha256
import json

from check_open_mode_pullback import verify as verify_open, check_simplicial, point_of_cell, projections, mediator
from check_projector_fold_sheets import parameters
from check_fold_coefficient_attachment import mode, direction
from potential_complex_pullback import digest, depth

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/open_mode_pullback_store.json'


def inward(x,s):
    if not 0<=s<=1: raise ValueError('realization parameter outside [0,1]')
    depth(x)
    return tuple((1-s)*a+s/len(x) for a in x)


def act_q(x,v,s):
    if len(x)!=3 or len(v)!=4 or depth(v)!=1: raise ValueError('point type')
    return inward(x,s),v


def blowdown(x,v):
    h=depth(x)
    return x,tuple((1-h)/4+h*a for a in v)


# Exact polynomial identities in s,r,h,a. Zero is the empty dictionary.
EXP=(0,0,0,0)
def const(x): return {EXP:Q(x)} if x else {}
def var(i):
    powers=list(EXP); powers[i]=1
    return {tuple(powers):Q(1)}
def add(*polys):
    out={}
    for poly in polys:
        for power,value in poly.items(): out[power]=out.get(power,Q(0))+value
    return {p:v for p,v in out.items() if v}
def negative(poly): return {p:-v for p,v in poly.items()}
def mul(a,b):
    out={}
    for p,x in a.items():
        for q,y in b.items():
            power=tuple(i+j for i,j in zip(p,q)); out[power]=out.get(power,Q(0))+x*y
    return {p:v for p,v in out.items() if v}
def radial_poly(parameter,point,n): return add(mul(add(const(1),negative(parameter)),point),mul(parameter,const(Q(1,n))))


def polynomial_checks():
    s,r,h,a=(var(i) for i in range(4)); compose=add(s,r,negative(mul(s,r)))
    semigroup=all(radial_poly(s,radial_poly(r,a,n),n)==radial_poly(compose,a,n) for n in (3,4))
    # beta((1-s)h,v) == R_s(beta(h,v)), component by component.
    shrunk=mul(add(const(1),negative(s)),h)
    before=add(mul(add(const(1),negative(h)),const(Q(1,4))),mul(h,a))
    after=add(mul(add(const(1),negative(shrunk)),const(Q(1,4))),mul(shrunk,a))
    return {'semigroup_identity_exact':semigroup,
            'radial_blowdown_naturality_exact':after==radial_poly(s,before,4)}


def construct(source):
    r=source['record']; maps={}
    for name,prefix in [('Q','Q:'),('H','H:')]:
        maps[name]={v:prefix+'012|'+pair['right'] for v,pair in r[name]['vertices'].items()}
    for name,prefix in [('resolved_potential','C:'),('interface','J:')]:
        maps[name]={v:prefix+'0|'+pair['right'] for v,pair in r[name]['vertices'].items()}
    maps['T']={v:'012' for v in r['T']['vertices']}
    endpoints=[maps['Q'][v] for v in r['Q']['vertices']]
    # Carrier = one host flag times one direction flag, not necessarily one
    # staircase simplex. Fixed-s PL maps can cross its six staircase cells.
    carriers=[]
    for tf in r['T']['maximal_simplices']:
        for bf in r['B']['maximal_simplices']:
            carriers.append({'host_flag':tf,'direction_flag':bf,'host_center':'012'})
    point_source=source
    while point_source.get('schema')!='marici.potential-pullback.v1': point_source=point_source['source']
    mesh=point_source['record']['conforming_host_refinement']
    return {'kind':'retained-inward-realization','source_root':source['root'],
            'fixed_parameter_category':'PL maps after compatible subdivision',
            'parameterized_category':'continuous semialgebraic maps',
            'parameter_domain':'0 <= s <= 1; geometric deformation parameter, not physical time',
            'family':{'T':'x -> (1-s)x+s*q','H':'(x,z) -> ((1-s)x+s*q,z)',
                      'resolved_potential':'(t,v) -> ((1-s)t,v)',
                      'interface':'(t,z) -> ((1-s)t,z)',
                      'Q':'(x,v) -> ((1-s)x+s*q,v)'},
            'endpoint_vertex_maps':maps,'invariant_product_carriers':carriers,
            'endpoint_direction_vertices':sorted(set(endpoints)),
            'visible_host_vertex':{'barycentric':['1/3']*3,'spatial':mesh['points'][mesh['realized_vertex']]},
            'visible_potential_barycenter':['1/4']*4,
            'endpoint_readout':'(q,v) retains v, Gamma(v), and the original potential fold owner',
            'forgetful_readout':'radial blowdown sends every (q,v) to the old single vertex (q,b)',
            'scope':'potential-direction retention, not retention of each initial host location'}


def verify(packet):
    if set(packet)!={'schema','source','record','root'} or packet['schema']!='marici.inward-realization.v1': raise ValueError('schema')
    verify_open(packet['source']); record=packet['record']; r=packet['source']['record']
    if digest(record)!=packet['root'] or record!=construct(packet['source']): raise ValueError('source-bound realization mismatch')
    for name,mapping in record['endpoint_vertex_maps'].items(): check_simplicial(r[name],r[name],mapping)
    e=record['endpoint_vertex_maps']
    for a,b,m in [('H','interface','H_to_interface'),('resolved_potential','interface','potential_to_interface'),
                  ('Q','H','Q_to_H'),('Q','resolved_potential','Q_to_potential'),('Q','T','Q_to_host_location')]:
        for v in r[a]['vertices']:
            if r[m][e[a][v]]!=e[b][r[m][v]]: raise ValueError('endpoint naturality')
    for carrier in record['invariant_product_carriers']:
        if carrier['host_center'] not in carrier['host_flag']: raise ValueError('contraction can leave host carrier')
    if not all(polynomial_checks().values()): raise ValueError('polynomial identity')
    return {'endpoint_direction_vertices':len(record['endpoint_direction_vertices']),
            'invariant_product_carriers':len(record['invariant_product_carriers']),
            'endpoint_is_retraction_to':'{q} x B', 'all_five_endpoint_maps_simplicial':True,
            'polynomial_identities':polynomial_checks()}


def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False


def main():
    source=json.loads(SOURCE.read_text(encoding='utf-8')); verify_open(source)
    record=construct(source); packet={'schema':'marici.inward-realization.v1','source':source,'record':record,'root':digest(record)}
    report=verify(packet); r=source['record']; atlas_packet=source['source']['source']; p,n,recovery=parameters(atlas_packet['source'])
    q=(Q(1,3),)*3; b=(Q(1,4),)*4; params=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
    natural=True; retained=True; visible=True; composition=True; retract=True; endpoints=set()
    for simplex in r['Q']['maximal_simplices']:
        x,v=point_of_cell(r,simplex); (xx,z),(t,vv)=projections(x,v,p)
        for s in params:
            xs,vs=act_q(x,v,s); (newx,newz),(newt,newv)=projections(xs,vs,p)
            natural &= newx==inward(x,s) and newz==z and newt==(1-s)*t and newv==v
            natural &= mediator(newx,newz,newt,newv,p)==(xs,vs)
            retained &= vs==v and mode(p,direction(vs))==mode(p,direction(v))
            oldx,oldy=blowdown(x,v); bx,by=blowdown(xs,vs)
            visible &= (bx,by)==(inward(oldx,s),inward(oldy,s))
            retract &= act_q(q,v,s)==(q,v)
            for t2 in (Q(0),Q(1,3),Q(1)):
                composition &= act_q(*act_q(x,v,t2),s)==act_q(x,v,s+t2-s*t2)
        endpoints.add(act_q(x,v,Q(1)))
    checks={'all_endpoint_maps_are_actual_simplicial_maps':report['all_five_endpoint_maps_simplicial'],
            'all_216_flag_product_carriers_invariant':report['invariant_product_carriers']==216,
            'exact_polynomial_semigroup_law':report['polynomial_identities']['semigroup_identity_exact'],
            'exact_polynomial_blowdown_naturality':report['polynomial_identities']['radial_blowdown_naturality_exact'],
            'naturality_on_all_1296_cell_interiors_and_five_parameters':natural,
            'potential_direction_and_actual_mode_retained_through_endpoint':retained,
            'visible_realization_commutes_with_old_radial_contraction':visible,
            'sampled_semigroup_compositions_agree':composition,
            'whole_endpoint_fiber_fixed_during_realization':retract}
    final_owners=set(); center_states=[]
    atlas=atlas_packet['record']
    for face,owner in zip(r['B']['maximal_simplices'],atlas['original_fold_owners']):
        v=tuple(sum(Q(r['B']['vertices'][ref]['barycentric'][i]) for ref in face)/3 for i in range(4))
        x=(Q(1),Q(0),Q(0)); endpoint=act_q(x,v,Q(1))
        if endpoint!=(q,v): raise ValueError('endpoint direction loss')
        final_owners.add(tuple(owner)); center_states.append(endpoint)
    checks['all_24_fold_interiors_remain_active_at_final_vertex']=len(final_owners)==24
    checks['all_36_refined_direction_faces_have_distinct_endpoint_interiors']=len(set(center_states))==36
    checks['visible_endpoint_is_one_old_point']=all(blowdown(x,v)==(q,b) for x,v in center_states)
    checks['retained_endpoint_not_misreported_as_one_information_point']=len(set(center_states))>1 and report['endpoint_direction_vertices']==20
    e=record['endpoint_vertex_maps']['Q']
    checks['endpoint_retraction_is_idempotent']=all(e[e[v]]==e[v] for v in e)
    checks['outside_parameter_interval_rejected']=rejected(lambda:act_q(q,(Q(1),Q(0),Q(0),Q(0)),Q(2)))
    # Interior loop around the host vertex contracts to q with v fixed. This
    # is an explicit disk filling; a forced odd flat sheet swap is incompatible.
    circle=['0','01','1','12','2','02','0']; v=(Q(1),Q(0),Q(0),Q(0)); loops=[]
    for s in params:
        path=[]
        for label in circle:
            u=tuple(map(Q,r['T']['vertices'][label])); x=tuple(Q(1,6)+a/2 for a in u)
            path.append(act_q(x,v,s))
        loops.append(path)
    checks['host_belt_loop_has_explicit_fixed_direction_disk_filling']=all(path[0]==path[-1] for path in loops) and len(set(loops[-1]))==1
    # The scalar-product term proves the full family is generally not affine
    # on product cells. The receipt explicitly uses the semialgebraic category.
    joint=radial_poly(var(0),var(3),3)
    checks['parameterized_family_category_is_not_silently_PL']=joint.get((1,0,0,1))==Q(-1) and record['parameterized_category']=='continuous semialgebraic maps'
    bad=deepcopy(packet); key=next(iter(bad['record']['endpoint_vertex_maps']['Q'])); bad['record']['endpoint_vertex_maps']['Q'][key]='Q:012|missing'; bad['root']=digest(bad['record'])
    checks['rehashed_wrong_endpoint_direction_rejected']=rejected(lambda:verify(bad))
    bad=deepcopy(packet); bad['record']['family']['Q']='(x,v) -> (q,chosen_v)'; bad['root']=digest(bad['record'])
    checks['rehashed_fold_erasing_realization_rejected']=rejected(lambda:verify(bad))
    checks['complete_serialized_realization_reverifies']=verify(json.loads(json.dumps(packet)))==report
    result={'schema':'marici.inward-realization-check.v1','passed':all(checks.values()),'checks':checks,'realization':report,
            'tested_cell_interiors':1296,'tested_parameters':list(map(str,params)),
            'visible_host_point':record['visible_host_vertex'],'root':packet['root'],'source_root':source['root'],
            'source_file_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'disposition':'A witness-retaining inward realization with explicit point-only blowdown. All potential fold owners and direction/mode readouts survive at the host center. Host location history is not retained by the endpoint itself; no physical dynamics or particle identity is asserted.'}
    out=BASE/'results'
    (out/'inward_realization_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (out/'inward_realization.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
