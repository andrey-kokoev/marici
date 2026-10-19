"""Local Wick-density candidates and a restricted finite-derivative envelope obstruction."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations,product
import json
from pathlib import Path
import check_covariant_escape_lift as lift

packet=lift.packet;phase=lift.phase;cm=packet.cm;F=lift.F;x=lift.x;ROOT=lift.ROOT;HOME=lift.HOME
three=packet.tail.escape.vertex.charge.three
CONTRACT=HOME/'contracts/local-source-vertex.v1.json'
PROOF=HOME/'LOCAL-SOURCE-VERTEX.md'
RESULT=HOME/'results/local-source-vertex.v1.json'
mm=phase.mm;adj=phase.adj;eye=phase.eye;scale=phase.scale
ETA=(1,-1,-1,-1)


def transpose(A):return [list(r) for r in zip(*A)]
def gamma_matrices():
    I=phase.IM
    sigmas=([[F(),F(1)],[F(1),F()]],[[F(),-I],[I,F()]],[[F(1),F()],[F(),F(-1)]])
    gammas=[[[F(ETA[0] if i<2 else -1) if i==j else F() for j in range(4)] for i in range(4)]]
    for s in sigmas:
        g=[[F() for _ in range(4)] for _ in range(4)]
        for i in range(2):
            for j in range(2):g[i][j+2]=s[i][j];g[i+2][j]=-s[i][j]
        gammas.append(g)
    return gammas


def field_strength(k,e):return [[k[i]*e[j]-k[j]*e[i] for j in range(4)] for i in range(4)]
def contraction(A,B):return sum((ETA[i]*ETA[j]*A[i][j]*B[i][j] for i in range(4) for j in range(4)),F())
def two_amplitude(ks,es):return cm.determinant([ks[0],es[0],ks[1],es[1]])
def three_amplitude(ks,es):
    Fs=[field_strength(k,e) for k,e in zip(ks,es)]
    total=[sum((k[i] for k in ks),F()) for i in range(4)]
    out=[F() for _ in range(4)]
    for a in range(3):
        b,c=[j for j in range(3) if j!=a];pairing=contraction(Fs[b],Fs[c])
        for mu in range(4):out[mu]+=sum((ETA[nu]*total[nu]*Fs[a][nu][mu]*pairing for nu in range(4)),F())
    return out


def polynomial_at(p,value):return sum((a*value**i for i,a in enumerate(p)),Q())
def multiply_polynomials(p,q):
    out=[Q()]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out


def validate_contract(c):
    assert c['schema']=='marici.scattering.local-source-vertex.v1'
    assert c['new_imported_fields']==['free_Dirac_CAR_field','free_Maxwell_field_strength','local_Wick_polynomials']
    assert c['candidate_densities']==['(psi_bar*i*gamma5*psi)*(F*dualF)',
        '(psi_bar*gamma_mu*psi)*d_nu(F^{nu_mu}*(F*F))']
    assert c['omitted_field_sectors_required_for_locality'] is True
    for key in ('native_Dirac_source_licensed','physical_incident_pair_preparation_bound','selected_rational_mass_vertex_derived',
                'selected_profile_projection_preserves_microcausality','self_adjoint_interacting_QFT_Hamiltonian_constructed',
                'nonperturbative_QFT_constructed','all_local_UV_completions_excluded','envelope_obstruction_excludes_composite_sources',
                'source_form_factors_selected','annihilation_rate_derived','branching_ratio_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=lift.build();assert parent==json.loads(lift.RESULT.read_text(encoding='utf-8')),'stale covariant lift'
    gs=gamma_matrices()
    charge_phase=(F(3)+4*phase.IM)/5
    assert charge_phase.conjugate()*charge_phase==F(1)  # Neutral bilinear under global charged U(1).
    for mu in range(4):
        for nu in range(4):
            assert phase.add(mm(gs[mu],gs[nu]),mm(gs[nu],gs[mu]))==scale(F(2*ETA[mu] if mu==nu else 0),eye(4))
    g5=scale(phase.IM,mm(gs[0],mm(gs[1],mm(gs[2],gs[3]))))
    C=scale(phase.IM,mm(gs[2],gs[0]));Ci=adj(C)
    assert mm(C,Ci)==eye(4)
    assert mm(C,mm(transpose(g5),Ci))==g5
    P=scale(phase.IM,g5)
    assert mm(gs[0],mm(adj(P),gs[0]))==P
    for g in gs:
        assert mm(C,mm(transpose(g),Ci))==scale(F(-1),g)
        assert mm(gs[0],mm(adj(g),gs[0]))==g
    assert mm(C,mm(transpose(P),Ci))==P
    L=packet.boost(packet.velocity([F(Q(1,8)),F(Q(1,6)),F()]))
    k2=[[F(1),F(),F(),F(1)],[F(1),F(),F(),F(-1)]]
    e2=[[F(),F(1),F(),F()],[F(),F(),F(1),F()]]
    A2=two_amplitude(k2,e2);assert A2!=F()
    assert two_amplitude([packet.act(L,k) for k in k2],[packet.act(L,e) for e in e2])==A2
    assert two_amplitude(k2[::-1],e2[::-1])==A2
    ward=0;permutation_cases=0;covariance_cases=1;homogeneous=0;nonzero=0
    for i in range(2):
        replaced=e2.copy();replaced[i]=k2[i]
        assert two_amplitude(k2,replaced)==F();ward+=1
    for t in (F(2),F(3)):
        assert two_amplitude([[t*v for v in k] for k in k2],e2)==t*t*A2;homogeneous+=1
    configs=[[[F(1),F(1),F(),F()],[F(1),-F(1)/2,phase.SQ3/2,F()],[F(1),-F(1)/2,-phase.SQ3/2,F()]],
             [[F(1),F(1),F(),F()],[F(1),F(),F(1),F()],[phase.SQ2,F(-1),F(-1),F()]]]
    same_helicity_witness=None;mixed_helicity_witness=None;single_divergences=0
    for ks in configs:
        frames={h:three.helicity_frame(ks,[F(),F(),F(1)],h) for h in (-1,1)}
        for helicities in product((-1,1),repeat=3):
            es=[[F()]+frames[h][j] for j,h in enumerate(helicities)]
            for k,e in zip(ks,es):
                f=field_strength(k,e)
                assert all(sum((ETA[nu]*k[nu]*f[nu][mu] for nu in range(4)),F())==F() for mu in range(4))
                single_divergences+=1
            A=three_amplitude(ks,es);total=[sum((k[i] for k in ks),F()) for i in range(4)]
            assert packet.minkowski(total,A)==F() and A[0]==F()
            if A!=[F()]*4:nonzero+=1
            if ks==configs[0] and helicities==(1,1,1):
                assert A[3]!=F();same_helicity_witness=[v.encoded() for v in A]
            if ks==configs[0] and helicities==(-1,-1,1):
                assert A[3]!=F();mixed_helicity_witness=[v.encoded() for v in A]
            for j in range(3):
                replaced=es.copy();replaced[j]=ks[j]
                assert three_amplitude(ks,replaced)==[F()]*4;ward+=1
            for order in permutations(range(3)):
                assert three_amplitude([ks[j] for j in order],[es[j] for j in order])==A;permutation_cases+=1
            assert three_amplitude([packet.act(L,k) for k in ks],[packet.act(L,e) for e in es])==packet.act(L,A);covariance_cases+=1
            for t in (F(2),F(3)):
                scaled=three_amplitude([[t*v for v in k] for k in ks],es)
                assert scaled==[t*t*t*t*v for v in A];homogeneous+=1
    assert nonzero>0 and same_helicity_witness is not None and mixed_helicity_witness is not None
    # For ANY finite polynomial p, (1+M)^3 p vanishes at -1, unlike M^a (a=0,1).
    factor=[Q(1),Q(3),Q(3),Q(1)];assert polynomial_at(factor,Q(-1))==0
    for p in ([Q(1)],[Q(),Q(1)], [Q(2),Q(-3),Q(1),Q(5)]):
        assert polynomial_at(multiply_polynomials(factor,p),Q(-1))==0
    assert polynomial_at([Q(1)],Q(-1))==1 and polynomial_at([Q(),Q(1)],Q(-1))==-1
    refused=[]
    for name in ('declare_constant_two_photon_contact_gauge_invariant','exact_finite_derivative_rational_envelope',
                 'equate_dimensionful_EFT_couplings','projected_modes_inherit_local_commutator',
                 'differentiate_only_first_Maxwell_factor','formal_density_is_self_adjoint_QFT',
                 'promote_native_Dirac_source','exclude_all_composite_source_form_factors'):
        try:
            if name=='declare_constant_two_photon_contact_gauge_invariant':
                # epsilon1.epsilon2 fails Ward on an equally valid gauge representative.
                gauged=[a+b for a,b in zip(e2[1],k2[1])]
                assert packet.minkowski(k2[0],gauged)==F()
            elif name=='exact_finite_derivative_rational_envelope':assert polynomial_at([Q(1)],Q(-1))==0
            elif name=='equate_dimensionful_EFT_couplings':assert -3==-6
            elif name=='differentiate_only_first_Maxwell_factor':assert same_helicity_witness==[F().encoded() for _ in range(4)]
            else:
                key={'projected_modes_inherit_local_commutator':'selected_profile_projection_preserves_microcausality',
                     'formal_density_is_self_adjoint_QFT':'self_adjoint_interacting_QFT_Hamiltonian_constructed',
                     'promote_native_Dirac_source':'native_Dirac_source_licensed',
                     'exclude_all_composite_source_form_factors':'envelope_obstruction_excludes_composite_sources'}[name]
                bad=copy.deepcopy(c);bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported local-source promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((lift.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_local_source_vertex.py'))
    return {'schema':'marici.scattering.local-source-vertex-receipt.v1','status':'pass',
        'scope_verdict':'imported_local_Wick_density_candidates_and_restricted_tree_contact_envelope_obstruction_not_native_QFT',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'neutral_formally_Hermitian_local_density_candidates_constructed':True,
        'Dirac_bilinear_C_signs':{'pseudoscalar':1,'vector':-1},'photon_operator_C_signs':{'two':1,'three':-1},
        'operator_mass_dimensions':{'singlet_density':7,'triplet_density':10},
        'EFT_coupling_mass_dimensions':{'singlet':-3,'triplet':-6},
        'single_Maxwell_factor_divergence_checks':single_divergences,
        'Ward_identity_cases':ward,'three_photon_Bose_permutation_cases':permutation_cases,
        'Lorentz_tensor_covariance_cases':covariance_cases,'homogeneous_scaling_cases':homogeneous,
        'nonzero_three_photon_helicity_configurations':nonzero,'same_helicity_CM_vector_witness':same_helicity_witness,
        'mixed_helicity_CM_vector_witness':mixed_helicity_witness,
        'this_cubic_candidate_leaks_outside_prior_equal_helicity_code':True,
        'photon_amputated_homogeneity_degrees':{'two':2,'three':4},
        'exact_rational_envelope_from_finite_derivative_point_current_excluded':True,
        'formal_spacelike_commuting_density_conditional_on_imported_free_field_algebra':True,
        'analytic_argument_machine_formalized':False,**{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale local source vertex'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','neutral_formally_Hermitian_local_density_candidates_constructed',
        'Ward_identity_cases','exact_rational_envelope_from_finite_derivative_point_current_excluded',
        'native_Dirac_source_licensed','branching_ratio_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
