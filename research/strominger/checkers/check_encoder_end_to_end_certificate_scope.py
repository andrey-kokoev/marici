"""Source identities and exact hostiles for end-to-end certificate sufficiency.

No candidate word is accepted here. The uniform bounds are the written theorem
in the companion packet, conditional on an actual word-distance certificate.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_witnessed_interface_compiler import ROOT, BASE, rat, mm, tr, inverse, eye, minus, scale, rank, enc


def zero(A):return all(not x for row in A for x in row)


def main():
    files={k:BASE/'results'/v for k,v in {
        'source':'neutron-seam-control-transport.json',
        'memory':'neutron-comparison-memory.json',
        'scattering':'neutron-autonomous-rim-scattering.json'}.items()}
    raw={k:p.read_bytes() for k,p in files.items()}
    data={k:json.loads(v) for k,v in raw.items()}
    assert all(v['status']=='passed' for v in data.values())
    M=rat(data['source']['metric'])
    B=rat(data['memory']['residual_incidence'])
    Gamma=rat(data['memory']['memory_metric'])
    S=mm(mm(mm(inverse(M),tr(B)),Gamma),B)
    A0=scale(F(1,4),rat(data['source']['native_energy']))
    E=rat(data['scattering']['exact_bright_basis'])
    g=mm(mm(tr(E),M),E)
    L=mm(mm(inverse(g),tr(E)),M)
    Kb=mm(mm(L,S),E)
    assert rank(E)==5 and mm(L,E)==eye(5)
    assert zero(mm(A0,E)) and mm(S,E)==mm(E,Kb)
    assert mm(tr(Kb),g)==mm(g,Kb)
    contacts=[row[:2] for row in E]
    assert mm(mm(tr(contacts),M),contacts)==scale(F(3),eye(2))
    # Scalar proximity alone cannot certify a reader. Exact isometric encoder
    # e1->e2 has zero encoding error; retaining the old e1 reader erases it.
    J=[[F(0)],[F(1)]]
    old_reader=[[F(1),F(0)]]
    transported_reader=tr(J)
    assert mm(tr(J),J)==eye(1)
    assert mm(old_reader,J)==[[F(0)]]
    assert mm(transported_reader,J)==[[F(1)]]
    # An exact encoder can also fail storage: two source modes with K=0,
    # encoded into target coordinates 0 and 2, target H=diag(0,0,1).
    # At declared parameter pi, exact target evolution is diag(1,1,-1).
    J2=[[F(1),F(0)],[F(0),F(0)],[F(0),F(1)]]
    H=[[F(0)]*3 for _ in range(3)]
    H[2][2]=F(1)
    evolution=eye(3)
    evolution[2][2]=F(-1)
    x=[[F(1)],[F(1)]]
    assert mm(tr(J2),J2)==eye(2)
    defect=mm(H,J2)
    assert not zero(defect)
    recovered=mm(mm(mm(tr(J2),evolution),J2),x)
    assert recovered==[[F(1)],[F(-1)]]
    assert mm(tr(x),recovered)==[[F(0)]]
    # Normalize both vectors by sqrt(2): ideal and recovered states are
    # orthogonal. Encoding error zero did not bound storage fidelity loss.
    hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(raw[k]).hexdigest() for k,p in files.items()}
    own=Path(__file__).resolve()
    hashes[own.relative_to(ROOT).as_posix()]=hashlib.sha256(own.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    result={'status':'pass','actual_bright_dimension':5,
        'actual_native_energy_zero_on_bright':True,
        'actual_bright_generator_invariant_and_metric_self_adjoint':True,
        'actual_contact_columns_have_gram_3I':True,
        'reader_hostile':{'encoding_error':0,'old_reader_amplitude':0,'transported_reader_amplitude':1},
        'storage_hostile':{'encoding_error':0,'normalized_recovered_state_fidelity':0,'intertwining_defect':enc(defect)},
        'conditional_bounds':{
            'encoded_free_hold_state_error':'<= delta uniformly in storage parameter',
            'decoded_free_hold_state_error':'<= 2 delta uniformly in storage parameter',
            'normalized_transported_contact_amplitude_error':'<= 2 delta uniformly in storage parameter'},
        'scope':'Tests exact source prerequisites and two counterexamples to matrix-error-only certification. Bounds require permitted metric-unitary word V, ready-input proximity to J, actual ideal intertwining and transported contacts. No compiler word, coupled-lead execution, or physical implementation certified.',
        'source_hashes':hashes}
    (BASE/'results/encoder-end-to-end-certificate-scope.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','matrix_error_only_certificate':'falsified_by_both_hostiles','actual_bright_prerequisites':'pass'}))


if __name__=='__main__':main()
