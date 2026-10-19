"""EF1-B relative phase-space coordinate unitary and Bose-symmetric profiles."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from math import factorial
from pathlib import Path
import check_cm_separation_map as cm

F=cm.F;x=cm.x;phase=cm.phase;ROOT=cm.ROOT;HOME=cm.HOME
CONTRACT=HOME/'contracts/relative-photon-measure.v1.json'
PROOF=HOME/'RELATIVE-PHOTON-MEASURE.md'
RESULT=HOME/'results/relative-photon-measure.v1.json'
ZERO=(0,0,0)


def clean(p):return {a:c for a,c in p.items() if c}
def const(c):return clean({ZERO:F(c)})
def var(i):return {tuple(int(i==j) for j in range(3)):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for a,c in p.items():out[a]=out.get(a,F())+c
    return clean(out)
def scale(c,p):return clean({a:c*v for a,v in p.items()})
def mul(p,q):
    out={}
    for a,c in p.items():
        for b,d in q.items():
            k=tuple(v+w for v,w in zip(a,b));out[k]=out.get(k,F())+c*d
    return clean(out)
def power(p,n):
    out=const(1)
    for _ in range(n):out=mul(out,p)
    return out
def conj(p):return {a:c.conjugate() for a,c in p.items()}
def scalar_power(v,n):
    out=F(1)
    for _ in range(n):out=out*v
    return out
def evaluate(p,ys):return sum((c*scalar_power(ys[0],a[0])*scalar_power(ys[1],a[1])*scalar_power(ys[2],a[2]) for a,c in p.items()),F())
def simplex_integral(p):
    # Normalized dnu_3=2 dy1 dy2, y3=1-y1-y2.
    return sum((c*Q(2*factorial(a[0])*factorial(a[1])*factorial(a[2]),factorial(sum(a)+2))
                for a,c in p.items()),F())
def inner(p,q):return simplex_integral(mul(conj(p),q))
def permute(p,order):return clean({tuple(a[i] for i in order):c for a,c in p.items()})

def coordinates(u,v):
    assert u>0 and v>0;D=u+v+u*v
    return u*v/D,v/D,u/D

def rho(u,v):
    assert u>0 and v>0
    return 2*u*v/(u+v+u*v)**3

def sphere_integral(p):
    # Polynomial in z=cos(theta), normalized solid-angle measure.
    return sum((c*Q(1,k+1) for k,c in enumerate(p) if k%2==0),F())
def ordinary_product(p,q):
    out=[F()]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]=out[i+j]+a*b
    return out

def validate_contract(c):
    assert c['schema']=='marici.scattering.relative-photon-measure.v1'
    assert c['relative_state_scope']=='fixed_future_timelike_total_four_momentum_fiber'
    assert c['reference_measures']=={'seed':'du dv times normalized SO(3) Haar',
        'three_body':'2 dy1 dy2 times normalized SO(3) Haar','two_body':'normalized solid angle'}
    for key in ('sharp_configuration_is_normalizable_profile','native_seed_measure_selected','native_input_to_photon_isometry_constructed',
                'full_Fock_wavepacket_constructed','helicity_lorentz_intertwiner_constructed',
                'profile_selected_by_native_dynamics','relative_two_three_sector_amplitude_selected',
                'branching_ratio_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=cm.build();assert parent==json.loads(cm.RESULT.read_text(encoding='utf-8')),'stale classical CM map'
    y=[var(i) for i in range(3)];one=const(1)
    # Polynomial verification of the cleared rational-chart Jacobian.
    u,v=y[:2];D=add(u,v,mul(u,v))
    determinant_numerator=add(mul(power(v,2),u),mul(power(u,2),mul(v,add(one,v))))
    assert determinant_numerator==mul(mul(u,v),D)
    chart_tests=0
    for a in range(1,6):
        for b in range(1,6):
            U,V=Q(a,3),Q(b,4);ys=coordinates(U,V)
            assert sum(ys)==1 and all(z>0 for z in ys)
            assert ys[0]/ys[1]==U and ys[0]/ys[2]==V
            assert rho(1/U,V/U)/U**3==rho(U,V) and rho(V,U)==rho(U,V)
            chart_tests+=1
    S2=add(*(power(z,2) for z in y));root60=2*phase.root(6)
    p0=one;p1=scale(root60,add(S2,const(Q(-1,2))))
    profiles=[p0,p1];gram=[[inner(a,b) for b in profiles] for a in profiles]
    assert gram==[[F(1),F()],[F(),F(1)]]
    for order in permutations(range(3)):
        assert all(permute(p,order)==p for p in profiles)
    plus=scale(F(1)/phase.SQ2,add(p0,p1));minus=scale(F(1)/phase.SQ2,add(p0,scale(F(-1),p1)))
    imaginary=scale(F(1)/phase.SQ2,add(p0,scale(phase.IM,p1)))
    assert inner(plus,plus)==inner(minus,minus)==inner(imaginary,imaginary)==F(1)
    observable_gap=inner(plus,mul(S2,plus))-inner(minus,mul(S2,minus))
    assert observable_gap==F(1)/phase.root(6)
    # Actual half-density evaluations at exact square-root anchors.
    for U,V,h in ((Q(1),Q(1),phase.SQ6/9),(Q(2),Q(1,3),F(Q(2,9)))):
        assert h*h==F(rho(U,V));ys=tuple(F(z) for z in coordinates(U,V))
        for p in (p0,p1,plus,minus,imaginary):
            target=evaluate(p,ys);seed=h*target;assert seed/h==target
    # Two explicit, positive symmetric profile densities. Selection is not native.
    examples={}
    for alpha in (1,3):
        C2=Q(factorial(3*alpha-1),2*factorial(alpha-1)**3)
        density=scale(F(C2),power(mul(mul(y[0],y[1]),y[2]),alpha-1))
        assert simplex_integral(density)==F(1)
        energy=scale(F(Q(1,2)),add(one,scale(F(-1),y[0])))
        mean=simplex_integral(mul(density,energy));second=simplex_integral(mul(density,power(energy,2)))
        variance=second-mean*mean
        assert mean==F(Q(1,3)) and variance==F(Q(1,18*(3*alpha+1)))
        examples[str(alpha)]={'density_coefficient':str(C2),'mean_energy_fraction':'1/3',
            'variance_energy_fraction':str(Q(1,18*(3*alpha+1)))}
    # Normalized even two-ray angular profiles, conditional in its own sector.
    q0=[F(1)];q1=[-phase.root(4)/2,F(),3*phase.root(4)/2]
    assert sphere_integral(ordinary_product(q0,q0))==sphere_integral(ordinary_product(q1,q1))==F(1)
    assert sphere_integral(q1)==F() and all(not q1[i] for i in range(1,len(q1),2))
    omitted_norm=simplex_integral(scale(F(5040),mul(y[0],mul(power(y[1],4),power(y[2],4)))))
    assert omitted_norm==F(Q(8,55))
    refused=[]
    for name in ('omit_half_density','erase_coherent_cross_term','declare_sharp_seed_a_normalizable_profile','select_spectrum_from_geometry',
                 'infer_branching_from_sector_volumes','promote_to_full_Fock_packet','claim_native_input_isometry'):
        try:
            if name=='omit_half_density':assert omitted_norm==F(1)
            elif name=='erase_coherent_cross_term':assert observable_gap==F()
            else:
                bad=copy.deepcopy(c)
                key={'declare_sharp_seed_a_normalizable_profile':'sharp_configuration_is_normalizable_profile',
                     'select_spectrum_from_geometry':'profile_selected_by_native_dynamics',
                     'infer_branching_from_sector_volumes':'branching_ratio_derived',
                     'promote_to_full_Fock_packet':'full_Fock_wavepacket_constructed',
                     'claim_native_input_isometry':'native_input_to_photon_isometry_constructed'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported relative-profile promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((cm.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_relative_photon_measure.py'))
    return {'schema':'marici.scattering.relative-photon-measure-receipt.v1','status':'pass',
        'scope_verdict':'conditional_relative_coordinate_unitary_and_Bose_profiles_not_native_emission',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'weight_ratio_coordinates':['u=w2/w1','v=w3/w1'],
        'shape_coordinates':['y1=uv/(u+v+uv)','y2=v/(u+v+uv)','y3=u/(u+v+uv)'],
        'absolute_chart_jacobian':'uv/(u+v+uv)^3','seed_half_density_squared':'2uv/(u+v+uv)^3',
        'chart_and_permutation_checks':chart_tests,'relative_coordinate_unitary_constructed':True,
        'three_body_orthonormal_profile_gram':x.encoded(gram),
        'coherent_plus_minus_S2_expectation_gap':observable_gap.encoded(),
        'normalizable_Bose_relative_profiles_constructed':True,'two_body_even_profiles_verified':True,
        'omitted_half_density_squared_norm':str(Q(8,55)),
        'sharp_configuration_is_normalizable_profile':False,
        'helicity_assumption':'all_equal_helicities_in_a_fixed_measurable_polarization_frame',
        'symmetric_density_examples':examples,'total_four_momentum_wavepacket_supplied':False,
        'native_seed_measure_selected':False,'native_input_to_photon_isometry_constructed':False,
        'full_Fock_wavepacket_constructed':False,'helicity_lorentz_intertwiner_constructed':False,
        'profile_selected_by_native_dynamics':False,'relative_two_three_sector_amplitude_selected':False,
        'branching_ratio_derived':False,'analytic_argument_machine_formalized':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,'high_energy_protocol_executed':False,
        'physical_outcomes_admitted':False,'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale relative photon measure'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','absolute_chart_jacobian','relative_coordinate_unitary_constructed',
        'normalizable_Bose_relative_profiles_constructed','symmetric_density_examples',
        'native_input_to_photon_isometry_constructed','full_Fock_wavepacket_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
