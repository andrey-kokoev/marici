"""Read-only recovery of existing intrinsic five-cell maps and attachment ambiguity."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/five-cell-attachment-bridge.v1.json'
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
# Imports expose exact algebra only; never call owner main(), which writes stores.
from check_diagonal_spin_networks import A,S5,ZERO,ONE,mm,adj,rank,add,scale,decode,recover,smul,sadj,sparse
from check_pentachoron_cycle_transport import eye,power


def load(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def digest(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def dense(entries,n,m):return tuple(tuple(entries.get((i,j),ZERO) for j in range(m)) for i in range(n))
def record(M):return [[x.record() for x in row] for row in M]


def audit():
    receipt_path='research/strominger/results/diagonal-spin-networks/verification.json'
    receipt=load(receipt_path);assert receipt['status']=='passed'
    dependencies={receipt_path,'docs/arrow-assembly.md','research/strominger/diagonal-spin-networks.md',
        'research/strominger/retained-coefficient-network.md',
        'research/scattering/seed-composition/check_five_cell_attachment_bridge.py',
        'research/matter/element-isotope-catalog.json'}
    binding=[]
    for p,h in {**receipt['source_hashes'],**receipt['network_packets']}.items():
        assert digest(p)==h,p
        dependencies.add(p);binding.append({'path':p,'matches_owner_hash':True})
    # Also check direct hashes of prerequisite receipts, not just the outer one.
    for p in receipt['source_hashes']:
        if p.endswith('.json'):
            prior=load(p)
            for path,h in prior.get('source_hashes',{}).items():
                assert digest(path)==h,path
                dependencies.add(path)
    rows=[]
    for chirality in (1,-1):
        prefix=f'research/strominger/results/diagonal-spin-networks/chirality-{chirality}-'
        packets={name:load(prefix+name+'.json') for name in ('constant','complementary','low')}
        P={name:tuple(tuple(decode(x) for x in row) for row in packet['logical_projector']) for name,packet in packets.items()}
        C=P['constant'];B=P['complementary'];Q=P['low']
        assert add(C,B)==Q and mm(C,B)==tuple(tuple(ZERO for _ in range(10)) for _ in range(10))
        Jentries=recover(packets['constant']['encoding']);J=dense(Jentries,40,10)
        assert mm(adj(J),J)==eye(10)
        face_order=[tuple(k) for k in packets['constant']['face_order']]
        # Geometric cell 4 is source attachment BCDE; source pole A is
        # geometric vertex E (4). Do not identify source A with geometric A.
        R=tuple(tuple(ONE if j==8+i else ZERO for j in range(10)) for i in range(2))
        Ws={name:tuple(tuple(S5*row[8+j] for j in range(2)) for row in P[name]) for name in ('constant','complementary')}
        for name,W in Ws.items():
            assert mm(adj(W),W)==eye(2) and mm(W,adj(W))==P[name]
            assert mm(R,W)==scale(S5.inverse(),eye(2))
            packet=packets[name]
            assert packet['measures']['return_rank']==2 and packet['measures']['transfers']==3120
            N=recover(packet['operators']['N']);L=recover(packet['operators']['L'])
            assert N==smul(smul(Jentries,sparse(P[name])),sadj(Jentries))
            assert smul(N,L)==N and smul(N,N)==N
        Wc=Ws['constant'];Wb=Ws['complementary']
        assert mm(adj(Wc),Wb)==tuple(tuple(ZERO for _ in range(2)) for _ in range(2))
        difference=add(Wc,scale(A(-1),Wb))
        assert rank(difference)==2 and mm(R,difference)==tuple(tuple(ZERO for _ in range(2)) for _ in range(2))
        assert mm(adj(difference),difference)==scale(A(2),eye(2))
        face_rows=[2*k+i for k,(c,d) in enumerate(face_order) if c==4 for i in range(2)]
        assert len(face_rows)==8
        face_c=mm(J,Wc);face_b=mm(J,Wb)
        assert tuple(face_c[i] for i in face_rows)==tuple(face_b[i] for i in face_rows)
        # Reconstruct intrinsic local attachment encoding; four Pauli projectors
        # sum to 2I, so the local eight-coordinate map is a rank-two isometry.
        local=scale(S5,tuple(face_c[i] for i in face_rows))
        assert mm(adj(local),local)==eye(2)
        cases=[case for case in receipt['cases'] if case['chirality']==chirality]
        assert len(cases)==5
        for case in cases:
            assert case['network_measures']['constant']['transfers']==3120
            for action in case['actions']:
                T=tuple(tuple(decode(x) for x in row) for row in action['logical_transport'])
                assert mm(adj(T),T)==eye(10)
                for name,W in Ws.items():
                    assert mm(T,P[name])==mm(P[name],T)
                    U=mm(mm(adj(W),T),W)
                    assert mm(T,W)==mm(W,U) and mm(adj(U),U)==eye(2)
                if len(action['cycle'])==6:
                    assert power(T,5)==scale(A(-1),eye(10))
        rows.append({'chirality':chirality,'logical_cell_coordinates':10,'raw_face_coordinates':40,
                     'local_attachment_coordinates':8,'local_logical_rank':2,
                     'doublet_ranks':[rank(C),rank(B)],'orthogonal_global_doublets':True,
                     'attachment_restriction':'R*W_constant=R*W_complementary=I/sqrt(5)',
                     'identical_attachment_face_encoding':True,
                     'difference_rank':rank(difference),'difference_attachment_zero':True,
                     'difference_gram':'2I','constant_isometry':record(Wc),'complementary_isometry':record(Wb),
                     'local_face_encoding':record(local),
                     'source_bound_case_transports_checked':len(cases),
                     'protocol_counts':[3120,3120],'count_selects_doublet':False})
    atlas=load('research/matter/element-isotope-catalog.json')
    electron=next(c for c in atlas['constituents'] if c['id']=='electron-candidate')
    assert electron['claims'][1]['status']=='unconstructed'
    return {
        'schema':'marici.scattering.five-cell-attachment-bridge.v1',
        'status':'existing_conditional_five_cell_intertwiners_recovered_local_attachment_does_not_choose_global_doublet',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'owner_hash_checks':binding,'bridges':rows,
        'source_label_binding':{'source_A':'geometric_E (index 4)','source_BCDE':'geometric_ABCD attachment facet (cell 4)'},
        'correspondence_correction':{'atlas_unconstructed_gate':'Compatible physical five-cell spinor and energy transport',
                                    'conditional_mathematical_maps_exist':True,
                                    'old_fixed_cell_obstruction_still_valid':True,
                                    'absence_of_all_five_cell_maps_claimed':False,
                                    'remaining_selection':'Two orthogonal global doublets share the same local attachment readout and count; selecting one remains explicit.',
                                    'full_physical_gate_closed':False},
        'boundary':{'native_144_replaced_by_3120':False,'central_lift_sign_is_physical_period':False,
                    'intrinsic_attachment_frame_identified_with_old_native_frame_without_adapter':False,
                    'atlas_or_shared_store_rewritten':False,'physical_charge_mass_or_species_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Compare the reconstructed intrinsic attachment face encoding with the native tetrahedral spinor fixture using an explicit face/Pauli frame adapter; test metric and protocol intertwining before interpreting seed inversion as conjugation.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale five-cell attachment receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: existing intrinsic five-cell intertwiners recovered in both chiralities; owner hashes and ten cases checked.')
    print('PASS: orthogonal rank-two global doublets have identical local attachment readouts and identical protocol counts.')
    print('Boundary: conditional transport exists; native-frame adapter, doublet selection and physical gate remain open.')


if __name__=='__main__':main()
