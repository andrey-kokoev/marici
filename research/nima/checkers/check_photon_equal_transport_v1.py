"""Exact actual-source curve: equal nonzero degree-six transport, different cuts."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_degree6_scale_null_v1 as previous
t=previous.t;p=previous.p
CONTRACT=HOME/'contracts/photon-equal-transport-v1.json';PROOF=HOME/'photon-equal-transport-v1.md'
TEST=HOME/'checkers/test_photon_equal_transport_v1.py';MANIFEST=HOME/'scc-models/photon-equal-transport-v1.json'
RESULT=HOME/'results/photon-equal-transport-v1.json'
TARGET=(-Q(1,960),Q(1,960),Q(),Q(),Q(),Q())
BASE=(Q(1,1152),Q(1,5760),Q(),Q(),Q(),Q(),Q())
LINE=(Q(-3),Q(-3),Q(),Q(),Q(5),Q(1),Q())


def source(v):
    v=Q(v);d=7+30*v*v;P=14*v/d;q=(7-30*v*v)/d
    return Q(1),Q(),P,q,Q(),-Q(7,16)*P*P,-Q(5,56)*P*P,-Q(5,84)*P*q


def polynomial_certificate():
    d=(Q(7),Q(),Q(30));pn=(Q(),Q(14));qn=(Q(7),Q(),Q(-30));zero=(Q(),)
    dd=p.mul(d,d);pp=p.mul(pn,pn);pq=p.mul(pn,qn);qq=p.mul(qn,qn)
    source_num=(dd,zero,p.mul(pn,d),p.mul(qn,d),zero,p.scale(-Q(7,16),pp),p.scale(-Q(5,56),pp),p.scale(-Q(5,84),pq))
    weight_num=(p.scale(-Q(7,16),pp),p.scale(-Q(5,56),pp),p.scale(-Q(5,84),pq),zero,zero,zero,pp,pq,zero,qq,zero,zero)
    # Certify factorization in all twelve coordinates as polynomial identities, not just sample products.
    for (i,j),w in zip(t.cut.PAIRS,weight_num):assert p.mul(source_num[i],source_num[j])==p.mul(w,dd)
    project=lambda row:previous.sum_polys(tuple(p.scale(x,y) for x,y in zip(row,weight_num)))
    for row,value in zip(t.FLOW,TARGET):assert project(row)==p.scale(value,dd)
    for row,base,line in zip(previous.RESP,BASE,LINE):
        assert project(row)==p.add(p.scale(base,dd),p.scale(line/Q(4032),pp))
    # d(v)>0 for all real v: the only nonzero coefficients are positive constant and square.
    assert d==(Q(7),Q(),Q(30))
    return {'denominator':list(map(str,d)),
            'source_numerators_over_denominator_squared':[list(map(str,row)) for row in source_num],
            'monomial_numerators_over_denominator_squared':[list(map(str,row)) for row in weight_num],
            'factorization_polynomial_identities':12,'constant_transport_polynomial_identities':6,'cut_response_polynomial_identities':7}


def validate(c):
    assert c['schema']=='marici.photon-equal-transport.v1' and c['owner']=='marici.Nima'
    for k in ('actual_real_constant_nonzero_transport_curve','distinct_degree6_cuts_certified',
              'quartic_contacts_retained_not_fixed_away','polynomial_source_factorization_certified'):
        assert c[k] is True,k
    for k in ('joint_degree45_and_transport_fibres_classified','physical_matching_selected',
              'native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=previous.build();cert=polynomial_certificate()
    controls=0
    for v in (Q(n,d) for d in (1,2,3,7) for n in range(-4,5)):
        x=source(v);assert previous.transport(x)==TARGET and any(TARGET)
        assert previous.cut_coordinates(x)==tuple(b+x[2]**2*l/4032 for b,l in zip(BASE,LINE))
        assert x[3]**2+Q(30,7)*x[2]**2==1;controls+=1
    x=source(Q(1));y=source(Q(2))
    assert x!=y and x!=tuple(-v for v in y) and all(x[i] and y[i] for i in (5,6,7))
    assert previous.transport(x)==previous.transport(y)==TARGET
    Rx=previous.cut_coordinates(x);Ry=previous.cut_coordinates(y);delta=(y[2]**2-x[2]**2)/4032
    assert delta and tuple(b-a for a,b in zip(Rx,Ry))==tuple(delta*l for l in LINE)
    Cx=t.cut.combine(t.CASES,x);Cy=t.cut.combine(t.CASES,y)
    assert Cx!=Cy
    # The forward D response is already different; no source-only difference hidden from all cuts.
    forward_difference=p.evaluate(p.add(Cy[0],p.scale(-1,Cx[0])),Q())
    assert forward_difference==-6*delta and forward_difference
    # Leading degree-four data agree; degree-five gp detects the family. No stronger joint-data failure is claimed.
    import check_photon_joint_cut_fibres_v1 as joint
    Jx=joint.observe(x[:5]);Jy=joint.observe(y[:5])
    assert Jx[:3]==Jy[:3] and Jx!=Jy
    refused=['infer_global_cut_recovery_from_zero_fibre_equivalence','use_only_a_Jacobian_null_vector',
             'pretend_quartic_contacts_were_zero','claim_lower_degree_data_equal_from_equal_degree6_running']
    for key in ('joint_degree45_and_transport_fibres_classified','physical_matching_selected',
                'native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned equal-transport promotion: '+key)
    paths={ROOT/v for v in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve(),Path(joint.__file__).resolve()))
    encode=lambda values:list(map(str,values))
    return {'schema':'marici.photon-equal-transport-receipt.v1','status':'pass',
        'scope':'exact_actual_eight_source_degree6_equal_nonzero_transport_different_cut_not_joint_lower_data',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'rational_parameter_controls':controls,'constant_transport':encode(TARGET),
        'source_at_parameter_1':encode(x),'source_at_parameter_2':encode(y),
        'cut_coordinates_at_1':encode(Rx),'cut_coordinates_at_2':encode(Ry),
        'cut_line_parameter_difference':str(delta),'forward_D_cut_difference':str(forward_difference),
        'degree4_data_equal':True,'degree5_data_equal':False,'all_three_quartic_contacts_nonzero_in_pair':True,
        'general_curve_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale equal-transport source receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','constant_transport','forward_D_cut_difference','degree5_data_equal','physical_matching_selected')}))

if __name__=='__main__':main()
