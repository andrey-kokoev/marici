"""Exact spanning certificate for source-relative exchange uniqueness.

Given C, its positive metric and a linear isometry that fixes agreement,
implements zero readable output for an empty bank, and fixes ker(C), the
existing exchange is the only map. Analytic inference of the empty-bank
output from those conditions is recorded in the accompanying packet.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
from check_four_packet_record_feedback import (
    basis,readout,lift,exchange,sub,add,mm,transpose,matrix_of,rank,
)
ROOT=Path(__file__).resolve().parents[1]


def main():
    Z4=(F(0),)*4;Z16=(F(0),)*16
    C=tuple(zip(*(readout(e) for e in basis(16))))
    assert mm(C,transpose(C))==tuple(basis(4))
    kernel=[sub(e,lift(readout(e))) for e in basis(16)]
    assert rank(kernel)==12 and all(readout(k)==Z4 for k in kernel)
    agreed=[x+lift(x) for x in basis(4)]
    empty=[x+Z16 for x in basis(4)]
    unread=[Z4+k for k in kernel]
    # These 24 source vectors span all 20 coordinates (kernel list redundant).
    inputs=agreed+empty+unread
    targets=agreed+[Z4+lift(x) for x in basis(4)]+unread
    assert rank(inputs)==20
    E=matrix_of(lambda v:sum(exchange(v[:4],v[4:]),()),20)
    assert mm(transpose(E),E)==tuple(basis(20))
    for v,w in zip(inputs,targets):
        assert sum(exchange(v[:4],v[4:]),())==w
    # Select a nonredundant domain basis as a directly inspectable certificate.
    selected=[];selected_targets=[]
    for v,w in zip(inputs,targets):
        if rank(selected+[v])>len(selected):
            selected.append(v);selected_targets.append(w)
    assert len(selected)==20
    assert mm(E,transpose(tuple(selected)))==transpose(tuple(selected_targets))
    # Explicit readable-mode basis: (x,a,k) -> (a,x,k).
    for x in basis(4):
        for a in basis(4):
            for k in kernel:
                t=add(lift(a),k)
                assert exchange(x,t)==(a,add(lift(x),k))
    result=dict(schema='marici.nima.record-exchange-uniqueness.v1',status='pass',
        assumptions=['fixed coisometry C and positive Euclidean metrics','linearity and isometry',
                     'agreement states (x,C^T x) are fixed',
                     'empty bank gives zero outgoing carrier in the exchanged port',
                     'unread bank states (0,k), Ck=0, are fixed'],
        selected_map='E(x,t)=(Ct,C^T x+(I-C^T C)t)',
        source_constraint_rank=20,full_dimension=20,kernel_dimension=12,
        inference='Agreement and isometry force the empty-bank record output to be C^T x once its carrier output is zero. The resulting specified images span the full space, proving uniqueness among linear maps.',
        conclusion='The existing exchange stage is unique under these inherited port conditions. Its rotations, adapter, metric and physical meaning are not selected by this theorem.',
        domain_basis=[[str(x) for x in v] for v in selected],
        image_basis=[[str(x) for x in v] for v in selected_targets],
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_record_feedback.py',
            'comparison-update-dynamics-and-energy-normalization.md',
            'four-packet-record-feedback.md','checkers/check_record_exchange_uniqueness.py')})
    (ROOT/'results/record-exchange-uniqueness.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('domain_basis','image_basis','source_sha256')},indent=2))


if __name__=='__main__':main()
