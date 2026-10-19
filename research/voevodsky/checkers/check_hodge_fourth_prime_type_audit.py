"""Retrospective native-type/polarization audit of the F41 CM-positive control.

Consumes the separately replayed count receipt. Does not itself rerun fields.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import check_hodge_fourth_prime_controls as source

ROOT=source.ROOT
OUT=ROOT/'research/voevodsky/results/hodge-fourth-prime-type-audit-v1.json'
NOTE=ROOT/'research/voevodsky/hodge-fourth-prime-type-audit-v1.md'


def partial_crt():
    old=json.loads(source.previous.OUT.read_text(encoding='utf-8'))['CRT_partition']
    survivors=set(old['joint_survivors']);unknown=set(old['uncertified_residues']);unexcluded=survivors|unknown
    source.require(len(survivors)==2 and len(unknown)==98 and len(unexcluded)==100,'prior CRT partition')
    labels=[];joint=[]
    for a in range(8177*41):
        if a%8177 not in unexcluded or a%41==12:labels.append(0)
        elif a%8177 in survivors and a%41==4:labels.append(1);joint.append(a)
        elif a%8177 in survivors:labels.append(2)
        else:labels.append(3)
    source.require([labels.count(j) for j in range(4)]==[331257,2,78,3920] and joint==[297459,333703],'partial fourth-prime CRT counts')
    return {'domain':'integer a on lambda2,b2 line; necessary one-way screens only','modulus':335257,'excluded_count':331257,'newly_excluded_over_lifted_old_rule':100,
        'jointly_certified_necessary_classes':joint,'centered_joint_representatives':[-37798,-1554],
        'old_certified_but_uncounted_at41_count':78,'old_uncertified_not_excluded_by41_count':3920,
        'uncertified_or_uncounted_count':3998,'classification_sha256':sha256(bytes(labels)).hexdigest(),
        'rule':'exclude_old_veto_or_a41_equals12;certify_joint_only_old_survivor_and_a41_equals4;retain_all_other_unknowns'}


def report():
    source.verify_frozen_base()
    parent=json.loads(source.OUT.read_text(encoding='utf-8'))
    source.require(parent['passed'] and all(parent['checks'].values()),'positive count receipt required')
    for name,digest in parent['source_sha256'].items():
        source.require(sha256((ROOT/name).read_bytes()).hexdigest()==digest,'stale F41 parent input: '+name)
    source.require(parent['negative_a_mod41']==[12] and parent['literal_controls_excluded']==[3087] and
        parent['prediction_both_controls_CM_absent_survived'] is False,'retain falsified two-absence prediction')
    data=json.loads(source.COUNTS.read_text(encoding='utf-8'))
    rows=[r for r in data['rows'] if r['a']==4];r=source.reconstruct(rows,4)
    stored=next(c for c in parent['finite_field_cases'] if c['a_mod41']==4)
    source.require(all(stored[k]==v for k,v in r.items()),'typed audit polynomial differs from count receipt')
    beta=source.elliptic_beta();f7=tuple(map(tuple,r['Gaussian_characteristic_coefficients_descending']))
    cert=source.previous.arithmetic.cm_certificate(tuple(r['Frobenius_characteristic_coefficients_descending']),beta)
    source.require(cert['geometric_reduction_Ei_multiplicity_in_complement']==1 and cert['cyclotomic_factors']==[{'order':1,'multiplicity':2}],'unique F41 CM factor')
    same=source.previous.native_factors(f7,beta,[1]);opposite=source.previous.native_factors(f7,source.bar(beta),[1])
    source.require(same['degree']==0 and opposite['degree']==1,'opposite type, not just rational CM multiplicity')
    p=source.previous.pol.spectral_certificate(f7,beta,source.bar(beta),41)
    source.require(p['exact_idempotent'] and p['exact_Rosati_self_adjoint'] and p['Gaussian_rank']==1,'exact typed projector identities')
    source.require(p['derivative_norm_valuation3']==2 and p['integral_at3'] is False,'nonunit coefficient control')
    e=tuple(tuple(Q(n,d) for n,d in z) for z in p['projector_coefficients_ascending'])
    source.require(source.previous.pol.integral_at3(source.previous.pol.scale(e,(3,0))),'3 times projector coefficient integrality')
    source.previous.known_axis_split_certificate(4)
    source.previous.pol.norm_parity_certificate()
    source.previous.joint.signature_certificate(source.previous.joint.SIGNATURE)
    paths=[Path(__file__),NOTE,source.OUT,source.COUNTS,ROOT/'research/voevodsky/hodge-inert-elliptic-projector-v1.md',
        ROOT/'research/voevodsky/hodge-scalar-37-census-v1.md']
    return {'schema':'marici.hodge-fourth-prime-type-audit-result.v1','passed':True,
        'question':'Does the positive F41 factor veto or merely preserve the actual -1554 control?',
        'disposition':'necessary_typed_screen_survives_not_a_complex_lift','parameters_lambda_a_b':[2,-1554,2],
        'necessary_screened_primes':[13,17,37,41],'a_mod41':4,'same_type_certificate':same,'opposite_type_certificate':opposite,
        'inert3_projector':p,'primitive_axis_v3_upper_bound_conditional_on_axis_existence':1,
        'primitive_axis_v3_values_conditional_on_target_isogeny':[1],
        'target_hypotheses':{'fixed_X6_End0':'Q(i)','fixed_X6_signature':[3,3],'fixed_X6_Hermitian_determinant_class':-3,
            'actual_first_axis_theta_degree':4,'principal_source':True,'target_isogeny_need_not_be_K_linear':True},
        'preregistered_both_CM_absent_prediction_falsified':True,'other_tested_literal_3087_excluded':True,
        'partial_fourth_prime_CRT_partition':partial_crt(),
        'all_lifts_of_either_old_CRT_class_excluded':False,'actual_opposite_complex_axis_constructed':False,
        'nonunit_polynomial_proves_actual_lattice_denominator':False,'theta_degree6_constructed':False,
        'fixed_X6_identified':False,'Hodge_proved':False,'Hodge_refuted':False,
        'count_verification':'Consumes the fresh separate two-control count receipt; no independent field replay in this audit.',
        'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','same_type_certificate','opposite_type_certificate','inert3_projector')},indent=2))
