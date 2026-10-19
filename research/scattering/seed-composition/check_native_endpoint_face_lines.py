"""Exact weighted face-line adapter and its conjugate-source boundary."""
from fractions import Fraction as F
from itertools import combinations
import argparse
import json

from check_source_charge_sector_bridge import audit as sector_audit, conjugate
from check_native_intrinsic_spinor_adapter import native_decode
from check_five_cell_attachment_bridge import (
    A,ZERO,ONE,mm,adj,rank,add,scale,decode,eye,record,load,digest,ROOT,BASE)
from check_diagonal_spin_networks import CI,S3

DEST=BASE/'results/native-endpoint-face-lines.v1.json'


def zeros(n,m):return tuple(tuple(ZERO for _ in range(m)) for _ in range(n))
def column(v):return tuple((x,) for x in v)


def audit():
    previous=sector_audit()
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    P=[tuple(tuple(native_decode(x) for x in row) for row in p) for p in native['face_projectors']]
    L=tuple(tuple(P[i//2][i%2][j%2] if i//2==j//2 else ZERO for j in range(8)) for i in range(8))
    N=tuple(tuple(mm(P[i//2],P[j//2])[i%2][j%2]/2 for j in range(8)) for i in range(8))
    H=add(add(eye(8),scale(A(-1),L)),scale(A(2),add(eye(8),scale(A(-1),N))))
    K=tuple(tuple(decode(x) for x in row) for row in load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));assert adj(Q)==Q and mm(Q,Q)==eye(4)
    # Rooted gauge: use the same source projector column, then the actual
    # endpoint anchor overlap convention. Verify every non-anchor overlap too.
    anchor=tuple(P[0][i][0] for i in range(2));n0=mm(adj(column(anchor)),column(anchor))[0][0]
    assert n0==A(F(1,2))+S3/6
    w=[anchor]
    for i in range(1,4):w.append(tuple(row[0]/Q[i][0] for row in mm(P[i],column(anchor))))
    V=tuple(tuple(w[j][i%2] if i//2==j else ZERO for j in range(4)) for i in range(8))
    D=scale(n0.inverse(),adj(V));R=add(eye(8),scale(A(-1),L))
    assert mm(adj(V),V)==scale(n0,eye(4)) and mm(D,V)==eye(4) and mm(V,D)==L
    assert rank(V)==rank(R)==4
    assert mm(H,V)==mm(V,K) and mm(D,mm(H,V))==K
    assert mm(H,R)==scale(A(3),R)
    assert mm(D,R)==zeros(4,8)
    assert add(mm(V,D),R)==eye(8)
    assert add(mm(mm(adj(D),scale(n0,eye(4))),D),mm(adj(R),R))==eye(8)
    selected=mm(D,mm(N,V))
    assert selected==scale(A(F(1,2)),add(eye(4),Q))
    assert rank(selected)==2 and mm(K,selected)==zeros(4,4)
    # Both L/G/N stage operators are transported, in addition to the source
    # kinetic defect H. L becomes I; G=N become the selected rank-two projector.
    assert mm(D,mm(L,V))==eye(4)
    assert mm(N,V)==mm(V,selected)
    loops=[]
    for i,j,k in combinations(range(4),3):
        overlap_loop=(S3*Q[j][i])*(S3*Q[k][j])*(S3*Q[i][k])
        assert overlap_loop in (CI,-CI)
        loops.append({'face':[i,j,k],'loop_phase':overlap_loop.record(),
                      'conjugate_loop_phase':overlap_loop.flip(8).record()})
        assert overlap_loop.flip(8)==-overlap_loop
    # Exact relation to the owner's arbitrary nonzero-column weighted frame:
    # balancing and phases are a diagonal coordinate adapter, not a new K.
    oldV=tuple(tuple(P[j][i%2][0] if i//2==j else ZERO for j in range(4)) for i in range(8))
    norms=[mm(adj(column(tuple(P[j][i][0] for i in range(2)))),column(tuple(P[j][i][0] for i in range(2))))[0][0] for j in range(4)]
    alpha=[]
    for j in range(4):
        i=next(i for i in range(2) if P[j][i][0]!=ZERO)
        a=w[j][i]/P[j][i][0];alpha.append(a)
        assert all(w[j][k]==a*P[j][k][0] for k in range(2))
        assert a.flip(8)*a*norms[j]==n0
    gauge=tuple(tuple(alpha[i] if i==j else ZERO for j in range(4)) for i in range(4))
    assert mm(oldV,gauge)==V
    barV=conjugate(V);barL=conjugate(L);barH=conjugate(H);barK=conjugate(K)
    assert L!=barL and mm(L,barV)!=barV
    assert rank(mm(R,barV))==4
    assert mm(barH,barV)==mm(barV,barK)
    assert mm(conjugate(D),barV)==eye(4)

    dependencies=set(previous['source_sha256'])|{
        'research/voevodsky/checkers/check_spinor_matter_link_adapter.py',
        'research/voevodsky/checkers/check_spinor_quantum_leads.py',
        'research/scattering/seed-composition/check_native_endpoint_face_lines.py'}
    return {
        'schema':'marici.scattering.native-endpoint-face-lines.v1',
        'status':'native_face_line_metric_and_kinetic_adapter_exact_conjugation_changes_selected_source',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'adapter':{'raw_native_dimension':8,'selected_face_lines':4,'excluded_polarization_rank':4,
                   'coherent_doublet_rank':2,'V':record(V),'decoder_D':record(D),
                   'line_metric':'n0*I4, n0=(3+sqrt(3))/6','weighted_metric':record(scale(n0,eye(4))),
                   'rooted_gauge':'w0=P0 e0; wi=Pi w0/Q(i,0)',
                   'owner_column_frame_adapter':record(gauge),'D_V_equals_I':True,'V_D_equals_L':True,
                   'lossless_split':'x -> (D x,(I-L)x)','decoder':'V*line_record + residual_record',
                   'combined_norm_preserved':True},
        'operator_transport':{'native_defect':'H=(I-L)+2(I-N)',
                              'H_V_equals_V_K':True,'endpoint_K':'I-Q',
                              'transported_native_L':'I4','transported_native_G_and_N':'(I4+Q)/2',
                              'endpoint_kinetic_spectrum':'0 (rank two), 2 (rank two)',
                              'excluded_polarization_energy':'H*(I-L)=3*(I-L)',
                              'native_144_not_replaced_by_reduced_coordinate_support_count':True},
        'wilson_loops':loops,
        'conjugation_gate':{'bare_raw_conjugation_preserves_im_L':False,
                            'rank_of_conjugate_lines_outside_original_L':4,
                            'conjugate_partner':'bar(H)*bar(V)=bar(V)*bar(K)',
                            'fixed_face_diagonal_gauge_maps_bar_K_to_K':False,
                            'reason':'fixed labelled triangle loop products are diagonal-gauge invariant; +/-i reverse under conjugation',
                            'additional_face_permutation_or_antiunitary_frame_maps_excluded':False},
        'boundary':{'signed_charge_or_sector_swap_derived_by_adapter':False,'physical_endpoint_interaction_admitted':False,
                    'global_doublet_selection_derived':False,'shared_sources_or_receipts_rewritten':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Pull the actual endpoint charging diagonals back through V and test closure of the native rank-two coherent return, retaining both rank-two line-mismatch and rank-four polarization records. Determine whether the charged interaction preserves that doublet or mixes it with noncoherent directions.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale native/endpoint face-line receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact weighted native-to-endpoint face-line adapter transports metric, L/G/N and kinetic operator.')
    print('PASS: four excluded polarization directions retained; bare conjugation changes the selected source and loop phases.')
    print('Boundary: coordinate/sector bridge only; signed charge, physical interaction and preparation remain inputs.')


if __name__=='__main__':main()
