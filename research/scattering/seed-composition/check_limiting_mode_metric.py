"""Perron pullback distortion and obstruction to mode-commuting compensation."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import audit as incidence_audit, mm, transpose, eye, encode
from check_segmented_copy_transport import audit as transport_audit
from check_survival_transfer import audit as survival_audit, ring, plus, times, scale

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/limiting-mode-metric.v1.json'


def pgram(E,weights):
    return [[sum_poly([scale(w,row[i]*row[j]) for w,row in zip(weights,E)]) for j in range(2)] for i in range(2)]
def sum_poly(terms):
    out=ring([F(0)])
    for term in terms:out=plus(out,term)
    return out

def pmatmul(A,B):
    return [[sum_poly([times(a,b) for a,b in zip(row,col)]) for col in zip(*B)] for row in A]
def rational_matrix(A):return [[ring([F(x)]) for x in row] for row in A]


def audit():
    previous=survival_audit();transport=transport_audit();incidence=incidence_audit()
    E=transport['matrices']['synchronized_mode_frame']+[[F(0),F(0)] for _ in range(6)]
    one=ring([F(1)]);rho=ring([F(0),F(1)]);inv=ring([-F(1,2),0,0,0,F(16)])
    inv2=times(inv,inv);inv3=times(inv2,inv)
    values=[one,scale(rho,2),scale(inv2,F(1,4)),scale(inv3,F(1,2)),inv,one,scale(inv,F(1,2)),inv2,scale(rho,2)]
    group=previous['classes']['closed_strongly_connected_components'][0]
    cp=[9,10,11,6,7,8,3,4,5,0,1,2,17,15,16,13,14,12]
    h=[None]*18
    for s,v in zip(group,values):h[s]=h[cp[s]]=v
    G=pgram(E,h)
    A=plus(ring([F(4)]),plus(scale(inv2,F(1,2)),inv3))
    B=plus(rho,scale(inv,F(1,2)))
    assert G==[[plus(A,B),B],[B,B]]
    det=plus(times(G[0][0],G[1][1]),scale(times(G[0][1],G[1][0]),-1))
    assert det==times(A,B)
    lo,hi=previous['perron_certificate']['unique_positive_root_bracket']
    # Coarse rational interval bounds suffice; no numerical eigenvector fit.
    Amin=4+1/(2*hi**2)+1/hi**3;Amax=4+1/(2*lo**2)+1/lo**3
    Bmin=lo+1/(2*hi);Bmax=hi+1/(2*lo)
    assert Amin>2*Bmax and Amax<8*Bmin and Bmin>0
    G0=mm(transpose(E),E);assert G0==[[9,1],[1,1]]
    T=incidence['matrices']['reference_mode_step_T'];Gref=[[F(3),F(0)],[F(0),F(1)]]
    assert mm(mm(transpose(T),Gref),T)==Gref
    Tp=rational_matrix(T)
    defect=[[plus(x,scale(y,-1)) for x,y in zip(row,orig)] for row,orig in zip(pmatmul(pmatmul(transpose(Tp),G),Tp),G)]
    assert any(v!=ring([F(0)]) for row in defect for v in row)
    # Every real commuting map is C=aI+bT (T has irreducible degree-two
    # minimal polynomial). These exact coefficient checks certify conformality.
    assert mm(T,T)==[[F(-T[i][j]-int(i==j)) for j in range(2)] for i in range(2)]
    cross=[[x+y for x,y in zip(row,col)] for row,col in zip(mm(transpose(T),Gref),mm(Gref,T))]
    assert cross==[[-v for v in row] for row in Gref]
    inverse_ref=[[F(1,3),F(0)],[F(0),F(1)]]
    assert mm(mm(T,inverse_ref),transpose(T))==inverse_ref
    assert [[x+y for x,y in zip(row,col)] for row,col in zip(mm(T,inverse_ref),mm(inverse_ref,transpose(T)))]==[[-v for v in row] for row in inverse_ref]
    # det(G)/trace(Gref^-1 G)^2 is unchanged by commuting congruence.
    trace=scale(plus(A,scale(B,4)),F(1,3))
    difference=plus(scale(times(A,B),18),scale(times(plus(A,scale(B,4)),plus(A,scale(B,4))),-1))
    assert difference==scale(times(plus(A,scale(B,-8)),plus(A,scale(B,-2))),-1)
    assert difference!=ring([F(0)])
    # Since 2B<A<8B, the invariant exceeds G0's value 1/2.
    # Reflection-compatible diagonal weighting need not preserve the plane.
    assert h[0]!=h[2]
    assert E[0]==[-F(1),F(0)] and E[2]==[F(1),F(0)]
    assert scale(h[0],-1)!=scale(h[2],-1)

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_limiting_mode_metric.py']
    return {
        'schema':'marici.scattering.limiting-mode-metric.v1',
        'status':'limiting_conditioning_distorts_selected_metric_no_scalar_or_reference_commuting_compensation',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'pullback':{'G0':G0,'reference_invariant_metric':Gref,
                     'Gh':'[[A+B,B],[B,B]]','A':'4+1/(2*rho^2)+1/rho^3','B':'rho+1/(2*rho)',
                     'Gh_entries_modulo_quintic':G,'determinant':'A*B',
                     'rational_bounds':{'A':[Amin,Amax],'B':[Bmin,Bmax]},
                     'strict_inequalities':'0<2*B<A<8*B','scalar_multiple_of_G0':False,
                     'invariant_under_reference_T':False,
                     'asymptotic_scope':'E^t diag(q_n) E / rho^n -> c*Gh for the symmetric terminal seed'},
        'commuting_compensation':{'centralizer':'C=a*I+b*T',
                                  'conformal_factor':'k=a^2-a*b+b^2>0 for nonzero C',
                                  'identity':'C^t Gref C=k*Gref',
                                  'congruence_invariant':'det(G)/(trace(Gref^-1 G))^2',
                                  'G0_invariant':'1/2','Gh_invariant':'9*A*B/(A+4*B)^2 > 1/2',
                                  'C_t_Gh_C_equals_scalar_G0_possible':False,
                                  'C_t_Gh_C_equals_scalar_Gref_possible':False,
                                  'scope':'invertible real maps commuting with the unchanged reference mode step'},
        'state_filter':{'reflection_parity_preserved':True,'initial_plane_preserved_by_diag_h':False,
                        'witness':'rows 0 and 2 must be opposite in E, but h0=1 and h2=1/(4*rho^2) differ',
                        'sqrt_h_filter_also_preserves_plane':False},
        'possible_noncommuting_whitening':{'exists_for_positive_Gh':True,
                                          'recipe':'If Gh=U^t U is upper Cholesky, C=U^-1*diag(sqrt(3),1) gives C^t Gh C=Gref',
                                          'commutes_with_reference_T':False,
                                          'preserves_original_step_without_conjugation':False,
                                          'source_authorized':False},
        'boundary':{'all_control_or_dilation_schemes_excluded':False,'native_algebraic_filter_derived':False,
                    'physical_clock_metric_or_photons_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Advance the independently open atlas/seed source-correspondence audit: compare exact source claims and admitted operations with the now-explicit requirements for controller policy, odd preparation, label recombination and algebraic/state-dependent filtering. Keep this conditional construction separate from physical-channel admission.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale limiting-mode receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact Perron pullback has 2B<A<8B; no scalar normalization restores the initial mode metric.')
    print('PASS: centralizer-congruence invariant excludes any compensator commuting with the reference mode step.')
    print('Boundary: noncommuting whitening exists mathematically, but native filtering and physical interpretation remain open.')


if __name__=='__main__':main()
