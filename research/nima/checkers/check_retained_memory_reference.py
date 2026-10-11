"""Trace reference creation by the existing conservative exchange itself.

No new Boolean control or +/-J reference pair is introduced. Readable past
carrier data is retained in the existing bank and returns after mixing.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT,E2,tensor,rotate,MAX_DEPTH
from check_four_packet_record_feedback import (
    readout,lift,left_rotate,cycle,inverse_cycle,budget,add,sub,basis,
)
ROOT=Path(__file__).resolve().parents[1]
Z4=(F(0),)*4;Z16=(F(0),)*16


def compare_step(x,t):
    active=rotate(x);bank=left_rotate(t);reference=readout(bank)
    delta=sub(reference,active)
    out=cycle(x,t)
    # This is the actual old exchange written as a mismatch response.
    assert out==(add(active,delta),sub(bank,lift(delta)))
    assert readout(out[1])==active
    assert readout(left_rotate(out[1]))==readout(t)
    assert inverse_cycle(*out)==(x,t)
    assert budget(*out)==budget(x,t)
    if delta==Z4:assert out==(active,bank)
    return out,delta


def main():
    for x in basis(4):
        state=(x,Z16);history=[];carriers=[x]
        for _ in range(MAX_DEPTH):
            history.append(state);state,delta=compare_step(*state);carriers.append(state[0])
        assert carriers==[x,Z4,Z4,rotate(x)]
        assert state[1]==Z16
        for old in reversed(history):
            state=inverse_cycle(*state);assert state==old
    # The two reference-lineage equations are linear and checked on a full basis.
    for v in basis(20):
        x,t=v[:4],v[4:]
        first,_=compare_step(x,t)
        second,_=compare_step(*first)
        assert readout(first[1])==rotate(x)
        assert readout(left_rotate(second[1]))==rotate(x)
    reports=[]
    for name,t in (('empty_bank',Z16),('ordinary_bank',tensor(UNIT,UNIT)),
                   ('twisted_bank',tensor(E2,E2))):
        state=(UNIT,t);history=[];deltas=[];outputs=[];norm=budget(*state)
        for _ in range(MAX_DEPTH):
            history.append(state);state,d=compare_step(*state)
            deltas.append([str(v) for v in d]);outputs.append([str(v) for v in state[0]])
        for parent in reversed(history):
            state=inverse_cycle(*state);assert state==parent
        reports.append(dict(preparation=name,initial_budget=str(norm),mismatches=deltas,
                            carriers=outputs,retained_parents=len(history),reverse_recovery=True))
    assert reports[0]['mismatches'][1]==['0']*4
    result=dict(schema='marici.nima.retained-memory-reference.v1',status='pass',
        existing_law='incoming x_bar=Rx, t_bar=Lt; delta=C t_bar-x_bar; x_next=x_bar+delta; t_next=t_bar-C^T delta',
        lineage=['C t_(n+1)=R x_n','C L t_(n+2)=R x_n'],
        fixtures=reports,
        disposition='The existing bank creates and retains the comparison reference from a previous carrier value. With an initially empty bank, nonzero reference data comes from the carrier, not from an independently inserted reference pair. It is not the certified target of the current witness.',
        limits='This recovers and checks an existing memory-lift mechanism. It does not select the initial carrier, port, metric or mixer, generate the tetrahedral bank from nothing, or remove the fixed-reference interpretation gates of that adapter. Zero bank is a declared initialization; no physical energy or time scale inferred.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_record_feedback.py','comparison-update-dynamics-and-energy-normalization.md',
            'four-packet-record-feedback.md','checkers/check_retained_memory_reference.py')})
    (ROOT/'results/retained-memory-reference.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
