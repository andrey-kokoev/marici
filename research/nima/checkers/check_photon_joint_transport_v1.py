"""Joint degree4/5 cuts plus degree6 transport: exact full-cut reconstruction and source fibres."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_equal_transport_v1 as equal
import check_photon_joint_degree6_fibres_v1 as nonzero
import check_photon_zero_leading_fibres_v1 as zero
t=equal.t;five=nonzero.five;p=t.cut.p
CONTRACT=HOME/'contracts/photon-joint-transport-v1.json';PROOF=HOME/'photon-joint-transport-v1.md'
TEST=HOME/'checkers/test_photon_joint_transport_v1.py';MANIFEST=HOME/'scc-models/photon-joint-transport-v1.json'
RESULT=HOME/'results/photon-joint-transport-v1.json'


def response_from_transport(B,m3):
    G,Gp,Gpp,F,Fp,H=map(Q,B);m3=Q(m3)
    m2=5*m3-Gpp/2;d2=(Gp-4*m2+2*m3)/6;d0=-G-d2-m2-m3
    o2=(Fp-12*F)/18;o0=-4*F-o2
    return d0,d2,o0,o2,m2,m3,H/3


def cut_from_response(R):
    d0,d2,o0,o2,m2,m3,h=R
    return (p.add((d0,),p.scale(d2,t.cut.LEGENDRE[2])),
            p.add((o0,),p.scale(o2,t.cut.LEGENDRE[2])),
            p.add(p.scale(m2,t.cut.D22[0]),p.scale(m3,t.cut.D22[1])),p.scale(-h,t.cut.prev.K))


def classify(data45,B):
    if len(data45)!=7 or len(B)!=6:raise ValueError('complete seven lower-cut and six transport coordinates required')
    data45=tuple(map(Q,data45));B=tuple(map(Q,B));c=five.chart(data45)
    a,b,_,u,_,w,_=data45
    if a:
        square=u*u/a;chart='g2-nonzero'
    elif b:
        square=w*w/(100*b);chart='f2-only'
    else:
        o2=(B[4]-12*B[3])/18
        square=-Q(336,5)*(B[2]+2*o2);chart='zero-leading'
    R=response_from_transport(B,square/4032);C=cut_from_response(R)
    fibre=zero.classify(data45,C,t.CASES) if c['stratum']=='zero-leading' else nonzero.classify(data45,C,t.CASES)
    return {'chart':chart,'g3_square':square,'response':R,'cut':C,'fibre':fibre}


def certificate():
    # Inverting the augmented response map is an exact seven-dimensional linear identity.
    for i in range(7):
        R=tuple(Q(int(i==j)) for j in range(7));B=tuple(t.dot(row,R) for row in equal.previous.L)
        assert response_from_transport(B,R[5])==R
    # Zero-leading identity holds coefficientwise on the entire cubic-square monomial block.
    row=t.add(t.FLOW[2],t.scale(Q(1,9),t.add(t.FLOW[4],t.scale(-12,t.FLOW[3]))))
    assert row[6:]==(-Q(5,336),Q(),Q(),Q(),Q(),Q())
    return {'augmented_linear_inverse_basis_checks':7,'zero_leading_square_identity':'g3^2=-(336/5)*(B_G6doubleprime+2*O2)',
            'leading_square_charts':['(g2*g3)^2/g2^2','(g2*f3+10*f2*g3)^2/(100*f2^2) when g2=0'],
            'zero_leading_cubic_block_row':list(map(str,row[6:]))}


def validate(c):
    assert c['schema']=='marici.photon-joint-transport.v1' and c['owner']=='marici.Nima'
    for k in ('full_degree6_cut_reconstructed_from_joint_data','real_joint_image_and_fibres_classified',
              'all_leading_and_zero_leading_strata_retained','quartic_nuisance_contacts_retained',
              'irrational_source_branches_retained'):
        assert c[k] is True,k
    for k in ('transport_alone_recovers_full_cut','uniformly_stable_cut_reconstruction_derived',
              'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c)
    parents=(equal.build(),nonzero.build(),zero.build());cert=certificate();counts={}
    sources=list(product((Q(-1),Q(1)),repeat=8))
    sources += [(Q(),Q(s),Q(2),Q(3),Q(4),Q(1),Q(-2),Q(3)) for s in (-2,2)]
    for quartic in product((Q(-1),Q(1)),repeat=3):
        for h in (Q(-1),Q(),Q(1)):
            sources.append((Q(1),Q(-6),Q(1),Q(),h)+quartic)
            for a in (Q(-1),Q(),Q(1)):sources.append((Q(1),Q(-6),a,-10*a,h)+quartic)
    for cubic in product((Q(-1),Q(),Q(1)),repeat=3):
        for quartic in ((Q(),)*3,(Q(1),Q(-2),Q(3))):sources.append((Q(),Q())+cubic+quartic)
    for h in (Q(-1),Q(),Q(1)):
        for quartic in ((Q(),)*3,(Q(1),Q(-2),Q(3))):sources.append((Q(),Q(),Q(1),Q(-10),h)+quartic)
    for x in sources:
        J=five.observe(x[:5]);B=equal.previous.transport(x);r=classify(J,B)
        assert r['response']==equal.previous.cut_coordinates(x)
        assert r['cut']==t.cut.combine(t.CASES,x) and r['g3_square']==x[2]**2
        direct=zero.classify(J,r['cut'],t.CASES) if not any(x[:2]) else nonzero.classify(J,r['cut'],t.CASES)
        assert r['fibre']==direct;counts[r['chart']]=counts.get(r['chart'],0)+1
    # Nonsquare leading root, independent nonsquare h branches, and mixed cubic radicals.
    x=(Q(1),Q(2),Q(3),Q(4),Q(5),Q(1),Q(-2),Q(3))
    r=classify(tuple(2*v for v in five.observe(x[:5])),tuple(2*v for v in equal.previous.transport(x)))
    assert r['fibre']['root_square']==2 and r['fibre']['base']==x
    x=(Q(1),Q(-6),Q(1),Q(-10),Q(),Q(1),Q(-2),Q(3))
    C=nonzero.plus(t.cut.combine(t.CASES,x),nonzero.scale(Q(2),t.CASES[11]))
    z=equal.previous.weights(x);z=z[:11]+(Q(2),)
    B=tuple(t.dot(row,z) for row in t.FLOW);r=classify(five.observe(x[:5]),B)
    assert r['cut']==C and r['fibre']['h_square']==2 and r['fibre']['actual_fibre_size']==4
    zc=zero.expected_cut((Q(7),Q(700),Q(-70),Q(2),Q()),t.CASES)
    zi=zero.extract(zc);z=(Q(),)*6+(zi[0],zi[2],Q(),zi[1],Q(),zi[3])
    r=classify((Q(),)*7,tuple(t.dot(row,z) for row in t.FLOW))
    assert r['cut']==zc and r['fibre']['root_square']==7 and r['fibre']['h_square']==Q(2,7)
    # The equal-transport pair is now distinguished by the lower cut data, and each cut is recovered.
    for v in (Q(1),Q(2)):
        x=equal.source(v);assert classify(five.observe(x[:5]),equal.TARGET)['cut']==t.cut.combine(t.CASES,x)
    invalid=[((Q(),)*6,(Q(),)*6),((Q(),)*7,(Q(),)*5),
             ((Q(1),Q(1),Q(),Q(),Q(),Q(),Q()),(Q(),)*6),
             ((Q(),)*7,(Q(),Q(),Q(1),Q(),Q(),Q()))]
    x=(Q(1),Q(2),Q(3),Q(4),Q(5),Q(1),Q(-2),Q(3));B=list(equal.previous.transport(x));B[5]+=1
    invalid.append((five.observe(x[:5]),tuple(B)))
    x=(Q(),Q(),Q(1),Q(1),Q(1),Q(),Q(),Q());B=list(equal.previous.transport(x));B[0]+=1
    invalid.append(((Q(),)*7,tuple(B)))
    for J,B in invalid:
        try:classify(J,B)
        except ValueError:pass
        else:raise AssertionError('incomplete or nonrealizable joint data admitted')
    refused=['infer_transport_only_inverse','extend_nonzero_leading_chart_across_zero','drop_free_quartics_or_radical_signs','infer_uniform_stability_from_exact_charts']
    for key in ('transport_alone_recovers_full_cut','uniformly_stable_cut_reconstruction_derived',
                'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned joint-transport promotion: '+key)
    paths=set().union(*({ROOT/path for path in parent['source_sha256']} for parent in parents))
    paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-joint-transport-receipt.v1','status':'pass',
        'scope':'exact_joint_degree45_cuts_and_degree6_transport_image_and_source_fibres_not_stability_or_physical_matching',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'source_checks':len(sources),'chart_counts':counts,'algebraic_controls':3,'invalid_joint_data_refused':len(invalid),
        'source_fibres_equal_full_joint_cut_fibres':True,'zero_leading_quartic_free_dimension':3,
        'general_real_image_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale joint-transport receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','source_checks','chart_counts','full_degree6_cut_reconstructed_from_joint_data','uniformly_stable_cut_reconstruction_derived')}))

if __name__=='__main__':main()
