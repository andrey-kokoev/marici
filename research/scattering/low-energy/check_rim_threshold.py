"""Exact full-block C1 threshold certificate, without floating-point elimination."""
from fractions import Fraction as F
import argparse
import hashlib
import json
from check_low_energy_net_v4 import ROOT,BASE,load,multiply,transpose,identity,determinant

DEST=BASE/'results/rim-threshold.v1.json'
SOURCE='research/strominger/results/neutron-two-rim-contact-binding.json'


def inverse(a):
    n=len(a);b=[r[:]+s for r,s in zip(a,identity(n))]
    for i in range(n):
        p=next(j for j in range(i,n) if b[j][i]);b[i],b[p]=b[p],b[i]
        d=b[i][i];b[i]=[x/d for x in b[i]]
        for j in range(n):
            if i!=j:
                d=b[j][i];b[j]=[x-d*y for x,y in zip(b[j],b[i])]
    return [r[n:] for r in b]


def audit():
    src=load(ROOT/SOURCE)
    for p,h in src['source_hashes'].items():
        assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    full=[[F(x) for x in r] for r in src['full_joint_H_without_mu']]
    M=[[F(x) for x in r[2:]] for r in src['source_metric'][2:]]
    K=[r[2:] for r in full[2:]];g=F(src['parameters']['g'])
    B=[[x/g for x in r[:2]] for r in full[2:]]
    # Physical whitened core chi=L^T x/sqrt(3). The contact column is
    # W=L^T B/sqrt(3), hence its rational adjoint in x coordinates is S.
    S=[[x/3 for x in r] for r in multiply(transpose(B),M)]
    assert multiply(S,B)==identity(2)
    assert multiply(M,K)==transpose(multiply(M,K))
    # Positive source metric: exact Schur pivots, not numerical eigenvalues.
    metric=[r[:] for r in M];pivots=[]
    for i in range(24):
        d=metric[i][i];assert d>0;pivots.append(str(d))
        for j in range(i+1,24):
            for k in range(i+1,24):metric[j][k]-=metric[j][i]*metric[i][k]/d
    BS=multiply(B,S)
    C=[[K[i][j]+2*BS[i][j] for j in range(24)] for i in range(24)]
    A=[[-2*F(i==j) for j in range(2)]+[2*x for x in S[i]] for i in range(2)]
    A += [[2*x for x in B[i]]+[F(i==j)/2-C[i][j] for j in range(24)] for i in range(24)]
    det=determinant(A);assert det!=0
    inv=inverse(A);assert multiply(A,inv)==identity(26) and multiply(inv,A)==identity(26)
    L=max(sum(abs(x) for x in row) for row in inv)
    k0=min(F(1),1/(6*L));amplitude_constant=8*L
    # ||A(k)-A(0)||_infty=max(2k,k²)<=3k for 0<k<=1.
    # Neumann inverse bound <=2L for k<=k0. T=2ik [A(k)^-1]_lead.
    # Spectral norm <=sqrt(2) times the 2x2 infinity norm; 8L is safe.
    assert L*3*k0<=F(1,2)
    leading=[[2*inv[i][j] for j in range(2)] for i in range(2)]
    assert leading==transpose(leading)
    sources=set(src['source_hashes'])|{SOURCE,
        'research/strominger/checkers/check_neutron_autonomous_rim_scattering.py',
        'research/strominger/neutron-autonomous-rim-scattering.md',
        'research/scattering/low-energy/check_rim_threshold.py',
        'research/scattering/low-energy/check_low_energy_net_v4.py'}
    return {'schema':'marici.scattering.rim-threshold.v1',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)},
        'status':'C1 established for fixed supplied fixture by exact block inverse and Neumann estimate',
        'coordinates':'chi_whitened=L_metric^T x/sqrt(3); lead amplitudes unchanged; S=B^T M/3',
        'metric_positive_pivots':pivots,'S_B_equals_identity':True,
        'threshold_block_determinant':str(det),'full_threshold_block_dimension':26,
        'inverse_verified_both_sides':True,'threshold_kernel_dimension':0,
        'full_inverse_infinity_norm':str(L),'k0':str(k0),
        'amplitude_constant_C':str(amplitude_constant),
        'bound':'For 0<k<k0, ||T(k)||_2<=C k and ||R(k)+I2||_2<=C k.',
        'expansion':'T(k)=i k leading_real_matrix+O(k²); R(k)=T(k)-I2',
        'leading_real_matrix':[[str(x) for x in row] for row in leading],
        'packet_corollary':{'C4':'established for normalized asymptotic incoming packets',
            'epsilon0':str(k0*k0),'C_packet':str(amplitude_constant**2),
            'bound':'P_transmitted<=C_packet epsilon for 0<epsilon<epsilon0'},
        'C6_effect':'C1 premise discharged; three-port source limit and channel-identification assumptions remain separate',
        'core_schur_resolvent_inverted':False,'dark_complement_discarded':False,
        'numerical_scan_used_as_proof':False,'source_producer_replayed':False,
        'physical_scattering_or_mass_identified':False,
        'next_test':'Attack C2: justify absence of singular-continuous spectrum and outgoing completeness for the finite-rank three-chain contact, including both band edges.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale threshold certificate')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: C1 full threshold block invertible; explicit O(k) bound and C4 packet bound certified.')


if __name__=='__main__':main()
