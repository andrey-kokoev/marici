"""Lift the algebraic split to all twelve boundary occurrences, retaining parity and zero sectors."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, rank, eye, encode
from check_segmented_copy_transport import audit as segmented_audit
from check_graded_boundary_transport import audit as graded_audit, add as madd, scale as mscale
from check_moving_boundary_plane import audit as moving_audit, determinant
from check_algebraic_projector import audit as projector_audit, pmul, psub, pscale, remainder
from check_retained_word_transport import poly, add, sub, mul, scale

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/full-boundary-split.v1.json'


def zero(n):return [[F(0)]*n for _ in range(n)]
def mpadd(a,b):
    n=len(a[0]);return [madd(a[i] if i<len(a) else zero(n),b[i] if i<len(b) else zero(n)) for i in range(max(len(a),len(b)))]
def mpscale(a,c):return [mscale(m,c) for m in a]
def mpshift(a,k):return [zero(len(a[0])) for _ in range(k)]+a

def mpmul(a,b):
    out=[zero(len(a[0])) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=madd(out[i+j],mm(x,y))
    return out


def audit():
    previous=projector_audit();seg=segmented_audit()['matrices']
    graded=graded_audit()['minimal_constant_carrier'];moving=moving_audit()
    A=seg['one_step_boundary_A'];C=mm(seg['internal_exit_B'],seg['internal_entry_D']);K=seg['macro_K']
    source=json.loads((BASE/'three-vertex-candidate.v1.json').read_text(encoding='utf-8'))
    occurrences=[(p,a,b) for p,pair in enumerate(source['displayed_triangle_pairs']) for triangle in pair for a,b in zip(triangle,triangle[1:])]
    relabel={'A':'C','C':'A','B':'B','D':'Ep','Ep':'D','E':'Dp','Dp':'E'}
    permutation=[occurrences.index((1-p,relabel[a],relabel[b])) for p,a,b in occurrences]
    assert permutation==[9,10,11,6,7,8,3,4,5,0,1,2]
    J=[[F(i==permutation[j]) for j in range(12)] for i in range(12)]
    I=eye(12);odd=mscale(madd(I,mscale(J,-1)),F(1,2));even=mscale(madd(I,J),F(1,2))
    assert mm(J,J)==I and mm(J,A)==mm(A,J) and mm(J,C)==mm(C,J)
    H=graded['embedding_H']
    assert mm(J,H)==mscale(H,-1)
    assert rank(mm(odd,K))==rank(mm(even,K))==4
    assert rank([a+b for a,b in zip(H,mm(odd,K))])==4

    # Each pair's six-boundary block has two additional zero eigenvalues.
    z=poly(variable=0);lam=poly(variable=1);z2=mul(z,z)
    A6=[row[:6] for row in A[:6]];C6=[row[:6] for row in C[:6]]
    pencil=[[sub(scale(lam,i==j),add(scale(z,A6[i][j]),scale(z2,C6[i][j]))) for j in range(6)] for i in range(6)]
    zp=[poly(1)]
    for _ in range(5):zp.append(mul(zp[-1],z))
    chi=add(sub(mul(mul(lam,lam),mul(lam,lam)),mul(zp[4],mul(lam,lam))),sub(scale(mul(add(zp[4],zp[5]),lam),-1),zp[5]))
    assert determinant(pencil)==mul(mul(lam,lam),chi)
    # Coefficientwise annihilator lambda*chi, stronger than the characteristic
    # identity lambda^2*chi: the zero sector is semisimple for nonzero z.
    Fseries=[zero(6),A6,C6];powers=[[eye(6)]]
    for _ in range(5):powers.append(mpmul(powers[-1],Fseries))
    annihilator=mpadd(mpadd(powers[5],mpscale(mpshift(powers[3],4),-1)),
                     mpadd(mpscale(mpshift(powers[2],4),-1),mpadd(mpscale(mpshift(powers[2],5),-1),mpscale(mpshift(powers[1],5),-1))))
    assert all(m==zero(6) for m in annihilator)

    # Universal CRT correction: the four-carrier projector alone need not
    # vanish at lambda=0, so remove the zero sector before lifting it.
    tau=poly(variable=0);delta=poly(variable=1);epsilon=poly(variable=2)
    f=[delta,scale(tau,-1),poly(1)];g=[epsilon,tau,poly(1)];characteristic=pmul(f,g)
    c0=mul(delta,epsilon)
    R=add(mul(sub(epsilon,delta),sub(epsilon,delta)),scale(mul(mul(tau,tau),add(delta,epsilon)),2))
    h=[add(scale(mul(tau,tau),2),sub(epsilon,delta)),scale(tau,-2)]
    E=pmul(g,h);N=psub([c0],characteristic);Pi=pmul(N,E);den=mul(c0,R)
    Z=pscale(characteristic,R);Comp=psub(psub([den],Pi),Z)
    modulus=[{}]+characteristic
    for numerator in [Pi,Z,Comp]:
        assert remainder(psub(pmul(numerator,numerator),pscale(numerator,den)),modulus)==[{}]
    for first,second in [(Pi,Z),(Pi,Comp),(Z,Comp)]:assert remainder(pmul(first,second),modulus)==[{}]
    assert remainder(pmul(f,Pi),modulus)==[{}]
    assert remainder(pmul(g,Comp),modulus)==[{}]

    # Exact base-point matrices and source embedding tests.
    K2=mm(K,K);K3=mm(K2,K);K4=mm(K3,K)
    Z0=madd(madd(mscale(K4,-1),K2),madd(mscale(K,2),I))
    Nonzero=madd(I,mscale(Z0,-1))
    naive=mscale(madd(madd(K3,mscale(K2,-1)),mscale(K,-1)),F(1,2))
    selected=mm(Nonzero,naive);complement=madd(madd(I,mscale(Z0,-1)),mscale(selected,-1))
    assert [rank(p) for p in [Z0,selected,complement]]==[4,4,4]
    for p in [Z0,selected,complement]:
        assert mm(p,p)==p and mm(p,K)==mm(K,p)
    assert madd(madd(Z0,selected),complement)==I
    for p,q in [(Z0,selected),(Z0,complement),(selected,complement)]:assert mm(p,q)==zero(12)
    selected_odd=mm(odd,selected);selected_even=mm(even,selected)
    assert rank(selected_odd)==rank(selected_even)==2
    assert mm(selected,H)==mm(H,previous['local_cross_checks']['base_projector'])
    assert mm(selected_odd,H)==mm(selected,H) and mm(selected_even,H)==[[F(0)]*4 for _ in range(12)]
    assert rank(mm(selected,seg['prefix_copy_Q']))==4
    assert rank(mm(selected_even,seg['prefix_copy_Q']))==2
    assert any(selected_odd[i][j] for i in range(6) for j in range(6,12))
    # Any scalar function of the block-diagonal boundary operator remains block
    # diagonal; it cannot equal this cross-pair correlated rank-two projector.
    assert all(selected[i][j]==0 for i in range(6) for j in range(6,12))

    # The naive lift happens to vanish on zero modes exactly at z=1; its actual
    # branch derivative shows why that single fixture is insufficient.
    tau0,tau1=moving['induced_step']['trace_series'][:2]
    d0,d1=moving['induced_step']['determinant_series'][:2]
    e0=-1;e1=-5+d1
    h0=2*tau0*tau0+e0-d0;h1=4*tau0*tau1+e1-d1
    assert h0==0 and e0*h1/F(4)==-F(3,4)

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_full_boundary_split.py']
    return {
        'schema':'marici.scattering.full-boundary-split.v1',
        'status':'full_selected_rank_four_zero_sector_retained_rank_two_requires_parity_selection',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'full_space':{'dimension':12,'per_pair_characteristic':'lambda^2*chi(lambda,z)',
                       'full_characteristic':'lambda^4*chi(lambda,z)^2','annihilator':'lambda*chi(lambda,z)',
                       'positive_axis_ranks':{'zero':4,'selected':4,'other_nonzero':4}},
        'corrected_projectors':{'Z0':'chi(F)/chi(0), chi(0)=-z^5',
                                'N':'I-Z0','selected':'N*g(F)*h(F)/R',
                                'other_nonzero':'I-Z0-selected',
                                'universal_identities_verified_modulo_lambda_chi':True,
                                'naive_zero_mode_value_at_z_one':0,
                                'naive_zero_mode_value_derivative_at_z_one':'-3/4'},
        'correlation_selector':{'graph_reflection':relabel,'occurrence_permutation':permutation,
                                'commutes_with_one_and_two_step_blocks':True,
                                'even_projector':'(I+J)/2','odd_projector':'(I-J)/2',
                                'old_four_carrier':'odd nonzero sector; J H=-H',
                                'selected_even_rank':2,'selected_odd_rank':2,
                                'full_selected_prefix_input_rank_at_one':4,
                                'even_selected_prefix_input_rank_at_one':2,
                                'old_rank_two_projector':'selected * (I-J)/2',
                                'scalar_spectral_function_of_F_alone_selects_odd_copy':False},
        'base_matrices':{'zero':Z0,'selected':selected,'other_nonzero':complement,
                         'selected_odd':selected_odd,'selected_even':selected_even},
        'retention':{'three_way_split_recovers_input_by_sum':True,
                     'six_rank_two_spectral_parity_records_available':True,
                     'zero_or_even_records_silently_discarded':False},
        'boundary':{'odd_parity_preparation_source_selected':False,'independent_photons_constructed':False,
                    'physical_metric_or_clock_derived':False,'physical_annihilation_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Test whether a source-authorized operation prepares the odd correlation sector while retaining its even and zero records; in parallel the independent atlas/seed source-correspondence frontier remains executable.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale full-boundary split receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: full boundary spectrum splits into ranks 4+4+4; zero-corrected algebraic projectors verified.')
    print('PASS: old synchronized rank two is selected odd parity, not the whole rank-four selected spectral sector.')
    print('Boundary: reflection symmetry supplies an observable, not authority to prepare its odd sector or independent photons.')


if __name__=='__main__':main()
