"""General degree2-by-degree3 photon Born interference, with coupled Bose waves."""
import argparse
from fractions import Fraction as Q
from itertools import product
from math import factorial
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_degree5_cut_v1 as family
base=family.w
CONTRACT=HOME/'contracts/photon-general-degree5-cut-v1.json';PROOF=HOME/'photon-general-degree5-cut-v1.md'
TEST=HOME/'checkers/test_photon_general_degree5_cut_v1.py';MANIFEST=HOME/'scc-models/photon-general-degree5-cut-v1.json'
RESULT=HOME/'results/photon-general-degree5-cut-v1.json'
NAMES=('g2','f2','g3','f3','h3')
MONOMIALS=('g2*g3','g2*f3','g2*h3','f2*g3','f2*f3','f2*h3')
K=(Q(),Q(1),Q(-1)) # d^2_02 = sqrt(6)*K


def unit_born():
    data=[[[] for _ in base.PHI] for _ in NAMES]
    for c,s in ((Q(1),Q()),(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))):
        rows=base.amplitude_rows(c,s)
        for n in range(5):
            for i,row in enumerate(rows):data[n][i].append((s*s,row[n]))
    return tuple(tuple(family.interpolate(points) for points in column) for column in data)


def project(phi):
    wave=dict(family.project((phi,))[0])
    # Store the coefficient b in physical F02=sqrt(6)*b, avoiding approximate radicals.
    b=family.integral(family.mul(K,phi[4]))/8
    assert family.scale(240*b,K)==phi[4], 'unretained single-minus Born wave'
    wave['off']=b
    return wave


def sym_product(A,B):
    """(AB+BA)/2 for [[a,sqrt(6)b],[sqrt(6)b,d]], in (a,b,d) coordinates."""
    a,b,d=A;e,f,h=B
    return a*e+6*b*f,(a*f+b*h+e*b+f*d)/2,d*h+6*b*f


def reconstruct(A,B):
    D=O=M=(Q(),)
    for J in (0,2):
        if J==0:p=A['plus'][0]*B['plus'][0]
        else:p=sym_product((A['plus'][2],A['off'],A['mixed'][0]),(B['plus'][2],B['off'],B['mixed'][0]))[0]
        minus=A['minus'][J]*B['minus'][J]
        D=family.add(D,family.scale(8*(2*J+1)*(p+minus),family.LEGENDRE[J]))
        O=family.add(O,family.scale(8*(2*J+1)*(p-minus),family.LEGENDRE[J]))
    J2=sym_product((A['plus'][2],A['off'],A['mixed'][0]),(B['plus'][2],B['off'],B['mixed'][0]))
    M=family.add(family.scale(40*J2[2],family.D22[0]),family.scale(56*A['mixed'][1]*B['mixed'][1],family.D22[1]))
    H=family.scale(240*J2[1],K)
    return D,O,M,H


def inventory():
    born=unit_born();waves=tuple(project(phi) for phi in born)
    cuts=tuple(reconstruct(waves[i],waves[j]) for i in (0,1) for j in (2,3,4))
    return born,waves,cuts


def combine(cuts,weights):
    out=[(Q(),) for _ in range(4)]
    for case,c in zip(cuts,weights):
        for i,p in enumerate(case):out[i]=family.add(out[i],family.scale(c,p))
    return tuple(out)


def coefficient_map(cuts):
    return tuple(tuple(case[r][n] if n<len(case[r]) else Q() for case in cuts)
                 for r in range(4) for n in range(max(len(case[r]) for case in cuts)))


def square_psd(a,b,d):
    # Square of a real symmetric physical 2x2 wave: no degree-six cut inventory claimed.
    x=a*a+6*b*b;y=b*(a+d);z=d*d+6*b*b
    return x>=0 and z>=0 and x*z-6*y*y==(a*d-6*b*b)**2>=0


def validate(c):
    assert c['schema']=='marici.photon-general-degree5-cut.v1' and c['owner']=='marici.Nima'
    assert c['coupling_order']==list(NAMES) and c['bilinear_order']==list(MONOMIALS)
    for k in ('general_leading_degree5_Born_cut_inventory_constructed','coupled_single_minus_Bose_wave_retained',
              'six_source_monomials_retained_with_rank_four_readout','restricted_R_family_reduction_verified'):
        assert c[k] is True,k
    for k in ('general_log_window_tensor_constructed','signed_interference_assumed_positive',
              'couplings_selected_from_cut_readout','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parent=family.build()
    text=base.primary.compact(base.primary.load_primary()[2])
    for anchor in (r'2\Phi_5^\ell(s)',r'2\Phi_3^\ell(s)',r'\frac{1}{32\pi}'):
        assert anchor in text,'missing physical Bose/partial-wave source anchor'
    # Spin-2 finite Wigner sum: sqrt(96)/4=sqrt(6), with positive sign.
    assert factorial(2)**2*factorial(4)==96 and factorial(2)**2==4
    assert 6*family.integral(family.mul(K,K))==Q(1,5)
    born,waves,cuts=inventory()
    # Explicit general polynomial formulas, checked against matrix projection rather than fed to it.
    expected=(
        ((Q(1,16),),(Q(),),(Q(-1,48),Q(1,24),Q(-1,48)),(Q(),)),
        ((Q(),),(Q(1,96),),(Q(),),(Q(),)),
        ((Q(),),(Q(),),(Q(),),(Q(),Q(1,80),Q(-1,80))),
        ((Q(),),(Q(5,48),),(Q(),),(Q(),)),
        ((Q(1,60),Q(1,240),Q(-1,240)),(Q(),),(Q(),),(Q(),)),
        ((Q(),),(Q(),),(Q(),),(Q(),Q(1,480),Q(-1,480))))
    assert cuts==expected,(cuts,expected)
    R=(Q(1,16),Q(-3,16),Q(),Q(-1,16),Q(3,16),Q())
    restricted=combine(cuts,R);target=family.reconstruct(family.project(family.born_polynomials()))
    assert restricted[:3]==target and restricted[3]==(Q(),)
    # Source/readout distinction: six bilinear coordinates, not six independent cut responses.
    C=coefficient_map(cuts);_,pivots=base.reduced_rows(C);kernel=base.nullspace(C)
    assert len(pivots)==4 and kernel==((Q(),Q(-10),Q(),Q(1),Q(),Q()),(Q(),Q(),Q(-1,6),Q(),Q(),Q(1)))
    assert cuts[2][3]!=(Q(),) and cuts[5][3]!=(Q(),)
    assert combine(cuts,(Q(),Q(),Q(1),Q(),Q(),Q(-6)))[3]==(Q(),)
    # Dropping the source's factor two on F02 halves the induced single-minus section.
    bad=dict(waves[4]);bad['off']/=2
    assert reconstruct(waves[0],bad)[3]==family.scale(Q(1,2),cuts[2][3])
    assert reconstruct(waves[0],bad)[3]!=cuts[2][3]
    # Interference can be indefinite even though the complete Born wave square is PSD.
    A=(waves[1]['plus'][2],waves[1]['off'],waves[1]['mixed'][0])
    B=(waves[4]['plus'][2],waves[4]['off'],waves[4]['mixed'][0]);p=sym_product(A,B)
    determinant=p[0]*p[2]-6*p[1]*p[1];assert determinant<0
    psd=0
    for values in product((Q(-1),Q(),Q(1)),repeat=5):
        a=b=d=Q()
        for weight,wv in zip(values,waves):
            a+=weight*wv['plus'][2];b+=weight*wv['off'];d+=weight*wv['mixed'][0]
        assert square_psd(a,b,d);psd+=1
    # A fifth angle checks each tensor-derived unit-coupling input polynomial.
    c0,s0=Q(7,25),Q(24,25);rows=base.amplitude_rows(c0,s0)
    for j,phis in enumerate(born):
        for i,p in enumerate(phis):assert family.evaluate(p,s0*s0)==rows[i][j]
    refused=['drop_single_minus_off_diagonal_Bose_wave','omit_factor_two_on_Phi5','identify_six_sources_with_four_cut_responses','assume_signed_interference_PSD']
    for key in ('general_log_window_tensor_constructed','signed_interference_assumed_positive',
                'couplings_selected_from_cut_readout','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported general-cut promotion: '+key)
    paths={ROOT/p for p in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    enc=lambda p:list(map(str,p))
    return {'schema':'marici.photon-general-degree5-cut-receipt.v1','status':'pass',
        'scope':'general_real_parity_even_degree2_by_degree3_Born_interference_right_cut_not_full_log_window',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'coupling_order':list(NAMES),'bilinear_order':list(MONOMIALS),'angular_variable':'alpha=(1-z)/2',
        'unit_coupling_Born_Phi':[[enc(p) for p in phis] for phis in born],
        'pi_times_unit_Bose_waves':[{k:str(v) if isinstance(v,Q) else enc(v) for k,v in wv.items()} for wv in waves],
        'pi_times_cut_D_O_M_Phi5':[[enc(p) for p in case] for case in cuts],
        'source_coordinate_dimension':6,'cut_readout_rank':4,'readout_kernel':[enc(v) for v in kernel],
        'single_minus_g2_h3_coefficient':'1/80','single_minus_f2_h3_coefficient':'1/480',
        'single_minus_polynomial':'alpha*(1-alpha)*(6*g2+f2)*h3/480',
        'restricted_R_family_match':True,'complete_wave_square_PSD_controls':psd,
        'indefinite_interference_J2_determinant':str(determinant),
        'general_partial_wave_proof_machine_formalized':False,**{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale general degree-five cut receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','source_coordinate_dimension','cut_readout_rank','single_minus_polynomial','restricted_R_family_match','general_log_window_tensor_constructed')}))

if __name__=='__main__':main()
