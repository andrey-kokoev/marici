"""Exact real-source certificate: zero degree-six transport iff zero cut, not zero interaction."""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_general_degree6_window_v1 as t
p=t.cut.p;base=t.base
CONTRACT=HOME/'contracts/photon-degree6-scale-null-v1.json';PROOF=HOME/'photon-degree6-scale-null-v1.md'
TEST=HOME/'checkers/test_photon_degree6_scale_null_v1.py';MANIFEST=HOME/'scc-models/photon-degree6-scale-null-v1.json'
RESULT=HOME/'results/photon-degree6-scale-null-v1.json'
RESP=(t.D0,t.D2,t.O0,t.O2,t.M2,t.M3,t.H)
L=((Q(-1),Q(-1),Q(),Q(),Q(-1),Q(-1),Q()),
   (Q(),Q(6),Q(),Q(),Q(4),Q(-2),Q()),
   (Q(),Q(),Q(),Q(),Q(-2),Q(10),Q()),
   (Q(),Q(),-Q(1,4),-Q(1,4),Q(),Q(),Q()),
   (Q(),Q(),Q(-3),Q(15),Q(),Q(),Q()),
   (Q(),Q(),Q(),Q(),Q(),Q(),Q(3)))

def weights(source):return tuple(source[i]*source[j] for i,j in t.cut.PAIRS)
def cut_coordinates(source):return tuple(t.dot(row,weights(source)) for row in RESP)
def transport(source):return tuple(t.dot(row,weights(source)) for row in t.FLOW)
def locus(source):
    g,f,P,q,h,K,J,M=source
    return P==q==h==0 and ((g==f==0) or (K==J==M==0))


def certificate():
    # The six transport equations reduce the seven cut coordinates to a single line.
    assert tuple(t.combine(row,RESP) for row in L)==t.FLOW
    assert base.nullspace(L)==((Q(-3),Q(-3),Q(),Q(),Q(5),Q(1),Q()),)
    assert t.M3==tuple(Q(1,4032) if i==6 else Q() for i in range(12))
    E0=t.add(t.D0,t.scale(3,t.M3));E2=t.add(t.D2,t.scale(3,t.M3));EM=t.add(t.M2,t.scale(-5,t.M3))
    # These are polynomial identities before imposing null transport or reality inequalities.
    unit=lambda i:tuple(Q(int(i==j)) for j in range(12))
    identity=t.add(t.add(t.scale(40,E0),t.scale(-140,EM)),t.scale(-2450,E2))
    target=t.add(t.add(unit(1),t.scale(-Q(355,224),unit(6))),
                 t.add(t.scale(-Q(25,64),unit(9)),t.scale(-Q(259,48),unit(11))))
    assert identity==target
    assert t.scale(-1440,t.O2)==t.add(unit(4),t.scale(-3,unit(11)))
    assert t.scale(960,t.H)==t.add(t.scale(10,unit(8)),unit(10))
    # h=0,f=0: E2=0 is a positive sum in P^2,q^2. h=0,f!=0 gives J=0;
    # the identity above then forces the same conclusion, using positive square coefficients.
    assert E2[6]==Q(1,1344) and E2[9]==Q(1,5760)
    h0_positive=(Q(355,224),Q(25,64))
    assert all(x>0 for x in h0_positive)
    # h!=0: q=-10P, f*J=3h^2; write u=P^2/h^2>=0, a=g/f.
    # Null D0,D2,M2 imply a=259/144+(3035/224)u>0.
    U=(Q(),Q(1));one=(Q(1),);zero=(Q(),)
    a=(Q(259,144),Q(3035,224));aa=p.mul(a,a)
    gK=p.add(p.add(p.scale(-Q(5,12),U),p.scale(Q(7,10),a)),(-Q(7,60),))
    fM=(-Q(7,16),-Q(365,96))
    # All weights below are multiplied by a and divided by h^2.
    # The omitted P*h,q*h entries do not enter any of these even-helicity rows;
    # their single-minus combination vanishes separately by q=-10P.
    w=(p.mul(a,gK),p.scale(3,aa),p.mul(aa,fM),gK,p.scale(3,a),p.mul(a,fM),
       p.mul(a,U),p.scale(-10,p.mul(a,U)),zero,p.scale(100,p.mul(a,U)),zero,a)
    evalrow=lambda row:sum_polys(tuple(p.scale(x,y) for x,y in zip(row,w)))
    for row in (E0,E2,EM,t.O2):
        assert row[8]==row[10]==0 and evalrow(row)==zero
    negative=evalrow(t.O0)
    expression=sum_polys((p.scale(Q(1,8),a),p.scale(-Q(49,640),aa),(-Q(7,576),),
                          p.scale(-1,p.mul(U,sum_polys((p.scale(Q(511,768),aa),(Q(25,576),),p.scale(Q(5,48),a)))))))
    assert negative==expression and len(negative)==4 and all(c<0 for c in negative)
    # Thus a*O0/h^2<0 for every u>=0, contradicting the null O0 equation.
    # With the cubic triple zero, the nonzero-leading quartic map is injective:
    # f!=0 uses D2,O2,O0; f=0,g!=0 uses O0 and the D0/M2 determinant below.
    determinant=Q(1,16)*(-Q(1,240))-Q(1,96)*Q(1,56)
    assert determinant==-Q(1,2240)
    return {'response_null_line':['-3','-3','0','0','5','1','0'],
            'h_zero_positive_square_coefficients':list(map(str,h0_positive)),
            'h_nonzero_a_affine':list(map(str,a)),
            'h_nonzero_strictly_negative_polynomial':list(map(str,negative)),
            'quartic_g_only_determinant':'-1/2240'}


def sum_polys(polys):
    out=(Q(),)
    for poly in polys:out=p.add(out,poly)
    return out


def validate(c):
    assert c['schema']=='marici.photon-degree6-scale-null.v1' and c['owner']=='marici.Nima'
    assert c['source_order']==list(t.cut.NAMES)
    for k in ('real_source_zero_transport_iff_zero_cut','complete_null_source_locus_classified',
              'strict_real_domain_polynomial_certificate','nonzero_Born_sources_retained'):
        assert c[k] is True,k
    for k in ('global_transport_fibres_classified','zero_transport_implies_zero_entire_interaction',
              'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=t.build();cert=certificate()
    total=nulls=0
    for source in product((Q(-1),Q(),Q(1)),repeat=8):
        zero_flow=not any(transport(source));zero_cut=not any(cut_coordinates(source))
        assert zero_flow==zero_cut==locus(source);total+=1;nulls+=int(zero_flow)
    # The parent's extra linear vector must not be mislabeled a real nonzero-cut null source.
    cutmap=tuple(tuple(t.get(case[r],n) for case in t.CASES) for r in range(4) for n in range(max(len(c[r]) for c in t.CASES)))
    extra=next(k for k in base.nullspace(t.FLOW) if any(t.dot(row,k) for row in cutmap))
    assert all(t.dot(row,extra)==0 for row in t.FLOW) and any(t.dot(row,extra) for row in RESP)
    witnesses=((Q(1),Q(2),Q(),Q(),Q(),Q(),Q(),Q()),(Q(),)*5+(Q(1),Q(2),Q(3)))
    born=[]
    for x in witnesses:
        assert not any(transport(x)) and not any(cut_coordinates(x)) and locus(x)
        amplitude=t.dot(base.amplitude_rows(Q(1),Q())[0],x);assert amplitude==1;born.append(str(amplitude))
    refused=['treat_extra_linear_kernel_as_real_source','infer_zero_interaction_from_zero_degree6_running',
             'equate_zero_fibre_with_all_data_fibres','force_quartic_nuisance_contacts_zero_before_elimination']
    for key in ('global_transport_fibres_classified','zero_transport_implies_zero_entire_interaction',
                'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unearned null-source promotion: '+key)
    paths={ROOT/path for path in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-degree6-scale-null-receipt.v1','status':'pass',
        'scope':'zero_degree6_transport_and_cut_on_real_eight_Born_source_locus_not_global_fibre_identification',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'certificate':cert,'grid_source_checks':total,'grid_null_sources':nulls,
        'null_source_locus':'{(g,f,0,0,0,0,0,0)} union {(0,0,0,0,0,K,L,M)}',
        'nonzero_Born_witness_forward_values':born,'null_fibre_proof_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale degree-six null-source receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','grid_source_checks','grid_null_sources','real_source_zero_transport_iff_zero_cut','global_transport_fibres_classified')}))

if __name__=='__main__':main()
