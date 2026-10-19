"""Exact charged-doublet closure criterion, retained leakage and dressed ground control."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_native_endpoint_face_lines import audit as face_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,rank,add,scale,decode,eye,record,load,digest,ROOT,BASE
from assemble_endpoint_charging import geometry,block_diagonal

DEST=BASE/'results/charged-spinor-closure.v1.json'


def zero(n,m=None):return tuple(tuple(ZERO for _ in range(n if m is None else m)) for _ in range(n))
def diagonal(values):return tuple(tuple(A(x) if i==j else ZERO for j in range(len(values))) for i,x in enumerate(values))
def trace(M):return sum((M[i][i] for i in range(len(M))),ZERO)


def audit():
    previous=face_audit();parent=load('research/strominger/results/common-endpoint-charging.json')
    op=parent['source_operators']['electron'];spec=load('research/strominger/contracts/common-endpoint-charging.json')
    beta,eta=F(spec['beta']),F(spec['eta'])
    K=tuple(tuple(decode(x) for x in row) for row in op['kinetic_operator'])
    P=scale(A(F(1,2)),add(eye(4),add(eye(4),scale(A(-1),K))))
    Q=add(eye(4),scale(A(-1),K));R=add(eye(4),scale(A(-1),P))
    assert mm(P,P)==P and rank(P)==rank(R)==2
    assert all(P[i][j]!=ZERO for i in range(4) for j in range(4))
    graph=geometry(4,[tuple(e) for e in op['internal_edges']],op['exterior_ports'])
    V=tuple(tuple(decode(x) for x in row) for row in previous['adapter']['V'])
    D=tuple(tuple(decode(x) for x in row) for row in previous['adapter']['decoder_D'])
    L=mm(V,D);N=mm(mm(V,P),D);polarization=add(eye(8),scale(A(-1),L))
    mismatch=add(L,scale(A(-1),N))
    assert rank(N)==rank(mismatch)==2 and rank(polarization)==4
    rows=[];ranks={};unit_tests=[]
    for q in (-1,1):
        for flux in product(range(-2,3),repeat=4):
            if sum(flux)!=q:continue
            shifts=block_diagonal(graph,q,flux,beta,eta)
            constant=(beta/F(8)+eta/2)*q*q+5*beta*sum(x*x for x in flux)/8
            assert shifts==[constant-beta*q*x/4 for x in flux]
            H=add(K,diagonal(shifts));leak=mm(R,mm(H,P))
            assert leak!=zero(4)
            r=rank(leak);ranks[r]=ranks.get(r,0)+1
            hs=mm(adj(leak),leak)
            mean=sum(shifts)/4
            expected=sum((x-mean)**2 for x in shifts)/3
            assert trace(hs)==A(expected)
            assert expected==beta*beta*q*q*sum((F(x)-F(q,4))**2 for x in flux)/48
            # Minimal selected-line lift of the potential; no field coupling on
            # excluded polarization is inferred. This explicit extension keeps
            # polarization separate but leaks into rank-two line mismatch.
            native_free=add(add(eye(8),scale(A(-1),L)),scale(A(2),add(eye(8),scale(A(-1),N))))
            charged_native=add(native_free,mm(mm(V,diagonal(shifts)),D))
            assert mm(charged_native,V)==mm(V,H)
            assert mm(charged_native,polarization)==scale(A(3),polarization)
            assert mm(polarization,mm(charged_native,N))==zero(8)
            native_leak=mm(mismatch,mm(charged_native,N))
            assert rank(native_leak)==r and native_leak!=zero(8)
            rows.append({'charge':q,'flux':flux,'leak_rank':r,'leak_Hilbert_Schmidt_squared':str(expected)})
        for i in range(4):
            flux=[q*int(j==i) for j in range(4)];shifts=block_diagonal(graph,q,flux,beta,eta)
            H=add(K,diagonal(shifts));leak=mm(R,mm(H,P))
            assert rank(leak)==1 and trace(mm(adj(leak),leak))==A(beta*beta/64)
            assert rank(mm(P,diagonal([int(j==i) for j in range(4)])))==1
            unit_tests.append({'q':q,'lead':i,'leak_rank':1,'leak_squared':str(beta*beta/64)})
    assert len(rows)==160 and set(ranks)=={1,2}
    # Universal diagonal test: [diag(d),P]_ij=(d_i-d_j)P_ij, and all
    # offdiagonals are nonzero. Closure iff d is constant.
    for values in ([1]*4,[0,1,0,0],[2,-1,3,0]):
        pot=diagonal(values);comm=add(mm(pot,P),scale(A(-1),mm(P,pot)))
        assert (comm==zero(4))==(len(set(values))==1)
    # Exact source unit-flux ground: r=(v+sqrt(v²+4))/2, r²-vr=1,
    # vector r*e_i+Qe_i. Its mismatch fraction is 1/2-1/sqrt(v²+4).
    v=beta/4;radicand=v*v+4
    def reduce_r(coefficients):
        p=list(coefficients)+[F(0)]*max(0,2-len(coefficients))
        for j in range(len(p)-1,1,-1):
            c=p[j];p[j]=0;p[j-1]+=v*c;p[j-2]+=c
        return p[:2]
    # H0(r e+Qe)=(r-1-vr)e+(1-r)Qe;
    # (1-r)(r e+Qe) has the same coefficients modulo r²-vr-1.
    assert reduce_r([-1,1-v])==reduce_r([0,1,-1])
    assert reduce_r([1,-1])==[1,-1]
    assert reduce_r([v*v,-4*v,4])==[radicand,0]  # (2r-v)^2=v²+4
    rootlo=F(0);roothi=radicand+1
    for _ in range(70):
        mid=(rootlo+roothi)/2
        if mid*mid<radicand:rootlo=mid
        else:roothi=mid
    fraction_lo=F(1,2)-1/rootlo;fraction_hi=F(1,2)-1/roothi
    assert 0<fraction_lo<fraction_hi<F(1,2)
    for i in range(4):
        e=tuple((ONE if j==i else ZERO,) for j in range(4));qe=mm(Q,e)
        assert mm(adj(e),qe)==zero(1) and mm(adj(qe),qe)==eye(1)
        assert mm(P,e)==scale(A(F(1,2)),add(e,qe))
        assert mm(R,e)==scale(A(F(1,2)),add(e,scale(A(-1),qe)))
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_charged_spinor_closure.py'}
    return {
        'schema':'marici.scattering.charged-spinor-closure.v1',
        'status':'all_unit_charge_integer_fluxes_break_original_doublet_closure_dressed_ground_contains_line_mismatch',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'closure_criterion':{'selected_projector':'P=(I+Q)/2','diagonal_preserves_P':'all four entries equal',
                              'proof':'Hermitian closure is equivalent to commutation; [diag(d),P]_ij=(d_i-d_j)P_ij with every P_ij nonzero.',
                              'endpoint_diagonal':'c-(beta*q/4)*ell_i',
                              'constant_c':'(beta/8+eta/2)*q^2+(5*beta/8)*||ell||^2',
                              'unit_charge_integer_flux_preserves_P':False,
                              'reason':'For q=+/-1 and beta>0, closure requires equal integer ell_i, but 4*ell_i=q is impossible.',
                              'general_exceptions':'q=0, or uniform flux with q divisible by four, or turning off beta outside the tested positive-coupling contract'},
        'leakage':{'formula':'|| (I-P) diag(d) P ||_HS^2 = sum_i(d_i-mean(d))^2/3',
                    'endpoint_formula':'beta^2*q^2/48 * sum_i(ell_i-q/4)^2',
                    'finite_flux_checks':rows,'rank_counts':ranks,'unit_flux_checks':unit_tests,
                    'unit_flux_short_time':'mismatch norm from initial coherent y is t^2*||leak*y||^2+O(t^3), not a derived physical rate'},
        'retained_native_split':{'coherent_rank':2,'line_mismatch_rank':2,'polarization_rank':4,
                                 'potential_extension':'H_native+V*diag(shifts)*D; keeps the free 3*(I-L) polarization block without deriving a field coupling there',
                                 'coherent_to_mismatch_leak_checked':True,
                                 'coherent_to_polarization_leak_in_this_declared_extension':False},
        'dressed_unit_flux_ground':{'v':'beta/4','r':'(v+sqrt(v^2+4))/2','vector':'r*e_i+Q*e_i',
                                    'unshifted_eigenvalue':'1-r',
                                    'algebraic_identity':'r^2-v*r-1=0',
                                    'norm_squared':'r^2+1','coherent_norm_squared':'(r+1)^2/2',
                                    'mismatch_norm_squared':'(r-1)^2/2',
                                    'mismatch_fraction':'1/2-1/sqrt(v^2+4)',
                                    'fixture_v':str(v),'mismatch_fraction_rational_bounds':[str(fraction_lo),str(fraction_hi)],
                                    'original_coherent_doublet_ground':False,
                                    'owner_ground_multiplicity':'four orthogonal lead-flux sectors, not a preserved two-dimensional logical spin ground'},
        'boundary':{'all_dressed_spinor_sectors_impossible':False,'physical_spin_or_charge_lost':False,
                    'excluded_polarization_field_coupling_derived':False,'formal_outcome_admitted':False,
                    'shared_sources_or_receipts_rewritten':False},
        'next_gate':'Construct each unit-flux dressed low spectral projector and test whether one common rank-two carrier or source-compatible spin transport works across all four flux-labelled blocks. Keep field labels and all mismatch/polarization records.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale charged-doublet receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: diagonal closure iff constant; every integer unit-charge flux breaks the original coherent doublet.')
    print('PASS: exact leakage formula and 160 flux checks; dressed unit-flux ground has strictly positive line mismatch.')
    print('Boundary: charged low sectors may be reconstructed; no physical spin loss or annihilation conclusion.')


if __name__=='__main__':main()
