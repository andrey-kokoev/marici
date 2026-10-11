"""Exact Clifford encoder/decoder and retained-syndrome history recovery.

Synthesizes from the prior component stabilizers, not a new chosen code. Fault
model is one physical Pauli event during encoded storage with ideal controls.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import importlib.util
import json
from check_coupled_six_piece_belt import R
from check_encoded_history_memory import ZERO,ONE,add,mul,scale,inner,pauli

BASE=Path(__file__).resolve().parents[1]


def raw(row):
    return [sum(row[i]<<i for i in range(5)),sum(row[5+i]<<i for i in range(5)),sum(row[i]*row[5+i] for i in range(5))%4]


def conjugate(p,g):
    x,z,phase=p
    kind,i,*extra=g
    xi,zi=(x>>i)&1,(z>>i)&1
    if kind=='H':
        phase+=2*xi*zi
        if xi!=zi: x^=1<<i; z^=1<<i
    elif kind=='S':
        phase+=xi
        if xi: z^=1<<i
    elif kind=='X': phase+=2*zi
    elif kind=='CX':
        j=extra[0]
        if xi: x^=1<<j
        if (z>>j)&1: z^=1<<i
    elif kind=='SWAP':
        j=extra[0]
        if xi!=((x>>j)&1): x^=(1<<i)|(1<<j)
        if zi!=((z>>j)&1): z^=(1<<i)|(1<<j)
    else: raise AssertionError(kind)
    return [x,z,phase%4]


def inverse(circuit):
    result=[]
    for gate in reversed(circuit): result.extend([gate]*3 if gate[0]=='S' else [gate])
    return result


def apply(circuit,state):
    v=list(state)
    for kind,i,*extra in circuit:
        out=[ZERO]*32
        for b,a in enumerate(v):
            if kind=='H':
                low=b&~(1<<i)
                out[low]=add(out[low],scale(R(0,F(1,2)),a))
                out[low|(1<<i)]=add(out[low|(1<<i)],scale(R(0,F((-1)**((b>>i)&1),2)),a))
            elif kind=='S': out[b]=mul((F(0),F(1)),a) if b&(1<<i) else a
            elif kind=='X': out[b^(1<<i)]=a
            elif kind=='CX': out[b^(1<<extra[0]) if b&(1<<i) else b]=a
            elif kind=='SWAP':
                j=extra[0]
                dest=b^((1<<i)|(1<<j)) if ((b>>i)&1)!=((b>>j)&1) else b
                out[dest]=a
            else: raise AssertionError(kind)
        v=out
    return v


def main():
    source=BASE.parent/'kitaev/checkers/check_s3_five_rail_code_freeze.py'
    spec=importlib.util.spec_from_file_location('owning_five_rail_code',source)
    owner=importlib.util.module_from_spec(spec); spec.loader.exec_module(owner)
    cert=owner.certify('five_qubit_perfect_code',2,owner.QUBIT)
    rows=[raw(row) for row in owner.QUBIT+[cert['logical_z']]]
    lx=raw(cert['logical_x'])
    reduction=[]
    def gate(g):
        nonlocal rows,lx
        reduction.append(g)
        rows=[conjugate(p,g) for p in rows]
        lx=conjugate(lx,g)
    for i in range(5):
        pivot=next(j for j in range(i,5) if (rows[i][0]|rows[i][1])&(1<<j))
        if pivot!=i: gate(('SWAP',i,pivot))
        for j in range(i,5):
            x,z,_=rows[i]
            if not (x|z)&(1<<j): continue
            if x&(1<<j) and z&(1<<j): gate(('S',j))
            elif z&(1<<j): gate(('H',j))
        for j in range(i+1,5):
            if rows[i][0]&(1<<j): gate(('CX',i,j))
        gate(('H',i))
        assert rows[i][0]==0 and rows[i][1]==1<<i
        if rows[i][2]==2: gate(('X',i))
        assert rows[i]==[0,1<<i,0]
        # Change the generator basis, not the physical state or gate list.
        for j in range(i+1,5):
            assert not rows[j][0]&(1<<i)
            if rows[j][1]&(1<<i): rows[j][1]^=1<<i
    assert lx[0]==1<<4
    encoder=[('S',4)]*lx[2]+inverse(reduction)
    decoder=inverse(encoder)
    basis=[]
    for bit in (0,1):
        v=[ZERO]*32; v[bit<<4]=ONE
        basis.append(apply(encoder,v))
    assert inner(basis[0],basis[0])==inner(basis[1],basis[1])==ONE
    assert inner(basis[0],basis[1])==ZERO
    assert pauli(cert['logical_x'],basis[0])==basis[1]
    for v in basis: assert all(pauli(s,v)==v for s in owner.QUBIT)
    for j in range(32):
        v=[ZERO]*32; v[j]=ONE
        assert apply(decoder,apply(encoder,v))==v
    errors=[(0,)*10]+owner.single_rail_errors(2)
    table=[]
    for error in errors:
        transformed=raw(error)
        for g in decoder: transformed=conjugate(transformed,g)
        x,z,phase=transformed
        syndrome=x&15
        logical_x,logical_z=(x>>4)&1,(z>>4)&1
        correction=[0]*10
        correction[4],correction[9]=logical_x,logical_z
        common_phase=None
        for bit in (0,1):
            noisy=pauli(error,basis[bit])
            decoded=apply(decoder,noisy)
            recovered=pauli(correction,decoded)
            amplitude=recovered[syndrome|(bit<<4)]
            assert inner([amplitude],[amplitude])==ONE
            assert all(a==ZERO for j,a in enumerate(recovered) if j!=(syndrome|(bit<<4)))
            if common_phase is None: common_phase=amplitude
            else: assert amplitude==common_phase
        table.append({'physical_error':list(error),'decoded_syndrome':syndrome,
                      'controlled_logical_x':logical_x,'controlled_logical_z':logical_z})
    assert len({row['decoded_syndrome'] for row in table})==16
    previous_path=BASE/'results/encoded_history_memory.json'
    previous_raw=previous_path.read_bytes()
    previous=json.loads(previous_raw)
    assert previous['source_code_sha256']==sha256(source.read_bytes()).hexdigest()
    report={'status':'history_encoder_decoder_and_recovery_controls_checked',
            'component_encoder_gates':encoder,'component_decoder_gates':decoder,
            'component_encoder_gate_count':len(encoder),'five_block_encoder_gate_count':5*len(encoder),
            'five_block_decoder_gate_count':5*len(decoder),
            'encoder_input':'Five logical history bits, each with four ready-zero data ancillas; 22 labels occupy a subspace of 32 logical states.',
            'exact_gate_field':'Q(sqrt(2),i), with rational coefficient arithmetic',
            'full_component_inverse_basis_checks':32,
            'component_error_and_logical_input_cases':32,
            'decoder_retains_syndrome_in_four_ancillas':True,
            'recovery_table':table,
            'recovery_control':'Decode; coherently apply the table-selected logical Pauli, retaining four syndrome bits per component. Error-dependent common phases remain in the syndrome amplitude.',
            'noise_interface':'During encoded storage, at most one physical data qubit experiences an error in span{I,X,Y,Z}; encoding, decoding and correction controls are ideal for this test.',
            'arbitrary_single_qubit_channel_corrected':True,
            'not_claimed':['This bare Clifford decoder is not fault-tolerant against faults during decoding; it is not the prior verified-Shor recovery gadget.',
                'A finite-time general system-bath Hamiltonian can generate multiple-qubit errors; the one-event channel is an explicit noise assumption, not a derived bath.',
                'The logical history-label phase fault remains a zero-syndrome logical operation.',
                'Encoded modular history addressing, microscopic noise couplings, work/reset accounting, local autonomous control and lifetimes remain open.'],
            'source_code_sha256':sha256(source.read_bytes()).hexdigest(),
            'previous_history_code_receipt_sha256':sha256(previous_raw).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/history_code_circuit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('component_encoder_gates','component_decoder_gates','recovery_table')},indent=2))


if __name__=='__main__': main()
