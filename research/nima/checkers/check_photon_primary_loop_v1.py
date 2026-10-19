"""Offline primary-source regression for photon one-loop coefficients (exact Q arithmetic)."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_normalization_v1 as norm
CONTRACT=HOME/'contracts/photon-primary-loop-v1.json'
PROOF=HOME/'photon-primary-loop-v1.md'
TEST=HOME/'checkers/test_photon_primary_loop_v1.py'
MANIFEST=HOME/'scc-models/photon-primary-loop-v1.json'
CAPTURE=HOME/'checkers/capture_photon_primary_source_v1.py'
PROVENANCE=HOME/'sources/photon-scattering-2024-provenance.json'
RESULT=HOME/'results/photon-primary-loop-v1.json'
PDF_SHA='886acd1357146f94cde8e503e919d5a36d4b6d7cab2bf519eb08e51472d535eb'
TEX_SHA='293b917c57639e64e3db4f059e77a70e6370c7e5b04a5979d683c879654c59da'
PDF_TEXT_SHA='8470ea45e95f7200cc48194ab07eefab238351d8411ed62844f6f0ad99ba9cf5'
ZERO=(Q(),Q(),Q())


def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def square(v):
    g,f=v;return g*g,2*g*f,f*f

def evaluate(p,g,f):return p[0]*g*g+p[1]*g*f+p[2]*f*f

def compact(text):return re.sub(r'\s+','',text)


def parse_primary_betas(text):
    """Recognize only the printed rational forms in eq. (1.8); do not execute TeX."""
    text=compact(text)
    def one(pattern):
        matches=re.findall(pattern,text)
        assert len(matches)==1,'ambiguous or unsupported primary coefficient syntax'
        return tuple(map(int,matches[0] if isinstance(matches[0],tuple) else (matches[0],)))
    f,g,d=one(r'\\beta_\{1,1\}&=-\\frac\{(\d+)f_2\^2\+(\d+)g_2\^2\}\{(\d+)\\pi\^2\}')
    d12,=one(r'\\beta_\{1,2\}=\\frac\{f_2\^2\}\{(\d+)\\pi\^2\}')
    d13,=one(r'\\beta_\{1,3\}&=-\\frac\{g_2\^2\}\{(\d+)\\pi\^2\}')
    n2,d2=one(r'\\beta_\{2\}=-\\frac\{(\d+)f_2g_2\}\{(\d+)\\pi\^2\}')
    return {'beta11':(-Q(g,d),Q(),-Q(f,d)),
            'beta12':(Q(),Q(),Q(1,d12)),
            'beta13':(-Q(1,d13),Q(),Q()),
            'beta2':(Q(),-Q(n2,d2),Q())}


def check_conventions(text):
    text=compact(text)
    anchors=(r'\Phi_1(s,t,u)&=g_2s^2',r'\Phi_2(s,t,u)&=f_2(s^2+t^2+u^2)',
             r'\Phi_3(s,t,u)=\Phi_1(u,t,s)',r'\frac{1}{32\pi}\int_0^\pi',
             r'1+2i\Phi_3^\ell(s)',r'\frac{1}{\sqrt2}',r'S=1+iT',
             r'\times(2\pi)^3\delta^{(3)}',r'2\Im\mathbbF_4^\ell=(\mathbbF_2^\ell)^2',
             r'\log(-s)=\log(|s|)-i\pi\theta(s)')
    for anchor in anchors:assert anchor in text,'missing primary convention: '+anchor
    return len(anchors)


def load_primary():
    p=json.loads(PROVENANCE.read_text(encoding='utf-8'))
    assert p['input_sha256']['pdf']==PDF_SHA
    assert p['snapshot_sha256']=={'tex_excerpt':TEX_SHA,'pdf_text_excerpt':PDF_TEXT_SHA}
    files={k:PROVENANCE.parent/v for k,v in p['snapshot_files'].items()}
    for k,path in files.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest()==p['snapshot_sha256'][k],'changed primary excerpt'
    pdf=files['pdf_text_excerpt'].read_text(encoding='utf-8')
    assert 'JHEP10(2024)103' in pdf and '(1.8)' in pdf and '(C.4)' in pdf
    return p,files,files['tex_excerpt'].read_text(encoding='utf-8')


def derive_betas():
    """From Born angular polynomials and 2 Im F4=F2^2; pi factors stripped by grade."""
    ct=norm.ct;integrate=norm.mom.integrate
    # s=1. t=-alpha, u=-(1-alpha). Independent tree angular data, not loop targets.
    p=[Q(2),Q(-2),Q(2)]  # 1+alpha^2+(1-alpha)^2
    P2=[Q(1),Q(-6),Q(6)]
    d22=[Q(1),Q(-2),Q(1)]
    E0=integrate(p);E2=integrate(ct.multiply(P2,p))
    I22=integrate(ct.multiply(d22,d22))
    assert p==[E0+5*E2*P2[0],5*E2*P2[1],5*E2*P2[2]],'unretained scalar Born partial wave'
    # pi times physical Born eigenvalues. Equal-helicity F=Phi1+/-Phi2.
    plus=(Q(1,16),E0/16);minus=(Q(1,16),-E0/16)
    im_phi1_J0=scale(Q(1,4),add(square(plus),square(minus)))
    im_phi2_J0=scale(Q(1,4),add(square(plus),scale(-1,square(minus))))
    im_phi1_J2=scale(Q(1,2),square((Q(),E2/16)))
    # Reconstruct M with 16*pi*(2J+1); P2=1-6*tu/s^2.
    D=scale(16,add(im_phi1_J0,scale(5,im_phi1_J2)))
    beta12=scale(16*5*6,im_phi1_J2)
    O=scale(16,im_phi2_J0)
    # Mixed physical F=2 Phi3, not Phi3. Divide its Im by two on reconstruction.
    mixed_F=(2*I22/16,Q())
    im_phi3_J2=scale(Q(1,4),square(mixed_F))
    M=scale(16*5,im_phi3_J2)
    betas={'beta11':scale(-1,D),'beta12':beta12,'beta13':scale(-1,M),'beta2':scale(-1,O)}
    return betas,{'E0':str(E0),'E2':str(E2),'I22':str(I22)}


def assert_primary_matches(parsed):
    derived,_=derive_betas()
    assert parsed==derived,{k:(parsed[k],derived[k]) for k in derived if parsed[k]!=derived[k]}


def forward_abs(parsed,g,f,branch_sign=-1):
    # Abs log(-s-i0)=-pi, so pi times cut is -pi^2 times the log coefficient.
    return tuple(branch_sign*evaluate(parsed[k],g,f) for k in ('beta11','beta2','beta13'))


def validate_contract(c):
    assert c['schema']=='marici.photon-primary-loop.v1'
    assert c['owner']=='marici.Nima' and c['predecessor']=='photon-normalization-v1'
    assert c['kernel_dictionary']=='T_red=M/(16*pi)'
    assert c['coefficient_pi_power']==-2
    assert c['logarithm_boundary']=='log(-s-i0)=log(s)-i*pi for s>0'
    assert c['quadratic_basis']==['g2_gamma^2','g2_gamma*f2_gamma','f2_gamma^2']
    for k in ('primary_pdf_text_inspected_against_author_TeX','primary_source_regression_independently_verified',
              'four_loop_coefficients_matched_as_exact_polynomials','forward_invisible_log_coefficient_beta12_checked'):
        assert c[k] is True,k
    for k in ('existing_reduced_coefficients_rescaled','paper_g2_equals_project_Dirac_g2',
              'off_forward_covariant_tensor_constructed','finite_matching_coefficients_fixed',
              'global_UV_positivity_assumptions_admitted','native_preparation_or_physical_rates_derived','all_paper_claims_verified'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    provenance,files,text=load_primary();anchors=check_conventions(text)
    parsed=parse_primary_betas(text);derived,moments=derive_betas();assert_primary_matches(parsed)
    predecessor=norm.build()
    assert predecessor['status']=='pass_with_primary_source_residual' # immutable earlier-stage provenance
    cut=forward_abs(parsed,Q(1,4),Q(-1,4))
    fm,fp,mixed=norm.mom.pair_eigenvalues(2,2);reduced=((fm+fp)/2,(fp-fm)/2,mixed)
    assert cut==tuple(x/16 for x in reduced)
    assert tuple(map(str,cut))==('19/2560','-5/768','1/1280')
    log_control={k:str(evaluate(v,Q(1,4),Q(-1,4))) for k,v in parsed.items()}
    # Independent forward Gram check for each coordinate of the GF quadratic basis, not a fitted factor.
    for g,f in ((Q(1),Q()),(Q(),Q(1)),(Q(1),Q(1)),(Q(2,3),Q(-4,5))):
        assert forward_abs(parsed,g,f)==norm.direct_invariant_pi_cut(g,f)
    # Hostile beta12 preserves every forward target, but fails the independent J2 equation.
    bad_text=text.replace(r'\frac{f_2^2}{240\pi^2}',r'\frac{f_2^2}{120\pi^2}')
    assert bad_text!=text;bad=parse_primary_betas(bad_text)
    assert forward_abs(bad,Q(1,4),Q(-1,4))==cut
    hostile_delta=add(bad['beta12'],scale(-1,derived['beta12']))
    assert hostile_delta==(Q(),Q(),Q(1,240))
    refused=[]
    try:assert_primary_matches(bad)
    except AssertionError:refused.append('forward_invisible_beta12_factor_two')
    else:raise AssertionError('forward-only comparison silently admitted an angular error')
    assert forward_abs(parsed,Q(1,4),Q(-1,4),branch_sign=1)!=cut
    refused.append('opposite_log_rim_sign')
    assert tuple(x*32 for x in cut)!=reduced;refused.append('double_count_Bose_phase_volume')
    for k in ('off_forward_covariant_tensor_constructed','finite_matching_coefficients_fixed',
              'global_UV_positivity_assumptions_admitted','native_preparation_or_physical_rates_derived','all_paper_claims_verified'):
        try:
            bad_c=copy.deepcopy(c);bad_c[k]=True;validate_contract(bad_c)
        except AssertionError:refused.append(k)
        else:raise AssertionError('unsupported primary-text promotion: '+k)
    paths={ROOT/p for p in predecessor['source_sha256']}
    paths.update((CONTRACT,PROOF,TEST,MANIFEST,CAPTURE,PROVENANCE,Path(__file__).resolve(),*files.values()))
    return {'schema':'marici.photon-primary-loop-receipt.v1','status':'pass',
        'scope':'primary_source_normalization_and_four_one_loop_coefficients_not_a_full_off_forward_tensor',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'primary_pdf_sha256':PDF_SHA,'primary_convention_anchors':anchors,'partial_wave_angular_moments':moments,
        'pi_squared_beta_quadratic_coordinates':{k:list(map(str,v)) for k,v in parsed.items()},
        'pi_squared_beta_at_common_Born_R_s_squared':log_control,
        'pi_times_invariant_B_std_D_O_M':list(map(str,cut)),'reduced_B_D_O_M':list(map(str,reduced)),
        'polynomial_identity_coefficients_checked':sum(len(v) for v in parsed.values()),
        'forward_invisible_beta12_hostile_residual':list(map(str,hostile_delta)),
        'historical_predecessor_source_flag_left_unchanged':True,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');a=parser.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale primary-loop receipt'
    else:
        RESULT.parent.mkdir(parents=True,exist_ok=True)
        RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','primary_source_regression_independently_verified',
        'pi_times_invariant_B_std_D_O_M','pi_squared_beta_at_common_Born_R_s_squared','existing_reduced_coefficients_rescaled')}))

if __name__=='__main__':main()
